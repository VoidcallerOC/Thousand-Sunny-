from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
source = Image.open(root / 'assets/img/logo.png').convert('RGBA')
source.thumbnail((96, 96), Image.Resampling.LANCZOS)
source.save(root / 'assets/img/brand/thousand-sunny-logo-96.webp', 'WEBP', quality=82, method=6)
mark = Image.open(root / 'assets/img/brand/thousand-sunny-ship-mark-v1.webp').convert('RGBA')
mark.thumbnail((96, 96), Image.Resampling.LANCZOS)
mark.save(root / 'assets/img/brand/thousand-sunny-ship-mark-96.webp', 'WEBP', quality=82, method=6)
print('Generated optimized 96px WebP brand assets.')
