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
