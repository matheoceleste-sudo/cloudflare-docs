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

import hashlib
import unicodedata
import re
import json
import os
import shutil
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from content import (
    DATE_GUIDES, DATE_GUIDES_FR,  # noqa: E402
    SITE, SERVICES, ZONES, POSTS, FAQ, ENGAGEMENTS, BEFORE_AFTER, BEFORE_AFTER_HD,
    PACKS_AUTO, OPTIONS_AUTO, TARIFS_TEXTILE, TARIFS_DEVIS,
    GOOGLE_NOTE, REVIEWS, DEPLACEMENT, CRENEAUX, HERO, VILLES, GUIDES,
)

OUT = os.path.join(HERE, "site")
TODAY = date.today().isoformat()


def empreinte(chemin):
    """Huit caractères tirés du contenu du fichier, pour casser les caches."""
    try:
        with open(os.path.join(HERE, chemin), "rb") as fh:
            return hashlib.sha1(fh.read()).hexdigest()[:8]
    except OSError:
        return "0"


_MOTS = {1: "une", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six",
         7: "sept", 8: "huit", 9: "neuf", 10: "dix", 11: "onze", 12: "douze"}


def en_lettres(n):
    """Nombre en toutes lettres, chiffre au-delà de douze."""
    return _MOTS.get(n, str(n))


NB_SERVICES = en_lettres(len(SERVICES))
NB_ZONES = en_lettres(len(ZONES))


def titre_page(t):
    """Ajoute la marque au titre, mais seulement si Google peut encore l'afficher.

    Google tronque autour de 60 caractères ; au-delà, le suffixe de marque
    ne fait que masquer la fin du titre. On l'omet donc quand ça ne rentre pas,
    et on ne le répète jamais si la marque est déjà dans le titre.
    """
    t = t.strip()
    if SITE["name"].lower() in t.lower():
        return t
    suffixe = " | " + SITE["name"]
    return t + suffixe if len(t) + len(suffixe) <= 60 else t


def slug_ancre(txt):
    """Ancre d'URL lisible : sans accent, sans espace, en minuscules."""
    base = unicodedata.normalize("NFKD", str(txt))
    base = "".join(c for c in base if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")


def liste_prestations(sep=", ", fin=" et "):
    """Énumération des prestations, dérivée de SERVICES pour ne jamais dater."""
    noms = [s["short"].lower() for s in SERVICES]
    return sep.join(noms[:-1]) + fin + noms[-1]


_AMP = re.compile(r"&(?!(?:[a-zA-Z][a-zA-Z0-9]{1,31}|#\d{1,7}|#[xX][0-9a-fA-F]{1,6});)")


def esc(txt):
    """Échappe une valeur destinée à un attribut HTML, sans doubler les entités."""
    return _AMP.sub("&amp;", str(txt)).replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

V_CSS = empreinte("theme/theme.css")
V_JS = empreinte("theme/theme.js")
V_RESA = empreinte("theme/reservation.js")

# ---------------------------------------------------------------------------
# Jeu d'icônes (contours 24×24, héritent de currentColor)
# ---------------------------------------------------------------------------
ICONS = {
    "car":      '<path d="M5 17h14M6.5 17V9.7l1.7-3.9A2 2 0 0 1 10 4.6h4a2 2 0 0 1 1.8 1.2l1.7 3.9V17M4 12h16"/><circle cx="8" cy="17" r="1.6"/><circle cx="16" cy="17" r="1.6"/>',
    "sofa":     '<path d="M3 17v-5.5A2.5 2.5 0 0 1 5.5 9h13A2.5 2.5 0 0 1 21 11.5V17M3 17h18M5 17v2M19 17v2M6 9V7a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v2"/>',
    "boat":     '<path d="M4 17l1.6-5.6a1 1 0 0 1 .96-.72h10.88a1 1 0 0 1 .96.72L20 17M12 10.7V4.4M12 4.4l4.6 2.3-4.6 2M2.6 19.6c1.6 0 1.6 1.2 3.2 1.2s1.6-1.2 3.2-1.2 1.6 1.2 3.2 1.2 1.6-1.2 3.2-1.2 1.6 1.2 3.2 1.2"/>',
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
    "ozone":    '<circle cx="6.5" cy="14.5" r="3.1"/><circle cx="17.5" cy="14.5" r="3.1"/><circle cx="12" cy="6.5" r="3.1"/><path d="M8.9 12.2 10.4 9.4M13.6 9.4l1.5 2.8M9.6 14.5h4.8"/>',
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
def head(title, meta, canonical, base, image="assets/img/og-image.png", schema=None,
         robots=None, og_type="website", published=None, modified=None, preload=None):
    """En-tête commun à toutes les pages.

    `og_type`  : "article" sur les billets et les guides, "website" ailleurs.
    `published`/`modified` : dates ISO, ajoutées en Open Graph pour les articles.
    `preload`  : chemin d'image LCP à précharger (relatif à `base`).
    """
    ld = ""
    for block in (schema or []):
        ld += '<script type="application/ld+json">%s</script>\n' % json.dumps(
            block, ensure_ascii=False, separators=(",", ":")
        )
    if robots == "noindex":
        directives = "noindex,follow"
    else:
        # Autorise les grandes vignettes dans Google Images et Discover,
        # et lève la limite de longueur des extraits affichés.
        directives = "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    og_art = ""
    if og_type == "article":
        if published:
            og_art += '<meta property="article:published_time" content="%s">\n' % published
        og_art += '<meta property="article:modified_time" content="%s">\n' % (modified or published or "")
        og_art += '<meta property="article:author" content="%s">\n' % esc(SITE["manager"])
    pre = ""
    if preload:
        pre = '<link rel="preload" as="image" href="%s%s" fetchpriority="high">\n' % (base, preload)
    t, m = esc(title), esc(meta)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{m}">
<meta name="robots" content="{directives}">
<link rel="canonical" href="{SITE['url']}/{canonical}">
<meta name="author" content="{esc(SITE['manager'])}">
<meta name="theme-color" content="#0e5fbb">
<meta name="geo.region" content="FR-IDF">
<meta name="geo.placename" content="{esc(SITE['city'])}">
<meta name="geo.position" content="{SITE['lat']};{SITE['lon']}">
<meta name="ICBM" content="{SITE['lat']}, {SITE['lon']}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(SITE['name'])}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{SITE['url']}/{canonical}">
<meta property="og:image" content="{SITE['url']}/{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(SITE['name'])} — {esc(SITE['slogan'])}">
{og_art}<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{m}">
<meta name="twitter:image" content="{SITE['url']}/{image}">
<link rel="icon" href="{base}assets/img/lion.svg" type="image/svg+xml">
<link rel="stylesheet" href="{base}assets/css/theme.css?v={V_CSS}">
{pre}<script>document.documentElement.className+=' js';</script>
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
    <li><a href="{base}zones.html"><strong>Les 8 départements</strong></a></li>
    <li><a href="{base}villes.html"><strong>Toutes les villes</strong></a></li>
  </ul>
</li>
<li class="menu-item-has-children{' current-menu-item' if current in ('blog', 'guides') else ''}">
  <a href="{base}guides.html">Conseils {icon('chevron', 'caret')}</a>
  <ul class="sub-menu">
    <li><a href="{base}guides.html"><strong>Guides pratiques</strong></a></li>
    <li><a href="{base}blog.html"><strong>Astuces &amp; conseils</strong></a></li>
  </ul>
</li>
<li{cls('apropos')}><a href="{base}a-propos.html">À propos</a></li>
<li{cls('contact')}><a href="{base}contact.html">Contact</a></li>
</ul>
<div class="nav-cta">
  <a class="btn" href="{base}reservation.html">Réserver en ligne</a>
  <a class="btn btn-outline" href="{base}devis.html">Demander un devis</a>
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
      <a class="btn btn-sm" href="{base}reservation.html">Réserver</a>
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
      <a class="btn btn-light" href="{base}reservation.html">Réserver en ligne</a>
      <a class="btn btn-ghost-light" href="{base}devis.html">Demander un devis</a>
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
          Entreprise de nettoyage à domicile et en entreprise, à Paris et dans les {NB_ZONES} départements
          d'Île-de-France&nbsp;: {liste_prestations().capitalize()}.
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
        <h2 class="widget-title">Prestations</h2>
        <ul>{services_links}</ul>
      </div>
      <div>
        <h2 class="widget-title">Zones</h2>
        <ul>{zones_links}<li><a href="{base}zones.html">Les 8 départements</a></li>
        <li><a href="{base}villes.html">Toutes les villes</a></li></ul>
      </div>
      <div>
        <h2 class="widget-title">L'entreprise</h2>
        <ul>
          <li><a href="{base}a-propos.html">À propos</a></li>
          <li><a href="{base}tarifs.html">Tarifs</a></li>
          <li><a href="{base}realisations.html">Réalisations</a></li>
          <li><a href="{base}guides.html">Guides pratiques</a></li>
          <li><a href="{base}blog.html">Conseils &amp; astuces</a></li>
          <li><a href="{base}reservation.html">Réserver en ligne</a></li>
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
  <a href="{base}reservation.html">{icon('calendar')}Réserver</a>
</div>

<div class="cookie-bar" id="cookie-bar" role="dialog" aria-label="Information cookies">
  <p>Ce site n'utilise <strong>aucun cookie publicitaire</strong> ni outil de traçage — uniquement un
     stockage local strictement nécessaire. <a href="{base}politique-cookies.html">En savoir plus</a>.</p>
  <button class="btn btn-sm" id="cookie-ok" type="button">J'ai compris</button>
</div>

<script src="{base}assets/js/theme.js?v={V_JS}" defer></script>
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


def service_tile(base, s):
    """
    Vignette pleine image : photo en fond, nom de la prestation en capitales
    par-dessus. Format immersif, réservé aux deux grandes vitrines
    (accueil et page Prestations) ; les listes secondaires gardent la carte
    compacte `service_card`.
    """
    return f"""<a class="tile reveal" href="{base}services/{s['slug']}.html" aria-label="{s['name']}">
  <img src="{base}assets/photos/{s['image']}" alt="{s['name']}" loading="lazy" width="640" height="420">
  <span class="tile-veil"></span>
  <span class="tile-price">{s['price']}</span>
  <span class="tile-body">
    <span class="tile-name">{s['short']}</span>
    <span class="tile-more">En savoir plus {icon('arrow')}</span>
  </span>
</a>"""


def ba_block(base, before, after, title, sub, idx, largeur=800):
    """Comparateur avant/après. `largeur` = largeur d'affichage réelle, déclarée
    sur les images pour que le navigateur réserve la bonne place."""
    return f"""<div class="reveal">
  <div class="ba" style="--pos:50%">
    <div class="ba-pane">
      <img src="{base}assets/photos/{before}" alt="{title} avant l'intervention MathClean"
           loading="lazy" width="{largeur}" height="{largeur * 3 // 4}">
      <img class="ba-after" src="{base}assets/photos/{after}" alt="{title} après l'intervention MathClean"
           loading="lazy" width="{largeur}" height="{largeur * 3 // 4}">
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


def editeur_schema():
    """Éditeur des articles : objet complet plutôt qu'un simple @id, pour que
    les validateurs n'aient pas à résoudre une référence hébergée ailleurs."""
    return {
        "@type": "Organization",
        "@id": SITE["url"] + "/#business",
        "name": SITE["name"],
        "url": SITE["url"] + "/",
        "logo": {"@type": "ImageObject",
                 "url": SITE["url"] + "/assets/img/og-image.png",
                 "width": 1200, "height": 630},
    }


def auteur_schema():
    """Auteur : la personne qui signe les articles sur le site."""
    return {"@type": "Person", "name": SITE["manager"],
            "url": SITE["url"] + "/a-propos.html",
            "worksFor": {"@id": SITE["url"] + "/#business"}}


def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": SITE["url"] + "/#business",
        "name": SITE["name"],
        "slogan": SITE["slogan"],
        "description": ("Entreprise de nettoyage à domicile et en entreprise à Paris et en "
                        "Île-de-France : %s. Devis gratuit, intervention 7j/7, sans acompte."
                        % liste_prestations()),
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


_IMG_LAZY = re.compile(r'<img\b(?![^>]*\bfetchpriority=)[^>]*?\sloading="lazy"[^>]*>')


def promouvoir_image_lcp(html):
    """Sort la première image du contenu du chargement différé.

    C'est presque toujours l'élément LCP de la page : la laisser en
    `loading="lazy"` retarde son affichage et pénalise le score Core Web
    Vitals. On la traite ici, une fois pour toutes, plutôt que dans chaque
    gabarit — l'accueil, lui, précharge déjà son héros et n'est pas concerné.
    """
    debut = html.find('<main')
    if debut == -1 or 'fetchpriority="high"' in html:
        # La page désigne déjà son élément LCP (le héros de l'accueil).
        return html
    m = _IMG_LAZY.search(html, debut)
    if not m:
        return html
    balise = m.group(0).replace(' loading="lazy"', ' loading="eager" fetchpriority="high"')
    return html[:m.start()] + balise + html[m.end():]


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(promouvoir_image_lcp(html))
    return path


# ===========================================================================
# ACCUEIL
# ===========================================================================
def build_home():
    base = ""
    # Six vignettes sur l'accueil ; la septième reste accessible par le bouton
    # « voir toutes les prestations » et par la page Prestations.
    cards = "".join(service_tile(base, s) for s in SERVICES[:6])
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
        ba_block(base, b, a, t, s, i)
        for i, (b, a, t, s) in enumerate(BEFORE_AFTER[:BEFORE_AFTER_HD])
    )
    posts = "".join(post_card(base, p) for p in POSTS[:3])

    body = f"""
<section class="hero">
  <div class="hero-media">
    <img src="assets/photos/{HERO['image']}" alt="{HERO['alt']}"
         width="1125" height="1500" fetchpriority="high"
         style="object-position:{HERO['position']}">
  </div>
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow eyebrow-gold">{SITE['name']} · {SITE['slogan']}</span>
      <h1>Entreprise de nettoyage à Paris <em>&amp; en Île-de-France</em></h1>
      <p class="hero-lead">
        {liste_prestations().capitalize()}.
        Nous venons chez vous, entièrement équipés, 7&nbsp;jours sur 7 — sans acompte,
        et vous ne réglez qu'une fois le résultat constaté.
      </p>
      <div class="hero-badges">
        <span class="badge">{icon('check')}Intervention sous 24 h</span>
        <span class="badge">{icon('check')}Devis gratuit et ferme</span>
        <span class="badge">{icon('check')}8 départements couverts</span>
      </div>
      <div class="btn-row">
        <a class="btn btn-gold" href="reservation.html">Réserver en ligne</a>
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
      <h2>{NB_SERVICES.capitalize()} métiers, une seule exigence</h2>
      <p class="lead">
        Chaque matière appelle un produit et un geste différents. C'est ce travail de diagnostic —
        comprendre la matière avant de la nettoyer — qui sépare un résultat correct d'un résultat qui tient.
      </p>
    </div>
    <div class="tile-grid">{cards}</div>
    <div class="btn-row center" style="margin-top:36px">
      <a class="btn btn-outline" href="services.html">Voir les {NB_SERVICES} prestations</a>
    </div>
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

{reviews_section(base, soft=False)}

<section class="section section-soft">
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

<section class="section">
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
        {"@context": "https://schema.org", "@type": "WebSite",
         "@id": SITE["url"] + "/#site", "name": SITE["name"],
         "url": SITE["url"] + "/", "inLanguage": "fr-FR",
         "publisher": {"@id": SITE["url"] + "/#business"}},
    ]
    html = (
        head(titre_page("Entreprise de nettoyage à Paris et en Île-de-France"),
             "Nettoyage auto, textile, bateau, terrasse, vitres, entreprise et fin de chantier "
             "à Paris et en Île-de-France. 7j/7, devis gratuit, sans acompte.",
             "", base, schema=schema,
             preload="assets/photos/" + HERO["image"])
        + header(base, "home") + body + footer(base)
    )
    return write("index.html", html)


# ===========================================================================
# PRESTATIONS
# ===========================================================================
def build_services_archive():
    base = ""
    trail = [("Prestations", None)]
    cards = "".join(service_tile(base, s) for s in SERVICES)
    detail = "".join(
        '<dt><a href="services/%s.html">%s</a> <span class="presta-prix">%s</span></dt>'
        '<dd>%s</dd>' % (x["slug"], x["name"], x["price"], x["excerpt"])
        for x in SERVICES
    )
    liste_schema = {
        "@context": "https://schema.org", "@type": "ItemList",
        "name": "Prestations de nettoyage MathClean",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": x["name"],
             "url": "%s/services/%s.html" % (SITE["url"], x["slug"])}
            for i, x in enumerate(SERVICES)
        ],
    }
    body = f"""
{page_title_block(base, trail, "Nos prestations de nettoyage",
    "%s métiers, à domicile comme en entreprise, partout à Paris et en Île-de-France. " % NB_SERVICES.capitalize() +
    "Chaque prestation dispose de sa page dédiée : méthode, contenu détaillé et réponses aux questions courantes.")}

<section class="section">
  <div class="container">
    <div class="tile-grid tile-grid--all">{cards}</div>
  </div>
</section>

<section class="section">
  <div class="container container-narrow">
    <h2>Ce que recouvre chaque prestation</h2>
    <dl class="presta-detail">{detail}</dl>
  </div>
</section>

<section class="section section-soft">
  <div class="container container-narrow">
    <h2>Comment savoir laquelle vous concerne</h2>
    <p>
      La question n'est pas tant la surface que la <strong>matière</strong> et l'<strong>état</strong>.
      Un textile taché en profondeur relève de l'injection-extraction, pas d'un shampoing de surface.
      Une pierre poreuse ne supporte pas la même pression qu'une dalle béton. Un local vidé après
      travaux demande deux passages, parce que la poussière de plâtre retombe pendant vingt-quatre heures.
      C'est pour cela que chaque prestation a sa page&nbsp;: elle décrit la méthode employée, ce qui est
      inclus, et ce qui ne l'est pas.
    </p>
    <p>
      Trois repères simples pour vous orienter&nbsp;:
    </p>
    <ul class="checklist">
      <li>Une <strong>odeur</strong> qui revient malgré un nettoyage&nbsp;: la source est encore là.
        C'est le domaine du <a href="services/traitement-ozone-paris.html">traitement par ozone</a>,
        après nettoyage et non à sa place.</li>
      <li>Une <strong>tache</strong> ancienne sur un tissu&nbsp;: ne la frottez pas avant notre passage,
        vous risquez de l'étaler dans la fibre. Voir le
        <a href="services/nettoyage-textile-paris.html">nettoyage textile</a>.</li>
      <li>Un <strong>besoin régulier</strong> plutôt qu'une intervention unique&nbsp;: nous établissons
        un rythme et un tarif fixes. Voir le
        <a href="services/nettoyage-entreprise-paris.html">nettoyage pour entreprise</a>.</li>
    </ul>
    <p>
      Dans le doute, notre <a href="guides.html">bibliothèque de guides</a> détaille les méthodes,
      les prix constatés et les erreurs qui coûtent cher. Et si votre besoin n'entre dans aucune
      case, dites-le-nous&nbsp;: nous vous répondrons franchement, y compris si ce n'est pas notre métier.
    </p>
    <div class="notice notice-blue" style="margin-top:30px">
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
    html = (head(titre_page("Nos prestations de nettoyage à Paris et en IDF"),
                 "Les %s prestations MathClean : auto, textile, bateau, terrasse, vitres, "
                 "entreprise, ozone, fin de chantier. À Paris et en IDF." % NB_SERVICES,
                 "services.html", base,
                 schema=[crumb_schema([("Prestations", "services.html")]), liste_schema])
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
    html = (head(titre_page(s["title"]), s["meta"], "services/%s.html" % s["slug"], base, schema=schema)
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
    html = (head(titre_page("Tarifs de nettoyage à Paris — auto dès 40 €"),
                 "Tarifs MathClean : packs auto de 40 à 240 €, textile dès 15 €, professionnel "
                 "sur devis. Sans acompte, frais de déplacement annoncés d'avance.",
                 "tarifs.html", base, schema=schema)
            + header(base, "tarifs") + body + footer(base))
    return write("tarifs.html", html)


# ===========================================================================
# RÉALISATIONS
# ===========================================================================
def build_realisations():
    base = ""
    trail = [("Réalisations", None)]
    ba = "".join(ba_block(base, b, a, t, s, i)
                 for i, (b, a, t, s) in enumerate(BEFORE_AFTER[:BEFORE_AFTER_HD]))
    # Les clichés de faible définition passent dans une grille de trois colonnes :
    # affichés petit, ils restent nets.
    ba_petit = "".join(ba_block(base, b, a, t, s, i + BEFORE_AFTER_HD, largeur=380)
                       for i, (b, a, t, s) in enumerate(BEFORE_AFTER[BEFORE_AFTER_HD:]))
    body = f"""
{page_title_block(base, trail, "Nos réalisations",
    "Des interventions réelles, réalisées chez nos clients particuliers et professionnels. "
    "Faites glisser le curseur pour comparer l'avant et l'après.")}

<section class="section">
  <div class="container">
    <div class="grid grid-2">{ba}</div>
    <h2 style="margin:56px 0 26px">Nos autres chantiers</h2>
    <div class="grid grid-3">{ba_petit}</div>
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
    <h2>Ce que montrent — et ne montrent pas — ces photos</h2>
    <p>
      Toutes ces images viennent de chantiers réels, chez des clients particuliers et professionnels.
      L'avant et l'après sont pris <strong>au même endroit, sous la même lumière</strong>, à quelques
      heures d'intervalle. Nous n'associons jamais deux photos qui ne proviennent pas de la même
      intervention&nbsp;: ce serait montrer un résultat qui n'a pas eu lieu.
    </p>
    <p>
      Il faut aussi dire ce qu'un nettoyage ne fait pas. Une fibre brûlée, un cuir craquelé, une pierre
      rongée par le gel ou un vernis parti ne reviennent pas&nbsp;: le nettoyage retire ce qui s'est
      déposé, il ne reconstitue pas ce qui a disparu. Quand nous voyons ce type de dégât sur vos photos,
      nous vous le disons au devis, avant l'intervention, plutôt que de vous laisser l'espérer.
    </p>

    <h2>Les méthodes employées sur ces chantiers</h2>
    <ul class="checklist">
      <li><strong>Injection-extraction</strong> pour les textiles&nbsp;: on injecte une solution dans la
        fibre puis on l'aspire immédiatement avec la saleté dissoute. Pas d'auréole, parce qu'il ne
        reste pas d'eau stagnante. Voir le
        <a href="guides/injection-extraction.html">guide dédié</a>.</li>
      <li><strong>Vapeur à haute température</strong> pour les surfaces dures et les recoins&nbsp;:
        elle décolle le gras sans détergent agressif.</li>
      <li><strong>Haute pression réglée selon le support</strong> pour les extérieurs&nbsp;: le réglage
        change du tout au tout entre une dalle béton et une pierre tendre.</li>
      <li><strong>Eau osmosée</strong> pour les vitres&nbsp;: privée de ses minéraux, elle sèche sans
        rien déposer. Voir <a href="guides/eau-osmosee-vitres.html">pourquoi ça marche</a>.</li>
    </ul>
    <p>
      Le détail par prestation figure sur <a href="services.html">nos pages de prestations</a>, avec
      ce qui est inclus et les tarifs correspondants.
    </p>
  </div>
</section>

{reviews_section(base, soft=False)}

{cta_band(base)}
"""
    html = (head(titre_page("Nos réalisations de nettoyage — avant / après"),
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
  <h2><a href="zones/{z['slug']}.html">{z['name']} ({z['num']})</a></h2>
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
    html = (head(titre_page("Zones d'intervention en Île-de-France"),
                 "MathClean intervient dans les huit départements d'Île-de-France : Paris 75, "
                 "92, 93, 94, 91, 78, 77 et 95. Devis gratuit, déplacement annoncé d'avance.",
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
      <a class="btn btn-outline" href="{base}services.html">Voir les {NB_SERVICES} prestations</a>
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
    html = (head(titre_page("Entreprise de nettoyage en %s (%s)" % (z["name"], z["num"])),
                 "Nettoyage automobile, textile, terrasse, vitres et entreprise en %s (%s). "
                 "Intervention à domicile 7j/7, devis gratuit, sans acompte." % (z["name"], z["num"]),
                 "zones/%s.html" % z["slug"], base, schema=schema)
            + header(base, "zones") + body + footer(base))
    return write("zones/%s.html" % z["slug"], html)


# ===========================================================================
# BLOG
# ===========================================================================
def post_card(base, p, niveau="h3"):
    """Carte d'article. `niveau` suit la hiérarchie de la page qui l'accueille."""
    return f"""<article class="post-card reveal">
  <a class="post-thumb" href="{base}blog/{p['slug']}.html" tabindex="-1" aria-hidden="true">
    <img src="{base}assets/photos/{p['image']}" alt="{p['title']} — conseil de nettoyage MathClean"
         loading="lazy" width="640" height="360">
  </a>
  <div class="post-body">
    <div class="post-meta">
      <span class="post-cat">{p['cat']}</span>
      <time datetime="{p['date']}">{p['date_fr']}</time>
    </div>
    <{niveau}><a href="{base}blog/{p['slug']}.html">{p['title']}</a></{niveau}>
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
        f'<li><a href="{base}blog.html#cat-{slug_ancre(c)}">{c}<span>{n}</span></a></li>'
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
    # Regroupement par catégorie : chaque rubrique porte l'ancre visée par la
    # colonne latérale, et introduit un h2 qui manquait entre le h1 et les cartes.
    cats = []
    for p in POSTS:
        if p["cat"] not in cats:
            cats.append(p["cat"])
    cards = ""
    for c in sorted(cats):
        dedans = [p for p in POSTS if p["cat"] == c]
        cards += (
            '<section class="cat-block" id="cat-%s">\n<h2 class="cat-title">%s</h2>\n'
            '<div class="grid grid-2">%s</div>\n</section>\n'
            % (slug_ancre(c), c, "".join(post_card(base, p) for p in dedans))
        )
    body = f"""
{page_title_block(base, trail, "Conseils &amp; astuces de nettoyage",
    "Un bon entretien au quotidien prolonge la vie de vos biens et espace les nettoyages en profondeur. "
    "Voici nos méthodes de professionnels — y compris les erreurs qui coûtent cher.")}

<section class="section">
  <div class="container blog-layout">
    <div>
      {cards}
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
    html = (head(titre_page("Conseils et astuces de nettoyage"),
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
         "author": auteur_schema(),
         "publisher": editeur_schema(),
         "isPartOf": {"@type": "WebSite", "@id": SITE["url"] + "/#site"},
         "mainEntityOfPage": "%s/blog/%s.html" % (SITE["url"], p["slug"])},
    ]
    html = (head(titre_page(p["title"]), p["meta"], "blog/%s.html" % p["slug"], base,
                 image="assets/photos/%s" % p["image"], schema=schema,
                 og_type="article", published=p["date"])
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
          <a href="services/nettoyage-entreprise-paris.html">bureaux, commerces et locaux d'activité</a> en
          passage régulier ou ponctuel, prenons en charge la
          <a href="services/nettoyage-fin-de-chantier-paris.html">remise en état après travaux</a> pour
          les artisans et les agences, et intervenons sur des
          <a href="services/nettoyage-bateau-paris.html">bateaux à quai</a>, sur la Seine
          comme en port de plaisance.
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

{reviews_section(base, soft=False)}

{cta_band(base)}
"""
    schema = [crumb_schema([("À propos", "a-propos.html")]),
              {"@context": "https://schema.org", "@type": "AboutPage",
               "name": "À propos de MathClean", "url": SITE["url"] + "/a-propos.html",
               "mainEntity": {"@id": SITE["url"] + "/#business"}}]
    html = (head(titre_page("À propos de MathClean, entreprise de nettoyage"),
                 "MathClean, entreprise installée à Tremblay-en-France : notre méthode, nos "
                 "engagements et le terrain que nous couvrons en Île-de-France.",
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

<section class="section section-soft">
  <div class="container container-narrow">
    <h2>Ce qui nous aide à chiffrer juste du premier coup</h2>
    <p>
      Un devis ferme suppose que nous ayons vu le travail. Trois informations suffisent presque
      toujours à éviter un aller-retour&nbsp;:
    </p>
    <ul class="checklist">
      <li><strong>Deux ou trois photos</strong>, dont une de près sur la zone gênante. C'est ce qui
        nous renseigne le mieux&nbsp;: la matière, l'ancienneté de la tache, l'état général.</li>
      <li><strong>La matière</strong> quand vous la connaissez&nbsp;: tissu, microfibre, alcantara,
        cuir, laine, synthétique. Elle change la méthode, donc le temps, donc le prix.</li>
      <li><strong>L'accès</strong>&nbsp;: étage, ascenseur, place de stationnement, code d'entrée.
        Nous venons avec du matériel, pas seulement avec un chiffon.</li>
    </ul>

    <h2>Ce que contient notre devis</h2>
    <p>
      Un montant unique et une ligne vague ne vous permettent pas de comparer. Le nôtre détaille
      <strong>poste par poste</strong>&nbsp;: chaque prestation, sa durée estimée, son prix, et les
      frais de déplacement calculés depuis {SITE['city']} — {SITE['travel_fee']}. Le total affiché est
      celui que vous réglerez&nbsp;: pas de supplément découvert sur place, pas d'acompte demandé
      à la signature.
    </p>
    <p>
      Si nous estimons qu'une intervention ne donnera pas le résultat que vous espérez — une fibre
      déjà abîmée, un support attaqué — nous vous le disons dans le devis. Un refus argumenté vaut
      mieux qu'une prestation décevante.
    </p>
    <p>
      Avant de signer chez nous ou ailleurs, notre guide
      <a href="guides/devis-nettoyage-questions-a-poser.html">les 7 questions à poser avant de signer</a>
      liste ce qu'un devis sérieux doit contenir.
    </p>

    <h2>Délais de réponse et d'intervention</h2>
    <p>
      Nous répondons <strong>sous 24 heures</strong>, week-ends compris. L'intervention suit
      généralement sous 24 à 72 heures selon votre département&nbsp;: le plus court en
      Seine-Saint-Denis et dans le Val-d'Oise, où se trouve notre atelier, un peu plus long dans
      les Yvelines et en Seine-et-Marne. Pour un besoin urgent, l'appel au
      <a href="tel:{SITE['phone_link']}">{SITE['phone']}</a> reste plus rapide que le formulaire.
    </p>
  </div>
</section>
"""
    html = (head(titre_page("Devis gratuit de nettoyage à Paris et en IDF"),
                 "Devis gratuit et sans engagement pour un nettoyage auto, textile, terrasse, "
                 "vitres ou entreprise à Paris et en Île-de-France. Réponse sous 24 h.",
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
          <a class="btn btn-outline" href="{SITE['review_url']}" target="_blank" rel="noopener">{icon('star')}Laisser un avis</a>
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

{find_us(base)}

<section class="section">
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
    html = (head(titre_page("Contacter MathClean — nettoyage en Île-de-France"),
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
    html = (head(titre_page(title_tag), meta, slug, base, robots=robots,
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
    html = (head(titre_page("Merci, votre demande a bien été envoyée"),
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
    html = (head(titre_page("Page introuvable"),
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
# AVIS GOOGLE
# ===========================================================================
def stars(n=5):
    """Cinq étoiles pleines jusqu'à n."""
    out = ""
    for i in range(1, 6):
        cls = "star-on" if i <= n else "star-off"
        out += '<span class="%s">%s</span>' % (cls, icon("star"))
    return '<span class="stars" role="img" aria-label="%d étoiles sur 5">%s</span>' % (n, out)


def reviews_section(base, soft=True):
    """
    Bloc « avis clients ».

    Les avis affichés proviennent exclusivement de `REVIEWS` dans content.py,
    que le client remplit avec ses vrais avis Google. Tant que la liste est
    vide, on n'affiche que la note globale et le lien vers la fiche : aucun
    témoignage n'est inventé.
    """
    note = GOOGLE_NOTE
    cards = ""
    for auteur, date, score, texte in REVIEWS:
        initiale = auteur.strip()[:1].upper() or "?"
        cards += f"""<figure class="review reveal">
  <div class="review-head">
    <span class="review-avatar" aria-hidden="true">{initiale}</span>
    <div>
      <figcaption class="review-author">{auteur}</figcaption>
      <span class="review-date">{date}</span>
    </div>
    <span class="review-source" title="Avis publié sur Google">G</span>
  </div>
  {stars(score)}
  <blockquote><p>{texte}</p></blockquote>
</figure>"""

    if cards:
        corps = f'<div class="grid grid-3" style="margin-top:34px">{cards}</div>'
        pied = ""
    else:
        corps = ""
        pied = f"""<div class="notice notice-blue" style="margin-top:28px">
  {icon('info')}
  <p>
    Nous ne publions aucun avis rédigé par nos soins. Nos retours clients sont
    consultables dans leur intégralité sur notre fiche Google, avec le nom et
    la date de chacun.
  </p>
</div>"""

    return f"""<section class="section{' section-soft' if soft else ''}">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Ils nous font confiance</span>
      <h2>Nos avis Google</h2>
      <p class="lead">
        Tous nos avis sont publics et vérifiés sur Google : aucun témoignage
        n'est reproduit ici sans sa source.
      </p>
    </div>

    <div class="rating-card reveal">
      <div class="rating-score">
        <strong>{note['score']}</strong>
        {stars(5)}
        <span>{note['nombre']} avis Google</span>
      </div>
      <p>
        Chaque prestation est notée par le client lui-même, directement sur notre
        fiche Google — sans filtre et sans intermédiaire.
      </p>
      <div class="btn-row">
        <a class="btn" href="{SITE['review_url']}" target="_blank" rel="noopener">
          {icon('star')}Lire &amp; laisser un avis
        </a>
        <a class="btn btn-outline" href="{SITE['maps_url']}" target="_blank" rel="noopener">
          {icon('pin')}Voir la fiche Google
        </a>
      </div>
    </div>
    {corps}
    {pied}
  </div>
</section>"""


def find_us(base):
    """Bloc « nous trouver » : itinéraire et avis Google."""
    return f"""<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Nous trouver</span>
      <h2>Venir à l'atelier, ou nous laisser un avis</h2>
      <p class="lead">
        Nous nous déplaçons chez vous dans toute l'Île-de-France. L'atelier se
        situe à {SITE['city']} ({SITE['postcode']}).
      </p>
    </div>
    <div class="find-grid">
      <div class="find-card reveal">
        <span class="feature-icon">{icon('pin')}</span>
        <h3>Itinéraire</h3>
        <p>{SITE['address']}, {SITE['postcode']} {SITE['city']}</p>
        <a class="btn btn-block" href="{SITE['maps_url']}" target="_blank" rel="noopener">
          Ouvrir dans Google Maps
        </a>
      </div>
      <div class="find-card reveal">
        <span class="feature-icon">{icon('star')}</span>
        <h3>Laisser un avis</h3>
        <p>Votre retour sur Google aide énormément — et rassure les prochains clients.</p>
        <a class="btn btn-gold btn-block" href="{SITE['review_url']}" target="_blank" rel="noopener">
          Noter MathClean sur Google
        </a>
      </div>
      <div class="find-card reveal">
        <span class="feature-icon">{icon('phone')}</span>
        <h3>Nous appeler</h3>
        <p>{SITE['hours']} — vous parlez directement à la personne qui interviendra.</p>
        <a class="btn btn-outline btn-block" href="tel:{SITE['phone_link']}">{SITE['phone']}</a>
      </div>
    </div>
  </div>
</section>"""


# ===========================================================================
# RÉSERVATION EN LIGNE
# ===========================================================================
def build_reservation():
    base = ""
    trail = [("Réserver", None)]

    # Données de tarification transmises au script du configurateur.
    data = {
        "packs": [{"nom": n, "min": lo, "max": hi, "portee": sc, "desc": d, "lignes": li}
                  for n, lo, hi, sc, d, _f, li in PACKS_AUTO],
        "options": [{"nom": n, "prix": p, "desc": d} for n, p, d in OPTIONS_AUTO],
        "textile": [{"nom": n, "prix": p, "desc": d} for n, p, d in TARIFS_TEXTILE],
        "services": [{"slug": s["slug"], "nav": s["nav"], "prix": s["price"],
                      "univers": ("auto" if s["slug"].startswith("nettoyage-automobile")
                                  else "textile" if s["slug"].startswith("nettoyage-textile")
                                  else "devis")}
                     for s in SERVICES],
        "deplacement": DEPLACEMENT,
        "creneaux": CRENEAUX,
    }
    data_json = json.dumps(data, ensure_ascii=False)

    cartes = ""
    for s in SERVICES:
        cartes += f"""<label class="pick">
  <input type="radio" name="univers" value="{s['slug']}">
  <span class="pick-body">
    <span class="pick-icon">{icon(s['icon'])}</span>
    <span class="pick-name">{s['nav']}</span>
    <span class="pick-price">{s['price']}</span>
  </span>
</label>"""

    body = f"""
{page_title_block(base, trail, "Réserver votre intervention",
    "Composez votre prestation en quatre étapes : vous voyez le prix se construire au fur et "
    "à mesure, frais de déplacement compris. Aucun acompte — vous réglez après l'intervention.")}

<section class="section">
  <div class="container resa-layout">
    <noscript>
      <div class="notice">
        {icon('info')}
        <p>
          Le configurateur de réservation a besoin de JavaScript. Vous pouvez tout aussi bien
          <a href="devis.html">remplir le formulaire de devis</a> ou nous appeler au
          <a href="tel:{SITE['phone_link']}">{SITE['phone']}</a> — c'est souvent plus rapide.
        </p>
      </div>
    </noscript>

    <div class="resa" id="resa" hidden>
      <ol class="resa-steps" id="resa-steps">
        <li class="is-on"><span>1</span>Prestation</li>
        <li><span>2</span>Détail</li>
        <li><span>3</span>Lieu &amp; date</li>
        <li><span>4</span>Coordonnées</li>
      </ol>

      <form id="resa-form" action="{SITE['form_action']}" method="POST">
        <input type="hidden" name="_subject" value="Nouvelle réservation — MathClean">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_next" value="{SITE['url']}/merci.html">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="Récapitulatif" id="resa-recap">
        <input type="hidden" name="Total estimé" id="resa-total-field">

        <!-- Étape 1 -->
        <fieldset class="resa-panel is-on" data-step="1">
          <legend class="resa-legend">Que souhaitez-vous faire nettoyer ?</legend>
          <div class="pick-grid">{cartes}</div>
        </fieldset>

        <!-- Étape 2 -->
        <fieldset class="resa-panel" data-step="2">
          <legend class="resa-legend">Précisez votre besoin</legend>
          <div id="resa-detail"></div>
        </fieldset>

        <!-- Étape 3 -->
        <fieldset class="resa-panel" data-step="3">
          <legend class="resa-legend">Où et quand intervenons-nous ?</legend>
          <div class="form-grid">
            <div class="field field-full">
              <label for="r-adr">Adresse d'intervention <span class="req">*</span></label>
              <input id="r-adr" name="Adresse" type="text" autocomplete="street-address"
                     placeholder="12 rue de la Paix">
            </div>
            <div class="field">
              <label for="r-cp">Code postal <span class="req">*</span></label>
              <input id="r-cp" name="Code postal" type="text" inputmode="numeric"
                     autocomplete="postal-code" placeholder="75002">
            </div>
            <div class="field">
              <label for="r-ville">Ville <span class="req">*</span></label>
              <input id="r-ville" name="Ville" type="text" autocomplete="address-level2"
                     placeholder="Paris">
            </div>
            <div class="field field-full">
              <div class="notice notice-blue" id="r-dep-box">
                {icon('truck')}
                <p id="r-dep">Renseignez votre adresse pour connaître les frais de déplacement.</p>
              </div>
            </div>
            <div class="field">
              <label for="r-date">Date souhaitée <span class="req">*</span></label>
              <input id="r-date" name="Date souhaitée" type="date">
            </div>
            <div class="field">
              <label for="r-creneau">Créneau <span class="req">*</span></label>
              <select id="r-creneau" name="Créneau"></select>
            </div>
            <div class="field field-full">
              <span class="field-hint">
                La date est une préférence : nous vous la confirmons par téléphone ou par e-mail.
                Délais habituels — 24 à 48 h à Paris et en petite couronne, 48 à 72 h en grande couronne.
              </span>
            </div>
          </div>
        </fieldset>

        <!-- Étape 4 -->
        <fieldset class="resa-panel" data-step="4">
          <legend class="resa-legend">Vos coordonnées</legend>
          <div class="form-grid">
            <div class="field">
              <label for="r-nom">Nom et prénom <span class="req">*</span></label>
              <input id="r-nom" name="Nom" type="text" autocomplete="name">
            </div>
            <div class="field">
              <label for="r-tel">Téléphone <span class="req">*</span></label>
              <input id="r-tel" name="Téléphone" type="tel" autocomplete="tel">
            </div>
            <div class="field field-full">
              <label for="r-mail">E-mail <span class="req">*</span></label>
              <input id="r-mail" name="Email" type="email" autocomplete="email">
            </div>
            <div class="field">
              <label for="r-type">Vous êtes</label>
              <select id="r-type" name="Type de client">
                <option value="Particulier">Un particulier</option>
                <option value="Professionnel">Un professionnel / une entreprise</option>
              </select>
            </div>
            <div class="field">
              <label for="r-acces">Accès sur place</label>
              <input id="r-acces" name="Accès" type="text" placeholder="Étage, parking, digicode…">
            </div>
            <div class="field field-full">
              <label for="r-msg">Précisions utiles</label>
              <textarea id="r-msg" name="Message" style="min-height:110px"
                        placeholder="Nature des taches, matière, contraintes d'horaires…"></textarea>
            </div>
            <div class="field field-full">
              <label class="consent">
                <input type="checkbox" id="r-ok" name="Consentement" value="oui">
                <span>
                  J'accepte d'être recontacté au sujet de cette réservation
                  (<a href="politique-confidentialite.html">politique de confidentialité</a>).
                </span>
              </label>
            </div>
          </div>
        </fieldset>

        <div class="resa-error" id="resa-error" role="alert" hidden></div>

        <div class="resa-nav">
          <button class="btn btn-outline" type="button" id="resa-prev" hidden>Précédent</button>
          <button class="btn" type="button" id="resa-next">Continuer</button>
          <button class="btn btn-gold" type="submit" id="resa-send" hidden>Confirmer ma réservation</button>
        </div>
      </form>
    </div>

    <aside class="resa-ticket" id="resa-ticket" hidden>
      <h2>Votre réservation</h2>
      <ul id="resa-lines"><li class="resa-empty">Rien de sélectionné pour l'instant.</li></ul>
      <div class="resa-total">
        <span>Total estimé</span>
        <strong id="resa-total">—</strong>
      </div>
      <p class="field-hint" id="resa-note">
        Prix indicatif : la fourchette dépend du véhicule ou de la pièce. Le montant exact vous
        est confirmé avant l'intervention. Aucun acompte.
      </p>
    </aside>
  </div>
</section>

{find_us(base)}
"""
    schema = [crumb_schema([("Réserver", "reservation.html")])]
    html = (head(titre_page("Réserver un nettoyage en ligne à Paris"),
                 "Réservez votre intervention MathClean en ligne : choisissez la prestation, "
                 "voyez le prix se construire, frais de déplacement compris. Sans acompte, 7j/7.",
                 "reservation.html", base, schema=schema)
            + header(base, "reservation") + body
            + '<script id="resa-data" type="application/json">' + data_json + '</script>\n'
            + '<script src="assets/js/reservation.js?v=' + V_RESA + '" defer></script>\n'
            + footer(base))
    return write("reservation.html", html)


# ===========================================================================
# VILLES
# ===========================================================================
import math  # noqa: E402


def distance_atelier(lat, lon):
    """
    Distance routière approchée depuis l'atelier, en kilomètres.
    Vol d'oiseau majoré du même coefficient que le configurateur (1,25).
    """
    d = DEPLACEMENT
    r = math.pi / 180
    dla = (lat - d["lat"]) * r
    dlo = (lon - d["lon"]) * r
    a = (math.sin(dla / 2) ** 2
         + math.cos(d["lat"] * r) * math.cos(lat * r) * math.sin(dlo / 2) ** 2)
    km = 6371 * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) * d["coef_route"]
    return km


def frais_pour(km):
    d = DEPLACEMENT
    return int(math.ceil(km / d["palier_km"]) * d["palier_eur"]) if km > 0.4 else 0


def zone_de(dept):
    return next((z for z in ZONES if z["num"] == dept), ZONES[0])


def build_ville(v):
    slug, nom, cp, dept, lat, lon, angle, presta = v
    base = "../"
    z = zone_de(dept)
    km = distance_atelier(lat, lon)
    km_txt = ("moins d'un kilomètre" if km < 1
              else "environ %d km" % round(km))
    frais = frais_pour(km)
    frais_txt = ("aucun frais de déplacement" if frais == 0
                 else "environ %d € de frais de déplacement" % frais)
    frais_court = "Aucun" if frais == 0 else "~ %d €" % frais
    delai = ("24 à 48 h" if dept in ("75", "92", "93", "94") else "48 à 72 h")

    trail = [("Villes", "villes.html"), (nom, None)]
    # Trois vignettes exactement : la grille fait trois colonnes, une ligne
    # pleine se lit mieux qu'une rangée suivie d'une case orpheline.
    ordre = {sl: i for i, sl in enumerate(presta)}
    services = sorted((x for x in SERVICES if x["slug"] in presta),
                      key=lambda x: ordre[x["slug"]])[:3]
    tiles = "".join(service_tile(base, x) for x in services)
    autres = "".join(
        '<li><a href="%svilles/%s.html">%s</a></li>' % (base, o[0], o[1])
        for o in VILLES if o[3] == dept and o[0] != slug
    ) or '<li><a href="%szones/%s.html">Tout le département</a></li>' % (base, z["slug"])

    faq = [
        ("Intervenez-vous à %s sans supplément ?" % nom,
         "Nous intervenons à %s comme partout en Île-de-France. Depuis notre atelier de %s, "
         "comptez %s, soit %s. Le montant exact est calculé sur votre adresse précise dans le "
         "configurateur de réservation, et affiché avant que vous validiez."
         % (nom, SITE["city"], km_txt, frais_txt)),
        ("Quel est le délai d'intervention à %s ?" % nom,
         "Habituellement %s, 7j/7. Pour une urgence, appelez-nous au %s : nous réorganisons "
         "la tournée quand c'est possible." % (delai, SITE["phone"])),
        ("Faut-il fournir de l'eau ou de l'électricité ?",
         "Non. Nous venons entièrement autonomes, ce qui nous permet d'intervenir en parking "
         "souterrain, en pied d'immeuble ou en copropriété sans accès technique."),
    ]

    body = f"""
{page_title_block(base, trail, "Entreprise de nettoyage à %s (%s)" % (nom, cp),
   "Nettoyage à domicile et en entreprise à %s : automobile, textile, terrasse, vitres, "
   "locaux et fin de chantier. Devis gratuit, intervention 7j/7." % nom)}

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">MathClean à {nom}</span>
        <h2>Ce que nous faisons le plus à {nom}</h2>
        <p>{angle}</p>
        <p>
          {nom} dépend du département <a href="{base}zones/{z['slug']}.html">{z['name']} ({dept})</a>.
          Depuis notre atelier de {SITE['city']}, comptez <strong>{km_txt}</strong> —
          soit {frais_txt} — et un délai habituel de <strong>{delai}</strong>.
        </p>
        <div class="btn-row" style="margin-top:1.5rem">
          <a class="btn" href="{base}reservation.html">Réserver à {nom}</a>
          <a class="btn btn-outline" href="tel:{SITE['phone_link']}">{icon('phone')}{SITE['phone']}</a>
        </div>
      </div>
      <div class="reveal">
        <div class="table-wrap">
          <table class="price-table">
            <caption>En pratique à {nom}</caption>
            <tbody>
              <tr><th scope="row">Code postal</th><td class="amount">{cp}</td></tr>
              <tr><th scope="row">Département</th><td class="amount">{z['name']} ({dept})</td></tr>
              <tr><th scope="row">Distance depuis l'atelier</th><td class="amount">{km_txt}</td></tr>
              <tr><th scope="row">Frais de déplacement</th><td class="amount">{frais_court}</td></tr>
              <tr><th scope="row">Délai habituel</th><td class="amount">{delai}</td></tr>
              <tr><th scope="row">Acompte</th><td class="amount">Aucun</td></tr>
            </tbody>
          </table>
        </div>
        <p class="field-hint" style="margin-top:12px">
          Distance calculée depuis le centre de la commune : le montant exact dépend de votre
          adresse et vous est confirmé avant validation.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Nos prestations</span>
      <h2>Ce que nous proposons à {nom}</h2>
    </div>
    <div class="tile-grid">{tiles}</div>
    <div class="btn-row center" style="margin-top:34px">
      <a class="btn btn-outline" href="{base}services.html">Voir les {NB_SERVICES} prestations</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container-narrow">
    <div class="section-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>Nettoyage à {nom} : vos questions</h2>
    </div>
    {faq_block(faq, 'faq-ville')}
  </div>
</section>

{cta_band(base, "Un besoin à %s ?" % nom,
          "Devis gratuit et sans engagement, réponse sous 24 h. Aucun acompte à verser.")}

<section class="section section-soft">
  <div class="container container-narrow">
    <div class="section-head center">
      <span class="eyebrow">À proximité</span>
      <h2>Autres villes du {z['num']}</h2>
    </div>
    <ul class="city-list">{autres}</ul>
    <div class="btn-row center" style="margin-top:26px">
      <a class="btn btn-outline" href="{base}villes.html">Toutes les villes couvertes</a>
    </div>
  </div>
</section>
"""
    schema = [
        crumb_schema([("Villes", "villes.html"), (nom, "villes/%s.html" % slug)]),
        {"@context": "https://schema.org", "@type": "Service",
         "name": "Entreprise de nettoyage à %s" % nom,
         "provider": {"@id": SITE["url"] + "/#business"},
         "areaServed": {"@type": "City", "name": nom,
                        "address": {"@type": "PostalAddress", "postalCode": cp,
                                    "addressLocality": nom, "addressCountry": "FR"}},
         "url": "%s/villes/%s.html" % (SITE["url"], slug)},
        faq_schema(faq),
    ]
    html = (head(titre_page("Nettoyage à %s (%s) — devis gratuit" % (nom, cp)),
                 "Nettoyage à domicile et en entreprise à %s (%s) : auto, textile, "
                 "terrasse, vitres, locaux. Intervention 7j/7, sans acompte." % (nom, cp),
                 "villes/%s.html" % slug, base, schema=schema)
            + header(base, "zones") + body + footer(base))
    return write("villes/%s.html" % slug, html)


def build_villes_archive():
    base = ""
    trail = [("Villes", None)]
    par_dept = {}
    for v in VILLES:
        par_dept.setdefault(v[3], []).append(v)
    blocs = ""
    for z in ZONES:
        lst = par_dept.get(z["num"])
        if not lst:
            continue
        items = "".join(
            '<li><a href="villes/%s.html">%s <span>%s</span></a></li>' % (v[0], v[1], v[2])
            for v in sorted(lst, key=lambda x: x[1])
        )
        blocs += f"""<div class="widget reveal">
  <h2 class="widget-title"><a href="zones/{z['slug']}.html">{z['name']} ({z['num']})</a></h2>
  <ul class="widget-links">{items}</ul>
</div>"""
    body = f"""
{page_title_block(base, trail, "Les villes où nous intervenons",
  "Une page par commune, avec la distance depuis notre atelier de %s, les frais de "
  "déplacement correspondants et le délai habituel. Cette liste n'est pas exhaustive : "
  "nous couvrons les huit départements franciliens." % SITE['city'])}

<section class="section">
  <div class="container">
    <div class="grid grid-3">{blocs}</div>
  </div>
</section>

<section class="section section-soft">
  <div class="container container-narrow">
    <h2>Comment sont calculés les frais de déplacement</h2>
    <p>
      Nous partons de notre atelier de {SITE['city']} ({SITE['postcode'][:2]}) et facturons
      <strong>{SITE['travel_fee']}</strong>. Le compteur est arrondi par tranche entière&nbsp;: une
      commune à sept kilomètres et une commune à dix kilomètres relèvent du même palier. Le montant
      vous est annoncé <em>avant</em> que vous validiez quoi que ce soit, jamais découvert sur la facture.
    </p>
    <p>
      Chaque page de commune indique la distance réelle par la route, le montant correspondant et
      le délai d'intervention habituel. Ces distances sont calculées depuis l'atelier, puis majorées
      d'un coefficient routier&nbsp;: elles reflètent le trajet, pas la ligne droite.
    </p>

    <h2>Et si votre commune n'est pas dans la liste</h2>
    <p>
      Cette liste réunit les communes où nous intervenons le plus souvent&nbsp;; elle n'est pas
      limitative. Nous couvrons les {NB_ZONES} départements franciliens, y compris les communes
      rurales de Seine-et-Marne et du Val-d'Oise. Au-delà de l'Île-de-France, nous étudions au cas
      par cas&nbsp;: dites-nous où vous êtes, nous vous répondrons franchement si le déplacement
      n'a pas de sens.
    </p>
    <p>
      Pour les professionnels multi-sites, nous établissons un forfait unique plutôt qu'un
      déplacement par adresse&nbsp;: voir le
      <a href="services/nettoyage-entreprise-paris.html">nettoyage pour entreprise</a>.
    </p>
    <div class="notice notice-blue" style="margin-top:30px">
      {icon('info')}
      <p>
        <strong>Votre commune n'y figure pas ?</strong> Nous intervenons dans toute
        l'Île-de-France. Appelez le {SITE['phone']} ou utilisez
        <a href="reservation.html">le configurateur</a> : il calcule les frais de
        déplacement sur votre adresse exacte.
      </p>
    </div>
  </div>
</section>

{cta_band(base)}
"""
    html = (head(titre_page("Villes couvertes en Île-de-France"),
                 "Toutes les communes où MathClean intervient : Paris, Hauts-de-Seine, "
                 "Seine-Saint-Denis, Val-de-Marne, Essonne, Yvelines, Seine-et-Marne, Val-d'Oise.",
                 "villes.html", base, schema=[crumb_schema([("Villes", "villes.html")])])
            + header(base, "zones") + body + footer(base))
    return write("villes.html", html)


# ===========================================================================
# GUIDES
# ===========================================================================
def guide_card(base, g, niveau="h3"):
    """Carte de guide. `niveau` suit la hiérarchie de la page qui l'accueille."""
    return f"""<article class="post-card reveal">
  <a class="post-thumb" href="{base}guides/{g['slug']}.html" tabindex="-1" aria-hidden="true">
    <img src="{base}assets/photos/{g['image']}" alt="{g['h1']} — guide MathClean"
         loading="lazy" width="640" height="360">
  </a>
  <div class="post-body">
    <div class="post-meta"><span class="post-cat">{g['cat']}</span></div>
    <{niveau}><a href="{base}guides/{g['slug']}.html">{g['h1']}</a></{niveau}>
    <p>{g['lead']}</p>
    <span class="service-more">Lire le guide {icon('arrow')}</span>
  </div>
</article>"""


def build_guide(g):
    base = "../"
    trail = [("Guides", "guides.html"), (g["cat"], None)]
    service = next((s for s in SERVICES if s["slug"] == g["service"]), SERVICES[0])
    corps = ""
    for titre, paras in g["sections"]:
        corps += "<h2>%s</h2>" % titre + "".join("<p>%s</p>" % p for p in paras)
    autres = "".join(guide_card(base, o) for o in GUIDES if o["slug"] != g["slug"])[:0]
    proches = [o for o in GUIDES if o["cat"] == g["cat"] and o["slug"] != g["slug"]][:3]
    if len(proches) < 3:
        proches += [o for o in GUIDES if o["slug"] != g["slug"] and o not in proches][:3 - len(proches)]
    autres = "".join(guide_card(base, o) for o in proches)

    body = f"""
<section class="page-title">
  <div class="container">{breadcrumbs(base, trail)}</div>
</section>

<section class="section">
  <div class="container blog-layout">
    <article>
      <header class="entry-header">
        <div class="post-meta" style="margin-bottom:14px">
          <span class="post-cat">{g['cat']}</span>
          <span>Par {SITE['manager']} — {SITE['name']}</span>
          <time datetime="{g.get('date', DATE_GUIDES)}">{DATE_GUIDES_FR}</time>
        </div>
        <h1>{g['h1']}</h1>
        <p class="lead">{g['lead']}</p>
      </header>

      <figure><img src="{base}assets/photos/{g['image']}" alt="{g['h1']}" width="1000" height="600"></figure>

      <div class="entry-content">{corps}</div>

      <h2 style="margin-top:2.2em">Questions fréquentes</h2>
      {faq_block(g['faq'], 'faq-guide')}

      <div class="notice notice-blue" style="margin-top:34px">
        {icon('sparkle')}
        <p>
          <strong>Besoin d'un devis ?</strong> MathClean intervient à Paris et dans toute
          l'Île-de-France, 7j/7 et sans acompte. Découvrez notre
          <a href="{base}services/{service['slug']}.html">{service['nav'].lower()}</a>,
          <a href="{base}reservation.html">réservez en ligne</a> ou appelez le
          <a href="tel:{SITE['phone_link']}">{SITE['phone']}</a>.
        </p>
      </div>

      <footer class="entry-footer">
        <ul class="tag-list">
          <li><a href="{base}guides.html">{g['cat']}</a></li>
          <li><a href="{base}services/{service['slug']}.html">{service['nav']}</a></li>
          <li><a href="{base}villes.html">Île-de-France</a></li>
        </ul>
      </footer>
    </article>
    {sidebar(base)}
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">À lire aussi</span>
      <h2>Nos autres guides</h2>
    </div>
    <div class="grid grid-3">{autres}</div>
  </div>
</section>

{cta_band(base)}
"""
    schema = [
        crumb_schema([("Guides", "guides.html"), (g["h1"], "guides/%s.html" % g["slug"])]),
        {"@context": "https://schema.org", "@type": "Article",
         "headline": g["h1"], "description": g["lead"],
         "image": "%s/assets/photos/%s" % (SITE["url"], g["image"]),
         "datePublished": g.get("date", DATE_GUIDES),
         "dateModified": g.get("date", DATE_GUIDES),
         "inLanguage": "fr-FR",
         "author": auteur_schema(),
         "publisher": editeur_schema(),
         "isPartOf": {"@type": "WebSite", "@id": SITE["url"] + "/#site"},
         "mainEntityOfPage": "%s/guides/%s.html" % (SITE["url"], g["slug"])},
        faq_schema(g["faq"]),
    ]
    html = (head(titre_page(g["title"]), g["meta"], "guides/%s.html" % g["slug"], base,
                 image="assets/photos/%s" % g["image"], schema=schema,
                 og_type="article", published=g.get("date", DATE_GUIDES))
            + header(base, "guides") + body + footer(base))
    return write("guides/%s.html" % g["slug"], html)


def build_guides_archive():
    base = ""
    trail = [("Guides", None)]
    cats = []
    for g in GUIDES:
        if g["cat"] not in cats:
            cats.append(g["cat"])
    cards = ""
    for c in sorted(cats):
        dedans = [g for g in GUIDES if g["cat"] == c]
        cards += (
            '<section class="cat-block" id="cat-%s">\n<h2 class="cat-title">%s</h2>\n'
            '<div class="grid grid-2">%s</div>\n</section>\n'
            % (slug_ancre(c), c, "".join(guide_card(base, g) for g in dedans))
        )
    body = f"""
{page_title_block(base, trail, "Guides pratiques du nettoyage",
  "Comment choisir un prestataire, ce que coûte réellement une prestation, comment "
  "fonctionne l'injection-extraction : nos réponses détaillées aux questions qu'on nous "
  "pose le plus.")}

<section class="section">
  <div class="container blog-layout">
    <div>{cards}</div>
    {sidebar(base)}
  </div>
</section>

{cta_band(base)}
"""
    html = (head(titre_page("Guides pratiques du nettoyage"),
                 "Guides MathClean : choisir une entreprise de nettoyage, prix d'un canapé ou "
                 "d'un detailing auto, injection-extraction, eau osmosée, entretien de bureaux.",
                 "guides.html", base, schema=[crumb_schema([("Guides", "guides.html")])])
            + header(base, "guides") + body + footer(base))
    return write("guides.html", html)


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
    """
    Accès ouvert à tous les robots, y compris ceux des assistants IA, qu'on
    nomme explicitement pour lever toute ambiguïté d'interprétation.
    """
    ia = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User",
          "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended",
          "CCBot", "Bytespider", "meta-externalagent"]
    lignes = ["User-agent: *", "Allow: /", ""]
    for bot in ia:
        lignes += ["User-agent: %s" % bot, "Allow: /", ""]
    lignes += ["Sitemap: %s/sitemap.xml" % SITE["url"], ""]
    return write("robots.txt", "\n".join(lignes))


def build_llms_txt():
    """
    Fiche de synthèse destinée aux robots des assistants IA. Convention
    /llms.txt : un résumé factuel, court et structuré, plus lisible pour un
    modèle que le HTML d'un site entier. Tout ce qu'il contient est vérifiable
    sur le site.
    """
    presta = "\n".join(
        "- %s (%s) : %s %s/services/%s.html"
        % (s["name"], s["price"], s["excerpt"].split(".")[0].strip(), SITE["url"], s["slug"])
        for s in SERVICES
    )
    guides = "\n".join(
        "- %s : %s/guides/%s.html" % (g["h1"], SITE["url"], g["slug"]) for g in GUIDES
    )
    zones = ", ".join("%s (%s)" % (z["name"], z["num"]) for z in ZONES)
    villes = ", ".join(v[1] for v in VILLES)
    txt = f"""# MathClean

> Entreprise de nettoyage à domicile et en entreprise, à Paris et dans les huit
> départements d'Île-de-France. Entreprise individuelle dirigée par {SITE['manager']},
> basée à {SITE['city']} ({SITE['postcode']}).

## Identité
- Nom : {SITE['name']}
- SIRET : {SITE['siret']}
- Adresse : {SITE['address']}, {SITE['postcode']} {SITE['city']}, France
- Téléphone : {SITE['phone']}
- E-mail : {SITE['email']}
- Horaires : {SITE['hours']}
- Site : {SITE['url']}
- Fiche Google : {SITE['review_url']}

## Engagements vérifiables
- Devis gratuit, ferme et détaillé poste par poste.
- Aucun acompte : le règlement se fait après l'intervention, une fois le résultat constaté.
- Frais de déplacement : {SITE['travel_fee']}, annoncés avant validation.
- Intervention 7j/7, y compris week-ends et jours fériés ; horaires décalés pour les commerces.
- Matériel, produits, eau et électricité fournis : aucun accès technique requis sur place.
- TVA non applicable, article 293 B du Code général des impôts.

## Prestations
{presta}

## Tarifs de référence
- Detailing automobile : 4 formules, de 40 € à 240 € selon le véhicule.
- Textile : chaise 15 €, fauteuil 25 €, canapé 2 places 39 €, 3 places 49 €, angle 69 €,
  matelas 1 place 39 €, 2 places 49 €, tapis 39 € à 59 €.
- Bateau, terrasse, vitres, entreprise, fin de chantier : sur devis après échange ou visite.
- Grille complète : {SITE['url']}/tarifs.html

## Zone d'intervention
Départements : {zones}.
Villes documentées : {villes}.

## Guides de référence
{guides}

## Réserver
- Configurateur en ligne : {SITE['url']}/reservation.html
- Devis : {SITE['url']}/devis.html
- Téléphone : {SITE['phone']}
"""
    return write("llms.txt", txt)


def build_redirects():
    """
    Redirections 301, lues par Cloudflare Pages et par Workers static assets.
    La prestation « locaux » a été renommée « entreprise » : l'ancienne adresse,
    déjà indexée, doit continuer de fonctionner.
    """
    lignes = [
        # Prestations renommées ou retirées
        "/services/nettoyage-locaux-paris.html       /services/nettoyage-entreprise-paris.html  301",
        "/services/nettoyage-bureau-paris.html       /services/nettoyage-entreprise-paris.html  301",
        "/services/nettoyage-avion-paris.html        /services.html                             301",
        # L'ancien site relayait déjà ces adresses ; on garde la chaîne intacte
        "/services/polissage-carrosserie-paris.html  /services/nettoyage-automobile-paris.html  301",
        "/services/nettoyage-canape-paris.html       /services/nettoyage-textile-paris.html     301",
        "/services/nettoyage-matelas-paris.html      /services/nettoyage-textile-paris.html     301",
        "/services/nettoyage-tapis-paris.html        /services/nettoyage-textile-paris.html     301",
        # La page « astuces » est devenue le blog
        "/astuces-nettoyage.html                     /blog.html                                 301",
    ]
    return write("_redirects", "\n".join(lignes) + "\n")


def clean_stale(kept):
    """
    Supprime les pages générées lors d'un build précédent qui ne le sont plus
    (une prestation retirée, par exemple). Sans cela, `site/` accumulerait des
    pages orphelines toujours en ligne.
    """
    kept = {os.path.normpath(k) for k in kept}
    removed = []
    for root, _dirs, files in os.walk(OUT):
        if os.path.join(OUT, "assets") in root:
            continue
        for f in files:
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(root, f), OUT)
            if os.path.normpath(rel) not in kept:
                os.remove(os.path.join(root, f))
                removed.append(rel)
    return removed


# ===========================================================================
# ORCHESTRATION
# ===========================================================================
def copy_theme_assets():
    for src, dst in (("theme/theme.css", "site/assets/css/theme.css"),
                     ("theme/theme.js", "site/assets/js/theme.js"),
                     ("theme/reservation.js", "site/assets/js/reservation.js")):
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
    pages.append((build_villes_archive(), "0.8", "monthly"))
    for v in VILLES:
        pages.append((build_ville(v), "0.7", "monthly"))
    pages.append((build_guides_archive(), "0.8", "monthly"))
    for g in GUIDES:
        pages.append((build_guide(g), "0.7", "monthly"))
    pages.append((build_blog_archive(), "0.7", "weekly"))
    for i, p in enumerate(POSTS):
        prev_post = POSTS[i - 1] if i > 0 else None
        next_post = POSTS[i + 1] if i < len(POSTS) - 1 else None
        pages.append((build_post(p, prev_post, next_post), "0.6", "yearly"))
    pages.append((build_apropos(), "0.8", "yearly"))
    pages.append((build_reservation(), "1.0", "monthly"))
    pages.append((build_devis(), "0.9", "monthly"))
    pages.append((build_contact(), "0.8", "yearly"))
    for path in build_legal():
        pages.append((path, "0.3", "yearly"))

    extra = [build_merci(), build_404()]   # noindex : hors sitemap

    build_sitemap(pages)
    build_robots()
    build_redirects()
    build_llms_txt()

    stale = clean_stale([p for p, _pr, _f in pages] + extra)

    print("Site généré dans %s" % OUT)
    print("%d pages indexables + merci.html, 404.html, sitemap.xml, robots.txt, _redirects"
          % len(pages))
    if stale:
        print("Pages obsolètes supprimées : %s" % ", ".join(stale))


if __name__ == "__main__":
    main()
