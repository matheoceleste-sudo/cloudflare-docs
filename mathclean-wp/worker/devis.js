/* La page du devis : GET /devis/{jeton}, et son acceptation.
 *
 * Adresse secrète, jamais indexée, pas de compte à créer. Le client ouvre,
 * lit, imprime en PDF s'il veut, et accepte d'un bouton. L'acceptation vaut
 * « bon pour accord » : elle est horodatée et conservée.
 */

import { ech, eur, dateFr, dateCourte, pageHtml, versPage } from "./commun.js";
import { envoyer } from "./courriel.js";
import { accepteClient, accepteArtisan } from "./modeles.js";
import { identite } from "./reservation.js";

const VALIDITE_JOURS = 30;

function expire(creeLe) {
  return new Date(new Date(creeLe).getTime() + VALIDITE_JOURS * 864e5);
}

function styles() {
  return `
  :root{--bleu:#0e5fbb;--or:#9a7b2e;--encre:#16212e;--corps:#4a5766;--ligne:#e2e8f0;--doux:#f5f8fc}
  *,*::before,*::after{box-sizing:border-box}
  body{margin:0;background:var(--doux);color:var(--corps);
       font:400 16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
  .feuille{max-width:820px;margin:28px auto;background:#fff;border:1px solid var(--ligne);
           border-radius:10px;overflow:hidden}
  .bandeau{background:var(--encre);color:#fff;padding:26px 34px;display:flex;
           justify-content:space-between;align-items:flex-start;gap:20px;flex-wrap:wrap}
  .marque{font:700 24px/1.1 inherit;letter-spacing:-.02em}
  .marque span{color:#6ea8e8}
  .devise{font:600 11px/1.5 inherit;color:var(--or);letter-spacing:.14em;text-transform:uppercase;margin-top:5px}
  .numero{text-align:right;font-size:14px;color:#c3cfdd}
  .numero strong{display:block;color:#fff;font-size:18px;letter-spacing:.02em}
  .dedans{padding:30px 34px}
  h1{margin:0 0 6px;font:700 25px/1.25 inherit;color:var(--encre);letter-spacing:-.02em}
  .sous{margin:0 0 26px;color:#7b8794;font-size:14px}
  .parties{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-bottom:28px}
  .partie{background:var(--doux);border:1px solid var(--ligne);border-radius:6px;padding:15px 17px;font-size:14px;line-height:1.6}
  .partie h2{margin:0 0 7px;font:700 11px/1.4 inherit;color:#7b8794;letter-spacing:.12em;text-transform:uppercase}
  table{width:100%;border-collapse:collapse;margin-bottom:8px}
  th{text-align:left;font:700 11px/1.4 inherit;color:#7b8794;letter-spacing:.1em;
     text-transform:uppercase;padding:0 0 9px;border-bottom:2px solid var(--encre)}
  th.num,td.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
  td{padding:12px 0;border-bottom:1px solid var(--ligne);font-size:15px}
  tfoot td{border:0;padding-top:16px;font-weight:700;color:var(--encre);font-size:19px}
  .mention{font-size:13px;color:#7b8794;margin:0 0 26px}
  .encart{background:#fff8e6;border-left:3px solid var(--or);padding:14px 16px;
          border-radius:0 6px 6px 0;font-size:14px;margin:22px 0}
  .encart strong{color:var(--encre)}
  .actions{display:flex;gap:12px;flex-wrap:wrap;margin:26px 0 10px}
  .btn{display:inline-flex;align-items:center;justify-content:center;gap:.5em;
       border:1.5px solid var(--bleu);background:var(--bleu);color:#fff;
       font-family:inherit;font-size:15px;font-weight:600;line-height:1;padding:15px 26px;border-radius:6px;cursor:pointer;
       text-decoration:none;min-height:48px}
  .btn:hover{background:#0a4a94;border-color:#0a4a94}
  .btn-second{background:transparent;color:var(--bleu);border-color:#c3d5ea}
  .btn-second:hover{background:var(--bleu);color:#fff}
  .fait{background:#eef7ee;border-left:3px solid #2e7d32;padding:16px 18px;
        border-radius:0 6px 6px 0;margin:22px 0}
  .fait strong{color:#1b5e20}
  .legal{border-top:1px solid var(--ligne);margin-top:30px;padding-top:20px;
         font-size:12.5px;line-height:1.65;color:#7b8794}
  .legal h2{margin:0 0 8px;font:700 11px/1.4 inherit;color:#7b8794;
            letter-spacing:.12em;text-transform:uppercase}
  .legal p{margin:0 0 10px}
  .perime{background:#fdeaea;border-left:3px solid #c62828;padding:14px 16px;
          border-radius:0 6px 6px 0;margin:22px 0;font-size:14px}
  @media(max-width:620px){
    .parties{grid-template-columns:1fr}
    .dedans,.bandeau{padding-left:20px;padding-right:20px}
    .numero{text-align:left}
  }
  @media print{
    body{background:#fff}
    .feuille{margin:0;border:0;border-radius:0;max-width:none}
    .actions,.noimp{display:none!important}
    .bandeau{background:#fff;color:var(--encre);border-bottom:3px solid var(--encre)}
    .marque span{color:var(--bleu)}
    .numero,.numero strong{color:var(--encre)}
  }`;
}

/** Rendu de la page. `etat` porte un message ponctuel (accepté, question posée). */
function rendu(site, d, lignes, etat) {
  const perime = new Date() > expire(d.cree_le) && d.statut !== "accepte";
  const chiffre = d.total_eur != null;
  const accepte = d.statut === "accepte";

  const corpsTable = chiffre
    ? `<table>
      <thead><tr><th>Désignation</th><th class="num">Qté</th><th class="num">P.U.</th><th class="num">Total</th></tr></thead>
      <tbody>${lignes
        .map(
          (l) => `<tr>
          <td>${ech(l.libelle)}</td>
          <td class="num">${l.qte}</td>
          <td class="num">${ech(eur(l.pu))}</td>
          <td class="num">${ech(eur(l.total))}</td>
        </tr>`
        )
        .join("")}</tbody>
      <tfoot><tr><td colspan="3">Total à régler</td><td class="num">${ech(eur(d.total_eur))}</td></tr></tfoot>
    </table>
    <p class="mention">Montants nets en euros. TVA non applicable, article 293 B du Code général des impôts.</p>`
    : `<div class="encart">
        <strong>Chiffrage en cours.</strong> Cette prestation se chiffre après
        échange ou visite : le prix dépend de ce qu'il y a réellement sur place.
        Mathéo Céleste vous rappelle sous 24 h, et le montant apparaîtra ici
        même — vous recevrez un message dès qu'il sera posé.
      </div>`;

  const bloc = accepte
    ? `<div class="fait">
        <strong>Devis accepté le ${ech(dateFr(d.accepte_le))}.</strong>
        <p style="margin:6px 0 0">Vous allez être appelé pour caler le créneau
        définitif. Aucun acompte : le règlement se fait après l'intervention,
        une fois le résultat constaté ensemble.</p>
      </div>`
    : perime
      ? `<div class="perime">Ce devis a dépassé sa durée de validité de ${VALIDITE_JOURS} jours.
         Il reste consultable, mais les montants sont à confirmer. Un appel au
         ${ech(site.tel)} suffit à le remettre à jour.</div>`
      : chiffre
        ? `<div class="actions">
            <form method="POST" action="/devis/${ech(d.jeton)}/accepter" style="margin:0">
              <button class="btn" type="submit">Accepter ce devis</button>
            </form>
            <a class="btn btn-second" href="mailto:${ech(site.contact)}?subject=${encodeURIComponent(
              "Question sur le devis " + d.reference
            )}">Poser une question</a>
          </div>
          <p class="mention noimp">Accepter vaut « bon pour accord » : la date et
          l'heure sont enregistrées. Vous ne versez aucun acompte, et vous
          pouvez encore tout annuler par un simple appel.</p>`
        : `<div class="actions">
            <a class="btn" href="tel:${ech(site.tel_lien)}">Appeler le ${ech(site.tel)}</a>
          </div>`;

  const messageEtat =
    etat === "accepte"
      ? ""
      : etat === "deja"
        ? `<div class="fait"><strong>C'était déjà fait.</strong> Votre acceptation avait bien été enregistrée.</div>`
        : "";

  return `<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Devis ${ech(d.reference)} — MathClean</title>
<style>${styles()}</style>
</head><body>
<main class="feuille">
  <header class="bandeau">
    <div>
      <div class="marque">Math<span>Clean</span></div>
      <div class="devise">Une exigence de roi</div>
    </div>
    <div class="numero">
      <strong>${chiffre ? "DEVIS" : "DEMANDE"} ${ech(d.reference)}</strong>
      Établi le ${ech(dateCourte(d.cree_le))}<br>
      ${chiffre ? `Valable jusqu'au ${ech(dateCourte(expire(d.cree_le).toISOString()))}` : "Chiffrage sous 24 h"}
    </div>
  </header>
  <div class="dedans">
    <h1>${ech(d.prestation_nom)}</h1>
    <p class="sous">${
      d.date_souhaitee
        ? `Date souhaitée : ${ech(dateFr(d.date_souhaitee))}${d.creneau ? ` · ${ech(d.creneau)}` : ""}`
        : "Date à convenir ensemble"
    }</p>

    ${messageEtat}

    <div class="parties">
      <div class="partie">
        <h2>Prestataire</h2>
        <strong>${ech(site.nom)}</strong> — Mathéo Céleste<br>
        ${ech(site.adresse)}, ${ech(site.cp)} ${ech(site.ville)}<br>
        SIRET ${ech(site.siret)}<br>
        ${ech(site.tel)}
      </div>
      <div class="partie">
        <h2>Client</h2>
        <strong>${ech(d.nom)}</strong><br>
        ${d.adresse ? `${ech(d.adresse)}<br>` : ""}
        ${ech(d.code_postal || "")} ${ech(d.ville || "")}<br>
        ${ech(d.telephone)}
      </div>
    </div>

    ${corpsTable}
    ${d.message ? `<p class="mention"><strong>Votre message :</strong> ${ech(d.message)}</p>` : ""}
    ${bloc}

    <div class="legal">
      <h2>Conditions</h2>
      <p><strong>Validité.</strong> Ce devis est gratuit et engage ${ech(site.nom)}
      pendant ${VALIDITE_JOURS} jours à compter de son établissement. Les montants
      sont fermes pour le périmètre décrit ci-dessus ; une prestation différente
      de ce qui a été déclaré fait l'objet d'un nouveau devis, présenté et
      accepté avant toute exécution.</p>
      <p><strong>Règlement.</strong> Aucun acompte n'est demandé. Le règlement
      intervient après l'intervention, une fois le résultat constaté ensemble —
      espèces, carte bancaire ou virement.</p>
      <p><strong>TVA.</strong> TVA non applicable, article 293 B du Code général
      des impôts (franchise en base).</p>
      <p><strong>Rétractation.</strong> Conformément aux articles L221-18 et
      suivants du Code de la consommation, le consommateur qui contracte à
      distance dispose de quatorze jours pour se rétracter, sans motif. Lorsque
      l'intervention est demandée avant la fin de ce délai, le client peut y
      renoncer expressément et reste alors redevable du service déjà fourni.</p>
      <p class="noimp" style="margin-top:14px;">
        <a href="${ech(site.url)}/mentions-legales" style="color:var(--bleu)">Mentions légales et conditions</a> ·
        <a href="${ech(site.url)}/politique-confidentialite" style="color:var(--bleu)">Confidentialité</a> ·
        <a href="#" onclick="window.print();return false" style="color:var(--bleu)">Imprimer ou enregistrer en PDF</a>
      </p>
    </div>
  </div>
</main>
</body></html>`;
}

async function charger(env, jetonUrl) {
  return env.DB.prepare(`SELECT * FROM demandes WHERE jeton = ?`).bind(jetonUrl).first();
}

export async function pageDevis(env, jetonUrl) {
  const d = await charger(env, jetonUrl);
  if (!d) return pageHtml(introuvable(), 404);

  // Premier affichage : on note que le client a ouvert. Cela arrête les
  // relances « sans réponse » sur quelqu'un qui a bien reçu le devis.
  if (!d.vu_le) {
    await env.DB.prepare(
      `UPDATE demandes SET vu_le = ?, statut = CASE WHEN statut = 'devis_envoye' THEN 'vu' ELSE statut END WHERE id = ?`
    ).bind(new Date().toISOString(), d.id).run();
  }

  const site = identite(env);
  let lignes = [];
  try {
    lignes = JSON.parse(d.lignes || "[]");
  } catch {
    lignes = [];
  }
  return pageHtml(rendu(site, d, lignes, null));
}

export async function accepterDevis(request, env, ctx, jetonUrl) {
  const d = await charger(env, jetonUrl);
  if (!d) return pageHtml(introuvable(), 404);

  const site = identite(env);
  if (d.statut === "accepte") return versPage(`/devis/${jetonUrl}?etat=deja`);
  if (d.total_eur == null) return versPage(`/devis/${jetonUrl}`);

  const maintenant = new Date().toISOString();
  await env.DB.prepare(
    `UPDATE demandes SET statut = 'accepte', accepte_le = ? WHERE id = ? AND statut != 'accepte'`
  ).bind(maintenant, d.id).run();

  let lignes = [];
  try {
    lignes = JSON.parse(d.lignes || "[]");
  } catch {
    lignes = [];
  }
  const accepte = { ...d, statut: "accepte", accepte_le: maintenant };

  ctx.waitUntil(
    (async () => {
      await envoyer(env, d.id, "accepte_client", {
        a: d.email,
        ...accepteClient(site, accepte, lignes),
      });
      await envoyer(env, d.id, "accepte_notif", {
        a: site.contact,
        ...accepteArtisan(site, accepte, `${site.url}/admin?demande=${d.id}`),
      });
    })()
  );

  return versPage(`/devis/${jetonUrl}?etat=accepte`);
}

function introuvable() {
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Devis introuvable — MathClean</title>
<style>${styles()}</style></head><body>
<main class="feuille"><div class="dedans">
  <h1>Ce devis n'existe pas</h1>
  <p>Le lien est peut-être incomplet, ou le devis a été supprimé.
  Un appel au <a href="tel:+33623075259">06 23 07 52 59</a> règle la question
  plus vite qu'un message.</p>
  <p><a class="btn" href="https://mathclean.fr/">Retour au site</a></p>
</div></main></body></html>`;
}
