from bs4 import BeautifulSoup
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text(encoding='utf-8')
optcg_html = (root / 'one-piece-tcg.html').read_text(encoding='utf-8')
vercel = json.loads((root / 'vercel.json').read_text(encoding='utf-8') )
robots = (root / 'robots.txt').read_text(encoding='utf-8')
sitemap = (root / 'sitemap.xml').read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
optcg_soup = BeautifulSoup(optcg_html, 'html.parser')
errors = []

# Protect the critical-rendering-path implementation on every page.
for label, page_html in [('Homepage', html), ('One Piece TCG page', optcg_html)]:
    if 'fonts.googleapis.com' in page_html:
        errors.append(f'{label} still loads the render-blocking Google Fonts stylesheet.')
    if not page_html.count('data-critical-css-version="1"'):
        errors.append(f'{label} is missing inline critical CSS.')
    if 'rel="preload" href="/assets/css/styles.css?v=34" as="style"' not in page_html:
        errors.append(f'{label} is missing the asynchronous main stylesheet preload.')
    if '<noscript><link rel="stylesheet" href="/assets/css/styles.css?v=34" /></noscript>' not in page_html:
        errors.append(f'{label} is missing the no-JavaScript stylesheet fallback.')
for font_file in ('assets/fonts/figtree-latin.woff2', 'assets/fonts/syne-latin.woff2'):
    if not (root / font_file).is_file():
        errors.append(f'Missing self-hosted font asset: {font_file}')

robots_meta = soup.find('meta', attrs={'name': 'robots'})
if robots_meta and 'noindex' in (robots_meta.get('content') or '').lower():
    errors.append('Homepage still has a noindex robots meta tag.')

for rule in vercel.get('headers', []):
    for header in rule.get('headers', []):
        if header.get('key', '').lower() == 'x-robots-tag' and 'noindex' in header.get('value', '').lower():
            errors.append('Vercel configuration still adds an X-Robots-Tag noindex header.')

if not soup.title or 'West Hartford' not in soup.title.get_text():
    errors.append('Homepage title does not include the local service area.')

hero = soup.select_one('.hero')
if hero and hero.find('h1') and 'sr-only' not in (hero.find('h1').get('class') or []):
    errors.append('Hero must not contain a prominent SEO H1.')

footer_context = soup.select_one('footer .footer-seo')
footer_text = footer_context.get_text(' ', strip=True) if footer_context else ''
h1 = soup.find('h1')
has_local_h1 = bool(h1 and 'West Hartford' in h1.get_text())
has_footer_local = bool(footer_context and 'West Hartford' in footer_text)
if not has_local_h1 and not has_footer_local:
    errors.append('Homepage is missing a local-business H1.')

if not footer_context or 'Trading card shop' not in footer_text or 'West Hartford, CT' not in footer_text:
    errors.append('Footer must include compact local business context.')

schema_node = soup.find('script', attrs={'type': 'application/ld+json'})
if not schema_node:
    errors.append('Missing LocalBusiness structured data.')
else:
    schema = json.loads(schema_node.get_text())
    if schema.get('url') != 'https://www.thousandsunnytcg.com/':
        errors.append('Structured-data URL is not the live canonical domain.')
    if not schema.get('image') or not all('www.thousandsunnytcg.com' in url for url in schema['image']):
        errors.append('Structured-data images are not live-domain URLs.')

if 'Sitemap: https://www.thousandsunnytcg.com/sitemap.xml' not in robots:
    errors.append('robots.txt is missing the live sitemap declaration.')

# Keep the dedicated One Piece TCG landing page indexable and internally coherent.
optcg_canonical = optcg_soup.find('link', rel='canonical')
if not optcg_canonical or optcg_canonical.get('href') != 'https://www.thousandsunnytcg.com/one-piece-tcg':
    errors.append('One Piece TCG page has an incorrect or missing canonical URL.')
optcg_robots = optcg_soup.find('meta', attrs={'name': 'robots'})
if not optcg_robots or 'noindex' in (optcg_robots.get('content') or '').lower():
    errors.append('One Piece TCG page is missing an indexable robots directive.')
if not optcg_soup.title or 'West Hartford' not in optcg_soup.title.get_text():
    errors.append('One Piece TCG page title does not include the local service area.')
if not optcg_soup.find('meta', attrs={'property': 'og:image:alt'}):
    errors.append('One Piece TCG page is missing social-image alt metadata.')
optcg_jsonld = []
for node in optcg_soup.find_all('script', attrs={'type': 'application/ld+json'}):
    try:
        optcg_jsonld.append(json.loads(node.get_text()))
    except json.JSONDecodeError as exc:
        errors.append(f'One Piece TCG JSON-LD is invalid: {exc}')
if not any(isinstance(data, dict) and any(item.get('@type') == 'BreadcrumbList' for item in data.get('@graph', []) if isinstance(item, dict)) for data in optcg_jsonld):
    errors.append('One Piece TCG page is missing BreadcrumbList structured data.')

try:
    sitemap_root = ET.fromstring(sitemap)
    urls = [node.text for node in sitemap_root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    homepage = 'https://www.thousandsunnytcg.com/'
    if homepage not in urls:
        errors.append('Sitemap is missing the live canonical homepage.')
    off_domain = [url for url in urls if not url.startswith(homepage)]
    if off_domain:
        errors.append(f'Sitemap lists non-canonical URLs: {", ".join(off_domain)}')
    duplicates = sorted({url for url in urls if urls.count(url) > 1})
    if duplicates:
        errors.append(f'Sitemap lists duplicate URLs: {", ".join(duplicates)}')
except ET.ParseError as exc:
    errors.append(f'Sitemap is not valid XML: {exc}')

if errors:
    print('SEO validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print('SEO validation passed.')
print('No production noindex rules, no prominent hero SEO heading, compact footer context, live-domain LocalBusiness data, robots.txt, and sitemap.xml are present.')
