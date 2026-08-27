from bs4 import BeautifulSoup
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text(encoding='utf-8')
vercel = json.loads((root / 'vercel.json').read_text(encoding='utf-8'))
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

h1s = soup.find_all('h1')
if len(h1s) != 1 or 'Thousand Sunny Cards & Collectibles' not in h1s[0].get_text(' ', strip=True):
    errors.append('Homepage must have exactly one descriptive business-name H1.')

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
    if urls != ['https://www.thousandsunnytcg.com/']:
        errors.append('Sitemap does not contain exactly the live canonical homepage.')
except ET.ParseError as exc:
    errors.append(f'Sitemap is not valid XML: {exc}')

if errors:
    print('SEO validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print('SEO validation passed.')
print('No production noindex rules, one descriptive H1, live-domain LocalBusiness data, robots.txt, and sitemap.xml are present.')
