/* =========================================================================
   MAISON CÉLESTE — Interactions
   Menu mobile · header au scroll · reveals · filtres olfactifs · formulaires
   ========================================================================= */
(function () {
  'use strict';

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Année dynamique ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Header condensé au scroll ---------- */
  var header = document.getElementById('site-header');
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 40) header.classList.add('is-scrolled');
      else header.classList.remove('is-scrolled');
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Menu mobile ---------- */
  var burger = document.getElementById('burger');
  var mobileNav = document.getElementById('mobile-nav');
  if (burger && mobileNav) {
    var setMenu = function (open) {
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
      mobileNav.classList.toggle('is-open', open);
      document.body.classList.toggle('nav-open', open);
    };
    burger.addEventListener('click', function () {
      setMenu(burger.getAttribute('aria-expanded') !== 'true');
    });
    mobileNav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setMenu(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        burger.focus();
      }
    });
  }

  /* ---------- Hero animé au scroll : le flacon se remplit ---------- */
  var heroScroll = document.getElementById('heroScroll');
  if (heroScroll) {
    var liquid = document.getElementById('hsLiquid');
    var meniscus = document.getElementById('hsMeniscus');
    var glow = document.getElementById('heroGlow');
    var bottle = document.getElementById('heroBottle');
    var fillBar = document.getElementById('fillBar');
    var cue = document.getElementById('scrollCue');
    var caps = Array.prototype.slice.call(heroScroll.querySelectorAll('.hero-cap'));
    var capName = document.getElementById('hsCap');

    var LIQ_BOTTOM = 274, LIQ_MAX = 178; // géométrie du liquide dans le SVG
    var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };

    var setActive = function (name) {
      caps.forEach(function (c) { c.classList.toggle('is-active', c.dataset.cap === name); });
    };

    if (prefersReduced) {
      // Mouvement réduit : flacon plein, titre affiché, pas de scrub.
      heroScroll.classList.add('no-scrub');
      setActive('title');
      if (glow) glow.style.opacity = 0.4;
    } else {
      var ticking = false;
      var render = function () {
        ticking = false;
        var rect = heroScroll.getBoundingClientRect();
        var scrollable = heroScroll.offsetHeight - window.innerHeight;
        var p = scrollable > 0 ? clamp(-rect.top / scrollable, 0, 1) : 0;

        // Remplissage : plein un peu avant la fin (0 → 1 sur 0..0.82)
        var fill = clamp(p / 0.82, 0, 1);
        var top = LIQ_BOTTOM - LIQ_MAX * fill;
        liquid.setAttribute('y', top.toFixed(1));
        liquid.setAttribute('height', (LIQ_MAX * fill).toFixed(1));
        meniscus.setAttribute('cy', top.toFixed(1));
        meniscus.setAttribute('opacity', fill > 0.02 ? '1' : '0');

        // Halo + flottement + léger balancement du flacon
        if (glow) glow.style.opacity = (0.15 + fill * 0.5).toFixed(3);
        if (bottle) bottle.style.transform =
          'translateY(' + (12 - fill * 12).toFixed(1) + 'px) rotate(' + (Math.sin(p * Math.PI * 2) * 1.5).toFixed(2) + 'deg)';
        // Le bouchon se soulève légèrement au début (on "verse")
        if (capName) capName.style.transform = 'translateY(' + (-6 * clamp(1 - p / 0.12, 0, 1)).toFixed(1) + 'px)';
        if (fillBar) fillBar.style.height = (fill * 100).toFixed(1) + '%';

        // Captions selon la progression
        var name = p < 0.15 ? 'title' : p < 0.4 ? 'n1' : p < 0.62 ? 'n2' : p < 0.83 ? 'n3' : 'final';
        setActive(name);
        if (cue) cue.style.opacity = p > 0.88 ? '0' : '1';
      };
      var onHeroScroll = function () {
        if (!ticking) { ticking = true; window.requestAnimationFrame(render); }
      };
      window.addEventListener('scroll', onHeroScroll, { passive: true });
      window.addEventListener('resize', onHeroScroll);
      render();
    }
  }

  /* ---------- Reveals au scroll ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    if (prefersReduced || !('IntersectionObserver' in window)) {
      reveals.forEach(function (el) { el.classList.add('is-in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-in');
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
      reveals.forEach(function (el) {
        if (!el.classList.contains('is-in')) io.observe(el);
      });
    }
  }

  /* ---------- Filtre par famille olfactive (page Collection) ---------- */
  var filterBar = document.getElementById('filter-bar');
  if (filterBar) {
    var cards = document.querySelectorAll('[data-family]');
    filterBar.addEventListener('click', function (e) {
      var chip = e.target.closest('.filter-chip');
      if (!chip) return;
      var family = chip.getAttribute('data-filter');
      filterBar.querySelectorAll('.filter-chip').forEach(function (c) {
        c.classList.toggle('is-active', c === chip);
        c.setAttribute('aria-pressed', String(c === chip));
      });
      cards.forEach(function (card) {
        var match = family === 'all' || card.getAttribute('data-family') === family;
        card.classList.toggle('is-hidden', !match);
      });
    });
  }

  /* ---------- Validation formulaires ---------- */
  var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Newsletter (accueil)
  var nl = document.getElementById('newsletter-form');
  if (nl) {
    nl.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = document.getElementById('nl-email');
      var err = document.getElementById('nl-error');
      var ok = document.getElementById('nl-success');
      if (!emailRe.test(input.value.trim())) {
        if (err) err.style.display = 'block';
        input.focus();
        return;
      }
      if (err) err.style.display = 'none';
      nl.style.display = 'none';
      if (ok) { ok.style.display = 'block'; ok.classList.add('is-visible'); }
    });
  }

  // Formulaire de contact
  var cf = document.getElementById('contact-form');
  if (cf) {
    var fields = cf.querySelectorAll('[data-required]');
    var validate = function (field) {
      var input = field.querySelector('input, textarea');
      var val = input.value.trim();
      var valid = val.length > 0;
      if (input.type === 'email') valid = emailRe.test(val);
      field.classList.toggle('has-error', !valid);
      return valid;
    };
    fields.forEach(function (field) {
      var input = field.querySelector('input, textarea');
      input.addEventListener('blur', function () {
        if (field.classList.contains('has-error')) validate(field);
      });
    });
    cf.addEventListener('submit', function (e) {
      e.preventDefault();
      var allValid = true;
      var first = null;
      fields.forEach(function (field) {
        var ok = validate(field);
        if (!ok && !first) first = field.querySelector('input, textarea');
        allValid = allValid && ok;
      });
      if (!allValid) { if (first) first.focus(); return; }
      cf.reset();
      var success = document.getElementById('contact-success');
      if (success) { success.classList.add('is-visible'); success.scrollIntoView({ behavior: prefersReduced ? 'auto' : 'smooth', block: 'center' }); }
    });
  }
})();
