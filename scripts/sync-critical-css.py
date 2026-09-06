from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
critical = (root / "assets/css/critical.css").read_text(encoding="utf-8").strip()
replacement = f'  <style data-critical-css-version="1">\n{critical}\n  </style>'
pattern = re.compile(r'  <style data-critical-css-version="1">.*?  </style>', re.DOTALL)
for name in ("index.html", "one-piece-tcg.html"):
    path = root / name
    html = path.read_text(encoding="utf-8")
    updated, count = pattern.subn(replacement, html, count=1)
    if count != 1:
        raise SystemExit(f"Critical CSS block not found in {name}")
    path.write_text(updated, encoding="utf-8")
    print(f"Synchronized {name}")
