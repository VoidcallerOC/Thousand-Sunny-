const GAMES = [
  { tag: "Trading Card Game", name: "Pokémon", note: "Booster boxes, ETBs, singles & graded slabs.", icon: "zap" },
  { tag: "Trading Card Game", name: "One Piece TCG", note: "Sealed, singles & our own Straw Hat crew.", icon: "anchor" },
  { tag: "Trading Card Game", name: "Magic: The Gathering", note: "Singles, sealed, Commander decks & supplies.", icon: "spark" },
  { tag: "Trading Card Game", name: "Yu-Gi-Oh!", note: "Structure decks, tins, singles & sealed.", icon: "layers" },
  { tag: "Collectibles", name: "Anime Figures & Statues", note: "From shelf pieces to life-size showstoppers.", icon: "user" },
  { tag: "Collectibles", name: "Funko Pop!", note: "Anime, gaming & pop-culture vinyl — plus exclusives.", icon: "box" },
  { tag: "Reads & Games", name: "Manga & Board Games", note: "Latest volumes, box sets & tabletop nights.", icon: "book" },
  { tag: "Snack Bar", name: "Japanese Snacks & Drinks", note: "Ramune, Pocky, Hi-Chew & the cold-drink fridge.", icon: "cup" },
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
  { src: "/assets/img/store-figures.jpg", alt: "Store floor with anime figure shelves, board games and manga against purple walls", caption: "Figures, statues, board games & manga", w: 1350, h: 1800 },
  { src: "/assets/img/store-luffy.jpg", alt: "Life-size Luffy Gear 5 statue beside the collectibles shelves", caption: "Our life-size Gear 5 greeter", w: 1300, h: 1733, top: true },
  { src: "/assets/img/gallery-figures.jpg", alt: "Tall shelves packed with One Piece and anime figures and Funko Pops", caption: "Walls of anime figures & Pops", w: 1150, h: 1331 },
  { src: "/assets/img/gallery-art.jpg", alt: "Framed anime wall art and boxed figures on wooden shelves", caption: "Framed art & boxed collectibles", w: 1170, h: 1412 },
  { src: "/assets/img/gallery-merch.jpg", alt: "Anime tumblers, wall scrolls and a One Piece board game on display", caption: "Tumblers, scrolls & merch", w: 1170, h: 1389 },
  { src: "/assets/img/store-counter.jpg", alt: "Front counter with Japanese candy, lollipops, drink fridges and a neon star sign", caption: "Snacks, drinks & the neon out front", w: 1300, h: 1733, wide: true },
  { src: "/assets/img/play-hall.jpg", alt: "Long communal wooden table with chairs running through the store", caption: "The communal table", w: 1169, h: 1396 },
  { src: "/assets/img/event-room.jpg", alt: "Event room with a long table, chairs and figure shelves", caption: "Room for the whole crew", w: 1168, h: 1387 },
  { src: "/assets/img/play-room.jpg", alt: "Private play room with a Luffy poster, TV and purple accent wall", caption: "Private room + big screen", w: 1168, h: 1389 },
  { src: "/assets/img/store-case.jpg", alt: "Glass display case of graded Pokémon and One Piece cards and collectibles", caption: "Graded slabs & grails", w: 1200, h: 1600 },
];

const ICONS = {
  zap: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
  anchor: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="12" cy="5" r="2"/><path d="M12 7v14M5 13a7 7 0 0 0 14 0M5 13H2m20 0h-3"/></svg>',
  spark: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M6 18l2.5-2.5"/></svg>',
  layers: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="m12 2 9 5-9 5-9-5z"/><path d="m3 12 9 5 9-5M3 17l9 5 9-5"/></svg>',
  user: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="12" cy="8" r="4"/><path d="M4 20a8 8 0 0 1 16 0"/></svg>',
  box: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v10"/></svg>',
  book: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v15H6.5A2.5 2.5 0 0 0 4 19.5z"/></svg>',
  cup: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M18 8h1a3 3 0 0 1 0 6h-1M5 8h13v9a4 4 0 0 1-4 4H9a4 4 0 0 1-4-4z"/></svg>',
};

const $ = (s, c = document) => c.querySelector(s);
const $$ = (s, c = document) => [...c.querySelectorAll(s)];
const DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const REDUCE = matchMedia("(prefers-reduced-motion: reduce)").matches;
const FINE = matchMedia("(hover: hover) and (pointer: fine)").matches;

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

function renderGames() {
  const grid = $("#gamesGrid");
  if (!grid) return;
  grid.innerHTML = GAMES.map(
    (g) => `<article class="game" data-tilt>
      <span class="game-foil" aria-hidden="true"></span>
      <span class="tag">${g.tag}</span>
      ${ICONS[g.icon] || ""}
      <h4>${g.name}</h4>
      <p>${g.note}</p>
    </article>`,
  ).join("");
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
    <img src="${p.src}" alt="${p.alt}" width="${p.w}" height="${p.h}" loading="lazy" />
    <span class="gleam" aria-hidden="true"></span>
    <span>${p.caption}</span>
  </button>`;
}

function renderGalleries() {
  const gallery = $("#gallery");
  const play = $("#playGrid");
  if (gallery) gallery.innerHTML = [0, 1, 2, 3, 4, 5].map((i) => shot(i)).join("");
  if (play) play.innerHTML = [6, 7, 8].map((i) => shot(i)).join("");
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
  const img = $("#lightboxImg");
  const cap = $("#lightboxCap");
  const count = $("#lightboxCount");
  const strip = $("#lightboxStrip");
  if (!dialog) return;
  let index = 0;
  let startX = 0;

  if (strip) {
    strip.innerHTML = PHOTOS.map(
      (p, i) => `<button type="button" data-jump="${i}" aria-label="${p.caption}"><img src="${p.src}" alt=""></button>`,
    ).join("");
  }

  const show = (i) => {
    index = (i + PHOTOS.length) % PHOTOS.length;
    const p = PHOTOS[index];
    img.src = p.src;
    img.alt = p.alt;
    cap.textContent = p.caption;
    if (count) count.textContent = `${index + 1} / ${PHOTOS.length}`;
    strip?.querySelectorAll("button").forEach((b, n) => b.classList.toggle("is-on", n === index));
    if (!dialog.open) dialog.showModal();
  };

  document.addEventListener("click", (e) => {
    const jump = e.target.closest("[data-jump]");
    if (jump && dialog.contains(jump)) {
      show(Number(jump.dataset.jump));
      return;
    }
    const btn = e.target.closest("[data-photo]");
    if (btn) show(Number(btn.dataset.photo));
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

function initTilt() {
  if (REDUCE || !FINE) return;
  $$("[data-tilt]").forEach((el) => {
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
  const photo = $("#heroPhoto");
  const word = $("#wordmark");
  const tick = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    const p = max > 0 ? Math.min(1, scrollY / max) : 0;
    if (sprog) sprog.style.setProperty("--p", `${(p * 100).toFixed(2)}%`);
    if (REDUCE) return;
    const heroP = Math.min(1, scrollY / (innerHeight * 0.72));
    if (photo) photo.style.setProperty("--hero-y", `${(heroP * 70).toFixed(1)}px`);
    if (word) word.style.setProperty("--rubber", `${(-0.04 + heroP * 0.07).toFixed(3)}em`);
  };
  tick();
  window.addEventListener("scroll", tick, { passive: true });
}

function initReveal() {
  const nodes = $$(".reveal");
  if (!nodes.length) return;
  if (REDUCE) {
    nodes.forEach((n) => n.classList.add("is-in"));
    return;
  }
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

function tickStatus() {
  const status = getStatus();
  $$("[data-open-badge]").forEach((el) => renderBadge(el, status));
  renderHours(status);
  renderClock(status);
  return status;
}

document.addEventListener("DOMContentLoaded", () => {
  renderGames();
  renderGalleries();
  tickStatus();
  initNav();
  initLightbox();
  initTilt();
  initMagnetic();
  initScrollFx();
  initReveal();
  initCopy();
  initEaster();
  const y = $("#year");
  if (y) y.textContent = new Date().getFullYear();
  const track = $("#marquee");
  if (track) track.innerHTML += track.innerHTML;
  setInterval(tickStatus, 30_000);
});
