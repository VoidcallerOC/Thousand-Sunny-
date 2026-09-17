# Thousand Sunny One Piece TCG SEO Expansion Report

**Date:** September 16, 2026  
**Author:** Manus AI

## Outcome

The site now has a stronger, non-fabricated One Piece TCG topic cluster while preserving the broader local trading-card-shop positioning. The implementation expands the existing One Piece hub, adds a static featured-card collection based only on photographed display-case cards, and reinforces internal links from the homepage. The canonical site and implementation were audited before changes were made. [1]

The repository is a **zero-build static site**. It has no commerce platform, inventory feed, card database, confirmed One Piece event feed, or server-rendered product architecture. The implementation therefore avoids unsupported set, deck, guide, product, and event pages.

## A. Files Changed

| File | Change |
| --- | --- |
| `index.html` | Preserved broad TCG metadata; added a concise, crawlable One Piece TCG section and links to the hub and featured-card collection. |
| `one-piece-tcg.html` | Strengthened page metadata, H1, visible breadcrumbs, Connecticut/local-play language, and contextual card links. |
| `one-piece-tcg-cards.html` | Added generated static source for the featured One Piece display-case card collection. |
| `scripts/build-one-piece-cards.py` | Added source-of-truth generator for the static featured-card page. |
| `assets/css/styles.css` | Added reserved-layout styles for breadcrumbs and the static card grid. |
| `vercel.json` | Added a clean-URL rewrite for `/one-piece-tcg/cards`. |
| `sitemap.xml` | Added the canonical featured-card URL and updated modification dates. |
| `scripts/validate-seo.py` | Expanded checks for all three canonical pages, metadata, JSON-LD, route rewrite, internal links, and image dimensions. |
| `scripts/check-assets.py` | Included the featured-card source in raw-image checks. |
| `scripts/check-page-integrity.sh` and `scripts/lib-page-checks.sh` | Added truncation and marker guards for the generated card page. |
| `scripts/check-deploy-contract.sh` | Added required-file, sitemap, and clean-URL rewrite guards. |
| `scripts/probe-live-site.sh` and `scripts/probe-production-endpoints.sh` | Added the featured-card public route to production monitoring. |
| `scripts/measure-cls.py` | Added the new static source to desktop and mobile layout-shift measurement. |
| `README.md` | Documented the card collection’s data boundary and regeneration workflow. |

## B. Routes Created or Modified

| Public route | Status | Canonical URL | Notes |
| --- | --- | --- | --- |
| `/` | Modified | `https://www.thousandsunnytcg.com/` | Retains broader TCG, Pokémon, and local-shop scope; now contains a crawlable One Piece section. |
| `/one-piece-tcg` | Modified | `https://www.thousandsunnytcg.com/one-piece-tcg` | Remains the authoritative One Piece TCG hub. |
| `/one-piece-tcg/cards` | Created | `https://www.thousandsunnytcg.com/one-piece-tcg/cards` | Clean URL rewrites to the generated static `one-piece-tcg-cards.html` source. |

## C. SEO Changes

The homepage title and social metadata now emphasize Thousand Sunny as a broader West Hartford trading card shop. This retains existing relevance for card-shop, Pokémon, TCG, and local searches. A new visible `One Piece TCG at Thousand Sunny` section naturally establishes the One Piece Card Game, singles, sealed product, starter decks, graded showcase cards, Connecticut, West Hartford, and local play updates without claiming real-time inventory or an unconfirmed tournament schedule.

The One Piece hub now uses the title **“One Piece TCG Cards & Collectibles in Connecticut | Thousand Sunny”** and a matching H1. It has a visible breadcrumb, an explicit featured-card section, and local-play copy that says confirmed details are published only when locked. The page retains its indexable robots directive, canonical URL, Open Graph metadata, Twitter metadata, FAQ content, and contextual store details.

The featured-card page has unique metadata, one H1, a canonical URL, social metadata, a visible breadcrumb, static HTML card entries, and a clear availability disclaimer. It contains no prices, no offers, no stock count, and no claim that the display case is a real-time online catalog.

## D. One Piece Keyword and Topic Architecture

The implemented architecture follows the data that actually exists:

```text
Homepage
└── One Piece TCG hub
    └── Featured One Piece TCG cards
```

The hub naturally covers **One Piece TCG**, **One Piece Card Game**, **One Piece cards**, **One Piece singles**, **sealed product**, **starter decks**, **graded cards**, **Connecticut**, **West Hartford**, **local play**, and **confirmed event updates**. The featured-card page adds a crawlable collection of photographed One Piece display-case cards without presenting them as individual products.

The following route types were intentionally not created: `/one-piece-tcg/sets/`, `/one-piece-tcg/decks/`, `/one-piece-tcg/guides/`, `/one-piece-tcg/events/`, individual card pages, and set-specific pages. The repository has no verified source data to support them, and adding them would create thin or fabricated SEO pages.

## E. Structured-Data Changes

The existing homepage `Store`/`HobbyShop` and `WebSite` data remains in place. Its description was broadened so it accurately represents the full TCG and collectibles business rather than turning the homepage into a One Piece-only page.

The hub keeps its accurate `WebPage`, `BreadcrumbList`, `Store`/`HobbyShop`, `WebSite`, and visible-content-matching `FAQPage` schema. Its WebPage description and topical keywords were improved for One Piece TCG and Connecticut relevance.

The featured-card page adds `WebPage`, `BreadcrumbList`, `ItemList`, `Store`/`HobbyShop`, and `WebSite` entities. The `ItemList` names the nine cards visible in the page’s static HTML. It deliberately does not use `Product`, `Offer`, or `Event` schema because the project does not provide verified price, availability, product, registration, or event-date data.

## F. Internal-Linking Changes

The homepage now links to the One Piece hub and the featured-card collection in the primary navigation, mobile navigation, shelf set list, new One Piece section, and footer. The hub links to the featured-card collection in its navigation, mobile navigation, content section, and footer. The collection links back to the hub, homepage, store event board, sell/trade flow, and visit information.

These links use varied descriptive anchors, including “Explore One Piece TCG,” “View featured One Piece cards,” and “Featured One Piece TCG cards.” The result is a clear internal path from the general local shop page to the authoritative hub and then to real, photographed card content.

## G. Sitemap and Robots Changes

`robots.txt` remains indexable and still declares the canonical sitemap. The sitemap now lists exactly the homepage, the One Piece hub, and the featured-card collection. The generated cards source is exposed at its canonical nested URL through an explicit Vercel rewrite, which is guarded by the deployment and SEO validators.

## H. Performance and CLS Verification

The recent layout-stability safeguards were audited before modification. The existing deferred `initPage()` behavior in `assets/js/main.js` was left intact. No new SEO body content is injected after first paint: the hub, homepage section, and featured-card entries are all static HTML.

The critical CSS itself was not changed. The stylesheet cache version was deliberately advanced from `v=36` to `v=37` on all three canonical pages, keeping the asynchronous stylesheet preload and no-JavaScript fallback in lockstep. The new card grid reserves media space with CSS aspect ratios and explicit image width and height attributes. Its below-the-fold card images are lazy loaded.

`python3 scripts/measure-cls.py` recorded **0 CLS** with no layout-shift entries for the homepage, One Piece hub, and featured-card source at both 1365×900 and 390×844 viewports.

## I. Build and Test Results

The site has no compiled production build because it is a zero-build static site. The complete available validation suite passed:

```text
bash scripts/check-page-integrity.sh      PASS
bash scripts/check-deploy-contract.sh     PASS
python3 scripts/validate-seo.py           PASS
python3 scripts/check-assets.py           PASS
npm test                                  PASS
python3 scripts/measure-cls.py            PASS — six zero-CLS measurements
git diff --check                          PASS
```

The local static source pages returned HTTP 200, and the featured-card page contained nine static card entries, a unique title, a canonical URL, and an H1. The Vercel configuration rewrite is also validated automatically. A local `vercel dev` route test could not be run because the CLI requested a separate unauthenticated Vercel login; no credentials or deployment settings were changed.

## J. Items Not Implemented Because the Data Model Does Not Support Them

The project does not contain a real inventory source, product identifiers, prices, availability, a set catalog, deck data, a guide library, confirmed One Piece event records, or individual product pages. Therefore it does not support truthful product pages, individual card pages, OP17/OP16/OP15 set pages, deck pages, event landing pages, Product schema, Offer schema, or Event schema. The implementation intentionally avoids claims that could not be verified from the site’s existing data.

## K. Remaining SEO Opportunities

The strongest next step is to add a maintained, verified source of truth for inventory and events. Once the store has real card, set, price, availability, and event fields, it can publish static or server-rendered pages for only those real entities. Confirmed One Piece events could then include visible dates, formats, location, registration URLs, and valid Event schema.

A future inventory model should distinguish display-case photography from sellable listings and should preserve the same static or server-rendered crawlability used here. It should not expose a page until it has a durable canonical URL, a descriptive unique title, visible page content, and supporting data for every schema field.

## References

[1]: https://www.thousandsunnytcg.com/ "Thousand Sunny Cards & Collectibles"
