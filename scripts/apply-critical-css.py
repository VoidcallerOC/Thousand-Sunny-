from pathlib import Path

root = Path(__file__).resolve().parents[1]
critical = (root / "assets/css/critical.css").read_text(encoding="utf-8").strip()
style_block = f'  <style data-critical-css-version="1">\n{critical}\n  </style>'
old = '''  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Syne:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/assets/css/styles.css?v=32" />'''
new = f'''{style_block}
  <link rel="preload" href="/assets/css/styles.css?v=33" as="style" onload="this.onload=null;this.rel='stylesheet'" />
  <noscript><link rel="stylesheet" href="/assets/css/styles.css?v=33" /></noscript>'''
for name in ("index.html", "one-piece-tcg.html"):
    path = root / name
    html = path.read_text(encoding="utf-8")
    if old not in html:
        raise SystemExit(f"Expected blocking stylesheet block not found in {name}")
    path.write_text(html.replace(old, new, 1), encoding="utf-8")
    print(f"Updated {name}")
