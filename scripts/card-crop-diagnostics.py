#!/usr/bin/env python3
"""Human-quality validation view for the card-crop system (development only).

Renders one contact sheet with, for every gallery image:

    SOURCE (with the detected card box) | FINAL CROP that will be displayed

plus the classification (RAW / PSA / BGS / …), the crop mode (auto vs manual
override) and the detector's confidence.  It makes it obvious at a glance if the
algorithm ever selected the slab, the grading label, the background, or only
part of the card.

    python3 scripts/card-crop-diagnostics.py

Output: scripts/diagnostics/card-crop-diagnostics.png  (git-ignored dev artifact)
Requires: pip install numpy opencv-python pillow
"""
import importlib.util
import json
import os

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = os.path.join(ROOT, "assets", "data", "card-crops.json")
OUT_DIR = os.path.join(ROOT, "scripts", "diagnostics")
OUT = os.path.join(OUT_DIR, "card-crop-diagnostics.png")

# Load the detector so the diagnostic shows the *auto* box even for images that
# ship with a manual override.
_spec = importlib.util.spec_from_file_location(
    "detect_card_crops", os.path.join(ROOT, "scripts", "detect-card-crops.py"))
_dcc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_dcc)

TYPE_COLOR = {
    "RAW": (90, 220, 120), "PSA": (240, 120, 120), "BGS": (240, 200, 110),
    "OTHER_SLAB": (200, 160, 240), "UNKNOWN": (160, 160, 160),
}


def load_meta():
    if os.path.exists(META):
        return json.load(open(META, encoding="utf-8"))["cards"]
    return None


def main():
    cards = load_meta()
    if cards is None:
        # fall back to detecting straight from the catalog
        recs = _dcc.build(check=True)
        cards = recs
    os.makedirs(OUT_DIR, exist_ok=True)

    col_src, col_fin, gap, pad, textw = 210, 150, 14, 12, 190
    row_h = 320
    items = list(cards.values())
    cols = 3
    rows = (len(items) + cols - 1) // cols
    cell_w = col_src + col_fin + textw + gap * 3
    sheet = Image.new("RGB", (cols * cell_w + pad, rows * (row_h + pad) + pad), (17, 17, 20))
    d = ImageDraw.Draw(sheet)

    for i, rec in enumerate(items):
        path = os.path.join(ROOT, rec["src"].lstrip("/"))
        det = _dcc.detect(path, hint=rec.get("caption", ""))
        im = Image.open(path).convert("RGB")
        W, H = im.size
        r = i // cols
        c = i % cols
        ox = pad + c * cell_w
        oy = pad + r * (row_h + pad)

        # SOURCE with auto box (red) + final chosen box (green)
        s = min(col_src / W, row_h / H)
        src = im.resize((int(W * s), int(H * s)))
        ds = ImageDraw.Draw(src)
        a = det["crop"]
        ds.rectangle([a["x"] * s, a["y"] * s, (a["x"] + a["w"]) * s, (a["y"] + a["h"]) * s],
                     outline=(255, 80, 80), width=2)
        f = rec["crop"]
        ds.rectangle([f["x"] * s, f["y"] * s, (f["x"] + f["w"]) * s, (f["y"] + f["h"]) * s],
                     outline=(70, 240, 110), width=2)
        sheet.paste(src, (ox, oy))

        # FINAL crop (what the gallery displays)
        fin = im.crop((f["x"], f["y"], f["x"] + f["w"], f["y"] + f["h"]))
        fs = min(col_fin / fin.width, row_h / fin.height)
        fin = fin.resize((int(fin.width * fs), int(fin.height * fs)))
        fx = ox + col_src + gap
        sheet.paste(fin, (fx, oy))

        # text column
        tx = fx + col_fin + gap
        typ = rec["type"]
        d.text((tx, oy + 2), rec["file"][5:-4], fill=(235, 235, 235))
        d.text((tx, oy + 18), typ, fill=TYPE_COLOR.get(typ, (200, 200, 200)))
        d.text((tx, oy + 34), f"mode: {rec['mode']}", fill=(210, 210, 210))
        d.text((tx, oy + 50), f"conf: {rec['confidence']:.2f}", fill=(210, 210, 210))
        d.text((tx, oy + 70), f"auto:  {a['w']}x{a['h']}", fill=(255, 150, 150))
        d.text((tx, oy + 84), f"final: {f['w']}x{f['h']}", fill=(140, 240, 170))
        d.text((tx, oy + 104), f"card AR {f['w']/f['h']:.3f}", fill=(180, 200, 235))
        if rec.get("mode") == "manual":
            d.text((tx, oy + 124), "override", fill=(255, 210, 120))

    # legend
    d.text((pad, sheet.height - 0), "", fill=(0, 0, 0))
    sheet.save(OUT)
    print(f"Wrote {os.path.relpath(OUT, ROOT)}  ({sheet.width}x{sheet.height})")
    print("Red box = detector's automatic card box; Green box = final crop shown "
          "in the gallery (manual override where it differs).")


if __name__ == "__main__":
    main()
