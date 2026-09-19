from bs4 import BeautifulSoup
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
site = 'https://www.thousandsunnytcg.com'
page_specs = {
    'Homepage': {
        'path': root / 'index.html',
        'canonical': f'{site}/',
    },
    'One Piece TCG hub': {
        'path': root / 'one-piece-tcg.html',
        'canonical': f'{site}/one-piece-tcg',
    },
    'Featured One Piece cards': {
        'path': root / 'one-piece-tcg-cards.html',
        'canonical': f'{site}/one-piece-tcg/cards',
    },
}

pages = {}
for label, spec in page_specs.items():
    html = spec['path'].read_text(encoding='utf-8')
    pages[label] = {'html': html, 'soup': BeautifulSoup(html, 'html.parser'), **spec}

vercel = json.loads((root / 'vercel.json').read_text(encoding='utf-8'))
robots = (root / 'robots.txt').read_text(encoding='utf-8')
sitemap = (root / 'sitemap.xml').read_text(encoding='utf-8')
errors = []


def canonical_of(soup):
    node = soup.find('link', rel='canonical')
    return node.get('href') if node else None


def jsonld_items(label, soup):
    items = []
    for node in soup.find_all('script', attrs={'type': 'application/ld+json'}):
        try:
            items.append(json.loads(node.get_text()))
        except json.JSONDecodeError as exc:
            errors.append(f'{label} JSON-LD is invalid: {exc}')
    return items


def graph_types(items):
    types = []
    for item in items:
        if not isinstance(item, dict):
            continue
        values = item.get('@graph', [item])
        for value in values:
            if isinstance(value, dict):
                value_type = value.get('@type')
                types.extend(value_type if isinstance(value_type, list) else [value_type])
    return set(types)


for label, page in pages.items():
    html, soup, canonical = page['html'], page['soup'], page['canonical']
    title = soup.title.get_text(strip=True) if soup.title else ''
    description = soup.find('meta', attrs={'name': 'description'})
    robots_meta = soup.find('meta', attrs={'name': 'robots'})
    h1s = soup.find_all('h1')

    if not title:
        errors.append(f'{label} is missing a title.')
    if not description or not (description.get('content') or '').strip():
        errors.append(f'{label} is missing a meta description.')
    if canonical_of(soup) != canonical:
        errors.append(f'{label} has an incorrect or missing canonical URL.')
    if robots_meta and 'noindex' in (robots_meta.get('content') or '').lower():
        errors.append(f'{label} has a noindex robots directive.')
    if len(h1s) != 1 or not h1s[0].get_text(' ', strip=True):
        errors.append(f'{label} must have exactly one non-empty H1.')

    if 'fonts.googleapis.com' in html:
        errors.append(f'{label} still loads the render-blocking Google Fonts stylesheet.')
    if html.count('data-critical-css-version="1"') != 1:
        errors.append(f'{label} is missing inline critical CSS.')
    if 'rel="preload" href="/assets/css/styles.css?v=38" as="style"' not in html:
        errors.append(f'{label} is missing the asynchronous v38 main stylesheet preload.')
    if '<noscript><link rel="stylesheet" href="/assets/css/styles.css?v=38" /></noscript>' not in html:
        errors.append(f'{label} is missing the v38 no-JavaScript stylesheet fallback.')

    for property_name in ('og:title', 'og:description', 'og:url', 'og:image', 'og:image:alt'):
        if not soup.find('meta', attrs={'property': property_name}):
            errors.append(f'{label} is missing {property_name} metadata.')
    for property_name in ('twitter:card', 'twitter:title', 'twitter:description', 'twitter:image', 'twitter:image:alt'):
        if not soup.find('meta', attrs={'name': property_name}):
            errors.append(f'{label} is missing {property_name} metadata.')

    page['jsonld'] = jsonld_items(label, soup)

for font_file in ('assets/fonts/figtree-latin.woff2', 'assets/fonts/syne-latin.woff2'):
    if not (root / font_file).is_file():
        errors.append(f'Missing self-hosted font asset: {font_file}')

for rule in vercel.get('headers', []):
    for header in rule.get('headers', []):
        if header.get('key', '').lower() == 'x-robots-tag' and 'noindex' in header.get('value', '').lower():
            errors.append('Vercel configuration adds an X-Robots-Tag noindex header.')

featured_cards_rewrite = {
    'source': '/one-piece-tcg/cards',
    'destination': '/one-piece-tcg-cards',
}
if featured_cards_rewrite not in vercel.get('rewrites', []):
    errors.append('Vercel is missing the featured-cards clean-URL rewrite.')

home = pages['Homepage']
home_soup = home['soup']
home_title = home_soup.title.get_text() if home_soup.title else ''
if 'West Hartford' not in home_title:
    errors.append('Homepage title does not include the local service area.')
hero = home_soup.select_one('.hero')
if hero and hero.find('h1') and 'sr-only' not in (hero.find('h1').get('class') or []):
    errors.append('Homepage must not contain a prominent SEO H1.')
footer_context = home_soup.select_one('footer .footer-seo')
footer_text = footer_context.get_text(' ', strip=True) if footer_context else ''
if not footer_context or 'Trading card shop' not in footer_text or 'West Hartford, CT' not in footer_text:
    errors.append('Homepage footer must include compact local-business context.')
if not home_soup.select_one('section#one-piece h2'):
    errors.append('Homepage is missing the crawlable One Piece TCG section.')
if not home_soup.select_one('a[href="/one-piece-tcg"]'):
    errors.append('Homepage is missing an internal link to the One Piece hub.')
if not home_soup.select_one('a[href="/one-piece-tcg/cards"]'):
    errors.append('Homepage is missing an internal link to featured One Piece cards.')

home_types = graph_types(home['jsonld'])
if not ({'Store', 'HobbyShop'} & home_types):
    errors.append('Homepage is missing LocalBusiness-style structured data.')
if 'WebSite' not in home_types:
    errors.append('Homepage is missing WebSite structured data.')

hub = pages['One Piece TCG hub']
hub_soup = hub['soup']
hub_title = hub_soup.title.get_text() if hub_soup.title else ''
if 'One Piece TCG' not in hub_title or 'Connecticut' not in hub_title:
    errors.append('One Piece hub title must include One Piece TCG and Connecticut.')
if not hub_soup.select_one('.breadcrumb'):
    errors.append('One Piece hub is missing visible breadcrumb navigation.')
if not hub_soup.select_one('a[href="/one-piece-tcg/cards"]'):
    errors.append('One Piece hub is missing an internal link to featured cards.')
hub_types = graph_types(hub['jsonld'])
if 'BreadcrumbList' not in hub_types:
    errors.append('One Piece hub is missing BreadcrumbList structured data.')
if 'FAQPage' not in hub_types:
    errors.append('One Piece hub is missing FAQPage structured data that mirrors its visible FAQ.')

cards = pages['Featured One Piece cards']
cards_soup = cards['soup']
cards_title = cards_soup.title.get_text() if cards_soup.title else ''
if 'Featured One Piece TCG Cards' not in cards_title or 'Connecticut' not in cards_title:
    errors.append('Featured-cards page title must include featured One Piece TCG cards and Connecticut.')
if not cards_soup.select_one('.breadcrumb'):
    errors.append('Featured-cards page is missing visible breadcrumb navigation.')
featured_cards = cards_soup.select('.featured-card')
if len(featured_cards) < 1:
    errors.append('Featured-cards page has no crawlable photographed card entries.')
for image in cards_soup.select('.featured-card img'):
    if not image.get('width') or not image.get('height'):
        errors.append('Featured-card images must reserve layout space with width and height.')
    if image.get('loading') != 'lazy':
        errors.append('Below-the-fold featured-card images must be lazy loaded.')
cards_types = graph_types(cards['jsonld'])
if not {'BreadcrumbList', 'ItemList'} <= cards_types:
    errors.append('Featured-cards page is missing BreadcrumbList or ItemList structured data.')
if {'Product', 'Offer', 'Event'} & cards_types:
    errors.append('Featured-cards page must not invent Product, Offer, or Event structured data.')

if 'Sitemap: https://www.thousandsunnytcg.com/sitemap.xml' not in robots:
    errors.append('robots.txt is missing the live sitemap declaration.')

try:
    sitemap_root = ET.fromstring(sitemap)
    urls = [node.text for node in sitemap_root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    expected_urls = {spec['canonical'] for spec in page_specs.values()}
    missing = expected_urls - set(urls)
    if missing:
        errors.append(f'Sitemap is missing canonical URLs: {", ".join(sorted(missing))}')
    off_domain = [url for url in urls if not url.startswith(f'{site}/')]
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
print('Every canonical page has unique crawlable metadata, critical CSS v38, structured data, and internal links.')
