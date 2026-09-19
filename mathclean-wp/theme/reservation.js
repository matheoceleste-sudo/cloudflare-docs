/* ==========================================================================
   MathClean — configurateur de réservation.
   Chargé uniquement par reservation.html. Sans JavaScript, le <noscript> de
   la page renvoie vers le formulaire de devis : rien n'est perdu.

   Principes de l'interface :
   — choisir une prestation fait avancer d'elle-même à l'étape suivante ;
   — le total reste visible, y compris sur mobile, grâce à la barre basse ;
   — une erreur s'affiche sous le champ fautif, pas seulement en haut ;
   — l'adresse se saisit par suggestions, ce qui remplit code postal, ville,
     frais de déplacement et délai d'un seul geste.
   ========================================================================== */
(function () {
  'use strict';

  var dataEl = document.getElementById('resa-data');
  var form   = document.getElementById('resa-form');
  if (!dataEl || !form) return;

  var D = JSON.parse(dataEl.textContent);
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var box      = $('#resa');
  var ticket   = $('#resa-ticket');
  var panels   = $$('.resa-panel', form);
  var stepsUI  = $$('#resa-steps li');
  var errBox   = $('#resa-error');
  var btnPrev  = $('#resa-prev');
  var btnNext  = $('#resa-next');
  var btnSend  = $('#resa-send');
  var bar      = $('#resa-bar');
  var barNext  = $('#resa-bar-next');
  var barSend  = $('#resa-bar-send');
  var barTotal = $('#resa-bar-total');

  box.hidden = false;
  ticket.hidden = false;
  bar.hidden = false;

  var step = 1;
  var atteinte = 1;   /* étape la plus avancée visitée : les précédentes sont cliquables */
  var state = { service: null, univers: null, pack: null, options: [], textile: {},
                dep: null, dept: null };

  var eur = function (n) { return Math.round(n) + ' €'; };

  /* -- Créneaux ----------------------------------------------------------- */
  var sel = $('#r-creneau');
  D.creneaux.forEach(function (c) {
    var o = document.createElement('option');
    o.value = c; o.textContent = c;
    sel.appendChild(o);
  });

  /* Première date proposée : demain en petite couronne, après-demain
     ailleurs — proposer un délai que nous ne tenons pas serait pire que
     ne rien proposer. */
  function majDate() {
    var proche = state.dept && D.delais.proches.indexOf(state.dept) >= 0;
    var jours = state.dept ? (proche ? D.delais.jours_proche : D.delais.jours_loin)
                           : D.delais.jours_proche;
    var d = new Date(Date.now() + jours * 86400000);
    var min = d.toISOString().slice(0, 10);
    var champ = $('#r-date');
    champ.min = min;
    if (champ.value && champ.value < min) champ.value = min;

    var note = $('#r-delai');
    if (state.dept) {
      note.innerHTML = 'Dans le <strong>' + state.dept + '</strong>, nous intervenons ' +
        'habituellement sous <strong>' + (proche ? D.delais.proche : D.delais.loin) +
        '</strong>. La date reste une préférence : nous vous la confirmons par téléphone ' +
        'ou par e-mail.';
    }
  }

  /* -- Erreurs : sous le champ concerné ------------------------------------ */
  function nettoyerErreurs() {
    $$('.field-error').forEach(function (e) { e.remove(); });
    $$('.is-wrong').forEach(function (e) { e.classList.remove('is-wrong'); });
    errBox.hidden = true;
  }

  function fail(msg, selecteur) {
    nettoyerErreurs();
    var cible = selecteur && $(selecteur);
    if (cible) {
      cible.classList.add('is-wrong');
      var p = document.createElement('p');
      p.className = 'field-error';
      p.textContent = msg;
      (cible.closest('.field') || cible.parentNode).appendChild(p);
      cible.focus({ preventScroll: true });
      cible.scrollIntoView({ behavior: 'smooth', block: 'center' });
    } else {
      errBox.textContent = msg;
      errBox.hidden = false;
      errBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    return false;
  }

  /* -- Étape 2 : le détail dépend de la prestation choisie ----------------- */
  function buildDetail() {
    var host = $('#resa-detail');
    host.innerHTML = '';
    if (!state.service) return;

    if (state.univers === 'auto') {
      var h = '<p class="resa-intro">Choisissez votre formule. Les quatre packs sont à prix ' +
              'fixe : le même montant pour une citadine et pour un grand véhicule.</p>' +
              '<div class="pack-pick">';
      D.packs.forEach(function (p, i) {
        h += '<label class="pick pick-wide"><input type="radio" name="pack" value="' + i + '">' +
             '<span class="pick-body"><span class="pick-name">' + p.nom + '</span>' +
             '<span class="pick-scope">' + p.portee + '</span>' +
             '<span class="pick-price">' + p.prix + ' €</span>' +
             '<span class="pick-desc">' + p.desc + '</span></span></label>';
      });
      h += '</div><h3 class="resa-sub">Options — facultatives</h3><div class="pack-pick">';
      D.options.forEach(function (o, i) {
        h += '<label class="pick pick-wide"><input type="checkbox" name="opt" value="' + i + '">' +
             '<span class="pick-body"><span class="pick-name">' + o.nom + '</span>' +
             '<span class="pick-price">+ ' + o.prix + ' €</span>' +
             '<span class="pick-desc">' + o.desc + '</span></span></label>';
      });
      host.innerHTML = h + '</div>';

    } else if (state.univers === 'textile') {
      var t = '<p class="resa-intro">Indiquez les quantités. Le déplacement n’est facturé ' +
              'qu’une fois, quel que soit le nombre de pièces.</p><div class="qty-list">';
      D.textile.forEach(function (a, i) {
        t += '<div class="qty-row" id="row' + i + '">' +
             '<div class="qty-id"><strong>' + a.nom + '</strong><span>' + a.desc + '</span></div>' +
             '<div class="qty-price">' + a.prix + ' €<em class="qty-sub" id="sub' + i + '"></em></div>' +
             '<div class="qty-ctl">' +
             '<button type="button" class="qty-btn" data-i="' + i + '" data-d="-1" ' +
             'aria-label="Retirer un ' + a.nom + '">−</button>' +
             '<output id="q' + i + '" aria-live="polite">0</output>' +
             '<button type="button" class="qty-btn" data-i="' + i + '" data-d="1" ' +
             'aria-label="Ajouter un ' + a.nom + '">+</button></div></div>';
      });
      host.innerHTML = t + '</div>';

    } else {
      host.innerHTML =
        '<div class="notice notice-blue"><p><strong>' + state.nav + '</strong> se chiffre au ' +
        'cas par cas : surface, état et accès changent tout. Nous établissons un ' +
        '<strong>devis gratuit et ferme</strong> sous ' + D.delais.reponse_txt + ', souvent sur ' +
        'la base de quelques photos.</p></div>' +
        '<div class="field field-full" style="margin-top:18px">' +
        '<label for="r-brief">Décrivez ce qu’il y a à nettoyer <span class="req">*</span></label>' +
        '<textarea id="r-brief" name="Descriptif" style="min-height:130px" ' +
        'placeholder="' + state.exemple + '"></textarea>' +
        '<span class="field-hint">Surface approximative, nombre de pièces ou de vitrages, ' +
        'fréquence souhaitée : tout ce que vous savez nous évite un aller-retour.</span></div>';
    }
    bindDetail();
    draw();
  }

  function bindDetail() {
    $$('input[name="pack"]').forEach(function (r) {
      r.addEventListener('change', function () {
        state.pack = parseInt(r.value, 10);
        nettoyerErreurs();
        draw();
      });
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
        $('#sub' + i).textContent = q ? '× ' + q + ' = ' + (D.textile[i].prix * q) + ' €' : '';
        $('#row' + i).classList.toggle('is-picked', q > 0);
        nettoyerErreurs();
        draw();
      });
    });
  }

  /* -- Récapitulatif et total --------------------------------------------- */
  function compute() {
    var lines = [], total = 0, devis = false;

    if (state.univers === 'auto' && state.pack !== null) {
      var p = D.packs[state.pack];
      lines.push({ t: p.nom, p: eur(p.prix) });
      total += p.prix;
      state.options.forEach(function (i) {
        var o = D.options[i];
        lines.push({ t: o.nom, p: '+ ' + o.prix + ' €' });
        total += o.prix;
      });
    } else if (state.univers === 'textile') {
      Object.keys(state.textile).forEach(function (i) {
        var q = state.textile[i];
        if (!q) return;
        var a = D.textile[i];
        lines.push({ t: a.nom + ' × ' + q, p: eur(a.prix * q) });
        total += a.prix * q;
      });
    } else if (state.service) {
      lines.push({ t: state.nav, p: 'sur devis' });
      devis = true;
    }

    if (state.dep && state.dep.eur > 0) {
      lines.push({ t: 'Déplacement (environ ' + state.dep.km + ' km)', p: eur(state.dep.eur) });
      total += state.dep.eur;
    }
    return { lines: lines, total: total, devis: devis };
  }

  function draw() {
    var r = compute();
    var ul = $('#resa-lines');
    ul.innerHTML = r.lines.length
      ? r.lines.map(function (l) { return '<li><span>' + l.t + '</span><b>' + l.p + '</b></li>'; }).join('')
      : '<li class="resa-empty">Rien de sélectionné pour l’instant.</li>';

    var txt;
    if (!r.lines.length) txt = '—';
    else if (r.devis) txt = r.total > 0 ? 'Sur devis + ' + eur(r.total) : 'Sur devis';
    else txt = eur(r.total);

    $('#resa-presta').value = state.nav || '';
    $('#resa-total').textContent = txt;
    barTotal.textContent = txt;
    $('#resa-total-field').value = txt;
    $('#resa-recap').value = r.lines.map(function (l) { return l.t + ' : ' + l.p; }).join(' | ');

    var fin = $('#resa-final');
    if (fin) {
      fin.innerHTML = r.lines.length
        ? '<h3>Votre demande</h3><ul>' +
          r.lines.map(function (l) { return '<li><span>' + l.t + '</span><b>' + l.p + '</b></li>'; }).join('') +
          '</ul><p class="resa-final-total"><span>Total estimé</span><strong>' + txt + '</strong></p>' +
          '<p class="field-hint">Besoin de corriger quelque chose ? Les étapes ci-dessus restent ' +
          'cliquables.</p>'
        : '';
    }
  }

  /* -- Frais de déplacement et suggestions d'adresse ----------------------- */
  /* L'API Adresse (data.gouv.fr) sert deux fois : à compléter l'adresse
     pendant la frappe, puis à situer le point pour le déplacement. */
  var acTimer = null, acItems = [], acIndex = -1;
  var champAdr = $('#r-adr'), listeAdr = $('#r-adr-list');

  function volDoiseau(la1, lo1, la2, lo2) {
    var R = 6371, r = Math.PI / 180;
    var dLa = (la2 - la1) * r, dLo = (lo2 - lo1) * r;
    var a = Math.sin(dLa / 2) * Math.sin(dLa / 2) +
            Math.cos(la1 * r) * Math.cos(la2 * r) * Math.sin(dLo / 2) * Math.sin(dLo / 2);
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  }

  function poserDeplacement(lat, lon) {
    var dep = D.deplacement;
    var km = volDoiseau(dep.lat, dep.lon, lat, lon) * dep.coef_route;
    var fee = Math.ceil(km / dep.palier_km) * dep.palier_eur;
    state.dep = { km: km < 10 ? Math.round(km * 10) / 10 : Math.round(km), eur: fee };
    $('#r-dep').innerHTML =
      'Environ <strong>' + state.dep.km + ' km</strong> depuis notre atelier, soit ' +
      '<strong>' + fee + ' €</strong> de déplacement, déjà ajoutés au total. ' +
      'Toute tranche de 5 km entamée est due ; le retour n’est pas facturé.';
    draw();
  }

  function fermerListe() {
    listeAdr.hidden = true;
    listeAdr.innerHTML = '';
    champAdr.setAttribute('aria-expanded', 'false');
    acItems = []; acIndex = -1;
  }

  function choisir(i) {
    var f = acItems[i];
    if (!f) return;
    champAdr.value = f.properties.name || f.properties.label;
    $('#r-cp').value = f.properties.postcode || '';
    $('#r-ville').value = f.properties.city || '';
    state.dept = (f.properties.postcode || '').slice(0, 2);
    fermerListe();
    nettoyerErreurs();
    majDate();
    poserDeplacement(f.geometry.coordinates[1], f.geometry.coordinates[0]);
  }

  function suggerer() {
    var q = champAdr.value.trim();
    if (q.length < 4) { fermerListe(); return; }
    fetch('https://api-adresse.data.gouv.fr/search/?limit=5&q=' + encodeURIComponent(q))
      .then(function (res) { if (!res.ok) throw 0; return res.json(); })
      .then(function (j) {
        acItems = (j.features || []).filter(function (f) {
          return f.properties && f.properties.label;
        });
        if (!acItems.length) { fermerListe(); return; }
        listeAdr.innerHTML = acItems.map(function (f, i) {
          return '<li role="option" id="ac' + i + '" data-i="' + i + '">' +
                 f.properties.label + '</li>';
        }).join('');
        listeAdr.hidden = false;
        champAdr.setAttribute('aria-expanded', 'true');
        acIndex = -1;
      })
      .catch(fermerListe);
  }

  champAdr.addEventListener('input', function () {
    clearTimeout(acTimer);
    acTimer = setTimeout(suggerer, 250);
  });
  champAdr.addEventListener('keydown', function (e) {
    if (listeAdr.hidden) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      acIndex += (e.key === 'ArrowDown' ? 1 : -1);
      if (acIndex < 0) acIndex = acItems.length - 1;
      if (acIndex >= acItems.length) acIndex = 0;
      $$('li', listeAdr).forEach(function (li, i) { li.classList.toggle('is-on', i === acIndex); });
    } else if (e.key === 'Enter' && acIndex >= 0) {
      e.preventDefault();
      choisir(acIndex);
    } else if (e.key === 'Escape') {
      fermerListe();
    }
  });
  listeAdr.addEventListener('mousedown', function (e) {
    var li = e.target.closest('li[data-i]');
    if (li) { e.preventDefault(); choisir(parseInt(li.getAttribute('data-i'), 10)); }
  });
  champAdr.addEventListener('blur', function () { setTimeout(fermerListe, 150); });

  /* Saisie manuelle du code postal et de la ville : même calcul, sans
     suggestion. Un visiteur qui refuse les suggestions n'est pas pénalisé. */
  var depTimer = null;
  function calcDep() {
    var cp = $('#r-cp').value.trim(), ville = $('#r-ville').value.trim();
    state.dept = cp.slice(0, 2) || null;
    majDate();
    if (!cp && !ville) {
      state.dep = null;
      $('#r-dep').textContent = 'Renseignez votre adresse pour connaître les frais de déplacement.';
      draw();
      return;
    }
    var q = [champAdr.value, cp, ville].join(' ').trim();
    $('#r-dep').textContent = 'Calcul en cours…';
    fetch('https://api-adresse.data.gouv.fr/search/?limit=1&q=' + encodeURIComponent(q))
      .then(function (res) { if (!res.ok) throw 0; return res.json(); })
      .then(function (j) {
        if (!j.features || !j.features.length) throw 0;
        var c = j.features[0].geometry.coordinates;   /* [lon, lat] */
        poserDeplacement(c[1], c[0]);
      })
      .catch(function () {
        state.dep = null;
        $('#r-dep').textContent = 'Adresse non reconnue. Ce n’est pas bloquant : nous calculons ' +
                                  'les frais de déplacement et vous les annonçons avant de valider.';
        draw();
      });
  }
  ['#r-cp', '#r-ville'].forEach(function (s) {
    $(s).addEventListener('input', function () {
      clearTimeout(depTimer);
      depTimer = setTimeout(calcDep, 600);
    });
  });

  /* -- Étape 1 : choix de la prestation, qui fait avancer ------------------ */
  $$('input[name="univers"]').forEach(function (r) {
    r.addEventListener('change', function () {
      var s = D.services.filter(function (x) { return x.slug === r.value; })[0];
      state.service = s.slug;
      state.univers = s.univers;
      state.nav = s.nav;
      state.exemple = s.exemple;
      state.pack = null; state.options = []; state.textile = {};
      buildDetail();
      nettoyerErreurs();
      /* Le choix vaut validation de l'étape : enchaîner évite un clic. */
      setTimeout(function () { show(2); }, 180);
    });
  });

  /* -- Navigation entre les étapes ---------------------------------------- */
  function show(n) {
    step = n;
    atteinte = Math.max(atteinte, n);
    panels.forEach(function (p) { p.classList.toggle('is-on', +p.getAttribute('data-step') === n); });
    stepsUI.forEach(function (li, i) {
      li.classList.toggle('is-on', i + 1 === n);
      li.classList.toggle('is-done', i + 1 < atteinte && i + 1 !== n);
      var b = $('button', li);
      b.disabled = i + 1 > atteinte;
      b.setAttribute('aria-current', i + 1 === n ? 'step' : 'false');
    });
    btnPrev.hidden = n === 1;
    btnNext.hidden = n === 4;
    btnSend.hidden = n !== 4;
    barNext.hidden = n === 4;
    barSend.hidden = n !== 4;
    nettoyerErreurs();
    box.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function valid(n) {
    if (n === 1 && !state.service) return fail('Choisissez d’abord une prestation.');
    if (n === 2) {
      if (state.univers === 'auto' && state.pack === null)
        return fail('Choisissez une formule parmi les quatre.');
      if (state.univers === 'textile') {
        var total = Object.keys(state.textile).reduce(function (a, k) { return a + state.textile[k]; }, 0);
        if (!total) return fail('Indiquez au moins une pièce à nettoyer, avec le bouton +.');
      }
      if (state.univers === 'devis' && !$('#r-brief').value.trim())
        return fail('Décrivez brièvement ce qu’il y a à nettoyer.', '#r-brief');
    }
    if (n === 3) {
      if (!$('#r-cp').value.trim())
        return fail('Indiquez votre code postal.', '#r-cp');
      if (!$('#r-ville').value.trim())
        return fail('Indiquez votre ville.', '#r-ville');
      if (!$('#r-date').value)
        return fail('Choisissez une date souhaitée.', '#r-date');
    }
    return true;
  }

  function suivant() { if (valid(step)) show(step + 1); }
  btnNext.addEventListener('click', suivant);
  barNext.addEventListener('click', suivant);
  btnPrev.addEventListener('click', function () { show(step - 1); });

  /* Revenir sur une étape déjà franchie, en un clic. */
  stepsUI.forEach(function (li, i) {
    $('button', li).addEventListener('click', function () {
      if (i + 1 <= atteinte) show(i + 1);
    });
  });

  form.addEventListener('submit', function (e) {
    var manquant = [['#r-nom', 'votre nom'], ['#r-tel', 'votre téléphone'],
                    ['#r-mail', 'votre e-mail']].filter(function (c) {
      return !$(c[0]).value.trim();
    })[0];
    if (manquant) {
      e.preventDefault();
      fail('Renseignez ' + manquant[1] + ' pour que nous puissions vous répondre.', manquant[0]);
      return;
    }
    if (!$('#r-ok').checked) {
      e.preventDefault();
      fail('Cochez la case pour accepter d’être recontacté au sujet de cette réservation.', '#r-ok');
      return;
    }
    draw();
    /* Les boutons de choix portent des valeurs techniques (un slug, un
       index). Le récapitulatif dit déjà la même chose en clair : on les
       neutralise pour que l'e-mail reçu reste lisible. */
    $$('[name="univers"],[name="pack"],[name="opt"]').forEach(function (e) { e.disabled = true; });
  });

  majDate();
  show(1);
  draw();
})();
