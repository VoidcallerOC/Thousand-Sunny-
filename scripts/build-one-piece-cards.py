#!/usr/bin/env python3
"""Build the static One Piece display-case collection from verified photographed cards.

This page intentionally contains no inventory, price, availability, or product schema.
The cards are a crawlable visual collection that is backed by the existing display-case
photography and should be refreshed whenever the curated showcase changes.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "one-piece-tcg.html"
TARGET = ROOT / "one-piece-tcg-cards.html"
CANONICAL = "https://www.thousandsunnytcg.com/one-piece-tcg/cards"

CARDS = [
    {
        "id": "monkey-d-luffy-bgs-10",
        "name": "Monkey D. Luffy · BGS 10",
        "alt": "Beckett graded Monkey D. Luffy One Piece trading card",
        "src": "card-2219-c1",
        "width": 859,
        "height": 1635,
    },
    {
        "id": "monkey-d-luffy-pristine-10",
        "name": "Monkey D. Luffy · Pristine 10",
        "alt": "Pristine 10 Monkey D. Luffy One Piece card",
        "src": "card-2220-c1",
        "width": 956,
        "height": 1673,
    },
    {
        "id": "monkey-d-luffy",
        "name": "Monkey D. Luffy",
        "alt": "Monkey D. Luffy One Piece card",
        "src": "card-2222-c1",
        "width": 1249,
        "height": 1745,
    },
    {
        "id": "shanks",
        "name": "Shanks",
        "alt": "Shanks One Piece card",
        "src": "card-2223-c1",
        "width": 1260,
        "height": 1760,
    },
    {
        "id": "nami",
        "name": "Nami",
        "alt": "Nami One Piece card",
        "src": "card-2227-c1",
        "width": 984,
        "height": 1403,
    },
    {
        "id": "gear-two-pristine-10",
        "name": "Gear Two · Pristine 10",
        "alt": "Pristine 10 Gear Two One Piece card in Beckett slab",
        "src": "card-2286-c2",
        "width": 832,
        "height": 1602,
    },
    {
        "id": "monkey-d-luffy-sp-pristine-10",
        "name": "Monkey D. Luffy SP · Pristine 10",
        "alt": "Pristine 10 Monkey D. Luffy SP One Piece card in Beckett slab",
        "src": "card-2285-c1",
        "width": 832,
        "height": 1584,
    },
    {
        "id": "portgas-d-ace-manga-art",
        "name": "Portgas D. Ace · Manga Art Pristine 10",
        "alt": "Pristine 10 Portgas D. Ace Manga Art One Piece card in Beckett slab",
        "src": "card-2283-c2",
        "width": 1024,
        "height": 1649,
    },
    {
        "id": "boa-hancock-manga-alternate-art",
        "name": "Boa Hancock · Manga Alternate Art PSA 10",
        "alt": "PSA 10 Boa Hancock Manga Alternate Art One Piece card",
        "src": "card-2284-c3",
        "width": 880,
        "height": 1611,
    },
]


def card_markup(card: dict[str, object]) -> str:
    stem = str(card["src"])
    return f'''          <article class="featured-card" id="{card["id"]}">
            <picture>
              <source type="image/avif" srcset="/assets/img/optimized/{stem}-320.avif 320w, /assets/img/optimized/{stem}-640.avif 640w, /assets/img/optimized/{stem}-960.avif 960w" sizes="(min-width: 1024px) 33vw, (min-width: 640px) 50vw, 100vw" />
              <img src="/assets/img/optimized/{stem}-640.webp" srcset="/assets/img/optimized/{stem}-320.webp 320w, /assets/img/optimized/{stem}-640.webp 640w, /assets/img/optimized/{stem}-960.webp 960w" sizes="(min-width: 1024px) 33vw, (min-width: 640px) 50vw, 100vw" alt="{card["alt"]}" width="{card["width"]}" height="{card["height"]}" loading="lazy" decoding="async" />
            </picture>
            <div class="featured-card__copy">
              <p class="featured-card__label">One Piece TCG · display case</p>
              <h3>{card["name"]}</h3>
              <p>Photographed in Thousand Sunny’s featured card showcase.</p>
            </div>
          </article>'''


store = {
    "@type": ["Store", "HobbyShop"],
    "@id": "https://www.thousandsunnytcg.com/#store",
    "name": "Thousand Sunny Cards & Collectibles",
    "alternateName": ["Thousand Sunny TCG", "Thousand Sunny Cards", "TSCC"],
    "url": "https://www.thousandsunnytcg.com/",
    "telephone": "+1-757-358-7643",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "75 Park Rd",
        "addressLocality": "West Hartford",
        "addressRegion": "CT",
        "postalCode": "06119",
        "addressCountry": "US",
    },
    "sameAs": [
        "https://www.instagram.com/tscc_ct/",
        "https://www.facebook.com/p/Thousand-Sunny-Cards-and-Collectibles-61587789147573/",
    ],
}

schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "WebPage",
            "@id": f"{CANONICAL}#webpage",
            "name": "Featured One Piece TCG Cards at Thousand Sunny",
            "url": CANONICAL,
            "description": "A photographed collection of featured One Piece TCG cards from Thousand Sunny’s display case in West Hartford, Connecticut.",
            "isPartOf": {"@id": "https://www.thousandsunnytcg.com/#website"},
            "about": [
                {"@type": "Thing", "name": "One Piece Card Game"},
                {"@type": "Thing", "name": "One Piece TCG cards"},
            ],
            "mainEntity": {"@id": f"{CANONICAL}#featured-cards"},
            "breadcrumb": {"@id": f"{CANONICAL}#breadcrumb"},
        },
        store,
        {
            "@type": "BreadcrumbList",
            "@id": f"{CANONICAL}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.thousandsunnytcg.com/"},
                {"@type": "ListItem", "position": 2, "name": "One Piece TCG", "item": "https://www.thousandsunnytcg.com/one-piece-tcg"},
                {"@type": "ListItem", "position": 3, "name": "Featured One Piece Cards", "item": CANONICAL},
            ],
        },
        {
            "@type": "ItemList",
            "@id": f"{CANONICAL}#featured-cards",
            "name": "Featured One Piece TCG display-case cards",
            "numberOfItems": len(CARDS),
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": index,
                    "name": card["name"],
                    "url": f"{CANONICAL}#{card['id']}",
                }
                for index, card in enumerate(CARDS, start=1)
            ],
        },
        {
            "@type": "WebSite",
            "@id": "https://www.thousandsunnytcg.com/#website",
            "url": "https://www.thousandsunnytcg.com/",
            "name": "Thousand Sunny TCG",
            "alternateName": "Thousand Sunny Cards & Collectibles",
            "publisher": {"@id": "https://www.thousandsunnytcg.com/#store"},
        },
    ],
}

cards_html = "\n".join(card_markup(card) for card in CARDS)
source = SOURCE.read_text(encoding="utf-8")
head_prefix = source[: source.index('  <script type="application/ld+json">')]
metadata = {
    r"<title>.*?</title>": "<title>Featured One Piece TCG Cards in Connecticut | Thousand Sunny</title>",
    r'<meta name="description" content=".*?" />': '<meta name="description" content="See photographed One Piece TCG cards from Thousand Sunny’s display case in West Hartford, Connecticut. Ask about current availability before visiting." />',
    r'<link rel="canonical" href=".*?" />': f'<link rel="canonical" href="{CANONICAL}" />',
    r'<meta property="og:title" content=".*?" />': '<meta property="og:title" content="Featured One Piece TCG Cards | Thousand Sunny" />',
    r'<meta property="og:description" content=".*?" />': '<meta property="og:description" content="Photographed One Piece TCG cards from Thousand Sunny’s display case in West Hartford, Connecticut." />',
    r'<meta property="og:url" content=".*?" />': f'<meta property="og:url" content="{CANONICAL}" />',
    r'<meta name="twitter:title" content=".*?" />': '<meta name="twitter:title" content="Featured One Piece TCG Cards | Thousand Sunny" />',
    r'<meta name="twitter:description" content=".*?" />': '<meta name="twitter:description" content="Photographed One Piece TCG cards from Thousand Sunny’s display case in West Hartford, Connecticut." />',
}
for pattern, replacement in metadata.items():
    head_prefix, count = re.subn(pattern, replacement, head_prefix, count=1)
    if count != 1:
        raise SystemExit(f"Expected head metadata was not found for pattern: {pattern}")

body = f'''</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <div class="sprog" id="sprog" aria-hidden="true"></div>
  <div class="grain" aria-hidden="true"></div>

  <header class="nav" id="nav">
    <a class="brand" href="/" aria-label="Thousand Sunny Cards home">
      <img src="/assets/img/brand/thousand-sunny-ship-mark-96.webp" alt="Thousand Sunny ship logo" width="48" height="48" id="sunMark" />
      <span>
        <span class="brand-name">Thousand S<span class="gold">u</span>nny</span>
        <span class="brand-tag">Thousand Sunny TCG · Cards &amp; Collectibles</span>
      </span>
    </a>
    <nav class="nav-links" aria-label="Primary">
      <a href="/">Home</a>
      <a href="/one-piece-tcg">One Piece TCG</a>
      <a href="/one-piece-tcg/cards" aria-current="page">Featured cards</a>
      <a href="/#events">Events</a>
      <a href="/#visit">Visit</a>
    </nav>
    <div class="nav-cta"><a class="btn btn--primary btn--sm" href="/#visit">Visit</a></div>
    <button class="nav-toggle" id="navToggle" type="button" aria-label="Open menu" aria-expanded="false"><span></span></button>
  </header>

  <div class="nav-drawer" id="navMenu" hidden>
    <div class="nav-drawer-sheet">
      <div class="nav-drawer-handle"></div>
      <div class="nav-drawer-head">
        <p class="nav-drawer-title">Menu</p>
        <button class="icon-btn" id="navClose" type="button" aria-label="Close menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
      </div>
      <nav class="nav-drawer-links" aria-label="Mobile">
        <a href="/">Home</a>
        <a href="/one-piece-tcg">One Piece TCG</a>
        <a href="/one-piece-tcg/cards" aria-current="page">Featured cards</a>
        <a href="/#events">Events</a>
        <a href="/#trade">Sell &amp; trade</a>
        <a href="/#visit">Visit</a>
      </nav>
      <a class="btn btn--primary btn--block" href="/#visit">Plan your visit</a>
    </div>
  </div>

  <main id="main">
    <section class="hero" id="top">
      <div class="hero-media">
        <picture>
          <source media="(min-width: 768px)" type="image/avif" srcset="/assets/img/optimized/gear5-wide-640.avif 640w, /assets/img/optimized/gear5-wide-960.avif 960w, /assets/img/optimized/gear5-wide-1120.avif 1120w" sizes="100vw" />
          <source media="(min-width: 768px)" type="image/webp" srcset="/assets/img/optimized/gear5-wide-640.webp 640w, /assets/img/optimized/gear5-wide-960.webp 960w, /assets/img/optimized/gear5-wide-1120.webp 1120w" sizes="100vw" />
          <source type="image/avif" srcset="/assets/img/optimized/gear5-tall-480.avif 480w, /assets/img/optimized/gear5-tall-640.avif 640w" sizes="min(100vw, 640px)" />
          <source type="image/webp" srcset="/assets/img/optimized/gear5-tall-480.webp 480w, /assets/img/optimized/gear5-tall-640.webp 640w" sizes="min(100vw, 640px)" />
          <img class="hero-photo" src="/assets/img/optimized/gear5-tall-640.webp" alt="Life-size Gear 5 Luffy greeter at Thousand Sunny Cards in West Hartford" width="830" height="1383" sizes="100vw" fetchpriority="high" />
        </picture>
      </div>
      <div class="hero-shade"></div>
      <div class="wrap hero-copy">
        <p class="eyebrow">West Hartford · Connecticut</p>
        <h1 class="h-sec">Featured One Piece TCG <span class="gold">cards</span></h1>
        <p class="hero-lead">A photographed collection from Thousand Sunny’s display case. The cards shown are real showcase pieces, not a live online inventory.</p>
        <div class="cta-actions">
          <a class="btn btn--primary" href="#cards">View the featured cards</a>
          <a class="btn btn--ghost" href="/one-piece-tcg">One Piece TCG hub</a>
        </div>
      </div>
    </section>

    <section class="section" id="cards">
      <div class="wrap">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="/">Home</a></li>
            <li><a href="/one-piece-tcg">One Piece TCG</a></li>
            <li aria-current="page">Featured cards</li>
          </ol>
        </nav>
        <p class="eyebrow">From the display case</p>
        <h2 class="h-sec">One Piece TCG cards <span class="gold">we photographed</span></h2>
        <p class="lead">These One Piece cards have been photographed in Thousand Sunny’s featured display case. They document the shop’s collector focus; grades, condition, and availability can change, so call or text before making a special trip for a specific card.</p>
        <div class="featured-card-grid">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section section--surface" id="shop-one-piece">
      <div class="wrap">
        <p class="eyebrow">One Piece Card Game at the shop</p>
        <h2 class="h-sec">Singles, sealed product, and <span class="gold">collector cards</span></h2>
        <p class="lead">Thousand Sunny carries One Piece Card Game singles, sealed product, starter decks, and graded cards when they are in stock. The collection rotates with the shop’s current stock, while this page remains a photographed showcase rather than a sales catalog.</p>
        <div class="cta-actions">
          <a class="btn btn--primary" href="/one-piece-tcg#stock">One Piece TCG at Thousand Sunny</a>
          <a class="btn btn--ghost" href="/#trade">Sell or trade One Piece cards</a>
        </div>
      </div>
    </section>

    <section class="section" id="play-and-visit">
      <div class="wrap">
        <p class="eyebrow">Local community</p>
        <h2 class="h-sec">Play, trade, and <span class="gold">visit the Sunny</span></h2>
        <p class="lead">For confirmed One Piece TCG game nights, release tables, or tournaments, use the store’s event board and social updates. Thousand Sunny does not publish an unconfirmed event schedule or real-time online card inventory.</p>
        <div class="cta-actions">
          <a class="btn btn--primary" href="/one-piece-tcg#locals">One Piece TCG event updates</a>
          <a class="btn btn--ghost" href="/#visit">Hours, directions, and contact</a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="wrap">
      <div class="footer-top">
        <div class="footer-brand">
          <a class="brand" href="/"><img src="/assets/img/brand/thousand-sunny-logo-96.webp" alt="" width="44" height="44" /><span class="brand-name">Thousand S<span class="gold">u</span>nny</span></a>
          <p>One Piece TCG shop in West Hartford, CT. Buy · Sell · Trade · Collect.</p>
        </div>
        <div class="footer-cols">
          <div class="footer-col">
            <p class="footer-heading">Explore</p>
            <a href="/">Home</a>
            <a href="/one-piece-tcg">One Piece TCG</a>
            <a href="/one-piece-tcg/cards">Featured One Piece cards</a>
            <a href="/#events">Events</a>
            <a href="/#trade">Sell &amp; trade</a>
          </div>
          <div class="footer-col">
            <p class="footer-heading">Visit</p>
            <a href="/#visit">Hours</a>
            <a href="https://maps.google.com/?q=Thousand+Sunny+Cards+%26+Collectibles+75+Park+Rd+West+Hartford+CT+06119" target="_blank" rel="noopener">75 Park Rd, West Hartford, CT 06119</a>
          </div>
          <div class="footer-col">
            <p class="footer-heading">Follow</p>
            <a href="https://www.instagram.com/tscc_ct/" target="_blank" rel="noopener">Instagram @tscc_ct</a>
            <a href="tel:+17573587643">(757) 358-7643</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <span class="site">Thousand Sunny <span class="gold">Cards</span></span>
        <span>© <span id="year">2026</span> Thousand Sunny Cards &amp; Collectibles · West Hartford, CT</span>
        <span class="forge-attribution">Website by <a href="https://forge-ct.com" target="_blank" rel="noopener noreferrer">Forge-CT</a></span>
        <span class="footer-seo">Thousand Sunny TCG · One Piece card shop and Trading card shop in West Hartford, CT · Thousand Sunny Cards</span>
      </div>
    </div>
  </footer>

  <nav class="dock" aria-label="Quick actions">
    <a href="tel:+17573587643">Call</a>
    <a href="https://maps.google.com/?q=Thousand+Sunny+Cards+%26+Collectibles+75+Park+Rd+West+Hartford+CT+06119" target="_blank" rel="noopener">Directions</a>
    <a href="/#visit">Hours</a>
  </nav>
  <script>window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};</script>
  <script defer src="/_vercel/insights/script.js"></script>
  <script src="/assets/js/speed-insights.js" defer></script>
  <script src="/assets/js/main.js?v=36" defer></script>
</body>
</html>
'''

TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(
    f'{head_prefix}  <script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n  </script>\n{body}',
    encoding="utf-8",
)
print(f"Wrote {TARGET.relative_to(ROOT)} with {len(CARDS)} featured cards.")
