/* =========================================================
   MathClean — interactions
   ========================================================= */
(function () {
  "use strict";

  /* ---------------------------------------------------------------
     CONFIGURATION — les seules lignes à modifier au quotidien.
     --------------------------------------------------------------- */
  var CONFIG = {
    // Adresse qui reçoit les demandes de devis.
    email: "contact@mathclean.fr",

    // Laisser à null pour envoyer par e-mail depuis le poste du visiteur.
    // Renseigner l'URL d'un service de formulaire (Formspree, Worker
    // Cloudflare, etc.) pour un envoi en arrière-plan sans client mail.
    endpoint: null,

    // Tarifs horaires HT servant à l'estimation indicative.
    tarifHoraire: {
      bureaux: 25,
      appartement: 27,
      location: 29,
      chantier: 34,
      vitrerie: 32,
      copro: 26
    },

    // Durée d'intervention estimée, en heures, par tranche de surface.
    dureeParSurface: { 30: 2, 60: 3, 110: 4.5, 200: 6.5, 350: 9 }
  };

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  /* ─────────────── Année du copyright ─────────────── */
  var yearEl = $("#year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ─────────────── Date par défaut : demain ─────────────── */
  var dateInput = $("#date-input");
  if (dateInput) {
    var tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    var iso = tomorrow.toISOString().slice(0, 10);
    dateInput.value = iso;
    dateInput.min = new Date().toISOString().slice(0, 10);
  }

  /* ─────────────── Header : ombre au scroll ─────────────── */
  var header = $("#header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ─────────────── Menu mobile ─────────────── */
  var burger = $(".burger");
  var mobileMenu = $("#menu-mobile");

  if (burger && mobileMenu) {
    var setMenu = function (open) {
      burger.setAttribute("aria-expanded", String(open));
      header.classList.toggle("is-open", open);
      mobileMenu.hidden = !open;
      burger.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
    };

    burger.addEventListener("click", function () {
      setMenu(burger.getAttribute("aria-expanded") !== "true");
    });

    $$("a", mobileMenu).forEach(function (link) {
      link.addEventListener("click", function () { setMenu(false); });
    });

    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setMenu(false);
    });

    // Le menu mobile n'a plus lieu d'être si l'on repasse en grand écran.
    window.addEventListener("resize", function () {
      if (window.innerWidth > 860) setMenu(false);
    });
  }

  /* ─────────────── Apparition progressive des sections ─────────────── */
  var revealTargets = $$(".card, .feature, .price-card, .steps li, .quote, .zones-block, .faq details");
  if ("IntersectionObserver" in window && revealTargets.length) {
    revealTargets.forEach(function (el) { el.classList.add("reveal"); });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry, i) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        el.style.transitionDelay = Math.min(i * 60, 240) + "ms";
        el.classList.add("is-visible");
        observer.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px" });
    revealTargets.forEach(function (el) { observer.observe(el); });
  }

  /* ─────────────── Formulaire de devis ─────────────── */
  var form = $("#quote-form");
  if (!form) return;

  var steps = $$(".step", form);
  var progressBar = $("#progress-bar");
  var stepNow = $("#step-now");
  var current = 1;

  var showStep = function (n) {
    current = n;
    steps.forEach(function (step) {
      step.hidden = Number(step.dataset.step) !== n;
    });
    if (progressBar) progressBar.style.width = Math.min(n, 2) * 50 + "%";
    if (stepNow) stepNow.textContent = String(Math.min(n, 2));

    var firstField = $("input, select, textarea", steps[n - 1]);
    if (firstField && n > 1) firstField.focus();
  };

  var validateStep = function (n) {
    var scope = steps[n - 1];
    var ok = true;
    $$("input, select, textarea", scope).forEach(function (field) {
      if (!field.required) return;
      var valid = field.type === "checkbox" ? field.checked : String(field.value).trim() !== "";
      if (field.type === "email" && valid) valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value);
      field.setAttribute("aria-invalid", valid ? "false" : "true");
      if (!valid && ok) { field.focus(); ok = false; }
    });
    return ok;
  };

  $$("[data-next]", form).forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (validateStep(current)) showStep(current + 1);
    });
  });

  $$("[data-prev]", form).forEach(function (btn) {
    btn.addEventListener("click", function () { showStep(current - 1); });
  });

  /* ─────────────── Estimation indicative en direct ─────────────── */
  var estimateValue = $("#estimate-value");
  var prestation = $("#prestation");
  var surface = $("#surface");
  var frequence = $("#frequence");

  var arrondir = function (n) { return Math.round(n / 5) * 5; };

  var updateEstimate = function () {
    if (!estimateValue || !prestation || !surface || !frequence) return;

    var taux = CONFIG.tarifHoraire[prestation.value] || 27;
    var heures = CONFIG.dureeParSurface[surface.value] || 3;
    var coefficient = parseFloat(frequence.value) || 1;

    var base = taux * heures * coefficient;
    var bas = arrondir(base * 0.9);
    var haut = arrondir(base * 1.12);

    estimateValue.textContent = bas + " € à " + haut + " € HT par passage";
  };

  [prestation, surface, frequence].forEach(function (field) {
    if (field) field.addEventListener("change", updateEstimate);
  });
  updateEstimate();

  /* ─────────────── Envoi ─────────────── */
  var labelPrestation = {
    bureaux: "Nettoyage de bureaux",
    appartement: "Ménage appartement",
    location: "Location courte durée (Airbnb)",
    chantier: "Nettoyage de fin de chantier",
    vitrerie: "Vitrerie",
    copro: "Parties communes / copropriété"
  };

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!validateStep(2)) return;

    var data = new FormData(form);
    var lignes = [
      "Prestation : " + (labelPrestation[data.get("prestation")] || data.get("prestation")),
      "Adresse : " + data.get("adresse"),
      "Surface : environ " + data.get("surface") + " m²",
      "Date souhaitée : " + data.get("date") + " (" + data.get("creneau") + ")",
      "",
      "Nom : " + data.get("nom"),
      "Téléphone : " + data.get("tel"),
      "E-mail : " + data.get("email"),
      "",
      "Précisions : " + (data.get("message") || "—"),
      "",
      "Estimation affichée : " + (estimateValue ? estimateValue.textContent : "—")
    ].join("\n");

    var submitBtn = $("[type=submit]", form);
    if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = "Envoi…"; }

    var done = function () { showStep(3); };

    if (CONFIG.endpoint) {
      fetch(CONFIG.endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(Object.fromEntries(data.entries()))
      })
        .then(done)
        .catch(function () {
          if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = "Recevoir mon tarif"; }
          window.alert(
            "L'envoi a échoué. Appelez-nous au 01 23 45 67 89 ou écrivez à " + CONFIG.email + "."
          );
        });
      return;
    }

    // Sans service d'envoi configuré, on ouvre le client mail du visiteur.
    window.location.href =
      "mailto:" + CONFIG.email +
      "?subject=" + encodeURIComponent("Demande de tarif — " + (labelPrestation[data.get("prestation")] || "MathClean")) +
      "&body=" + encodeURIComponent(lignes);
    done();
  });

  showStep(1);
})();
