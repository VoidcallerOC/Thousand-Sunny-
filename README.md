# Thousand Sunny Cards & Collectibles — Website

The official single-page site for **Thousand Sunny Cards & Collectibles** — a
trading card, anime and collectibles shop in **Connecticut**. Pokémon · One
Piece TCG · Magic · Yu-Gi-Oh · anime figures & statues · Funko Pop! · graded
slabs · manga · Japanese snacks. _Buy · Sell · Trade · Collect._

Forked from the same zero-build template family as **Hard Hittin' Cards** and
**The Stronghold**, re-themed for the Sunny crew: violet-black + **Sunny gold**
(`#F5B301`), with the shop's real logo and interior photos.

A fast, fully interactive, **zero-build** static site. No frameworks, no
compile step — just open `index.html`. That means it hosts anywhere and stays
easy to update for years.

```
index.html            ← page markup & content
assets/
  css/styles.css      ← all styling / design system
  js/main.js          ← interactions + EDITABLE content (shelves, hours)
  img/logo.png        ← Thousand Sunny (TSCC) logo mark
  img/favicon.png     ← browser tab icon
  img/*.jpg           ← store photos used in the gallery, Play & the case
vercel.json           ← deploy config (clean URLs + long-lived asset caching)
```

## Preview it locally

Because the asset paths are absolute (`/assets/...`), run a tiny local server
rather than double-clicking the file:

```bash
# from this folder — pick whichever you have
python3 -m http.server 8000      # → http://localhost:8000
# or
npx serve .
```

## Update the content (no coding needed)

Open **`assets/js/main.js`** and edit the blocks at the top:

- **`GAMES`** — the "Cards, Anime & Collectibles" cards on the shelf.
- **`HOURS`** — store hours, Sunday → Saturday. Times are the pretty labels;
  the row for today auto-highlights. Set `closed: true` for a day off.

## Business details (live on the site)

- **Address** — 75 Park Rd, West Hartford, CT 06119 (contact row, Google Maps
  embed, and `LocalBusiness` structured data).
- **Phone / text** — (757) 358-7643.
- **Hours** — Mon–Fri 11 AM – 8 PM; Sat & Sun closed (out at card shows). Edit
  in `assets/js/main.js` `HOURS`.
- **Instagram** — [@tscc_ct](https://www.instagram.com/tscc_ct/).
- **Facebook** — linked in the Visit contact block and footer.

### ⚓ Still to confirm before launch

- **Domain** — `index.html` canonical/OG URLs use `thousandsunnycards.com` as a
  placeholder; update to the real domain (search for `thousandsunnycards.com`).

## Deploy to Vercel

- Import the repo at [vercel.com/new](https://vercel.com/new), or run
  `npx vercel`. No build step or framework preset needed — it's static.
  `vercel.json` is included.
- Point the shop's domain at the Vercel project.

Any other static host works too (Netlify, GitHub Pages, Cloudflare Pages).

## Notes

- Fonts (Anton / Oswald / Inter) load from Google Fonts. To go fully offline,
  self-host them and swap the `<link>` in `index.html`.
- Respects `prefers-reduced-motion` and is fully keyboard-navigable.
- Includes SEO meta tags, Open Graph, and LocalBusiness structured data.
- Store photos and the logo are optimized for the web; originals live in the
  shop's shared drive.
