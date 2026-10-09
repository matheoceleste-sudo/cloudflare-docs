/* La console : /admin
 *
 * Pensée pour un téléphone, parce que c'est là qu'elle sera ouverte — entre
 * deux interventions, pas devant un bureau. Une clé, un cookie, pas de compte.
 *
 * Ce qu'elle permet : voir les demandes, chiffrer un sur-devis et l'envoyer
 * d'un bouton, poser la date d'intervention (dont dépendent le rappel de la
 * veille et la demande d'avis), et relancer un envoi qui a échoué.
 */

import {
  ech, eur, dateFr, dateCourte, pageHtml, versPage, memeSecret, propre,
} from "./commun.js";
import { envoyer, reprendre } from "./courriel.js";
import { devisFerme } from "./modeles.js";
import { identite } from "./reservation.js";
import { passeQuotidienne } from "./relances.js";

const COOKIE = "mc_admin";

function autorise(request, env) {
  const clef = env.ADMIN_CLE;
  if (!clef) return false;
  const brut = request.headers.get("cookie") || "";
  const m = brut.match(new RegExp(`(?:^|;\\s*)${COOKIE}=([^;]+)`));
  return !!m && memeSecret(decodeURIComponent(m[1]), clef);
}

const ETATS = {
  nouveau: ["À chiffrer", "#b26a00", "#fff4e0"],
  devis_envoye: ["Devis envoyé", "#0e5fbb", "#e8f1fb"],
  vu: ["Devis consulté", "#0e5fbb", "#e8f1fb"],
  accepte: ["Accepté", "#1b5e20", "#eaf5ea"],
  planifie: ["Planifié", "#1b5e20", "#eaf5ea"],
  realise: ["Réalisé", "#555", "#eee"],
  refuse: ["Refusé", "#8a1c1c", "#fdeaea"],
  clos: ["Classé", "#777", "#f0f0f0"],
};

function pastille(statut) {
  const [txt, fg, bg] = ETATS[statut] || [statut, "#555", "#eee"];
  return `<span style="display:inline-block;padding:3px 9px;border-radius:3px;
    background:${bg};color:${fg};font:600 11px/1.5 inherit;letter-spacing:.04em;
    text-transform:uppercase;white-space:nowrap">${ech(txt)}</span>`;
}

function styles() {
  return `
  *,*::before,*::after{box-sizing:border-box}
  body{margin:0;background:#f1f5f9;color:#334155;
       font:400 15px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
  .haut{background:#16212e;color:#fff;padding:16px 20px;display:flex;
        justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}
  .haut b{font-size:17px;letter-spacing:-.01em}
  .haut a{color:#8fc0f5;text-decoration:none;font-size:14px}
  main{max-width:960px;margin:20px auto;padding:0 14px}
  .carte{background:#fff;border:1px solid #e2e8f0;border-radius:8px;
         padding:16px 18px;margin-bottom:14px}
  .carte h2{margin:0 0 4px;font:700 17px/1.3 inherit;color:#16212e}
  .meta{font-size:13px;color:#64748b;margin:0 0 10px}
  .rang{display:flex;justify-content:space-between;gap:12px;align-items:flex-start;flex-wrap:wrap}
  .somme{font:700 20px/1 inherit;color:#16212e;white-space:nowrap;font-variant-numeric:tabular-nums}
  table{width:100%;border-collapse:collapse;font-size:14px;margin:10px 0}
  td{padding:6px 0;border-bottom:1px solid #f1f5f9}
  td:last-child{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
  a.lien{color:#0e5fbb}
  form{margin:0}
  label{display:block;font:600 12px/1.6 inherit;color:#64748b;
        letter-spacing:.06em;text-transform:uppercase;margin:10px 0 4px}
  input,textarea,select{width:100%;padding:11px 12px;border:1px solid #cbd5e1;
        border-radius:5px;font:inherit;font-size:15px;background:#fff;min-height:44px}
  textarea{min-height:92px;resize:vertical;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px}
  .btn{display:inline-flex;align-items:center;justify-content:center;
       background:#0e5fbb;color:#fff;border:1.5px solid #0e5fbb;border-radius:5px;
       padding:12px 20px;font-family:inherit;font-size:15px;font-weight:600;line-height:1;cursor:pointer;text-decoration:none;
       min-height:46px;margin-top:12px}
  .btn-léger{background:#fff;color:#0e5fbb;border-color:#c3d5ea}
  .btn-rouge{background:#fff;color:#8a1c1c;border-color:#e3b5b5}
  .grille{display:grid;grid-template-columns:1fr 1fr;gap:12px}
  .avis{padding:12px 14px;border-radius:5px;margin-bottom:14px;font-size:14px}
  .avis-ok{background:#eaf5ea;border-left:3px solid #1b5e20;color:#1b5e20}
  .avis-ko{background:#fdeaea;border-left:3px solid #8a1c1c;color:#8a1c1c}
  .filtres{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:14px}
  .filtres a{padding:7px 13px;border-radius:999px;background:#fff;
             border:1px solid #e2e8f0;text-decoration:none;color:#475569;font-size:14px}
  .filtres a.actif{background:#16212e;color:#fff;border-color:#16212e}
  .vide{text-align:center;color:#94a3b8;padding:40px 0}
  @media(max-width:560px){.grille{grid-template-columns:1fr}}`;
}

function page(titre, corps) {
  return pageHtml(`<!doctype html><html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>${ech(titre)} — console MathClean</title><style>${styles()}</style></head>
<body><div class="haut"><b>MathClean · console</b>
<a href="/admin">Toutes les demandes</a></div><main>${corps}</main></body></html>`);
}

/* ------------------------------------------------------------- connexion */

function formulaireConnexion(erreur) {
  return pageHtml(`<!doctype html><html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Console MathClean</title>
<style>${styles()}</style></head><body>
<main style="max-width:380px;margin:12vh auto">
  <div class="carte">
    <h2>Console MathClean</h2>
    ${erreur ? `<div class="avis avis-ko">Clé incorrecte.</div>` : ""}
    <form method="POST" action="/admin/connexion">
      <label for="c">Clé d'accès</label>
      <input id="c" name="cle" type="password" autocomplete="current-password" required autofocus>
      <button class="btn" type="submit" style="width:100%">Entrer</button>
    </form>
  </div>
</main></body></html>`);
}

async function connexion(request, env) {
  const f = await request.formData();
  if (!env.ADMIN_CLE || !memeSecret(propre(f.get("cle"), 200), env.ADMIN_CLE)) {
    return formulaireConnexion(true);
  }
  return new Response(null, {
    status: 303,
    headers: {
      location: "/admin",
      "set-cookie": `${COOKIE}=${encodeURIComponent(env.ADMIN_CLE)}; Path=/admin; HttpOnly; Secure; SameSite=Lax; Max-Age=2592000`,
    },
  });
}

/* ------------------------------------------------------------- la liste */

async function liste(env, url) {
  const filtre = url.searchParams.get("f") || "actives";
  const clauses = {
    actives: `statut IN ('nouveau','devis_envoye','vu','accepte','planifie')`,
    chiffrer: `statut = 'nouveau'`,
    acceptes: `statut IN ('accepte','planifie')`,
    toutes: `1=1`,
  };
  const where = clauses[filtre] || clauses.actives;
  const r = await env.DB.prepare(
    `SELECT * FROM demandes WHERE ${where} ORDER BY cree_le DESC LIMIT 100`
  ).all();

  const onglet = (cle, txt) =>
    `<a href="/admin?f=${cle}" class="${filtre === cle ? "actif" : ""}">${txt}</a>`;

  const cartes = (r.results || [])
    .map(
      (d) => `<a class="carte" href="/admin?demande=${d.id}" style="display:block;text-decoration:none;color:inherit">
      <div class="rang">
        <div>
          <h2>${ech(d.nom)} — ${ech(d.prestation_nom)}</h2>
          <p class="meta">${ech(d.reference)} · ${ech(dateCourte(d.cree_le))} ·
          ${ech(d.ville || "")} ${ech(d.code_postal || "")}
          ${d.relances ? ` · ${d.relances} relance${d.relances > 1 ? "s" : ""}` : ""}</p>
          ${pastille(d.statut)}
        </div>
        <div class="somme">${d.total_eur != null ? ech(eur(d.total_eur)) : "—"}</div>
      </div>
    </a>`
    )
    .join("");

  // Sans fournisseur d'envoi, le système enregistre tout et n'envoie rien :
  // les clients ne reçoivent aucun devis. C'est le seul état vraiment
  // dangereux du dispositif, donc il s'affiche en haut et en rouge.
  const sansEnvoi = !env.RESEND_API_KEY && !env.BREVO_API_KEY;
  const alerte = sansEnvoi
    ? `<div class="avis avis-ko"><strong>Aucune clé d'envoi configurée.</strong>
       Les demandes sont bien enregistrées, mais aucun devis ne part. Posez
       RESEND_API_KEY ou BREVO_API_KEY dans les secrets du Worker : tout ce
       qui a échoué repartira à la passe suivante.</div>`
    : "";

  return page(
    "Demandes",
    `${alerte}
    <div class="filtres">
      ${onglet("actives", "En cours")}
      ${onglet("chiffrer", "À chiffrer")}
      ${onglet("acceptes", "Acceptées")}
      ${onglet("toutes", "Tout")}
    </div>
    ${cartes || `<div class="carte vide">Aucune demande dans cette vue.</div>`}
    <div class="carte">
      <h2>Passe de relances</h2>
      <p class="meta">Elle tourne chaque nuit. Ce bouton la déclenche
      maintenant : relances dues, rappels de la veille, demandes d'avis, et
      reprise des envois qui avaient échoué. La lancer deux fois n'envoie
      rien de plus.</p>
      <form method="POST" action="/admin/relances">
        <button class="btn btn-léger" type="submit">Lancer la passe maintenant</button>
      </form>
    </div>`
  );
}

/* ------------------------------------------------------------ une demande */

async function detail(env, id, message) {
  const d = await env.DB.prepare(`SELECT * FROM demandes WHERE id = ?`).bind(id).first();
  if (!d) return page("Introuvable", `<div class="carte vide">Demande introuvable.</div>`);

  const site = identite(env);
  let lignes = [];
  try {
    lignes = JSON.parse(d.lignes || "[]");
  } catch {
    lignes = [];
  }

  const envois = await env.DB.prepare(
    `SELECT type, envoye_le, statut, detail FROM courriels WHERE demande_id = ? ORDER BY id`
  ).bind(id).all();

  const journalEnvois = (envois.results || [])
    .map(
      (c) => `<tr><td>${ech(c.type)}</td>
        <td style="text-align:left;color:${c.statut === "ok" ? "#1b5e20" : "#8a1c1c"}">
        ${ech(c.statut)}${c.statut === "erreur" ? ` — ${ech(String(c.detail || "").slice(0, 120))}` : ""}</td>
        <td>${ech(dateCourte(c.envoye_le))}</td></tr>`
    )
    .join("");

  const enEchec = (envois.results || []).filter((c) => c.statut === "erreur");

  const tableLignes = lignes.length
    ? `<table>${lignes
        .map(
          (l) =>
            `<tr><td>${ech(l.libelle)}${l.qte > 1 ? ` × ${l.qte}` : ""}</td><td>${ech(eur(l.total))}</td></tr>`
        )
        .join("")}</table>`
    : "";

  const blocChiffrage =
    d.total_eur == null
      ? `<div class="carte">
          <h2>Chiffrer et envoyer le devis</h2>
          <p class="meta">Une ligne par poste, au format <code>libellé | montant</code>.
          Le déplacement est ajouté automatiquement s'il manque.</p>
          <form method="POST" action="/admin/chiffrer">
            <input type="hidden" name="id" value="${d.id}">
            <label for="l">Postes du devis</label>
            <textarea id="l" name="lignes" required placeholder="Dégraissage hotte et filtres | 380
Conduit d'extraction jusqu'au ventilateur | 240
Déplacement | 15"></textarea>
            <button class="btn" type="submit">Enregistrer et envoyer le devis au client</button>
          </form>
        </div>`
      : "";

  const blocDate = `<div class="carte">
      <h2>Date d'intervention</h2>
      <p class="meta">Elle commande le rappel de la veille et la demande d'avis
      trois jours après. Sans elle, ni l'un ni l'autre ne partent.</p>
      <form method="POST" action="/admin/date">
        <input type="hidden" name="id" value="${d.id}">
        <div class="grille">
          <div>
            <label for="di">Date</label>
            <input id="di" name="date" type="date" value="${ech(d.date_intervention || "")}">
          </div>
          <div>
            <label for="st">Statut</label>
            <select id="st" name="statut">
              ${Object.keys(ETATS)
                .map(
                  (k) =>
                    `<option value="${k}"${k === d.statut ? " selected" : ""}>${ech(ETATS[k][0])}</option>`
                )
                .join("")}
            </select>
          </div>
        </div>
        <button class="btn" type="submit">Enregistrer</button>
      </form>
    </div>`;

  const blocReprise = enEchec.length
    ? `<div class="carte">
        <h2>Envois en échec</h2>
        <p class="meta">${enEchec.length} courriel(s) ne sont pas partis.
        La cause est indiquée dans le journal ci-dessous.</p>
        <form method="POST" action="/admin/reprendre">
          <input type="hidden" name="id" value="${d.id}">
          <button class="btn btn-léger" type="submit">Réessayer ces envois</button>
        </form>
      </div>`
    : "";

  return page(
    d.reference,
    `${message ? `<div class="avis avis-ok">${ech(message)}</div>` : ""}
    <div class="carte">
      <div class="rang">
        <div>
          <h2>${ech(d.nom)}</h2>
          <p class="meta">${ech(d.reference)} · créée le ${ech(dateFr(d.cree_le))}</p>
          ${pastille(d.statut)}
        </div>
        <div class="somme">${d.total_eur != null ? ech(eur(d.total_eur)) : "à chiffrer"}</div>
      </div>
      <table>
        <tr><td>Prestation</td><td style="text-align:left">${ech(d.prestation_nom)}</td></tr>
        <tr><td>Téléphone</td><td style="text-align:left"><a class="lien" href="tel:${ech(d.telephone)}">${ech(d.telephone)}</a></td></tr>
        <tr><td>Courriel</td><td style="text-align:left"><a class="lien" href="mailto:${ech(d.email)}">${ech(d.email)}</a></td></tr>
        <tr><td>Adresse</td><td style="text-align:left">${ech(d.adresse || "—")}, ${ech(d.code_postal || "")} ${ech(d.ville || "")}</td></tr>
        <tr><td>Accès</td><td style="text-align:left">${ech(d.acces || "—")}</td></tr>
        <tr><td>Souhait</td><td style="text-align:left">${ech(d.date_souhaitee ? dateFr(d.date_souhaitee) : "—")} ${ech(d.creneau || "")}</td></tr>
        <tr><td>Client</td><td style="text-align:left">${ech(d.type_client || "—")}</td></tr>
        ${d.vu_le ? `<tr><td>Devis ouvert</td><td style="text-align:left">${ech(dateFr(d.vu_le))}</td></tr>` : ""}
        ${d.accepte_le ? `<tr><td>Accepté</td><td style="text-align:left">${ech(dateFr(d.accepte_le))}</td></tr>` : ""}
      </table>
      ${d.message ? `<p style="padding:11px 13px;background:#f8fafc;border-left:3px solid #0e5fbb;white-space:pre-wrap;font-size:14px">${ech(d.message)}</p>` : ""}
      ${tableLignes}
      <p style="margin-top:12px"><a class="lien" href="${ech(site.url)}/devis/${ech(d.jeton)}">Voir le devis tel que le client le voit →</a></p>
    </div>
    ${blocChiffrage}
    ${blocDate}
    ${blocReprise}
    <div class="carte">
      <h2>Courriels</h2>
      ${journalEnvois ? `<table>${journalEnvois}</table>` : `<p class="meta">Aucun envoi pour l'instant.</p>`}
    </div>`
  );
}

/* --------------------------------------------------------------- actions */

async function chiffrer(request, env, ctx) {
  const f = await request.formData();
  const id = parseInt(f.get("id"), 10);
  const brut = propre(f.get("lignes"), 4000);

  const lignes = [];
  let total = 0;
  for (const ligne of brut.split("\n")) {
    const t = ligne.trim();
    if (!t) continue;
    const sep = t.lastIndexOf("|");
    if (sep < 0) continue;
    const libelle = t.slice(0, sep).trim();
    const montant = Math.round(parseFloat(t.slice(sep + 1).replace(",", ".").replace(/[^\d.-]/g, "")));
    if (!libelle || !Number.isFinite(montant)) continue;
    lignes.push({ libelle, qte: 1, pu: montant, total: montant });
    total += montant;
  }
  if (!lignes.length) return versPage(`/admin?demande=${id}&m=${encodeURIComponent("Aucune ligne lisible.")}`);

  await env.DB.prepare(
    `UPDATE demandes SET lignes = ?, total_eur = ?, regime = 'ferme',
            statut = 'devis_envoye' WHERE id = ?`
  ).bind(JSON.stringify(lignes), total, id).run();

  const d = await env.DB.prepare(`SELECT * FROM demandes WHERE id = ?`).bind(id).first();
  const site = identite(env);
  ctx.waitUntil(
    (async () => {
      // Un sur-devis chiffré après coup n'a jamais reçu le courriel « devis ».
      await reprendre(env, id, "devis");
      await envoyer(env, id, "devis", {
        a: d.email,
        ...devisFerme(site, d, lignes, `${site.url}/devis/${d.jeton}`),
      });
    })()
  );
  return versPage(`/admin?demande=${id}&m=${encodeURIComponent("Devis chiffré et envoyé au client.")}`);
}

async function poserDate(request, env) {
  const f = await request.formData();
  const id = parseInt(f.get("id"), 10);
  const date = propre(f.get("date"), 20) || null;
  const statut = propre(f.get("statut"), 20);
  const valide = Object.prototype.hasOwnProperty.call(ETATS, statut) ? statut : null;
  await env.DB.prepare(
    `UPDATE demandes SET date_intervention = ?, statut = COALESCE(?, statut) WHERE id = ?`
  ).bind(date, valide, id).run();
  return versPage(`/admin?demande=${id}&m=${encodeURIComponent("Enregistré.")}`);
}

async function reprendreEnvois(request, env) {
  const f = await request.formData();
  const id = parseInt(f.get("id"), 10);
  await reprendre(env, id, null);
  return versPage(
    `/admin?demande=${id}&m=${encodeURIComponent("Envois remis en file : ils repartiront à la prochaine action ou à la passe de nuit.")}`
  );
}

/* --------------------------------------------------------------- routeur */

export async function routeAdmin(request, env, ctx, url) {
  const chemin = url.pathname;

  if (chemin === "/admin/connexion" && request.method === "POST") {
    return connexion(request, env);
  }
  if (!autorise(request, env)) return formulaireConnexion(false);

  if (request.method === "POST") {
    if (chemin === "/admin/chiffrer") return chiffrer(request, env, ctx);
    if (chemin === "/admin/date") return poserDate(request, env);
    if (chemin === "/admin/reprendre") return reprendreEnvois(request, env);
    if (chemin === "/admin/relances") {
      const j = await passeQuotidienne(env);
      return versPage(`/admin?m=${encodeURIComponent(`Passe exécutée : ${JSON.stringify(j)}`)}`);
    }
  }

  const demande = url.searchParams.get("demande");
  if (demande) return detail(env, parseInt(demande, 10), url.searchParams.get("m"));
  return liste(env, url);
}
