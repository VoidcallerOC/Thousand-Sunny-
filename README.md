# Thousand Sunny Cards & Collectibles — Website

Official site for **Thousand Sunny Cards & Collectibles** — a trading card,
anime and collectibles shop in **West Hartford, CT**. Pokémon · One Piece TCG ·
Magic · Yu-Gi-Oh · anime figures & statues · Funko Pop! · graded slabs · manga ·
Japanese snacks. _Buy · Sell · Trade · Collect._

Photography-led single page: the Gear 5 greeter in the hero, live open/closed
status, lightbox gallery, and a phone dock for Call / Directions / Hours.

Zero-build static site. No frameworks — just open `index.html`. Hosts anywhere.

```
index.html            ← page markup
assets/
  css/styles.css      ← design system
  js/main.js          ← shelves, hours, lightbox, open-now
  img/logo.png        ← TSCC sun mark
  img/og.jpg          ← social share card
  img/*.jpg           ← store photos
vercel.json           ← clean URLs, host redirects, asset caching
```

## Preview locally

Asset paths are absolute (`/assets/...`), so serve the folder:

```bash
python3 -m http.server 8000
```

## Update content

Edit the blocks at the top of **`assets/js/main.js`**:

- **`GAMES`** — the shelf category tiles
- **`CARD_PHOTOS`** — graded case lightbox
- **`HOURS`** — Sunday → Saturday. Today's row highlights automatically.
  Set `closed: true` for a day off.

## Live details

- **Canonical site** — [www.thousandsunnytcg.com](https://www.thousandsunnytcg.com/)
- **Address** — 75 Park Rd, West Hartford, CT 06119
- **Phone / text** — (757) 358-7643
- **Hours** — Mon–Fri 11 AM – 8 PM; Sat & Sun closed (card shows)
- **Instagram** — [@tscc_ct](https://www.instagram.com/tscc_ct/)
- **Facebook** — linked in Visit + footer
- **Vercel project** — `thousand-sunny-cards` (apex + www on thousandsunnytcg.com)

## Deploy

Push to `main`. Vercel project **thousand-sunny-cards** is linked to this repo
and serves production at [www.thousandsunnytcg.com](https://www.thousandsunnytcg.com/).
Apex `thousandsunnytcg.com` and the `*.vercel.app` host redirect to www.
