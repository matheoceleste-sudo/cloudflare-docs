// Générateur statique du site « Hottes ta cuisine » — `node build.mjs` produit dist/
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { services } from "./src/data/services.mjs";
import { guides1 } from "./src/data/guides1.mjs";
import { guides2 } from "./src/data/guides2.mjs";
import { sectors } from "./src/data/sectors.mjs";
import { base, depts, cities } from "./src/data/places.mjs";
import { svcShort, secShort } from "./src/data/copy.mjs";
import { sprite, ico, mark, wordmark } from "./src/icons.mjs";

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const DIST = path.join(ROOT, "dist");

/* Configuration — à adapter avant la mise en ligne */
const SITE = {
  name: "Hottes ta cuisine",
  tagline: "Nettoyage de hottes et de cuisines",
  url: "https://www.hottestacuisine.fr",
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
  legal: "MathClean, entreprise individuelle de Mathéo Céleste",
  siret: "924 565 990 00010",
  updated: "2026-09-27",
  updatedLabel: "septembre 2026"
};

const guides = [...guides1, ...guides2];
const CATS = {
  reg: "Réglementation", feu: "Sécurité incendie", hyg: "Hygiène", ent: "Entretien",
  equ: "Équipements", par: "Particuliers", ges: "Gestion"
};
const svcBy = Object.fromEntries(services.map((s) => [s.slug, s]));
const guideBy = Object.fromEntries(guides.map((g) => [g.slug, g]));
const deptBy = Object.fromEntries(depts.map((d) => [d.code, d]));
const MAIN = ["nettoyage-hotte-professionnelle", "degraissage-conduit-extraction", "nettoyage-tourelle-caisson-extraction", "nettoyage-filtres-hotte", "nettoyage-cuisine-professionnelle", "remise-en-etat-cuisine"];

/* Utilitaires */
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const strip = (h) => h.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
const readMin = (h) => Math.max(3, Math.round(strip(h).split(" ").length / 200));
const km = (a, b) => {
  const R = 6371, r = Math.PI / 180, dLat = (b.lat - a.lat) * r, dLon = (b.lon - a.lon) * r;
  const x = Math.sin(dLat / 2) ** 2 + Math.cos(a.lat * r) * Math.cos(b.lat * r) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(x));
};
const aV = (n) => (n.startsWith("Le ") ? "au " + n.slice(3) : n.startsWith("Les ") ? "aux " + n.slice(4) : "à " + n);
const deV = (n) => (n.startsWith("Le ") ? "du " + n.slice(3) : n.startsWith("Les ") ? "des " + n.slice(4) : "de " + n);
const hash = (s) => [...s].reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 7);
const pad = (n) => String(n).padStart(2, "0");
const cleanBody = (h) => h
  .replace(/<div class="callout[^"]*">\s*<svg[^>]*>.*?<\/svg>/g, '<div class="note">')
  .replace(/class="check cols"/g, 'class="check"');
const pages = [];

function toc(html) {
  const list = [];
  const out = html.replace(/<h2>(.*?)<\/h2>/g, (m, t) => {
    const id = strip(t).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
    list.push([id, strip(t)]);
    return `<h2 id="${id}">${t}</h2>`;
  });
  return { html: out, list };
}

/* ------------------------------------------------------------------ */
/* Gabarit                                                              */
/* ------------------------------------------------------------------ */
function layout(p) {
  const depth = p.path.split("/").length - 1;
  const r = "../".repeat(depth);
  const L = (x) => r + x;
  const canonical = SITE.url + "/" + (p.path === "index.html" ? "" : p.path);
  const cur = (s) => (p.section === s ? ' aria-current="page"' : "");
  const crumbs = p.crumbs || [];
  const ld = [...(p.jsonld || [])];
  if (crumbs.length) ld.push({
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    itemListElement: [["Accueil", ""], ...crumbs].map(([n, u], i) => ({ "@type": "ListItem", position: i + 1, name: n, item: SITE.url + "/" + (u || "") }))
  });
  const crumbHtml = crumbs.length ? `<nav class="crumbs" aria-label="Fil d'Ariane"><a href="${L("index.html")}">Accueil</a>${crumbs.map(([n, u], i) => i === crumbs.length - 1 ? `<span>/</span><span aria-current="page">${esc(n)}</span>` : `<span>/</span><a href="${L(u)}">${esc(n)}</a>`).join("")}</nav>` : "";
  const head = p.head === false ? "" : p.headHtml || `
<header class="ph"><div class="wrap">
  ${crumbHtml}
  ${p.label ? `<p class="label">${p.label}</p>` : ""}
  <h1>${p.h1}</h1>
  ${p.lead ? `<p class="lead">${p.lead}</p>` : ""}
  ${p.meta || ""}
  ${p.actions ? `<div class="actions">${p.actions}</div>` : ""}
</div></header>`;
  const navItems = [["prestations.html", "Prestations", "presta"], ["notre-savoir-faire.html", "Savoir-faire", "savoir"], ["realisations.html", "Réalisations", "real"], ["conseils.html", "Conseils", "conseils"], ["zones.html", "Zones", "zones"], ["contact.html", "Contact", "contact"]];
  const html = `<!DOCTYPE html>
<html lang="fr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(p.title)}</title>
<meta name="description" content="${esc(p.desc)}">
<meta name="robots" content="${p.noindex ? "noindex,follow" : "index,follow,max-image-preview:large"}">
<link rel="canonical" href="${canonical}">
<meta name="theme-color" content="#f4f1ec">
<meta property="og:type" content="${p.ogType || "website"}">
<meta property="og:site_name" content="${SITE.name}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="${esc(p.title)}">
<meta property="og:description" content="${esc(p.desc)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${SITE.url}/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="${L("assets/img/favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="${L("assets/css/style.css")}">
${ld.map((o) => `<script type="application/ld+json">${JSON.stringify(o)}</script>`).join("\n")}
</head>
<body>
${sprite}
<a class="skip" href="#main">Aller au contenu</a>
<header class="hd"><div class="wrap">
  <a class="logo" href="${L("index.html")}" aria-label="${SITE.name}, accueil">${mark()}<span class="logo-word">${wordmark}</span></a>
  <nav class="nav" aria-label="Menu principal"><ul>${navItems.map(([u, n, s]) => `<li><a href="${L(u)}"${cur(s)}>${n}</a></li>`).join("")}</ul></nav>
  <div class="hd-cta">
    <a class="hd-tel" href="tel:${SITE.tel}">${SITE.phone}</a>
    <a class="btn btn-sm" href="${L("reservation.html")}">Réserver</a>
    <button class="burger" type="button" data-menu-open aria-controls="nav-mobile" aria-expanded="false">Menu</button>
  </div>
</div></header>
<div class="nav-mobile" id="nav-mobile" role="dialog" aria-label="Menu">
  <div class="top"><a class="logo" href="${L("index.html")}">${mark()}<span class="logo-word">${wordmark}</span></a><button class="burger" type="button" data-menu-close>Fermer</button></div>
  <ul>${[["index.html", "Accueil"], ...navItems].map(([u, n]) => `<li><a href="${L(u)}">${n}</a></li>`).join("")}</ul>
  <div class="foot"><a class="btn" href="${L("reservation.html")}">Réserver une intervention</a><a class="btn btn-line" href="tel:${SITE.tel}">${SITE.phone}</a></div>
</div>
<main id="main">
${head.replace(/\{r\}/g, r)}
${p.body.replace(/\{r\}/g, r)}
</main>
${footer(L)}
<div class="callbar"><a href="tel:${SITE.tel}">${ico("phone")}Appeler</a><a class="primary" href="${L("reservation.html")}">Réserver</a></div>
<script src="${L("assets/js/site.js")}" defer></script>
${(p.scripts || []).map((s) => `<script src="${L(s)}" defer></script>`).join("\n")}
</body>
</html>`;
  pages.push({ path: p.path, html, noindex: !!p.noindex, priority: p.priority || 0.6 });
}

function footer(L) {
  const top = ["paris-11", "le-blanc-mesnil", "saint-denis", "boulogne-billancourt", "courbevoie", "montreuil", "creteil", "versailles", "argenteuil", "rungis", "roissy-en-france", "massy", "nanterre", "aubervilliers"];
  return `<footer class="ft"><div class="wrap">
<div class="ft-top">
  <div><a class="logo" href="${L("index.html")}">${mark("#141412")}<span class="logo-word">${wordmark}</span></a>
  <p class="big">Parlons de votre cuisine.</p>
  <p><a href="tel:${SITE.tel}">${SITE.phone}</a><br>${SITE.hours}</p></div>
  <div><h4>Prestations</h4><ul>${MAIN.map((s) => `<li><a href="${L("prestations/" + s + ".html")}">${svcShort[s][0]}</a></li>`).join("")}<li><a href="${L("prestations.html")}">Tout voir</a></li></ul></div>
  <div><h4>Entreprise</h4><ul><li><a href="${L("notre-savoir-faire.html")}">Savoir-faire</a></li><li><a href="${L("methode.html")}">Méthode</a></li><li><a href="${L("realisations.html")}">Réalisations</a></li><li><a href="${L("reglementation.html")}">Réglementation</a></li><li><a href="${L("conseils.html")}">Conseils</a></li><li><a href="${L("faq.html")}">Questions fréquentes</a></li></ul></div>
  <div><h4>Nous trouver</h4><ul><li>${SITE.cp} ${SITE.city}</li><li>Paris et Île-de-France</li><li><a href="${L("ou-nous-trouver.html")}">Voir la carte</a></li><li><a href="${L("reservation.html")}">Réserver en ligne</a></li><li><a href="${L("devis.html")}">Devis gratuit</a></li></ul></div>
</div>
<div class="ft-cities">${top.map((s) => { const c = cities.find((x) => x.slug === s); return `<a href="${L("villes/nettoyage-hotte-" + s + ".html")}">Hotte ${c.name}</a>`; }).join("")}<a href="${L("zones.html")}">Toutes les villes</a></div>
<div class="ft-bottom"><span>© <span data-year>2026</span> ${SITE.name}</span><span><a href="${L("mentions-legales.html")}">Mentions légales</a> · <a href="${L("confidentialite.html")}">Confidentialité</a> · <a href="${L("plan-du-site.html")}">Plan du site</a></span></div>
</div></footer>`;
}

/* ------------------------------------------------------------------ */
/* Blocs                                                                */
/* ------------------------------------------------------------------ */
const V = {
  loop: (r, cap = "") => `<video data-autoplay muted loop playsinline preload="metadata" poster="${r}assets/videos/tourelle-mousse.webp" aria-label="Dégraissage d'une tourelle d'extraction en toiture"><source src="${r}assets/videos/tourelle-mousse.mp4" type="video/mp4"></video>${cap}`,
  site: (r) => `<video controls muted playsinline preload="none" poster="${r}assets/videos/chantier-toiture.webp" aria-label="Intervention en toiture sur un extracteur de cuisine"><source src="${r}assets/videos/chantier-toiture.mp4" type="video/mp4"></video>`
};
const IMG = {
  tourelle: ["assets/photos/tourelle-degraissage.webp", "Tourelle d'extraction en cours de dégraissage, en toiture"],
  conduit: ["assets/photos/conduit-graisse.webp", "Départ de conduit encrassé, vu depuis la hotte"]
};
const img = (r, k, cls = "") => `<img src="${r}${IMG[k][0]}" alt="${IMG[k][1]}" loading="lazy"${cls}>`;

const faqHtml = (list) => `<div class="faq">${list.map(([q, a]) => `<details><summary>${q}</summary><div><p>${a}</p></div></details>`).join("")}</div>`;
const faqLd = (list) => ({ "@context": "https://schema.org", "@type": "FAQPage", mainEntity: list.map(([q, a]) => ({ "@type": "Question", name: q, acceptedAnswer: { "@type": "Answer", text: a } })) });

const cta = (title = "Parlons de votre cuisine.", text = "Un appel suffit pour fixer une visite. Le devis est gratuit, et il arrive sous 24 heures.", q = "") => `
<section class="sec-dark"><div class="wrap cta">
<p class="label"><b>—</b>Contact</p>
<h2 class="mt1">${title}</h2>
<p>${text}</p>
<div class="actions"><a class="btn btn-light" href="{r}reservation.html${q}">Réserver une intervention</a><a class="btn btn-ghost" href="tel:${SITE.tel}">${SITE.phone}</a></div>
</div></section>`;

const svcIndex = (slugs) => `<ol class="index">${slugs.map((s, i) => `<li class="reveal"><a href="{r}prestations/${s}.html"><span class="n">${pad(i + 1)}</span><span class="t">${svcShort[s][0]}</span><span class="d">${svcShort[s][1]}</span><span class="go">→</span></a></li>`).join("")}</ol>`;
const postList = (list) => `<ul class="posts">${list.map((g) => `<li data-cat="${g.cat}"><a href="{r}conseils/${g.slug}.html"><span class="c">${CATS[g.cat]}</span><span><span class="t">${g.title}</span><span class="d">${g.desc}</span></span><span class="r">${readMin(g.body)} min</span></a></li>`).join("")}</ul>`;

const method = [
  ["Visite", "Nous regardons la hotte, le tracé du conduit et l'accès au toit. Devis sous 24 heures."],
  ["Protection", "Bâches sur les équipements, extracteur consigné. Rien ne coule sur vos plans de travail."],
  ["Dégraissage", "Filtres, hotte, plénum, conduit, tourelle. Grattage, mousse, brossage, rinçage."],
  ["Certificat", "Photos avant et après, certificat signé, date du prochain passage."]
];
const methodCols = (dark = false) => `<div class="cols c4">${method.map(([t, d], i) => `<div class="col reveal"><span class="n">${pad(i + 1)}</span><h3>${t}</h3><p>${d}</p></div>`).join("")}</div>`;

const creds = [
  ["CAP Agent de propreté et d'hygiène", "Techniques, produits, sécurité."],
  ["Bac pro Hygiène, propreté, stérilisation", "Organisation, protocoles, contrôle qualité."],
  ["Travail en hauteur", "Interventions en toiture, protections antichute."],
  ["Risque chimique et électrique", "Dosage des produits, consignation des moteurs."],
  ["Hygiène alimentaire (HACCP)", "Travailler en cuisine sans risque pour les denrées."],
  ["Sauveteur secouriste du travail", "Savoir réagir sur un chantier."]
];

const provider = {
  "@type": "LocalBusiness", "@id": SITE.url + "/#business", name: SITE.name, telephone: SITE.tel, url: SITE.url,
  image: SITE.url + "/assets/img/og-image.jpg", priceRange: "Sur devis",
  address: { "@type": "PostalAddress", streetAddress: SITE.street, postalCode: SITE.cp, addressLocality: SITE.city, addressRegion: "Île-de-France", addressCountry: "FR" },
  geo: { "@type": "GeoCoordinates", latitude: base.lat, longitude: base.lon },
  areaServed: depts.map((d) => ({ "@type": "AdministrativeArea", name: `${d.name} (${d.code})` })),
  openingHoursSpecification: [{ "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], opens: "08:00", closes: "20:00" }]
};

/* Schéma au trait du circuit d'extraction */
const parts = {
  hotte: ["La hotte", "Elle capte les fumées au-dessus des feux. Nous dégraissons le caisson, les gouttières et les rampes, dedans comme dehors."],
  filtres: ["Les filtres", "La première barrière. Déposés, trempés dans un bain chaud, rincés et contrôlés un par un."],
  plenum: ["Le plénum", "La chambre derrière les filtres. Souvent la zone la plus grasse de la hotte. Grattage, puis mousse dégraissante."],
  conduit: ["Le conduit", "La zone la plus dangereuse en cas de feu. Nettoyé par les trappes de visite, photographié à chaque ouverture."],
  tourelle: ["La tourelle", "Le moteur de l'extraction, en toiture. Consignée, dégraissée, contrôlée, puis remise en route."]
};
function diagram() {
  const ink = "#191917";
  const spots = [["hotte", 300, 312, 1], ["filtres", 118, 288, 2], ["plenum", 212, 262, 3], ["conduit", 340, 150, 4], ["tourelle", 460, 66, 5]];
  return `<div class="diagram" data-diagram>
<svg viewBox="0 0 540 430" role="img" aria-labelledby="dg"><title id="dg">Schéma d'une extraction de cuisine : hotte, filtres, plénum, conduit, tourelle</title>
<g fill="none" stroke="${ink}" stroke-width="1.2" stroke-linejoin="round">
<path d="M0 92 H540" stroke-dasharray="2 5"/>
<path d="M162 250 V168 H392 V92"/><path d="M198 250 V204 H428 V92"/>
<path d="M270 168 v36 M300 168 v36" stroke-dasharray="3 4"/>
<rect x="380" y="58" width="60" height="34"/><path d="M366 58 Q410 22 454 58 Z"/><circle cx="410" cy="75" r="9"/>
<path d="M60 320 L110 250 H250 L300 320 Z"/><path d="M52 320 H308"/>
<path d="M88 316 l24 -44 M100 316 l24 -44 M112 316 l24 -44 M124 316 l24 -44"/>
<rect x="60" y="370" width="240" height="40"/><path d="M60 382 H300"/>
<path d="M92 368 h52 M186 368 h58"/>
</g>
<g fill="none" stroke="#a8502a" stroke-width="1" stroke-dasharray="3 5"><path d="M118 360 C118 330 150 300 180 270 S 180 200 300 186 S 400 140 410 40"/></g>
<text x="12" y="84" font-family="Inter,sans-serif" font-size="11" fill="#77726a" letter-spacing="1.5">TOITURE</text>
${spots.map(([k, x, y, n]) => `<g class="hotspot" data-key="${k}" tabindex="0" role="button" aria-label="${parts[k][0]}"><circle cx="${x}" cy="${y}" r="13"/><text x="${x}" y="${y + 4}" text-anchor="middle">${n}</text></g>`).join("")}
</svg>
<div class="diagram-tabs">${Object.entries(parts).map(([k, v], i) => `<button type="button" data-key="${k}" aria-pressed="false">${pad(i + 1)} ${v[0].replace(/^(La|Le|Les) /, "")}</button>`).join("")}</div>
<div class="diagram-panel" aria-live="polite"></div>
${Object.entries(parts).map(([k, v]) => `<template data-key="${k}"><strong>${v[0]}</strong>${v[1]}</template>`).join("")}
</div>`;
}

/* Carte de zone, au trait */
function zoneMap(highlight = null) {
  const X = (lon) => (lon - 1.95) * 600, Y = (lat) => (49.24 - lat) * 912;
  const bx = X(base.lon), by = Y(base.lat), k = 8.2;
  return `<svg viewBox="0 0 600 660" role="img" aria-label="Zone d'intervention en Île-de-France">
${[10, 20, 30].map((d) => `<circle cx="${bx.toFixed(1)}" cy="${by.toFixed(1)}" r="${(d * k).toFixed(1)}" fill="none" stroke="#c6bfb3" stroke-width="1"/><text x="${(bx + d * k * 0.71 + 4).toFixed(1)}" y="${(by - d * k * 0.71).toFixed(1)}" font-size="11" fill="#77726a" font-family="Inter,sans-serif">${d} km</text>`).join("")}
<text x="${X(2.30).toFixed(1)}" y="${Y(48.80).toFixed(1)}" font-size="12" fill="#77726a" font-family="Inter,sans-serif" letter-spacing="2">PARIS</text>
${cities.map((c) => { const hi = c.slug === highlight; return `<a href="{r}villes/nettoyage-hotte-${c.slug}.html"><circle cx="${X(c.lon).toFixed(1)}" cy="${Y(c.lat).toFixed(1)}" r="${hi ? 6 : 2.8}" fill="${hi ? "#a8502a" : "#191917"}"><title>${c.name}</title></circle></a>${hi ? `<text x="${(X(c.lon) + 10).toFixed(1)}" y="${(Y(c.lat) + 4).toFixed(1)}" font-size="13" fill="#191917" font-family="Inter,sans-serif">${c.name}</text>` : ""}`; }).join("")}
<circle cx="${bx.toFixed(1)}" cy="${by.toFixed(1)}" r="8" fill="#a8502a"/><text x="${(bx + 14).toFixed(1)}" y="${(by - 10).toFixed(1)}" font-size="13" fill="#191917" font-family="Inter,sans-serif">${SITE.city}</text>
</svg>`;
}

function freqTool() {
  const sel = (id, name, label, opts, def) => `<div><label for="${id}">${label}</label><select id="${id}" name="${name}">${opts.map(([v, t]) => `<option value="${v}"${v === def ? " selected" : ""}>${t}</option>`).join("")}</select></div>`;
  return `<div class="tool"><form class="form" data-freq-tool data-resa="{r}reservation.html" data-devis="{r}devis.html">
${sel("f-c", "cuisson", "Cuisson principale", [["0", "Vapeur, four, cuisson douce"], ["1", "Cuisine traditionnelle"], ["2", "Plancha, pizzas, friture occasionnelle"], ["3", "Friture, grill, wok, rôtisserie"]], "1")}
<div class="row">${sel("f-v", "volume", "Couverts par jour", [["0", "Moins de 80"], ["1", "80 à 200"], ["2", "200 à 400"], ["3", "Plus de 400"]], "1")}${sel("f-h", "heures", "Heures de cuisson par jour", [["0", "Moins de 4 h"], ["1", "4 à 8 h"], ["2", "8 à 12 h"], ["3", "Plus de 12 h"]], "1")}</div>
<div class="row">${sel("f-f", "filtres", "Nettoyage des filtres", [["0", "Plusieurs fois par semaine"], ["1", "Chaque semaine"], ["2", "Chaque mois"], ["3", "Rarement"]], "1")}${sel("f-d", "dernier", "Dernier dégraissage complet", [["2", "Moins de 3 mois"], ["5", "3 à 6 mois"], ["9", "6 à 12 mois"], ["24", "Plus d'un an"]], "5")}</div>
<div><button class="btn" type="submit">Calculer</button></div>
</form><div class="tool-result" aria-live="polite"></div></div>`;
}

/* ------------------------------------------------------------------ */
/* Accueil                                                              */
/* ------------------------------------------------------------------ */
const homeFaq = [
  ["Combien coûte un nettoyage de hotte ?", "Le prix dépend de la hotte, de la longueur du conduit, de l'accès au toit et de l'encrassement. Nous établissons un devis gratuit après une visite ou sur photos, sous 24 heures."],
  ["Tous les combien faut-il la faire nettoyer ?", "Une fois par an au minimum dans un établissement recevant du public. Deux à quatre fois par an pour une cuisine qui frit ou grille beaucoup."],
  ["Faut-il fermer pendant l'intervention ?", "Non. Nous venons la nuit, tôt le matin ou le jour de fermeture. La cuisine est rendue propre et prête pour le service."],
  ["Qui intervient ?", "Des techniciens formés et diplômés dans les métiers de la propreté, habilités au travail en hauteur et formés à l'hygiène alimentaire."]
];

function home() {
  const headHtml = `
<section class="hero"><div class="wrap hero-grid">
  <div>
    <p class="label"><b>01</b>Nettoyage de hottes · Île-de-France</p>
    <h1>Des hottes propres, <em>du filtre jusqu'au toit.</em></h1>
    <p class="lead">Nous dégraissons les hottes, les conduits et les extracteurs des cuisines professionnelles. Et nous remettons la cuisine au propre.</p>
    <div class="actions"><a class="btn" href="reservation.html">Réserver une intervention</a><a class="btn btn-line" href="tel:${SITE.tel}">${SITE.phone}</a></div>
    <ul class="facts"><li>Certificat à chaque passage</li><li>Hors de vos services</li><li>Devis gratuit</li></ul>
  </div>
  <figure class="hero-media reveal">${V.loop("")}<figcaption>Tourelle d'extraction, en cours de dégraissage</figcaption></figure>
</div></section>`;

  const body = `
<section class="sec"><div class="wrap">
  <p class="label"><b>02</b>Notre métier</p>
  <p class="statement mt2 reveal">Une hotte, ce n'est pas que des filtres. <span>Derrière, il y a le plénum, le conduit, l'extracteur. C'est là que la graisse s'accumule. C'est là que nous travaillons.</span></p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="head"><p class="label"><b>03</b>Prestations</p><div><h2>Ce que nous faisons</h2><p>Six prestations principales, un seul niveau d'exigence. Prix sur devis.</p></div></div>
  ${svcIndex(MAIN)}
  <p class="mt2"><a class="arrow" href="prestations.html">Toutes les prestations</a></p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="head"><p class="label"><b>04</b>Sur le chantier</p><div><h2>Ce que l'on trouve, et ce que l'on laisse</h2></div></div>
  <div class="gallery">
    <figure class="a reveal"><div class="m">${img("", "tourelle")}</div><figcaption>Tourelle d'extraction. Mousse dégraissante sur la turbine.</figcaption></figure>
    <figure class="b reveal"><div class="m">${img("", "conduit")}</div><figcaption>Départ de conduit, vu depuis la hotte, avant intervention.</figcaption></figure>
    <figure class="c reveal"><div class="m">${V.site("")}</div><figcaption>En toiture, pendant le dégraissage.</figcaption></figure>
  </div>
  <p class="mt2"><a class="arrow" href="realisations.html">Voir les réalisations</a></p>
</div></section>

<section class="sec-dark"><div class="wrap">
  <div class="head"><p class="label"><b>05</b>Méthode</p><div><h2>Quatre temps, toujours les mêmes</h2></div></div>
  ${methodCols(true)}
  <p class="mt3"><a class="arrow" href="methode.html">La méthode en détail</a></p>
</div></section>

<section class="sec" style="padding-top:var(--s1)"><div class="wrap split top">
  <div><p class="label"><b>06</b>L'équipe</p><h2 class="mt1">Formés. Diplômés. Spécialisés.</h2></div>
  <div><p class="statement" style="font-size:clamp(1.3rem,2vw,1.6rem);line-height:1.4">Chaque intervention est réalisée par des techniciens diplômés des métiers de la propreté, formés au travail en hauteur et à l'hygiène alimentaire.</p>
  <ul class="list mt2">${creds.slice(0, 4).map(([t]) => `<li>${t}</li>`).join("")}</ul>
  <p class="mt2"><a class="arrow" href="notre-savoir-faire.html">Notre savoir-faire</a></p></div>
</div></section>

<section class="sec sec-line" style="padding-top:var(--s1)"><div class="wrap split">
  <div><p class="label"><b>07</b>Réglementation</p><h2 class="mt1">Une fois par an, au minimum.</h2></div>
  <div><p>Dans un établissement recevant du public, le règlement de sécurité incendie impose un nettoyage complet de l'extraction chaque année. Votre assureur vous demandera le certificat.</p><a class="arrow" href="reglementation.html">Ce que dit la loi</a></div>
</div></section>

<section class="sec sec-line" style="padding-top:var(--s1)"><div class="wrap split">
  <div class="zone reveal">${zoneMap()}</div>
  <div><p class="label"><b>08</b>Zone</p><h2 class="mt1">Basés ${SITE.au}. Partout en Île-de-France.</h2>
  <p class="mt1">Paris et les huit départements. Délais courts en Seine-Saint-Denis et en petite couronne.</p>
  <ul class="pills mt2">${depts.map((d) => `<li><a href="zones/${d.slug}.html">${d.name}</a></li>`).join("")}</ul>
  <p class="mt2"><a class="arrow" href="ou-nous-trouver.html">Où nous trouver</a></p></div>
</div></section>

<section class="sec sec-line" style="padding-top:var(--s1)"><div class="wrap">
  <div class="head"><p class="label"><b>09</b>Questions</p><div><h2>En bref</h2></div></div>
  ${faqHtml(homeFaq)}
</div></section>
${cta()}`;
  layout({
    path: "index.html", section: "home", headHtml, body, priority: 1,
    title: "Hottes ta cuisine · Nettoyage de hottes professionnelles en Île-de-France",
    desc: "Dégraissage de hottes, conduits et extracteurs, nettoyage de cuisines professionnelles en Île-de-France. Techniciens diplômés, certificat remis, devis gratuit.",
    jsonld: [{ "@context": "https://schema.org", ...provider }, { "@context": "https://schema.org", "@type": "WebSite", name: SITE.name, url: SITE.url }, faqLd(homeFaq)]
  });
}

/* ------------------------------------------------------------------ */
/* Prestations                                                          */
/* ------------------------------------------------------------------ */
function servicePages() {
  const hotte = services.filter((s) => s.group === "hotte").map((s) => s.slug);
  const cuisine = services.filter((s) => s.group === "cuisine").map((s) => s.slug);
  layout({
    path: "prestations.html", section: "presta", crumbs: [["Prestations", "prestations.html"]],
    title: "Prestations · Nettoyage de hotte et de cuisine | Hottes ta cuisine",
    desc: "Dégraissage de hotte, conduit, tourelle et filtres, certificat, contrat d'entretien, nettoyage et remise en état de cuisine. Prix sur devis.",
    label: "Prestations", h1: "Hottes, extraction, cuisines.",
    lead: "Seize prestations, toutes réalisées par nos techniciens. Les prix sont sur devis, gratuit, sous 24 heures.",
    body: `<section class="sec"><div class="wrap">
<div class="head"><p class="label"><b>01</b>Hottes et extraction</p><div><h2>Le circuit d'extraction</h2></div></div>${svcIndex(hotte)}
</div></section>
<section class="sec"><div class="wrap">
<div class="head"><p class="label"><b>02</b>Cuisines</p><div><h2>Le reste de la cuisine</h2></div></div>${svcIndex(cuisine).replace(/<span class="n">(\d+)<\/span>/g, (m, n) => `<span class="n">${pad(+n + hotte.length)}</span>`)}
</div></section>
<section class="sec sec-line" style="padding-top:var(--s1)"><div class="wrap split top">
<div><p class="label"><b>03</b>Prix</p><h2 class="mt1">Pourquoi sur devis</h2></div>
<div><p>Deux cuisines ne se ressemblent jamais. La longueur du conduit, le nombre de trappes, l'accès au toit et l'encrassement changent tout. Un prix affiché « à partir de » ne vous dirait rien.</p><p>Notre devis est gratuit, ferme et détaillé élément par élément. Le certificat et les photos sont toujours compris.</p><a class="arrow" href="{r}devis.html">Demander un devis</a></div>
</div></section>${cta()}`
  });

  for (const s of services) {
    const [name, short, lead] = svcShort[s.slug];
    const related = (s.related || []).map((x) => guideBy[x]).filter(Boolean);
    const others = services.filter((o) => o.group === s.group && o.slug !== s.slug).slice(0, 4).map((o) => o.slug);
    const faq = [...s.faq, ["Où intervenez-vous ?", `Partout en Île-de-France, depuis notre base ${SITE.du}.`]];
    const media = s.group === "hotte" ? (s.slug.includes("conduit") ? img("{r}", "conduit") : img("{r}", "tourelle")) : `<img src="{r}assets/photos/avant-plan-travail.webp" alt="Surface inox encrassée avant nettoyage" loading="lazy">`;
    layout({
      path: `prestations/${s.slug}.html`, section: "presta",
      crumbs: [["Prestations", "prestations.html"], [name, `prestations/${s.slug}.html`]],
      title: s.metaTitle.replace("Clairvent", SITE.name), desc: s.desc,
      label: s.group === "hotte" ? "Hottes et extraction" : "Cuisines", h1: s.title, lead,
      actions: `<a class="btn" href="{r}reservation.html?prestation=${s.slug}">Réserver</a><a class="btn btn-line" href="{r}devis.html">Devis gratuit</a>`,
      priority: s.pillar ? 0.9 : 0.8,
      body: `
<section class="sec"><div class="wrap split">
  <div class="frame reveal" style="aspect-ratio:4/5">${media}</div>
  <div><p class="label"><b>01</b>En quelques mots</p><p class="statement mt1" style="font-size:clamp(1.2rem,1.8vw,1.55rem);line-height:1.45">${s.intro[0]}</p></div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="head"><p class="label"><b>02</b>Compris</p><div><h2>Ce que nous faisons</h2></div></div>
  <ul class="list two">${s.includes.map((x) => `<li>${x}</li>`).join("")}</ul>
</div></section>
<section class="sec-dark"><div class="wrap">
  <div class="head"><p class="label"><b>03</b>Déroulé</p><div><h2>Comment ça se passe</h2></div></div>
  <div class="cols c4">${s.steps.map(([t, d], i) => `<div class="col reveal"><span class="n">${pad(i + 1)}</span><h3>${t}</h3><p>${d}</p></div>`).join("")}</div>
</div></section>
<section class="sec" style="padding-top:var(--s1)"><div class="wrap editorial">
  <aside><span class="label"><b>04</b>En détail</span></aside>
  <div class="prose">${cleanBody(s.body)}
  <h2>Le prix</h2><p>Sur devis gratuit, après une visite ou sur photos. Vous le recevez sous 24 heures.</p>
  <div class="actions"><a class="btn" href="{r}reservation.html?prestation=${s.slug}">Réserver</a><a class="arrow" href="tel:${SITE.tel}">${SITE.phone}</a></div></div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="head"><p class="label"><b>05</b>Questions</p><div><h2>Ce qu'on nous demande</h2></div></div>${faqHtml(faq)}
</div></section>
${related.length ? `<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>06</b>À lire</p><div><h2>Conseils liés</h2></div></div>${postList(related)}</div></section>` : ""}
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>07</b>Aussi</p><div><h2>Prestations proches</h2></div></div>${svcIndex(others)}</div></section>
${cta(undefined, undefined, `?prestation=${s.slug}`)}`,
      jsonld: [
        { "@context": "https://schema.org", "@type": "Service", name: s.title, description: s.desc, provider: { "@id": SITE.url + "/#business", ...provider }, areaServed: { "@type": "AdministrativeArea", name: "Île-de-France" } },
        faqLd(faq)
      ]
    });
  }
}

/* ------------------------------------------------------------------ */
/* Secteurs                                                             */
/* ------------------------------------------------------------------ */
function sectorPages() {
  layout({
    path: "secteurs.html", section: "presta", crumbs: [["Secteurs", "secteurs.html"]],
    title: "Secteurs · Nettoyage de hotte par type de cuisine | Hottes ta cuisine",
    desc: "Restaurants, fast-food, pizzerias, grills, woks, hôtels, cantines, EHPAD, dark kitchens, traiteurs, food trucks : une méthode adaptée à chaque cuisine.",
    label: "Secteurs", h1: "Chaque cuisine a sa graisse.",
    lead: "Un wok, un grill et un four de boulangerie n'encrassent pas une hotte de la même façon. Nous adaptons les produits et le rythme.",
    body: `<section class="sec"><div class="wrap"><ol class="index">${sectors.map((s, i) => `<li class="reveal"><a href="{r}secteurs/${s.slug}.html"><span class="n">${pad(i + 1)}</span><span class="t">${s.name}</span><span class="d">${secShort[s.slug]}</span><span class="go">→</span></a></li>`).join("")}</ol></div></section>${cta()}`
  });
  for (const s of sectors) {
    const faq = [
      ["À quelle fréquence ?", `${s.freq}. Le minimum légal en ERP reste d'un nettoyage complet par an.`],
      ["Sans fermer ?", "Oui. Nous intervenons en dehors de vos heures de production."],
      ["Quel prix ?", "Sur devis gratuit, selon votre installation, sous 24 heures."]
    ];
    layout({
      path: `secteurs/${s.slug}.html`, section: "presta",
      crumbs: [["Secteurs", "secteurs.html"], [s.name, `secteurs/${s.slug}.html`]],
      title: `${s.name} · Nettoyage de hotte | Hottes ta cuisine`, desc: s.desc,
      label: "Secteur", h1: s.name, lead: secShort[s.slug],
      actions: `<a class="btn" href="{r}reservation.html">Réserver</a><a class="btn btn-line" href="{r}devis.html">Devis gratuit</a>`,
      body: `
<section class="sec"><div class="wrap editorial">
  <aside><span class="label"><b>01</b>Votre cuisine</span></aside>
  <div class="prose"><p class="statement" style="font-size:clamp(1.4rem,2.2vw,1.9rem);line-height:1.35;color:var(--ink)">${s.context}</p>
  <h2>Points de vigilance</h2><ul class="check">${s.risks.map((x) => `<li>${x}</li>`).join("")}</ul>
  <h2>Rythme conseillé</h2><p><strong>${s.freq}.</strong> Nous l'ajustons à ce que nous voyons dans votre conduit, photos à l'appui.</p>
  <blockquote>Estimez votre rythme en trente secondes avec notre <a href="{r}diagnostic.html">outil de diagnostic</a>.</blockquote></div>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>02</b>Prestations</p><div><h2>Adaptées à votre activité</h2></div></div>${svcIndex(s.services)}</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>03</b>Questions</p><div><h2>En bref</h2></div></div>${faqHtml(faq)}</div></section>
${cta()}`,
      jsonld: [faqLd(faq)]
    });
  }
}

/* ------------------------------------------------------------------ */
/* Conseils                                                             */
/* ------------------------------------------------------------------ */
function guidePages() {
  layout({
    path: "conseils.html", section: "conseils", crumbs: [["Conseils", "conseils.html"]],
    title: "Conseils · Hottes, extraction et cuisines | Hottes ta cuisine",
    desc: `${guides.length} conseils pratiques : réglementation, sécurité incendie, hygiène, entretien des hottes et des cuisines.`,
    label: "Conseils", h1: "Ce que nous expliquons chaque jour.",
    lead: "Réglementation, sécurité, hygiène, entretien. Des réponses claires, sans jargon.",
    body: `<section class="sec"><div class="wrap">
<div class="filters" data-filter><button type="button" data-cat="all" aria-pressed="true">Tout</button>${Object.entries(CATS).map(([k, n]) => `<button type="button" data-cat="${k}" aria-pressed="false">${n}</button>`).join("")}<input type="search" placeholder="Rechercher" aria-label="Rechercher un conseil"></div>
${postList(guides)}
</div></section>${cta()}`
  });
  guides.forEach((g, i) => {
    const { html, list } = toc(cleanBody(g.body));
    const same = guides.filter((x) => x.cat === g.cat && x.slug !== g.slug).slice(0, 3);
    const svc = (g.services || []).filter((x) => svcBy[x]);
    const next = guides[(i + 1) % guides.length];
    layout({
      path: `conseils/${g.slug}.html`, section: "conseils", ogType: "article",
      crumbs: [["Conseils", "conseils.html"], [g.title, `conseils/${g.slug}.html`]],
      title: `${g.title} | Hottes ta cuisine`, desc: g.desc,
      label: CATS[g.cat], h1: g.title, lead: g.desc,
      meta: `<p class="meta"><span>${readMin(g.body)} min de lecture</span><span>Mis à jour en ${SITE.updatedLabel}</span></p>`,
      priority: 0.7,
      body: `
<section class="sec"><div class="wrap editorial">
  <aside>${list.length > 2 ? `<span class="label">Sommaire</span><ol>${list.map(([id, t]) => `<li><a href="#${id}">${t}</a></li>`).join("")}</ol>` : ""}</aside>
  <article class="prose">${html}
  ${svc.length ? `<div class="note"><p>Besoin d'un professionnel ? ${svc.map((x) => `<a href="{r}prestations/${x}.html">${svcShort[x][0]}</a>`).join(", ")}. Devis gratuit sous 24 heures.</p></div>` : ""}
  <p class="small">Rédigé par l'équipe technique de ${SITE.name}.</p></article>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label">À lire ensuite</p><div><h2>Dans la même rubrique</h2></div></div>${postList(same.length ? same : [next])}</div></section>
${cta()}`,
      jsonld: [{ "@context": "https://schema.org", "@type": "Article", headline: g.title, description: g.desc, dateModified: SITE.updated, datePublished: SITE.updated, inLanguage: "fr-FR", author: { "@type": "Organization", name: SITE.name }, publisher: { "@type": "Organization", name: SITE.name }, mainEntityOfPage: SITE.url + "/conseils/" + g.slug + ".html" }]
    });
  });
}

/* ------------------------------------------------------------------ */
/* Zones et villes                                                      */
/* ------------------------------------------------------------------ */
function placePages() {
  layout({
    path: "zones.html", section: "zones", crumbs: [["Zones", "zones.html"]],
    title: "Zones d'intervention · Île-de-France | Hottes ta cuisine",
    desc: `Nettoyage de hotte dans ${cities.length} villes d'Île-de-France, depuis ${SITE.city} (93).`,
    label: "Zones", h1: "Partout en Île-de-France.",
    lead: `Depuis ${SITE.city}, nous rejoignons Paris et les huit départements. Les délais varient peu, le travail pas du tout.`,
    actions: `<a class="btn btn-line" href="{r}ou-nous-trouver.html">Où nous trouver</a>`,
    body: `<section class="sec"><div class="wrap">${depts.map((d) => `<div class="dept"><h3><a href="{r}zones/${d.slug}.html" style="text-decoration:none">${d.name}</a><small>${d.code} · ${cities.filter((c) => c.dept === d.code).length} villes</small></h3><ul class="city-cols">${cities.filter((c) => c.dept === d.code).map((c) => `<li><a href="{r}villes/nettoyage-hotte-${c.slug}.html">${c.name}</a></li>`).join("")}</ul></div>`).join("")}</div></section>${cta()}`
  });
  for (const d of depts) {
    const list = cities.filter((c) => c.dept === d.code);
    layout({
      path: `zones/${d.slug}.html`, section: "zones",
      crumbs: [["Zones", "zones.html"], [d.name, `zones/${d.slug}.html`]],
      title: `Nettoyage de hotte ${d.art} ${d.name} (${d.code}) | Hottes ta cuisine`,
      desc: `Dégraissage de hotte, conduit et extracteur, nettoyage de cuisine ${d.art} ${d.name} (${d.code}). Certificat, devis gratuit.`,
      label: `Département ${d.code}`, h1: `Nettoyage de hotte ${d.art} ${d.name}`, lead: d.desc,
      actions: `<a class="btn" href="{r}reservation.html">Réserver</a><a class="btn btn-line" href="tel:${SITE.tel}">${SITE.phone}</a>`,
      priority: 0.7,
      body: `<section class="sec"><div class="wrap">
<div class="head"><p class="label"><b>01</b>Villes</p><div><h2>Où nous intervenons</h2><p>Et dans toutes les autres communes du département.</p></div></div>
<ul class="city-cols">${list.map((c) => `<li><a href="{r}villes/nettoyage-hotte-${c.slug}.html">${c.name}</a></li>`).join("")}</ul>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>02</b>Prestations</p><div><h2>Ce que nous faisons</h2></div></div>${svcIndex(MAIN)}</div></section>${cta()}`
    });
  }

  const intros = [
    (c, dist) => `Nous dégraissons les hottes, conduits et extracteurs des cuisines ${aV(c.name).replace(/^à /, "de ").replace(/^au /, "du ")}. Notre base est à ${dist} km.`,
    (c, dist) => `Restaurants, cuisines collectives, particuliers : nous intervenons ${aV(c.name)}, à ${dist} km de notre base.`,
    (c, dist) => `Hotte, conduit, tourelle, cuisine. Nous venons ${aV(c.name)} depuis ${SITE.city}, à ${dist} km.`
  ];
  const generic = {
    "75": "À Paris, les cuisines sont souvent en pied d'immeuble, avec des conduits qui montent sur plusieurs étages. Nous coordonnons avec les syndics.",
    "93": "La Seine-Saint-Denis est notre département. Ce sont nos délais les plus courts.",
    "92": "Restaurants de quartier et grandes cuisines d'entreprise.",
    "94": "Restaurants, cuisines collectives et métiers de bouche.",
    "95": "Restaurants de centre-ville, hôtels et zones commerciales.",
    "77": "Des passages regroupés par secteur pour garder des délais courts.",
    "91": "Restaurants, cantines et restauration d'entreprise.",
    "78": "Restaurants et hôtels de centre-ville, restauration d'entreprise."
  };
  for (const c of cities) {
    const d = deptBy[c.dept];
    const dist = Math.max(1, Math.round(km(base, c)));
    const delay = dist <= 12 ? "sous 48 à 72 heures" : dist <= 25 ? "sous 3 à 5 jours" : "dans la semaine";
    const near = cities.filter((x) => x.slug !== c.slug).map((x) => [x, km(c, x)]).sort((a, b) => a[1] - b[1]).slice(0, 8).map((x) => x[0]);
    const q = `?ville=${encodeURIComponent(c.name)}`;
    const faq = [
      [`Intervenez-vous la nuit ${aV(c.name)} ?`, "Oui. La nuit, tôt le matin ou le jour de fermeture, pour ne jamais gêner le service."],
      ["Quel prix ?", "Sur devis gratuit, déplacement compris, selon la hotte, le conduit et l'accès au toit."],
      ["Sous quel délai ?", `Devis sous 24 heures. Intervention ${delay} en général, plus vite en cas d'urgence.`]
    ];
    layout({
      path: `villes/nettoyage-hotte-${c.slug}.html`, section: "zones",
      crumbs: [["Zones", "zones.html"], [d.name, `zones/${d.slug}.html`], [c.name, `villes/nettoyage-hotte-${c.slug}.html`]],
      title: `Nettoyage de hotte ${aV(c.name)}${c.dept !== "75" ? ` (${c.dept})` : ""} | Hottes ta cuisine`,
      desc: `Nettoyage et dégraissage de hotte ${aV(c.name)} : hotte, conduit, tourelle, cuisine. Techniciens diplômés, certificat, devis gratuit.`,
      label: `${d.name} · ${d.code}`, h1: `Nettoyage de hotte ${aV(c.name)}`,
      lead: intros[hash(c.slug) % intros.length](c, dist),
      actions: `<a class="btn" href="{r}reservation.html${q}">Réserver</a><a class="btn btn-line" href="tel:${SITE.tel}">${SITE.phone}</a>`,
      body: `
<section class="sec"><div class="wrap split top">
  <div><p class="label"><b>01</b>Sur place</p><p class="statement mt1" style="font-size:clamp(1.4rem,2.2vw,1.9rem);line-height:1.35">${c.note || generic[c.dept]}</p></div>
  <dl class="kv">
    <div><dt>Distance</dt><dd>${dist} km de ${SITE.city}</dd></div>
    <div><dt>Délai</dt><dd>Devis sous 24 h, intervention ${delay}</dd></div>
    <div><dt>Créneaux</dt><dd>Nuit, matin, jour de fermeture</dd></div>
    <div><dt>Prix</dt><dd>Sur devis, déplacement compris</dd></div>
    <div><dt>Remis</dt><dd>Certificat et photos</dd></div>
  </dl>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>02</b>Prestations</p><div><h2>${c.name}</h2></div></div>${svcIndex(MAIN)}</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>03</b>Questions</p><div><h2>En bref</h2></div></div>${faqHtml(faq)}</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>04</b>Autour</p><div><h2>Aussi près ${deV(c.name)}</h2></div></div>
<ul class="pills">${near.map((x) => `<li><a href="{r}villes/nettoyage-hotte-${x.slug}.html">${x.name}</a></li>`).join("")}<li><a href="{r}zones/${d.slug}.html">${d.name}</a></li></ul></div></section>
${cta(`Une hotte ${aV(c.name)} ?`, "Appelez-nous ou réservez en ligne. Devis gratuit sous 24 heures.", q)}`,
      jsonld: [
        { "@context": "https://schema.org", "@type": "Service", name: `Nettoyage de hotte ${aV(c.name)}`, provider: { "@id": SITE.url + "/#business", ...provider }, areaServed: { "@type": "City", name: c.name } },
        faqLd(faq)
      ]
    });
  }
}

/* ------------------------------------------------------------------ */
/* Pages de fond                                                        */
/* ------------------------------------------------------------------ */
function corePages() {
  layout({
    path: "notre-savoir-faire.html", section: "savoir", crumbs: [["Savoir-faire", "notre-savoir-faire.html"]],
    title: "Savoir-faire · Techniciens formés et diplômés | Hottes ta cuisine",
    desc: "Des techniciens diplômés des métiers de la propreté, spécialisés dans le dégraissage des hottes et des cuisines. Nos formations, nos engagements, notre matériel.",
    label: "Savoir-faire", h1: "Un seul métier, fait sérieusement.",
    lead: "Les hottes, l'extraction et les cuisines. Rien d'autre. C'est ce qui nous permet de bien le faire.",
    body: `
<section class="sec"><div class="wrap split">
  <div class="frame reveal" style="aspect-ratio:4/5">${img("{r}", "tourelle")}</div>
  <div><p class="label"><b>01</b>L'équipe</p><h2 class="mt1">Formés et diplômés.</h2><p class="mt1">Un dégraissage d'extraction se fait avec des produits puissants, en hauteur, sur des moteurs, au-dessus d'une cuisine. Cela ne s'improvise pas.</p><p>Nos techniciens sont diplômés des métiers de la propreté. Chaque nouveau venu suit notre protocole avant d'intervenir seul.</p></div>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>02</b>Formations</p><div><h2>Ce qu'ils savent faire</h2></div></div>
<div class="cols c3">${creds.map(([t, d], i) => `<div class="col reveal"><span class="n">${pad(i + 1)}</span><h3>${t}</h3><p>${d}</p></div>`).join("")}</div></div></section>
<section class="sec-dark"><div class="wrap"><div class="head"><p class="label"><b>03</b>Engagements</p><div><h2>Ce que nous promettons</h2></div></div>
<div class="cols c4">${[["Le circuit complet", "Rien n'est laissé de côté. Ce qui est inaccessible est écrit."], ["La transparence", "Des photos à chaque trappe, un certificat honnête."], ["Votre service d'abord", "Nous venons quand vous êtes fermés."], ["La reprise", "Un point non conforme ? Nous revenons, sans frais."]].map(([t, d], i) => `<div class="col"><span class="n">${pad(i + 1)}</span><h3>${t}</h3><p>${d}</p></div>`).join("")}</div></div></section>
<section class="sec" style="padding-top:var(--s1)"><div class="wrap split top">
<div><p class="label"><b>04</b>Matériel</p><h2 class="mt1">Des outils de professionnels</h2></div>
<ul class="list">${["Brosses rotatives pour conduits ronds et rectangulaires", "Grattoirs et raclettes inox", "Canons à mousse dégraissante", "Bacs de trempage chauffés pour les filtres", "Vapeur et haute pression maîtrisée", "Protections antichute pour la toiture"].map((x) => `<li>${x}</li>`).join("")}</ul>
</div></section>${cta()}`
  });

  layout({
    path: "methode.html", section: "savoir", crumbs: [["Méthode", "methode.html"]],
    title: "Méthode · Dégraissage de hotte étape par étape | Hottes ta cuisine",
    desc: "Notre méthode de dégraissage en quatre temps et le schéma du circuit d'extraction : hotte, filtres, plénum, conduit, tourelle.",
    label: "Méthode", h1: "Suivre la graisse jusqu'au bout.",
    lead: "Elle monte des feux, traverse les filtres, se dépose dans le plénum, le conduit, puis sur la turbine. Nous suivons le même chemin.",
    body: `
<section class="sec"><div class="wrap split top"><div class="reveal">${diagram()}</div>
<div><p class="label"><b>01</b>Le circuit</p><p class="mt1">Touchez un numéro pour voir ce que nous faisons à chaque étage.</p></div></div></section>
<section class="sec-dark"><div class="wrap"><div class="head"><p class="label"><b>02</b>Quatre temps</p><div><h2>Toujours dans cet ordre</h2></div></div>${methodCols(true)}</div></section>
<section class="sec" style="padding-top:var(--s1)"><div class="wrap editorial"><aside><span class="label"><b>03</b>Procédés</span></aside>
<div class="prose"><table><thead><tr><th>Procédé</th><th>Pour</th></tr></thead><tbody>
<tr><td>Grattage</td><td>Dépôts épais ou carbonisés, avant tout produit</td></tr>
<tr><td>Mousse dégraissante</td><td>Parois et plafonds, grâce au temps de contact</td></tr>
<tr><td>Brossage rotatif</td><td>Intérieur des conduits, par les trappes</td></tr>
<tr><td>Trempage à chaud</td><td>Filtres et pièces démontables</td></tr>
<tr><td>Vapeur</td><td>Finitions et zones sensibles à l'eau</td></tr>
<tr><td>Haute pression</td><td>Turbines, avec récupération des eaux</td></tr></tbody></table>
<h2>Sécurité</h2><p>Extracteur consigné, protections individuelles, antichute en toiture. Les eaux grasses sont récupérées, jamais rejetées dans les évacuations pluviales.</p></div></div></section>
<section class="sec"><div class="wrap split"><div><p class="label"><b>04</b>En vidéo</p><h2 class="mt1">Sur le toit</h2><p class="mt1">Dégraissage d'une tourelle, filmé pendant une intervention.</p></div><div class="frame" style="aspect-ratio:9/16;max-width:420px">${V.site("{r}")}</div></div></section>
${cta()}`
  });

  const regFaq = [
    ["Une fois par an, pour tous les restaurants ?", "Pour les établissements recevant du public, oui, au minimum. Les autres cuisines professionnelles restent soumises au Code du travail, au bail et à l'assurance."],
    ["Qui contrôle ?", "La commission de sécurité, les services sanitaires, et l'expert de l'assureur en cas de sinistre."],
    ["Que risque-t-on sans certificat ?", "Un avis défavorable, une mise en demeure, ou une indemnisation discutée après un sinistre, selon votre contrat."]
  ];
  layout({
    path: "reglementation.html", section: "savoir", crumbs: [["Réglementation", "reglementation.html"]],
    title: "Réglementation · Nettoyage de hotte professionnelle | Hottes ta cuisine",
    desc: "Article GC 21 du règlement de sécurité ERP, hygiène, Code du travail, assurance : la réglementation du nettoyage des hottes, simplement.",
    label: "Réglementation", h1: "Ce que dit la loi, simplement.",
    lead: "Quatre textes, une même conclusion : l'extraction se nettoie en entier, au moins une fois par an, et on garde la preuve.",
    body: `<section class="sec"><div class="wrap editorial"><aside><span class="label">Sommaire</span><ol><li><a href="#erp">Sécurité incendie</a></li><li><a href="#hyg">Hygiène</a></li><li><a href="#trav">Code du travail</a></li><li><a href="#ass">Assurance et bail</a></li></ol></aside>
<div class="prose">
<h2 id="erp">Sécurité incendie</h2><p>Le règlement de sécurité des établissements recevant du public (arrêté du 25 juin 1980) consacre une section aux cuisines. Son <strong>article GC 21</strong> prévoit un nettoyage de l'installation d'extraction <strong>au moins une fois par an</strong> : conduits, filtres et extracteurs compris.</p>
<h2 id="hyg">Hygiène</h2><p>Le règlement (CE) n° 852/2004 impose des locaux et des équipements propres et entretenus. Une hotte qui goutte se remarque lors d'une inspection.</p>
<h2 id="trav">Code du travail</h2><p>L'employeur maintient les installations d'aération en bon état et prévient le risque incendie. Cela vaut aussi pour les cuisines sans public.</p>
<h2 id="ass">Assurance et bail</h2><p>Votre contrat peut fixer une fréquence et exiger des justificatifs. Votre bail répartit les charges d'entretien. Après un sinistre, l'expert demandera les certificats.</p>
<div class="note"><p>Résumé pratique. Il ne remplace ni les textes officiels (Légifrance), ni l'avis de votre préventionniste ou de votre assureur.</p></div>
</div></div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label">Questions</p><div><h2>En bref</h2></div></div>${faqHtml(regFaq)}</div></section>${cta()}`,
    jsonld: [faqLd(regFaq)]
  });

  layout({
    path: "certificat-de-degraissage.html", section: "savoir", crumbs: [["Certificat", "certificat-de-degraissage.html"]],
    title: "Certificat de dégraissage de hotte | Hottes ta cuisine",
    desc: "Le certificat remis après chaque nettoyage de hotte : éléments traités, réserves, photos. Le document attendu par l'assureur et la commission de sécurité.",
    label: "Certificat", h1: "Une preuve, pas une formalité.",
    lead: "Remis à chaque intervention. Il dit ce qui a été fait, ce qui ne l'a pas été, et quand revenir.",
    body: `<section class="sec"><div class="wrap split top">
<div class="certif reveal"><span class="stamp">Spécimen</span><span class="label">Certificat de nettoyage</span><h3>Installation d'extraction</h3>
<table><tbody>${[["Établissement", "Nom, adresse, activité"], ["Date", "JJ/MM/AAAA, 23 h – 3 h"], ["Technicien", "Nom, qualification"], ["Hotte", "Longueur, dégraissage intérieur et extérieur"], ["Filtres", "Nombre, type, trempage"], ["Plénum", "Gratté et dégraissé"], ["Conduit", "Longueur traitée, trappes"], ["Extracteur", "Turbine dégraissée, observations"], ["Réserves", "Zones inaccessibles, anomalies"], ["Prochain passage", "Date conseillée"]].map(([a, b]) => `<tr><th>${a}</th><td>${b}</td></tr>`).join("")}</tbody></table>
<p class="small mt1 mb0">Annexe : photos avant et après. Signatures.</p></div>
<div><p class="label"><b>01</b>Pourquoi le nôtre tient</p><ul class="list mt1">${["Délivré uniquement après une intervention réelle", "Chaque élément du circuit est détaillé", "Les zones inaccessibles sont écrites", "Photos prises à chaque trappe", "Envoyé en PDF pour le registre de sécurité"].map((x) => `<li>${x}</li>`).join("")}</ul>
<p class="mt2">À présenter à la commission de sécurité, à l'assureur, au bailleur ou au syndic, et à un repreneur.</p><a class="arrow" href="{r}conseils/certificat-nettoyage-hotte-assurance.html">Le certificat et l'assurance</a></div>
</div></section>${cta("Un certificat à renouveler ?")}`
  });

  layout({
    path: "realisations.html", section: "real", crumbs: [["Réalisations", "realisations.html"]],
    title: "Réalisations · Photos et vidéos de chantier | Hottes ta cuisine",
    desc: "Photos et vidéos d'interventions réelles : tourelles d'extraction, conduits, cuisines professionnelles.",
    label: "Réalisations", h1: "Sur le chantier.",
    lead: "Des images de nos interventions. Pas de banque d'images.",
    body: `
<section class="sec"><div class="wrap gallery">
  <figure class="a reveal"><div class="m">${img("{r}", "tourelle")}</div><figcaption>Tourelle d'extraction. Mousse dégraissante sur la turbine, en toiture.</figcaption></figure>
  <figure class="b reveal"><div class="m">${img("{r}", "conduit")}</div><figcaption>Départ de conduit, vu depuis la hotte, avant intervention.</figcaption></figure>
  <figure class="c reveal"><div class="m">${V.loop("{r}")}</div><figcaption>Rinçage de la turbine.</figcaption></figure>
</div></section>
<section class="sec"><div class="wrap split">
  <div><p class="label"><b>01</b>Vidéo</p><h2 class="mt1">Quarante secondes en toiture</h2><p class="mt1">Un extracteur de cuisine pendant son dégraissage. Graisse, mousse, rinçage.</p></div>
  <div class="frame" style="aspect-ratio:9/16;max-width:420px">${V.site("{r}")}</div>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><p class="label"><b>02</b>Cuisines</p><div><h2>Avant, après</h2><p>Chaque paire vient d'une même intervention, au même endroit.</p></div></div>
<div class="cols c2">
<figure class="reveal" style="margin:0"><div class="ba"><div class="m"><img src="{r}assets/photos/avant-plan-travail.webp" alt="Inox encrassé, avant" loading="lazy"></div><div class="m"><img src="{r}assets/photos/apres-plan-travail.webp" alt="Même inox, après" loading="lazy"></div></div><figcaption>Plan de travail inox. Avant, après.</figcaption></figure>
<figure class="reveal" style="margin:0"><div class="ba"><div class="m"><img src="{r}assets/photos/avant-frigo.webp" alt="Réfrigération, avant" loading="lazy"></div><div class="m"><img src="{r}assets/photos/apres-frigo.webp" alt="Réfrigération, après" loading="lazy"></div></div><figcaption>Réfrigération. Avant, après.</figcaption></figure>
</div></div></section>
${cta()}`
  });

  layout({
    path: "diagnostic.html", section: "savoir", crumbs: [["Diagnostic", "diagnostic.html"]],
    title: "Diagnostic gratuit · Fréquence de dégraissage | Hottes ta cuisine",
    desc: "Calculez la fréquence de dégraissage adaptée à votre hotte et vérifiez votre conformité en trente secondes.",
    label: "Outil", h1: "Tous les combien ?",
    lead: "Cinq questions pour estimer le bon rythme de dégraissage. Puis huit points pour vérifier votre conformité.",
    body: `<section class="sec"><div class="wrap split top">
<div><p class="label"><b>01</b>Fréquence</p><div class="mt2">${freqTool()}</div></div>
<div><p class="label"><b>02</b>Conformité</p><div class="tool mt2"><form class="form" data-conform-tool data-devis="{r}devis.html">
<div class="choices" style="flex-direction:column;align-items:stretch">${["Certificat de moins de 12 mois", "Il couvre hotte, filtres, conduit et extracteur", "Filtres à chicanes, nettoyés chaque semaine", "Aucune graisse ne goutte ni ne coule en toiture", "Le conduit a des trappes de visite", "Le registre de sécurité est à jour", "Un extincteur pour feux d'huiles près des feux", "L'équipe connaît les gestes en cas de feu"].map((t, i) => `<label class="choice block"><input type="checkbox" name="c${i}"><span>${t}</span></label>`).join("")}</div>
<div><button class="btn" type="submit">Voir mon score</button></div></form><div class="tool-result" aria-live="polite"></div></div></div>
</div></section>${cta()}`
  });

  const faqAll = [
    ...homeFaq,
    ["Remettez-vous un certificat ?", "Oui, à chaque intervention, avec les photos avant et après."],
    ["Ramonage ou dégraissage ?", "Le ramonage concerne les conduits de fumée (four à bois, chaudière). Le dégraissage concerne l'extraction des hottes. Deux opérations, deux certificats."],
    ["Et les conduits sans trappe ?", "Nous nettoyons tout ce qui est accessible, et nous l'écrivons sur le certificat, avec nos conseils pour la pose de trappes."],
    ["Faut-il être présent ?", "Pour la première fois, au début et à la fin. Ensuite, un accès convenu suffit."],
    ["Vos produits sont-ils sûrs pour la cuisine ?", "Ils sont dosés, puis rincés des surfaces en contact alimentaire. La cuisine est utilisable dès notre départ."],
    ["Pouvez-vous refaire un nettoyage raté ?", "Oui. Constat, nettoyage complet, réception avec vous sur la base du constat."],
    ["Chez les particuliers aussi ?", "Oui, pour les hottes domestiques et les cuisines, partout en Île-de-France."],
    ["En urgence ?", "Appelez-nous. Nous faisons le maximum, nuit et week-end compris."]
  ];
  layout({
    path: "faq.html", section: "savoir", crumbs: [["Questions fréquentes", "faq.html"]],
    title: "Questions fréquentes · Nettoyage de hotte | Hottes ta cuisine",
    desc: "Prix, fréquence, certificat, déroulé, qualifications, urgence : les réponses courtes aux questions que l'on nous pose.",
    label: "Questions", h1: "Questions fréquentes.", lead: "Les réponses courtes. Pour le reste, un appel.",
    body: `<section class="sec"><div class="wrap">${faqHtml(faqAll)}</div></section>${cta()}`, jsonld: [faqLd(faqAll)]
  });

  /* Réservation */
  const ch = (name, list, type = "radio") => list.map(([v, s]) => `<label class="choice"><input type="${type}" name="${name}" value="${esc(v)}"${type === "checkbox" && s ? ` data-slug="${s}"` : ""}><span>${v}${type === "radio" && s ? `<small>${s}</small>` : ""}</span></label>`).join("");
  const opts = (list) => list.map((o) => `<option>${o}</option>`).join("");
  layout({
    path: "reservation.html", section: "", crumbs: [["Réservation", "reservation.html"]],
    title: "Réserver un nettoyage de hotte | Hottes ta cuisine",
    desc: "Réservez en ligne votre nettoyage de hotte ou de cuisine : prestation, date, créneau, coordonnées. Confirmation et devis sous 24 heures.",
    label: "Réservation", h1: "Réserver.", lead: "Deux minutes. Nous vous rappelons pour confirmer, puis vous recevez le devis sous 24 heures.",
    scripts: ["assets/js/reservation.js"],
    body: `<section class="sec"><div class="wrap">
<noscript><p>La réservation en ligne demande JavaScript. <a href="devis.html">Demandez un devis</a> ou appelez le <a href="tel:${SITE.tel}">${SITE.phone}</a>.</p></noscript>
<div class="resa" id="resa" hidden><div>
<ol class="resa-steps">${["Prestation", "Installation", "Date", "Coordonnées", "Envoi"].map((t, i) => `<li><button type="button"><span>${pad(i + 1)}</span>${t}</button></li>`).join("")}</ol>
<form id="resa-form" action="${SITE.form}" method="POST" novalidate>
<input type="hidden" name="_subject" value="Nouvelle réservation · ${SITE.name}"><input type="hidden" name="_next" value="${SITE.url}/merci.html"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table"><input type="hidden" name="Récapitulatif" id="resa-recap"><input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
<div class="resa-panel" data-step="1"><h2>Pour quel établissement ?</h2>
<div class="choices">${ch("profil", [["Restaurant"], ["Restauration rapide"], ["Hôtel"], ["Collectivité"], ["Boulangerie, traiteur"], ["Dark kitchen, food truck"], ["Particulier"], ["Autre"]])}</div>
<p class="q">Prestations souhaitées</p><div class="choices">${services.map((s) => `<label class="choice"><input type="checkbox" name="prestations" value="${esc(svcShort[s.slug][0])}" data-slug="${s.slug}"><span>${svcShort[s.slug][0]}</span></label>`).join("")}</div></div>
<div class="resa-panel" data-step="2" hidden><h2>Votre installation</h2><div class="form">
<div class="row"><div><label for="r-nb">Nombre de hottes</label><select id="r-nb" name="nb_hottes">${opts(["1", "2", "3", "4 ou plus", "Je ne sais pas"])}</select></div><div><label for="r-long">Longueur de la hotte</label><select id="r-long" name="longueur">${opts(["Moins de 2 m", "2 à 4 m", "4 à 6 m", "Plus de 6 m", "Hotte domestique", "Je ne sais pas"])}</select></div></div>
<div class="row"><div><label for="r-acces">Accès à l'extracteur</label><select id="r-acces" name="acces">${opts(["Toit accessible", "Toit difficile d'accès", "Caisson en local technique", "Je ne sais pas"])}</select></div><div><label for="r-dernier">Dernier dégraissage</label><select id="r-dernier" name="dernier">${opts(["Moins de 6 mois", "6 à 12 mois", "Plus d'un an", "Jamais, ou je ne sais pas"])}</select></div></div>
<div><label for="r-msg">Précisions</label><textarea id="r-msg" name="message" placeholder="Type de cuisson, accès, jour de fermeture…"></textarea></div></div></div>
<div class="resa-panel" data-step="3" hidden><h2>Quand ?</h2><div class="split top" style="gap:48px">
<div class="cal" id="resa-cal"><div class="cal-head"><button type="button" data-cal-prev aria-label="Mois précédent">‹</button><strong></strong><button type="button" data-cal-next aria-label="Mois suivant">›</button></div><div class="cal-grid"></div></div>
<div><input type="hidden" name="date" id="r-date"><label class="choice block"><input type="checkbox" id="r-flex" name="flexible" value="Oui"><span>Je suis flexible</span></label>
<p class="q">Créneau</p><div class="choices">${ch("creneau", [["Tôt le matin", "6 h – 10 h"], ["Entre deux services", "15 h – 18 h"], ["Après le service", "22 h – 3 h"], ["Jour de fermeture", "Journée"], ["En journée", "Particuliers"]])}</div></div></div></div>
<div class="resa-panel" data-step="4" hidden><h2>Vos coordonnées</h2><div class="form">
<div class="row"><div><label for="r-nom">Nom *</label><input id="r-nom" type="text" name="nom" required data-label="votre nom" autocomplete="name"></div><div><label for="r-soc">Établissement</label><input id="r-soc" type="text" name="societe" autocomplete="organization"></div></div>
<div class="row"><div><label for="r-tel">Téléphone *</label><input id="r-tel" type="tel" name="tel" required data-label="votre téléphone" autocomplete="tel" pattern="[0-9 +().-]{9,}"></div><div><label for="r-mail">E-mail *</label><input id="r-mail" type="email" name="email" required data-label="votre e-mail" autocomplete="email"></div></div>
<div><label for="r-adr">Adresse</label><input id="r-adr" type="text" name="adresse" autocomplete="street-address"></div>
<div class="row"><div><label for="r-cp">Code postal *</label><input id="r-cp" type="text" name="cp" required data-label="le code postal" inputmode="numeric" pattern="[0-9]{5}" autocomplete="postal-code"></div><div><label for="r-ville">Ville *</label><input id="r-ville" type="text" name="ville" required data-label="la ville" autocomplete="address-level2"></div></div></div></div>
<div class="resa-panel" data-step="5" hidden><h2>On vérifie ?</h2><dl class="kv recap" id="resa-recap-view"></dl>
<label class="choice block mt2"><input type="checkbox" id="r-rgpd" name="consentement" value="Oui"><span>J'accepte d'être rappelé pour confirmer le rendez-vous</span></label>
<p class="small mt1">Rien n'est dû à ce stade. Le rendez-vous est confirmé par téléphone, après acceptation du devis.</p></div>
<p class="resa-error" id="resa-error" role="alert"></p>
<div class="resa-nav"><button type="button" class="btn btn-line" id="resa-prev">Retour</button><button type="button" class="btn" id="resa-next">Continuer</button><button type="submit" class="btn" id="resa-submit" hidden>Envoyer</button></div>
</form></div>
<aside class="summary"><span class="label">Votre demande</span><dl><dt>Établissement</dt><dd id="s-profil">—</dd><dt>Prestations</dt><dd id="s-presta">—</dd><dt>Date</dt><dd id="s-date">—</dd><dt>Lieu</dt><dd id="s-lieu">—</dd><dt>Prix</dt><dd>Sur devis, sous 24 h</dd></dl>
<p class="small mt2">Plus simple ? <a href="tel:${SITE.tel}">${SITE.phone}</a></p></aside>
</div></div></section>`
  });

  layout({
    path: "devis.html", section: "", crumbs: [["Devis", "devis.html"]],
    title: "Devis gratuit · Nettoyage de hotte et de cuisine | Hottes ta cuisine",
    desc: "Demandez un devis gratuit pour le nettoyage de votre hotte, conduit ou cuisine. Réponse sous 24 heures, photos bienvenues.",
    label: "Devis", h1: "Un devis, gratuit.", lead: "Quelques lignes, une ou deux photos si vous pouvez. Réponse sous 24 heures.",
    body: `<section class="sec"><div class="wrap split top"><form class="form" action="${SITE.form}" method="POST" enctype="multipart/form-data">
<input type="hidden" name="_subject" value="Demande de devis · ${SITE.name}"><input type="hidden" name="_next" value="${SITE.url}/merci.html"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table"><input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
<div class="row"><div><label for="d-nom">Nom *</label><input id="d-nom" type="text" name="Nom" required autocomplete="name"></div><div><label for="d-soc">Établissement</label><input id="d-soc" type="text" name="Établissement"></div></div>
<div class="row"><div><label for="d-tel">Téléphone *</label><input id="d-tel" type="tel" name="Téléphone" required autocomplete="tel"></div><div><label for="d-mail">E-mail *</label><input id="d-mail" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div><label for="d-cp">Code postal *</label><input id="d-cp" type="text" name="Code postal" required inputmode="numeric" pattern="[0-9]{5}"></div><div><label for="d-type">Vous êtes</label><select id="d-type" name="Profil">${opts(["Restaurant", "Collectivité ou santé", "Hôtel", "Boulangerie, traiteur", "Dark kitchen, food truck", "Particulier", "Syndic, gestionnaire"])}</select></div></div>
<div><label for="d-msg">Votre besoin *</label><textarea id="d-msg" name="Message" required placeholder="Type de cuisine, taille de la hotte, date souhaitée…"></textarea></div>
<div><label for="d-ph">Photos (facultatif)</label><input id="d-ph" type="file" name="attachment" accept="image/*"></div>
<label class="choice block"><input type="checkbox" name="Consentement" value="Oui" required><span>J'accepte d'être recontacté au sujet de ma demande</span></label>
<div><button class="btn" type="submit">Envoyer</button></div></form>
<div><p class="label"><b>—</b>Ou directement</p><p class="statement mt1" style="font-size:clamp(1.8rem,3vw,2.6rem)"><a href="tel:${SITE.tel}" style="text-decoration:none">${SITE.phone}</a></p><p class="muted">${SITE.hours}</p></div>
</div></section>`
  });

  layout({
    path: "contact.html", section: "contact", crumbs: [["Contact", "contact.html"]],
    title: "Contact | Hottes ta cuisine",
    desc: `Appelez Hottes ta cuisine au ${SITE.phone} (${SITE.hours}) ou écrivez-nous. Nettoyage de hotte et de cuisine en Île-de-France.`,
    label: "Contact", h1: "Le plus simple, c'est d'appeler.",
    lead: "Un technicien vous répond, sans standard.",
    jsonld: [{ "@context": "https://schema.org", ...provider }],
    body: `<section class="sec"><div class="wrap split top">
<div><p class="statement" style="font-size:clamp(2.2rem,4.6vw,4rem)"><a href="tel:${SITE.tel}" style="text-decoration:none">${SITE.phone}</a></p>
<dl class="kv mt2"><div><dt>Standard</dt><dd>${SITE.hours}</dd></div><div><dt>Interventions</dt><dd>7j/7, jour et nuit, sur rendez-vous</dd></div><div><dt>Base</dt><dd>${SITE.cp} ${SITE.city}</dd></div><div><dt>Zone</dt><dd>Paris et Île-de-France</dd></div></dl>
<div class="actions mt2"><a class="btn" href="{r}reservation.html">Réserver</a><a class="arrow" href="{r}ou-nous-trouver.html">Où nous trouver</a></div>
<p class="small mt2">Feu en cours : appelez le 18 ou le 112.</p></div>
<form class="form" action="${SITE.form}" method="POST"><input type="hidden" name="_subject" value="Message · ${SITE.name}"><input type="hidden" name="_next" value="${SITE.url}/merci.html"><input type="hidden" name="_captcha" value="false"><input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
<p class="label">Ou écrivez-nous</p>
<div class="row"><div><label for="c-nom">Nom *</label><input id="c-nom" type="text" name="Nom" required autocomplete="name"></div><div><label for="c-tel">Téléphone</label><input id="c-tel" type="tel" name="Téléphone" autocomplete="tel"></div></div>
<div><label for="c-mail">E-mail *</label><input id="c-mail" type="email" name="email" required autocomplete="email"></div>
<div><label for="c-msg">Message *</label><textarea id="c-msg" name="Message" required></textarea></div>
<label class="choice block"><input type="checkbox" name="Consentement" value="Oui" required><span>J'accepte d'être recontacté</span></label>
<div><button class="btn" type="submit">Envoyer</button></div></form>
</div></section>`
  });

  const bbox = [base.lon - 0.05, base.lat - 0.025, base.lon + 0.05, base.lat + 0.025].map((n) => n.toFixed(4)).join("%2C");
  layout({
    path: "ou-nous-trouver.html", section: "zones", crumbs: [["Où nous trouver", "ou-nous-trouver.html"]],
    title: `Où nous trouver · ${SITE.city} (93) | Hottes ta cuisine`,
    desc: `Hottes ta cuisine est basé ${SITE.au} (${SITE.cp}), en Seine-Saint-Denis. Carte, accès et zone d'intervention.`,
    label: "Où nous trouver", h1: `${SITE.city}, Seine-Saint-Denis.`,
    lead: "Au nord-est de Paris, entre l'A1, l'A3 et l'A86. Un bon point de départ pour toute l'Île-de-France.",
    jsonld: [{ "@context": "https://schema.org", ...provider }],
    body: `<section class="sec"><div class="wrap">
<iframe class="map" title="Carte ${SITE.city}" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=${bbox}&amp;layer=mapnik&amp;marker=${base.lat}%2C${base.lon}"></iframe>
<p class="small mt1">Carte © contributeurs OpenStreetMap</p></div></section>
<section class="sec"><div class="wrap split top">
<dl class="kv"><div><dt>Base</dt><dd>${SITE.cp} ${SITE.city}</dd></div><div><dt>Téléphone</dt><dd><a href="tel:${SITE.tel}">${SITE.phone}</a></dd></div><div><dt>Standard</dt><dd>${SITE.hours}</dd></div><div><dt>Accès</dt><dd>A1, A3, A86, N2</dd></div><div><dt>Accueil du public</dt><dd>Non. Nous intervenons chez vous.</dd></div></dl>
<div class="zone">${zoneMap()}</div>
</div></section>${cta()}`
  });

  const legal = (pth, t, h, body) => layout({ path: pth, title: `${t} | ${SITE.name}`, desc: `${t} du site ${SITE.name}.`, h1: h, crumbs: [[t, pth]], priority: 0.2, body: `<section class="sec"><div class="wrap editorial"><aside></aside><div class="prose">${body}</div></div></section>` });
  legal("mentions-legales.html", "Mentions légales", "Mentions légales.", `<h2>Éditeur</h2><p>${SITE.name} est une marque exploitée par ${SITE.legal}.<br>${SITE.street}, ${SITE.cp} ${SITE.city}<br>SIRET ${SITE.siret}<br>${SITE.phone} · ${SITE.email}<br>Directeur de la publication : Mathéo Céleste</p><h2>Hébergement</h2><p>[Nom, adresse et téléphone de l'hébergeur à compléter.]</p><h2>Propriété intellectuelle</h2><p>Textes, schémas, photos et vidéos appartiennent à ${SITE.name}, sauf mention contraire.</p><h2>Crédits</h2><p>Carte © contributeurs OpenStreetMap. Polices : Instrument Serif, Inter (Google Fonts).</p><h2>Responsabilité</h2><p>Les informations réglementaires sont données à titre indicatif et ne remplacent pas les textes officiels.</p>`);
  legal("confidentialite.html", "Confidentialité", "Confidentialité.", `<h2>Ce que nous collectons</h2><p>Les informations saisies dans nos formulaires : nom, établissement, téléphone, e-mail, adresse, message et photos éventuelles.</p><h2>Pourquoi</h2><p>Pour répondre à votre demande, établir un devis et organiser l'intervention. Rien n'est vendu ni cédé.</p><h2>Transmission</h2><p>Les formulaires passent par le service FormSubmit jusqu'à notre messagerie.</p><h2>Durée</h2><p>Trois ans au plus pour une demande sans suite, la durée légale pour les clients.</p><h2>Vos droits</h2><p>Accès, rectification, effacement, opposition : ${SITE.email}. Vous pouvez aussi saisir la CNIL.</p><h2>Cookies</h2><p>Aucun cookie publicitaire, aucune mesure d'audience.</p>`);

  layout({
    path: "plan-du-site.html", title: `Plan du site | ${SITE.name}`, desc: `Toutes les pages du site ${SITE.name}.`, h1: "Plan du site.", crumbs: [["Plan du site", "plan-du-site.html"]], priority: 0.3,
    body: `<section class="sec"><div class="wrap">
<div class="dept"><h3>Pages</h3><ul class="city-cols">${[["index.html", "Accueil"], ["prestations.html", "Prestations"], ["secteurs.html", "Secteurs"], ["notre-savoir-faire.html", "Savoir-faire"], ["methode.html", "Méthode"], ["reglementation.html", "Réglementation"], ["certificat-de-degraissage.html", "Certificat"], ["realisations.html", "Réalisations"], ["diagnostic.html", "Diagnostic"], ["faq.html", "FAQ"], ["conseils.html", "Conseils"], ["zones.html", "Zones"], ["ou-nous-trouver.html", "Où nous trouver"], ["reservation.html", "Réservation"], ["devis.html", "Devis"], ["contact.html", "Contact"]].map(([u, n]) => `<li><a href="{r}${u}">${n}</a></li>`).join("")}</ul></div>
<div class="dept"><h3>Prestations</h3><ul class="city-cols">${services.map((s) => `<li><a href="{r}prestations/${s.slug}.html">${svcShort[s.slug][0]}</a></li>`).join("")}</ul></div>
<div class="dept"><h3>Secteurs</h3><ul class="city-cols">${sectors.map((s) => `<li><a href="{r}secteurs/${s.slug}.html">${s.name}</a></li>`).join("")}</ul></div>
<div class="dept"><h3>Conseils</h3><ul class="city-cols" style="columns:2 320px">${guides.map((g) => `<li><a href="{r}conseils/${g.slug}.html">${g.title}</a></li>`).join("")}</ul></div>
<div class="dept"><h3>Villes</h3><ul class="city-cols">${cities.map((c) => `<li><a href="{r}villes/nettoyage-hotte-${c.slug}.html">${c.name}</a></li>`).join("")}</ul></div>
</div></section>`
  });

  layout({
    path: "merci.html", noindex: true, title: `Merci | ${SITE.name}`, desc: "Votre demande est envoyée.",
    h1: "Merci, c'est reçu.", lead: `Nous vous rappelons rapidement (${SITE.hours}). Le devis suit sous 24 heures.`,
    actions: `<a class="btn" href="{r}index.html">Accueil</a><a class="arrow" href="{r}conseils.html">Lire nos conseils</a>`, body: ""
  });
  layout({
    path: "404.html", noindex: true, title: `Page introuvable | ${SITE.name}`, desc: "Cette page n'existe pas.",
    h1: "Partie par l'extraction.", lead: "Cette page n'existe pas, ou plus.",
    actions: `<a class="btn" href="/index.html">Accueil</a><a class="btn btn-line" href="/prestations.html">Prestations</a>`, body: ""
  });
}

/* ------------------------------------------------------------------ */
/* Génération                                                           */
/* ------------------------------------------------------------------ */
fs.rmSync(DIST, { recursive: true, force: true });
home(); servicePages(); sectorPages(); guidePages(); placePages(); corePages();
for (const p of pages) {
  const f = path.join(DIST, p.path);
  fs.mkdirSync(path.dirname(f), { recursive: true });
  fs.writeFileSync(f, p.html);
}
fs.cpSync(path.join(ROOT, "src/assets"), path.join(DIST, "assets"), { recursive: true });
fs.mkdirSync(path.join(DIST, "assets/img"), { recursive: true });
fs.writeFileSync(path.join(DIST, "assets/img/favicon.svg"), mark().replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" style="color:#191917" ').replace(/currentColor/g, "#191917"));
if (fs.existsSync(path.join(ROOT, "src/og-image.jpg"))) fs.copyFileSync(path.join(ROOT, "src/og-image.jpg"), path.join(DIST, "assets/img/og-image.jpg"));
fs.writeFileSync(path.join(DIST, "assets/img/logo.svg"), `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 60"><g transform="translate(0 4) scale(1.3)" style="color:#191917">${mark().replace(/<\/?svg[^>]*>/g, "").replace(/currentColor/g, "#191917")}</g><text x="68" y="40" font-family="Inter,Arial,sans-serif" font-size="30" font-weight="500" fill="#191917">Hottes <tspan font-family="'Instrument Serif',Georgia,serif" font-style="italic" font-size="36" font-weight="400">ta</tspan> cuisine</text></svg>`);

const indexable = pages.filter((p) => !p.noindex);
fs.writeFileSync(path.join(DIST, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${indexable.map((p) => `  <url><loc>${SITE.url}/${p.path === "index.html" ? "" : p.path}</loc><lastmod>${SITE.updated}</lastmod><priority>${p.priority.toFixed(1)}</priority></url>`).join("\n")}\n</urlset>\n`);
fs.writeFileSync(path.join(DIST, "robots.txt"), `User-agent: *\nAllow: /\nDisallow: /merci.html\n\nSitemap: ${SITE.url}/sitemap.xml\n`);
fs.writeFileSync(path.join(DIST, "llms.txt"), `# ${SITE.name}\n\n> Nettoyage et dégraissage de hottes, conduits d'extraction et cuisines, en Île-de-France. Basé ${SITE.au} (${SITE.cp}).\n\n- Téléphone : ${SITE.phone} (${SITE.hours})\n- Prix : sur devis gratuit, sous 24 heures\n- Circuit complet : hotte, filtres, plénum, conduit, extracteur\n- Techniciens formés et diplômés dans les métiers de la propreté\n- Certificat et photos à chaque intervention\n\nPages : ${SITE.url}/prestations.html · ${SITE.url}/reglementation.html · ${SITE.url}/reservation.html · ${SITE.url}/conseils.html\n`);
console.log(`✔ ${pages.length} pages (${indexable.length} indexables) · prestations ${services.length} · secteurs ${sectors.length} · conseils ${guides.length} · départements ${depts.length} · villes ${cities.length}`);
