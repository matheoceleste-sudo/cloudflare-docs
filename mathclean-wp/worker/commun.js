/* Fonctions partagées : échappement, dates, références, validation. */

const ENTITES = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };

/** Échappe tout ce qui vient du client avant de l'écrire dans du HTML. */
export function ech(v) {
  return String(v == null ? "" : v).replace(/[&<>"']/g, (c) => ENTITES[c]);
}

/** Même chose pour un attribut d'URL. */
export function echUrl(v) {
  return encodeURIComponent(String(v == null ? "" : v));
}

/** Date lisible en heure de Paris : « mardi 14 octobre 2026 ». */
export function dateFr(iso, options) {
  if (!iso) return "";
  const d = new Date(iso);
  if (isNaN(d)) return String(iso);
  return new Intl.DateTimeFormat("fr-FR", {
    timeZone: "Europe/Paris",
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
    ...(options || {}),
  }).format(d);
}

/** Date courte : « 14/10/2026 ». */
export function dateCourte(iso) {
  if (!iso) return "";
  const d = new Date(iso);
  if (isNaN(d)) return String(iso);
  return new Intl.DateTimeFormat("fr-FR", {
    timeZone: "Europe/Paris",
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  }).format(d);
}

/** Montant en euros, séparateur français, sans décimale inutile. */
export function eur(n) {
  if (n == null) return "—";
  return new Intl.NumberFormat("fr-FR", {
    style: "currency",
    currency: "EUR",
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(n);
}

/** Jeton d'adresse : 32 caractères hexadécimaux, imprévisibles. */
export function jeton() {
  const o = new Uint8Array(16);
  crypto.getRandomValues(o);
  return Array.from(o, (b) => b.toString(16).padStart(2, "0")).join("");
}

/** Empreinte d'une adresse IP : on compte les demandes sans conserver l'IP. */
export async function empreinteIp(ip, sel) {
  const d = new TextEncoder().encode(`${sel || "mathclean"}:${ip || ""}`);
  const h = await crypto.subtle.digest("SHA-256", d);
  return Array.from(new Uint8Array(h).slice(0, 12), (b) =>
    b.toString(16).padStart(2, "0")
  ).join("");
}

/**
 * Référence lisible et croissante : MC-2026-0001.
 *
 * Le compteur repart de 1 chaque année. Il est tiré du nombre de demandes
 * déjà créées dans l'année, puis vérifié par la contrainte d'unicité : en cas
 * de collision, l'appelant retente.
 */
export async function prochaineReference(db) {
  const annee = new Intl.DateTimeFormat("fr-FR", {
    timeZone: "Europe/Paris",
    year: "numeric",
  }).format(new Date());
  const r = await db
    .prepare(`SELECT COUNT(*) AS n FROM demandes WHERE reference LIKE ?`)
    .bind(`MC-${annee}-%`)
    .first();
  const n = ((r && r.n) || 0) + 1;
  return `MC-${annee}-${String(n).padStart(4, "0")}`;
}

/** Validation d'adresse électronique : volontairement permissive mais utile. */
export function emailValide(v) {
  return typeof v === "string" && /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v.trim());
}

/** Téléphone français, tolérant sur les espaces et les préfixes. */
export function telephoneValide(v) {
  const n = String(v || "").replace(/[\s.\-()]/g, "");
  return /^(?:\+33|0033|0)[1-9]\d{8}$/.test(n);
}

/** Coupe une chaîne et retire les caractères de contrôle. */
export function propre(v, max) {
  return String(v == null ? "" : v)
    // eslint-disable-next-line no-control-regex
    .replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, "")
    .trim()
    .slice(0, max || 500);
}

/** Réponse HTML avec les en-têtes qui vont bien. */
export function pageHtml(html, statut) {
  return new Response(html, {
    status: statut || 200,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "x-robots-tag": "noindex, nofollow",
      "referrer-policy": "no-referrer",
      "cache-control": "no-store",
    },
  });
}

/** Redirection après formulaire : 303 pour que le rechargement ne reposte pas. */
export function versPage(url) {
  return new Response(null, { status: 303, headers: { location: url } });
}

/** Comparaison à durée constante, pour les clés d'administration. */
export function memeSecret(a, b) {
  const x = new TextEncoder().encode(String(a || ""));
  const y = new TextEncoder().encode(String(b || ""));
  if (x.length !== y.length) return false;
  let d = 0;
  for (let i = 0; i < x.length; i++) d |= x[i] ^ y[i];
  return d === 0;
}
