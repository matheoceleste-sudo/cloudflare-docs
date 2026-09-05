/* ==========================================================================
   MathClean — configurateur de réservation.
   Chargé uniquement par reservation.html. Sans JavaScript, le <noscript> de
   la page renvoie vers le formulaire de devis : rien n'est perdu.
   ========================================================================== */
(function () {
  'use strict';

  var dataEl = document.getElementById('resa-data');
  var form   = document.getElementById('resa-form');
  if (!dataEl || !form) return;

  var D = JSON.parse(dataEl.textContent);
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var box     = $('#resa');
  var ticket  = $('#resa-ticket');
  var panels  = $$('.resa-panel', form);
  var stepsUI = $$('#resa-steps li');
  var errBox  = $('#resa-error');
  var btnPrev = $('#resa-prev');
  var btnNext = $('#resa-next');
  var btnSend = $('#resa-send');

  box.hidden = false;
  ticket.hidden = false;

  var step = 1;
  var state = { service: null, univers: null, pack: null, options: [], textile: {}, dep: null };

  var eur = function (n) { return Math.round(n) + ' €'; };

  /* -- Créneaux et date minimale ------------------------------------------ */
  var sel = $('#r-creneau');
  D.creneaux.forEach(function (c) {
    var o = document.createElement('option');
    o.value = c; o.textContent = c;
    sel.appendChild(o);
  });
  var demain = new Date(Date.now() + 86400000);
  $('#r-date').min = demain.toISOString().slice(0, 10);

  /* -- Étape 2 : le détail dépend de la prestation choisie ----------------- */
  function buildDetail() {
    var host = $('#resa-detail');
    host.innerHTML = '';
    if (!state.service) return;

    if (state.univers === 'auto') {
      var h = '<p class="resa-intro">Choisissez votre formule. La fourchette va de la citadine au grand véhicule ; le montant exact vous est confirmé avant l’intervention.</p><div class="pack-pick">';
      D.packs.forEach(function (p, i) {
        h += '<label class="pick pick-wide"><input type="radio" name="pack" value="' + i + '">' +
             '<span class="pick-body"><span class="pick-name">' + p.nom + '</span>' +
             '<span class="pick-scope">' + p.portee + '</span>' +
             '<span class="pick-price">' + p.min + ' € à ' + p.max + ' €</span>' +
             '<span class="pick-desc">' + p.desc + '</span></span></label>';
      });
      h += '</div><h3 class="resa-sub">Options</h3><div class="pack-pick">';
      D.options.forEach(function (o, i) {
        h += '<label class="pick pick-wide"><input type="checkbox" name="opt" value="' + i + '">' +
             '<span class="pick-body"><span class="pick-name">' + o.nom + '</span>' +
             '<span class="pick-price">+ ' + o.prix + ' €</span>' +
             '<span class="pick-desc">' + o.desc + '</span></span></label>';
      });
      host.innerHTML = h + '</div>';

    } else if (state.univers === 'textile') {
      var t = '<p class="resa-intro">Indiquez les quantités. Le déplacement n’est facturé qu’une fois, quel que soit le nombre de pièces.</p><div class="qty-list">';
      D.textile.forEach(function (a, i) {
        t += '<div class="qty-row"><div><strong>' + a.nom + '</strong><span>' + a.desc + '</span></div>' +
             '<div class="qty-price">' + a.prix + ' €</div>' +
             '<div class="qty-ctl"><button type="button" class="qty-btn" data-i="' + i + '" data-d="-1" aria-label="Retirer un ' + a.nom + '">−</button>' +
             '<output id="q' + i + '">0</output>' +
             '<button type="button" class="qty-btn" data-i="' + i + '" data-d="1" aria-label="Ajouter un ' + a.nom + '">+</button></div></div>';
      });
      host.innerHTML = t + '</div>';

    } else {
      host.innerHTML =
        '<div class="notice notice-blue"><p><strong>' + state.nav + '</strong> se chiffre au cas par cas : ' +
        'surface, état et accès changent tout. Nous établissons un <strong>devis gratuit et ferme</strong> ' +
        'après échange — souvent sur la base de quelques photos.</p></div>' +
        '<div class="field field-full" style="margin-top:18px">' +
        '<label for="r-brief">Décrivez ce qu’il y a à nettoyer <span class="req">*</span></label>' +
        '<textarea id="r-brief" name="Descriptif" style="min-height:130px" ' +
        'placeholder="Exemple : terrasse en bois exotique d’environ 30 m², très grisée, accès par le garage."></textarea></div>';
    }
    bindDetail();
    draw();
  }

  function bindDetail() {
    $$('input[name="pack"]').forEach(function (r) {
      r.addEventListener('change', function () { state.pack = parseInt(r.value, 10); draw(); });
    });
    $$('input[name="opt"]').forEach(function (c) {
      c.addEventListener('change', function () {
        var i = parseInt(c.value, 10);
        var at = state.options.indexOf(i);
        if (c.checked && at < 0) state.options.push(i);
        if (!c.checked && at >= 0) state.options.splice(at, 1);
        draw();
      });
    });
    $$('.qty-btn').forEach(function (b) {
      b.addEventListener('click', function () {
        var i = b.getAttribute('data-i');
        var d = parseInt(b.getAttribute('data-d'), 10);
        var q = Math.max(0, (state.textile[i] || 0) + d);
        state.textile[i] = q;
        $('#q' + i).textContent = q;
        draw();
      });
    });
  }

  /* -- Récapitulatif et total --------------------------------------------- */
  function compute() {
    var lines = [], min = 0, max = 0;

    if (state.univers === 'auto' && state.pack !== null) {
      var p = D.packs[state.pack];
      lines.push({ t: p.nom, p: p.min + ' € à ' + p.max + ' €' });
      min += p.min; max += p.max;
      state.options.forEach(function (i) {
        var o = D.options[i];
        lines.push({ t: o.nom, p: '+ ' + o.prix + ' €' });
        min += o.prix; max += o.prix;
      });
    } else if (state.univers === 'textile') {
      Object.keys(state.textile).forEach(function (i) {
        var q = state.textile[i];
        if (!q) return;
        var a = D.textile[i];
        lines.push({ t: a.nom + ' × ' + q, p: eur(a.prix * q) });
        min += a.prix * q; max += a.prix * q;
      });
    } else if (state.service) {
      lines.push({ t: state.nav, p: 'sur devis' });
    }

    if (state.dep && state.dep.eur > 0) {
      lines.push({ t: 'Déplacement (' + state.dep.km + ' km)', p: eur(state.dep.eur) });
      min += state.dep.eur; max += state.dep.eur;
    }
    return { lines: lines, min: min, max: max };
  }

  function draw() {
    var r = compute();
    var ul = $('#resa-lines');
    ul.innerHTML = r.lines.length
      ? r.lines.map(function (l) { return '<li><span>' + l.t + '</span><b>' + l.p + '</b></li>'; }).join('')
      : '<li class="resa-empty">Rien de sélectionné pour l’instant.</li>';

    var txt;
    if (!r.lines.length) txt = '—';
    else if (r.max === 0) txt = 'Sur devis';
    else txt = (r.min === r.max) ? eur(r.min) : eur(r.min) + ' à ' + eur(r.max);

    $('#resa-total').textContent = txt;
    $('#resa-total-field').value = txt;
    $('#resa-recap').value = r.lines.map(function (l) { return l.t + ' : ' + l.p; }).join(' | ');
  }

  /* -- Frais de déplacement (API Adresse, data.gouv.fr) -------------------- */
  var depTimer = null;
  function volDoiseau(la1, lo1, la2, lo2) {
    var R = 6371, r = Math.PI / 180;
    var dLa = (la2 - la1) * r, dLo = (lo2 - lo1) * r;
    var a = Math.sin(dLa / 2) * Math.sin(dLa / 2) +
            Math.cos(la1 * r) * Math.cos(la2 * r) * Math.sin(dLo / 2) * Math.sin(dLo / 2);
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  }
  function calcDep() {
    var q = [$('#r-adr').value, $('#r-cp').value, $('#r-ville').value].join(' ').trim();
    var out = $('#r-dep');
    if (!$('#r-cp').value.trim() && !$('#r-ville').value.trim()) {
      state.dep = null;
      out.textContent = 'Renseignez votre adresse pour connaître les frais de déplacement.';
      draw();
      return;
    }
    out.textContent = 'Calcul en cours…';
    fetch('https://api-adresse.data.gouv.fr/search/?limit=1&q=' + encodeURIComponent(q))
      .then(function (res) { if (!res.ok) throw 0; return res.json(); })
      .then(function (j) {
        if (!j.features || !j.features.length) throw 0;
        var c = j.features[0].geometry.coordinates;   /* [lon, lat] */
        var dep = D.deplacement;
        var km = volDoiseau(dep.lat, dep.lon, c[1], c[0]) * dep.coef_route;
        var fee = Math.ceil(km / dep.palier_km) * dep.palier_eur;
        state.dep = { km: km < 10 ? Math.round(km * 10) / 10 : Math.round(km), eur: fee };
        out.innerHTML = 'Environ <strong>' + state.dep.km + ' km</strong> depuis notre atelier — ' +
                        'frais de déplacement : <strong>' + fee + ' €</strong>, ajoutés au total.';
        draw();
      })
      .catch(function () {
        state.dep = null;
        out.textContent = 'Adresse non reconnue. Ce n’est pas bloquant : nous calculons les frais ' +
                          'de déplacement et vous les annonçons avant de valider.';
        draw();
      });
  }
  ['#r-adr', '#r-cp', '#r-ville'].forEach(function (s) {
    $(s).addEventListener('input', function () {
      clearTimeout(depTimer);
      depTimer = setTimeout(calcDep, 600);
    });
  });

  /* -- Étape 1 : choix de la prestation ------------------------------------ */
  $$('input[name="univers"]').forEach(function (r) {
    r.addEventListener('change', function () {
      var s = D.services.filter(function (x) { return x.slug === r.value; })[0];
      state.service = s.slug;
      state.univers = s.univers;
      state.nav = s.nav;
      state.pack = null; state.options = []; state.textile = {};
      buildDetail();
    });
  });

  /* -- Navigation entre les étapes ---------------------------------------- */
  function show(n) {
    step = n;
    panels.forEach(function (p) { p.classList.toggle('is-on', +p.getAttribute('data-step') === n); });
    stepsUI.forEach(function (li, i) {
      li.classList.toggle('is-on', i + 1 === n);
      li.classList.toggle('is-done', i + 1 < n);
    });
    btnPrev.hidden = n === 1;
    btnNext.hidden = n === 4;
    btnSend.hidden = n !== 4;
    errBox.hidden = true;
    box.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function fail(msg) {
    errBox.textContent = msg;
    errBox.hidden = false;
    return false;
  }

  function valid(n) {
    if (n === 1 && !state.service) return fail('Choisissez d’abord une prestation.');
    if (n === 2) {
      if (state.univers === 'auto' && state.pack === null) return fail('Choisissez une formule.');
      if (state.univers === 'textile') {
        var total = Object.keys(state.textile).reduce(function (a, k) { return a + state.textile[k]; }, 0);
        if (!total) return fail('Indiquez au moins une pièce à nettoyer.');
      }
      if (state.univers === 'devis' && !$('#r-brief').value.trim())
        return fail('Décrivez brièvement ce qu’il y a à nettoyer.');
    }
    if (n === 3) {
      if (!$('#r-cp').value.trim() || !$('#r-ville').value.trim())
        return fail('Indiquez au moins le code postal et la ville.');
      if (!$('#r-date').value) return fail('Choisissez une date souhaitée.');
    }
    return true;
  }

  btnNext.addEventListener('click', function () { if (valid(step)) show(step + 1); });
  btnPrev.addEventListener('click', function () { show(step - 1); });

  form.addEventListener('submit', function (e) {
    var ok = ['#r-nom', '#r-tel', '#r-mail'].every(function (s) { return $(s).value.trim(); });
    if (!ok || !$('#r-ok').checked) {
      e.preventDefault();
      fail('Renseignez vos nom, téléphone et e-mail, puis acceptez d’être recontacté.');
      return;
    }
    draw();
  });

  show(1);
  draw();
})();
