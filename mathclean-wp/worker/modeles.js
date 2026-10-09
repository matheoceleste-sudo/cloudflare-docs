/* Gabarits de courriels.
 *
 * Même ton que le site : on dit ce qui va se passer, on ne promet rien qu'on
 * ne tienne, et on ne fabrique pas d'urgence. Chaque message existe en HTML
 * et en texte brut — les deux sont lus, et un message sans version texte
 * part plus souvent en indésirable.
 */

import { ech, eur, dateFr, dateCourte } from "./commun.js";

const BLEU = "#0e5fbb";
const OR = "#9a7b2e";
const ENCRE = "#16212e";
const CORPS = "#4a5766";

/** Enveloppe commune. Styles en ligne : les clients de messagerie ignorent le reste. */
function enveloppe(site, titre, corps, pied) {
  return `<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${ech(titre)}</title></head>
<body style="margin:0;padding:0;background:#f5f8fc;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f5f8fc;padding:24px 12px;">
<tr><td align="center">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;background:#fff;border:1px solid #e2e8f0;border-radius:10px;overflow:hidden;">
  <tr><td style="background:${ENCRE};padding:22px 28px;">
    <div style="font:700 20px/1.2 system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;color:#fff;letter-spacing:-.02em;">
      Math<span style="color:#6ea8e8;">Clean</span>
    </div>
    <div style="font:600 11px/1.4 system-ui,sans-serif;color:${OR};letter-spacing:.14em;text-transform:uppercase;margin-top:4px;">
      Une exigence de roi
    </div>
  </td></tr>
  <tr><td style="padding:28px;font:400 15px/1.65 system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;color:${CORPS};">
    ${corps}
  </td></tr>
  <tr><td style="padding:18px 28px;background:#f8fafc;border-top:1px solid #e2e8f0;font:400 12px/1.6 system-ui,sans-serif;color:#7b8794;">
    ${pied || ""}
    <div style="margin-top:10px;">
      ${ech(site.nom)} · ${ech(site.adresse)}, ${ech(site.cp)} ${ech(site.ville)}<br>
      SIRET ${ech(site.siret)} · TVA non applicable, article 293 B du CGI<br>
      <a href="tel:${ech(site.tel_lien)}" style="color:${BLEU};text-decoration:none;">${ech(site.tel)}</a>
      · <a href="${ech(site.url)}" style="color:${BLEU};text-decoration:none;">mathclean.fr</a>
    </div>
  </td></tr>
</table>
</td></tr></table>
</body></html>`;
}

function bouton(url, libelle, couleur) {
  return `<table role="presentation" cellpadding="0" cellspacing="0" style="margin:22px 0;">
    <tr><td style="background:${couleur || BLEU};border-radius:6px;">
      <a href="${ech(url)}" style="display:inline-block;padding:14px 26px;font:600 15px/1 system-ui,sans-serif;color:#fff;text-decoration:none;">${ech(libelle)}</a>
    </td></tr></table>`;
}

function titre(t) {
  return `<h1 style="margin:0 0 16px;font:700 21px/1.3 system-ui,sans-serif;color:${ENCRE};letter-spacing:-.02em;">${ech(t)}</h1>`;
}

/** Tableau des lignes du devis. */
function tableauLignes(lignes, total) {
  const l = lignes
    .map(
      (x) => `<tr>
      <td style="padding:9px 0;border-bottom:1px solid #eef2f7;">${ech(x.libelle)}${
        x.qte > 1 ? ` <span style="color:#7b8794;">× ${x.qte}</span>` : ""
      }</td>
      <td style="padding:9px 0;border-bottom:1px solid #eef2f7;text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums;">${ech(eur(x.total))}</td>
    </tr>`
    )
    .join("");
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:18px 0;font-size:14px;">
    ${l}
    <tr>
      <td style="padding:13px 0 0;font-weight:700;color:${ENCRE};">Total</td>
      <td style="padding:13px 0 0;text-align:right;font-weight:700;font-size:19px;color:${ENCRE};white-space:nowrap;">${ech(eur(total))}</td>
    </tr>
  </table>
  <p style="margin:0;font-size:12px;color:#7b8794;">Montants nets. TVA non applicable, article 293 B du CGI.</p>`;
}

function lignesTexte(lignes, total) {
  return (
    lignes
      .map((x) => `  - ${x.libelle}${x.qte > 1 ? ` x ${x.qte}` : ""} : ${eur(x.total)}`)
      .join("\n") + `\n  TOTAL : ${eur(total)} (TVA non applicable, art. 293 B du CGI)`
  );
}

/* ------------------------------------------------------------------ devis */

export function devisFerme(site, d, lignes, urlDevis) {
  const quand =
    d.date_souhaitee
      ? `Vous avez demandé le ${dateFr(d.date_souhaitee)}${d.creneau ? `, ${d.creneau.toLowerCase()}` : ""}.`
      : "";
  const corps = `
    ${titre("Votre devis est prêt")}
    <p>Bonjour ${ech(d.nom)},</p>
    <p>Voici le devis pour la prestation que vous venez de réserver, établi
    d'après ce que vous avez indiqué. Il est <strong>ferme</strong> : c'est ce
    montant que vous réglerez, sans acompte, une fois le travail constaté
    avec vous.</p>
    ${tableauLignes(lignes, d.total_eur)}
    ${quand ? `<p>${ech(quand)}</p>` : ""}
    ${bouton(urlDevis, "Voir et accepter le devis")}
    <p>Le devis reste valable <strong>30 jours</strong>. Si quelque chose ne
    correspond pas à votre besoin, répondez simplement à ce message : on
    ajuste avant de venir, pas après.</p>
    <p style="margin-top:22px;">Mathéo Céleste<br>
    <span style="color:#7b8794;">MathClean</span></p>`;
  const pied = `Devis n° ${ech(d.reference)} du ${ech(dateCourte(d.cree_le))}.`;
  const texte = `Bonjour ${d.nom},

Voici le devis pour la prestation que vous venez de reserver, etabli d'apres
ce que vous avez indique. Il est ferme : c'est ce montant que vous reglerez,
sans acompte, une fois le travail constate avec vous.

${lignesTexte(lignes, d.total_eur)}

${quand}

Voir et accepter le devis : ${urlDevis}

Le devis reste valable 30 jours. Si quelque chose ne correspond pas a votre
besoin, repondez simplement a ce message : on ajuste avant de venir.

Matheo Celeste - MathClean
Devis n° ${d.reference} du ${dateCourte(d.cree_le)}
${site.tel} - ${site.url}`;

  return {
    sujet: `Votre devis MathClean — ${eur(d.total_eur)} (${d.reference})`,
    html: enveloppe(site, "Votre devis MathClean", corps, pied),
    texte,
  };
}

/* ------------------------------------------- accusé pour les « sur devis » */

export function accuseSurDevis(site, d, urlDevis) {
  const corps = `
    ${titre("Votre demande est bien arrivée")}
    <p>Bonjour ${ech(d.nom)},</p>
    <p>Votre demande pour <strong>${ech(d.prestation_nom)}</strong> est
    enregistrée sous la référence ${ech(d.reference)}.</p>
    <p>Cette prestation ne se chiffre pas à l'aveugle : le prix dépend de ce
    qu'il y a réellement sur place. Je vous rappelle sous 24 h pour en parler,
    et vous recevez ensuite un devis ferme et détaillé, poste par poste.
    Tant que vous ne l'avez pas accepté, vous n'êtes engagé à rien.</p>
    ${bouton(urlDevis, "Suivre ma demande")}
    <p>Si vous voulez accélérer, appelez directement le
    <a href="tel:${ech(site.tel_lien)}" style="color:${BLEU};">${ech(site.tel)}</a>
    — c'est moi qui réponds.</p>
    <p style="margin-top:22px;">Mathéo Céleste<br>
    <span style="color:#7b8794;">MathClean</span></p>`;
  const texte = `Bonjour ${d.nom},

Votre demande pour ${d.prestation_nom} est enregistree sous la reference ${d.reference}.

Cette prestation ne se chiffre pas a l'aveugle : le prix depend de ce qu'il y
a reellement sur place. Je vous rappelle sous 24 h pour en parler, et vous
recevez ensuite un devis ferme et detaille, poste par poste. Tant que vous ne
l'avez pas accepte, vous n'etes engage a rien.

Suivre ma demande : ${urlDevis}

Pour accelerer, appelez le ${site.tel} - c'est moi qui reponds.

Matheo Celeste - MathClean`;

  return {
    sujet: `Demande reçue — ${d.prestation_nom} (${d.reference})`,
    html: enveloppe(site, "Votre demande est bien arrivée", corps, ""),
    texte,
  };
}

/* ------------------------------------------------ notification à l'artisan */

export function notifArtisan(site, d, lignes, urlAdmin) {
  const chiffre =
    d.total_eur != null
      ? tableauLignes(lignes, d.total_eur)
      : `<p style="padding:12px 14px;background:#fff8e6;border-left:3px solid ${OR};"><strong>À chiffrer.</strong> Prestation sur devis : le client a reçu un accusé de réception, pas un prix.</p>`;
  const corps = `
    ${titre(d.total_eur != null ? "Nouvelle réservation chiffrée" : "Nouvelle demande à chiffrer")}
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="font-size:14px;">
      <tr><td style="padding:4px 0;color:#7b8794;width:130px;">Référence</td><td style="padding:4px 0;"><strong>${ech(d.reference)}</strong></td></tr>
      <tr><td style="padding:4px 0;color:#7b8794;">Prestation</td><td style="padding:4px 0;">${ech(d.prestation_nom)}</td></tr>
      <tr><td style="padding:4px 0;color:#7b8794;">Client</td><td style="padding:4px 0;">${ech(d.nom)} (${ech(d.type_client || "—")})</td></tr>
      <tr><td style="padding:4px 0;color:#7b8794;">Téléphone</td><td style="padding:4px 0;"><a href="tel:${ech(d.telephone)}" style="color:${BLEU};">${ech(d.telephone)}</a></td></tr>
      <tr><td style="padding:4px 0;color:#7b8794;">Courriel</td><td style="padding:4px 0;"><a href="mailto:${ech(d.email)}" style="color:${BLEU};">${ech(d.email)}</a></td></tr>
      <tr><td style="padding:4px 0;color:#7b8794;">Adresse</td><td style="padding:4px 0;">${ech(d.adresse || "—")}, ${ech(d.code_postal || "")} ${ech(d.ville || "")}</td></tr>
      <tr><td style="padding:4px 0;color:#7b8794;">Accès</td><td style="padding:4px 0;">${ech(d.acces || "—")}</td></tr>
      <tr><td style="padding:4px 0;color:#7b8794;">Souhait</td><td style="padding:4px 0;">${ech(d.date_souhaitee ? dateFr(d.date_souhaitee) : "—")} ${ech(d.creneau || "")}</td></tr>
    </table>
    ${d.message ? `<p style="margin:16px 0;padding:12px 14px;background:#f5f8fc;border-left:3px solid ${BLEU};white-space:pre-wrap;">${ech(d.message)}</p>` : ""}
    ${chiffre}
    ${bouton(urlAdmin, "Ouvrir dans la console")}`;
  const texte = `${d.total_eur != null ? "NOUVELLE RESERVATION CHIFFREE" : "NOUVELLE DEMANDE A CHIFFRER"}

Reference  : ${d.reference}
Prestation : ${d.prestation_nom}
Client     : ${d.nom} (${d.type_client || "-"})
Telephone  : ${d.telephone}
Courriel   : ${d.email}
Adresse    : ${d.adresse || "-"}, ${d.code_postal || ""} ${d.ville || ""}
Acces      : ${d.acces || "-"}
Souhait    : ${d.date_souhaitee ? dateFr(d.date_souhaitee) : "-"} ${d.creneau || ""}
${d.message ? `\nMessage du client :\n${d.message}\n` : ""}
${d.total_eur != null ? lignesTexte(lignes, d.total_eur) : "A CHIFFRER (prestation sur devis)"}

Console : ${urlAdmin}`;

  return {
    sujet:
      (d.total_eur != null ? `Réservation ${eur(d.total_eur)}` : "Demande à chiffrer") +
      ` — ${d.prestation_nom} — ${d.nom} (${d.reference})`,
    html: enveloppe(site, "Nouvelle demande", corps, ""),
    texte,
  };
}

/* --------------------------------------------------------------- relances */

const RELANCES = [
  {
    cle: "relance1",
    sujet: (d) => `Votre devis MathClean est toujours valable (${d.reference})`,
    intro:
      "Je reviens vers vous au sujet du devis envoyé il y a quelques jours. " +
      "Il est toujours valable, et rien n'a changé.",
    relance:
      "Si vous hésitez sur un point — le périmètre, la date, un poste du " +
      "devis — dites-le moi : c'est plus simple d'ajuster maintenant.",
  },
  {
    cle: "relance2",
    sujet: (d) => `Votre devis — avez-vous une question ? (${d.reference})`,
    intro:
      "Votre devis n'a pas encore eu de suite, et c'est très bien ainsi : " +
      "rien ne presse de votre côté.",
    relance:
      "Je préfère quand même poser la question une fois — s'il manque une " +
      "information pour décider, je vous la donne. Et si le besoin a disparu, " +
      "dites-le moi d'un mot, je classe le dossier.",
  },
  {
    cle: "relance3",
    sujet: (d) => `Je clos votre dossier ${d.reference} — sauf avis contraire`,
    intro:
      "Sans nouvelles de votre part, je vais classer cette demande. " +
      "Ce n'est pas un reproche : un devis sans suite est une réponse aussi.",
    relance:
      "Si vous souhaitez le reprendre plus tard, gardez ce message : le lien " +
      "reste actif et je rétablirai le prix s'il a bougé entre-temps.",
  },
];

export function relance(site, d, numero, urlDevis) {
  const r = RELANCES[numero - 1];
  const montant =
    d.total_eur != null
      ? `<p style="padding:12px 14px;background:#f5f8fc;border-left:3px solid ${BLEU};"><strong>${ech(d.prestation_nom)}</strong> — ${ech(eur(d.total_eur))}</p>`
      : `<p style="padding:12px 14px;background:#f5f8fc;border-left:3px solid ${BLEU};"><strong>${ech(d.prestation_nom)}</strong></p>`;
  const corps = `
    ${titre("Votre devis MathClean")}
    <p>Bonjour ${ech(d.nom)},</p>
    <p>${ech(r.intro)}</p>
    ${montant}
    <p>${ech(r.relance)}</p>
    ${bouton(urlDevis, "Revoir le devis")}
    <p style="margin-top:22px;">Mathéo Céleste<br>
    <span style="color:#7b8794;">MathClean · ${ech(site.tel)}</span></p>`;
  const texte = `Bonjour ${d.nom},

${r.intro}

${d.prestation_nom}${d.total_eur != null ? ` - ${eur(d.total_eur)}` : ""}

${r.relance}

Revoir le devis : ${urlDevis}

Matheo Celeste - MathClean - ${site.tel}`;
  return {
    sujet: r.sujet(d),
    html: enveloppe(site, "Votre devis MathClean", corps, `Devis n° ${ech(d.reference)}.`),
    texte,
  };
}

/* ------------------------------------------------- la veille, puis l'avis */

export function veilleIntervention(site, d) {
  const corps = `
    ${titre("Rendez-vous demain")}
    <p>Bonjour ${ech(d.nom)},</p>
    <p>Un mot pour confirmer notre rendez-vous de demain,
    <strong>${ech(dateFr(d.date_intervention))}</strong>${d.creneau ? `, ${ech(d.creneau.toLowerCase())}` : ""},
    au ${ech(d.adresse || "")} ${ech(d.code_postal || "")} ${ech(d.ville || "")}.</p>
    <p>Rien à préparer de particulier. Si vous pouvez dégager l'accès et
    libérer une prise de courant à proximité, on gagne du temps tous les deux.</p>
    <p>Un imprévu ? Appelez-moi au
    <a href="tel:${ech(site.tel_lien)}" style="color:${BLEU};">${ech(site.tel)}</a>,
    on décale sans frais.</p>
    <p style="margin-top:22px;">Mathéo Céleste<br>
    <span style="color:#7b8794;">MathClean</span></p>`;
  const texte = `Bonjour ${d.nom},

Un mot pour confirmer notre rendez-vous de demain, ${dateFr(d.date_intervention)}${d.creneau ? `, ${d.creneau.toLowerCase()}` : ""},
au ${d.adresse || ""} ${d.code_postal || ""} ${d.ville || ""}.

Rien a preparer de particulier. Si vous pouvez degager l'acces et liberer une
prise de courant a proximite, on gagne du temps tous les deux.

Un imprevu ? Appelez-moi au ${site.tel}, on decale sans frais.

Matheo Celeste - MathClean`;
  return {
    sujet: `Rendez-vous demain — ${dateCourte(d.date_intervention)}`,
    html: enveloppe(site, "Rendez-vous demain", corps, ""),
    texte,
  };
}

export function demandeAvis(site, d) {
  const corps = `
    ${titre("Un avis, si le travail vous a convenu")}
    <p>Bonjour ${ech(d.nom)},</p>
    <p>J'espère que le résultat tient ses promesses quelques jours après.</p>
    <p>MathClean est une entreprise d'une personne, sans commercial et sans
    publicité : les avis Google sont à peu près la seule chose qui fait venir
    les clients suivants. Si le travail vous a convenu, deux lignes m'aident
    réellement.</p>
    ${bouton(site.avis_url, "Laisser un avis Google", OR)}
    <p>Et si quelque chose ne va pas, dites-le moi d'abord à moi : je reviens
    le corriger. Un avis sert à décrire ce qui s'est passé, pas à régler un
    problème que je peux encore résoudre.</p>
    <p style="margin-top:22px;">Mathéo Céleste<br>
    <span style="color:#7b8794;">MathClean · ${ech(site.tel)}</span></p>`;
  const texte = `Bonjour ${d.nom},

J'espere que le resultat tient ses promesses quelques jours apres.

MathClean est une entreprise d'une personne, sans commercial et sans
publicite : les avis Google sont a peu pres la seule chose qui fait venir les
clients suivants. Si le travail vous a convenu, deux lignes m'aident
reellement.

Laisser un avis : ${site.avis_url}

Et si quelque chose ne va pas, dites-le moi d'abord a moi : je reviens le
corriger.

Matheo Celeste - MathClean - ${site.tel}`;
  return {
    sujet: "Votre avis sur l'intervention MathClean",
    html: enveloppe(site, "Un avis, si le travail vous a convenu", corps, ""),
    texte,
  };
}

/* ------------------------------------------------- devis accepté : les deux */

export function accepteClient(site, d, lignes) {
  const corps = `
    ${titre("Devis accepté — c'est noté")}
    <p>Bonjour ${ech(d.nom)},</p>
    <p>J'ai bien reçu votre acceptation du devis ${ech(d.reference)}.</p>
    ${d.total_eur != null ? tableauLignes(lignes, d.total_eur) : ""}
    <p>Je vous appelle pour caler le créneau définitif. Vous recevrez un
    rappel la veille de l'intervention.</p>
    <p><strong>Aucun acompte</strong> : vous réglez après, une fois le
    résultat constaté avec moi.</p>
    <p style="margin-top:22px;">Mathéo Céleste<br>
    <span style="color:#7b8794;">MathClean · ${ech(site.tel)}</span></p>`;
  const texte = `Bonjour ${d.nom},

J'ai bien recu votre acceptation du devis ${d.reference}.
${d.total_eur != null ? `\n${lignesTexte(lignes, d.total_eur)}\n` : ""}
Je vous appelle pour caler le creneau definitif. Vous recevrez un rappel la
veille de l'intervention.

Aucun acompte : vous reglez apres, une fois le resultat constate avec moi.

Matheo Celeste - MathClean - ${site.tel}`;
  return {
    sujet: `Devis accepté — ${d.reference}`,
    html: enveloppe(site, "Devis accepté", corps, ""),
    texte,
  };
}

export function accepteArtisan(site, d, urlAdmin) {
  const corps = `
    ${titre("Devis accepté")}
    <p><strong>${ech(d.nom)}</strong> vient d'accepter le devis
    ${ech(d.reference)}${d.total_eur != null ? ` (${ech(eur(d.total_eur))})` : ""}.</p>
    <p>${ech(d.prestation_nom)} — ${ech(d.ville || "")} ${ech(d.code_postal || "")}<br>
    <a href="tel:${ech(d.telephone)}" style="color:${BLEU};">${ech(d.telephone)}</a></p>
    <p><strong>À faire :</strong> appeler pour caler la date, puis la saisir
    dans la console. Le rappel de la veille et la demande d'avis en dépendent.</p>
    ${bouton(urlAdmin, "Saisir la date d'intervention")}`;
  const texte = `${d.nom} vient d'accepter le devis ${d.reference}${d.total_eur != null ? ` (${eur(d.total_eur)})` : ""}.

${d.prestation_nom} - ${d.ville || ""} ${d.code_postal || ""}
Telephone : ${d.telephone}

A FAIRE : appeler pour caler la date, puis la saisir dans la console.
Le rappel de la veille et la demande d'avis en dependent.

${urlAdmin}`;
  return {
    sujet: `ACCEPTÉ — ${d.nom} — ${d.prestation_nom} (${d.reference})`,
    html: enveloppe(site, "Devis accepté", corps, ""),
    texte,
  };
}
