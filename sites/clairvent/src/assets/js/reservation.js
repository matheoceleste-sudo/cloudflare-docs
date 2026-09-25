/* Clairvent — assistant de réservation en 5 étapes (sans dépendance) */
(function () {
  "use strict";
  var d = document;
  var root = d.getElementById("resa");
  if (!root) return;
  root.hidden = false;
  var form = d.getElementById("resa-form");
  var panels = root.querySelectorAll(".resa-panel");
  var stepBtns = root.querySelectorAll(".resa-steps li");
  var prev = d.getElementById("resa-prev"), next = d.getElementById("resa-next"), submit = d.getElementById("resa-submit");
  var err = d.getElementById("resa-error");
  var step = 1, maxReached = 1, total = panels.length;
  var chosenDate = null;

  /* Pré-remplissage via l'URL : ?prestation=slug&ville=Nom */
  var params = new URLSearchParams(location.search);
  var pre = params.get("prestation");
  if (pre) {
    var box = form.querySelector('input[name="prestations"][data-slug="' + pre + '"]');
    if (box) box.checked = true;
  }
  var villeP = params.get("ville");
  if (villeP) { var v = form.querySelector("#r-ville"); if (v) v.value = villeP; }
  var profP = params.get("profil");
  if (profP) { var p = form.querySelector('input[name="profil"][value="' + profP + '"]'); if (p) p.checked = true; }

  function val(name) {
    var els = form.querySelectorAll('[name="' + name + '"]');
    var out = [];
    els.forEach(function (el) {
      if ((el.type === "checkbox" || el.type === "radio")) { if (el.checked) out.push(el.value); }
      else if (el.value) out.push(el.value);
    });
    return out.join(", ");
  }

  function validate(s) {
    var msg = "";
    if (s === 1) {
      if (!val("profil")) msg = "Indiquez le type d'établissement.";
      else if (!val("prestations")) msg = "Choisissez au moins une prestation.";
    }
    if (s === 3) {
      if (!chosenDate && !form.querySelector("#r-flex").checked) msg = "Choisissez une date dans le calendrier, ou cochez « Je suis flexible ».";
      else if (!val("creneau")) msg = "Choisissez un créneau d'intervention.";
    }
    if (s === 4) {
      var req = form.querySelectorAll('.resa-panel[data-step="4"] [required]');
      for (var i = 0; i < req.length; i++) {
        if (!req[i].checkValidity()) { msg = "Merci de compléter : " + (req[i].dataset.label || req[i].name) + "."; req[i].focus(); break; }
      }
    }
    if (s === 5 && !form.querySelector("#r-rgpd").checked) msg = "Merci d'accepter d'être recontacté pour confirmer le rendez-vous.";
    err.textContent = msg;
    return !msg;
  }

  function go(s) {
    step = Math.max(1, Math.min(total, s));
    maxReached = Math.max(maxReached, step);
    panels.forEach(function (p) { p.hidden = +p.dataset.step !== step; });
    stepBtns.forEach(function (li, i) {
      li.classList.toggle("on", i + 1 === step);
      li.classList.toggle("done", i + 1 < step);
      li.querySelector("button").disabled = i + 1 > maxReached;
    });
    prev.style.visibility = step === 1 ? "hidden" : "visible";
    next.hidden = step === total;
    submit.hidden = step !== total;
    err.textContent = "";
    if (step === total) buildRecap();
    var top = root.getBoundingClientRect().top + window.scrollY - 100;
    if (window.scrollY > top) window.scrollTo({ top: top, behavior: "smooth" });
  }

  next.addEventListener("click", function () { if (validate(step)) go(step + 1); });
  prev.addEventListener("click", function () { go(step - 1); });
  stepBtns.forEach(function (li, i) {
    li.querySelector("button").addEventListener("click", function () {
      if (i + 1 <= maxReached && (i + 1 < step || validate(step))) go(i + 1);
    });
  });

  /* Calendrier */
  var cal = d.getElementById("resa-cal");
  var monthLabel = cal.querySelector("strong");
  var grid = cal.querySelector(".cal-grid");
  var today = new Date(); today.setHours(0, 0, 0, 0);
  var minDate = new Date(today); minDate.setDate(minDate.getDate() + 2);
  var maxDate = new Date(today); maxDate.setDate(maxDate.getDate() + 120);
  var view = new Date(today.getFullYear(), today.getMonth(), 1);
  var fmt = new Intl.DateTimeFormat("fr-FR", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
  function renderCal() {
    monthLabel.textContent = new Intl.DateTimeFormat("fr-FR", { month: "long", year: "numeric" }).format(view);
    grid.innerHTML = "";
    ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"].forEach(function (w) {
      var s = d.createElement("span"); s.className = "dow"; s.textContent = w; grid.appendChild(s);
    });
    var first = (view.getDay() + 6) % 7;
    for (var i = 0; i < first; i++) grid.appendChild(d.createElement("span"));
    var days = new Date(view.getFullYear(), view.getMonth() + 1, 0).getDate();
    for (var day = 1; day <= days; day++) {
      (function (dt) {
        var b = d.createElement("button");
        b.type = "button"; b.textContent = dt.getDate();
        b.setAttribute("aria-label", fmt.format(dt));
        if (dt < minDate || dt > maxDate) b.disabled = true;
        if (+dt === +today) b.classList.add("today");
        if (chosenDate && +dt === +chosenDate) b.classList.add("sel");
        b.addEventListener("click", function () {
          chosenDate = dt;
          form.querySelector("#r-date").value = fmt.format(dt);
          form.querySelector("#r-flex").checked = false;
          renderCal(); updateSummary();
        });
        grid.appendChild(b);
      })(new Date(view.getFullYear(), view.getMonth(), day));
    }
  }
  cal.querySelector("[data-cal-prev]").addEventListener("click", function () {
    var p = new Date(view.getFullYear(), view.getMonth() - 1, 1);
    if (p >= new Date(today.getFullYear(), today.getMonth(), 1)) { view = p; renderCal(); }
  });
  cal.querySelector("[data-cal-next]").addEventListener("click", function () {
    var n = new Date(view.getFullYear(), view.getMonth() + 1, 1);
    if (n <= maxDate) { view = n; renderCal(); }
  });
  form.querySelector("#r-flex").addEventListener("change", function () {
    if (this.checked) { chosenDate = null; form.querySelector("#r-date").value = "Flexible"; renderCal(); }
    updateSummary();
  });
  renderCal();

  /* Récapitulatif */
  var sum = {
    profil: d.getElementById("s-profil"), prestations: d.getElementById("s-presta"),
    date: d.getElementById("s-date"), lieu: d.getElementById("s-lieu")
  };
  function updateSummary() {
    sum.profil.textContent = val("profil") || "—";
    sum.prestations.textContent = val("prestations") || "—";
    var dt = form.querySelector("#r-date").value;
    sum.date.textContent = dt ? dt + (val("creneau") ? " · " + val("creneau") : "") : "—";
    var ville = [val("cp"), val("ville")].filter(Boolean).join(" ");
    sum.lieu.textContent = ville || "—";
  }
  form.addEventListener("change", updateSummary);
  form.addEventListener("input", updateSummary);
  updateSummary();

  function buildRecap() {
    var lines = [
      ["Établissement", val("profil")],
      ["Prestations", val("prestations")],
      ["Nombre de hottes", val("nb_hottes")],
      ["Longueur de hotte", val("longueur")],
      ["Accès à l'extracteur", val("acces")],
      ["Dernier dégraissage", val("dernier")],
      ["Date souhaitée", form.querySelector("#r-date").value],
      ["Créneau", val("creneau")],
      ["Nom", val("nom")],
      ["Établissement / société", val("societe")],
      ["Téléphone", val("tel")],
      ["E-mail", val("email")],
      ["Adresse", [val("adresse"), val("cp"), val("ville")].filter(Boolean).join(" ")],
      ["Précisions", val("message")]
    ];
    var html = "";
    var txt = "";
    lines.forEach(function (l) {
      if (!l[1]) return;
      html += "<dt>" + l[0] + "</dt><dd>" + l[1].replace(/</g, "&lt;") + "</dd>";
      txt += l[0] + " : " + l[1] + "\n";
    });
    d.getElementById("resa-recap-view").innerHTML = html;
    d.getElementById("resa-recap").value = txt;
  }

  form.addEventListener("submit", function (e) {
    if (!validate(5)) { e.preventDefault(); return; }
    buildRecap();
    submit.disabled = true; submit.textContent = "Envoi en cours…";
  });

  go(1);
})();
