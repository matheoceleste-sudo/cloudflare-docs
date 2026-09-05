/* ==========================================================================
   MathClean — scripts du thème. Vanilla JS, aucune dépendance.
   Chargé en <script defer>, donc le DOM est prêt à l'exécution.
   ========================================================================== */
(function () {
  'use strict';

  var $  = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  /* -- 1. Menu mobile ----------------------------------------------------- */
  var nav      = $('#site-nav');
  var toggle   = $('#nav-toggle');
  var backdrop = $('#nav-backdrop');

  function closeNav() {
    if (!nav) return;
    nav.classList.remove('is-open');
    if (backdrop) backdrop.classList.remove('is-on');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (backdrop) backdrop.classList.toggle('is-on', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
  }
  if (backdrop) backdrop.addEventListener('click', closeNav);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeNav(); });

  /* Sous-menus : au clic en mobile, au survol en desktop (géré en CSS). */
  $$('.menu-item-has-children > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth > 1080) return;
      e.preventDefault();
      link.parentNode.classList.toggle('is-open');
    });
  });

  /* Referme le menu quand on repasse en desktop. */
  var mq = window.matchMedia('(min-width:1081px)');
  (mq.addEventListener ? mq.addEventListener.bind(mq, 'change') : mq.addListener.bind(mq))(function (e) {
    if (e.matches) closeNav();
  });

  /* -- 2. En-tête collant + bouton « haut de page » ------------------------ */
  var header = $('.site-header');
  var toTop  = $('#to-top');

  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;
    if (header) header.classList.toggle('is-stuck', y > 8);
    if (toTop)  toTop.classList.toggle('is-on', y > 550);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (toTop) {
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* -- 3. Apparition des blocs au défilement ------------------------------ */
  var revealables = $$('.reveal');
  var showAll = function () {
    revealables.forEach(function (el) { el.classList.add('is-visible'); });
  };

  if (revealables.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        });
      }, { rootMargin: '0px 0px -60px 0px', threshold: 0.08 });
      revealables.forEach(function (el) { io.observe(el); });

      /* Filet de sécurité : si l'observateur n'a rien déclenché (capture
         d'écran, impression, onglet en arrière-plan), on affiche tout. */
      window.setTimeout(showAll, 2500);
      window.addEventListener('beforeprint', showAll);
    } else {
      showAll();
    }
  }

  /* -- 4. Comparateurs avant / après -------------------------------------- */
  $$('.ba').forEach(function (box) {
    var range = $('.ba-range', box);
    if (!range) return;
    var apply = function () { box.style.setProperty('--pos', range.value + '%'); };
    range.addEventListener('input', apply);
    apply();
  });

  /* -- 5. FAQ : une seule réponse ouverte à la fois ------------------------ */
  $$('[data-faq]').forEach(function (group) {
    var items = $$('details', group);
    items.forEach(function (item) {
      item.addEventListener('toggle', function () {
        if (!item.open) return;
        items.forEach(function (other) { if (other !== item) other.open = false; });
      });
    });
  });

  /* -- 6. Estimation indicative sur la page devis -------------------------- */
  var estimator = $('#estimateur');
  if (estimator) {
    var choix  = $('#f-prestation', estimator);
    var sortie = $('#estimation', estimator);
    var repere = {
      'Nettoyage automobile'          : 'À partir de 40 € (Extérieur Éclat) — 120 € pour l’Intégral.',
      'Nettoyage textile'             : 'À partir de 15 € la chaise, 39 € le canapé 2 places, 49 € le matelas 2 places.',
      'Nettoyage de bateau'           : 'Sur devis, après échange sur la taille et l’état du bateau.',
      'Nettoyage de terrasse'         : 'Sur devis, selon la surface et le matériau (bois, pierre, béton).',
      'Nettoyage de vitres'           : 'Sur devis, selon le nombre et l’accessibilité des ouvrants.',
      'Nettoyage pour entreprise'     : 'Sur devis, en passage ponctuel ou régulier.',
      'Nettoyage de fin de chantier'  : 'Sur devis, selon la surface et l’ampleur des travaux.'
    };
    var maj = function () {
      var v = choix.value;
      if (!v || !repere[v]) { sortie.hidden = true; return; }
      $('#estimation-txt', estimator).textContent = repere[v];
      sortie.hidden = false;
    };
    choix.addEventListener('change', maj);
    maj();
  }

  /* Pré-sélection de la prestation via ?prestation=… (liens « Réserver »). */
  var presta = new URLSearchParams(window.location.search).get('prestation');
  if (presta) {
    var select = $('#f-prestation');
    if (select) {
      $$('option', select).forEach(function (opt) {
        if (opt.value.toLowerCase().indexOf(presta.toLowerCase()) === 0) {
          select.value = opt.value;
          select.dispatchEvent(new Event('change'));
        }
      });
    }
  }

  /* -- 7. Bandeau cookies (information, pas de traceur publicitaire) ------- */
  var bar = $('#cookie-bar');
  if (bar) {
    var KEY = 'mcCookies';
    var seen;
    try { seen = localStorage.getItem(KEY); } catch (e) { seen = '1'; }
    if (!seen) bar.classList.add('is-on');
    var accept = $('#cookie-ok', bar);
    if (accept) {
      accept.addEventListener('click', function () {
        bar.classList.remove('is-on');
        try { localStorage.setItem(KEY, '1'); } catch (e) {}
      });
    }
  }

  /* -- 8. Année courante dans le pied de page ----------------------------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
