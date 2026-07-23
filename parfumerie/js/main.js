/* =========================================================
   SILLAGE — animations & boutique (anime.js v3)
   ========================================================= */
(function () {
  "use strict";

  const reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  const hasHover = window.matchMedia("(hover: hover)").matches;

  /* ------------------------------------------------------------------ *
   * 1. DATA
   * ------------------------------------------------------------------ */
  const PARFUMS = [
    {
      idx: "N°01",
      name: "Noir Absolu",
      family: "Boisé — Ambré",
      notes: ["Oud", "Cuir", "Encens"],
      price: 185,
      accent: "#c9a15a",
      liquidTop: "#c9963e",
      liquidBottom: "#3a2712",
      capA: "#e7cf9a",
      capB: "#7c5d2a",
      desc:
        "Un boisé ténébreux et magnétique. L'oud fumé s'enlace au cuir et à l'encens pour une signature nocturne qui ne s'oublie pas.",
      pyr: {
        Tête: "Bergamote · Poivre noir",
        Cœur: "Cuir · Rose sombre",
        Fond: "Oud · Encens · Ambre",
      },
    },
    {
      idx: "N°02",
      name: "Rose Éternelle",
      family: "Floral — Poudré",
      notes: ["Rose de Mai", "Pivoine", "Musc"],
      price: 165,
      accent: "#d98aa0",
      liquidTop: "#e59ab0",
      liquidBottom: "#4a1f2c",
      capA: "#f4cdd8",
      capB: "#8f4c5e",
      desc:
        "Une rose qui refuse de faner. Cueillie à Grasse, adoucie de pivoine et voilée d'un musc poudré, elle habille la peau d'un printemps perpétuel.",
      pyr: {
        Tête: "Poire · Bergamote",
        Cœur: "Rose de Mai · Pivoine",
        Fond: "Musc blanc · Iris · Santal",
      },
    },
    {
      idx: "N°03",
      name: "Bois de Lune",
      family: "Boisé — Frais",
      notes: ["Vétiver", "Cèdre", "Ambre gris"],
      price: 175,
      accent: "#6fb39a",
      liquidTop: "#7ec9ae",
      liquidBottom: "#10352e",
      capA: "#c2e6d9",
      capB: "#356e5c",
      desc:
        "La fraîcheur d'une forêt sous la lune. Vétiver et cèdre respirent, l'ambre gris apporte la caresse saline d'un souvenir marin.",
      pyr: {
        Tête: "Bergamote · Cardamome",
        Cœur: "Vétiver · Cèdre",
        Fond: "Ambre gris · Mousse · Musc",
      },
    },
    {
      idx: "N°04",
      name: "Iris Nocturne",
      family: "Floral — Boisé",
      notes: ["Iris", "Violette", "Santal"],
      price: 195,
      accent: "#a68cd6",
      liquidTop: "#b49bde",
      liquidBottom: "#2a2140",
      capA: "#ddd0f2",
      capB: "#5c4c86",
      desc:
        "Le velours d'un iris à la tombée du jour. Poudré, mystérieux, réchauffé de santal — une élégance qui se murmure plus qu'elle ne se déclare.",
      pyr: {
        Tête: "Poivre rose · Mandarine",
        Cœur: "Iris · Violette",
        Fond: "Santal · Fève tonka · Musc",
      },
    },
  ];

  const euro = (n) => n.toLocaleString("fr-FR") + "€";

  /* ------------------------------------------------------------------ *
   * 2. FLACON SVG (parametric, unique gradient ids per instance)
   * ------------------------------------------------------------------ */
  function flacon(p, id) {
    const g = (s) => `${s}-${id}`;
    return `
    <svg class="flacon" viewBox="0 0 220 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Flacon ${p.name}">
      <defs>
        <linearGradient id="${g("liquid")}" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="${p.liquidTop}"/>
          <stop offset="1" stop-color="${p.liquidBottom}"/>
        </linearGradient>
        <linearGradient id="${g("cap")}" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="${p.capA}"/>
          <stop offset="1" stop-color="${p.capB}"/>
        </linearGradient>
        <linearGradient id="${g("glass")}" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stop-color="rgba(255,255,255,0.16)"/>
          <stop offset="0.5" stop-color="rgba(255,255,255,0.03)"/>
          <stop offset="1" stop-color="rgba(255,255,255,0.10)"/>
        </linearGradient>
        <linearGradient id="${g("shine")}" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="rgba(255,255,255,0.55)"/>
          <stop offset="1" stop-color="rgba(255,255,255,0)"/>
        </linearGradient>
        <clipPath id="${g("clip")}">
          <rect x="46" y="76" width="128" height="268" rx="26"/>
        </clipPath>
      </defs>

      <rect x="84" y="6" width="52" height="52" rx="9" fill="url(#${g("cap")})"/>
      <rect x="84" y="6" width="52" height="12" rx="6" fill="rgba(255,255,255,0.22)"/>
      <rect x="92" y="54" width="36" height="18" rx="3" fill="url(#${g("cap")})" opacity="0.9"/>
      <rect x="88" y="70" width="44" height="10" rx="4" fill="rgba(255,255,255,0.06)"/>

      <rect x="46" y="76" width="128" height="268" rx="26" fill="url(#${g("glass")})"
            stroke="${p.accent}" stroke-opacity="0.35" stroke-width="1"/>

      <g clip-path="url(#${g("clip")})">
        <g class="flacon__liquid">
          <path d="M46,168 Q86,150 110,166 T174,166 L174,344 L46,344 Z" fill="url(#${g("liquid")})"/>
        </g>
        <circle class="bubble" cx="86" cy="330" r="3" fill="rgba(255,255,255,0.35)"/>
        <circle class="bubble" cx="128" cy="336" r="2.2" fill="rgba(255,255,255,0.3)"/>
        <circle class="bubble" cx="108" cy="340" r="2.6" fill="rgba(255,255,255,0.25)"/>
      </g>

      <rect x="60" y="96" width="14" height="220" rx="7" fill="url(#${g("shine")})" opacity="0.6"/>
      <rect x="150" y="120" width="6" height="150" rx="3" fill="url(#${g("shine")})" opacity="0.3"/>

      <circle cx="110" cy="250" r="30" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="0.8"/>
      <text x="110" y="248" text-anchor="middle" fill="rgba(255,255,255,0.8)"
            font-family="Cormorant Garamond, serif" font-size="20" font-style="italic">S</text>
      <text x="110" y="264" text-anchor="middle" fill="rgba(255,255,255,0.45)"
            font-family="Jost, sans-serif" font-size="5" letter-spacing="2">${p.idx}</text>
    </svg>`;
  }

  /* ------------------------------------------------------------------ *
   * 3. RENDER cards + hero flacon + marquee
   * ------------------------------------------------------------------ */
  const grid = document.getElementById("grid");
  grid.innerHTML = PARFUMS.map(
    (p, i) => `
    <article class="card" data-index="${i}" data-accent="${p.accent}" style="--accent:${p.accent}" role="button" tabindex="0" aria-label="Découvrir ${p.name}">
      <div class="card__idx">${p.idx}</div>
      <div class="card__stage">
        ${flacon(p, "c" + i)}
        <span class="card__open">Voir le parfum</span>
      </div>
      <div class="card__family">${p.family}</div>
      <h3 class="card__name">${p.name}</h3>
      <div class="card__notes">
        ${p.notes.map((n) => `<span class="card__note">${n}</span>`).join("")}
      </div>
      <div class="card__foot">
        <div class="card__price">${euro(p.price)} <small>100 ml</small></div>
        <button class="card__buy" data-add="${i}" data-cursor="link">Ajouter <span>→</span></button>
      </div>
    </article>`
  ).join("");

  document.querySelector(".hero__flacon").innerHTML = flacon(PARFUMS[0], "hero");

  const words = [
    "Fait à Paris",
    "Extrait de parfum",
    "Petites séries",
    "Douze semaines de macération",
    "Verre soufflé main",
  ];
  const track = document.getElementById("marquee-track");
  const chunk = words
    .map((w) => `<span class="marquee__item">${w}</span>`)
    .join("");
  track.innerHTML = chunk + chunk + chunk;

  /* ------------------------------------------------------------------ *
   * 4. CUSTOM CURSOR + SILLAGE TRAIL (event delegation for dynamic UI)
   * ------------------------------------------------------------------ */
  if (hasHover && !reduceMotion) {
    const cursor = document.querySelector(".cursor");
    const dot = cursor.querySelector(".cursor__dot");
    const ring = cursor.querySelector(".cursor__ring");
    const HOVER = "a, button, .card, [data-cursor='link']";
    let mx = window.innerWidth / 2,
      my = window.innerHeight / 2;
    let rx = mx,
      ry = my;
    let lastTrail = 0;

    window.addEventListener("mousemove", (e) => {
      mx = e.clientX;
      my = e.clientY;
      dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%, -50%)`;
      const now = performance.now();
      if (now - lastTrail > 45) {
        lastTrail = now;
        spawnTrail(mx, my);
      }
    });

    (function loop() {
      rx += (mx - rx) * 0.14;
      ry += (my - ry) * 0.14;
      ring.style.transform = `translate(${rx}px, ${ry}px) translate(-50%, -50%)`;
      requestAnimationFrame(loop);
    })();

    document.addEventListener("mouseover", (e) => {
      if (e.target.closest(HOVER)) cursor.classList.add("is-hover");
    });
    document.addEventListener("mouseout", (e) => {
      const from = e.target.closest(HOVER);
      const to = e.relatedTarget && e.relatedTarget.closest(HOVER);
      if (from && from !== to) cursor.classList.remove("is-hover");
    });

    function spawnTrail(x, y) {
      const d = document.createElement("div");
      d.className = "trail-dot";
      d.style.left = x + "px";
      d.style.top = y + "px";
      const accent = document.body.dataset.amb || "#c9a15a";
      d.style.background = `radial-gradient(circle, ${accent}, transparent 70%)`;
      document.body.appendChild(d);
      anime({
        targets: d,
        opacity: [0.7, 0],
        scale: [1, 2.4],
        translateX: (Math.random() - 0.5) * 26,
        translateY: (Math.random() - 0.5) * 26 - 10,
        duration: 1100,
        easing: "easeOutExpo",
        complete: () => d.remove(),
      });
    }
  }

  /* ------------------------------------------------------------------ *
   * 5. PRELOADER + HERO
   * ------------------------------------------------------------------ */
  const preloader = document.getElementById("preloader");
  const countEl = document.getElementById("count");

  function startHero() {
    anime
      .timeline({ easing: "easeOutExpo" })
      .add({ targets: ".hero__label", opacity: [0, 1], translateY: [30, 0], duration: 900 })
      .add(
        {
          targets: ".hero__title .l",
          translateY: ["110%", "0%"],
          duration: 1400,
          delay: anime.stagger(70),
        },
        "-=700"
      )
      .add(
        {
          targets: [".hero__sub", ".hero__scroll"],
          opacity: [0, 1],
          translateY: [30, 0],
          duration: 1000,
          delay: anime.stagger(140),
        },
        "-=900"
      )
      .add(
        { targets: ".hero__flacon", opacity: [0, 1], translateX: [80, 0], duration: 1600 },
        "-=1300"
      );

    if (!reduceMotion) {
      anime({
        targets: ".hero__flacon",
        translateY: ["-52%", "-48%"],
        rotate: ["-1.5deg", "1.5deg"],
        duration: 6000,
        direction: "alternate",
        loop: true,
        easing: "easeInOutSine",
      });
    }
  }

  let booted = false;
  function runPreloader() {
    if (booted) return;
    booted = true;
    if (reduceMotion) {
      preloader.style.display = "none";
      startHero();
      revealSetup();
      return;
    }

    anime
      .timeline({ easing: "easeOutExpo" })
      .add({
        targets: ".trail-path",
        strokeDashoffset: [anime.setDashoffset, 0],
        duration: 1600,
        easing: "easeInOutSine",
      })
      .add(
        {
          targets: ".preloader__word span",
          translateY: ["120%", "0%"],
          opacity: [0, 1],
          duration: 1100,
          delay: anime.stagger(60),
        },
        "-=1200"
      )
      .add({ targets: ".preloader__meta", opacity: [0, 1], duration: 700 }, "-=700");

    const counter = { v: 0 };
    anime({
      targets: counter,
      v: 100,
      duration: 2200,
      easing: "easeInOutQuart",
      round: 1,
      update: () => (countEl.textContent = counter.v),
      complete: () => {
        anime
          .timeline({ easing: "easeInOutExpo" })
          .add({
            targets: ".preloader__inner",
            opacity: [1, 0],
            translateY: [0, -30],
            duration: 700,
          })
          .add(
            {
              targets: ".preloader",
              translateY: ["0%", "-100%"],
              duration: 1100,
              complete: () => {
                preloader.style.display = "none";
                preloader.classList.add("is-done");
              },
            },
            "-=200"
          );
        startHero();
        revealSetup();
      },
    });
  }

  /* ------------------------------------------------------------------ *
   * 6. MANIFESTO split + 7. MARQUEE loop + 8. BUBBLES
   * ------------------------------------------------------------------ */
  const manifesto = document.querySelector("[data-split]");
  if (manifesto) {
    manifesto.innerHTML = manifesto.textContent
      .trim()
      .split(" ")
      .map((w) => `<span class="w">${w}</span>`)
      .join(" ");
  }

  if (!reduceMotion) {
    const third = track.scrollWidth / 3;
    anime({ targets: track, translateX: [0, -third], duration: 18000, easing: "linear", loop: true });

    document.querySelectorAll(".bubble").forEach((b, i) => {
      anime({
        targets: b,
        translateY: [0, -(90 + Math.random() * 40)],
        opacity: [0, 0.6, 0],
        duration: 3600 + Math.random() * 2400,
        delay: i * 600,
        loop: true,
        easing: "easeInOutSine",
      });
    });
  }

  /* ------------------------------------------------------------------ *
   * 9. SCROLL REVEALS
   * ------------------------------------------------------------------ */
  function revealSetup() {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          io.unobserve(el);

          if (el.classList.contains("reveal-up")) {
            anime({ targets: el, opacity: [0, 1], translateY: [30, 0], duration: 1100, easing: "easeOutExpo" });
          }
          if (el.classList.contains("manifesto")) {
            anime({
              targets: el.querySelectorAll(".w"),
              opacity: [0.12, 1],
              duration: 900,
              delay: anime.stagger(45),
              easing: "easeOutQuad",
            });
          }
          if (el.classList.contains("collection")) {
            anime({
              targets: el.querySelectorAll(".card"),
              opacity: [0, 1],
              translateY: [40, 0],
              duration: 1100,
              delay: anime.stagger(140),
              easing: "easeOutExpo",
            });
          }
          if (el.classList.contains("pyramid")) {
            anime({
              targets: el.querySelectorAll(".pyramid__bar i"),
              width: ["0%", "100%"],
              duration: 1400,
              delay: anime.stagger(220),
              easing: "easeInOutExpo",
            });
            anime({
              targets: el.querySelectorAll(".pyramid__row"),
              opacity: [0, 1],
              translateX: [-20, 0],
              duration: 900,
              delay: anime.stagger(220),
              easing: "easeOutExpo",
            });
          }
        });
      },
      { threshold: 0.18 }
    );
    document
      .querySelectorAll(".reveal-up, .manifesto, .collection, .pyramid")
      .forEach((el) => io.observe(el));
  }

  /* ------------------------------------------------------------------ *
   * 10. CARD HOVER — ambient tint
   * ------------------------------------------------------------------ */
  const root = document.documentElement;
  const defaultAmb = "rgba(201, 161, 90, 0.14)";
  function hexToRgba(hex, a) {
    const n = parseInt(hex.slice(1), 16);
    return `rgba(${(n >> 16) & 255}, ${(n >> 8) & 255}, ${n & 255}, ${a})`;
  }
  document.querySelectorAll(".card").forEach((card) => {
    const accent = card.dataset.accent;
    card.addEventListener("mouseenter", () => {
      document.body.dataset.amb = accent;
      root.style.setProperty("--amb-color", hexToRgba(accent, 0.18));
      root.style.setProperty("--amb-y", "50%");
    });
    card.addEventListener("mouseleave", () => {
      document.body.dataset.amb = "#c9a15a";
      root.style.setProperty("--amb-color", defaultAmb);
      root.style.setProperty("--amb-y", "12%");
    });
  });

  /* ------------------------------------------------------------------ *
   * 11. PRODUCT DETAIL OVERLAY
   * ------------------------------------------------------------------ */
  const detail = document.createElement("div");
  detail.className = "detail";
  detail.id = "detail";
  detail.setAttribute("aria-hidden", "true");
  detail.innerHTML = `
    <div class="detail__bg" data-close></div>
    <div class="detail__panel">
      <button class="detail__close" data-close aria-label="Fermer">✕</button>
      <div class="detail__stage"></div>
      <div class="detail__content">
        <span class="detail__idx"></span>
        <span class="detail__family"></span>
        <h2 class="detail__name"></h2>
        <p class="detail__desc"></p>
        <div class="detail__pyr"></div>
        <div class="detail__foot">
          <span class="detail__price"></span>
          <button class="btn-add" data-add-detail>Ajouter au panier</button>
        </div>
      </div>
    </div>`;
  document.body.appendChild(detail);

  const dPanel = detail.querySelector(".detail__panel");
  const dStage = detail.querySelector(".detail__stage");
  let detailIndex = 0;

  function openDetail(i) {
    const p = PARFUMS[i];
    detailIndex = i;
    dPanel.style.setProperty("--accent", p.accent);
    dStage.innerHTML = flacon(p, "d" + i);
    detail.querySelector(".detail__idx").textContent = p.idx;
    detail.querySelector(".detail__family").textContent = p.family;
    detail.querySelector(".detail__name").textContent = p.name;
    detail.querySelector(".detail__desc").textContent = p.desc;
    detail.querySelector(".detail__price").innerHTML = `${euro(p.price)} <small>100 ml — Extrait</small>`;
    detail.querySelector(".detail__pyr").innerHTML = Object.entries(p.pyr)
      .map(
        ([k, v]) =>
          `<div class="detail__pyr-row"><span class="detail__pyr-k">${k}</span><span class="detail__pyr-v">${v}</span></div>`
      )
      .join("");

    detail.classList.add("is-open");
    detail.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";

    if (reduceMotion) {
      detail.querySelector(".detail__bg").style.opacity = 1;
      dPanel.style.opacity = 1;
      dPanel.style.transform = "none";
      return;
    }
    anime.remove([detail.querySelector(".detail__bg"), dPanel]);
    anime({ targets: detail.querySelector(".detail__bg"), opacity: [0, 1], duration: 500, easing: "easeOutQuad" });
    anime({
      targets: dPanel,
      opacity: [0, 1],
      translateY: [40, 0],
      scale: [0.98, 1],
      duration: 800,
      easing: "easeOutExpo",
    });
    anime({
      targets: dStage.querySelector(".flacon"),
      scale: [0.85, 1],
      opacity: [0, 1],
      duration: 1000,
      easing: "easeOutExpo",
    });
    anime({
      targets: detail.querySelectorAll(
        ".detail__idx, .detail__family, .detail__name, .detail__desc, .detail__pyr-row, .detail__foot"
      ),
      opacity: [0, 1],
      translateY: [20, 0],
      duration: 700,
      delay: anime.stagger(70, { start: 200 }),
      easing: "easeOutExpo",
    });
    dStage.querySelectorAll(".bubble").forEach((b, k) => {
      anime({
        targets: b,
        translateY: [0, -110],
        opacity: [0, 0.6, 0],
        duration: 4000 + Math.random() * 2000,
        delay: k * 500,
        loop: true,
        easing: "easeInOutSine",
      });
    });
  }

  function closeDetail() {
    document.body.style.overflow = "";
    if (reduceMotion) {
      detail.classList.remove("is-open");
      detail.setAttribute("aria-hidden", "true");
      return;
    }
    anime({ targets: detail.querySelector(".detail__bg"), opacity: [1, 0], duration: 400, easing: "easeOutQuad" });
    anime({
      targets: dPanel,
      opacity: [1, 0],
      translateY: [0, 30],
      duration: 450,
      easing: "easeInQuad",
      complete: () => {
        detail.classList.remove("is-open");
        detail.setAttribute("aria-hidden", "true");
      },
    });
  }

  detail.addEventListener("click", (e) => {
    if (e.target.closest("[data-close]")) closeDetail();
    if (e.target.closest("[data-add-detail]")) addToCart(detailIndex, e.target.closest(".btn-add"));
  });

  // open detail from card (but not when clicking the "Ajouter" button)
  grid.addEventListener("click", (e) => {
    const addBtn = e.target.closest("[data-add]");
    if (addBtn) {
      e.stopPropagation();
      addToCart(+addBtn.dataset.add, addBtn);
      return;
    }
    const card = e.target.closest(".card");
    if (card) openDetail(+card.dataset.index);
  });
  grid.addEventListener("keydown", (e) => {
    if (e.key !== "Enter" && e.key !== " ") return;
    const card = e.target.closest(".card");
    if (card && !e.target.closest("[data-add]")) {
      e.preventDefault();
      openDetail(+card.dataset.index);
    }
  });

  /* ------------------------------------------------------------------ *
   * 12. CART
   * ------------------------------------------------------------------ */
  const cart = document.createElement("div");
  cart.className = "cart";
  cart.id = "cart";
  cart.setAttribute("aria-hidden", "true");
  cart.innerHTML = `
    <div class="cart__bg" data-cart-close></div>
    <aside class="cart__panel" role="dialog" aria-label="Panier">
      <div class="cart__head">
        <h3>Votre panier</h3>
        <button class="cart__close" data-cart-close aria-label="Fermer">✕</button>
      </div>
      <div class="cart__items" id="cartItems"></div>
      <div class="cart__foot">
        <div class="cart__total">
          <span class="cart__total-k">Total</span>
          <span class="cart__total-v" id="cartTotal">0€</span>
        </div>
        <button class="cart__checkout">Passer commande</button>
      </div>
    </aside>`;
  document.body.appendChild(cart);

  const cartPanel = cart.querySelector(".cart__panel");
  const cartBg = cart.querySelector(".cart__bg");
  const cartItemsEl = document.getElementById("cartItems");
  const cartTotalEl = document.getElementById("cartTotal");
  const cartCountEl = document.getElementById("cartCount");
  const cartToggle = document.getElementById("cartToggle");

  const STORE = "sillage-cart";
  let items = [];
  try {
    items = JSON.parse(localStorage.getItem(STORE)) || [];
  } catch (e) {
    items = [];
  }

  function save() {
    try {
      localStorage.setItem(STORE, JSON.stringify(items));
    } catch (e) {}
  }

  function cartCount() {
    return items.reduce((s, it) => s + it.qty, 0);
  }
  function cartTotal() {
    return items.reduce((s, it) => s + PARFUMS[it.i].price * it.qty, 0);
  }

  function renderCart() {
    if (!items.length) {
      cartItemsEl.innerHTML = `<p class="cart__empty">Votre sillage n'a pas encore commencé.</p>`;
    } else {
      cartItemsEl.innerHTML = items
        .map((it) => {
          const p = PARFUMS[it.i];
          return `
          <div class="cart-line" style="--accent:${p.accent}">
            <div class="cart-line__thumb"></div>
            <div>
              <div class="cart-line__name">${p.name}</div>
              <div class="cart-line__meta">
                <span>${euro(p.price)}</span>
                <span class="cart-line__qty">
                  <button data-dec="${it.i}" aria-label="Retirer un">−</button>
                  <span>${it.qty}</span>
                  <button data-inc="${it.i}" aria-label="Ajouter un">+</button>
                </span>
              </div>
            </div>
            <div class="cart-line__price">${euro(p.price * it.qty)}</div>
          </div>`;
        })
        .join("");
    }
    cartTotalEl.textContent = euro(cartTotal());
    const c = cartCount();
    cartCountEl.textContent = c;
    cartCountEl.classList.toggle("is-active", c > 0);
    save();
  }

  function addToCart(i, sourceEl) {
    const existing = items.find((it) => it.i === i);
    if (existing) existing.qty++;
    else items.push({ i, qty: 1 });
    renderCart();
    pulseCount();
    if (sourceEl && !reduceMotion) flyToCart(sourceEl, PARFUMS[i].accent);
  }

  function changeQty(i, delta) {
    const it = items.find((x) => x.i === i);
    if (!it) return;
    it.qty += delta;
    if (it.qty <= 0) items = items.filter((x) => x.i !== i);
    renderCart();
  }

  function pulseCount() {
    if (reduceMotion) return;
    anime({
      targets: cartCountEl,
      scale: [1, 1.5, 1],
      duration: 500,
      easing: "easeOutBack",
    });
  }

  function flyToCart(sourceEl, color) {
    const s = sourceEl.getBoundingClientRect();
    const t = cartToggle.getBoundingClientRect();
    const fly = document.createElement("div");
    fly.className = "fly";
    fly.style.setProperty("--fly", color);
    fly.style.left = s.left + s.width / 2 - 13 + "px";
    fly.style.top = s.top + s.height / 2 - 17 + "px";
    document.body.appendChild(fly);
    anime({
      targets: fly,
      left: t.left + t.width / 2 - 13 + "px",
      top: t.top + t.height / 2 - 17 + "px",
      scale: [1, 0.3],
      opacity: [1, 0.4],
      rotate: 40,
      duration: 750,
      easing: "cubicBezier(0.5, -0.2, 0.4, 1)",
      complete: () => fly.remove(),
    });
  }

  function openCart() {
    cart.classList.add("is-open");
    cart.setAttribute("aria-hidden", "false");
    if (reduceMotion) {
      cartBg.style.opacity = 1;
      cartPanel.style.transform = "none";
      return;
    }
    anime.remove([cartBg, cartPanel]);
    anime({ targets: cartBg, opacity: [0, 1], duration: 400, easing: "easeOutQuad" });
    anime({ targets: cartPanel, translateX: ["100%", "0%"], duration: 650, easing: "easeOutExpo" });
    anime({
      targets: cart.querySelectorAll(".cart-line"),
      opacity: [0, 1],
      translateX: [30, 0],
      delay: anime.stagger(70, { start: 150 }),
      duration: 600,
      easing: "easeOutExpo",
    });
  }

  function closeCart() {
    if (reduceMotion) {
      cart.classList.remove("is-open");
      cart.setAttribute("aria-hidden", "true");
      return;
    }
    anime({ targets: cartBg, opacity: [1, 0], duration: 350, easing: "easeOutQuad" });
    anime({
      targets: cartPanel,
      translateX: ["0%", "100%"],
      duration: 500,
      easing: "easeInExpo",
      complete: () => {
        cart.classList.remove("is-open");
        cart.setAttribute("aria-hidden", "true");
      },
    });
  }

  cartToggle.addEventListener("click", openCart);
  cart.addEventListener("click", (e) => {
    if (e.target.closest("[data-cart-close]")) return closeCart();
    const inc = e.target.closest("[data-inc]");
    const dec = e.target.closest("[data-dec]");
    if (inc) changeQty(+inc.dataset.inc, +1);
    if (dec) changeQty(+dec.dataset.dec, -1);
  });
  cart.querySelector(".cart__checkout").addEventListener("click", () => {
    if (!items.length) return;
    const c = cart.querySelector(".cart__checkout");
    c.textContent = "Merci — ceci est une démo ✦";
    setTimeout(() => (c.textContent = "Passer commande"), 2200);
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      if (detail.classList.contains("is-open")) closeDetail();
      if (cart.classList.contains("is-open")) closeCart();
    }
  });

  renderCart();

  /* ------------------------------------------------------------------ *
   * 13. Hero parallax
   * ------------------------------------------------------------------ */
  const heroFlacon = document.querySelector(".hero__flacon");
  window.addEventListener(
    "scroll",
    () => {
      const y = window.scrollY;
      if (heroFlacon && y < window.innerHeight && !reduceMotion) {
        heroFlacon.style.marginTop = y * 0.15 + "px";
      }
    },
    { passive: true }
  );

  /* ------------------------------------------------------------------ *
   * BOOT
   * ------------------------------------------------------------------ */
  window.addEventListener("load", runPreloader);
  if (document.readyState === "complete") runPreloader();
})();
