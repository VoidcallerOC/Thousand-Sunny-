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

## ⚓ Before launch — fill in the real business details

The following were seeded as **placeholders** and must be confirmed/replaced
(search the files for each):

- **Address** — `index.html`, the `data-todo="address"` contact row and the
  `LocalBusiness` structured-data block (currently "Connecticut" only).
- **Phone** — `index.html`, the `data-todo="phone"` contact row (add a real
  `tel:` link) and the structured data.
- **Hours** — `assets/js/main.js` `HOURS` (seeded, not confirmed).
- **Social links** — `index.html` uses `@thousandsunnycards` on Instagram and
  Facebook as placeholders; point them at the real profiles (search for
  `thousandsunnycards`).
- **Domain** — `index.html` canonical/OG URLs use `thousandsunnycards.com`;
  update if the real domain differs.

Optionally add a Google Maps embed to the Visit section once the address is set
(see The Stronghold's `index.html` `.map-embed` block for the pattern).

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
