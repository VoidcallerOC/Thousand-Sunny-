#!/usr/bin/env python3
"""Thousand Sunny — intelligent card-crop detection.

Card photos in the display-case gallery come in two very different forms:

    RAW      a loose trading card that fills most of the photograph.
    SLAB     a graded card (PSA / BGS / other) encapsulated in a plastic case
             with a printed grading label above it — the card is only part of
             the photograph.

The gallery's visual subject is always *the trading card*, never the slab, the
grading label, or the surrounding plastic.  This script inspects the actual
source pixels of every gallery image and produces a per-image crop rectangle so
the front-end can display the card and only the card.

Pipeline (see the phase comments below):

  1. INVENTORY      native width/height and aspect ratio of each source image.
  2. CLASSIFY       RAW vs PSA / BGS / OTHER_SLAB / UNKNOWN, from pixels.  A
                    filename/caption is used only as a tie-breaking hint.
  3. LOCATE CARD    RAW  -> trim any uniform border, keep the whole card.
                    SLAB -> drop the label band, take the dominant textured /
                    colourful region (the card) inside the plastic.
  4. CONFIDENCE     scored honestly; low-confidence images are NOT shipped with a
                    guessed crop — they fall back to a hand-verified manual
                    override (scripts/card-crop-overrides.json).
  5. EMIT           assets/data/card-crops.json  (inventory + crop metadata)
                    assets/js/card-crops.js       (window.CARD_CROPS for the page)

The crop is expressed in source pixels as {x, y, w, h} plus normalized
{left, top, right, bottom}.  The front-end keeps the card's own aspect ratio
(crop.w / crop.h) — cards are never stretched, squashed, or forced into a fixed
rectangle.

Usage:
    python3 scripts/detect-card-crops.py            # detect + write metadata
    python3 scripts/detect-card-crops.py --check     # detect + print, write nothing
"""
import argparse
import json
import os
import re
import sys

try:
    import cv2
    import numpy as np
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "This preprocessing script needs numpy + opencv:\n"
        "    pip install numpy opencv-python-headless\n"
    )
    raise

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_JS = os.path.join(ROOT, "assets", "js", "main.js")
OVERRIDES = os.path.join(ROOT, "scripts", "card-crop-overrides.json")
OUT_JSON = os.path.join(ROOT, "assets", "data", "card-crops.json")
OUT_JS = os.path.join(ROOT, "assets", "js", "card-crops.js")

TARGET_W = 600          # working resolution for analysis
CARD_AR = 0.715         # standard 2.5 x 3.5 trading-card ratio
CONF_THRESHOLD = 0.65   # below this, an image requires a manual override


# --------------------------------------------------------------------------- #
# low-level image maps
# --------------------------------------------------------------------------- #
def _prep(bgr):
    h, w = bgr.shape[:2]
    scale = TARGET_W / w
    small = cv2.resize(bgr, (TARGET_W, int(round(h * scale))),
                       interpolation=cv2.INTER_AREA)
    return small, scale


def _maps(small):
    """Return (busy, S, V, tex).

    busy = per-pixel likelihood of 'card content': high where the image is
    textured OR colourful.  A grading label is bright and flat (low busy); slab
    plastic is flat (low busy); card art — including monochrome manga art — is
    textured, so it stays high.
    """
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    S = hsv[:, :, 1].astype(np.float32) / 255.0
    V = hsv[:, :, 2].astype(np.float32) / 255.0
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY).astype(np.float32)
    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    grad = np.sqrt(gx * gx + gy * gy)
    tex = cv2.blur(grad, (11, 11))
    tex = np.clip(tex / (np.percentile(tex, 96) + 1e-6), 0, 1)
    satb = cv2.blur(S, (11, 11))
    busy = np.maximum(tex * 0.95, satb)
    return busy, S, V, tex


def _label_band(V, S):
    """End row of a genuine grading label anchored at the very top (0 if none).

    A real label is bright, low-saturation and wide, starts within the top 10%
    of the image and is closed at the FIRST sustained plastic gap so that a
    card's own bright top edge cannot extend it.  Holographic glare on a raw
    card fails these tests and is not treated as a label.
    """
    h, w = V.shape
    white = ((V > 0.58) & (S < 0.32)).astype(np.float32)
    rowwhite = white.mean(axis=1)
    if rowwhite[:max(1, int(h * 0.10))].max() < 0.45:
        return 0, 0.0
    end, run_low, started = -1, 0, False
    gap_break = max(4, int(h * 0.015))
    for y in range(int(h * 0.45)):
        if rowwhite[y] > 0.45:
            end, run_low, started = y, 0, True
        elif started:
            run_low += 1
            if run_low > gap_break:
                break
    if end < int(h * 0.03):
        return 0, 0.0
    cov = float((rowwhite[:end + 1] > 0.45).mean())
    return end, cov


def _run_edges(prof, frac=0.34):
    """First/last index where a profile rises above frac * (mean of its top 40%)."""
    n = len(prof)
    ref = float(np.mean(np.sort(prof)[-max(3, int(n * 0.4)):]))
    thr = ref * frac
    idx = np.where(prof > thr)[0]
    if len(idx) == 0:
        return 0, n - 1
    return int(idx[0]), int(idx[-1])


def _trim_uniform(busy, frac=0.16):
    """RAW bounds: trim near-uniform (low-busy) borders, keep the whole card."""
    col = cv2.blur(busy.mean(axis=0).reshape(1, -1), (13, 1)).ravel()
    row = cv2.blur(busy.mean(axis=1).reshape(1, -1), (13, 1)).ravel()
    x0, x1 = _run_edges(col, frac)
    y0, y1 = _run_edges(row, frac)
    return x0, y0, x1, y1


def _slab_card(busy, label_end):
    """SLAB bounds: card bbox inside the plastic, below the label band."""
    h, w = busy.shape
    m = (busy > 0.30).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((17, 17), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    if label_end > 0:
        m[:label_end + 1, :] = 0
    n, lbl, st, ce = cv2.connectedComponentsWithStats(m, connectivity=8)
    best, best_score = None, -1
    for i in range(1, n):
        x, y, ww, hh, area = st[i]
        if area < 0.04 * h * w:
            continue
        ar = ww / max(hh, 1)
        ar_score = np.exp(-((ar - CARD_AR) / 0.4) ** 2)
        fill = area / (ww * hh + 1e-6)
        score = area * (0.4 + 0.6 * ar_score) * (0.5 + 0.5 * fill)
        if score > best_score:
            best_score, best = score, (x, y, ww, hh, fill)
    if best is None:
        return 0, label_end, w - 1, h - 1, 0.0
    x, y, ww, hh, fill = best
    sub = busy[y:y + hh, x:x + ww]
    cx0, cx1 = _run_edges(sub.mean(axis=0), 0.28)
    ry0, ry1 = _run_edges(sub.mean(axis=1), 0.28)
    return x + cx0, y + ry0, x + cx1, y + ry1, float(fill)


def _slab_subtype(small, label_end, hint):
    """PSA / BGS / OTHER_SLAB from the label band, hint as a tie-breaker."""
    h = small.shape[0]
    band = small[:max(label_end, int(h * 0.12)), :]
    hsv = cv2.cvtColor(band, cv2.COLOR_BGR2HSV)
    Hh, Ss, Vv = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
    red = (((Hh < 10) | (Hh > 170)) & (Ss > 90) & (Vv > 80)).mean()
    dark = (Vv < 60).mean()          # Beckett "B" logo / dark header
    hint = (hint or "").lower()
    hint_psa = "psa" in hint
    hint_bgs = any(k in hint for k in ("bgs", "beckett", "pristine"))
    if hint_bgs and not hint_psa:
        return "BGS", {"red": round(float(red), 3), "dark": round(float(dark), 3)}
    if hint_psa:
        return "PSA", {"red": round(float(red), 3), "dark": round(float(dark), 3)}
    if red > 0.05:
        return "PSA", {"red": round(float(red), 3), "dark": round(float(dark), 3)}
    if dark > 0.12:
        return "BGS", {"red": round(float(red), 3), "dark": round(float(dark), 3)}
    return "OTHER_SLAB", {"red": round(float(red), 3), "dark": round(float(dark), 3)}


# --------------------------------------------------------------------------- #
# main detector
# --------------------------------------------------------------------------- #
def detect(path, hint=None):
    bgr = cv2.imread(path)
    if bgr is None:
        raise FileNotFoundError(path)
    H, W = bgr.shape[:2]
    small, scale = _prep(bgr)
    sh, sw = small.shape[:2]
    busy, S, V, tex = _maps(small)
    label_end, label_cov = _label_band(V, S)
    imar = W / H

    tx0, ty0, tx1, ty1 = _trim_uniform(busy)               # raw candidate
    sx0, sy0, sx1, sy1, fill = _slab_card(busy, label_end)  # slab candidate

    lm, rm, tm = sx0 / sw, (sw - 1 - sx1) / sw, sy0 / sh
    side_plastic = min(lm, rm)
    raw_cov = ((tx1 - tx0 + 1) * (ty1 - ty0 + 1)) / (sw * sh)

    # ---- PHASE 2: classify RAW vs SLAB from pixels ----------------------- #
    # Aspect ratio is the primary pixel signal (a slab is markedly taller than
    # the card it holds); a card that fills a ~0.71 frame is raw even under holo
    # glare that can mimic a label.  Label + plastic margins confirm.
    strong_label = label_end > int(sh * 0.03) and label_cov > 0.55
    looks_raw = imar >= 0.66 and raw_cov > 0.82
    looks_slab = imar < 0.63 or strong_label or (side_plastic > 0.06 and tm > 0.10)
    if looks_raw and imar >= 0.63:
        kind = "RAW"
    elif looks_slab:
        kind = "SLAB"
    else:
        kind = "RAW" if raw_cov > 0.85 else "UNKNOWN"

    if kind == "SLAB":
        x0, y0, x1, y1 = sx0, sy0, sx1, sy1
        subtype, sub_sig = _slab_subtype(small, label_end, hint)
    else:                                   # RAW / UNKNOWN -> near-full frame
        x0, y0, x1, y1 = tx0, ty0, tx1, ty1
        subtype, sub_sig = kind, {}

    fx, fy = x0 / scale, y0 / scale
    fw, fh = (x1 - x0 + 1) / scale, (y1 - y0 + 1) / scale
    fx = max(0, fx); fy = max(0, fy)
    fw = min(W - fx, fw); fh = min(H - fy, fh)
    car = fw / max(fh, 1)
    cov = (fw * fh) / (W * H)
    ar_score = float(np.exp(-((car - CARD_AR) / 0.16) ** 2))

    # ---- PHASE 4: confidence -------------------------------------------- #
    if kind == "UNKNOWN":
        conf = 0.15
    elif kind == "RAW":
        cov_score = float(np.clip((cov - 0.72) / 0.26, 0, 1))
        conf = 0.5 * ar_score + 0.5 * cov_score
    else:
        border = (float(np.clip(min(lm, rm) / 0.03, 0, 1)) * 0.4
                  + float(np.clip(tm / 0.08, 0, 1)) * 0.3
                  + float(np.clip((0.55 - tm) / 0.4, 0, 1)) * 0.3)
        cov_score = float(np.clip(1 - abs(cov - 0.62) / 0.3, 0, 1))
        fill_score = float(np.clip((fill - 0.55) / 0.35, 0, 1))
        conf = 0.42 * ar_score + 0.23 * border + 0.20 * cov_score + 0.15 * fill_score
    conf = round(float(np.clip(conf, 0, 1)), 3)

    crop = {"x": int(round(fx)), "y": int(round(fy)),
            "w": int(round(fw)), "h": int(round(fh))}
    return {
        "type": "RAW" if kind == "RAW" else ("UNKNOWN" if kind == "UNKNOWN" else subtype),
        "kind": kind,
        "w": W, "h": H, "aspect": round(imar, 4),
        "crop": crop,
        "confidence": conf,
        "signals": {
            "label_frac": round(label_end / sh, 3), "label_cov": round(label_cov, 3),
            "side_plastic": round(side_plastic, 3), "top_margin": round(tm, 3),
            "cov_area": round(cov, 3), "crop_ar": round(car, 3), "fill": round(fill, 3),
            **sub_sig,
        },
    }


# --------------------------------------------------------------------------- #
# catalog + IO
# --------------------------------------------------------------------------- #
def read_catalog():
    """Extract the gallery card list (src, alt, caption, tag) from main.js.

    main.js remains the catalog of *which* cards are shown; this script only
    reads their identity to know which images to analyse and to take a caption
    hint for PSA/BGS sub-typing.
    """
    txt = open(MAIN_JS, encoding="utf-8").read()
    start = txt.index("const CARD_PHOTOS")
    block = txt[start: txt.index("];", start) + 1]
    cards = []
    for line in block.splitlines():
        m = re.search(r'src:\s*"(/assets/img/collectibles/[^"]+)"', line)
        if not m:
            continue
        src = m.group(1)
        cap = re.search(r'caption:\s*"([^"]*)"', line)
        alt = re.search(r'alt:\s*"([^"]*)"', line)
        tag = re.search(r'tag:\s*"([^"]*)"', line)
        cards.append({
            "src": src,
            "file": os.path.basename(src),
            "caption": cap.group(1) if cap else "",
            "alt": alt.group(1) if alt else "",
            "tag": tag.group(1) if tag else "",
        })
    return cards


def load_overrides():
    if not os.path.exists(OVERRIDES):
        return {}
    return json.load(open(OVERRIDES, encoding="utf-8"))


def normalized(crop, W, H):
    return {
        "left": round(crop["x"] / W, 4),
        "top": round(crop["y"] / H, 4),
        "right": round((crop["x"] + crop["w"]) / W, 4),
        "bottom": round((crop["y"] + crop["h"]) / H, 4),
    }


def build(check=False):
    cards = read_catalog()
    overrides = load_overrides()
    records = {}
    summary = {"auto": 0, "manual": 0, "low_no_override": 0, "total": len(cards)}
    rows = []
    for c in cards:
        path = os.path.join(ROOT, c["src"].lstrip("/"))
        det = detect(path, hint=c["caption"] + " " + c["alt"])
        ov = overrides.get(c["file"])
        if ov:
            crop = ov["crop"]
            typ = ov.get("type", det["type"])
            mode = "manual"
            reason = ov.get("reason", "")
            summary["manual"] += 1
        else:
            crop = det["crop"]
            typ = det["type"]
            mode = "auto"
            reason = ""
            if det["confidence"] < CONF_THRESHOLD:
                summary["low_no_override"] += 1
            else:
                summary["auto"] += 1
        rec = {
            "file": c["file"],
            "src": c["src"],
            "caption": c["caption"],
            "type": typ,
            "mode": mode,
            "confidence": det["confidence"],
            "w": det["w"], "h": det["h"], "aspect": det["aspect"],
            "crop": crop,
            "cropNorm": normalized(crop, det["w"], det["h"]),
            "autoCrop": det["crop"],
            "autoType": det["type"],
            "signals": det["signals"],
        }
        if reason:
            rec["reason"] = reason
        records[c["file"]] = rec
        rows.append(rec)
        flag = ""
        if mode == "auto" and det["confidence"] < CONF_THRESHOLD:
            flag = "  !! LOW CONFIDENCE, NO OVERRIDE"
        print(f'{c["file"]:14s} {typ:11s} {mode:6s} conf={det["confidence"]:.2f} '
              f'ar={det["aspect"]:.3f} crop={crop}{flag}')

    print(f'\nAuto: {summary["auto"]}   Manual override: {summary["manual"]}   '
          f'Low-conf w/o override: {summary["low_no_override"]}   Total: {summary["total"]}')
    if summary["low_no_override"]:
        print("WARNING: low-confidence images without a manual override exist — "
              "add them to scripts/card-crop-overrides.json.")

    if check:
        return records

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    payload = {
        "_generated_by": "scripts/detect-card-crops.py",
        "_note": "Per-image card crop metadata. Do not edit by hand; edit the "
                 "detector or scripts/card-crop-overrides.json and re-run.",
        "cards": records,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")

    slim = {k: {"type": v["type"], "mode": v["mode"], "confidence": v["confidence"],
                "w": v["w"], "h": v["h"], "crop": v["crop"], "cropNorm": v["cropNorm"]}
            for k, v in records.items()}
    with open(OUT_JS, "w", encoding="utf-8") as f:
        f.write("/* GENERATED by scripts/detect-card-crops.py — do not edit by hand. */\n")
        f.write("/* Per-image card-crop metadata for the display-case gallery. */\n")
        f.write("window.CARD_CROPS = ")
        json.dump(slim, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    print(f"\nWrote {os.path.relpath(OUT_JSON, ROOT)} and {os.path.relpath(OUT_JS, ROOT)}")
    return records


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="detect and print only; write no files")
    args = ap.parse_args()
    build(check=args.check)
