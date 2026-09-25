/* Clairvent — scripts du site (navigation, schéma interactif, outils) */
(function () {
  "use strict";
  var d = document;
  d.documentElement.classList.remove("no-js");

  /* Menu mobile */
  var nav = d.getElementById("site-nav"), toggle = d.getElementById("nav-toggle"), backdrop = d.getElementById("nav-backdrop");
  function setNav(open) {
    if (!nav) return;
    nav.classList.toggle("open", open);
    if (backdrop) backdrop.classList.toggle("show", open);
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
    d.body.style.overflow = open ? "hidden" : "";
  }
  if (toggle) toggle.addEventListener("click", function () { setNav(!nav.classList.contains("open")); });
  if (backdrop) backdrop.addEventListener("click", function () { setNav(false); });
  d.querySelectorAll("[data-nav-close]").forEach(function (b) { b.addEventListener("click", function () { setNav(false); }); });
  d.addEventListener("keydown", function (e) { if (e.key === "Escape") setNav(false); });
  d.querySelectorAll(".main-nav .has-sub > a").forEach(function (a) {
    a.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width:1080px)").matches) {
        var li = a.parentElement;
        if (!li.classList.contains("open")) { e.preventDefault(); li.classList.add("open"); }
      }
    });
  });

  /* En-tête collant */
  var header = d.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-stuck", window.scrollY > 10); };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  }

  /* Apparition au défilement */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    d.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else d.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });

  /* Schéma interactif du circuit d'extraction */
  d.querySelectorAll("[data-diagram]").forEach(function (root) {
    var panel = root.querySelector(".diagram-panel");
    var spots = root.querySelectorAll(".hotspot");
    var tabs = root.querySelectorAll(".diagram-tabs button");
    function show(key) {
      spots.forEach(function (s) { s.classList.toggle("active", s.dataset.key === key); });
      tabs.forEach(function (t) { t.setAttribute("aria-pressed", t.dataset.key === key ? "true" : "false"); });
      var src = root.querySelector('template[data-key="' + key + '"]');
      if (src && panel) panel.innerHTML = src.innerHTML;
    }
    spots.forEach(function (s) {
      s.addEventListener("click", function () { show(s.dataset.key); });
      s.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); show(s.dataset.key); } });
    });
    tabs.forEach(function (t) { t.addEventListener("click", function () { show(t.dataset.key); }); });
    show("hotte");
  });

  /* Calculateur de fréquence de dégraissage */
  d.querySelectorAll("[data-freq-tool]").forEach(function (form) {
    var out = form.parentElement.querySelector(".tool-result");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var score = 0;
      score += +f.get("cuisson") || 0;
      score += +f.get("volume") || 0;
      score += +f.get("heures") || 0;
      score += +f.get("filtres") || 0;
      var last = +f.get("dernier") || 0;
      var res, months, level;
      if (score >= 9) { res = "Tous les 3 mois (4 fois par an)"; months = 3; level = 92; }
      else if (score >= 6) { res = "Tous les 4 mois (3 fois par an)"; months = 4; level = 70; }
      else if (score >= 3) { res = "Tous les 6 mois (2 fois par an)"; months = 6; level = 48; }
      else { res = "Une fois par an minimum"; months = 12; level = 22; }
      var late = last > months;
      out.innerHTML =
        '<span class="tag tag-accent">Recommandation indicative</span>' +
        '<b class="big">' + res + "</b>" +
        '<div class="meter" aria-hidden="true"><i style="width:' + level + '%"></i></div>' +
        "<p>Niveau d'encrassement attendu : <strong style=\"color:#fff\">" + (level > 80 ? "très élevé" : level > 60 ? "élevé" : level > 40 ? "modéré" : "faible") + "</strong>. " +
        "Le règlement de sécurité incendie impose au minimum un nettoyage annuel du circuit complet ; l'intensité de votre activité justifie ce rythme.</p>" +
        (late ? '<p style="color:#ffb070"><strong>Votre dernier dégraissage date de plus de ' + months + " mois : une intervention est à prévoir rapidement.</strong></p>" : "") +
        '<p class="mb0"><a class="btn btn-sm" href="' + form.dataset.resa + '">Planifier une intervention</a> <a class="btn btn-sm btn-ghost-light" href="' + form.dataset.devis + '">Demander un devis gratuit</a></p>';
      out.classList.add("show");
      out.scrollIntoView({ behavior: "smooth", block: "nearest" });
    });
  });

  /* Auto-diagnostic de conformité */
  d.querySelectorAll("[data-conform-tool]").forEach(function (form) {
    var out = form.parentElement.querySelector(".tool-result");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var boxes = form.querySelectorAll("input[type=checkbox]");
      var ok = 0; boxes.forEach(function (b) { if (b.checked) ok++; });
      var pct = Math.round((ok / boxes.length) * 100);
      var msg = pct === 100 ? "Excellent : votre installation coche tous les points clés."
        : pct >= 70 ? "Bonne base, mais quelques points peuvent vous être reprochés en cas de contrôle ou de sinistre."
        : "Plusieurs points essentiels manquent : votre responsabilité et votre couverture d'assurance peuvent être engagées.";
      out.innerHTML = '<span class="tag tag-accent">Votre score</span><b class="big">' + ok + " / " + boxes.length + " points</b>" +
        '<div class="meter" aria-hidden="true"><i style="width:' + pct + '%;background:linear-gradient(90deg,#d23c2a,#f3c34d,#5fd39c)"></i></div><p>' + msg + "</p>" +
        '<p class="mb0"><a class="btn btn-sm" href="' + form.dataset.devis + '">Faire contrôler mon installation</a></p>';
      out.classList.add("show");
    });
  });

  /* Filtre des conseils */
  var filterRoot = d.querySelector("[data-filter]");
  if (filterRoot) {
    var cards = d.querySelectorAll("[data-cat]");
    var input = filterRoot.querySelector("input");
    var current = "all";
    var apply = function () {
      var q = (input && input.value || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
      cards.forEach(function (c) {
        var txt = c.textContent.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
        var okCat = current === "all" || c.dataset.cat === current;
        c.hidden = !(okCat && (!q || txt.indexOf(q) > -1));
      });
    };
    filterRoot.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        current = b.dataset.cat;
        filterRoot.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        apply();
      });
    });
    if (input) input.addEventListener("input", apply);
  }

  /* Bouton flottant « être rappelé » */
  var fab = d.querySelector(".fab");
  if (fab) {
    fab.querySelector(".fab-btn").addEventListener("click", function () {
      var open = !fab.classList.contains("open");
      fab.classList.toggle("open", open);
      this.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* Année courante */
  d.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
