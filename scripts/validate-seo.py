from bs4 import BeautifulSoup
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text(encoding='utf-8')
vercel = json.loads((root / 'vercel.json').read_text(encoding='utf-8') )
robots = (root / 'robots.txt').read_text(encoding='utf-8')
sitemap = (root / 'sitemap.xml').read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
errors = []

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
