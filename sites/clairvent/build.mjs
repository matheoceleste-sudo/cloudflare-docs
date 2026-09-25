// Générateur statique du site Clairvent — `node build.mjs` produit le dossier dist/
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { services } from "./src/data/services.mjs";
import { guides1 } from "./src/data/guides1.mjs";
import { guides2 } from "./src/data/guides2.mjs";
import { sectors } from "./src/data/sectors.mjs";
import { base, depts, cities } from "./src/data/places.mjs";
import { sprite, ico, logo } from "./src/icons.mjs";

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const DIST = path.join(ROOT, "dist");

/* ------------------------------------------------------------------ */
/* Configuration — à adapter avant la mise en ligne                    */
/* ------------------------------------------------------------------ */
const SITE = {
  name: "Clairvent",
  tagline: "Hottes & cuisines professionnelles",
  url: "https://www.clairvent.fr",
  phone: "06 23 07 52 59",
  tel: "+33623075259",
  email: "matheoceleste@gmail.com",
  form: "https://formsubmit.co/matheoceleste@gmail.com",
  hours: "7j/7, de 8 h à 20 h",
  city: "Le Blanc-Mesnil",
  au: "au Blanc-Mesnil",
  du: "du Blanc-Mesnil",
  cp: "93150",
  street: "Rue Poussin",
  legal: "MathClean — entreprise individuelle de Mathéo Céleste",
  siret: "924 565 990 00010",
  updated: "2026-09-25",
  updatedLabel: "septembre 2026"
};

const guides = [...guides1, ...guides2];
const CATS = {
  reg: { name: "Réglementation", cls: "t-reg", icon: "doc" },
  feu: { name: "Sécurité incendie", cls: "t-feu", icon: "fire" },
  hyg: { name: "Hygiène & HACCP", cls: "t-hyg", icon: "shield" },
  ent: { name: "Entretien", cls: "t-ent", icon: "sparkle" },
  equ: { name: "Équipements", cls: "t-equ", icon: "fan" },
  par: { name: "Particuliers", cls: "t-par", icon: "home" },
  ges: { name: "Gestion & choix", cls: "t-ges", icon: "euro" }
};
const svcBySlug = Object.fromEntries(services.map((s) => [s.slug, s]));
const guideBySlug = Object.fromEntries(guides.map((g) => [g.slug, g]));
const deptByCode = Object.fromEntries(depts.map((d) => [d.code, d]));

/* ------------------------------------------------------------------ */
/* Utilitaires                                                          */
/* ------------------------------------------------------------------ */
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const strip = (h) => h.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
const words = (h) => strip(h).split(" ").length;
const km = (a, b) => {
  const R = 6371, r = Math.PI / 180;
  const dLat = (b.lat - a.lat) * r, dLon = (b.lon - a.lon) * r;
  const x = Math.sin(dLat / 2) ** 2 + Math.cos(a.lat * r) * Math.cos(b.lat * r) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(x));
};
const aV = (n) => (n.startsWith("Le ") ? "au " + n.slice(3) : n.startsWith("Les ") ? "aux " + n.slice(4) : "à " + n);
const deV = (n) => (n.startsWith("Le ") ? "du " + n.slice(3) : n.startsWith("Les ") ? "des " + n.slice(4) : "de " + n);
const hash = (s) => [...s].reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 7);
const pages = [];

function slugToHeadings(html) {
  const toc = [];
  const out = html.replace(/<h2>(.*?)<\/h2>/g, (m, t) => {
    const id = strip(t).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
    toc.push([id, strip(t)]);
    return `<h2 id="${id}">${t}</h2>`;
  });
  return { html: out, toc };
}

/* ------------------------------------------------------------------ */
/* Gabarit commun                                                       */
/* ------------------------------------------------------------------ */
function layout(p) {
  const depth = p.path.split("/").length - 1;
  const r = "../".repeat(depth);
  const canonical = SITE.url + "/" + (p.path === "index.html" ? "" : p.path);
  const L = (x) => r + x;
  const active = (sec) => (p.section === sec ? ' aria-current="page"' : "");
  const hotte = services.filter((s) => s.group === "hotte");
  const cuisine = services.filter((s) => s.group === "cuisine");
  const crumbs = p.crumbs || [];
  const ld = [
    ...(p.jsonld || []),
    crumbs.length
      ? {
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          itemListElement: [["Accueil", ""], ...crumbs].map(([n, u], i) => ({
            "@type": "ListItem", position: i + 1, name: n, item: SITE.url + "/" + (u || "")
          }))
        }
      : null
  ].filter(Boolean);

  const breadcrumbHtml = crumbs.length
    ? `<nav class="breadcrumbs" aria-label="Fil d'Ariane"><a href="${L("index.html")}">Accueil</a>${crumbs
        .map(([n, u], i) => (i === crumbs.length - 1 ? `<span>›</span><span aria-current="page">${esc(n)}</span>` : `<span>›</span><a href="${L(u)}">${esc(n)}</a>`))
        .join("")}</nav>`
    : "";

  const pageTitle = p.hero === false ? "" : p.heroHtml || `
<section class="page-title">
  <div class="container">
    ${breadcrumbHtml}
    ${p.eyebrow ? `<span class="eyebrow">${p.eyebrow}</span>` : ""}
    <h1>${p.h1}</h1>
    ${p.lead ? `<p class="lead">${p.lead}</p>` : ""}
    ${p.meta || ""}
    ${p.heroCta ? `<div class="hero-cta">${p.heroCta.replace(/\{r\}/g, r)}</div>` : ""}
  </div>
</section>`;

  const html = `<!DOCTYPE html>
<html lang="fr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(p.title)}</title>
<meta name="description" content="${esc(p.desc)}">
<meta name="robots" content="${p.noindex ? "noindex,follow" : "index,follow,max-image-preview:large,max-snippet:-1"}">
<link rel="canonical" href="${canonical}">
<meta name="theme-color" content="#0e1c2b">
<meta property="og:type" content="${p.ogType || "website"}">
<meta property="og:site_name" content="${SITE.name}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="${esc(p.title)}">
<meta property="og:description" content="${esc(p.desc)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${SITE.url}/assets/img/og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="FR-IDF">
<meta name="geo.placename" content="${SITE.city}">
<link rel="icon" href="${L("assets/img/favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="${L("assets/css/style.css")}">
${ld.map((o) => `<script type="application/ld+json">${JSON.stringify(o)}</script>`).join("\n")}
</head>
<body class="${p.bodyClass || ""}">
${sprite}
<a class="skip-link" href="#content">Aller au contenu</a>
<div class="topbar">
  <div class="container">
    <div class="topbar-l">
      <span>${ico("phone")}<a href="tel:${SITE.tel}">${SITE.phone}</a></span>
      <span>${ico("clock")}Standard ${SITE.hours}</span>
    </div>
    <div class="topbar-r">
      <span>${ico("moon")}Interventions de nuit et hors service</span>
      <span>${ico("pin")}Basés ${SITE.au} (93) · Île-de-France</span>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="${L("index.html")}" aria-label="${SITE.name} — accueil">
      ${logo}
      <span><span class="brand-name">Clair<b>vent</b></span><span class="brand-tag">${SITE.tagline}</span></span>
    </a>
    <nav class="main-nav" id="site-nav" aria-label="Menu principal">
      <button class="nav-toggle nav-close" type="button" data-nav-close aria-label="Fermer le menu" style="display:none"></button>
      <ul>
        <li><a href="${L("index.html")}"${active("home")}>Accueil</a></li>
        <li class="has-sub"><a href="${L("prestations.html")}"${active("presta")}>Prestations ${ico("caret", "caret")}</a>
          <ul class="sub mega">
            ${hotte.map((s) => `<li><a href="${L("prestations/" + s.slug + ".html")}">${s.nav}</a></li>`).join("")}
            ${cuisine.map((s) => `<li><a href="${L("prestations/" + s.slug + ".html")}">${s.nav}</a></li>`).join("")}
            <li class="all"><a href="${L("prestations.html")}">Toutes nos prestations →</a></li>
          </ul>
        </li>
        <li class="has-sub"><a href="${L("secteurs.html")}"${active("secteurs")}>Secteurs ${ico("caret", "caret")}</a>
          <ul class="sub">
            ${sectors.map((s) => `<li><a href="${L("secteurs/" + s.slug + ".html")}">${s.name}</a></li>`).join("")}
          </ul>
        </li>
        <li class="has-sub"><a href="${L("notre-savoir-faire.html")}"${active("savoir")}>Savoir-faire ${ico("caret", "caret")}</a>
          <ul class="sub">
            <li><a href="${L("notre-savoir-faire.html")}">Équipe formée &amp; diplômée</a></li>
            <li><a href="${L("methode.html")}">Notre méthode en 8 étapes</a></li>
            <li><a href="${L("reglementation.html")}">Réglementation</a></li>
            <li><a href="${L("certificat-de-degraissage.html")}">Le certificat de dégraissage</a></li>
            <li><a href="${L("realisations.html")}">Réalisations</a></li>
            <li><a href="${L("diagnostic.html")}">Outil de diagnostic</a></li>
            <li><a href="${L("faq.html")}">Questions fréquentes</a></li>
          </ul>
        </li>
        <li class="has-sub"><a href="${L("conseils.html")}"${active("conseils")}>Conseils ${ico("caret", "caret")}</a>
          <ul class="sub">
            ${Object.entries(CATS).map(([k, c]) => `<li><a href="${L("conseils.html")}#${k}">${c.name}</a></li>`).join("")}
            <li class="all"><a href="${L("conseils.html")}">Tous les conseils →</a></li>
          </ul>
        </li>
        <li class="has-sub"><a href="${L("zones.html")}"${active("zones")}>Zones ${ico("caret", "caret")}</a>
          <ul class="sub">
            ${depts.map((d) => `<li><a href="${L("zones/" + d.slug + ".html")}">${d.name} (${d.code})</a></li>`).join("")}
            <li class="all"><a href="${L("ou-nous-trouver.html")}">Où nous trouver →</a></li>
          </ul>
        </li>
        <li><a href="${L("contact.html")}"${active("contact")}>Contact</a></li>
      </ul>
      <div class="nav-mobile-cta">
        <a class="btn" href="${L("reservation.html")}">${ico("calendar")}Réserver une intervention</a>
        <a class="btn btn-outline" href="${L("devis.html")}">Demander un devis gratuit</a>
        <a class="btn btn-dark" href="tel:${SITE.tel}">${ico("phone")}${SITE.phone}</a>
      </div>
    </nav>
    <div class="header-cta">
      <a class="btn btn-outline btn-sm" href="tel:${SITE.tel}" aria-label="Appeler le ${SITE.phone}">${ico("phone")}<span class="btn-phone-txt">${SITE.phone}</span></a>
      <a class="btn btn-sm btn-resa" href="${L("reservation.html")}">Réserver</a>
      <button class="nav-toggle" id="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="nav-backdrop" id="nav-backdrop"></div>
<main id="content">
${pageTitle}
${p.body.replace(/\{r\}/g, r)}
</main>
${footer(L)}
<div class="callbar"><a href="tel:${SITE.tel}">${ico("phone")}Appeler</a><a class="primary" href="${L("reservation.html")}">${ico("calendar")}Réserver</a></div>
<div class="fab">
  <div class="fab-panel" id="fab-panel">
    <h3>On vous rappelle gratuitement</h3>
    <p>Laissez votre numéro : un technicien vous rappelle dans la journée (${SITE.hours}).</p>
    <form class="form" action="${SITE.form}" method="POST">
      <input type="hidden" name="_subject" value="Demande de rappel — ${SITE.name}">
      <input type="hidden" name="_next" value="${SITE.url}/merci.html">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="Page" value="${esc(p.title)}">
      <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
      <div><label for="cb-nom">Nom</label><input id="cb-nom" type="text" name="Nom" required autocomplete="name"></div>
      <div><label for="cb-tel">Téléphone</label><input id="cb-tel" type="tel" name="Téléphone" required autocomplete="tel"></div>
      <button class="btn" type="submit">Être rappelé</button>
      <p class="form-note mb0">Ou appelez directement le <a href="tel:${SITE.tel}">${SITE.phone}</a>.</p>
    </form>
  </div>
  <button class="fab-btn" type="button" aria-expanded="false" aria-controls="fab-panel" aria-label="Être rappelé">${ico("phone")}</button>
</div>
<script src="${L("assets/js/site.js")}" defer></script>
${(p.scripts || []).map((s) => `<script src="${L(s)}" defer></script>`).join("\n")}
</body>
</html>`;
  pages.push({ path: p.path, html, noindex: !!p.noindex, priority: p.priority || 0.6 });
}

function footer(L) {
  const top = ["paris-11", "le-blanc-mesnil", "saint-denis", "boulogne-billancourt", "courbevoie", "montreuil", "creteil", "versailles", "argenteuil", "rungis", "roissy-en-france", "serris-val-d-europe", "massy", "nanterre", "paris-8", "aubervilliers"];
  return `<footer class="site-footer">
  <div class="container footer-top">
    <div>
      <a class="brand" href="${L("index.html")}">${logo}<span><span class="brand-name">Clair<b>vent</b></span><span class="brand-tag" style="color:#8ea1b4">${SITE.tagline}</span></span></a>
      <p>Spécialistes du nettoyage de hottes, de conduits d'extraction et de cuisines, pour les professionnels et les particuliers d'Île-de-France. Techniciens formés et diplômés, certificat remis à chaque intervention, prix sur devis.</p>
      <p><a class="btn btn-sm" href="${L("devis.html")}">Devis gratuit</a></p>
    </div>
    <div>
      <h4>Prestations</h4>
      <ul>${services.slice(0, 8).map((s) => `<li><a href="${L("prestations/" + s.slug + ".html")}">${s.nav}</a></li>`).join("")}<li><a href="${L("prestations.html")}"><strong>Toutes les prestations</strong></a></li></ul>
    </div>
    <div>
      <h4>Clairvent</h4>
      <ul>
        <li><a href="${L("notre-savoir-faire.html")}">Notre savoir-faire</a></li>
        <li><a href="${L("methode.html")}">Notre méthode</a></li>
        <li><a href="${L("reglementation.html")}">Réglementation</a></li>
        <li><a href="${L("certificat-de-degraissage.html")}">Certificat de dégraissage</a></li>
        <li><a href="${L("realisations.html")}">Réalisations</a></li>
        <li><a href="${L("conseils.html")}">Conseils &amp; guides</a></li>
        <li><a href="${L("faq.html")}">FAQ</a></li>
        <li><a href="${L("plan-du-site.html")}">Plan du site</a></li>
      </ul>
    </div>
    <div>
      <h4>Nous joindre</h4>
      <ul class="footer-contact">
        <li>${ico("phone")}<a href="tel:${SITE.tel}"><strong>${SITE.phone}</strong></a></li>
        <li>${ico("clock")}<span>Standard ${SITE.hours}<br>Interventions jour, nuit et week-end</span></li>
        <li>${ico("pin")}<span>${SITE.cp} ${SITE.city}<br><a href="${L("ou-nous-trouver.html")}">Où nous trouver</a></span></li>
        <li>${ico("calendar")}<a href="${L("reservation.html")}">Réserver en ligne</a></li>
        <li>${ico("mail")}<a href="${L("contact.html")}">Formulaire de contact</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-cities"><div class="container"><strong style="color:#c6d2de">Nettoyage de hotte :</strong> ${top.map((s) => { const c = cities.find((x) => x.slug === s); return `<a href="${L("villes/nettoyage-hotte-" + s + ".html")}">${c.name}</a>`; }).join("")}<a href="${L("zones.html")}">Toutes les villes →</a></div></div>
  <div class="footer-bottom"><div class="container"><span>© <span data-year>2026</span> ${SITE.name} — Tous droits réservés.</span><span><a href="${L("mentions-legales.html")}">Mentions légales</a> · <a href="${L("confidentialite.html")}">Confidentialité</a> · <a href="${L("plan-du-site.html")}">Plan du site</a></span></div></div>
</footer>`;
}

/* ------------------------------------------------------------------ */
/* Blocs réutilisables                                                  */
/* ------------------------------------------------------------------ */
const diagramParts = {
  hotte: ["La hotte", "Elle capte les fumées et les vapeurs grasses au-dessus des postes de cuisson. Nous dégraissons le caisson, les gouttières et les rampes, dedans comme dehors."],
  filtres: ["Les filtres à chicanes", "Première barrière contre la graisse. Nous les déposons, les faisons tremper dans un bain dégraissant chaud, puis les rinçons et contrôlons un par un."],
  plenum: ["Le plénum", "La chambre cachée derrière les filtres, souvent la zone la plus grasse de la hotte. Grattage puis dégraissage en mousse active."],
  conduit: ["Le conduit d'extraction", "La zone la plus dangereuse en cas de feu. Nous le dégraissons par les trappes de visite, avec brossage rotatif et photos à chaque ouverture."],
  tourelle: ["La tourelle d'extraction", "Le moteur de votre ventilation, en toiture. Consignation, dégraissage de la turbine, contrôle visuel de la courroie et remise en service."]
};
function diagram(light = false) {
  const stroke = light ? "#0e1c2b" : "#cfdae5";
  const wall = light ? "#e9edf2" : "rgba(255,255,255,.06)";
  return `<div class="diagram${light ? " diagram-light" : ""}" data-diagram>
<svg viewBox="0 0 520 420" role="img" aria-labelledby="dg-t"><title id="dg-t">Schéma d'un système d'extraction de cuisine professionnelle : hotte, filtres, plénum, conduit et tourelle</title>
<defs><linearGradient id="dg-duct" x1="0" x2="1"><stop offset="0" stop-color="#8fa3b7"/><stop offset=".5" stop-color="#c9d4df"/><stop offset="1" stop-color="#8fa3b7"/></linearGradient>
<linearGradient id="dg-hood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dfe6ed"/><stop offset="1" stop-color="#9fb1c3"/></linearGradient></defs>
<rect x="10" y="92" width="500" height="318" rx="10" fill="${wall}"/>
<path d="M0 92h520" stroke="${stroke}" stroke-width="3" opacity=".6"/>
<text x="20" y="84" fill="${stroke}" opacity=".6" font-size="12" font-family="sans-serif">Toiture</text>
<path d="M180 250 V168 H410 V92" fill="none" stroke="url(#dg-duct)" stroke-width="36" stroke-linejoin="miter"/>
<path d="M180 250 V168 H410 V92" fill="none" stroke="#7a4a1c" stroke-width="36" stroke-dasharray="2 14" opacity=".45"/>
<rect x="268" y="152" width="26" height="32" rx="3" fill="#0e1c2b" opacity=".75"/><text x="252" y="205" fill="${stroke}" font-size="10.5" font-family="sans-serif" opacity=".75">trappe de visite</text>
<g><rect x="382" y="58" width="56" height="34" rx="4" fill="#9fb1c3"/><path d="M366 58 q44 -34 88 0z" fill="#c9d4df"/><circle cx="410" cy="76" r="9" fill="none" stroke="#0e1c2b" stroke-width="2"/><path d="M410 67v18M401 76h18" stroke="#0e1c2b" stroke-width="2"/></g>
<g stroke="#5fd39c" stroke-width="2.5" fill="none" stroke-linecap="round" opacity=".9"><path d="M396 30c-4-8 4-12 0-20"/><path d="M412 26c-4-8 4-12 0-20"/><path d="M428 30c-4-8 4-12 0-20"/></g>
<path d="M70 318 L290 318 L246 250 L114 250 Z" fill="url(#dg-hood)" stroke="#0e1c2b" stroke-width="2"/>
<path d="M130 262 L230 262" stroke="#7a4a1c" stroke-width="5" opacity=".5" stroke-linecap="round"/>
<g stroke="#4a5f75" stroke-width="3"><path d="M92 312l24-44"/><path d="M104 312l24-44"/><path d="M116 312l24-44"/><path d="M128 312l24-44"/></g>
<rect x="60" y="318" width="240" height="7" fill="#e0701b"/>
<rect x="60" y="372" width="240" height="38" rx="4" fill="#4a5f75"/><rect x="60" y="364" width="240" height="10" fill="#6b7c8f"/>
<g><ellipse cx="120" cy="360" rx="26" ry="5" fill="#2b3b4c"/><path d="M108 356c3-10 8-6 6-18 8 8 12 12 8 18" fill="#f3a03c"/><ellipse cx="220" cy="360" rx="30" ry="5" fill="#2b3b4c"/><path d="M210 356c2-8 6-5 5-13 6 6 9 9 6 13" fill="#f3c34d"/></g>
<g stroke="#e0701b" stroke-width="2" fill="none" stroke-dasharray="4 5" opacity=".8"><path d="M120 340c0-18 20-30 50-50"/><path d="M220 340c0-18-10-30-30-52"/></g>
${[
    ["hotte", 290, 300],
    ["filtres", 120, 290],
    ["plenum", 214, 262],
    ["conduit", 340, 168],
    ["tourelle", 452, 70]
  ].map(([k, x, y]) => `<g class="hotspot" data-key="${k}" tabindex="0" role="button" aria-label="${diagramParts[k][0]}"><circle class="pulse" cx="${x}" cy="${y}" r="11" fill="#e0701b"/><circle class="dot" cx="${x}" cy="${y}" r="11" fill="#e0701b" stroke="#fff" stroke-width="3"/></g>`).join("")}
</svg>
<div class="diagram-tabs">${Object.entries(diagramParts).map(([k, v]) => `<button type="button" data-key="${k}" aria-pressed="false">${v[0].replace(/^(La|Le|Les) /, "").replace(/^./, (m) => m.toUpperCase())}</button>`).join("")}</div>
<div class="diagram-panel" aria-live="polite"></div>
${Object.entries(diagramParts).map(([k, v]) => `<template data-key="${k}"><strong>${v[0]}</strong>${v[1]}</template>`).join("")}
</div>`;
}

const trustStrip = () => `<div class="trust"><div class="container">
<div class="trust-item">${ico("graduation")}<div><strong>Techniciens diplômés</strong><span>Formés aux métiers de la propreté</span></div></div>
<div class="trust-item">${ico("doc")}<div><strong>Certificat à chaque passage</strong><span>Photos avant / après incluses</span></div></div>
<div class="trust-item">${ico("moon")}<div><strong>Zéro service interrompu</strong><span>Nuit, matin, jour de fermeture</span></div></div>
<div class="trust-item">${ico("euro")}<div><strong>Devis gratuit sous 24 h</strong><span>Prix ferme, sur devis</span></div></div>
</div></div>`;

const credentials = [
  ["CAP", "CAP Agent de propreté et d'hygiène", "Techniques de nettoyage, produits, matériels et règles de sécurité : le socle de notre métier."],
  ["BAC PRO", "Bac pro Hygiène, propreté, stérilisation", "Organisation de chantiers, protocoles, contrôle de la qualité et traçabilité des interventions."],
  ["HAUT.", "Travail en hauteur", "Interventions en toiture et sur échafaudage avec les protections adaptées contre les chutes."],
  ["ÉLEC.", "Sensibilisation au risque électrique", "Consignation des extracteurs et des équipements avant toute intervention."],
  ["CHIM.", "Risque chimique", "Lecture des fiches de sécurité, dosage des dégraissants, équipements de protection individuelle."],
  ["HACCP", "Hygiène alimentaire", "Intervenir en cuisine sans compromettre la sécurité des denrées ni votre plan de maîtrise sanitaire."],
  ["SST", "Sauveteur secouriste du travail", "Savoir réagir et porter secours en cas d'accident sur un chantier."],
  ["INT.", "Formation interne Clairvent", "Nos protocoles d'extraction : circuit complet, photos à chaque trappe, certificat honnête."]
];
const credGrid = (n = 8) => `<div class="grid g4">${credentials.slice(0, n).map(([b, t, d]) => `<div class="card cred reveal"><span class="badge">${b}</span><div><h3>${t}</h3><p>${d}</p></div></div>`).join("")}</div>`;

const methodSteps = [
  ["Écoute et visite technique", "Au téléphone, sur photos ou sur place, nous relevons votre installation : longueur de hotte, tracé du conduit, accès, type de cuisson."],
  ["Devis ferme et détaillé", "Sous 24 h ouvrées, un devis gratuit, élément par élément, avec le créneau proposé. Pas de surprise le jour J."],
  ["Protection de la cuisine", "Bâchage des équipements, protection des sols et des plans de travail, consignation électrique de l'extracteur."],
  ["Filtres et hotte", "Dépose et trempage des filtres, grattage et dégraissage de la hotte et des gouttières."],
  ["Plénum et conduit", "Grattage des dépôts épais, brossage rotatif, mousse dégraissante, photos à chaque trappe de visite."],
  ["Extracteur", "Dégraissage de la turbine et du caisson en toiture, contrôle visuel de la courroie et du moteur."],
  ["Rinçage et remise en service", "Rinçage, séchage, remontage des filtres, essai de fonctionnement, cuisine rendue propre."],
  ["Certificat et suivi", "Certificat daté et signé, dossier photo, réserves éventuelles et date conseillée du prochain passage."]
];
const stepsHtml = (list, cls = "") => `<ol class="steps ${cls}">${list.map(([t, d]) => `<li class="reveal"><h3>${t}</h3><p>${d}</p></li>`).join("")}</ol>`;

const faqHtml = (list) => `<div class="faq">${list.map(([q, a]) => `<details><summary>${q}</summary><div><p>${a}</p></div></details>`).join("")}</div>`;
const faqLd = (list) => ({
  "@context": "https://schema.org", "@type": "FAQPage",
  mainEntity: list.map(([q, a]) => ({ "@type": "Question", name: q, acceptedAnswer: { "@type": "Answer", text: a } }))
});

const ctaBand = (title = "Votre extraction mérite un vrai dégraissage", text = "Devis gratuit sous 24 h, prix sur devis, intervention hors service. Un technicien diplômé vous répond.", q = "") => `
<section class="section-sm"><div class="container"><div class="cta-band">
<div><h2>${title}</h2><p>${text}</p></div>
<div class="actions"><a class="btn btn-light btn-lg" href="{r}reservation.html${q}">${ico("calendar")}Réserver</a><a class="btn btn-ghost-light btn-lg" href="tel:${SITE.tel}">${ico("phone")}${SITE.phone}</a></div>
</div></div></section>`;

const svcCard = (s) => `<a class="card card-link reveal" href="{r}prestations/${s.slug}.html"><span class="card-icon">${ico(s.icon)}</span><h3>${s.nav}</h3><p>${s.desc.split(".")[0]}.</p><span class="more">Découvrir ${ico("arrow")}</span></a>`;
const guideCard = (g) => {
  const c = CATS[g.cat];
  return `<a class="card card-link post-card reveal" href="{r}conseils/${g.slug}.html" data-cat="${g.cat}"><div class="thumb ${c.cls}">${ico(c.icon)}</div><span class="meta">${c.name} · ${Math.max(3, Math.round(words(g.body) / 200))} min de lecture</span><h3>${g.title}</h3><p>${g.desc}</p><span class="more">Lire le conseil ${ico("arrow")}</span></a>`;
};

const provider = {
  "@type": "LocalBusiness",
  "@id": SITE.url + "/#business",
  name: SITE.name,
  telephone: SITE.tel,
  url: SITE.url,
  image: SITE.url + "/assets/img/og-image.svg",
  priceRange: "Sur devis",
  address: { "@type": "PostalAddress", streetAddress: SITE.street, postalCode: SITE.cp, addressLocality: SITE.city, addressRegion: "Île-de-France", addressCountry: "FR" },
  geo: { "@type": "GeoCoordinates", latitude: base.lat, longitude: base.lon },
  areaServed: depts.map((d) => ({ "@type": "AdministrativeArea", name: `${d.name} (${d.code})` })),
  openingHoursSpecification: [{ "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], opens: "08:00", closes: "20:00" }]
};

function sidebar(extra = "") {
  return `<aside class="sidebar">
<div class="widget widget-cta"><h3>Besoin d'un dégraissage ?</h3><p>Un technicien vous répond ${SITE.hours}.</p><a class="phone-big" href="tel:${SITE.tel}">${SITE.phone}</a><a class="btn" href="{r}reservation.html">${ico("calendar")}Réserver en ligne</a><a class="btn btn-ghost-light" href="{r}devis.html">Devis gratuit</a></div>
${extra}
<div class="widget"><h3>Prestations</h3><ul>${services.slice(0, 9).map((s) => `<li><a href="{r}prestations/${s.slug}.html">${s.nav}</a></li>`).join("")}</ul></div>
<div class="widget"><h3>Catégories</h3><ul>${Object.entries(CATS).map(([k, c]) => `<li><a href="{r}conseils.html#${k}">${c.name}<small>${guides.filter((g) => g.cat === k).length}</small></a></li>`).join("")}</ul></div>
<div class="widget"><h3>Outil gratuit</h3><p class="muted" style="font-size:14.5px">Quelle fréquence de dégraissage pour votre cuisine ? Réponse en 30 secondes.</p><a class="btn btn-outline btn-sm" href="{r}diagnostic.html">Lancer le diagnostic</a></div>
</aside>`;
}

/* Carte de la zone d'intervention (projection simple) */
function zoneMap({ highlight = null, labels = true } = {}) {
  const X = (lon) => (lon - 1.95) * 600;
  const Y = (lat) => (49.12 - lat) * 912;
  const bx = X(base.lon), by = Y(base.lat);
  const pxPerKm = 8.2;
  const big = ["Paris 1er", "Versailles", "Cergy", "Meaux", "Melun", "Évry-Courcouronnes", "Roissy-en-France", "Boulogne-Billancourt", "Créteil", "Serris / Val d'Europe"];
  return `<svg viewBox="0 0 600 560" role="img" aria-label="Carte de la zone d'intervention de ${SITE.name} en Île-de-France">
<rect width="600" height="560" fill="#f7f9fb"/>
${[10, 25, 40].map((k) => `<circle cx="${bx.toFixed(1)}" cy="${by.toFixed(1)}" r="${(k * pxPerKm).toFixed(1)}" fill="${k === 10 ? "rgba(224,112,27,.12)" : "none"}" stroke="#e0701b" stroke-dasharray="5 6" stroke-width="1.4" opacity=".7"/><text x="${(bx + k * pxPerKm * 0.71 + 4).toFixed(1)}" y="${(by - k * pxPerKm * 0.71).toFixed(1)}" font-size="11" fill="#c25a0c" font-family="sans-serif">${k} km</text>`).join("")}
<ellipse cx="${X(2.347).toFixed(1)}" cy="${Y(48.859).toFixed(1)}" rx="${(0.09 * 600).toFixed(1)}" ry="${(0.05 * 912).toFixed(1)}" fill="rgba(31,95,158,.08)" stroke="#1f5f9e" stroke-width="1" opacity=".8"/>
<text x="${X(2.30).toFixed(1)}" y="${Y(48.90).toFixed(1)}" font-size="12" font-weight="700" fill="#1f5f9e" font-family="sans-serif">PARIS</text>
${cities.map((c) => {
    const x = X(c.lon), y = Y(c.lat);
    const hi = highlight && c.slug === highlight;
    return `<a href="{r}villes/nettoyage-hotte-${c.slug}.html"><circle class="city" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${hi ? 7 : 3.6}" ${hi ? 'fill="#e0701b" stroke="#fff" stroke-width="2"' : ""}><title>Nettoyage de hotte ${aV(c.name)}</title></circle></a>${(labels && big.includes(c.name) && !hi) ? `<text x="${(x + 6).toFixed(1)}" y="${(y + 4).toFixed(1)}" font-size="11" fill="#4a5f75" font-family="sans-serif">${c.name.replace(" 1er", "")}</text>` : ""}${hi ? `<text x="${(x + 10).toFixed(1)}" y="${(y + 4).toFixed(1)}" font-size="13" font-weight="700" fill="#0e1c2b" font-family="sans-serif">${c.name}</text>` : ""}`;
  }).join("")}
<g><circle cx="${bx.toFixed(1)}" cy="${by.toFixed(1)}" r="11" fill="#0e1c2b" stroke="#e0701b" stroke-width="3"/><text x="${(bx + 16).toFixed(1)}" y="${(by - 10).toFixed(1)}" font-size="13" font-weight="800" fill="#0e1c2b" font-family="sans-serif">Clairvent · ${SITE.city}</text></g>
</svg>`;
}

/* ------------------------------------------------------------------ */
/* Pages                                                                */
/* ------------------------------------------------------------------ */
const homeFaq = [
  ["Combien coûte un nettoyage de hotte professionnelle ?", "Nos prix sont établis sur devis, gratuit et sans engagement. Ils dépendent de la taille de la hotte, de la longueur et de l'accessibilité du conduit, du type d'extracteur et du niveau d'encrassement. Vous recevez un devis détaillé sous 24 heures ouvrées."],
  ["À quelle fréquence faut-il faire nettoyer sa hotte ?", "Au minimum une fois par an pour un établissement recevant du public, conformément au règlement de sécurité incendie. Pour une cuisine intensive (friture, grill, wok), deux à quatre dégraissages par an sont recommandés."],
  ["Vos techniciens sont-ils qualifiés ?", "Oui. Nos prestations sont réalisées par des techniciens formés et diplômés dans les métiers de la propreté, formés au travail en hauteur, au risque chimique, au risque électrique et à l'hygiène alimentaire."],
  ["Devez-vous fermer mon restaurant pendant l'intervention ?", "Non. Nous intervenons en dehors de vos services : la nuit, tôt le matin, l'après-midi ou le jour de fermeture."],
  ["Remettez-vous un certificat ?", "Oui, à chaque intervention : un certificat daté et signé, la liste des éléments nettoyés, les réserves éventuelles et un dossier photo avant / après."],
  ["Intervenez-vous chez les particuliers ?", "Oui. Nous nettoyons les hottes domestiques et réalisons des nettoyages complets de cuisine à domicile dans toute l'Île-de-France."]
];

function home() {
  const hotte = services.filter((s) => s.group === "hotte");
  const cuisine = services.filter((s) => s.group === "cuisine");
  const heroHtml = `
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow">${ico("shield")}Spécialiste hottes &amp; extraction · Île-de-France</span>
      <h1>Des hottes <em>vraiment</em> dégraissées, de la cuisine jusqu'au toit.</h1>
      <p class="lead">Clairvent nettoie l'ensemble de votre système d'extraction — hotte, filtres, plénum, conduit et tourelle — et remet votre cuisine en état. Des techniciens diplômés, un certificat à chaque passage, et jamais un service interrompu.</p>
      <div class="hero-cta">
        <a class="btn btn-lg" href="reservation.html">${ico("calendar")}Réserver une intervention</a>
        <a class="btn btn-lg btn-ghost-light" href="tel:${SITE.tel}">${ico("phone")}${SITE.phone}</a>
      </div>
      <ul class="hero-proof">
        <li>${ico("check")}<span>Circuit complet traité, pas seulement les filtres</span></li>
        <li>${ico("check")}<span>Certificat conforme pour l'assurance et la commission de sécurité</span></li>
        <li>${ico("check")}<span>Interventions de nuit, tôt le matin ou le jour de fermeture</span></li>
        <li>${ico("check")}<span>Devis gratuit sous 24 h — prix sur devis</span></li>
      </ul>
    </div>
    <div class="hero-visual">${diagram(false)}<p class="muted mb0" style="font-size:13px;margin-top:10px;color:#9fb1c3">Touchez un point orange pour découvrir ce que nous nettoyons.</p></div>
  </div>
</section>${trustStrip()}`;

  const body = `
<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Nos prestations</span><h2>Le nettoyage de hotte, notre unique métier</h2><p>Nous ne faisons pas « un peu de tout ». Nous nous consacrons aux hottes, à l'extraction et aux cuisines : c'est ce qui nous permet de le faire très bien.</p></div>
    <div class="grid g4">${hotte.map(svcCard).join("")}</div>
    <div class="section-head mt3"><h3 style="font-size:1.4rem">Et pour toute votre cuisine</h3><p>Nettoyage de fond, remise en état, nouveau nettoyage si le précédent vous a déçu : nous traitons aussi le reste de la cuisine.</p></div>
    <div class="grid g4">${cuisine.map(svcCard).join("")}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="container split">
    <div>
      <span class="eyebrow" style="color:#ffb070">Pourquoi c'est vital</span>
      <h2>La graisse de votre conduit est un combustible</h2>
      <p>Service après service, les vapeurs grasses se condensent derrière les filtres et tapissent le conduit. Une flambée ou un feu de friteuse suffit à embraser ce dépôt, et le tirage de l'extracteur propage le feu jusqu'au toit.</p>
      <p>C'est pourquoi le règlement de sécurité incendie impose un nettoyage du circuit complet <strong style="color:#fff">au minimum une fois par an</strong> dans les établissements recevant du public — et pourquoi votre assureur vous demandera le certificat.</p>
      <p><a class="btn" href="reglementation.html">Ce que dit la réglementation</a></p>
    </div>
    <div class="pledges">
      <div class="pledge"><b>100 %</b><span>du circuit traité : hotte, filtres, plénum, conduit, extracteur</span></div>
      <div class="pledge"><b>0</b><span>service interrompu : nous travaillons quand vous êtes fermés</span></div>
      <div class="pledge"><b>24 h</b><span>pour recevoir un devis gratuit, ferme et détaillé</span></div>
      <div class="pledge"><b>1</b><span>certificat et un dossier photo remis à chaque passage</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center"><span class="eyebrow">Notre méthode</span><h2>Huit étapes, zéro raccourci</h2><p>Un protocole identique sur chaque chantier, pour un résultat que vous pouvez vérifier sur photos.</p></div>
    ${stepsHtml(methodSteps, "g2")}
    <p class="center mt2"><a class="btn btn-outline" href="methode.html">Voir la méthode en détail</a></p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="split" style="align-items:start">
      <div>
        <span class="eyebrow">Savoir-faire</span>
        <h2>Des techniciens formés et diplômés, pas des intérimaires d'un jour</h2>
        <p class="lead-dark">Un dégraissage d'extraction se fait avec des produits puissants, en hauteur, sur des équipements électriques et au-dessus d'une cuisine où l'on prépare des repas. Cela ne s'improvise pas.</p>
        <p>Nos prestations sont réalisées par des personnes <strong>formées et diplômées dans les métiers du nettoyage</strong>, complétées par des formations spécifiques au travail en hauteur, au risque chimique, à la consignation électrique et à l'hygiène alimentaire. Chaque nouveau technicien suit notre protocole interne avant d'intervenir seul.</p>
        <ul class="check"><li>Diplômes de la propreté (CAP, Bac pro)</li><li>Habilitations et formations sécurité à jour</li><li>Encadrement et contrôle qualité sur chaque chantier</li></ul>
        <p><a class="btn" href="notre-savoir-faire.html">Découvrir notre équipe</a></p>
      </div>
      ${credGrid(4).replace("grid g4", "grid g2")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="certif reveal">
      <h3>Certificat de nettoyage d'extraction</h3>
      <p class="mb0" style="color:#6b5a3e">N° CV-2026-0000 · Spécimen</p>
      <table><tbody>
      <tr><th>Établissement</th><td>Restaurant exemple, 75011 Paris</td></tr>
      <tr><th>Hotte</th><td>✔ Dégraissée — 3,20 m</td></tr>
      <tr><th>Filtres</th><td>✔ 8 filtres à chicanes, trempage</td></tr>
      <tr><th>Plénum</th><td>✔ Gratté et dégraissé</td></tr>
      <tr><th>Conduit</th><td>✔ 11 m traités · 3 trappes</td></tr>
      <tr><th>Tourelle</th><td>✔ Turbine dégraissée</td></tr>
      <tr><th>Réserves</th><td>Coude n° 2 sans trappe de visite</td></tr>
      </tbody></table>
      <p class="mb0" style="font-size:13px;color:#6b5a3e">Photos avant / après jointes · Prochain passage conseillé : dans 4 mois</p>
    </div>
    <div>
      <span class="eyebrow">La preuve, noir sur blanc</span>
      <h2>Un certificat honnête, qui tient face à un expert</h2>
      <p>Notre certificat détaille chaque élément traité, la longueur de conduit nettoyée, les zones inaccessibles et nos recommandations. Il est accompagné de photos avant / après prises à chaque trappe de visite.</p>
      <p>C'est le document que demandent la commission de sécurité et votre assureur. Nous ne l'avons jamais délivré sans intervention réelle, et nous ne le ferons jamais.</p>
      <p><a class="btn btn-outline" href="certificat-de-degraissage.html">Voir le certificat en détail</a></p>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container split">
    <div>
      <span class="eyebrow">Outil gratuit</span>
      <h2>Tous les combien faut-il dégraisser <em style="font-style:normal;color:var(--accent-2)">votre</em> hotte ?</h2>
      <p>Quatre questions, trente secondes : notre outil estime la fréquence adaptée à votre cuisine, à partir des pratiques professionnelles courantes et du minimum réglementaire.</p>
      <p><a class="btn btn-outline" href="diagnostic.html">Faire aussi l'auto-diagnostic de conformité</a></p>
    </div>
    ${freqTool()}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Secteurs</span><h2>Chaque cuisine a sa graisse</h2><p>Un wok, un grill au charbon et un four de boulangerie n'encrassent pas une extraction de la même façon. Nous adaptons nos produits, nos outils et notre fréquence.</p></div>
    <div class="grid g4">${sectors.map((s) => `<a class="card card-link reveal" href="secteurs/${s.slug}.html"><span class="card-icon">${ico(s.icon)}</span><h3>${s.name}</h3><p>${s.freq}</p><span class="more">Voir ${ico("arrow")}</span></a>`).join("")}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Sur le terrain</span><h2>Des résultats que l'on peut vérifier</h2><p>Chaque paire de photos provient d'une même intervention réelle, prise au même endroit avant et après notre passage.</p></div>
    <div class="grid g2">
      <div class="ba reveal"><figure><img src="assets/photos/avant-plan-travail.webp" alt="Plan de travail inox encrassé avant nettoyage" loading="lazy" width="700" height="933"><figcaption>Avant</figcaption></figure><figure><img src="assets/photos/apres-plan-travail.webp" alt="Même plan de travail inox après nettoyage" loading="lazy" width="700" height="933"><figcaption>Après</figcaption></figure></div>
      <div class="ba reveal"><figure><img src="assets/photos/avant-frigo.webp" alt="Réfrigérateur encrassé avant nettoyage" loading="lazy"><figcaption>Avant</figcaption></figure><figure><img src="assets/photos/apres-frigo.webp" alt="Même réfrigérateur après nettoyage et désinfection" loading="lazy"><figcaption>Après</figcaption></figure></div>
    </div>
    <p class="center mt2"><a class="btn btn-outline" href="realisations.html">Voir nos réalisations</a></p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="zone-map reveal">${zoneMap()}</div>
    <div>
      <span class="eyebrow">Zone d'intervention</span>
      <h2>Basés ${SITE.au}, au cœur de l'Île-de-France</h2>
      <p>Notre base est située ${SITE.au} (93), à quelques minutes de Paris, de Roissy et des grands axes (A1, A3, A86). Nous intervenons dans les huit départements franciliens, avec des délais particulièrement courts en Seine-Saint-Denis, à Paris et en petite couronne.</p>
      <ul class="pill-list">${depts.map((d) => `<li><a href="zones/${d.slug}.html">${d.name} (${d.code})</a></li>`).join("")}</ul>
      <p class="mt2"><a class="btn" href="ou-nous-trouver.html">${ico("pin")}Où nous trouver</a> <a class="btn btn-outline" href="zones.html">Toutes les villes</a></p>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Conseils d'experts</span><h2>Nos derniers guides</h2><p>Réglementation, sécurité incendie, hygiène, entretien au quotidien : ce que nos techniciens expliquent chaque jour à nos clients.</p></div>
    <div class="grid g3">${["reglementation-nettoyage-hotte-erp", "frequence-degraissage-hotte", "incendie-conduit-extraction-comment-l-eviter", "certificat-nettoyage-hotte-assurance", "choisir-entreprise-nettoyage-hotte", "nettoyer-hotte-cuisine-maison"].map((s) => guideCard(guideBySlug[s])).join("")}</div>
    <p class="center mt2"><a class="btn btn-outline" href="conseils.html">Tous nos conseils (${guides.length})</a></p>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:880px">
    <div class="section-head center"><span class="eyebrow">Questions fréquentes</span><h2>Vous vous posez sûrement ces questions</h2></div>
    ${faqHtml(homeFaq)}
  </div>
</section>
${ctaBand()}`;
  layout({
    path: "index.html",
    title: "Nettoyage de hotte professionnelle en Île-de-France | Clairvent",
    desc: "Clairvent : nettoyage et dégraissage de hottes, conduits d'extraction et cuisines professionnelles en Île-de-France. Techniciens diplômés, certificat, devis gratuit.",
    section: "home",
    heroHtml,
    body,
    priority: 1,
    jsonld: [
      { "@context": "https://schema.org", ...provider, description: "Nettoyage de hottes, de conduits d'extraction et de cuisines professionnelles et particulières en Île-de-France." },
      { "@context": "https://schema.org", "@type": "WebSite", name: SITE.name, url: SITE.url },
      faqLd(homeFaq)
    ]
  });
}

function freqTool() {
  return `<div class="tool reveal">
<form data-freq-tool data-resa="{r}reservation.html" data-devis="{r}devis.html" class="form">
<div><label for="f-cuisson">Mode de cuisson principal</label><select id="f-cuisson" name="cuisson">
<option value="0">Vapeur, four, cuisson douce</option><option value="1" selected>Cuisine traditionnelle (piano, four, sauteuse)</option><option value="2">Plancha, pizzas, friture occasionnelle</option><option value="3">Friture, grill, wok, rôtisserie, kebab</option></select></div>
<div class="form-row">
<div><label for="f-volume">Couverts par jour</label><select id="f-volume" name="volume"><option value="0">Moins de 80</option><option value="1" selected>80 à 200</option><option value="2">200 à 400</option><option value="3">Plus de 400</option></select></div>
<div><label for="f-heures">Heures de cuisson par jour</label><select id="f-heures" name="heures"><option value="0">Moins de 4 h</option><option value="1" selected>4 à 8 h</option><option value="2">8 à 12 h</option><option value="3">Plus de 12 h</option></select></div>
</div>
<div class="form-row">
<div><label for="f-filtres">Nettoyage des filtres</label><select id="f-filtres" name="filtres"><option value="0">Plusieurs fois par semaine</option><option value="1" selected>Une fois par semaine</option><option value="2">Une fois par mois</option><option value="3">Rarement / jamais</option></select></div>
<div><label for="f-dernier">Dernier dégraissage complet</label><select id="f-dernier" name="dernier"><option value="2">Il y a moins de 3 mois</option><option value="5" selected>Il y a 3 à 6 mois</option><option value="9">Il y a 6 à 12 mois</option><option value="24">Plus d'un an / je ne sais pas</option></select></div>
</div>
<button class="btn" type="submit">${ico("search")}Calculer ma fréquence</button>
</form>
<div class="tool-result" aria-live="polite"></div>
</div>`;
}

function servicePages() {
  // Hub
  const hotte = services.filter((s) => s.group === "hotte");
  const cuisine = services.filter((s) => s.group === "cuisine");
  layout({
    path: "prestations.html",
    section: "presta",
    title: "Nos prestations : nettoyage de hotte et de cuisine | Clairvent",
    desc: "Toutes les prestations Clairvent : dégraissage de hotte, conduit, tourelle, filtres, certificat, contrat d'entretien, nettoyage et remise en état de cuisine.",
    h1: "Nos prestations de nettoyage de hotte et de cuisine",
    lead: "Du simple nettoyage de filtres au dégraissage complet d'une extraction de 30 mètres, en passant par la remise en état d'une cuisine : chaque prestation est réalisée par nos techniciens diplômés, sur devis.",
    crumbs: [["Prestations", "prestations.html"]],
    heroCta: `<a class="btn" href="{r}devis.html">Demander un devis gratuit</a><a class="btn btn-ghost-light" href="{r}reservation.html">Réserver</a>`,
    body: `${trustStrip()}
<section class="section"><div class="container">
<div class="section-head"><h2>Hottes et extraction</h2><p>Le cœur de notre métier : l'ensemble du circuit d'extraction des cuisines professionnelles, et les hottes des particuliers.</p></div>
<div class="grid g4">${hotte.map(svcCard).join("")}</div>
<div class="section-head mt3"><h2>Cuisines</h2><p>Nettoyage de fond, remise en état, nouveau nettoyage, équipements, chambres froides : pour une cuisine irréprochable du plafond au sol.</p></div>
<div class="grid g4">${cuisine.map(svcCard).join("")}</div>
</div></section>
<section class="section section-alt"><div class="container split">
<div><span class="eyebrow">Prix</span><h2>Pourquoi nos prix sont sur devis</h2><p>Deux cuisines ne se ressemblent jamais : longueur de hotte, tracé du conduit, nombre de trappes, accès à la toiture, niveau d'encrassement, horaires. Un prix affiché « à partir de » ne vous apprend rien et cache souvent un périmètre réduit.</p><p>Notre devis est gratuit, ferme et détaillé élément par élément. Il est établi après une visite technique ou l'étude de vos photos, et vous le recevez sous 24 heures ouvrées.</p><p><a class="btn" href="{r}devis.html">Recevoir mon devis</a></p></div>
<div><ul class="check"><li>Visite technique gratuite en Île-de-France</li><li>Devis sous 24 h ouvrées</li><li>Périmètre détaillé : hotte, filtres, plénum, conduit, extracteur</li><li>Certificat et photos toujours inclus</li><li>Aucun frais caché, aucun acompte exigé pour une première intervention ponctuelle</li><li>Tarif fixe par passage pour les contrats d'entretien</li></ul></div>
</div></section>
${ctaBand()}`
  });

  for (const s of services) {
    const related = (s.related || []).map((x) => guideBySlug[x]).filter(Boolean);
    const others = services.filter((o) => o.slug !== s.slug && o.group === s.group).slice(0, 4);
    const secs = sectors.filter((x) => x.services.includes(s.slug)).slice(0, 6);
    const faq = [...s.faq, ["Dans quelles villes intervenez-vous ?", `Nous intervenons dans toute l'Île-de-France depuis notre base ${SITE.du} (93) : Paris, Hauts-de-Seine, Seine-Saint-Denis, Val-de-Marne, Val-d'Oise, Seine-et-Marne, Essonne et Yvelines.`]];
    const body = `
<section class="section"><div class="container with-sidebar">
<article>
<div class="prose">
${s.intro.map((p) => `<p>${p}</p>`).join("")}
<h2>Ce que comprend la prestation</h2>
<ul class="check">${s.includes.map((i) => `<li>${i}</li>`).join("")}</ul>
${s.body}
<h2>Comment se déroule l'intervention</h2>
</div>
<div class="mt2">${stepsHtml(s.steps)}</div>
<div class="prose mt2">
<h2>Réalisée par des techniciens formés et diplômés</h2>
<p>Cette prestation est réalisée par nos techniciens, titulaires de diplômes des métiers de la propreté et formés au travail en hauteur, au risque chimique, à la consignation électrique et à l'hygiène alimentaire. <a href="../notre-savoir-faire.html">En savoir plus sur notre équipe</a>.</p>
<h2>Prix : sur devis gratuit</h2>
<p>Le prix de cette prestation dépend de votre installation et de son état. Nous vous remettons un devis gratuit, ferme et détaillé sous 24 heures ouvrées, après visite technique ou étude de vos photos.</p>
<p><a class="btn" href="../reservation.html?prestation=${s.slug}">${ico("calendar")}Réserver cette prestation</a> <a class="btn btn-outline" href="../devis.html">Demander un devis</a></p>
</div>
<h2 class="mt3">Questions fréquentes</h2>
${faqHtml(faq)}
${related.length ? `<h2 class="mt3">Nos conseils sur le sujet</h2><div class="grid g3">${related.map(guideCard).join("")}</div>` : ""}
</article>
${sidebar(secs.length ? `<div class="widget"><h3>Secteurs concernés</h3><ul>${secs.map((x) => `<li><a href="{r}secteurs/${x.slug}.html">${x.name}</a></li>`).join("")}</ul></div>` : "")}
</div></section>
<section class="section section-alt"><div class="container"><div class="section-head"><h2>Prestations complémentaires</h2></div><div class="grid g4">${others.map(svcCard).join("")}</div></div></section>
${ctaBand(undefined, undefined, `?prestation=${s.slug}`)}`;
    layout({
      path: `prestations/${s.slug}.html`,
      section: "presta",
      title: s.metaTitle,
      desc: s.desc,
      h1: s.title,
      lead: s.lead,
      eyebrow: `${ico(s.icon)}${s.group === "hotte" ? "Hottes & extraction" : "Nettoyage de cuisine"}`,
      crumbs: [["Prestations", "prestations.html"], [s.nav, `prestations/${s.slug}.html`]],
      heroCta: `<a class="btn" href="{r}reservation.html?prestation=${s.slug}">${ico("calendar")}Réserver</a><a class="btn btn-ghost-light" href="{r}devis.html">Devis gratuit</a><a class="btn btn-ghost-light" href="tel:${SITE.tel}">${ico("phone")}${SITE.phone}</a>`,
      body,
      priority: s.pillar ? 0.9 : 0.8,
      jsonld: [
        { "@context": "https://schema.org", "@type": "Service", name: s.title, description: s.desc, serviceType: s.nav, provider: { "@id": SITE.url + "/#business", ...provider }, areaServed: { "@type": "AdministrativeArea", name: "Île-de-France" }, offers: { "@type": "Offer", priceSpecification: { "@type": "PriceSpecification", priceCurrency: "EUR", description: "Prix sur devis gratuit" } } },
        faqLd(faq)
      ]
    });
  }
}

function sectorPages() {
  layout({
    path: "secteurs.html",
    section: "secteurs",
    title: "Nettoyage de hotte par secteur d'activité | Clairvent",
    desc: "Restaurants, fast-food, pizzerias, grills, cuisines asiatiques, hôtels, cantines, EHPAD, dark kitchens, traiteurs, food trucks : une méthode adaptée à chaque cuisine.",
    h1: "Une méthode adaptée à chaque cuisine",
    lead: "Chaque activité produit une graisse différente et impose ses contraintes horaires. Nous adaptons nos produits, nos outils et la fréquence de passage à votre secteur.",
    crumbs: [["Secteurs", "secteurs.html"]],
    body: `<section class="section"><div class="container"><div class="grid g3">${sectors.map((s) => `<a class="card card-link reveal" href="{r}secteurs/${s.slug}.html"><span class="card-icon">${ico(s.icon)}</span><h3>${s.name}</h3><p>${s.lead}</p><p><span class="tag tag-accent">${s.freq}</span></p><span class="more">Découvrir ${ico("arrow")}</span></a>`).join("")}</div></div></section>${ctaBand()}`
  });
  for (const s of sectors) {
    const svc = s.services.map((x) => svcBySlug[x]);
    const faq = [
      [`À quelle fréquence nettoyer la hotte ${s.name.toLowerCase().startsWith("h") ? "d'un" : "pour les"} ${s.name.toLowerCase()} ?`, `La fréquence indicative pour ce secteur est de ${s.freq.toLowerCase()}. Le minimum réglementaire en ERP reste d'un nettoyage complet par an, et le rythme exact dépend de votre volume et de vos modes de cuisson.`],
      ["Pouvez-vous intervenir sans perturber notre activité ?", "Oui. Nous intervenons en dehors de vos heures de production : la nuit, tôt le matin, l'après-midi ou le jour de fermeture."],
      ["Quel est le prix ?", "Nos prix sont établis sur devis gratuit, selon votre installation. Vous recevez un devis détaillé sous 24 heures ouvrées."]
    ];
    layout({
      path: `secteurs/${s.slug}.html`,
      section: "secteurs",
      title: `Nettoyage de hotte — ${s.name} | Clairvent`,
      desc: s.desc,
      h1: `Nettoyage de hotte et de cuisine : ${s.name.toLowerCase()}`,
      lead: s.lead,
      eyebrow: `${ico(s.icon)}Secteur`,
      crumbs: [["Secteurs", "secteurs.html"], [s.name, `secteurs/${s.slug}.html`]],
      heroCta: `<a class="btn" href="{r}reservation.html">${ico("calendar")}Réserver</a><a class="btn btn-ghost-light" href="{r}devis.html">Devis gratuit</a>`,
      body: `<section class="section"><div class="container with-sidebar"><article>
<div class="prose">
<h2>Les spécificités de votre cuisine</h2><p>${s.context}</p>
<h2>Les points de vigilance</h2><ul class="check">${s.risks.map((x) => `<li>${x}</li>`).join("")}</ul>
<h2>La fréquence recommandée</h2><p><strong>${s.freq}.</strong> Ce rythme est indicatif : nous l'ajustons à l'état réellement constaté à l'intérieur de votre conduit lors de chaque passage, photos à l'appui. Le minimum réglementaire pour un établissement recevant du public reste d'un nettoyage complet par an.</p>
<blockquote>Testez votre installation avec notre <a href="../diagnostic.html">outil de diagnostic gratuit</a> : il estime en 30 secondes la fréquence adaptée à votre activité.</blockquote>
<h2>Notre engagement</h2><p>Des techniciens formés et diplômés, un protocole identique sur chaque chantier, un certificat honnête et un dossier photo complet. Nous intervenons partout en Île-de-France depuis notre base ${SITE.du}.</p>
</div>
<h2 class="mt3">Les prestations adaptées</h2><div class="grid g2">${svc.map(svcCard).join("")}</div>
<h2 class="mt3">Questions fréquentes</h2>${faqHtml(faq)}
</article>${sidebar()}</div></section>${ctaBand()}`,
      jsonld: [faqLd(faq)]
    });
  }
}

function guidePages() {
  const catButtons = `<button type="button" data-cat="all" aria-pressed="true">Tous (${guides.length})</button>` + Object.entries(CATS).map(([k, c]) => `<button type="button" data-cat="${k}" aria-pressed="false" id="${k}">${c.name}</button>`).join("");
  layout({
    path: "conseils.html",
    section: "conseils",
    title: "Conseils et guides : hottes, extraction et cuisines | Clairvent",
    desc: `${guides.length} guides pratiques rédigés par nos techniciens : réglementation, sécurité incendie, hygiène, entretien des hottes et des cuisines professionnelles et domestiques.`,
    h1: "Conseils & guides d'experts",
    lead: "Réglementation, sécurité incendie, hygiène, entretien au quotidien : tout ce que nos techniciens expliquent chaque jour à nos clients, en accès libre.",
    crumbs: [["Conseils", "conseils.html"]],
    body: `<section class="section"><div class="container">
<div class="filters" data-filter>${catButtons}<input type="search" placeholder="Rechercher un conseil…" aria-label="Rechercher un conseil"></div>
<div class="grid g3">${guides.map(guideCard).join("")}</div>
</div></section>
<script>(function(){var h=location.hash.slice(1);if(h){var b=document.querySelector('[data-filter] button[data-cat="'+h+'"]');if(b)setTimeout(function(){b.click()},50);}})();</script>
${ctaBand()}`
  });
  guides.forEach((g, i) => {
    const c = CATS[g.cat];
    const { html, toc } = slugToHeadings(g.body);
    const rt = Math.max(3, Math.round(words(g.body) / 200));
    const same = guides.filter((x) => x.cat === g.cat && x.slug !== g.slug);
    const related = [...same, ...guides.filter((x) => x.cat !== g.cat)].filter((x) => x.slug !== g.slug).slice(0, 3);
    const svc = (g.services || []).map((x) => svcBySlug[x]).filter(Boolean);
    const prev = guides[(i - 1 + guides.length) % guides.length], next = guides[(i + 1) % guides.length];
    layout({
      path: `conseils/${g.slug}.html`,
      section: "conseils",
      ogType: "article",
      title: `${g.title} | Clairvent`,
      desc: g.desc,
      h1: g.title,
      lead: g.desc,
      eyebrow: `${ico(c.icon)}${c.name}`,
      meta: `<div class="post-meta"><span>${ico("calendar")}Mis à jour en ${SITE.updatedLabel}</span><span>${ico("clock")}${rt} min de lecture</span><span>${ico("users")}Équipe technique Clairvent</span></div>`,
      crumbs: [["Conseils", "conseils.html"], [c.name, `conseils.html#${g.cat}`], [g.title, `conseils/${g.slug}.html`]],
      body: `<section class="section"><div class="container with-sidebar"><article>
<div class="prose">
${toc.length > 2 ? `<nav class="toc" aria-label="Sommaire"><strong>Sommaire</strong><ol>${toc.map(([id, t]) => `<li><a href="#${id}">${t}</a></li>`).join("")}</ol></nav>` : ""}
${html}
${svc.length ? `<div class="callout"><svg class="ico"><use href="#i-sparkle"/></svg><p><strong>Besoin d'un professionnel ?</strong> Découvrez ${svc.map((s) => `<a href="../prestations/${s.slug}.html">${s.nav.toLowerCase()}</a>`).join(" et ")}. Devis gratuit sous 24 h.</p></div>` : ""}
<div class="author-box"><span class="avatar">${logo}</span><p><strong>Rédigé par l'équipe technique Clairvent</strong><br>Techniciens formés et diplômés dans les métiers de la propreté, spécialistes du dégraissage d'extraction en Île-de-France.</p></div>
</div>
<div class="grid g2 mt2"><a class="card card-link" href="{r}conseils/${prev.slug}.html"><span class="meta muted">← Conseil précédent</span><h3 style="font-size:1rem">${prev.title}</h3></a><a class="card card-link" href="{r}conseils/${next.slug}.html" style="text-align:right"><span class="meta muted">Conseil suivant →</span><h3 style="font-size:1rem">${next.title}</h3></a></div>
<h2 class="mt3">À lire aussi</h2><div class="grid g3">${related.map(guideCard).join("")}</div>
</article>${sidebar(`<div class="widget"><h3>Dans la même catégorie</h3><ul>${same.slice(0, 6).map((x) => `<li><a href="{r}conseils/${x.slug}.html">${x.title}</a></li>`).join("")}</ul></div>`)}</div></section>${ctaBand()}`,
      priority: 0.7,
      jsonld: [{
        "@context": "https://schema.org", "@type": "Article", headline: g.title, description: g.desc,
        dateModified: SITE.updated, datePublished: SITE.updated, inLanguage: "fr-FR",
        author: { "@type": "Organization", name: SITE.name + " — équipe technique" },
        publisher: { "@type": "Organization", name: SITE.name, logo: { "@type": "ImageObject", url: SITE.url + "/assets/img/favicon.svg" } },
        mainEntityOfPage: SITE.url + "/conseils/" + g.slug + ".html"
      }]
    });
  });
}

function placePages() {
  // Hub zones
  layout({
    path: "zones.html",
    section: "zones",
    title: "Zones d'intervention : nettoyage de hotte en Île-de-France | Clairvent",
    desc: `Nettoyage de hotte et de cuisine dans ${cities.length} villes d'Île-de-France : Paris, 92, 93, 94, 95, 77, 91, 78. Base ${SITE.au}, interventions rapides.`,
    h1: "Nos zones d'intervention en Île-de-France",
    lead: `Depuis notre base ${SITE.du} (93), nous intervenons dans les huit départements franciliens. Retrouvez ci-dessous toutes les villes où nos techniciens dégraissent hottes et cuisines chaque semaine.`,
    crumbs: [["Zones", "zones.html"]],
    heroCta: `<a class="btn" href="{r}ou-nous-trouver.html">${ico("pin")}Où nous trouver</a><a class="btn btn-ghost-light" href="{r}reservation.html">Réserver</a>`,
    body: `<section class="section"><div class="container split" style="align-items:start"><div class="zone-map">${zoneMap()}</div><div><h2>Huit départements, un seul niveau d'exigence</h2><p>Quel que soit votre département, vous bénéficiez de la même équipe, du même protocole et du même certificat. Seul le délai d'intervention varie légèrement selon la distance depuis notre base.</p><div class="grid g2">${depts.map((d) => `<a class="card card-link" href="{r}zones/${d.slug}.html"><h3>${d.name} (${d.code})</h3><p>${cities.filter((c) => c.dept === d.code).length} villes</p><span class="more">Voir ${ico("arrow")}</span></a>`).join("")}</div></div></div></section>
<section class="section section-alt"><div class="container">${depts.map((d) => `<div class="dept-title"><h2 class="mb0" style="font-size:1.4rem"><a href="{r}zones/${d.slug}.html" style="color:inherit;text-decoration:none">${d.name}</a></h2><span>${d.code}</span></div><ul class="city-list">${cities.filter((c) => c.dept === d.code).map((c) => `<li><a href="{r}villes/nettoyage-hotte-${c.slug}.html">Nettoyage de hotte ${aV(c.name)}</a></li>`).join("")}</ul>`).join("")}</div></section>${ctaBand()}`
  });

  for (const d of depts) {
    const list = cities.filter((c) => c.dept === d.code);
    const faq = [
      [`Intervenez-vous partout ${d.art} ${d.name} ?`, `Oui, nous intervenons dans toutes les communes ${d.art === "à" ? "de" : "du département"} ${d.name}, y compris celles qui ne figurent pas dans la liste ci-dessus.`],
      ["Quel est le délai pour une intervention ?", "Nous répondons sous 24 heures ouvrées avec un devis. L'intervention peut généralement être planifiée dans la semaine, et plus rapidement en cas d'urgence."],
      ["Le déplacement est-il facturé à part ?", "Non : le déplacement est intégré dans le devis, qui vous donne un prix global et ferme."]
    ];
    layout({
      path: `zones/${d.slug}.html`,
      section: "zones",
      title: `Nettoyage de hotte ${d.art} ${d.name} (${d.code}) | Clairvent`,
      desc: `Nettoyage et dégraissage de hotte, conduit d'extraction et cuisine ${d.art} ${d.name} (${d.code}). ${d.desc.split(":")[0]}. Devis gratuit, certificat.`,
      h1: `Nettoyage de hotte ${d.art} ${d.name} (${d.code})`,
      lead: d.desc,
      crumbs: [["Zones", "zones.html"], [`${d.name} (${d.code})`, `zones/${d.slug}.html`]],
      heroCta: `<a class="btn" href="{r}reservation.html">${ico("calendar")}Réserver</a><a class="btn btn-ghost-light" href="tel:${SITE.tel}">${ico("phone")}${SITE.phone}</a>`,
      body: `<section class="section"><div class="container with-sidebar"><article>
<div class="prose"><h2>Nos interventions ${d.art} ${d.name}</h2><p>Nos équipes dégraissent chaque semaine des hottes, des conduits et des extracteurs ${d.art} ${d.name}, pour des restaurants, des cuisines collectives, des hôtels et des particuliers. Toutes nos interventions suivent le même protocole en huit étapes et donnent lieu à un certificat et à un dossier photo.</p>
<h2>Les villes où nous intervenons</h2><ul class="city-list">${list.map((c) => `<li><a href="../villes/nettoyage-hotte-${c.slug}.html">${c.name}</a></li>`).join("")}</ul>
<h2>Nos prestations ${d.art} ${d.name}</h2><ul class="check cols">${services.map((s) => `<li><a href="../prestations/${s.slug}.html">${s.nav}</a></li>`).join("")}</ul></div>
<h2 class="mt3">Questions fréquentes</h2>${faqHtml(faq)}
</article>${sidebar()}</div></section>${ctaBand()}`,
      priority: 0.7,
      jsonld: [faqLd(faq)]
    });
  }

  const intros = [
    (c, d, dist) => `Vous exploitez un restaurant, une cuisine collective ou un commerce de bouche ${aV(c.name)} ? Clairvent dégraisse votre hotte, votre conduit et votre extracteur, et nettoie votre cuisine, sans interrompre vos services. Nos techniciens partent de notre base ${SITE.du}, à environ ${dist} km.`,
    (c, d, dist) => `À ${c.name}, nos techniciens diplômés prennent en charge le nettoyage complet de votre système d'extraction — hotte, filtres, plénum, conduit et tourelle — ainsi que le nettoyage de votre cuisine. Nous sommes basés ${SITE.au}, à environ ${dist} km.`,
    (c, d, dist) => `Clairvent intervient ${aV(c.name)} pour le dégraissage des hottes professionnelles et domestiques, des conduits et des extracteurs, et pour le nettoyage ou la remise en état des cuisines. Depuis notre base ${SITE.du}, ${c.name} se trouve à environ ${dist} km.`
  ];
  const generic = {
    "75": "Dans la capitale, les cuisines sont souvent installées en rez-de-chaussée ou en sous-sol d'immeubles anciens, avec des conduits qui montent sur plusieurs étages. Nous avons l'habitude de coordonner nos interventions avec les syndics et les gardiens.",
    "93": "En Seine-Saint-Denis, notre département d'implantation, nous bénéficions des délais d'intervention les plus courts, pour la restauration commerciale comme pour les cuisines collectives et les laboratoires.",
    "92": "Dans les Hauts-de-Seine, nous intervenons aussi bien dans les restaurants de quartier que dans les grandes cuisines de restauration d'entreprise.",
    "94": "Dans le Val-de-Marne, nous accompagnons restaurants, cuisines collectives et professionnels des métiers de bouche.",
    "95": "Dans le Val-d'Oise, nous intervenons dans les restaurants de centre-ville, les hôtels et la restauration des zones commerciales.",
    "77": "En Seine-et-Marne, nous planifions nos interventions par secteur pour garantir des délais maîtrisés, jusqu'à Meaux et Melun.",
    "91": "En Essonne, nous intervenons auprès des restaurants, des cuisines collectives et de la restauration d'entreprise.",
    "78": "Dans les Yvelines, nous intervenons dans les restaurants et hôtels de centre-ville comme dans les restaurants d'entreprise des pôles d'activité."
  };
  cities.forEach((c, i) => {
    const d = deptByCode[c.dept];
    const dist = Math.max(1, Math.round(km(base, c)));
    const delay = dist <= 12 ? "sous 48 à 72 h selon disponibilité" : dist <= 25 ? "généralement sous 3 à 5 jours" : "généralement dans la semaine";
    const near = cities.filter((x) => x.slug !== c.slug).map((x) => [x, km(c, x)]).sort((a, b) => a[1] - b[1]).slice(0, 8).map((x) => x[0]);
    const intro = intros[hash(c.slug) % intros.length](c, d, dist);
    const faq = [
      [`Intervenez-vous la nuit ${aV(c.name)} ?`, `Oui. À ${c.name} comme partout en Île-de-France, nous intervenons la nuit, tôt le matin, entre deux services ou le jour de fermeture, pour ne jamais interrompre votre activité.`],
      [`Quel est le prix d'un nettoyage de hotte ${aV(c.name)} ?`, "Nos prix sont établis sur devis gratuit et ferme, selon la taille de la hotte, la longueur du conduit, l'accès à l'extracteur et le niveau d'encrassement. Le déplacement est inclus dans le devis."],
      [`Sous quel délai pouvez-vous intervenir ${aV(c.name)} ?`, `Vous recevez votre devis sous 24 heures ouvrées. L'intervention est ${delay}, et plus rapidement en cas d'urgence : appelez-nous au ${SITE.phone}.`],
      ["Remettez-vous un certificat après l'intervention ?", "Oui, un certificat de nettoyage daté et signé, avec la liste des éléments traités et un dossier photo avant / après, à conserver dans votre registre de sécurité."]
    ];
    const q = `?ville=${encodeURIComponent(c.name)}`;
    layout({
      path: `villes/nettoyage-hotte-${c.slug}.html`,
      section: "zones",
      title: `Nettoyage de hotte ${aV(c.name)}${c.dept !== "75" ? ` (${c.dept})` : ""} — dégraissage & cuisine | Clairvent`,
      desc: `Nettoyage de hotte ${aV(c.name)} : dégraissage de hotte, conduit et tourelle, nettoyage de cuisine professionnelle ou domestique. Techniciens diplômés, certificat, devis gratuit.`,
      h1: `Nettoyage de hotte ${aV(c.name)}`,
      lead: `Dégraissage de hotte, de conduit et d'extracteur, nettoyage et remise en état de cuisine ${aV(c.name)}${c.dept !== "75" ? ` (${d.name})` : ""}. Techniciens diplômés, certificat remis, prix sur devis.`,
      crumbs: [["Zones", "zones.html"], [`${d.name} (${d.code})`, `zones/${d.slug}.html`], [c.name, `villes/nettoyage-hotte-${c.slug}.html`]],
      heroCta: `<a class="btn" href="{r}reservation.html${q}">${ico("calendar")}Réserver ${esc(aV(c.name))}</a><a class="btn btn-ghost-light" href="tel:${SITE.tel}">${ico("phone")}${SITE.phone}</a>`,
      body: `<section class="section"><div class="container with-sidebar"><article>
<div class="prose">
<p>${intro}</p>
<p>${c.note || generic[c.dept]}</p>
<dl class="kv" style="margin:22px 0;background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:16px 20px">
<dt>Ville</dt><dd>${c.name} — ${d.name} (${d.code})</dd>
<dt>Distance de notre base</dt><dd>environ ${dist} km (${SITE.city})</dd>
<dt>Délai indicatif</dt><dd>devis sous 24 h, intervention ${delay}</dd>
<dt>Créneaux</dt><dd>nuit, tôt le matin, entre deux services, jour de fermeture</dd>
<dt>Prix</dt><dd>sur devis gratuit, déplacement inclus</dd>
</dl>
<h2>Nos prestations ${aV(c.name)}</h2>
<ul class="check cols">${services.map((s) => `<li><a href="../prestations/${s.slug}.html">${s.nav}</a></li>`).join("")}</ul>
<h2>Un nettoyage complet, de la cuisine jusqu'au toit</h2>
<p>Nous ne nous contentons pas des filtres. À ${c.name} comme ailleurs, nous traitons l'ensemble du circuit d'extraction : la hotte, les filtres à chicanes, le plénum, le conduit par ses trappes de visite et la tourelle ou le caisson d'extraction. C'est ce qu'impose le règlement de sécurité incendie pour les établissements recevant du public, au minimum une fois par an.</p>
<h2>Particuliers ${aV(c.name)}</h2>
<p>Votre hotte domestique aspire mal ou sent la graisse ? Nous la démontons, la dégraissons et la remontons, et nous pouvons nettoyer toute votre cuisine dans la foulée. Découvrez le <a href="../prestations/nettoyage-hotte-particulier.html">nettoyage de hotte pour particuliers</a>.</p>
<h2>Comment réserver</h2>
<p>Réservez en ligne en deux minutes, appelez-nous au <a href="tel:${SITE.tel}">${SITE.phone}</a> (${SITE.hours}) ou demandez un devis gratuit avec photos de votre installation.</p>
<p><a class="btn" href="../reservation.html${q}">${ico("calendar")}Réserver une intervention</a> <a class="btn btn-outline" href="../devis.html">Demander un devis</a></p>
</div>
<div class="mt2">${stepsHtml(methodSteps.slice(1, 7).map(([t, x]) => [t, x]), "g2")}</div>
<h2 class="mt3">Questions fréquentes ${aV(c.name)}</h2>${faqHtml(faq)}
<h2 class="mt3">Nous intervenons aussi près ${deV(c.name)}</h2>
<ul class="pill-list">${near.map((x) => `<li><a href="{r}villes/nettoyage-hotte-${x.slug}.html">${x.name}</a></li>`).join("")}<li><a href="{r}zones/${d.slug}.html">Tout le département ${d.code}</a></li></ul>
<div class="zone-map mt2">${zoneMap({ highlight: c.slug, labels: false })}</div>
</article>${sidebar()}</div></section>${ctaBand(`Nettoyage de hotte ${esc(aV(c.name))}`, "Devis gratuit sous 24 h, intervention hors service, certificat remis. Un technicien vous répond.", q)}`,
      priority: 0.6,
      jsonld: [
        { "@context": "https://schema.org", "@type": "Service", name: `Nettoyage de hotte ${aV(c.name)}`, serviceType: "Nettoyage et dégraissage de hotte de cuisine", provider: { "@id": SITE.url + "/#business", ...provider }, areaServed: { "@type": "City", name: c.name, geo: { "@type": "GeoCoordinates", latitude: c.lat, longitude: c.lon } } },
        faqLd(faq)
      ]
    });
  });
}

function corePages() {
  /* Savoir-faire */
  layout({
    path: "notre-savoir-faire.html",
    section: "savoir",
    title: "Notre savoir-faire : techniciens formés et diplômés | Clairvent",
    desc: "Clairvent, ce sont des techniciens formés et diplômés dans les métiers de la propreté, spécialisés dans le dégraissage d'extraction. Découvrez notre équipe et nos engagements.",
    h1: "Un savoir-faire qui se voit, des diplômes qui se vérifient",
    lead: "Le nettoyage d'une extraction de cuisine est un métier technique. Nous l'avons choisi comme unique spécialité, et nous l'exerçons avec des personnes formées et diplômées.",
    crumbs: [["Notre savoir-faire", "notre-savoir-faire.html"]],
    body: `${trustStrip()}
<section class="section"><div class="container split">
<div><span class="eyebrow">Pourquoi Clairvent</span><h2>Une spécialité, pas une ligne de catalogue</h2>
<p>Beaucoup d'entreprises de nettoyage proposent le dégraissage de hotte parmi cinquante autres prestations. Chez Clairvent, c'est notre métier : les hottes, l'extraction et les cuisines. Rien d'autre.</p>
<p>Cette spécialisation change tout : nos techniciens connaissent les types de hottes, de conduits et d'extracteurs, les graisses propres à chaque cuisine, les produits compatibles avec chaque matériau, et les points que regardent un préventionniste ou un expert d'assurance.</p>
<ul class="check"><li>Des techniciens diplômés des métiers de la propreté</li><li>Des formations sécurité à jour : hauteur, chimique, électrique, secourisme</li><li>Une formation à l'hygiène alimentaire pour intervenir en cuisine</li><li>Un protocole interne identique sur chaque chantier</li><li>Un contrôle qualité et un dossier photo systématiques</li></ul></div>
<div class="photo reveal"><img src="{r}assets/photos/intervention-1.webp" alt="Technicien Clairvent constatant l'encrassement d'un équipement de cuisine professionnelle" loading="lazy" width="620" height="826"></div>
</div></section>
<section class="section section-alt"><div class="container"><div class="section-head center"><span class="eyebrow">Diplômes & formations</span><h2>Ce que savent nos techniciens</h2><p>Chaque intervention est réalisée par des personnes formées et diplômées dans le nettoyage, qui ont complété leur parcours par des formations spécifiques à notre métier.</p></div>${credGrid()}</div></section>
<section class="section"><div class="container split" style="align-items:start">
<div><span class="eyebrow">Nos engagements</span><h2>Ce que nous vous promettons, par écrit</h2>
<ol class="steps">
<li><h3>Le circuit complet</h3><p>Hotte, filtres, plénum, conduit et extracteur : rien n'est laissé de côté, et ce qui est inaccessible est écrit.</p></li>
<li><h3>La transparence</h3><p>Photos avant / après à chaque trappe, certificat honnête avec réserves.</p></li>
<li><h3>Votre activité d'abord</h3><p>Nous intervenons quand vous êtes fermés, et nous rendons une cuisine prête pour le service.</p></li>
<li><h3>La reprise</h3><p>Si un point n'est pas conforme à ce qui était prévu, nous revenons le reprendre sans frais.</p></li>
</ol></div>
<div><span class="eyebrow">Notre matériel</span><h2>Des outils de professionnels</h2>
<ul class="check"><li>Brosses rotatives pour conduits circulaires et rectangulaires</li><li>Raclettes et grattoirs inox pour les dépôts épais</li><li>Canons à mousse pour dégraissants à temps de pose</li><li>Bacs de trempage chauffés pour les filtres</li><li>Nettoyeurs vapeur et haute pression selon l'accès</li><li>Aspirateurs eau et poussière, bâches de protection</li><li>Équipements de protection contre les chutes pour la toiture</li><li>Appareils photo pour le dossier avant / après</li></ul>
<p><a class="btn" href="{r}methode.html">Découvrir notre méthode</a></p></div>
</div></section>
${ctaBand("Confiez votre extraction à des spécialistes")}`
  });

  /* Méthode */
  layout({
    path: "methode.html",
    section: "savoir",
    title: "Notre méthode de dégraissage de hotte en 8 étapes | Clairvent",
    desc: "Découvrez le protocole Clairvent de nettoyage d'extraction de cuisine en 8 étapes et explorez notre schéma interactif : hotte, filtres, plénum, conduit, tourelle.",
    h1: "Notre méthode en 8 étapes",
    lead: "Un protocole identique sur chaque chantier, du premier appel à la remise du certificat. Explorez le schéma pour comprendre ce que nous nettoyons.",
    crumbs: [["Notre méthode", "methode.html"]],
    body: `<section class="section"><div class="container split" style="align-items:start">
<div class="card">${diagram(true)}</div>
<div><h2>Le parcours de la graisse</h2><p>Les vapeurs grasses montent de la cuisson, traversent les filtres, se condensent dans le plénum puis dans le conduit, et finissent sur la turbine de l'extracteur. Pour dégraisser efficacement, il faut suivre ce parcours jusqu'au bout.</p><p>Touchez chaque point orange du schéma pour découvrir comment nous traitons chacun des éléments.</p><p><a class="btn btn-outline" href="{r}conseils/anatomie-systeme-extraction-cuisine.html">Comprendre votre système d'extraction</a></p></div>
</div></section>
<section class="section section-alt"><div class="container">${stepsHtml(methodSteps, "g2")}</div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="prose">
<h2>Les procédés que nous utilisons</h2>
<table><thead><tr><th>Procédé</th><th>Usage</th></tr></thead><tbody>
<tr><td>Grattage manuel</td><td>Dépôts épais, croûteux ou carbonisés, avant tout traitement chimique</td></tr>
<tr><td>Mousse dégraissante alcaline</td><td>Surfaces verticales et plafonds (plénum, parois de conduit), grâce au temps de contact</td></tr>
<tr><td>Brossage rotatif</td><td>Intérieur des conduits circulaires et rectangulaires, par les trappes</td></tr>
<tr><td>Trempage à chaud</td><td>Filtres à chicanes et pièces démontables</td></tr>
<tr><td>Vapeur sèche</td><td>Finitions et zones sensibles à l'eau</td></tr>
<tr><td>Haute pression maîtrisée</td><td>Turbines et zones extérieures, avec récupération des eaux</td></tr>
</tbody></table>
<h2>Sécurité et environnement</h2>
<p>Consignation électrique systématique, équipements de protection, protections antichute en toiture. Les eaux grasses et les résidus sont récupérés et ne sont pas rejetés dans les évacuations pluviales. Les produits sont dosés au plus juste et rincés des surfaces en contact alimentaire.</p>
</div></div></section>${ctaBand()}`
  });

  /* Réglementation */
  const regFaq = [
    ["La fréquence d'un an est-elle obligatoire pour tous les restaurants ?", "Pour les établissements recevant du public, le règlement de sécurité incendie prévoit un nettoyage au minimum annuel de l'installation d'extraction. D'autres obligations (Code du travail, assurance, bail) peuvent s'appliquer aux locaux ne recevant pas de public."],
    ["Qui contrôle ?", "La commission de sécurité lors de ses visites périodiques, les services sanitaires pour l'hygiène, et l'expert de l'assureur en cas de sinistre."],
    ["Que risque-t-on sans certificat ?", "Une observation ou un avis défavorable de la commission de sécurité, une mise en demeure en cas de contrôle sanitaire défavorable et, en cas de sinistre, une possible réduction ou un refus d'indemnisation selon votre contrat."]
  ];
  layout({
    path: "reglementation.html",
    section: "savoir",
    title: "Réglementation du nettoyage de hotte professionnelle | Clairvent",
    desc: "Article GC 21 du règlement de sécurité ERP, hygiène alimentaire, Code du travail, assurance : la réglementation du nettoyage des hottes et conduits expliquée simplement.",
    h1: "Réglementation : ce que vous devez savoir",
    lead: "Sécurité incendie, hygiène, droit du travail, assurance : quatre raisons de faire dégraisser votre extraction, et les textes qui les encadrent.",
    crumbs: [["Réglementation", "reglementation.html"]],
    body: `<section class="section"><div class="container with-sidebar"><article><div class="prose">
<h2>1. La sécurité incendie (ERP)</h2>
<p>Le règlement de sécurité contre les risques d'incendie et de panique dans les établissements recevant du public, fixé par l'arrêté du 25 juin 1980, consacre une section aux grandes cuisines (articles GC). L'<strong>article GC 21</strong> prévoit que l'installation d'extraction — conduits, filtres, extracteurs — soit nettoyée <strong>au minimum une fois par an</strong>. Le nettoyage doit couvrir l'ensemble du circuit.</p>
<h2>2. L'hygiène alimentaire</h2>
<p>Le règlement (CE) n° 852/2004 impose que les locaux et équipements soient propres et bien entretenus. Une hotte qui goutte, un plafond gras ou des filtres saturés peuvent être relevés lors d'une inspection sanitaire et figurer dans votre plan de nettoyage et de désinfection.</p>
<h2>3. Le Code du travail</h2>
<p>L'employeur doit maintenir les installations d'aération et d'assainissement des locaux de travail en bon état de fonctionnement et prévenir le risque incendie. Cette obligation s'applique à toutes les cuisines professionnelles, y compris celles qui ne reçoivent pas de public (dark kitchens, laboratoires).</p>
<h2>4. L'assurance et le bail</h2>
<p>Votre contrat d'assurance peut prévoir une fréquence d'entretien et exiger des justificatifs. Votre bail commercial précise la répartition des charges d'entretien. En cas de sinistre, l'expert vérifiera les certificats.</p>
<h2>5. Les références techniques</h2>
<p>La norme <a href="{r}conseils/norme-nf-en-16282-ventilation-cuisine.html">NF EN 16282</a> fournit un cadre technique pour la ventilation des cuisines professionnelles, notamment l'accessibilité pour le nettoyage.</p>
<div class="callout"><svg class="ico"><use href="#i-info"/></svg><p>Cette page est un résumé pratique. Elle ne remplace pas les textes officiels, disponibles sur Légifrance, ni l'avis de votre préventionniste, de votre bureau de contrôle ou de votre assureur.</p></div>
</div>
<h2 class="mt3">Questions fréquentes</h2>${faqHtml(regFaq)}
<h2 class="mt3">Pour aller plus loin</h2><div class="grid g3">${["reglementation-nettoyage-hotte-erp", "certificat-nettoyage-hotte-assurance", "registre-securite-cuisine-erp"].map((s) => guideCard(guideBySlug[s])).join("")}</div>
</article>${sidebar()}</div></section>${ctaBand("Mettez votre extraction en conformité")}`,
    jsonld: [faqLd(regFaq)]
  });

  /* Certificat */
  layout({
    path: "certificat-de-degraissage.html",
    section: "savoir",
    title: "Le certificat de dégraissage de hotte Clairvent | Clairvent",
    desc: "Découvrez le certificat de nettoyage de hotte et de conduit remis par Clairvent : contenu, photos, réserves. Le document attendu par votre assureur et la commission de sécurité.",
    h1: "Le certificat de dégraissage",
    lead: "Remis à chaque intervention, il prouve que votre extraction a été réellement nettoyée, dit ce qui a été fait et ce qui reste à faire.",
    crumbs: [["Certificat de dégraissage", "certificat-de-degraissage.html"]],
    body: `<section class="section"><div class="container split" style="align-items:start">
<div class="certif">
<h3>Certificat de nettoyage d'installation d'extraction</h3>
<p style="color:#6b5a3e">N° CV-AAAA-NNNN · Document spécimen</p>
<table><tbody>
<tr><th>Établissement</th><td>Nom, adresse, type d'activité</td></tr>
<tr><th>Date et horaires</th><td>JJ/MM/AAAA, de 23 h 00 à 03 h 30</td></tr>
<tr><th>Technicien(s)</th><td>Nom, qualification</td></tr>
<tr><th>Hotte</th><td>Longueur, état initial, dégraissage intérieur et extérieur</td></tr>
<tr><th>Filtres</th><td>Nombre, type, état, trempage</td></tr>
<tr><th>Plénum</th><td>Grattage, dégraissage</td></tr>
<tr><th>Conduit</th><td>Longueur traitée, nombre de trappes, état initial</td></tr>
<tr><th>Extracteur</th><td>Type, dégraissage de la turbine, observations</td></tr>
<tr><th>Réserves</th><td>Zones inaccessibles, trappes à poser, anomalies</td></tr>
<tr><th>Recommandation</th><td>Prochain passage conseillé</td></tr>
</tbody></table>
<p style="color:#6b5a3e;margin:0">Annexe : dossier photo avant / après · Signature du technicien et du client</p>
</div>
<div><h2>Ce qui rend notre certificat fiable</h2>
<ul class="check"><li>Il n'est délivré qu'après une intervention réelle de nos techniciens.</li><li>Il détaille chaque élément du circuit, pas une mention vague « hotte nettoyée ».</li><li>Il indique honnêtement les zones inaccessibles.</li><li>Il est accompagné de photos avant / après prises à chaque trappe.</li><li>Il est signé, daté et envoyé en PDF pour votre registre de sécurité.</li><li>Il propose une date pour le prochain passage.</li></ul>
<h2>À qui le présenter ?</h2><p>À la commission de sécurité lors de ses visites, à votre assureur à sa demande ou après un sinistre, à votre bailleur ou à votre syndic de copropriété s'ils le demandent, et à un repreneur en cas de cession.</p>
<p><a class="btn" href="{r}prestations/certificat-degraissage-hotte.html">La prestation certificat</a> <a class="btn btn-outline" href="{r}conseils/certificat-nettoyage-hotte-assurance.html">Le certificat et l'assurance</a></p></div>
</div></section>${ctaBand("Besoin d'un certificat à jour ?")}`
  });

  /* Réalisations */
  layout({
    path: "realisations.html",
    section: "savoir",
    title: "Nos réalisations : avant / après en cuisine professionnelle | Clairvent",
    desc: "Photos avant / après d'interventions réelles de nettoyage en cuisine professionnelle : inox, plans de travail, équipements, réfrigération.",
    h1: "Nos réalisations",
    lead: "Chaque paire de photos provient d'une même intervention réelle, prise au même endroit avant et après notre passage. Pas de banque d'images.",
    crumbs: [["Réalisations", "realisations.html"]],
    body: `<section class="section"><div class="container">
<div class="grid g2">
<div class="card"><div class="ba"><figure><img src="{r}assets/photos/avant-plan-travail.webp" alt="Plan de travail inox encrassé avant intervention" loading="lazy"><figcaption>Avant</figcaption></figure><figure><img src="{r}assets/photos/apres-plan-travail.webp" alt="Plan de travail inox après dégraissage" loading="lazy"><figcaption>Après</figcaption></figure></div><h3 class="mt1">Plan de travail inox — commerce de bouche</h3><p>Dégraissage, rinçage et essuyage dans le sens du grain de l'inox.</p></div>
<div class="card"><div class="ba"><figure><img src="{r}assets/photos/avant-frigo.webp" alt="Équipement réfrigéré encrassé avant nettoyage" loading="lazy"><figcaption>Avant</figcaption></figure><figure><img src="{r}assets/photos/apres-frigo.webp" alt="Équipement réfrigéré après nettoyage et désinfection" loading="lazy"><figcaption>Après</figcaption></figure></div><h3 class="mt1">Réfrigération — nettoyage et désinfection</h3><p>Nettoyage des parois, des clayettes et des joints, puis désinfection.</p></div>
</div>
<div class="split mt3"><div class="photo"><img src="{r}assets/photos/intervention-1.webp" alt="Dépôt gras accumulé sous un équipement de cuisine professionnelle" loading="lazy"></div><div><h2>Ce que l'on trouve sous les équipements</h2><p>Cette photo a été prise au démontage d'un équipement de cuisine professionnelle : un mélange de graisse et de résidus accumulé là où le nettoyage quotidien ne va jamais. C'est exactement ce que traite notre <a href="{r}prestations/nettoyage-cuisine-professionnelle.html">nettoyage de cuisine professionnelle</a>.</p><p>Pour les hottes et les conduits, chaque intervention donne lieu à un dossier photo remis avec le certificat. Par respect pour nos clients, ces dossiers ne sont pas publiés sans leur accord.</p></div></div>
</div></section>${ctaBand()}`
  });

  /* Diagnostic */
  layout({
    path: "diagnostic.html",
    section: "savoir",
    title: "Diagnostic gratuit : fréquence de dégraissage et conformité | Clairvent",
    desc: "Outil gratuit : calculez la fréquence de dégraissage adaptée à votre hotte et faites l'auto-diagnostic de conformité de votre installation d'extraction.",
    h1: "Diagnostic gratuit de votre extraction",
    lead: "Deux outils en ligne, sans inscription : estimez la fréquence de dégraissage adaptée à votre cuisine, puis vérifiez les points clés de votre conformité.",
    crumbs: [["Diagnostic", "diagnostic.html"]],
    body: `<section class="section"><div class="container split" style="align-items:start">
<div><h2>1. Quelle fréquence de dégraissage ?</h2><p>Répondez à quatre questions sur votre cuisine. L'estimation s'appuie sur le minimum réglementaire et sur les pratiques professionnelles courantes ; elle ne remplace pas une visite technique.</p>${freqTool()}</div>
<div><h2>2. Votre installation est-elle en règle ?</h2><p>Cochez les affirmations vraies pour votre établissement.</p>
<div class="tool"><form data-conform-tool data-devis="{r}devis.html" class="form">
${[
      "J'ai un certificat de dégraissage de moins de 12 mois",
      "Ce certificat couvre hotte, filtres, conduit ET extracteur",
      "Mes filtres sont à chicanes, en bon état, et nettoyés chaque semaine",
      "Aucune graisse ne goutte de la hotte ni ne coule en toiture",
      "Mon conduit dispose de trappes de visite accessibles",
      "Le registre de sécurité est à jour et disponible",
      "J'ai un extincteur adapté aux feux d'huiles près des postes de cuisson",
      "Mon équipe connaît les gestes en cas de feu de friteuse"
    ].map((t, i) => `<label class="choice"><input type="checkbox" name="c${i}"><span>${t}</span></label>`).join("")}
<button class="btn" type="submit">${ico("shield")}Voir mon score</button></form><div class="tool-result" aria-live="polite"></div></div></div>
</div></section>${ctaBand("Faites le point avec un technicien")}`,
    scripts: []
  });

  /* FAQ */
  const faqAll = [
    ...homeFaq,
    ["Quelle est la différence entre ramonage et dégraissage ?", "Le ramonage concerne les conduits de fumée (four à bois, chaudière) et élimine les suies. Le dégraissage concerne l'extraction des hottes de cuisine et élimine les graisses. Ce sont deux opérations et deux certificats distincts."],
    ["Nettoyez-vous les conduits sans trappes de visite ?", "Nous nettoyons tout ce qui est accessible depuis la hotte et l'extracteur, et nous indiquons honnêtement sur le certificat les zones non accessibles, avec nos recommandations de pose de trappes."],
    ["Faut-il être présent pendant l'intervention ?", "Pas nécessairement. Pour une première intervention, nous recommandons qu'un responsable soit présent au début et à la fin. Ensuite, un accès convenu (clés, code, gardien) suffit."],
    ["Vos produits sont-ils dangereux pour la cuisine ?", "Nous utilisons des produits professionnels, dosés et rincés des surfaces en contact alimentaire. La cuisine est rendue propre et utilisable dès la fin de l'intervention."],
    ["Pouvez-vous refaire un nettoyage de cuisine mal fait par un autre prestataire ?", "Oui, c'est notre prestation de remise en état : constat initial, nettoyage complet, et réception avec vous sur la base du constat."],
    ["Quels moyens de paiement acceptez-vous ?", "Virement, chèque et carte bancaire. Les conditions de règlement sont précisées sur le devis."],
    ["Êtes-vous assurés ?", "Oui, nous sommes assurés en responsabilité civile professionnelle. L'attestation est disponible sur simple demande."],
    ["Intervenez-vous en urgence ?", "En cas d'urgence (avant un contrôle, après un départ de feu, odeur ou fumée anormale), appelez-nous directement : nous faisons le maximum pour intervenir sous quelques jours, y compris la nuit et le week-end."]
  ];
  layout({
    path: "faq.html",
    section: "savoir",
    title: "Questions fréquentes sur le nettoyage de hotte | Clairvent",
    desc: "Prix, fréquence, certificat, déroulement, qualifications, urgence : toutes les réponses à vos questions sur le nettoyage de hotte et de cuisine.",
    h1: "Questions fréquentes",
    lead: "Les réponses aux questions que l'on nous pose le plus souvent. Vous ne trouvez pas la vôtre ? Appelez-nous.",
    crumbs: [["FAQ", "faq.html"]],
    body: `<section class="section"><div class="container" style="max-width:900px">${faqHtml(faqAll)}</div></section>${ctaBand("Une autre question ?", "Un technicien vous répond " + SITE.hours + ".")}`,
    jsonld: [faqLd(faqAll)]
  });

  /* Réservation */
  const presta = services.map((s) => `<label class="choice"><input type="checkbox" name="prestations" value="${esc(s.nav)}" data-slug="${s.slug}"><span>${s.nav}</span></label>`).join("");
  const profils = [["Restaurant", "Traditionnel, brasserie, gastronomique"], ["Restauration rapide", "Fast-food, snack, kebab, friterie"], ["Hôtel", "Restaurant d'hôtel, résidence"], ["Collectivité", "Cantine, restaurant d'entreprise, EHPAD"], ["Boulangerie / traiteur", "Laboratoire, snacking"], ["Dark kitchen / food truck", "Cuisine de livraison, mobile"], ["Particulier", "Hotte ou cuisine à domicile"], ["Autre", "Précisez dans le message"]];
  const radio = (name, list) => list.map(([v, s]) => `<label class="choice"><input type="radio" name="${name}" value="${esc(v)}"><span>${v}${s ? `<small>${s}</small>` : ""}</span></label>`).join("");
  layout({
    path: "reservation.html",
    section: "",
    title: "Réserver un nettoyage de hotte en ligne | Clairvent",
    desc: "Réservez en ligne votre nettoyage de hotte ou de cuisine en 5 étapes : prestation, installation, date et créneau, coordonnées. Confirmation et devis sous 24 h.",
    h1: "Réserver une intervention",
    lead: "Cinq étapes, deux minutes. Choisissez votre prestation, votre date et votre créneau : un technicien vous rappelle pour confirmer et vous envoie votre devis gratuit sous 24 h ouvrées.",
    crumbs: [["Réservation", "reservation.html"]],
    scripts: ["assets/js/reservation.js"],
    body: `<section class="section"><div class="container">
<noscript><div class="notice"><p>La réservation en ligne nécessite JavaScript. Vous pouvez <a href="devis.html">demander un devis</a> ou nous appeler au <a href="tel:${SITE.tel}">${SITE.phone}</a>.</p></div></noscript>
<div class="resa" id="resa" hidden>
<div class="resa-card">
<ol class="resa-steps">${["Prestation", "Installation", "Date", "Coordonnées", "Validation"].map((t, i) => `<li><button type="button"><span>${i + 1}</span>${t}</button></li>`).join("")}</ol>
<form id="resa-form" action="${SITE.form}" method="POST" novalidate>
<input type="hidden" name="_subject" value="Nouvelle réservation — ${SITE.name}">
<input type="hidden" name="_next" value="${SITE.url}/merci.html">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="Récapitulatif" id="resa-recap">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
<div class="resa-panel" data-step="1">
<h2>Quel est votre établissement ?</h2>
<div class="choice-grid">${radio("profil", profils)}</div>
<p class="sub-q">Quelles prestations souhaitez-vous ? <small class="muted">(plusieurs choix possibles)</small></p>
<div class="choice-grid">${presta}</div>
</div>
<div class="resa-panel" data-step="2" hidden>
<h2>Parlez-nous de votre installation</h2>
<p class="muted">Ces informations nous aident à préparer l'intervention. Répondez « je ne sais pas » si besoin : nous verrons ensemble.</p>
<div class="form-row">
<div><label for="r-nb">Nombre de hottes</label><select id="r-nb" name="nb_hottes"><option>1</option><option>2</option><option>3</option><option>4 ou plus</option><option>Je ne sais pas</option></select></div>
<div><label for="r-long">Longueur de la hotte principale</label><select id="r-long" name="longueur"><option>Moins de 2 m</option><option>2 à 4 m</option><option>4 à 6 m</option><option>Plus de 6 m</option><option>Hotte domestique</option><option>Je ne sais pas</option></select></div>
</div>
<div class="form-row mt1">
<div><label for="r-acces">Accès à l'extracteur</label><select id="r-acces" name="acces"><option>Toiture accessible (escalier, trappe)</option><option>Toiture difficile d'accès</option><option>Caisson en local technique / combles</option><option>Je ne sais pas</option></select></div>
<div><label for="r-dernier">Dernier dégraissage complet</label><select id="r-dernier" name="dernier"><option>Moins de 6 mois</option><option>6 à 12 mois</option><option>Plus d'un an</option><option>Jamais / je ne sais pas</option></select></div>
</div>
<div class="mt1"><label for="r-msg">Précisions <small>(type de cuisson, contraintes d'accès, urgence…)</small></label><textarea id="r-msg" name="message" placeholder="Ex. : friture et grill, conduit qui traverse 2 étages, fermeture le lundi…"></textarea></div>
</div>
<div class="resa-panel" data-step="3" hidden>
<h2>Quand souhaitez-vous intervenir ?</h2>
<p class="muted">Choisissez une date indicative : nous la confirmons par téléphone selon nos disponibilités.</p>
<div class="split" style="gap:24px;align-items:start">
<div class="cal" id="resa-cal"><div class="cal-head"><button type="button" data-cal-prev aria-label="Mois précédent">‹</button><strong></strong><button type="button" data-cal-next aria-label="Mois suivant">›</button></div><div class="cal-grid"></div></div>
<div><input type="hidden" name="date" id="r-date">
<label class="choice"><input type="checkbox" id="r-flex" name="flexible" value="Oui"><span>Je suis flexible<small>Proposez-moi la première date disponible</small></span></label>
<p class="sub-q">Créneau souhaité</p>
<div class="slots">${radio("creneau", [["Tôt le matin", "6 h – 10 h"], ["Entre deux services", "15 h – 18 h"], ["Après le service", "22 h – 3 h"], ["Jour de fermeture", "Journée complète"], ["En journée", "Particuliers, 8 h – 20 h"]])}</div></div>
</div>
</div>
<div class="resa-panel" data-step="4" hidden>
<h2>Vos coordonnées</h2>
<div class="form">
<div class="form-row"><div><label for="r-nom">Nom et prénom *</label><input id="r-nom" type="text" name="nom" required data-label="votre nom" autocomplete="name"></div><div><label for="r-soc">Établissement / société</label><input id="r-soc" type="text" name="societe" autocomplete="organization"></div></div>
<div class="form-row"><div><label for="r-tel">Téléphone *</label><input id="r-tel" type="tel" name="tel" required data-label="votre téléphone" autocomplete="tel" pattern="[0-9 +().-]{9,}"></div><div><label for="r-mail">E-mail *</label><input id="r-mail" type="email" name="email" required data-label="votre e-mail" autocomplete="email"></div></div>
<div><label for="r-adr">Adresse de l'intervention</label><input id="r-adr" type="text" name="adresse" autocomplete="street-address"></div>
<div class="form-row"><div><label for="r-cp">Code postal *</label><input id="r-cp" type="text" name="cp" required data-label="le code postal" inputmode="numeric" pattern="[0-9]{5}" autocomplete="postal-code"></div><div><label for="r-ville">Ville *</label><input id="r-ville" type="text" name="ville" required data-label="la ville" autocomplete="address-level2"></div></div>
</div>
</div>
<div class="resa-panel" data-step="5" hidden>
<h2>Vérifiez et envoyez</h2>
<dl class="kv" id="resa-recap-view" style="background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:16px 20px"></dl>
<label class="choice mt2"><input type="checkbox" id="r-rgpd" name="consentement" value="Oui"><span>J'accepte d'être recontacté par ${SITE.name} pour confirmer ce rendez-vous<small>Vos données servent uniquement à traiter votre demande. <a href="confidentialite.html">Confidentialité</a></small></span></label>
<p class="form-note mt1">Rien n'est dû à ce stade : la réservation devient définitive après notre appel de confirmation et l'acceptation du devis.</p>
</div>
<p class="resa-error" id="resa-error" role="alert" style="padding:0 30px"></p>
<div class="resa-nav"><button type="button" class="btn btn-outline" id="resa-prev">← Retour</button><button type="button" class="btn" id="resa-next">Continuer →</button><button type="submit" class="btn" id="resa-submit" hidden>${ico("check")}Envoyer ma réservation</button></div>
</form>
</div>
<aside class="summary widget widget-cta"><h3>Votre réservation</h3><dl><dt>Établissement</dt><dd id="s-profil">—</dd><dt>Prestations</dt><dd id="s-presta">—</dd><dt>Date &amp; créneau</dt><dd id="s-date">—</dd><dt>Lieu</dt><dd id="s-lieu">—</dd><dt>Prix</dt><dd>Sur devis gratuit, envoyé sous 24 h</dd></dl>
<div class="quote-note">${ico("phone")} Plus rapide ? <a href="tel:${SITE.tel}" style="color:#fff;font-weight:700">${SITE.phone}</a><br>${SITE.hours}</div></aside>
</div></div></section>
<section class="section section-alt"><div class="container"><div class="grid g3">
<div class="card"><span class="card-icon">${ico("phone")}</span><h3>1. Nous vous rappelons</h3><p>Un technicien vous appelle pour confirmer la date, le créneau et les détails de votre installation.</p></div>
<div class="card"><span class="card-icon">${ico("doc")}</span><h3>2. Vous recevez le devis</h3><p>Devis gratuit, ferme et détaillé sous 24 h ouvrées. Aucun engagement avant acceptation.</p></div>
<div class="card"><span class="card-icon">${ico("shield")}</span><h3>3. Nous intervenons</h3><p>Au créneau convenu, sans interrompre vos services. Certificat et photos remis à la fin.</p></div>
</div></div></section>`
  });

  /* Devis */
  layout({
    path: "devis.html",
    section: "",
    title: "Devis gratuit nettoyage de hotte et cuisine | Clairvent",
    desc: "Demandez votre devis gratuit de nettoyage de hotte, de conduit d'extraction ou de cuisine. Réponse sous 24 h ouvrées, visite technique gratuite en Île-de-France.",
    h1: "Demander un devis gratuit",
    lead: "Décrivez votre besoin, ajoutez quelques photos si vous le pouvez : vous recevez un devis ferme et détaillé sous 24 heures ouvrées.",
    crumbs: [["Devis gratuit", "devis.html"]],
    body: `<section class="section"><div class="container with-sidebar"><div class="card" style="padding:32px">
<form class="form" action="${SITE.form}" method="POST" enctype="multipart/form-data">
<input type="hidden" name="_subject" value="Demande de devis — ${SITE.name}">
<input type="hidden" name="_next" value="${SITE.url}/merci.html">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_template" value="table">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
<div class="form-row"><div><label for="d-nom">Nom et prénom *</label><input id="d-nom" type="text" name="Nom" required autocomplete="name"></div><div><label for="d-soc">Établissement</label><input id="d-soc" type="text" name="Établissement" autocomplete="organization"></div></div>
<div class="form-row"><div><label for="d-tel">Téléphone *</label><input id="d-tel" type="tel" name="Téléphone" required autocomplete="tel"></div><div><label for="d-mail">E-mail *</label><input id="d-mail" type="email" name="email" required autocomplete="email"></div></div>
<div class="form-row"><div><label for="d-cp">Code postal *</label><input id="d-cp" type="text" name="Code postal" required inputmode="numeric" pattern="[0-9]{5}"></div><div><label for="d-type">Vous êtes</label><select id="d-type" name="Profil"><option>Restaurant / restauration commerciale</option><option>Restauration collective / santé</option><option>Hôtel</option><option>Boulangerie / traiteur / laboratoire</option><option>Dark kitchen / food truck</option><option>Particulier</option><option>Syndic / gestionnaire</option></select></div></div>
<div><label>Prestations souhaitées</label><div class="choice-grid">${services.map((s) => `<label class="choice"><input type="checkbox" name="Prestations[]" value="${esc(s.nav)}"><span>${s.nav}</span></label>`).join("")}</div></div>
<div><label for="d-msg">Votre besoin *</label><textarea id="d-msg" name="Message" required placeholder="Type de cuisine, taille de la hotte, longueur approximative du conduit, date souhaitée…"></textarea></div>
<div><label for="d-photos">Photos de votre installation <small>(facultatif : hotte, filtres, extracteur)</small></label><input id="d-photos" type="file" name="attachment" accept="image/*"></div>
<label class="choice"><input type="checkbox" name="Consentement" value="Oui" required><span>J'accepte d'être recontacté au sujet de ma demande *<small><a href="confidentialite.html">Politique de confidentialité</a></small></span></label>
<button class="btn btn-lg" type="submit">${ico("mail")}Envoyer ma demande de devis</button>
<p class="form-note">Réponse sous 24 h ouvrées. Devis gratuit et sans engagement.</p>
</form></div>
${sidebar()}</div></section>`
  });

  /* Contact */
  layout({
    path: "contact.html",
    section: "contact",
    title: "Contact : appelez un technicien Clairvent | Clairvent",
    desc: `Contactez Clairvent au ${SITE.phone} (${SITE.hours}) ou via notre formulaire. Nettoyage de hotte et de cuisine en Île-de-France, base ${SITE.au}.`,
    h1: "Nous joindre",
    lead: "Le plus simple, c'est de nous appeler : un technicien vous répond directement, sans standard ni plateforme.",
    crumbs: [["Contact", "contact.html"]],
    jsonld: [{ "@context": "https://schema.org", ...provider }],
    body: `<section class="section"><div class="container">
<div class="grid g3">
<a class="card card-link" href="tel:${SITE.tel}"><span class="card-icon">${ico("phone")}</span><h3>Par téléphone</h3><p style="font-size:1.5rem;font-weight:800;color:var(--ink)">${SITE.phone}</p><p>${SITE.hours}. Réponse directe d'un technicien.</p><span class="more">Appeler ${ico("arrow")}</span></a>
<a class="card card-link" href="{r}reservation.html"><span class="card-icon">${ico("calendar")}</span><h3>Réserver en ligne</h3><p>Choisissez votre prestation, votre date et votre créneau en deux minutes.</p><span class="more">Réserver ${ico("arrow")}</span></a>
<a class="card card-link" href="{r}ou-nous-trouver.html"><span class="card-icon">${ico("pin")}</span><h3>Où nous trouver</h3><p>Base ${SITE.au} (${SITE.cp}), interventions dans toute l'Île-de-France.</p><span class="more">Voir la carte ${ico("arrow")}</span></a>
</div>
<div class="split mt3" style="align-items:start">
<div class="card" style="padding:32px"><h2>Écrivez-nous</h2>
<form class="form" action="${SITE.form}" method="POST">
<input type="hidden" name="_subject" value="Message de contact — ${SITE.name}">
<input type="hidden" name="_next" value="${SITE.url}/merci.html">
<input type="hidden" name="_captcha" value="false">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
<div class="form-row"><div><label for="c-nom">Nom *</label><input id="c-nom" type="text" name="Nom" required autocomplete="name"></div><div><label for="c-tel">Téléphone</label><input id="c-tel" type="tel" name="Téléphone" autocomplete="tel"></div></div>
<div><label for="c-mail">E-mail *</label><input id="c-mail" type="email" name="email" required autocomplete="email"></div>
<div><label for="c-sujet">Sujet</label><select id="c-sujet" name="Sujet"><option>Question sur une prestation</option><option>Demande de rappel</option><option>Contrat d'entretien</option><option>Urgence</option><option>Autre</option></select></div>
<div><label for="c-msg">Message *</label><textarea id="c-msg" name="Message" required></textarea></div>
<label class="choice"><input type="checkbox" name="Consentement" value="Oui" required><span>J'accepte d'être recontacté au sujet de ma demande *</span></label>
<button class="btn" type="submit">Envoyer</button>
</form></div>
<div><h2>Informations pratiques</h2>
<dl class="kv"><dt>Téléphone</dt><dd><a href="tel:${SITE.tel}">${SITE.phone}</a></dd><dt>Standard</dt><dd>${SITE.hours}</dd><dt>Interventions</dt><dd>7j/7, de jour comme de nuit, sur rendez-vous</dd><dt>Base</dt><dd>${SITE.cp} ${SITE.city}</dd><dt>Zone</dt><dd>Paris et toute l'Île-de-France</dd><dt>Devis</dt><dd>Gratuit, sous 24 h ouvrées</dd></dl>
<div class="callout callout-warn mt2"><svg class="ico"><use href="#i-alert"/></svg><p><strong>Feu en cours ?</strong> Appelez immédiatement le 18 ou le 112. Pour une intervention rapide après un sinistre, contactez-nous ensuite au ${SITE.phone}.</p></div>
</div></div>
</div></section>`
  });

  /* Où nous trouver */
  const bbox = [base.lon - 0.05, base.lat - 0.025, base.lon + 0.05, base.lat + 0.025].map((n) => n.toFixed(4)).join("%2C");
  const byDist = [...cities].map((c) => [c, km(base, c)]).sort((a, b) => a[1] - b[1]);
  layout({
    path: "ou-nous-trouver.html",
    section: "zones",
    title: `Où nous trouver : Clairvent ${SITE.au} (93) | Clairvent`,
    desc: `Clairvent est basé ${SITE.au} (${SITE.cp}), en Seine-Saint-Denis. Carte, accès, zone d'intervention et distances vers les villes d'Île-de-France.`,
    h1: `Basés ${SITE.au}, au service de toute l'Île-de-France`,
    lead: "Notre base technique est située au nord-est de Paris, à proximité immédiate de l'A1, de l'A3 et de l'A86 : un point de départ idéal pour rejoindre rapidement Paris et toute la région.",
    crumbs: [["Où nous trouver", "ou-nous-trouver.html"]],
    jsonld: [{ "@context": "https://schema.org", ...provider }],
    body: `<section class="section"><div class="container split" style="align-items:start">
<div><iframe class="map-frame" title="Carte : ${SITE.city}" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=${bbox}&amp;layer=mapnik&amp;marker=${base.lat}%2C${base.lon}"></iframe>
<p class="form-note">Carte © contributeurs OpenStreetMap. <a href="https://www.openstreetmap.org/?mlat=${base.lat}&amp;mlon=${base.lon}#map=14/${base.lat}/${base.lon}" rel="noopener" target="_blank">Agrandir la carte</a></p></div>
<div class="card" style="padding:28px"><h2>${SITE.name}</h2>
<dl class="kv"><dt>Base</dt><dd>${SITE.cp} ${SITE.city} — Seine-Saint-Denis</dd><dt>Téléphone</dt><dd><a href="tel:${SITE.tel}">${SITE.phone}</a></dd><dt>Standard</dt><dd>${SITE.hours}</dd><dt>Interventions</dt><dd>Sur site uniquement, jour et nuit</dd><dt>Accès routiers</dt><dd>A1, A3, A86, N2</dd><dt>À proximité</dt><dd>Paris (15 min hors trafic), aéroports de Roissy et du Bourget</dd></dl>
<div class="callout mt2"><svg class="ico"><use href="#i-info"/></svg><p>Nous n'accueillons pas de public : notre base est un dépôt technique. Toutes nos prestations sont réalisées chez vous, dans votre cuisine.</p></div>
<p class="mt2"><a class="btn" href="tel:${SITE.tel}">${ico("phone")}Appeler</a> <a class="btn btn-outline" href="{r}reservation.html">Réserver</a></p></div>
</div></section>
<section class="section section-alt"><div class="container split" style="align-items:start">
<div class="zone-map">${zoneMap()}</div>
<div><h2>Distances depuis notre base</h2><p>Les cercles indiquent 10, 25 et 40 km autour ${SITE.du}. Touchez un point pour voir la page de la ville.</p>
<div style="max-height:460px;overflow:auto;border:1px solid var(--line);border-radius:12px;background:#fff"><table style="width:100%;border-collapse:collapse;font-size:15px"><thead><tr style="position:sticky;top:0;background:var(--bg)"><th style="text-align:left;padding:10px 14px">Ville</th><th style="text-align:left;padding:10px 14px">Dép.</th><th style="text-align:right;padding:10px 14px">Distance</th></tr></thead><tbody>${byDist.map(([c, k]) => `<tr style="border-top:1px solid var(--line)"><td style="padding:8px 14px"><a href="{r}villes/nettoyage-hotte-${c.slug}.html">${c.name}</a></td><td style="padding:8px 14px">${c.dept}</td><td style="padding:8px 14px;text-align:right">≈ ${Math.max(1, Math.round(k))} km</td></tr>`).join("")}</tbody></table></div>
<p class="form-note">Distances à vol d'oiseau, arrondies.</p></div>
</div></section>${ctaBand()}`
  });

  /* Légal */
  layout({
    path: "mentions-legales.html",
    title: "Mentions légales | Clairvent",
    desc: "Mentions légales du site Clairvent : éditeur, hébergement, propriété intellectuelle.",
    h1: "Mentions légales",
    crumbs: [["Mentions légales", "mentions-legales.html"]],
    priority: 0.2,
    body: `<section class="section"><div class="container" style="max-width:900px"><div class="prose">
<h2>Éditeur du site</h2><p>${SITE.name} est une marque exploitée par ${SITE.legal}.<br>Adresse : ${SITE.street}, ${SITE.cp} ${SITE.city}, France<br>SIRET : ${SITE.siret}<br>Téléphone : ${SITE.phone}<br>E-mail : ${SITE.email}<br>Directeur de la publication : Mathéo Céleste</p>
<h2>Hébergement</h2><p>[À compléter avec le nom, l'adresse et le téléphone de votre hébergeur.]</p>
<h2>Propriété intellectuelle</h2><p>L'ensemble des contenus de ce site (textes, schémas, illustrations, photographies) est la propriété de ${SITE.name}, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
<h2>Crédits</h2><p>Carte : © contributeurs OpenStreetMap. Polices : Google Fonts (Plus Jakarta Sans, Fraunces).</p>
<h2>Responsabilité</h2><p>Les informations publiées, notamment réglementaires, sont fournies à titre indicatif. Elles ne remplacent pas les textes officiels ni l'avis d'un professionnel qualifié (préventionniste, bureau de contrôle, assureur).</p>
</div></div></section>`
  });
  layout({
    path: "confidentialite.html",
    title: "Politique de confidentialité | Clairvent",
    desc: "Comment Clairvent collecte et utilise les données personnelles transmises via ses formulaires de contact, de devis et de réservation.",
    h1: "Politique de confidentialité",
    crumbs: [["Confidentialité", "confidentialite.html"]],
    priority: 0.2,
    body: `<section class="section"><div class="container" style="max-width:900px"><div class="prose">
<h2>Données collectées</h2><p>Lorsque vous utilisez nos formulaires (contact, rappel, devis, réservation), nous collectons les informations que vous saisissez : nom, établissement, téléphone, e-mail, adresse d'intervention, description de votre besoin et, le cas échéant, les photos que vous joignez.</p>
<h2>Finalité</h2><p>Ces données servent uniquement à répondre à votre demande, à établir un devis, à organiser l'intervention et à assurer le suivi de nos prestations. Elles ne sont ni vendues ni cédées.</p>
<h2>Transmission</h2><p>Les formulaires sont acheminés par le service FormSubmit vers notre messagerie. Aucune autre transmission à des tiers n'a lieu, hors obligations légales.</p>
<h2>Durée de conservation</h2><p>Les demandes sans suite sont conservées au maximum trois ans. Les données clients sont conservées pendant la durée de la relation commerciale et les durées légales applicables.</p>
<h2>Vos droits</h2><p>Conformément au RGPD, vous disposez d'un droit d'accès, de rectification, d'effacement, d'opposition et de limitation. Pour l'exercer : ${SITE.email}. Vous pouvez également saisir la CNIL.</p>
<h2>Cookies</h2><p>Ce site n'utilise aucun cookie publicitaire ni outil de mesure d'audience. Les polices sont chargées depuis Google Fonts et la carte depuis OpenStreetMap.</p>
</div></div></section>`
  });

  /* Plan du site */
  layout({
    path: "plan-du-site.html",
    title: "Plan du site | Clairvent",
    desc: "Plan du site Clairvent : toutes les pages de prestations, secteurs, conseils et villes.",
    h1: "Plan du site",
    crumbs: [["Plan du site", "plan-du-site.html"]],
    priority: 0.3,
    body: `<section class="section"><div class="container"><div class="grid g3">
<div class="widget"><h3>Pages principales</h3><ul>${[["index.html", "Accueil"], ["prestations.html", "Prestations"], ["secteurs.html", "Secteurs"], ["notre-savoir-faire.html", "Notre savoir-faire"], ["methode.html", "Notre méthode"], ["reglementation.html", "Réglementation"], ["certificat-de-degraissage.html", "Certificat de dégraissage"], ["realisations.html", "Réalisations"], ["diagnostic.html", "Diagnostic"], ["faq.html", "FAQ"], ["conseils.html", "Conseils"], ["zones.html", "Zones"], ["ou-nous-trouver.html", "Où nous trouver"], ["reservation.html", "Réservation"], ["devis.html", "Devis"], ["contact.html", "Contact"]].map(([u, n]) => `<li><a href="{r}${u}">${n}</a></li>`).join("")}</ul></div>
<div class="widget"><h3>Prestations</h3><ul>${services.map((s) => `<li><a href="{r}prestations/${s.slug}.html">${s.nav}</a></li>`).join("")}</ul></div>
<div class="widget"><h3>Secteurs</h3><ul>${sectors.map((s) => `<li><a href="{r}secteurs/${s.slug}.html">${s.name}</a></li>`).join("")}</ul></div>
</div>
<div class="widget mt2"><h3>Conseils</h3><ul class="city-list" style="columns:2 320px">${guides.map((g) => `<li><a href="{r}conseils/${g.slug}.html">${g.title}</a></li>`).join("")}</ul></div>
<div class="widget mt2"><h3>Villes</h3><ul class="city-list">${depts.map((d) => `<li><a href="{r}zones/${d.slug}.html"><strong>${d.name} (${d.code})</strong></a></li>`).join("")}${cities.map((c) => `<li><a href="{r}villes/nettoyage-hotte-${c.slug}.html">${c.name}</a></li>`).join("")}</ul></div>
</div></section>`
  });

  /* Merci & 404 (non indexées) */
  layout({
    path: "merci.html", noindex: true,
    title: "Merci, votre demande est envoyée | Clairvent",
    desc: "Votre demande a bien été transmise à Clairvent.",
    h1: "Merci, c'est bien reçu !",
    lead: "Un technicien vous recontacte dans les meilleurs délais (" + SITE.hours + ") pour confirmer votre demande. Votre devis vous parvient sous 24 h ouvrées.",
    heroCta: `<a class="btn" href="{r}index.html">Retour à l'accueil</a><a class="btn btn-ghost-light" href="{r}conseils.html">Lire nos conseils</a>`,
    body: `<section class="section"><div class="container"><div class="grid g3">${["frequence-degraissage-hotte", "entretien-quotidien-hotte-restaurant", "certificat-nettoyage-hotte-assurance"].map((s) => guideCard(guideBySlug[s])).join("")}</div></div></section>`
  });
  layout({
    path: "404.html", noindex: true,
    title: "Page introuvable | Clairvent",
    desc: "La page demandée n'existe pas ou a été déplacée.",
    h1: "Cette page s'est envolée par l'extraction…",
    lead: "La page demandée n'existe pas ou a été déplacée. Voici quelques pistes pour retrouver votre chemin.",
    heroCta: `<a class="btn" href="/index.html">Accueil</a><a class="btn btn-ghost-light" href="/prestations.html">Prestations</a><a class="btn btn-ghost-light" href="/contact.html">Contact</a>`,
    body: `<section class="section"><div class="container"><div class="grid g4">${services.slice(0, 4).map(svcCard).join("").replace(/\{r\}/g, "/")}</div></div></section>`
  });
}

/* ------------------------------------------------------------------ */
/* Génération                                                           */
/* ------------------------------------------------------------------ */
fs.rmSync(DIST, { recursive: true, force: true });
home();
servicePages();
sectorPages();
guidePages();
placePages();
corePages();

for (const p of pages) {
  const f = path.join(DIST, p.path);
  fs.mkdirSync(path.dirname(f), { recursive: true });
  fs.writeFileSync(f, p.html);
}
fs.cpSync(path.join(ROOT, "src/assets"), path.join(DIST, "assets"), { recursive: true });

// Favicon + image de partage
fs.mkdirSync(path.join(DIST, "assets/img"), { recursive: true });
fs.writeFileSync(path.join(DIST, "assets/img/favicon.svg"), logo.replace('<svg viewBox', '<svg xmlns="http://www.w3.org/2000/svg" viewBox'));
fs.writeFileSync(path.join(DIST, "assets/img/og-image.svg"), `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0e1c2b"/><stop offset="1" stop-color="#1b344d"/></linearGradient></defs><rect width="1200" height="630" fill="url(#g)"/><circle cx="1050" cy="80" r="260" fill="#e0701b" opacity=".25"/><g transform="translate(90 170) scale(4)">${logo.replace(/<\/?svg[^>]*>/g, "")}</g><text x="340" y="270" font-family="Arial,sans-serif" font-size="96" font-weight="800" fill="#fff">Clair<tspan fill="#e0701b">vent</tspan></text><text x="344" y="340" font-family="Arial,sans-serif" font-size="38" fill="#c9d4df">Nettoyage de hottes &amp; cuisines professionnelles</text><text x="344" y="400" font-family="Arial,sans-serif" font-size="32" fill="#ffb070">Techniciens diplômés · Certificat · Île-de-France</text><text x="344" y="480" font-family="Arial,sans-serif" font-size="40" font-weight="700" fill="#fff">${SITE.phone}</text></svg>`);

// Sitemap, robots, llms.txt
const indexable = pages.filter((p) => !p.noindex);
fs.writeFileSync(path.join(DIST, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${indexable.map((p) => `  <url><loc>${SITE.url}/${p.path === "index.html" ? "" : p.path}</loc><lastmod>${SITE.updated}</lastmod><priority>${p.priority.toFixed(1)}</priority></url>`).join("\n")}
</urlset>
`);
fs.writeFileSync(path.join(DIST, "robots.txt"), `User-agent: *\nAllow: /\nDisallow: /merci.html\n\nSitemap: ${SITE.url}/sitemap.xml\n`);
fs.writeFileSync(path.join(DIST, "llms.txt"), `# ${SITE.name}

> Entreprise spécialisée dans le nettoyage et le dégraissage de hottes, de conduits d'extraction et de cuisines, pour les professionnels et les particuliers d'Île-de-France. Basée ${SITE.au} (${SITE.cp}).

## Identité
- Nom : ${SITE.name} (marque exploitée par ${SITE.legal})
- Téléphone : ${SITE.phone}
- Standard : ${SITE.hours} ; interventions de jour comme de nuit
- Zone : Paris et les huit départements d'Île-de-France
- Prix : sur devis gratuit, sous 24 h ouvrées

## Engagements
- Nettoyage du circuit complet : hotte, filtres, plénum, conduit, extracteur
- Techniciens formés et diplômés dans les métiers de la propreté
- Certificat et dossier photo remis à chaque intervention
- Interventions en dehors des services

## Pages clés
${[["prestations.html", "Prestations"], ["reglementation.html", "Réglementation"], ["notre-savoir-faire.html", "Savoir-faire"], ["reservation.html", "Réservation"], ["conseils.html", "Conseils"], ["zones.html", "Zones d'intervention"]].map(([u, n]) => `- ${n} : ${SITE.url}/${u}`).join("\n")}
`);

console.log(`✔ ${pages.length} pages générées (${indexable.length} indexables) dans dist/`);
console.log(`  prestations: ${services.length} · secteurs: ${sectors.length} · conseils: ${guides.length} · départements: ${depts.length} · villes: ${cities.length}`);
