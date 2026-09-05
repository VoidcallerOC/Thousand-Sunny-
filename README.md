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

## Page guards

On 2026-09-05 two commits replaced `index.html` with an 11-byte `PLACEHOLDER`
and then a 141-byte `restore-pending` stub. Both claimed in their commit
messages to be restoring the homepage. Both deployed, and the site served a
blank page for three and a half hours while every status-code monitor reported
it healthy — a stub still answers HTTP 200. CI went red on both commits and
that did not stop the deploy.

Three guards now stand between a gutted page and the live site:

| Guard | Runs | Effect |
| --- | --- | --- |
| `scripts/check-page-integrity.sh` | CI, every branch and PR | Marks the commit red |
| `scripts/vercel-ignore-build.sh` | Vercel, every deploy | **Refuses the deploy**; the last good one keeps serving |
| `scripts/probe-live-site.sh` | Canary, every 15 min | Fails the workflow when the live body is wrong |

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
bash scripts/probe-live-site.sh           # what the live site is serving
SITE_URL=http://localhost:8000 bash scripts/probe-live-site.sh   # a local server
```

## Deploy

Push to `main`. Vercel project **thousand-sunny-cards** is linked to this repo
and serves production at [www.thousandsunnytcg.com](https://www.thousandsunnytcg.com/).
Apex `thousandsunnytcg.com` and the `*.vercel.app` host redirect to www.
