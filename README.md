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
one-piece-tcg.html    ← One Piece TCG hub
one-piece-tcg-cards.html ← generated One Piece display-case collection
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

- **`CARD_PHOTOS`** — graded case lightbox
- **`TREASURE_ROAD_EVENTS`** — Catch us on the Road cards, sourced from the
  [@tscc Treasure profile](https://www.ontreasure.com/u/tscc). Treasure does not
  expose a public vendor-events API, so this catalog is the source of truth.
  Add a new object (title, dates, venue, individual Treasure URL, local poster)
  when the shop books another show. Cards whose `endDate` is before today in
  `America/New_York` hide automatically.
- **`HOURS`** — Sunday → Saturday. Today's row highlights automatically.
  Set `closed: true` for a day off.

### One Piece featured-card collection

`/one-piece-tcg/cards` is a static, crawlable collection of cards that have
actually been photographed in the display case. It is deliberately **not** a
live inventory: it does not publish prices, availability, product offers, or
individual product pages. Its source of truth is the verified `CARDS` list in
`scripts/build-one-piece-cards.py`, which uses only the existing One Piece
showcase photography and creates `one-piece-tcg-cards.html`. The Vercel rewrite
in `vercel.json` exposes that generated file at the nested clean URL.

After changing the verified card list, rebuild the static page before committing:

```bash
python3 scripts/build-one-piece-cards.py
```

## Live details

- **Canonical site** — [www.thousandsunnytcg.com](https://www.thousandsunnytcg.com/)
- **Address** — 75 Park Rd, West Hartford, CT 06119
- **Phone / text** — (757) 358-7643
- **Hours** — Mon–Fri 11 AM – 8 PM; Sat & Sun closed (card shows)
- **Instagram** — [@tscc_ct](https://www.instagram.com/tscc_ct/)
- **Facebook** — linked in Visit + footer
- **Vercel project** — `thousand-sunny-cards` (apex + www on thousandsunnytcg.com)

## Page guards

On 2026-09-05 two commits replaced `index.html` with an 11-byte `PLACEHOLDER`
and then a 141-byte `restore-pending` stub. Both claimed in their commit
messages to be restoring the homepage. Both deployed, and the site served a
blank page for three and a half hours while every status-code monitor reported
it healthy — a stub still answers HTTP 200. CI went red on both commits and
that did not stop the deploy.

The deployment contract and four guards now stand between a gutted page and the live site:

| Guard | Runs | Effect |
| --- | --- | --- |
| `scripts/check-deploy-contract.sh` | CI and Vercel, every deploy | Combines page, route, sitemap, and Vercel wiring checks |
| `scripts/check-page-integrity.sh` | CI, every branch and PR | Marks the commit red |
| `scripts/vercel-ignore-build.sh` | Vercel, every deploy | **Refuses the deploy**; the last good one keeps serving |
| `scripts/probe-live-site.sh` | Canary, every 15 min | Fails the workflow when the live body is wrong |
| `scripts/probe-production-endpoints.sh` | Canary, every 15 min | Checks robots, sitemap, verification, and JavaScript endpoints |

All three share one contract in `scripts/lib-page-checks.sh`: a minimum byte
size, a list of must-be-present markers (the address, the phone number, the
structured data, the stylesheet and script wiring), and a list of placeholder
sentinels that must be absent.

The Vercel hook is the one that actually prevents an outage. Its exit codes are
inverted by Vercel's contract — exit 0 skips the build, exit 1 proceeds — so a
failing page exits 0 and the previous deployment stays live.

If a legitimate redesign trips a guard, edit the markers or thresholds in
`scripts/lib-page-checks.sh` in the same commit as the redesign. Do not delete
the guard. To check a page before pushing:

```bash
bash scripts/check-page-integrity.sh      # the files in this repo
bash scripts/check-deploy-contract.sh     # the complete pre-deploy contract
bash scripts/probe-live-site.sh           # what the live site is serving
bash scripts/probe-production-endpoints.sh # discovery and tracking endpoints
SITE_URL=http://localhost:8000 bash scripts/probe-live-site.sh   # a local server
```

The scheduled canary also opens or updates a single `production-canary` GitHub
issue when a check fails, so a production outage is visible without creating a
new duplicate issue every fifteen minutes.

## Deploy

Push to `main`. Vercel project **thousand-sunny-cards** is linked to this repo
and serves production at [www.thousandsunnytcg.com](https://www.thousandsunnytcg.com/).
Apex `thousandsunnytcg.com` and the `*.vercel.app` host redirect to www.
