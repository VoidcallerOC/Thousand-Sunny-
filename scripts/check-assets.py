from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
allowed_raw = {
    "/assets/img/og-storefront-red-v1.jpg",
    "/assets/img/og.jpg",
    "/assets/img/logo.png",
    "/assets/img/favicon.png",
    "/assets/img/favicon-sunny-ship-v1.png",
    "/assets/img/apple-touch-icon-sunny-ship-v1.png",
    "/assets/img/brand/thousand-sunny-ship-mark-v1.webp",
    # Last-resort <img> fallbacks inside <picture> on the homepage.
    "/assets/img/gear5-tall.jpg",
    "/assets/img/gear5-wide.jpg",
    "/assets/img/store-case.jpg",
    "/assets/img/gallery-figures.jpg",
    "/assets/img/store-counter.jpg",
    "/assets/img/collectibles/card-2229-c1.jpg",
}

text_files = [root / "index.html", root / "assets/js/main.js"]
pattern = re.compile(r"""(?:src|href)=[\"'](/assets/img/[^\"']+\.(?:jpg|jpeg|png))[\"']""")

for path in text_files:
    text = path.read_text(encoding="utf-8")
    for match in pattern.findall(text):
        clean = match.split("?")[0]
        if clean.startswith("/assets/img/optimized/"):
            continue
        if clean in allowed_raw:
            continue
        if "/assets/img/pulls/" in clean:
            errors.append(f"{path.name} still uses raw pull image as a served src: {clean}")
            continue
        if "/assets/img/collectibles/" in clean:
            errors.append(f"{path.name} still serves a raw collectible JPG: {clean}")
            continue
        errors.append(f"{path.name} still serves a raw store image: {clean}")

if errors:
    print("Asset check failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Asset check passed.")
print("Rendered image fallbacks are on the allowlist; optimized sources remain required for new images.")
