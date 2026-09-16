const CARD_PHOTOS = [
  { src: "/assets/img/collectibles/card-2229-c1.jpg", alt: "PSA 10 Raikou V card from Crown Zenith", caption: "Raikou V · PSA 10", tag: "Crown Zenith", w: 852, h: 1540, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2231-c1.jpg", alt: "PSA 10 Suicune V card from Crown Zenith", caption: "Suicune V · PSA 10", tag: "Crown Zenith", w: 906, h: 1552, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2230-c1.jpg", alt: "PSA 10 Entei V card from Crown Zenith", caption: "Entei V · PSA 10", tag: "Crown Zenith", w: 882, h: 1633, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2219-c1.jpg", alt: "Beckett graded Monkey D. Luffy trading card", caption: "Monkey D. Luffy · BGS 10", tag: "One Piece", w: 859, h: 1635, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2218-c1.jpg", alt: "PSA graded Majin Buu Kid trading card", caption: "Majin Buu Kid · PSA 10", tag: "Dragon Ball", w: 884, h: 1661, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2217-c2.jpg", alt: "PSA graded Gogeta trading card", caption: "Gogeta · PSA 10", tag: "Dragon Ball", w: 857, h: 1673, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2220-c1.jpg", alt: "Pristine 10 Monkey D. Luffy One Piece card", caption: "Monkey D. Luffy · Pristine 10", tag: "One Piece", w: 956, h: 1673, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2222-c1.jpg", alt: "Monkey D. Luffy One Piece card", caption: "Monkey D. Luffy", tag: "One Piece", w: 786, h: 1410, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2223-c1.jpg", alt: "Shanks One Piece card", caption: "Shanks", tag: "One Piece", w: 792, h: 1422, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2227-c1.jpg", alt: "Nami One Piece card", caption: "Nami", tag: "One Piece", w: 984, h: 1403, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2286-c2.jpg", alt: "Pristine 10 Gear Two One Piece card in Beckett slab", caption: "Gear Two · Pristine 10", tag: "One Piece", w: 832, h: 1602, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2285-c1.jpg", alt: "Pristine 10 Monkey D. Luffy SP One Piece card in Beckett slab", caption: "Monkey D. Luffy SP · Pristine 10", tag: "One Piece", w: 832, h: 1584, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2283-c2.jpg", alt: "Pristine 10 Portgas D. Ace Manga Art One Piece card in Beckett slab", caption: "Portgas D. Ace · Pristine 10", tag: "One Piece", w: 1024, h: 1649, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2284-c3.jpg", alt: "PSA 10 Boa Hancock Manga Alternate Art One Piece card", caption: "Boa Hancock · PSA 10", tag: "One Piece", w: 880, h: 1611, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2224-c2.jpg", alt: "Lugia V Pokémon card", caption: "Lugia V", tag: "Pokémon", w: 848, h: 1451, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2225-c2.jpg", alt: "Espeon GX Pokémon card", caption: "Espeon GX", tag: "Pokémon", w: 860, h: 1484, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2226-c2.jpg", alt: "Flareon ex Pokémon card", caption: "Flareon ex", tag: "Pokémon", w: 834, h: 1456, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2221-c4.jpg", alt: "Reshiram EX Pokémon card", caption: "Reshiram EX", tag: "Pokémon", w: 754, h: 1330, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2213-c1.jpg", alt: "Zed From the Shadows Riftbound card", caption: "Zed · From the Shadows", tag: "Riftbound", w: 714, h: 1246, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2214-c1.jpg", alt: "Blind Monk Riftbound card", caption: "Blind Monk", tag: "Riftbound", w: 964, h: 1388, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2215-c1.jpg", alt: "Deceiver Riftbound card", caption: "Deceiver", tag: "Riftbound", w: 725, h: 1321, widths: [320, 640, 960] },
  { src: "/assets/img/collectibles/card-2216-c1.jpg", alt: "Blind Monk Riftbound card with dragon artwork", caption: "Blind Monk · Alt Art", tag: "Riftbound", w: 858, h: 1505, widths: [320, 640, 960] },
];

// Treasure @tscc road shows. No public vendor-events API — add a row here; cards filter by endDate (America/New_York calendar day).
const TREASURE_ROAD_EVENTS = [
  {
    slug: "northeast-sports-card-expo-connecticut-09122026",
    url: "https://www.ontreasure.com/events/northeast-sports-card-expo-connecticut-09122026",
    title: "Northeast Sports Card Expo: Connecticut",
    dateLabel: "Sat, Sep 12 – Sun, Sep 13",
    location: "Stamford, CT",
    startDate: "2026-09-12",
    endDate: "2026-09-13",
    poster: "/assets/img/events/northeast-sports-card-expo-connecticut.jpg",
    posterFallback: "https://qkdlfshzugzeqlznyqfv.supabase.co/storage/v1/object/public/posters/posters1787581346598",
    posterAlt: "Northeast Sports Card Expo: Connecticut event poster",
  },
  {
    slug: "glitch-collectibles-tcg-show-09272026",
    url: "https://www.ontreasure.com/events/glitch-collectibles-tcg-show-09272026",
    title: "Glitch Collectibles TCG Show - September 2026",
    dateLabel: "Sun, Sep 27 · 9 AM – 2 PM",
    location: "White's of Westport · Westport, MA",
    startDate: "2026-09-27",
    endDate: "2026-09-27",
    poster: "/assets/img/events/glitch-collectibles-tcg-show.jpg",
    posterFallback: "https://qkdlfshzugzeqlznyqfv.supabase.co/storage/v1/object/public/posters/posters1785352595624",
    posterAlt: "Glitch Collectibles TCG Show September 2026 event poster",
  },
  {
    slug: "collex-cards-collectibles-ll-10102026",
    url: "https://www.ontreasure.com/events/collex-cards-collectibles-ll-10102026",
    title: "ColleX Cards & Collectibles ll",
    dateLabel: "Sat, Oct 10",
    location: "Wallingford, CT",
    startDate: "2026-10-10",
    endDate: "2026-10-10",
    poster: "/assets/img/events/collex-cards-collectibles.jpg",
    posterFallback: "https://qkdlfshzugzeqlznyqfv.supabase.co/storage/v1/object/public/posters/posters1788382527916",
    posterAlt: "ColleX Cards and Collectibles event poster",
  },
  {
    slug: "hard-hittin-card-shows-at-foxwoods-casino-10172026",
    url: "https://www.ontreasure.com/events/hard-hittin-card-shows-at-foxwoods-casino-10172026",
    title: "Hard Hittin' Card Shows at FOXWOODS CASINO",
    dateLabel: "Sat, Oct 17 – Sun, Oct 18",
    location: "Mashantucket, CT",
    startDate: "2026-10-17",
    endDate: "2026-10-18",
    poster: "/assets/img/events/hard-hittin-foxwoods.jpg",
    posterFallback: "https://qkdlfshzugzeqlznyqfv.supabase.co/storage/v1/object/public/posters/posters1787710241358",
    posterAlt: "Hard Hittin' Card Shows at FOXWOODS CASINO event poster",
  },
  {
    slug: "the151cardshow-halloween-bash-10312026",
    url: "https://www.ontreasure.com/events/the151cardshow-halloween-bash-10312026",
    title: "The151CardShow - HALLOWEEN BASH",
    dateLabel: "Sat, Oct 31",
    location: "Vale Fieldhouse · Middletown, CT",
    startDate: "2026-10-31",
    endDate: "2026-10-31",
    poster: "/assets/img/events/the151cardshow-halloween-bash.jpg",
    posterFallback: "https://qkdlfshzugzeqlznyqfv.supabase.co/storage/v1/object/public/posters/posters1787089877141",
    posterAlt: "The151CardShow HALLOWEEN BASH event poster",
  },
];

const HOURS = [
  { day: "Sunday", closed: true },
  { day: "Monday", open: "11:00 AM", close: "8:00 PM", openMin: 11 * 60, closeMin: 20 * 60 },
  { day: "Tuesday", open: "11:00 AM", close: "8:00 PM", openMin: 11 * 60, closeMin: 20 * 60 },
  { day: "Wednesday", open: "11:00 AM", close: "8:00 PM", openMin: 11 * 60, closeMin: 20 * 60 },
  { day: "Thursday", open: "11:00 AM", close: "8:00 PM", openMin: 11 * 60, closeMin: 20 * 60 },
  { day: "Friday", open: "11:00 AM", close: "8:00 PM", openMin: 11 * 60, closeMin: 20 * 60 },
  { day: "Saturday", closed: true },
];

const PHOTOS = [
  { src: "/assets/img/store-figures.jpg", alt: "Store floor with anime figure shelves, board games and manga against purple walls", caption: "Figures, statues, board games & manga", w: 1350, h: 1800, widths: [480, 768, 1350] },
  { src: "/assets/img/gallery-figures.jpg", alt: "Tall shelves packed with One Piece and anime figures and Funko Pops", caption: "Walls of anime figures & Pops", w: 1150, h: 1331, widths: [480, 768, 1150] },
  { src: "/assets/img/gallery-art.jpg", alt: "Framed anime wall art and boxed figures on wooden shelves", caption: "Framed art & boxed collectibles", w: 1170, h: 1412, widths: [480, 768, 1170] },
  { src: "/assets/img/gallery-merch.jpg", alt: "Anime tumblers, wall scrolls and a One Piece board game on display", caption: "Tumblers, scrolls & merch", w: 1170, h: 1389, widths: [480, 768, 1170] },
  { src: "/assets/img/store-counter.jpg", alt: "Front counter with Japanese candy, lollipops, drink fridges and a neon star sign", caption: "Snacks, drinks & the neon out front", w: 1300, h: 1733, widths: [480, 768, 1300], wide: true },
  { src: "/assets/img/play-hall.jpg", alt: "Long communal wooden table with chairs running through the store", caption: "The communal table", w: 1169, h: 1396, widths: [480, 768, 1169] },
  { src: "/assets/img/event-room.jpg", alt: "Event room with a long table, chairs and figure shelves", caption: "Room for the whole crew", w: 1168, h: 1387, widths: [480, 768, 1168] },
  { src: "/assets/img/play-room.jpg", alt: "Private play room with a Luffy poster, TV and purple accent wall", caption: "Private room + big screen", w: 1168, h: 1389, widths: [480, 768, 1168] },
  { src: "/assets/img/store-case.jpg", alt: "Glass display case of graded Pokémon and One Piece cards and collectibles", caption: "Graded slabs & grails", w: 1200, h: 1600, widths: [480, 768, 1200] },
  { src: "/assets/img/store-overview-1.jpg", alt: "Wide view across the Thousand Sunny Cards and Collectibles store", caption: "A full look around the shop", w: 1920, h: 1440, widths: [640, 960, 1440], wide: true },
  { src: "/assets/img/store-overview-2.jpg", alt: "Overview of display cases, figures, cards, and collectibles inside Thousand Sunny", caption: "Cards, figures & collectibles throughout", w: 1920, h: 1440, widths: [640, 960, 1440], wide: true },
  { src: "/assets/img/store-gear5-statue-2026.jpg", alt: "Seated Gear 5 Luffy statue inside Thousand Sunny Cards and Collectibles", caption: "Gear 5 Luffy statue", w: 1440, h: 1920, widths: [480, 768, 1152] },
  { src: "/assets/img/store-collectible-displays-2026.jpg", alt: "Collectible display shelves and illuminated anime artwork inside Thousand Sunny", caption: "Collectible displays around the shop", w: 1440, h: 1920, widths: [480, 768, 1152] },
  { src: "/assets/img/store-shelf-wall-2026.jpg", alt: "Purple feature wall with shelves of anime and One Piece collectible boxes", caption: "Collectible lighting & shelf wall", w: 1440, h: 1920, widths: [480, 768, 1152] },
  { src: "/assets/img/storefront-sign-close-2026.jpg", alt: "Thousand Sunny Cards and Collectibles exterior storefront sign", caption: "The Thousand Sunny sign", w: 1440, h: 1920, widths: [480, 768, 1152] },
  { src: "/assets/img/storefront-sign-wide-2026.jpg", alt: "Exterior view of the Thousand Sunny Cards and Collectibles sign at 75 Park Road", caption: "Find us on Park Road", w: 1440, h: 1920, widths: [480, 768, 1152] },
];

const $ = (s, c = document) => c.querySelector(s);
const $$ = (s, c = document) => [...c.querySelectorAll(s)];

function track(name, data = {}) {
  if (typeof window.va === "function") window.va("event", { name, data });
}

function initAnalytics() {
  $$('a[href^="tel:"]').forEach((link) => link.addEventListener("click", () => track("call_click")));
  $$('a[href*="maps.google.com"]').forEach((link) => link.addEventListener("click", () => track("directions_click")));
  $$('a[href*="instagram.com"], a[href*="facebook.com"]').forEach((link) => link.addEventListener("click", () => track("social_click")));
  $$('a[href*="ontreasure.com"]').forEach((link) => link.addEventListener("click", () => track("treasure_link_click")));
  $$('a[href^="sms:"]').forEach((link) => link.addEventListener("click", () => track("text_click")));
  $("#offerForm")?.addEventListener("submit", () => track("offer_started"));
}

function imageBust(src, bust = "") {
  if (bust) return bust;
  return src.includes("/collectibles/") ? "4" : "";
}

function responsiveSrcset(src, widths, extension, bust = "") {
  const stem = src.split("/").pop().replace(/\.jpg$/i, "");
  const q = imageBust(src, bust) ? `?v=${imageBust(src, bust)}` : "";
  return widths.map((width) => `/assets/img/optimized/${stem}-${width}.${extension}${q} ${width}w`).join(", ");
}

function responsiveImage({ src, widths, sizes, alt = "", width, height, className = "", loading = "lazy", decoding = "async", fetchPriority = "", bust = "" }) {
  const classAttr = className ? ` class="${className}"` : "";
  const loadingAttr = loading ? ` loading="${loading}"` : "";
  const fetchPriorityAttr = fetchPriority ? ` fetchpriority="${fetchPriority}"` : "";
  const q = imageBust(src, bust) ? `?v=${imageBust(src, bust)}` : "";
  return `<picture class="responsive-picture">
    <source type="image/avif" srcset="${responsiveSrcset(src, widths, "avif", bust)}" sizes="${sizes}" />
    <source type="image/webp" srcset="${responsiveSrcset(src, widths, "webp", bust)}" sizes="${sizes}" />
    <img${classAttr} src="${src}${q}" alt="${alt}" width="${width}" height="${height}" sizes="${sizes}"${loadingAttr} decoding="${decoding}"${fetchPriorityAttr} />
  </picture>`;
}
const DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const REDUCE = matchMedia("(prefers-reduced-motion: reduce)").matches;
const FINE = matchMedia("(hover: hover) and (pointer: fine)").matches;
const DESKTOP_SCROLL_FX = FINE && matchMedia("(min-width: 768px)").matches;
const HERO_SCROLL_FX = DESKTOP_SCROLL_FX;
const SCROLL_REVEAL_FX = DESKTOP_SCROLL_FX;

function easternNow() {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/New_York",
    weekday: "long",
    hour: "numeric",
    minute: "numeric",
    hourCycle: "h23",
  }).formatToParts(new Date());
  const pick = (t) => parts.find((p) => p.type === t)?.value ?? "";
  const dayIndex = Math.max(0, DAYS.indexOf(pick("weekday")));
  return { dayIndex, nowMin: Number(pick("hour")) * 60 + Number(pick("minute")) };
}

function easternTodayISO() {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: "America/New_York",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(new Date());
}

function escapeHTML(value) {
  return String(value)
    .replace(/&/g, "\u0026amp;")
    .replace(/</g, "\u0026lt;")
    .replace(/>/g, "\u0026gt;")
    .replace(/"/g, "\u0026quot;");
}

function upcomingTreasureRoadEvents() {
  const today = easternTodayISO();
  return TREASURE_ROAD_EVENTS
    .filter((event) => event.endDate >= today)
    .sort((a, b) => a.startDate.localeCompare(b.startDate) || a.endDate.localeCompare(b.endDate));
}

function roadEventCardHTML(event, index) {
  const n = String(index + 1).padStart(2, "0");
  const title = escapeHTML(event.title);
  return `<a class="event-card" href="${escapeHTML(event.url)}" target="_blank" rel="noopener" aria-label="${escapeHTML(`Open ${event.title} on Treasure`)}">
    <div class="event-card-header"><span class="event-card-number">${n} <i aria-hidden="true">/</i> ON THE ROAD</span><span class="event-card-date">${escapeHTML(event.dateLabel)}</span><h3>${title}</h3><span class="event-card-location">${escapeHTML(event.location)}</span></div>
    <img class="event-card-poster" src="${escapeHTML(event.poster)}" alt="${escapeHTML(event.posterAlt)}" width="800" height="800" loading="lazy" decoding="async" data-fallback="${escapeHTML(event.posterFallback)}" />
    <span class="event-card-footer"><span>View event on Treasure</span><span aria-hidden="true">↗</span></span>
  </a>`;
}

function renderRoadEvents() {
  const grid = $("#roadEventGrid");
  const nextTitle = $("#roadNextTitle");
  const nextDetail = $("#roadNextDetail");
  const upcoming = upcomingTreasureRoadEvents();

  if (nextTitle && nextDetail) {
    if (upcoming.length) {
      const next = upcoming[0];
      nextTitle.textContent = next.title;
      nextDetail.textContent = `${next.dateLabel} · ${next.location}`;
    } else {
      nextTitle.textContent = "No upcoming shows on the board";
      nextDetail.textContent = "Check Treasure for the latest @tscc table details.";
    }
  }

  if (!grid) return;

  if (!upcoming.length) {
    grid.innerHTML = `<div class="event-empty"><span class="event-no">00</span><div><h3>No upcoming road shows posted</h3><p>When the next Treasure date is booked it will land here from the @tscc catalog.</p></div></div>`;
    return;
  }

  grid.innerHTML = upcoming.map(roadEventCardHTML).join("");
  grid.querySelectorAll("img.event-card-poster[data-fallback]").forEach((img) => {
    img.addEventListener("error", () => {
      const fallback = img.getAttribute("data-fallback");
      if (fallback && img.getAttribute("src") !== fallback) img.setAttribute("src", fallback);
    });
  });
}

function nextOpenDay(from) {
  for (let i = 1; i <= 7; i++) {
    const row = HOURS[(from + i) % 7];
    if (!row.closed) return row.day;
  }
  return "Monday";
}

function getStatus() {
  const { dayIndex, nowMin } = easternNow();
  const today = HOURS[dayIndex];
  if (!today.closed && nowMin >= today.openMin && nowMin < today.closeMin) {
    const remaining = today.closeMin - nowMin;
    return {
      open: true,
      dayIndex,
      nowMin,
      label: "Open now",
      detail: remaining <= 60 ? `Closes in ${remaining} min` : "Closes at 8:00 PM",
    };
  }
  if (today.closed) {
    return { open: false, dayIndex, nowMin, label: "Closed today", detail: "Weekends we're at the card shows" };
  }
  if (!today.closed && nowMin < today.openMin) {
    return { open: false, dayIndex, nowMin, label: "Closed", detail: "Opens today at 11:00 AM" };
  }
  return { open: false, dayIndex, nowMin, label: "Closed", detail: `Opens ${nextOpenDay(dayIndex)} at 11:00 AM` };
}

function renderBadge(el, status) {
  const compact = el.hasAttribute("data-compact");
  el.classList.toggle("is-open", status.open);
  el.innerHTML = `<span class="dot"></span><span class="label">${status.label}</span>${
    compact ? "" : `<span class="detail">· ${status.detail}</span>`
  }`;
}

function collectibleHTML(card, index) {
  const className = ["collectible-card", card.landscape ? "collectible-card--landscape" : ""].filter(Boolean).join(" ");
  return `<button class="${className}" type="button" data-card-photo="${index}" data-tilt aria-label="View ${card.caption}">
    <span class="collectible-card__media">${responsiveImage({ src: card.src, widths: card.widths, sizes: "(min-width: 960px) 25vw, (min-width: 640px) 50vw, 50vw", alt: card.alt, width: card.w, height: card.h, className: "collectible-card__image", loading: "lazy", bust: "4" })}</span>
    <span class="collectible-card__meta"><span>${card.tag}</span><strong>${card.caption}</strong></span>
  </button>`;
}

function renderGames() {
  const grid = $("#gamesGrid");
  if (!grid) return;
  grid.innerHTML = CARD_PHOTOS.map((card, index) => collectibleHTML(card, index)).join("");
}

function renderHours(status) {
  const list = $("#hoursList");
  if (!list) return;
  list.innerHTML = HOURS.map((h, i) => {
    const time = h.closed ? "Closed" : `${h.open} – ${h.close}`;
    return `<li class="${i === status.dayIndex ? "today" : ""}"><span class="d">${h.day}</span><span class="t">${time}</span></li>`;
  }).join("");
}

function renderClock(status) {
  const clock = $("#clock");
  if (clock) {
    const time = new Intl.DateTimeFormat("en-US", {
      timeZone: "America/New_York",
      hour: "numeric",
      minute: "2-digit",
    }).format(new Date());
    clock.textContent = `${time} in West Hartford`;
  }
  const meter = $("#dayMeter");
  if (!meter) return;
  const today = HOURS[status.dayIndex];
  if (!status.open || today.closed) {
    meter.hidden = true;
    return;
  }
  const span = today.closeMin - today.openMin;
  const pct = Math.min(100, Math.max(0, ((status.nowMin - today.openMin) / span) * 100));
  meter.hidden = false;
  meter.firstElementChild.style.setProperty("--m", `${pct}%`);
  meter.firstElementChild.style.width = `${pct}%`;
}

function shot(i, extra = "") {
  const p = PHOTOS[i];
  const cls = ["shot", extra, p.wide ? "shot--wide" : "", p.top ? "shot--top" : ""].filter(Boolean).join(" ");
  return `<button class="${cls}" type="button" data-photo="${i}">
    ${responsiveImage({ src: p.src, widths: p.widths, sizes: "(min-width: 1200px) 600px, (min-width: 768px) 50vw, 100vw", alt: p.alt, width: p.w, height: p.h })}
    <span class="gleam" aria-hidden="true"></span>
    <span>${p.caption}</span>
  </button>`;
}

function renderGalleries() {
  const gallery = $("#gallery");
  const play = $("#playGrid");
  if (gallery) gallery.innerHTML = [9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 4, 3].map((i) => shot(i)).join("");
  if (play) play.innerHTML = [5, 6, 7].map((i) => shot(i)).join("");
}

function initNav() {
  const nav = $("#nav");
  const onScroll = () => nav.classList.toggle("scrolled", window.scrollY > 16);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  const menu = $("#navMenu");
  const toggle = $("#navToggle");
  const closeBtn = $("#navClose");
  const open = () => {
    menu.hidden = false;
    toggle.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
  };
  const close = () => {
    menu.hidden = true;
    toggle.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  };
  toggle?.addEventListener("click", () => (menu.hidden ? open() : close()));
  closeBtn?.addEventListener("click", close);
  menu?.addEventListener("click", (e) => { if (e.target === menu) close(); });
  $$("#navMenu a").forEach((a) => a.addEventListener("click", close));
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
}

function initLightbox() {
  const dialog = $("#lightbox");
  const avif = $("#lightboxAvif");
  const webp = $("#lightboxWebp");
  const img = $("#lightboxImg");
  const cap = $("#lightboxCap");
  const count = $("#lightboxCount");
  const strip = $("#lightboxStrip");
  if (!dialog) return;
  let items = PHOTOS;
  let index = 0;
  let startX = 0;

  const renderStrip = () => {
    if (!strip) return;
    strip.innerHTML = items.map(
      (p, i) => `<button type="button" data-jump="${i}" aria-label="${p.caption}"><img src="/assets/img/optimized/${p.src.split("/").pop().replace(/\.jpg$/i, "")}-${p.widths[0]}.webp${imageBust(p.src) ? `?v=${imageBust(p.src)}` : ""}" alt="" width="56" height="72" loading="lazy" decoding="async"></button>`,
    ).join("");
  };

  const show = (i) => {
    index = (i + items.length) % items.length;
    const p = items[index];
    avif.srcset = responsiveSrcset(p.src, p.widths, "avif");
    webp.srcset = responsiveSrcset(p.src, p.widths, "webp");
    img.sizes = "100vw";
    img.src = imageBust(p.src) ? `${p.src}?v=${imageBust(p.src)}` : p.src;
    img.alt = p.alt;
    cap.textContent = p.caption;
    if (count) count.textContent = `${index + 1} / ${items.length}`;
    strip?.querySelectorAll("button").forEach((b, n) => b.classList.toggle("is-on", n === index));
    if (!dialog.open) dialog.showModal();
  };

  const open = (nextItems, nextIndex) => {
    items = nextItems;
    renderStrip();
    show(nextIndex);
  };

  document.addEventListener("click", (e) => {
    const jump = e.target.closest("[data-jump]");
    if (jump && dialog.contains(jump)) {
      show(Number(jump.dataset.jump));
      return;
    }
    const btn = e.target.closest("[data-photo], [data-card-photo]");
    if (btn) open(btn.hasAttribute("data-card-photo") ? CARD_PHOTOS : PHOTOS, Number(btn.dataset.cardPhoto ?? btn.dataset.photo));
  });
  dialog.querySelector("[data-close]")?.addEventListener("click", () => dialog.close());
  dialog.querySelector("[data-prev]")?.addEventListener("click", () => show(index - 1));
  dialog.querySelector("[data-next]")?.addEventListener("click", () => show(index + 1));
  dialog.addEventListener("click", (e) => { if (e.target === dialog) dialog.close(); });
  dialog.addEventListener("touchstart", (e) => { startX = e.changedTouches[0].clientX; }, { passive: true });
  dialog.addEventListener("touchend", (e) => {
    const dx = e.changedTouches[0].clientX - startX;
    if (dx > 48) show(index - 1);
    if (dx < -48) show(index + 1);
  }, { passive: true });
  document.addEventListener("keydown", (e) => {
    if (!dialog.open) return;
    if (e.key === "ArrowLeft") show(index - 1);
    if (e.key === "ArrowRight") show(index + 1);
  });
}

function bindTilt(scope = document) {
  if (REDUCE || !FINE) return;
  $$("[data-tilt]", scope).forEach((el) => {
    if (el.dataset.tiltBound) return;
    el.dataset.tiltBound = "1";
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width;
      const y = (e.clientY - r.top) / r.height;
      el.style.setProperty("--px", x.toFixed(3));
      el.style.setProperty("--py", y.toFixed(3));
      el.style.setProperty("--ry", `${((x - 0.5) * 14).toFixed(2)}deg`);
      el.style.setProperty("--rx", `${((0.5 - y) * 10).toFixed(2)}deg`);
      el.classList.add("is-lit");
    });
    el.addEventListener("pointerleave", () => {
      el.style.setProperty("--ry", "0deg");
      el.style.setProperty("--rx", "0deg");
      el.classList.remove("is-lit");
    });
  });
}

function initTilt() {
  bindTilt();
}

function initMagnetic() {
  if (REDUCE || !FINE) return;
  $$("[data-magnetic]").forEach((el) => {
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      const dx = e.clientX - (r.left + r.width / 2);
      const dy = e.clientY - (r.top + r.height / 2);
      el.style.transform = `translate(${dx * 0.22}px, ${dy * 0.28}px)`;
    });
    el.addEventListener("pointerleave", () => { el.style.transform = ""; });
  });
}

function initScrollFx() {
  const sprog = $("#sprog");
  if (!sprog) return;

  const tick = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    const p = max > 0 ? Math.min(1, scrollY / max) : 0;
    sprog.style.setProperty("--p", `${(p * 100).toFixed(2)}%`);
  };

  tick();
  window.addEventListener("scroll", tick, { passive: true });
}

function initReveal() {
  const nodes = $$(".reveal");
  if (!nodes.length) return;
  if (REDUCE || !SCROLL_REVEAL_FX || !("IntersectionObserver" in window)) {
    nodes.forEach((n) => n.classList.add("is-in"));
    return;
  }
  document.documentElement.classList.add("reveal-ready");
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          en.target.classList.add("is-in");
          io.unobserve(en.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -8% 0px" },
  );
  nodes.forEach((n) => io.observe(n));
}

function initCopy() {
  const toast = $("#toast");
  let hide;
  const ping = (msg) => {
    if (!toast) return;
    toast.textContent = msg;
    toast.hidden = false;
    requestAnimationFrame(() => toast.classList.add("is-on"));
    clearTimeout(hide);
    hide = setTimeout(() => {
      toast.classList.remove("is-on");
      setTimeout(() => { toast.hidden = true; }, 280);
    }, 1800);
  };
  $$("[data-copy]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const text = btn.getAttribute("data-copy") || "";
      try {
        await navigator.clipboard.writeText(text);
        ping("Address copied");
      } catch {
        ping("Copy from the listing");
      }
    });
  });
}

function initEaster() {
  const sun = $("#sunMark");
  const photo = $("#heroPhoto");
  let taps = 0;
  sun?.addEventListener("click", () => {
    taps += 1;
    if (taps < 7) return;
    taps = 0;
    document.documentElement.classList.add("gear5");
    setTimeout(() => document.documentElement.classList.remove("gear5"), 900);
  });
  photo?.addEventListener("click", () => {
    if (REDUCE) return;
    photo.classList.remove("is-bounce");
    void photo.offsetWidth;
    photo.classList.add("is-bounce");
  });
}

function initCaseReveal() {
  const region = $("#caseRevealRegion");
  const button = $("#caseReveal");
  const label = button?.querySelector(".case-reveal-label");
  const photo = $("#casePhoto");
  if (!region || !button || !label) return;

  const isMobileCase = () => window.matchMedia("(max-width: 699px)").matches;
  const setOpen = (open) => {
    const mobile = isMobileCase();
    region.classList.toggle("is-open", open);
    button.setAttribute("aria-expanded", String(open));
    button.setAttribute("aria-label", mobile || open ? `Browse all ${CARD_PHOTOS.length} cards in the display case gallery` : "Open the display case");
    label.textContent = mobile || open ? `Browse all ${CARD_PHOTOS.length} cards` : "Open the case";
  };

  setOpen(false);
  button.addEventListener("click", () => {
    if (isMobileCase()) {
      photo?.click();
      return;
    }
    if (!region.classList.contains("is-open")) {
      setOpen(true);
      return;
    }
    photo?.click();
  });
  window.matchMedia("(max-width: 699px)").addEventListener?.("change", () => setOpen(region.classList.contains("is-open")));
}

function initOfferFlow() {
  const form = $("#offerForm");
  const photos = $("#offerPhotos");
  const count = $("#offerPhotoCount");
  const status = $("#offerStatus");

  photos?.addEventListener("change", () => {
    const total = Math.min(photos.files.length, 6);
    if (photos.files.length > 6) {
      count.textContent = `${total} selected · first 6 suggested`;
      return;
    }
    count.textContent = total ? `${total} photo${total === 1 ? "" : "s"} selected` : "Optional · up to 6";
  });

  form?.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const type = data.get("offerType");
    const category = data.get("offerCategory");
    const details = String(data.get("offerDetails") || "").trim();
    const photoTotal = Math.min(photos?.files.length || 0, 6);
    const body = [
      "Hi Thousand Sunny — I’d like to start an offer.",
      `I want to: ${type}.`,
      `I’m bringing: ${category}.`,
      details ? `Quick inventory: ${details}` : "Quick inventory: I’ll share the details in person.",
      photoTotal ? `I have ${photoTotal} photo${photoTotal === 1 ? "" : "s"} to add.` : "",
    ].filter(Boolean).join("\n");
    if (status) status.textContent = "Your text draft is ready. Add the selected photos to the message before you send it.";
    window.location.href = `sms:+17573587643?&body=${encodeURIComponent(body)}`;
  });

  $$('[data-interest]').forEach((button) => {
    button.addEventListener("click", () => {
      const interest = button.dataset.interest;
      const body = `Hi Thousand Sunny — please let me know when ${interest} events or tables are posted.`;
      window.location.href = `sms:+17573587643?&body=${encodeURIComponent(body)}`;
    });
  });
}

function tickStatus() {
  const status = getStatus();
  $$("[data-open-badge]").forEach((el) => renderBadge(el, status));
  renderHours(status);
  renderClock(status);
  return status;
}

document.addEventListener("DOMContentLoaded", () => {
  renderRoadEvents();
  initAnalytics();
  renderGames();
  renderGalleries();
  tickStatus();
  initNav();
  initLightbox();
  initCaseReveal();
  initTilt();
  initMagnetic();
  initScrollFx();
  initReveal();
  initCopy();
  initEaster();
  initOfferFlow();
  const y = $("#year");
  if (y) y.textContent = new Date().getFullYear();
  const track = $("#marquee");
  if (track) track.innerHTML += track.innerHTML;
  setInterval(tickStatus, 30_000);
});
