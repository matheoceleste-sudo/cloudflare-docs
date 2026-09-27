/* Hottes ta cuisine — scripts du site */
(function () {
  "use strict";
  var d = document;
  d.documentElement.classList.remove("no-js");

  /* Menu mobile */
  var menu = d.getElementById("nav-mobile");
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("open", open);
    d.body.style.overflow = open ? "hidden" : "";
    d.querySelectorAll("[data-menu-open]").forEach(function (b) { b.setAttribute("aria-expanded", open ? "true" : "false"); });
  }
  d.querySelectorAll("[data-menu-open]").forEach(function (b) { b.addEventListener("click", function () { setMenu(true); }); });
  d.querySelectorAll("[data-menu-close]").forEach(function (b) { b.addEventListener("click", function () { setMenu(false); }); });
  d.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  /* En-tête : filet au défilement */
  var hd = d.querySelector(".hd");
  if (hd) {
    var onScroll = function () { hd.classList.toggle("is-stuck", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  }

  /* Apparition douce */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -10% 0px" });
    d.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else d.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });

  /* Vidéos : lecture seulement lorsqu'elles sont visibles */
  if ("IntersectionObserver" in window) {
    var vo = new IntersectionObserver(function (en) {
      en.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause();
      });
    }, { threshold: 0.25 });
    d.querySelectorAll("video[data-autoplay]").forEach(function (v) { vo.observe(v); });
  }

  /* Schéma du circuit d'extraction */
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

  /* Fréquence de dégraissage */
  d.querySelectorAll("[data-freq-tool]").forEach(function (form) {
    var out = form.parentElement.querySelector(".tool-result");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var score = (+f.get("cuisson") || 0) + (+f.get("volume") || 0) + (+f.get("heures") || 0) + (+f.get("filtres") || 0);
      var last = +f.get("dernier") || 0;
      var res, months, level;
      if (score >= 9) { res = "Tous les 3 mois"; months = 3; level = 92; }
      else if (score >= 6) { res = "Tous les 4 mois"; months = 4; level = 70; }
      else if (score >= 3) { res = "Tous les 6 mois"; months = 6; level = 48; }
      else { res = "Une fois par an"; months = 12; level = 22; }
      out.innerHTML =
        '<span class="label">Rythme conseillé</span><span class="big">' + res + "</span>" +
        '<div class="meter"><i style="width:' + level + '%"></i></div>' +
        "<p>Estimation indicative, à confirmer lors d'une visite. Le minimum légal en ERP reste d'un nettoyage complet par an.</p>" +
        (last > months ? "<p><strong>Votre dernier dégraissage date de plus de " + months + " mois. Il est temps de le prévoir.</strong></p>" : "") +
        '<div class="actions mt1"><a class="btn btn-sm" href="' + form.dataset.resa + '">Réserver</a><a class="arrow" href="' + form.dataset.devis + '">Demander un devis</a></div>';
      out.classList.add("show");
    });
  });

  /* Auto-diagnostic */
  d.querySelectorAll("[data-conform-tool]").forEach(function (form) {
    var out = form.parentElement.querySelector(".tool-result");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var boxes = form.querySelectorAll("input[type=checkbox]");
      var ok = 0; boxes.forEach(function (b) { if (b.checked) ok++; });
      var pct = Math.round((ok / boxes.length) * 100);
      var msg = pct === 100 ? "Tout est en ordre. Pensez simplement à garder ce rythme."
        : pct >= 70 ? "Une bonne base. Quelques points pourraient vous être reprochés lors d'un contrôle."
        : "Plusieurs points essentiels manquent. En cas de sinistre, votre couverture peut être discutée.";
      out.innerHTML = '<span class="label">Votre score</span><span class="big">' + ok + " sur " + boxes.length + "</span>" +
        '<div class="meter"><i style="width:' + pct + '%"></i></div><p>' + msg + "</p>" +
        '<a class="arrow" href="' + form.dataset.devis + '">Faire vérifier mon installation</a>';
      out.classList.add("show");
    });
  });

  /* Filtre des conseils */
  var fr = d.querySelector("[data-filter]");
  if (fr) {
    var items = d.querySelectorAll("[data-cat]");
    var input = fr.querySelector("input");
    var cur = "all";
    var norm = function (s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
    var apply = function () {
      var q = norm(input ? input.value : "");
      items.forEach(function (c) {
        c.hidden = !((cur === "all" || c.dataset.cat === cur) && (!q || norm(c.textContent).indexOf(q) > -1));
      });
    };
    fr.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        cur = b.dataset.cat;
        fr.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        apply();
      });
    });
    if (input) input.addEventListener("input", apply);
    var h = location.hash.slice(1);
    if (h) { var hb = fr.querySelector('button[data-cat="' + h + '"]'); if (hb) hb.click(); }
  }

  d.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
