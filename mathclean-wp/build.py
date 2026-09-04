#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du site MathClean.

Le principe est celui d'un thème WordPress : des gabarits partagés (en-tête,
pied de page, colonne latérale, cartes) assemblés avec le contenu de
`content.py`. Le résultat est un site 100 % statique, à déposer tel quel chez
n'importe quel hébergeur.

    python3 build.py

Sortie : ./site/
"""

import json
import os
import shutil
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from content import (  # noqa: E402
    SITE, SERVICES, ZONES, POSTS, FAQ, ENGAGEMENTS, BEFORE_AFTER,
    PACKS_AUTO, OPTIONS_AUTO, TARIFS_TEXTILE, TARIFS_DEVIS,
)

OUT = os.path.join(HERE, "site")
TODAY = date.today().isoformat()

# ---------------------------------------------------------------------------
# Jeu d'icônes (contours 24×24, héritent de currentColor)
# ---------------------------------------------------------------------------
ICONS = {
    "car":      '<path d="M5 17h14M6.5 17V9.7l1.7-3.9A2 2 0 0 1 10 4.6h4a2 2 0 0 1 1.8 1.2l1.7 3.9V17M4 12h16"/><circle cx="8" cy="17" r="1.6"/><circle cx="16" cy="17" r="1.6"/>',
    "sofa":     '<path d="M3 17v-5.5A2.5 2.5 0 0 1 5.5 9h13A2.5 2.5 0 0 1 21 11.5V17M3 17h18M5 17v2M19 17v2M6 9V7a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v2"/>',
    "boat":     '<path d="M4 17l1.6-5.6a1 1 0 0 1 .96-.72h10.88a1 1 0 0 1 .96.72L20 17M12 10.7V4.4M12 4.4l4.6 2.3-4.6 2M2.6 19.6c1.6 0 1.6 1.2 3.2 1.2s1.6-1.2 3.2-1.2 1.6 1.2 3.2 1.2 1.6-1.2 3.2-1.2 1.6 1.2 3.2 1.2"/>',
    "plane":    '<path d="M12 3c.7 0 1.25.58 1.25 1.3v4.4l7.35 4.1v1.85l-7.35-2.2v3.9l2.3 1.7v1.4L12 18.55 8.45 19.8v-1.4l2.3-1.7v-3.9L3.4 15v-1.85l7.35-4.1V4.3C10.75 3.58 11.3 3 12 3z"/>',
    "deck":     '<path d="M2.4 20h19.2M4.3 15.9h15.4M6.2 11.8h11.6M8.1 7.7h7.8M12 7.7V20"/>',
    "window":   '<rect x="3.4" y="3.4" width="17.2" height="17.2" rx="1.6"/><path d="M12 3.4V20.6M3.4 12h17.2"/>',
    "building": '<path d="M3 21h18M5 21V6.4a1 1 0 0 1 .7-.95l7-2.3a1 1 0 0 1 1.3.95V21M19 21v-9.4a1 1 0 0 0-.7-.95L14 9.2M8.6 8.4h1.8M8.6 12h1.8M8.6 15.6h1.8"/>',
    "tools":    '<path d="M14.6 5.4a3.6 3.6 0 0 0-5 4.6l-6.2 6.2a1.6 1.6 0 0 0 0 2.3l2.1 2.1a1.6 1.6 0 0 0 2.3 0l6.2-6.2a3.6 3.6 0 0 0 4.6-5l-2.6 2.6-2.5-.5-.5-2.5z"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "quote":    '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    "clock":    '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 1.9"/>',
    "shield":   '<path d="M12 3l7.5 3v5.4c0 4.3-3 8.2-7.5 9.6-4.5-1.4-7.5-5.3-7.5-9.6V6z"/><path d="M9.2 12.1l2 2 3.6-3.9"/>',
    "truck":    '<path d="M3 7.5A1.5 1.5 0 0 1 4.5 6H14v10H3z"/><path d="M14 9.5h3.6a2 2 0 0 1 1.7.95l1.4 2.3a2 2 0 0 1 .3 1.05V16h-7z"/><circle cx="7" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/>',
    "wallet":   '<path d="M3 7.5A2.5 2.5 0 0 1 5.5 5H18a1 1 0 0 1 1 1v2"/><path d="M3 7.5V18a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a1 1 0 0 0-1-1H5.5A2.5 2.5 0 0 1 3 7.5z"/><circle cx="16.5" cy="14" r="1.1"/>',
    "phone":    '<path d="M6.6 3.5h3l1.5 3.8-2 1.3a12 12 0 0 0 5.3 5.3l1.3-2 3.8 1.5v3a1.9 1.9 0 0 1-2.1 1.9C10.6 17.6 6.4 13.4 4.7 5.6A1.9 1.9 0 0 1 6.6 3.5z"/>',
    "mail":     '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6 8.5-6"/>',
    "pin":      '<path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
    "arrow":    '<path d="M4 12h15M13 6l6 6-6 6"/>',
    "chevron":  '<polyline points="6 9 12 15 18 9"/>',
    "check":    '<polyline points="20 6 9 17 4 12"/>',
    "up":       '<path d="M12 19V6M6 12l6-6 6 6"/>',
    "info":     '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 7.8v.2"/>',
    "star":     '<path d="M12 3.5l2.6 5.3 5.9.9-4.2 4.1 1 5.8-5.3-2.8-5.3 2.8 1-5.8-4.2-4.1 5.9-.9z"/>',
    "sparkle":  '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M18.5 15.5l.7 1.8 1.8.7-1.8.7-.7 1.8-.7-1.8-1.8-.7 1.8-.7z"/>',
}


def icon(name, cls=""):
    """Renvoie un <svg> du jeu d'icônes."""
    attrs = ' class="%s"' % cls if cls else ""
    return (
        '<svg%s viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
        'aria-hidden="true">%s</svg>' % (attrs, ICONS[name])
    )


# ---------------------------------------------------------------------------
# Gabarits partagés
# ---------------------------------------------------------------------------
def head(title, meta, canonical, base, image="assets/img/og-image.png", schema=None, robots=None):
    ld = ""
    for block in (schema or []):
        ld += '<script type="application/ld+json">%s</script>\n' % json.dumps(
            block, ensure_ascii=False, separators=(",", ":")
        )
    noindex = '<meta name="robots" content="noindex,follow">\n' if robots == "noindex" else ""
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta}">
{noindex}<link rel="canonical" href="{SITE['url']}/{canonical}">
<meta name="author" content="{SITE['name']}">
<meta name="theme-color" content="#0e5fbb">
<meta name="geo.region" content="FR-IDF">
<meta name="geo.placename" content="{SITE['city']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:url" content="{SITE['url']}/{canonical}">
<meta property="og:image" content="{SITE['url']}/{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta}">
<meta name="twitter:image" content="{SITE['url']}/{image}">
<link rel="icon" href="{base}assets/img/lion.svg" type="image/svg+xml">
<link rel="stylesheet" href="{base}assets/css/theme.css">
<script>document.documentElement.className+=' js';</script>
{ld}</head>
<body>
<a class="skip-link" href="#content">Aller au contenu</a>
"""


def nav_menu(base, current):
    """Menu principal. `current` = clé de la page pour l'état actif."""
    def cls(key):
        return ' class="current-menu-item"' if key == current else ""

    services_sub = "".join(
        '<li><a href="%sservices/%s.html">%s</a></li>' % (base, s["slug"], s["nav"])
        for s in SERVICES
    )
    zones_sub = "".join(
        '<li><a href="%szones/%s.html">%s (%s)</a></li>' % (base, z["slug"], z["name"], z["num"])
        for z in ZONES
    )
    return f"""<nav class="main-nav" id="site-nav" aria-label="Menu principal">
<ul>
<li{cls('home')}><a href="{base}index.html">Accueil</a></li>
<li class="menu-item-has-children{' current-menu-item' if current == 'services' else ''}">
  <a href="{base}services.html">Prestations {icon('chevron', 'caret')}</a>
  <ul class="sub-menu">
    {services_sub}
    <li><a href="{base}services.html"><strong>Toutes nos prestations</strong></a></li>
    <li><a href="{base}realisations.html">Nos réalisations (avant/après)</a></li>
  </ul>
</li>
<li{cls('tarifs')}><a href="{base}tarifs.html">Tarifs</a></li>
<li class="menu-item-has-children{' current-menu-item' if current == 'zones' else ''}">
  <a href="{base}zones.html">Zones {icon('chevron', 'caret')}</a>
  <ul class="sub-menu">
    {zones_sub}
    <li><a href="{base}zones.html"><strong>Toutes nos zones</strong></a></li>
  </ul>
</li>
<li{cls('blog')}><a href="{base}blog.html">Conseils</a></li>
<li{cls('apropos')}><a href="{base}a-propos.html">À propos</a></li>
<li{cls('contact')}><a href="{base}contact.html">Contact</a></li>
</ul>
<div class="nav-cta">
  <a class="btn" href="{base}devis.html">Demander un devis</a>
  <a class="btn btn-outline" href="tel:{SITE['phone_link']}">{icon('phone')}{SITE['phone']}</a>
</div>
</nav>"""


def header(base, current=""):
    return f"""<div class="topbar">
  <div class="container">
    <div class="topbar-info">
      <span>{icon('phone')}<a href="tel:{SITE['phone_link']}">{SITE['phone']}</a></span>
      <span class="topbar-note">{icon('clock')}{SITE['hours']}</span>
    </div>
    <span class="topbar-note">{icon('pin')}Paris &amp; Île-de-France · 75 · 77 · 78 · 91 · 92 · 93 · 94 · 95</span>
  </div>
</div>

<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="{base}index.html" aria-label="{SITE['name']} — accueil">
      <span class="brand-mark">{icon('sparkle')}</span>
      <span class="brand-text">
        <span class="brand-name">Math<span>Clean</span></span>
        <span class="brand-tag">{SITE['slogan']}</span>
      </span>
    </a>
    {nav_menu(base, current)}
    <div class="header-cta">
      <a class="btn btn-outline btn-sm btn-phone" href="tel:{SITE['phone_link']}">{icon('phone')}{SITE['phone']}</a>
      <a class="btn btn-sm" href="{base}devis.html">Devis gratuit</a>
      <button class="nav-toggle" id="nav-toggle" type="button" aria-expanded="false"
              aria-controls="site-nav" aria-label="Ouvrir le menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<div class="nav-backdrop" id="nav-backdrop"></div>
<main id="content">
"""


def cta_band(base, title="Un besoin de nettoyage ?",
             text="Devis gratuit et sans engagement, réponse sous 24 h. "
                  "Nous intervenons 7j/7 à Paris et dans toute l'Île-de-France."):
    return f"""<section class="section cta-band">
  <div class="container cta-inner">
    <div>
      <h2>{title}</h2>
      <p class="lead" style="color:#dbe7f5">{text}</p>
    </div>
    <div class="btn-row">
      <a class="btn btn-light" href="{base}devis.html">Demander un devis</a>
      <a class="btn btn-ghost-light" href="tel:{SITE['phone_link']}">{icon('phone')}{SITE['phone']}</a>
    </div>
  </div>
</section>"""


def footer(base):
    services_links = "".join(
        '<li><a href="%sservices/%s.html">%s</a></li>' % (base, s["slug"], s["nav"])
        for s in SERVICES
    )
    zones_links = "".join(
        '<li><a href="%szones/%s.html">%s (%s)</a></li>' % (base, z["slug"], z["name"], z["num"])
        for z in ZONES[:6]
    )
    return f"""</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <span class="brand-name" style="font-size:1.5rem">Math<span>Clean</span></span>
        <p class="footer-about">
          Entreprise de nettoyage à domicile et en entreprise, à Paris et dans les huit départements
          d'Île-de-France. Automobile, textile, bateau, terrasse, vitres, locaux et fin de chantier.
          Une exigence de roi, du particulier au professionnel.
        </p>
        <div class="footer-contact">
          <div>{icon('phone')}<a href="tel:{SITE['phone_link']}">{SITE['phone']}</a></div>
          <div>{icon('mail')}<a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
          <div>{icon('pin')}<span>{SITE['address']}, {SITE['postcode']} {SITE['city']}</span></div>
          <div>{icon('clock')}<span>{SITE['hours']}</span></div>
        </div>
      </div>
      <div>
        <h4>Prestations</h4>
        <ul>{services_links}</ul>
      </div>
      <div>
        <h4>Zones</h4>
        <ul>{zones_links}<li><a href="{base}zones.html">Toutes nos zones</a></li></ul>
      </div>
      <div>
        <h4>L'entreprise</h4>
        <ul>
          <li><a href="{base}a-propos.html">À propos</a></li>
          <li><a href="{base}tarifs.html">Tarifs</a></li>
          <li><a href="{base}realisations.html">Réalisations</a></li>
          <li><a href="{base}blog.html">Conseils &amp; astuces</a></li>
          <li><a href="{base}devis.html">Devis gratuit</a></li>
          <li><a href="{base}contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> {SITE['name']} — SIRET {SITE['siret']} — Tous droits réservés.</span>
      <ul class="footer-legal">
        <li><a href="{base}mentions-legales.html">Mentions légales</a></li>
        <li><a href="{base}politique-confidentialite.html">Confidentialité</a></li>
        <li><a href="{base}politique-cookies.html">Cookies</a></li>
      </ul>
    </div>
  </div>
</footer>

<button class="to-top" id="to-top" type="button" aria-label="Revenir en haut">{icon('up')}</button>

<div class="callbar">
  <a href="tel:{SITE['phone_link']}">{icon('phone')}Appeler</a>
  <a href="{base}devis.html">{icon('quote')}Devis gratuit</a>
</div>

<div class="cookie-bar" id="cookie-bar" role="dialog" aria-label="Information cookies">
  <p>Ce site n'utilise <strong>aucun cookie publicitaire</strong> ni outil de traçage — uniquement un
     stockage local strictement nécessaire. <a href="{base}politique-cookies.html">En savoir plus</a>.</p>
  <button class="btn btn-sm" id="cookie-ok" type="button">J'ai compris</button>
</div>

<script src="{base}assets/js/theme.js" defer></script>
</body>
</html>
"""


def breadcrumbs(base, trail):
    """`trail` = [(libellé, href|None)], le dernier élément étant la page courante."""
    parts = ['<a href="%sindex.html">Accueil</a>' % base]
    for label, href in trail:
        parts.append('<span class="sep">›</span>')
        if href:
            parts.append('<a href="%s%s">%s</a>' % (base, href, label))
        else:
            parts.append('<span aria-current="page">%s</span>' % label)
    return '<nav class="breadcrumbs" aria-label="Fil d\'Ariane">%s</nav>' % "".join(parts)


def crumb_schema(base_trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE["url"] + "/"}]
    for i, (label, href) in enumerate(base_trail, start=2):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            entry["item"] = "%s/%s" % (SITE["url"], href)
        items.append(entry)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def page_title_block(base, trail, h1, lead=""):
    lead_html = '<p class="lead">%s</p>' % lead if lead else ""
    return f"""<section class="page-title">
  <div class="container">
    {breadcrumbs(base, trail)}
    <h1>{h1}</h1>
    {lead_html}
  </div>
</section>"""


def service_card(base, s):
    return f"""<a class="service-card reveal" href="{base}services/{s['slug']}.html">
  <span class="service-thumb">
    <img src="{base}assets/photos/{s['image']}" alt="{s['name']}" loading="lazy" width="640" height="400">
    <span class="service-price">{s['price']}</span>
  </span>
  <span class="service-body">
    <h3>{s['nav']}</h3>
    <p>{s['excerpt']}</p>
    <span class="service-more">Découvrir la prestation {icon('arrow')}</span>
  </span>
</a>"""


def ba_block(base, before, after, title, sub, idx):
    return f"""<div class="reveal">
  <div class="ba" style="--pos:50%">
    <div class="ba-pane">
      <img src="{base}assets/photos/{before}" alt="{title} avant l'intervention MathClean" loading="lazy">
      <img class="ba-after" src="{base}assets/photos/{after}" alt="{title} après l'intervention MathClean" loading="lazy">
    </div>
    <span class="ba-tag ba-tag-before">Avant</span>
    <span class="ba-tag ba-tag-after">Après</span>
    <span class="ba-handle"></span>
    <input class="ba-range" type="range" min="0" max="100" value="50" step="0.5"
           aria-label="Comparer avant et après — {title}" id="ba-{idx}">
  </div>
  <div class="ba-caption"><strong>{title}</strong><span>{sub}</span></div>
</div>"""


def faq_block(items, group_id="faq"):
    html = '<div class="faq-list" data-faq id="%s">' % group_id
    for q, a in items:
        html += f"""<details class="faq-item">
  <summary>{q}</summary>
  <div class="faq-answer"><p>{a}</p></div>
</details>"""
    return html + "</div>"


def faq_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }


def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": SITE["url"] + "/#business",
        "name": SITE["name"],
        "slogan": SITE["slogan"],
        "description": "Entreprise de nettoyage à domicile à Paris et en Île-de-France : automobile, "
                       "canapé, matelas, tapis, bateau, avion, terrasse, vitres, locaux, bureaux et "
                       "fin de chantier. Devis gratuit, intervention 7j/7.",
        "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/assets/img/lion.svg",
        "image": SITE["url"] + "/assets/img/og-image.png",
        "telephone": "+33623075259",
        "email": SITE["email"],
        "priceRange": "€€",
        "currenciesAccepted": "EUR",
        "paymentAccepted": "Espèces, Carte bancaire, Virement",
        "legalName": SITE["name"],
        "founder": {"@type": "Person", "name": SITE["manager"]},
        "identifier": [
            {"@type": "PropertyValue", "name": "SIRET", "value": SITE["siret"].replace(" ", "")},
            {"@type": "PropertyValue", "name": "SIREN", "value": SITE["siren"].replace(" ", "")},
        ],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["address"],
            "addressLocality": SITE["city"],
            "addressRegion": "Île-de-France",
            "postalCode": SITE["postcode"],
            "addressCountry": "FR",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lon"]},
        "areaServed": [z["name"] for z in ZONES] + ["Île-de-France"],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "08:00", "closes": "20:00",
        }],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Prestations de nettoyage MathClean",
            "itemListElement": [
                {"@type": "Offer",
                 "itemOffered": {"@type": "Service", "name": s["name"]},
                 "url": "%s/services/%s.html" % (SITE["url"], s["slug"])}
                for s in SERVICES
            ],
        },
    }


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(html)
    return path


# ===========================================================================
# ACCUEIL
# ===========================================================================
def build_home():
    base = ""
    cards = "".join(service_card(base, s) for s in SERVICES)
    engagements = "".join(
        f"""<div class="feature reveal">
  <span class="feature-icon">{icon(ic)}</span>
  <h3>{title}</h3>
  <p>{text}</p>
</div>""" for ic, title, text in ENGAGEMENTS
    )
    zones_cards = "".join(
        f"""<a class="zone-card reveal" href="zones/{z['slug']}.html">
  <span>{z['name']}</span><span class="zone-num">{z['num']}</span>
</a>""" for z in ZONES
    )
    ba = "".join(
        ba_block(base, b, a, t, s, i) for i, (b, a, t, s) in enumerate(BEFORE_AFTER[:4])
    )
    posts = "".join(post_card(base, p) for p in POSTS[:3])

    body = f"""
<section class="hero">
  <div class="hero-media">
    <video src="assets/videos/detailing-5.mp4" poster="assets/videos/detailing-5.webp"
           autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video>
  </div>
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow eyebrow-gold">{SITE['name']} · {SITE['slogan']}</span>
      <h1>Entreprise de nettoyage à Paris <em>&amp; en Île-de-France</em></h1>
      <p class="hero-lead">
        Automobile, textile, bateau, avion, terrasse, vitres, locaux et fin de chantier.
        Nous venons chez vous, entièrement équipés, 7&nbsp;jours sur 7 — sans acompte,
        et vous ne réglez qu'une fois le résultat constaté.
      </p>
      <div class="hero-badges">
        <span class="badge">{icon('check')}Intervention sous 24 h</span>
        <span class="badge">{icon('check')}Devis gratuit et ferme</span>
        <span class="badge">{icon('check')}8 départements couverts</span>
      </div>
      <div class="btn-row">
        <a class="btn btn-gold" href="devis.html">Demander un devis gratuit</a>
        <a class="btn btn-ghost-light" href="tel:{SITE['phone_link']}">{icon('phone')}{SITE['phone']}</a>
      </div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="stat"><div class="stat-num">7j/7</div><div class="stat-label">Disponibilité, jours fériés compris</div></div>
  <div class="stat"><div class="stat-num">8</div><div class="stat-label">Départements franciliens couverts</div></div>
  <div class="stat"><div class="stat-num">24 h</div><div class="stat-label">Délai d'intervention à Paris</div></div>
  <div class="stat"><div class="stat-num">0 €</div><div class="stat-label">D'acompte à la réservation</div></div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Nos prestations</span>
      <h2>Huit métiers, une seule exigence</h2>
      <p class="lead">
        Chaque matière appelle un produit et un geste différents. C'est ce travail de diagnostic —
        comprendre la matière avant de la nettoyer — qui sépare un résultat correct d'un résultat qui tient.
      </p>
    </div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Qui sommes-nous</span>
        <h2>Le nettoyage fait à la main, par la personne qui vient chez vous</h2>
        <p>
          <strong>MathClean</strong> est une entreprise individuelle installée à {SITE['city']} (93).
          Pas de centre d'appels, pas de sous-traitance : quand vous appelez le {SITE['phone']},
          vous parlez directement à la personne qui viendra chez vous.
        </p>
        <p>
          Nous nous déplaçons avec nos machines, nos produits, notre eau et notre électricité.
          Vous n'avez ni prise ni point d'eau à fournir, ce qui nous permet d'intervenir
          en parking souterrain, en pied d'immeuble ou à quai.
        </p>
        <ul class="checklist checklist-gold" style="margin:1.5rem 0">
          <li>Produits sûrs pour les enfants et les animaux</li>
          <li>Frais de déplacement annoncés avant validation</li>
          <li>Règlement après l'intervention, jamais d'acompte</li>
        </ul>
        <a class="btn" href="a-propos.html">Notre méthode et nos engagements</a>
      </div>
      <div class="media-frame reveal">
        <img src="assets/photos/mathieo-mathclean.webp" alt="{SITE['manager']}, fondateur de MathClean, en intervention"
             loading="lazy" width="760" height="570">
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Nos résultats</span>
      <h2>Avant / après</h2>
      <p class="lead">
        Des interventions réelles, chez nos clients particuliers et professionnels.
        Faites glisser le curseur pour comparer.
      </p>
    </div>
    <div class="grid grid-2">{ba}</div>
    <div class="btn-row center" style="margin-top:38px">
      <a class="btn btn-outline" href="realisations.html">Voir toutes nos réalisations</a>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Pourquoi nous choisir</span>
      <h2>Nos engagements</h2>
      <p class="lead">Des règles simples, valables sur toutes nos prestations et dans tous les départements franciliens.</p>
    </div>
    <div class="grid grid-3">{engagements}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Comment ça se passe</span>
      <h2>De votre appel au résultat</h2>
    </div>
    <div class="steps">
      <div class="step reveal">
        <h3>Vous nous décrivez le besoin</h3>
        <p>Par téléphone ou via le formulaire de devis. Quelques photos suffisent souvent à cadrer précisément l'intervention.</p>
      </div>
      <div class="step reveal">
        <h3>Nous vous envoyons un devis ferme</h3>
        <p>Gratuit, détaillé poste par poste, frais de déplacement compris. Réponse sous 24 h.</p>
      </div>
      <div class="step reveal">
        <h3>Nous intervenons chez vous</h3>
        <p>Sous 24 à 48 h à Paris et en petite couronne, sous 48 à 72 h en grande couronne. Nous venons entièrement équipés.</p>
      </div>
      <div class="step reveal">
        <h3>Vous constatez, puis vous réglez</h3>
        <p>Contrôle final ensemble avant notre départ. Aucun acompte : le règlement se fait après l'intervention.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Où nous intervenons</span>
      <h2>Les huit départements d'Île-de-France</h2>
      <p class="lead">
        Depuis notre atelier de {SITE['city']} (93). Frais de déplacement : {SITE['travel_fee']},
        annoncés avant que vous validiez.
      </p>
    </div>
    <div class="grid grid-4">{zones_cards}</div>
    <div class="btn-row center" style="margin-top:34px">
      <a class="btn btn-outline" href="zones.html">Voir le détail des villes couvertes</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container-narrow">
    <div class="section-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>Ce qu'on nous demande le plus souvent</h2>
    </div>
    {faq_block(FAQ)}
    <div class="btn-row center" style="margin-top:30px">
      <a class="btn btn-outline" href="contact.html">Une autre question ? Écrivez-nous</a>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Conseils &amp; astuces</span>
      <h2>Entretenir soi-même, et savoir quand s'arrêter</h2>
      <p class="lead">Nos méthodes de professionnels, expliquées simplement — y compris les erreurs qui coûtent cher.</p>
    </div>
    <div class="grid grid-3">{posts}</div>
    <div class="btn-row center" style="margin-top:34px">
      <a class="btn btn-outline" href="blog.html">Tous nos conseils</a>
    </div>
  </div>
</section>

{cta_band(base)}
"""
    schema = [
        business_schema(),
        faq_schema(FAQ),
        {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"],
         "url": SITE["url"] + "/", "inLanguage": "fr-FR",
         "publisher": {"@id": SITE["url"] + "/#business"}},
    ]
    html = (
        head("Entreprise de nettoyage à Paris & Île-de-France | MathClean",
             "Nettoyage automobile, textile, bateau, terrasse, vitres, locaux et fin de chantier à "
             "Paris et en Île-de-France. Intervention à domicile 7j/7, devis gratuit, sans acompte.",
             "", base, schema=schema)
        + header(base, "home") + body + footer(base)
    )
    return write("index.html", html)


# ===========================================================================
# PRESTATIONS
# ===========================================================================
def build_services_archive():
    base = ""
    trail = [("Prestations", None)]
    cards = "".join(service_card(base, s) for s in SERVICES)
    body = f"""
{page_title_block(base, trail, "Nos prestations de nettoyage",
    "Huit métiers, à domicile comme en entreprise, partout à Paris et en Île-de-France. "
    "Chaque prestation dispose de sa page dédiée : méthode, contenu détaillé et réponses aux questions courantes.")}

<section class="section">
  <div class="container">
    <div class="grid grid-3">{cards}</div>
  </div>
</section>

<section class="section section-soft">
  <div class="container container-narrow">
    <div class="notice notice-blue">
      {icon('info')}
      <p>
        <strong>Vous ne savez pas quelle prestation choisir ?</strong> Décrivez-nous simplement votre
        besoin — quelques photos suffisent le plus souvent. Nous vous répondons sous 24 h avec un devis
        ferme, gratuit et sans engagement.
      </p>
    </div>
    <div class="btn-row center" style="margin-top:28px">
      <a class="btn" href="devis.html">Demander un devis</a>
      <a class="btn btn-outline" href="tarifs.html">Consulter les tarifs</a>
    </div>
  </div>
</section>

{cta_band(base)}
"""
    html = (head("Nos prestations de nettoyage à Paris & Île-de-France | MathClean",
                 "Toutes les prestations MathClean : nettoyage automobile, textile, bateau, avion, "
                 "terrasse, vitres, locaux, bureaux et fin de chantier à Paris et en Île-de-France.",
                 "services.html", base, schema=[crumb_schema([("Prestations", "services.html")])])
            + header(base, "services") + body + footer(base))
    return write("services.html", html)


def build_service(s):
    base = "../"
    trail = [("Prestations", "services.html"), (s["nav"], None)]
    intro = "".join("<p>%s</p>" % p for p in s["intro"])
    included = "".join("<li>%s</li>" % li for li in s["included"])
    steps = "".join(
        f'<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in s["steps"]
    )
    others = "".join(
        service_card(base, o) for o in SERVICES if o["slug"] != s["slug"]
    )
    zones_links = " · ".join(
        '<a href="%szones/%s.html">%s (%s)</a>' % (base, z["slug"], z["name"], z["num"])
        for z in ZONES
    )
    tarif_cta = (
        '<a class="btn btn-outline" href="%starifs.html">Voir la grille tarifaire</a>' % base
        if s["price"] != "sur devis" else ""
    )
    prix_note = (
        "Le prix exact dépend du véhicule ou de la pièce ; il vous est confirmé avant l'intervention."
        if s["price"] != "sur devis" else
        "Cette prestation se chiffre au cas par cas : nous établissons un devis gratuit et ferme après échange."
    )

    body = f"""
{page_title_block(base, trail, s["h1"], s["excerpt"])}

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">La prestation</span>
        <h2>{s['name']}</h2>
        {intro}
        <div class="btn-row" style="margin-top:1.6rem">
          <a class="btn" href="{base}devis.html?prestation={s['nav']}">Demander un devis gratuit</a>
          {tarif_cta}
        </div>
      </div>
      <div class="media-frame reveal">
        <img src="{base}assets/photos/{s['hero']}" alt="{s['name']} — MathClean" loading="lazy" width="760" height="570">
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Le contenu</span>
        <h2>{s['included_title']}</h2>
        <ul class="checklist" style="margin-top:1.4rem">{included}</ul>
      </div>
      <div class="reveal">
        <div class="notice">
          {icon('info')}
          <p>
            <strong>Tarif : {s['price']}.</strong>
            {prix_note}
            Les frais de déplacement ({SITE['travel_fee']}) s'ajoutent et vous sont annoncés avant validation.
          </p>
        </div>
        <div class="notice notice-blue" style="margin-top:18px">
          {icon('truck')}
          <p>
            <strong>Nous venons entièrement équipés</strong> — machines, produits, eau et électricité.
            Vous n'avez ni prise ni point d'eau à fournir.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Notre méthode</span>
      <h2>Comment nous procédons</h2>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="section section-soft">
  <div class="container container-narrow">
    <div class="section-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>{s['nav']} : vos questions</h2>
    </div>
    {faq_block(s['faq'], 'faq-service')}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Zones desservies</span>
      <h2>{s['nav']} partout en Île-de-France</h2>
      <p class="lead">{zones_links}</p>
    </div>
  </div>
</section>

{cta_band(base, "Besoin de cette prestation ?",
          "Devis gratuit et sans engagement, réponse sous 24 h. Aucun acompte : vous réglez après l'intervention.")}

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Découvrez aussi</span>
      <h2>Nos autres prestations</h2>
    </div>
    <div class="grid grid-3">{others}</div>
  </div>
</section>
"""
    schema = [
        crumb_schema([("Prestations", "services.html"), (s["nav"], "services/%s.html" % s["slug"])]),
        {"@context": "https://schema.org", "@type": "Service",
         "name": s["name"], "description": s["excerpt"],
         "serviceType": s["nav"],
         "provider": {"@id": SITE["url"] + "/#business"},
         "areaServed": [{"@type": "AdministrativeArea", "name": z["name"]} for z in ZONES],
         "url": "%s/services/%s.html" % (SITE["url"], s["slug"])},
        faq_schema(s["faq"]),
    ]
    html = (head(s["title"], s["meta"], "services/%s.html" % s["slug"], base, schema=schema)
            + header(base, "services") + body + footer(base))
    return write("services/%s.html" % s["slug"], html)


# ===========================================================================
# TARIFS
# ===========================================================================
def build_tarifs():
    base = ""
    trail = [("Tarifs", None)]

    packs = ""
    for name, lo, hi, scope, desc, featured, lines in PACKS_AUTO:
        flag = '<span class="pack-flag">Le plus demandé</span>' if featured else ""
        items = "".join("<li>%s</li>" % li for li in lines)
        packs += f"""<div class="pack reveal{' is-featured' if featured else ''}">
  {flag}
  <div class="pack-scope">{scope}</div>
  <h3>{name}</h3>
  <div class="pack-price">{lo} € <span>à {hi} €</span></div>
  <p class="pack-desc">{desc}</p>
  <ul class="checklist">{items}</ul>
  <a class="btn btn-outline" href="devis.html?prestation=Nettoyage automobile">Demander ce pack</a>
</div>"""

    options = "".join(
        f"<tr><th scope=\"row\">{n}<small>{d}</small></th><td class=\"amount\">+ {p} €</td></tr>"
        for n, p, d in OPTIONS_AUTO
    )
    textile = "".join(
        f"<tr><th scope=\"row\">{n}<small>{d}</small></th><td class=\"amount\">{p} €</td></tr>"
        for n, p, d in TARIFS_TEXTILE
    )
    devis_rows = "".join(
        f"<tr><th scope=\"row\"><a href=\"services/{slug}.html\">{n}</a><small>{d}</small></th>"
        f"<td class=\"amount\">Sur devis</td></tr>"
        for n, d, slug in TARIFS_DEVIS
    )

    faq_tarifs = [
        ("Pourquoi les packs automobiles affichent-ils une fourchette ?",
         "Parce qu'une citadine et un monospace 7 places ne demandent ni le même temps ni la même quantité "
         "de produit. Le bas de la fourchette correspond à une citadine, le haut à un grand véhicule. "
         "Le montant exact vous est confirmé avant l'intervention."),
        ("Comment sont calculés les frais de déplacement ?",
         "5 € par tranche de 5 km entre notre atelier de Tremblay-en-France (93) et votre adresse. "
         "Le montant vous est annoncé avant que vous validiez : rien ne s'ajoute le jour de l'intervention."),
        ("Faut-il verser un acompte ?",
         "Non. Vous réglez après l'intervention, une fois le résultat constaté avec vous. "
         "Espèces, carte bancaire ou virement."),
        ("Pourquoi certaines prestations sont-elles uniquement sur devis ?",
         "Parce qu'un semi-rigide de 6 mètres et un bateau habitable de 12 mètres, ou un studio et un "
         "plateau de bureaux, n'ont rien de comparable. Afficher un prix unique n'aurait aucun sens : "
         "nous préférons un devis ferme, établi après échange, auquel nous nous tenons."),
        ("La TVA s'applique-t-elle ?",
         "Non. MathClean bénéficie de la franchise en base de TVA (article 293 B du Code général des impôts) : "
         "les prix affichés sont les prix finaux, sans TVA à ajouter."),
    ]

    body = f"""
{page_title_block(base, trail, "Nos tarifs",
    "Les prix des prestations à tarif fixe, et le principe de facturation pour celles qui se chiffrent "
    "sur devis. Aucun acompte, aucun frais caché : le montant annoncé est celui que vous réglez.")}

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Automobile</span>
      <h2>Les quatre packs detailing</h2>
      <p class="lead">
        À domicile, sur votre place de parking ou sur votre lieu de travail. Le coffre est toujours
        compris, sans supplément.
      </p>
    </div>
    <div class="grid grid-4">{packs}</div>

    <div class="table-wrap" style="margin-top:44px">
      <table class="price-table">
        <caption>Options automobile, à ajouter à n'importe quel pack</caption>
        <thead><tr><th scope="col">Option</th><th scope="col" style="text-align:right">Supplément</th></tr></thead>
        <tbody>{options}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Textile</span>
      <h2>Canapé, matelas, tapis et fauteuil</h2>
      <p class="lead">
        Injection-extraction à domicile, détachage ciblé et traitement anti-acariens.
        Les matelas sont traités sur les deux faces.
      </p>
    </div>
    <div class="table-wrap">
      <table class="price-table">
        <caption>Tarifs par pièce traitée</caption>
        <thead><tr><th scope="col">Prestation</th><th scope="col" style="text-align:right">Tarif</th></tr></thead>
        <tbody>{textile}</tbody>
      </table>
    </div>
    <p class="field-hint" style="margin-top:14px">
      Plusieurs pièces à traiter le même jour ? Dites-le nous : nous ajustons le devis, le déplacement
      n'étant facturé qu'une fois.
    </p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Sur devis</span>
      <h2>Les prestations chiffrées au cas par cas</h2>
      <p class="lead">
        Devis gratuit, ferme et détaillé poste par poste, établi après échange ou visite.
        Nous nous y tenons.
      </p>
    </div>
    <div class="table-wrap">
      <table class="price-table">
        <thead><tr><th scope="col">Prestation</th><th scope="col" style="text-align:right">Tarif</th></tr></thead>
        <tbody>{devis_rows}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container container-narrow">
    <div class="notice">
      {icon('pin')}
      <p>
        <strong>Frais de déplacement :</strong> {SITE['travel_fee']}. Ils s'ajoutent au prix de la
        prestation et vous sont annoncés avant que vous validiez. Aucune surprise à l'arrivée.
      </p>
    </div>
    <div class="notice notice-blue" style="margin-top:18px">
      {icon('wallet')}
      <p>
        <strong>Aucun acompte.</strong> Vous réglez après l'intervention, une fois le résultat constaté
        avec vous — espèces, carte bancaire ou virement. TVA non applicable, article 293 B du CGI.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container-narrow">
    <div class="section-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>Comprendre nos tarifs</h2>
    </div>
    {faq_block(faq_tarifs, 'faq-tarifs')}
  </div>
</section>

{cta_band(base, "Un devis chiffré, gratuitement",
          "Décrivez-nous votre besoin en deux minutes. Réponse sous 24 h, sans engagement.")}
"""
    schema = [crumb_schema([("Tarifs", "tarifs.html")]), faq_schema(faq_tarifs)]
    html = (head("Tarifs de nettoyage à Paris — packs auto dès 40 €, textile dès 15 € | MathClean",
                 "Tarifs MathClean : packs detailing automobile de 40 à 240 €, nettoyage textile dès 15 €, "
                 "prestations professionnelles sur devis. Sans acompte, frais de déplacement annoncés d'avance.",
                 "tarifs.html", base, schema=schema)
            + header(base, "tarifs") + body + footer(base))
    return write("tarifs.html", html)


# ===========================================================================
# RÉALISATIONS
# ===========================================================================
def build_realisations():
    base = ""
    trail = [("Réalisations", None)]
    ba = "".join(ba_block(base, b, a, t, s, i) for i, (b, a, t, s) in enumerate(BEFORE_AFTER))
    body = f"""
{page_title_block(base, trail, "Nos réalisations",
    "Des interventions réelles, réalisées chez nos clients particuliers et professionnels. "
    "Faites glisser le curseur pour comparer l'avant et l'après.")}

<section class="section">
  <div class="container">
    <div class="grid grid-2">{ba}</div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">En action</span>
      <h2>Sur le terrain</h2>
      <p class="lead">Quelques images de nos interventions, prises pendant le travail.</p>
    </div>
    <div class="grid grid-3">
      <div class="media-frame reveal">
        <video src="assets/videos/detailing-3.mp4" poster="assets/videos/detailing-3.webp"
               muted loop playsinline controls preload="none"></video>
      </div>
      <div class="media-frame reveal">
        <video src="assets/videos/vitres-1.mp4" poster="assets/videos/vitres-1.webp"
               muted loop playsinline controls preload="none"></video>
      </div>
      <div class="media-frame reveal">
        <video src="assets/videos/detailing-6.mp4" poster="assets/videos/detailing-6.webp"
               muted loop playsinline controls preload="none"></video>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container-narrow">
    <div class="section-head center">
      <span class="eyebrow">Avis clients</span>
      <h2>Des avis publics, pas des témoignages choisis</h2>
    </div>
    <div class="notice notice-blue">
      {icon('star')}
      <p>
        Nous ne publions aucun avis rédigé par nos soins. Tous nos retours clients figurent sur notre
        fiche Google, avec le nom et la date de chacun, consultables dans leur intégralité.
      </p>
    </div>
    <div class="btn-row center" style="margin-top:26px">
      <a class="btn" href="{SITE['review_url']}" target="_blank" rel="noopener">Lire les avis sur Google</a>
    </div>
  </div>
</section>

{cta_band(base)}
"""
    html = (head("Nos réalisations — avant / après | MathClean",
                 "Avant/après de nos interventions de nettoyage à Paris et en Île-de-France : sièges auto, "
                 "canapés, terrasses, tapis, cuisines professionnelles.",
                 "realisations.html", base,
                 schema=[crumb_schema([("Réalisations", "realisations.html")])])
            + header(base, "services") + body + footer(base))
    return write("realisations.html", html)


# ===========================================================================
# ZONES
# ===========================================================================
def build_zones_archive():
    base = ""
    trail = [("Zones d'intervention", None)]
    cards = ""
    for z in ZONES:
        cities = "".join("<li>%s</li>" % c for c in z["cities"][:8])
        cards += f"""<div class="feature reveal">
  <span class="feature-icon">{icon('pin')}</span>
  <h3><a href="zones/{z['slug']}.html">{z['name']} ({z['num']})</a></h3>
  <p>{z['intro']}</p>
  <ul class="city-list" style="margin:16px 0">{cities}</ul>
  <a class="service-more" href="zones/{z['slug']}.html">Voir la page {z['name']} {icon('arrow')}</a>
</div>"""
    body = f"""
{page_title_block(base, trail, "Nos zones d'intervention en Île-de-France",
    "MathClean intervient dans les huit départements franciliens, depuis son atelier de "
    + SITE['city'] + " (93). Frais de déplacement : " + SITE['travel_fee'] + ", annoncés avant validation.")}

<section class="section">
  <div class="container">
    <div class="grid grid-2">{cards}</div>
  </div>
</section>

<section class="section section-soft">
  <div class="container container-narrow">
    <div class="notice">
      {icon('info')}
      <p>
        <strong>Votre commune n'apparaît pas ?</strong> Ces listes ne sont pas exhaustives : nous couvrons
        l'ensemble des huit départements. Appelez-nous au {SITE['phone']} pour vérifier notre disponibilité
        chez vous et connaître le montant exact du déplacement.
      </p>
    </div>
  </div>
</section>

{cta_band(base)}
"""
    html = (head("Zones d'intervention — nettoyage à Paris & en Île-de-France | MathClean",
                 "MathClean intervient à Paris (75), dans les Hauts-de-Seine (92), la Seine-Saint-Denis (93), "
                 "le Val-de-Marne (94), l'Essonne (91), les Yvelines (78), la Seine-et-Marne (77) et le Val-d'Oise (95).",
                 "zones.html", base, schema=[crumb_schema([("Zones d'intervention", "zones.html")])])
            + header(base, "zones") + body + footer(base))
    return write("zones.html", html)


def build_zone(z):
    base = "../"
    trail = [("Zones d'intervention", "zones.html"), ("%s (%s)" % (z["name"], z["num"]), None)]
    cities = "".join("<li>%s</li>" % c for c in z["cities"])
    services_cards = "".join(service_card(base, s) for s in SERVICES[:6])
    other_zones = "".join(
        f'<a class="zone-card reveal" href="{base}zones/{o["slug"]}.html"><span>{o["name"]}</span>'
        f'<span class="zone-num">{o["num"]}</span></a>'
        for o in ZONES if o["slug"] != z["slug"]
    )
    body = f"""
{page_title_block(base, trail, "Entreprise de nettoyage en %s (%s)" % (z["name"], z["num"]),
                  z["intro"])}

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Sur le terrain</span>
        <h2>Ce que nous faisons le plus en {z['name']}</h2>
        <p>{z['focus']}</p>
        <p>
          Nous venons avec nos machines, nos produits, notre eau et notre électricité : vous n'avez rien
          à fournir. Les frais de déplacement — {SITE['travel_fee']} — vous sont annoncés avant que vous
          validiez le devis.
        </p>
        <div class="btn-row" style="margin-top:1.5rem">
          <a class="btn" href="{base}devis.html">Devis gratuit en {z['name']}</a>
          <a class="btn btn-outline" href="tel:{SITE['phone_link']}">{icon('phone')}{SITE['phone']}</a>
        </div>
      </div>
      <div class="reveal">
        <h3>Les villes où nous intervenons</h3>
        <ul class="city-list" style="margin-bottom:18px">{cities}</ul>
        <p class="field-hint">
          Cette liste n'est pas exhaustive : nous couvrons l'ensemble du département.
          Appelez-nous pour vérifier notre disponibilité dans votre commune.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Nos prestations</span>
      <h2>Ce que nous proposons en {z['name']}</h2>
    </div>
    <div class="grid grid-3">{services_cards}</div>
    <div class="btn-row center" style="margin-top:34px">
      <a class="btn btn-outline" href="{base}services.html">Voir les huit prestations</a>
    </div>
  </div>
</section>

{cta_band(base, "Un besoin en %s ?" % z["name"],
          "Devis gratuit et sans engagement, réponse sous 24 h. Aucun acompte à verser.")}

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Autres départements</span>
      <h2>Nous intervenons aussi</h2>
    </div>
    <div class="grid grid-4">{other_zones}</div>
  </div>
</section>
"""
    schema = [
        crumb_schema([("Zones d'intervention", "zones.html"),
                      ("%s (%s)" % (z["name"], z["num"]), "zones/%s.html" % z["slug"])]),
        {"@context": "https://schema.org", "@type": "Service",
         "name": "Nettoyage en %s (%s)" % (z["name"], z["num"]),
         "provider": {"@id": SITE["url"] + "/#business"},
         "areaServed": {"@type": "AdministrativeArea", "name": z["name"]},
         "url": "%s/zones/%s.html" % (SITE["url"], z["slug"])},
    ]
    html = (head("Entreprise de nettoyage en %s (%s) | MathClean" % (z["name"], z["num"]),
                 "Nettoyage automobile, textile, terrasse, vitres et locaux en %s (%s). "
                 "Intervention à domicile 7j/7, devis gratuit, sans acompte." % (z["name"], z["num"]),
                 "zones/%s.html" % z["slug"], base, schema=schema)
            + header(base, "zones") + body + footer(base))
    return write("zones/%s.html" % z["slug"], html)


# ===========================================================================
# BLOG
# ===========================================================================
def post_card(base, p):
    return f"""<article class="post-card reveal">
  <a class="post-thumb" href="{base}blog/{p['slug']}.html" tabindex="-1" aria-hidden="true">
    <img src="{base}assets/photos/{p['image']}" alt="" loading="lazy" width="640" height="360">
  </a>
  <div class="post-body">
    <div class="post-meta">
      <span class="post-cat">{p['cat']}</span>
      <time datetime="{p['date']}">{p['date_fr']}</time>
    </div>
    <h3><a href="{base}blog/{p['slug']}.html">{p['title']}</a></h3>
    <p>{p['excerpt']}</p>
    <span class="service-more">Lire l'article {icon('arrow')}</span>
  </div>
</article>"""


def sidebar(base, current_slug=None):
    recent = [p for p in POSTS if p["slug"] != current_slug][:4]
    recent_html = "".join(
        f"""<li>
  <img src="{base}assets/photos/{p['image']}" alt="" loading="lazy" width="70" height="56">
  <div>
    <a href="{base}blog/{p['slug']}.html">{p['title']}</a>
    <time datetime="{p['date']}">{p['date_fr']}</time>
  </div>
</li>""" for p in recent
    )
    cats = {}
    for p in POSTS:
        cats[p["cat"]] = cats.get(p["cat"], 0) + 1
    cats_html = "".join(
        f'<li><a href="{base}blog.html#{c.lower()}">{c}<span>{n}</span></a></li>'
        for c, n in sorted(cats.items())
    )
    services_html = "".join(
        f'<li><a href="{base}services/{s["slug"]}.html">{s["nav"]}<span>{s["price"]}</span></a></li>'
        for s in SERVICES
    )
    return f"""<aside class="sidebar">
  <div class="widget widget-cta">
    <h3 class="widget-title">Un devis gratuit ?</h3>
    <p>Décrivez-nous votre besoin : réponse sous 24 h, sans engagement et sans acompte.</p>
    <a class="widget-phone" href="tel:{SITE['phone_link']}">{SITE['phone']}</a>
    <a class="btn btn-light btn-block" href="{base}devis.html">Demander un devis</a>
  </div>
  <div class="widget">
    <h3 class="widget-title">Articles récents</h3>
    <ul class="widget-posts">{recent_html}</ul>
  </div>
  <div class="widget">
    <h3 class="widget-title">Catégories</h3>
    <ul class="widget-links">{cats_html}</ul>
  </div>
  <div class="widget">
    <h3 class="widget-title">Nos prestations</h3>
    <ul class="widget-links">{services_html}</ul>
  </div>
</aside>"""


def build_blog_archive():
    base = ""
    trail = [("Conseils & astuces", None)]
    cards = "".join(post_card(base, p) for p in POSTS)
    body = f"""
{page_title_block(base, trail, "Conseils &amp; astuces de nettoyage",
    "Un bon entretien au quotidien prolonge la vie de vos biens et espace les nettoyages en profondeur. "
    "Voici nos méthodes de professionnels — y compris les erreurs qui coûtent cher.")}

<section class="section">
  <div class="container blog-layout">
    <div>
      <div class="grid grid-2">{cards}</div>
      <div class="notice notice-blue" style="margin-top:38px">
        {icon('info')}
        <p>
          Pour les taches tenaces, les acariens incrustés ou un textile de valeur, rien ne remplace une
          intervention professionnelle par injection-extraction. Un essai raté coûte plus cher que
          l'intervention : <a href="devis.html">demandez-nous un devis gratuit</a>.
        </p>
      </div>
    </div>
    {sidebar(base)}
  </div>
</section>

{cta_band(base)}
"""
    html = (head("Conseils & astuces de nettoyage | MathClean",
                 "Nos conseils de professionnels pour entretenir canapé, matelas, tapis, voiture, "
                 "terrasse, vitres et bateau — et savoir quand faire appel à un professionnel.",
                 "blog.html", base, schema=[crumb_schema([("Conseils & astuces", "blog.html")])])
            + header(base, "blog") + body + footer(base))
    return write("blog.html", html)


def build_post(p, prev_post, next_post):
    base = "../"
    trail = [("Conseils & astuces", "blog.html"), (p["title"], None)]
    service = next((s for s in SERVICES if s["slug"] == p["service"]), SERVICES[0])

    content = ""
    for kind, text in p["body"]:
        if kind == "p":
            content += "<p>%s</p>" % text
        elif kind == "h2":
            content += "<h2>%s</h2>" % text
        elif kind == "h3":
            content += "<h3>%s</h3>" % text
        elif kind == "blockquote":
            content += "<blockquote><p>%s</p></blockquote>" % text

    nav = '<div class="post-nav">'
    if prev_post:
        nav += (f'<a class="prev" href="{base}blog/{prev_post["slug"]}.html">'
                f'<small>Article précédent</small><strong>{prev_post["title"]}</strong></a>')
    else:
        nav += "<span></span>"
    if next_post:
        nav += (f'<a class="next" href="{base}blog/{next_post["slug"]}.html">'
                f'<small>Article suivant</small><strong>{next_post["title"]}</strong></a>')
    nav += "</div>"

    body = f"""
<section class="page-title">
  <div class="container">
    {breadcrumbs(base, trail)}
  </div>
</section>

<section class="section">
  <div class="container blog-layout">
    <article>
      <header class="entry-header">
        <div class="post-meta" style="margin-bottom:14px">
          <span class="post-cat">{p['cat']}</span>
          <time datetime="{p['date']}">{p['date_fr']}</time>
          <span>Par {SITE['manager']}</span>
        </div>
        <h1>{p['title']}</h1>
        <p class="lead">{p['excerpt']}</p>
      </header>

      <figure>
        <img src="{base}assets/photos/{p['image']}" alt="{p['title']}" width="1000" height="600">
      </figure>

      <div class="entry-content">{content}</div>

      <div class="notice notice-blue" style="margin-top:34px">
        {icon('sparkle')}
        <p>
          <strong>{p['cta']}</strong> Nous intervenons à domicile à Paris et dans toute l'Île-de-France,
          avec du matériel professionnel. Découvrez notre
          <a href="{base}services/{service['slug']}.html">{service['nav'].lower()}</a>
          ou <a href="{base}devis.html">demandez un devis gratuit</a>.
        </p>
      </div>

      <footer class="entry-footer">
        <ul class="tag-list">
          <li><a href="{base}blog.html">{p['cat']}</a></li>
          <li><a href="{base}services/{service['slug']}.html">{service['nav']}</a></li>
          <li><a href="{base}zones.html">Île-de-France</a></li>
        </ul>
        {nav}
      </footer>
    </article>
    {sidebar(base, p['slug'])}
  </div>
</section>

{cta_band(base)}
"""
    schema = [
        crumb_schema([("Conseils & astuces", "blog.html"), (p["title"], "blog/%s.html" % p["slug"])]),
        {"@context": "https://schema.org", "@type": "BlogPosting",
         "headline": p["title"], "description": p["excerpt"],
         "image": "%s/assets/photos/%s" % (SITE["url"], p["image"]),
         "datePublished": p["date"], "dateModified": p["date"],
         "inLanguage": "fr-FR",
         "author": {"@type": "Person", "name": SITE["manager"]},
         "publisher": {"@id": SITE["url"] + "/#business"},
         "mainEntityOfPage": "%s/blog/%s.html" % (SITE["url"], p["slug"])},
    ]
    html = (head("%s | MathClean" % p["title"], p["meta"], "blog/%s.html" % p["slug"], base,
                 image="assets/photos/%s" % p["image"], schema=schema)
            + header(base, "blog") + body + footer(base))
    return write("blog/%s.html" % p["slug"], html)


# ===========================================================================
# À PROPOS
# ===========================================================================
def build_apropos():
    base = ""
    trail = [("À propos", None)]
    engagements = "".join(
        f"""<div class="feature reveal">
  <span class="feature-icon">{icon(ic)}</span>
  <h3>{title}</h3>
  <p>{text}</p>
</div>""" for ic, title, text in ENGAGEMENTS
    )
    body = f"""
{page_title_block(base, trail, "MathClean, le nettoyage fait à la main",
    "Une entreprise de nettoyage installée à " + SITE['city'] + ", qui se déplace chez vous dans toute "
    "l'Île-de-France. Voici comment nous travaillons, avec quel matériel, et ce sur quoi nous nous engageons.")}

<section class="section">
  <div class="container">
    <div class="split">
      <div class="media-frame reveal">
        <img src="assets/photos/mathieo-mathclean.webp" alt="{SITE['manager']}, fondateur de MathClean"
             loading="lazy" width="760" height="570">
      </div>
      <div class="reveal">
        <span class="eyebrow">Qui est derrière MathClean</span>
        <h2>{SITE['manager']}</h2>
        <p>
          MathClean est une entreprise individuelle, déclarée au {SITE['address']} à {SITE['city']} ({SITE['postcode'][:2]}).
          Pas de centre d'appels, pas de sous-traitance : quand vous appelez le {SITE['phone']}, vous parlez
          directement à la personne qui viendra chez vous.
        </p>
        <p>
          Le nettoyage n'est pas un simple coup de chiffon. Une sellerie en cuir, une moquette en laine,
          une terrasse en bois exotique et une carrosserie vernie ne se traitent ni avec les mêmes produits,
          ni avec les mêmes gestes. C'est ce travail de diagnostic — <strong>comprendre la matière avant de
          la nettoyer</strong> — qui fait la différence entre un résultat correct et un résultat qui tient.
        </p>
        <p class="field-hint">SIRET {SITE['siret']} · TVA non applicable, article 293 B du CGI.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Notre méthode</span>
      <h2>Trois techniques, selon la matière</h2>
      <p class="lead">Nous n'appliquons pas le même traitement partout. Voici ce que recouvre concrètement chaque intervention.</p>
    </div>
    <div class="grid grid-3">
      <div class="feature reveal">
        <span class="feature-icon">{icon('sofa')}</span>
        <h3>Injection-extraction</h3>
        <p>
          Une solution nettoyante est injectée sous pression au cœur de la fibre, puis immédiatement
          réaspirée avec la saleté dissoute. C'est ce qui permet de traiter un canapé, un matelas ou un
          tapis <strong>sans le détremper</strong> — donc sans auréole au séchage. Comptez 4 à 6 h de
          séchage selon la ventilation de la pièce.
        </p>
      </div>
      <div class="feature reveal">
        <span class="feature-icon">{icon('sparkle')}</span>
        <h3>Vapeur haute température</h3>
        <p>
          La vapeur sèche désinfecte par la chaleur seule, sans produit chimique. Elle décolle la graisse
          cuite d'une plancha, assainit un habitacle de voiture et élimine acariens et allergènes sur les
          surfaces textiles. Utile partout où l'on veut un résultat sain sans résidu.
        </p>
      </div>
      <div class="feature reveal">
        <span class="feature-icon">{icon('deck')}</span>
        <h3>Haute pression maîtrisée</h3>
        <p>
          Sur une terrasse, la pression se règle selon le support. Le béton, la pierre et le carrelage
          encaissent ; le bois, non — une pression trop forte ouvre la fibre et abîme la lame durablement.
          Nous privilégions le brossage doux sur bois, suivi d'un anti-mousse et, si besoin, d'un saturateur.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Nos engagements</span>
      <h2>Ce sur quoi vous pouvez compter</h2>
      <p class="lead">Des règles simples, valables sur toutes nos prestations et dans tous les départements franciliens.</p>
    </div>
    <div class="grid grid-3">{engagements}</div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Notre terrain</span>
        <h2>Particuliers et professionnels, partout en Île-de-France</h2>
        <p>
          Chez les particuliers, l'essentiel de notre activité tourne autour du
          <a href="services/nettoyage-textile-paris.html">textile</a> — canapés, matelas, tapis et
          moquettes — et du <a href="services/nettoyage-automobile-paris.html">nettoyage automobile</a>
          à domicile, souvent avant une revente ou après un long trajet. La
          <a href="services/nettoyage-terrasse-paris.html">remise en état des terrasses</a> complète
          ces demandes au fil des saisons.
        </p>
        <p>
          Côté professionnels, nous entretenons
          <a href="services/nettoyage-locaux-paris.html">bureaux, commerces et locaux d'activité</a> en
          passage régulier ou ponctuel, prenons en charge la
          <a href="services/nettoyage-fin-de-chantier-paris.html">remise en état après travaux</a> pour
          les artisans et les agences, et intervenons sur des
          <a href="services/nettoyage-bateau-paris.html">bateaux à quai</a> comme en
          <a href="services/nettoyage-avion-paris.html">cabine d'aviation d'affaires</a>.
        </p>
        <p>
          Le détail des villes couvertes, département par département, se trouve sur notre page
          <a href="zones.html">zones d'intervention</a>.
        </p>
        <div class="btn-row" style="margin-top:1.5rem">
          <a class="btn" href="devis.html">Demander un devis gratuit</a>
          <a class="btn btn-outline" href="tarifs.html">Voir les tarifs</a>
        </div>
      </div>
      <div class="media-frame reveal">
        <img src="assets/photos/intervention-1.webp" alt="Intervention MathClean en Île-de-France"
             loading="lazy" width="760" height="570">
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container-narrow">
    <div class="section-head center">
      <span class="eyebrow">Nos clients en parlent</span>
      <h2>Des avis publics, pas des témoignages choisis</h2>
    </div>
    <div class="notice notice-blue">
      {icon('star')}
      <p>
        Nous ne publions aucun avis rédigé par nos soins. Tous nos retours clients sont sur notre fiche
        Google, avec leur nom et leur date, consultables dans leur intégralité.
      </p>
    </div>
    <div class="btn-row center" style="margin-top:26px">
      <a class="btn" href="{SITE['review_url']}" target="_blank" rel="noopener">Lire les avis sur Google</a>
    </div>
  </div>
</section>

{cta_band(base)}
"""
    schema = [crumb_schema([("À propos", "a-propos.html")]),
              {"@context": "https://schema.org", "@type": "AboutPage",
               "name": "À propos de MathClean", "url": SITE["url"] + "/a-propos.html",
               "mainEntity": {"@id": SITE["url"] + "/#business"}}]
    html = (head("À propos — MathClean, entreprise de nettoyage en Île-de-France | MathClean",
                 "MathClean, entreprise individuelle installée à Tremblay-en-France : notre méthode "
                 "(injection-extraction, vapeur, haute pression), nos engagements et notre terrain.",
                 "a-propos.html", base, schema=schema)
            + header(base, "apropos") + body + footer(base))
    return write("a-propos.html", html)


# ===========================================================================
# DEVIS
# ===========================================================================
def build_devis():
    base = ""
    trail = [("Devis gratuit", None)]
    options = "".join('<option value="%s">%s</option>' % (s["nav"], s["nav"]) for s in SERVICES)
    body = f"""
{page_title_block(base, trail, "Demander un devis gratuit",
    "Décrivez-nous votre besoin en deux minutes. Nous vous répondons sous 24 h avec un devis ferme, "
    "détaillé poste par poste, gratuit et sans engagement.")}

<section class="section">
  <div class="container blog-layout">
    <div class="form-card" id="estimateur">
      <form action="{SITE['form_action']}" method="POST">
        <input type="hidden" name="_subject" value="Nouvelle demande de devis — MathClean">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_next" value="{SITE['url']}/merci.html">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">

        <h2 style="font-size:1.35rem">Votre demande</h2>
        <div class="form-grid" style="margin-top:22px">
          <div class="field">
            <label for="f-nom">Nom et prénom <span class="req">*</span></label>
            <input id="f-nom" name="Nom" type="text" required autocomplete="name" placeholder="Marie Dupont">
          </div>
          <div class="field">
            <label for="f-tel">Téléphone <span class="req">*</span></label>
            <input id="f-tel" name="Téléphone" type="tel" required autocomplete="tel" placeholder="06 12 34 56 78">
          </div>
          <div class="field field-full">
            <label for="f-mail">E-mail <span class="req">*</span></label>
            <input id="f-mail" name="Email" type="email" required autocomplete="email" placeholder="marie.dupont@exemple.fr">
          </div>

          <div class="field field-full">
            <label for="f-prestation">Prestation souhaitée <span class="req">*</span></label>
            <select id="f-prestation" name="Prestation" required>
              <option value="">— Choisissez une prestation —</option>
              {options}
              <option value="Plusieurs prestations">Plusieurs prestations / je ne sais pas encore</option>
            </select>
          </div>

          <div class="field field-full" id="estimation" hidden>
            <div class="notice notice-blue">
              {icon('info')}
              <p><strong>Repère de prix :</strong> <span id="estimation-txt"></span>
                 Les frais de déplacement ({SITE['travel_fee']}) s'ajoutent et vous sont annoncés
                 avant validation.</p>
            </div>
          </div>

          <div class="field">
            <label for="f-type">Vous êtes</label>
            <select id="f-type" name="Type de client">
              <option value="Particulier">Un particulier</option>
              <option value="Professionnel">Un professionnel / une entreprise</option>
            </select>
          </div>
          <div class="field">
            <label for="f-quand">Quand souhaitez-vous l'intervention ?</label>
            <select id="f-quand" name="Délai souhaité">
              <option value="Dès que possible">Dès que possible</option>
              <option value="Cette semaine">Cette semaine</option>
              <option value="Ce mois-ci">Ce mois-ci</option>
              <option value="Pas encore décidé">Pas encore décidé</option>
            </select>
          </div>

          <div class="field">
            <label for="f-adresse">Adresse d'intervention</label>
            <input id="f-adresse" name="Adresse" type="text" autocomplete="street-address" placeholder="12 rue de la Paix">
          </div>
          <div class="field">
            <label for="f-cp">Code postal et ville</label>
            <input id="f-cp" name="Code postal et ville" type="text" autocomplete="postal-code" placeholder="75002 Paris">
          </div>

          <div class="field field-full">
            <label for="f-message">Décrivez votre besoin <span class="req">*</span></label>
            <textarea id="f-message" name="Message" required
                      placeholder="Exemple : canapé d'angle en tissu beige, taches de café anciennes, 3e étage avec ascenseur."></textarea>
            <span class="field-hint">
              Plus vous êtes précis, plus le devis sera juste. N'hésitez pas à nous envoyer des photos
              par SMS au {SITE['phone']} après l'envoi du formulaire.
            </span>
          </div>

          <div class="field field-full">
            <label class="consent">
              <input type="checkbox" name="Consentement" value="oui" required>
              <span>
                J'accepte que mes informations soient utilisées pour être recontacté au sujet de ma
                demande. Voir la <a href="politique-confidentialite.html">politique de confidentialité</a>.
              </span>
            </label>
          </div>

          <div class="field field-full">
            <button class="btn btn-block" type="submit">Envoyer ma demande de devis</button>
            <span class="field-hint" style="margin-top:10px;text-align:center">
              Réponse sous 24 h · Gratuit et sans engagement · Aucun acompte
            </span>
          </div>
        </div>
      </form>
    </div>

    <aside class="sidebar">
      <div class="widget widget-cta">
        <h3 class="widget-title">Plus rapide par téléphone</h3>
        <p>Nous décrochons 7j/7, y compris tard le soir et tôt le matin.</p>
        <a class="widget-phone" href="tel:{SITE['phone_link']}">{SITE['phone']}</a>
        <a class="btn btn-light btn-block" href="tel:{SITE['phone_link']}">Appeler maintenant</a>
      </div>
      <div class="widget">
        <h3 class="widget-title">Ce qui se passe ensuite</h3>
        <div class="steps" style="grid-template-columns:1fr;gap:20px">
          <div class="step"><h3 style="font-size:1rem">Nous vous rappelons</h3><p>Sous 24 h, pour préciser votre besoin.</p></div>
          <div class="step"><h3 style="font-size:1rem">Vous recevez un devis ferme</h3><p>Détaillé poste par poste, frais de déplacement compris.</p></div>
          <div class="step"><h3 style="font-size:1rem">Nous intervenons</h3><p>Sous 24 à 72 h selon votre département.</p></div>
        </div>
      </div>
      <div class="widget">
        <h3 class="widget-title">Nos tarifs de référence</h3>
        <ul class="widget-links">
          <li><a href="tarifs.html">Detailing automobile<span>dès 40 €</span></a></li>
          <li><a href="tarifs.html">Canapé, matelas, tapis<span>dès 15 €</span></a></li>
          <li><a href="tarifs.html">Voir toute la grille<span>{icon('arrow')}</span></a></li>
        </ul>
      </div>
    </aside>
  </div>
</section>
"""
    html = (head("Devis gratuit de nettoyage à Paris & Île-de-France | MathClean",
                 "Demandez un devis gratuit et sans engagement pour un nettoyage automobile, textile, "
                 "terrasse, vitres ou locaux à Paris et en Île-de-France. Réponse sous 24 h.",
                 "devis.html", base, schema=[crumb_schema([("Devis gratuit", "devis.html")])])
            + header(base, "devis") + body + footer(base))
    return write("devis.html", html)


# ===========================================================================
# CONTACT
# ===========================================================================
def build_contact():
    base = ""
    trail = [("Contact", None)]
    options = "".join('<option value="%s">%s</option>' % (s["nav"], s["nav"]) for s in SERVICES)
    body = f"""
{page_title_block(base, trail, "Nous contacter",
    "Une question, un doute sur une matière, un besoin urgent ? Nous répondons 7j/7, "
    "y compris tard le soir et tôt le matin.")}

<section class="section">
  <div class="container">
    <div class="split" style="align-items:start">
      <div class="reveal">
        <span class="eyebrow">MathClean à votre service</span>
        <h2>Par téléphone, c'est le plus rapide</h2>
        <ul class="info-list" style="margin-top:1.8rem">
          <li>
            <span class="info-icon">{icon('phone')}</span>
            <div>
              <strong><a href="tel:{SITE['phone_link']}">{SITE['phone']}</a></strong>
              <span>{SITE['hours']} — vous parlez directement à la personne qui interviendra.</span>
            </div>
          </li>
          <li>
            <span class="info-icon">{icon('mail')}</span>
            <div>
              <strong><a href="mailto:{SITE['email']}">{SITE['email']}</a></strong>
              <span>Réponse sous 24 h. Vous pouvez joindre des photos à votre message.</span>
            </div>
          </li>
          <li>
            <span class="info-icon">{icon('pin')}</span>
            <div>
              <strong>{SITE['address']}, {SITE['postcode']} {SITE['city']}</strong>
              <span>Notre atelier. Nous nous déplaçons chez vous dans les huit départements franciliens.</span>
            </div>
          </li>
          <li>
            <span class="info-icon">{icon('clock')}</span>
            <div>
              <strong>Délais d'intervention</strong>
              <span>Paris et petite couronne : 24 à 48 h. Grande couronne : 48 à 72 h.</span>
            </div>
          </li>
        </ul>
        <div class="btn-row" style="margin-top:2rem">
          <a class="btn" href="tel:{SITE['phone_link']}">{icon('phone')}Appeler maintenant</a>
          <a class="btn btn-outline" href="{SITE['maps_url']}" target="_blank" rel="noopener">Obtenir l'itinéraire</a>
        </div>
      </div>

      <div class="form-card reveal">
        <h2 style="font-size:1.35rem">Écrivez-nous</h2>
        <p class="field-hint" style="margin-bottom:20px">
          Pour une demande chiffrée, préférez notre <a href="devis.html">formulaire de devis</a>,
          plus complet.
        </p>
        <form action="{SITE['form_action']}" method="POST">
          <input type="hidden" name="_subject" value="Message depuis le site — MathClean">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_next" value="{SITE['url']}/merci.html">
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="form-grid">
            <div class="field">
              <label for="c-nom">Nom et prénom <span class="req">*</span></label>
              <input id="c-nom" name="Nom" type="text" required autocomplete="name">
            </div>
            <div class="field">
              <label for="c-tel">Téléphone <span class="req">*</span></label>
              <input id="c-tel" name="Téléphone" type="tel" required autocomplete="tel">
            </div>
            <div class="field field-full">
              <label for="c-mail">E-mail <span class="req">*</span></label>
              <input id="c-mail" name="Email" type="email" required autocomplete="email">
            </div>
            <div class="field field-full">
              <label for="c-sujet">Sujet</label>
              <select id="c-sujet" name="Sujet">
                <option value="Question générale">Question générale</option>
                {options}
                <option value="Demande professionnelle">Demande professionnelle / entreprise</option>
              </select>
            </div>
            <div class="field field-full">
              <label for="c-message">Votre message <span class="req">*</span></label>
              <textarea id="c-message" name="Message" required></textarea>
            </div>
            <div class="field field-full">
              <label class="consent">
                <input type="checkbox" name="Consentement" value="oui" required>
                <span>J'accepte d'être recontacté au sujet de ma demande
                  (<a href="politique-confidentialite.html">politique de confidentialité</a>).</span>
              </label>
            </div>
            <div class="field field-full">
              <button class="btn btn-block" type="submit">Envoyer mon message</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container container-narrow">
    <div class="section-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>Peut-être avez-vous déjà la réponse</h2>
    </div>
    {faq_block(FAQ, 'faq-contact')}
  </div>
</section>

{cta_band(base)}
"""
    schema = [crumb_schema([("Contact", "contact.html")]),
              {"@context": "https://schema.org", "@type": "ContactPage",
               "url": SITE["url"] + "/contact.html",
               "mainEntity": {"@id": SITE["url"] + "/#business"}},
              faq_schema(FAQ)]
    html = (head("Contact — MathClean, nettoyage à Paris & Île-de-France | MathClean",
                 "Contactez MathClean au 06 23 07 52 59, 7j/7. Devis gratuit sous 24 h pour tout "
                 "nettoyage à domicile ou en entreprise à Paris et en Île-de-France.",
                 "contact.html", base, schema=schema)
            + header(base, "contact") + body + footer(base))
    return write("contact.html", html)


# ===========================================================================
# PAGES SIMPLES (merci, 404, mentions légales…)
# ===========================================================================
def simple_page(slug, title_tag, meta, h1, lead, content, trail_label, robots=None, current=""):
    base = ""
    body = f"""
{page_title_block(base, [(trail_label, None)], h1, lead)}

<section class="section">
  <div class="container container-narrow">
    <div class="entry-content">{content}</div>
  </div>
</section>

{cta_band(base)}
"""
    html = (head(title_tag, meta, slug, base, robots=robots,
                 schema=[crumb_schema([(trail_label, slug)])])
            + header(base, current) + body + footer(base))
    return write(slug, html)


def build_merci():
    base = ""
    body = f"""
<section class="section" style="padding-top:70px">
  <div class="container container-narrow text-center">
    <span class="feature-icon mx-auto" style="width:74px;height:74px">{icon('check')}</span>
    <h1 style="margin-top:22px">Merci, votre demande est bien partie</h1>
    <p class="lead">
      Nous revenons vers vous <strong>sous 24 heures</strong> avec un devis ferme, détaillé poste par
      poste. En attendant, vous pouvez nous envoyer des photos par SMS au {SITE['phone']} :
      cela nous aide à chiffrer plus précisément.
    </p>
    <div class="btn-row center" style="margin-top:30px">
      <a class="btn" href="tel:{SITE['phone_link']}">{icon('phone')}{SITE['phone']}</a>
      <a class="btn btn-outline" href="index.html">Retour à l'accueil</a>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">En attendant</span>
      <h2>Nos conseils d'entretien</h2>
    </div>
    <div class="grid grid-3">{"".join(post_card(base, p) for p in POSTS[:3])}</div>
  </div>
</section>
"""
    html = (head("Merci — votre demande a bien été envoyée | MathClean",
                 "Votre demande de devis a bien été transmise à MathClean. Réponse sous 24 h.",
                 "merci.html", base, robots="noindex")
            + header(base) + body + footer(base))
    return write("merci.html", html)


def build_404():
    base = ""
    body = f"""
<section class="section" style="padding-top:70px">
  <div class="container container-narrow text-center">
    <span class="eyebrow">Erreur 404</span>
    <h1>Cette page n'existe pas (ou plus)</h1>
    <p class="lead">
      Le lien est peut-être ancien, ou comporte une faute de frappe. Voici les pages les plus utiles.
    </p>
    <div class="btn-row center" style="margin-top:28px">
      <a class="btn" href="index.html">Retour à l'accueil</a>
      <a class="btn btn-outline" href="services.html">Voir nos prestations</a>
      <a class="btn btn-outline" href="devis.html">Demander un devis</a>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center"><h2>Nos prestations</h2></div>
    <div class="grid grid-3">{"".join(service_card(base, s) for s in SERVICES[:6])}</div>
  </div>
</section>
"""
    html = (head("Page introuvable | MathClean",
                 "La page demandée n'existe pas. Retrouvez nos prestations de nettoyage à Paris et en Île-de-France.",
                 "404.html", base, robots="noindex")
            + header(base) + body + footer(base))
    return write("404.html", html)


def build_legal():
    """Mentions légales, confidentialité et cookies, reprises du site existant."""
    written = []

    mentions = f"""
<h2>1. Éditeur du site</h2>
<p>
  Le site <strong>mathclean.fr</strong> est édité par <strong>{SITE['name']}</strong> — entreprise
  individuelle (micro-entreprise / auto-entrepreneur).
</p>
<ul>
  <li>Responsable de la publication : {SITE['manager']}.</li>
  <li>Siège / adresse professionnelle : {SITE['address']}, {SITE['postcode']} {SITE['city']}, France.</li>
  <li>Téléphone : <a href="tel:{SITE['phone_link']}">{SITE['phone']}</a></li>
  <li>E-mail : <a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
  <li>SIRET : {SITE['siret']} — SIREN : {SITE['siren']}</li>
  <li>TVA : TVA non applicable, article 293 B du Code général des impôts (franchise en base de TVA).</li>
</ul>

<h2>2. Hébergement</h2>
<p>
  Le site est hébergé par <strong>Cloudflare, Inc.</strong>, 101 Townsend Street, San Francisco,
  CA 94107, États-Unis — <a href="https://www.cloudflare.com" target="_blank" rel="noopener">www.cloudflare.com</a>.
</p>

<h2>3. Propriété intellectuelle</h2>
<p>
  L'ensemble des éléments du site (textes, logo, charte graphique, mise en page) est la propriété de
  {SITE['name']}, sauf mention contraire. Les photographies d'illustration proviennent de banques
  d'images libres de droits (Pexels) ou de nos propres interventions. Toute reproduction ou
  représentation, totale ou partielle, sans autorisation écrite préalable, est interdite.
</p>

<h2>4. Responsabilité</h2>
<p>
  {SITE['name']} s'efforce de fournir des informations exactes et à jour. Les tarifs « à partir de »
  sont indicatifs ; seul le devis accepté fait foi. {SITE['name']} ne saurait être tenue responsable
  d'éventuelles erreurs, omissions ou d'une indisponibilité temporaire du site.
</p>

<h2>5. Liens et données</h2>
<p>
  Pour en savoir plus sur le traitement de vos données personnelles, consultez notre
  <a href="politique-confidentialite.html">politique de confidentialité</a>. Pour les traceurs utilisés,
  consultez notre <a href="politique-cookies.html">politique de cookies</a>.
</p>

<h2>6. Droit applicable</h2>
<p>
  Les présentes mentions légales sont régies par le droit français. En cas de litige, et à défaut de
  résolution amiable, les tribunaux français seront seuls compétents.
</p>
"""
    written.append(simple_page(
        "mentions-legales.html",
        "Mentions légales | MathClean",
        "Mentions légales du site mathclean.fr : éditeur, hébergement, propriété intellectuelle et droit applicable.",
        "Mentions légales", "Informations légales relatives au site mathclean.fr et à l'entreprise MathClean.",
        mentions, "Mentions légales"))

    confidentialite = f"""
<blockquote><p>
  <strong>En bref :</strong> nous collectons uniquement les informations nécessaires pour établir vos
  devis et réaliser nos prestations. Nous ne les vendons jamais et vous pouvez demander leur suppression
  à tout moment.
</p></blockquote>

<h2>1. Responsable du traitement</h2>
<p>
  Le responsable du traitement des données est <strong>{SITE['name']}</strong> ({SITE['manager']},
  entrepreneur individuel), {SITE['address']}, {SITE['postcode']} {SITE['city']}.
  Contact : <a href="mailto:{SITE['email']}">{SITE['email']}</a> — {SITE['phone']}.
</p>

<h2>2. Données que nous collectons</h2>
<p>Lorsque vous remplissez un formulaire de devis ou de contact, nous pouvons collecter :</p>
<ul>
  <li>votre <strong>nom et prénom</strong> ;</li>
  <li>vos <strong>coordonnées</strong> (e-mail, téléphone) ;</li>
  <li>l'<strong>adresse d'intervention</strong> ;</li>
  <li>la <strong>description de votre besoin</strong> et, le cas échéant, les <strong>photos</strong> que vous nous transmettez ;</li>
  <li>les informations liées à votre demande (service, délai souhaité).</li>
</ul>
<p>Nous ne collectons aucune donnée sensible et n'utilisons aucun outil de publicité ciblée.</p>

<h2>3. Pourquoi (finalités) et sur quelle base</h2>
<ul>
  <li>Établir un <strong>devis</strong> et vous <strong>répondre</strong> — base : votre demande / mesures précontractuelles ;</li>
  <li>Organiser et réaliser la <strong>prestation</strong> — base : exécution du contrat ;</li>
  <li>Assurer le <strong>suivi et la facturation</strong> — base : obligation légale (comptabilité).</li>
</ul>

<h2>4. Qui a accès à vos données</h2>
<p>
  Vos données sont destinées uniquement à {SITE['name']}. Elles ne sont <strong>ni vendues ni
  cédées</strong> à des tiers à des fins commerciales. Pour recevoir les messages de vos formulaires,
  nous utilisons le service <strong>FormSubmit</strong> (envoi d'e-mails) ; le site est hébergé par
  <strong>Cloudflare</strong>. Ces prestataires techniques agissent en tant que sous-traitants. Certains
  serveurs pouvant être situés hors de l'Union européenne, les transferts éventuels sont encadrés par
  des garanties appropriées.
</p>

<h2>5. Combien de temps nous les conservons</h2>
<p>
  Les demandes de devis et les données de prospects sont conservées <strong>3 ans</strong> à compter du
  dernier contact, conformément à la recommandation de la CNIL en matière de prospection commerciale.
  Les documents comptables (clients) sont conservés selon les durées légales en vigueur
  (généralement 10 ans).
</p>

<h2>6. Vos droits (RGPD)</h2>
<p>
  Conformément au Règlement (UE) 2016/679 (RGPD) et à la loi « Informatique et Libertés », vous disposez
  d'un droit d'<strong>accès</strong>, de <strong>rectification</strong>, d'<strong>effacement</strong>,
  de <strong>limitation</strong>, d'<strong>opposition</strong> et de <strong>portabilité</strong> de
  vos données.
</p>
<p>
  Pour exercer ces droits, écrivez-nous à <a href="mailto:{SITE['email']}">{SITE['email']}</a>. Vous
  pouvez également introduire une réclamation auprès de la CNIL
  (<a href="https://www.cnil.fr" target="_blank" rel="noopener">www.cnil.fr</a>).
</p>

<h2>7. Cookies</h2>
<p>Le détail des traceurs utilisés figure dans notre <a href="politique-cookies.html">politique de cookies</a>.</p>

<h2>8. Mise à jour</h2>
<p>La présente politique peut être mise à jour. Dernière mise à jour : {TODAY}.</p>
"""
    written.append(simple_page(
        "politique-confidentialite.html",
        "Politique de confidentialité | MathClean",
        "Comment MathClean collecte, utilise et protège vos données personnelles. Vos droits RGPD et durées de conservation.",
        "Politique de confidentialité", "Vos données, votre confiance.",
        confidentialite, "Politique de confidentialité"))

    cookies = f"""
<blockquote><p>
  <strong>L'essentiel :</strong> ce site n'utilise <strong>aucun cookie publicitaire ni de traçage</strong>.
  Nous n'employons ni Google Analytics, ni pixel de réseau social, ni régie publicitaire.
</p></blockquote>

<h2>1. Qu'est-ce qu'un cookie ?</h2>
<p>
  Un « cookie » (ou traceur) est un petit fichier déposé sur votre appareil lorsque vous visitez un site.
  Il peut servir à faire fonctionner le site, à mémoriser vos préférences, ou — pour certains — à vous
  suivre à des fins statistiques ou publicitaires.
</p>

<h2>2. Les traceurs utilisés sur ce site</h2>
<p>Nous utilisons uniquement un stockage local <strong>strictement fonctionnel</strong> :</p>
<ul>
  <li>
    <strong>Bandeau d'information (« mcCookies »)</strong> — mémorise, sur votre propre navigateur, que
    vous avez vu et fermé notre bandeau, pour ne pas le réafficher à chaque visite.
  </li>
</ul>
<p>
  Cet élément étant strictement nécessaire au service que vous demandez, il ne requiert pas votre
  consentement préalable au sens de la réglementation. Il reste sur votre appareil et n'est transmis
  à personne.
</p>

<h2>3. Services tiers</h2>
<p>
  Certaines ressources peuvent être fournies par des services externes, qui reçoivent votre adresse IP
  du fait de leur chargement :
</p>
<ul>
  <li><strong>FormSubmit</strong> — acheminement des messages de vos formulaires ;</li>
  <li><strong>Cloudflare</strong> — hébergement et diffusion du site.</li>
</ul>
<p>
  Ces services ne déposent pas de cookie publicitaire dans le cadre de leur usage sur ce site. Le site
  n'utilise aucune police d'écriture ni ressource chargée depuis un serveur tiers : tout est servi
  depuis notre propre hébergement.
</p>

<h2>4. Gérer ou supprimer les traceurs</h2>
<p>
  Vous pouvez à tout moment effacer le stockage local et les cookies depuis les réglages de votre
  navigateur (rubrique « Confidentialité » / « Données de sites »). Cette suppression n'affecte
  en rien nos prestations.
</p>

<h2>5. Évolution</h2>
<p>
  Si nous ajoutions un jour un outil de mesure d'audience ou de publicité (par exemple Google Analytics),
  nous mettrions en place un véritable bandeau de consentement (accepter / refuser) et mettrions à jour
  la présente page.
</p>
<p>
  Pour toute question : <a href="mailto:{SITE['email']}">{SITE['email']}</a>.
  Voir aussi notre <a href="politique-confidentialite.html">politique de confidentialité</a>.
</p>
"""
    written.append(simple_page(
        "politique-cookies.html",
        "Politique de cookies | MathClean",
        "Ce site n'utilise aucun cookie publicitaire ni outil de traçage. Détail des traceurs strictement fonctionnels employés.",
        "Politique de cookies", "Transparence sur les traceurs utilisés par mathclean.fr.",
        cookies, "Politique de cookies"))

    return written


# ===========================================================================
# SITEMAP & ROBOTS
# ===========================================================================
def build_sitemap(urls):
    entries = ""
    for path, priority, freq in urls:
        loc = SITE["url"] + "/" + ("" if path == "index.html" else path)
        entries += (
            "  <url><loc>%s</loc><lastmod>%s</lastmod>"
            "<changefreq>%s</changefreq><priority>%s</priority></url>\n"
            % (loc, TODAY, freq, priority)
        )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + entries + "</urlset>\n")
    return write("sitemap.xml", xml)


def build_robots():
    return write("robots.txt",
                 "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE["url"])


# ===========================================================================
# ORCHESTRATION
# ===========================================================================
def copy_theme_assets():
    for src, dst in (("theme/theme.css", "site/assets/css/theme.css"),
                     ("theme/theme.js", "site/assets/js/theme.js")):
        shutil.copyfile(os.path.join(HERE, src), os.path.join(HERE, dst))


def main():
    copy_theme_assets()
    pages = []

    pages.append((build_home(), "1.0", "weekly"))
    pages.append((build_services_archive(), "0.9", "monthly"))
    for s in SERVICES:
        pages.append((build_service(s), "0.9", "monthly"))
    pages.append((build_tarifs(), "0.9", "monthly"))
    pages.append((build_realisations(), "0.7", "monthly"))
    pages.append((build_zones_archive(), "0.8", "monthly"))
    for z in ZONES:
        pages.append((build_zone(z), "0.8", "monthly"))
    pages.append((build_blog_archive(), "0.7", "weekly"))
    for i, p in enumerate(POSTS):
        prev_post = POSTS[i - 1] if i > 0 else None
        next_post = POSTS[i + 1] if i < len(POSTS) - 1 else None
        pages.append((build_post(p, prev_post, next_post), "0.6", "yearly"))
    pages.append((build_apropos(), "0.8", "yearly"))
    pages.append((build_devis(), "0.9", "monthly"))
    pages.append((build_contact(), "0.8", "yearly"))
    for path in build_legal():
        pages.append((path, "0.3", "yearly"))

    build_merci()   # noindex : hors sitemap
    build_404()     # noindex : hors sitemap

    build_sitemap(pages)
    build_robots()

    print("Site généré dans %s" % OUT)
    print("%d pages indexables + merci.html, 404.html, sitemap.xml, robots.txt" % len(pages))


if __name__ == "__main__":
    main()
