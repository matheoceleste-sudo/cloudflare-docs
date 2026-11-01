/* Envoi de courriel, et journal d'envoi.
 *
 * Deux fournisseurs sont reconnus, choisis par la clé présente dans les
 * secrets du Worker — rien à configurer d'autre :
 *
 *   RESEND_API_KEY  -> Resend   (3 000 courriels par mois en gratuit)
 *   BREVO_API_KEY   -> Brevo    (300 par jour en gratuit, société française)
 *
 * Si aucune des deux n'est posée, le système ne plante pas : il journalise
 * l'envoi en « erreur » avec le motif, et l'administration l'affiche. Un site
 * qui perd silencieusement les devis serait pire qu'un site sans automatisme.
 */

/* Au-delà, on cesse de représenter : une adresse fausse ne se corrigera
 * pas d'elle-même, et la console affiche l'échec pour qu'il soit traité. */
const MAX_TENTATIVES = 5;

/** Adresse d'expédition, et nom affiché. */
function expediteur(env) {
  const adresse = env.EXPEDITEUR || "devis@mathclean.fr";
  const nom = env.EXPEDITEUR_NOM || "MathClean";
  return { adresse, nom, complet: `${nom} <${adresse}>` };
}

async function viaResend(env, msg) {
  const e = expediteur(env);
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      authorization: `Bearer ${env.RESEND_API_KEY}`,
      "content-type": "application/json",
    },
    body: JSON.stringify({
      from: e.complet,
      to: [msg.a],
      reply_to: env.REPONDRE_A || env.CONTACT_EMAIL,
      subject: msg.sujet,
      html: msg.html,
      text: msg.texte,
    }),
  });
  if (!r.ok) throw new Error(`Resend ${r.status} : ${(await r.text()).slice(0, 300)}`);
  return "resend";
}

async function viaBrevo(env, msg) {
  const e = expediteur(env);
  const r = await fetch("https://api.brevo.com/v3/smtp/email", {
    method: "POST",
    headers: {
      "api-key": env.BREVO_API_KEY,
      "content-type": "application/json",
      accept: "application/json",
    },
    body: JSON.stringify({
      sender: { email: e.adresse, name: e.nom },
      to: [{ email: msg.a }],
      replyTo: { email: env.REPONDRE_A || env.CONTACT_EMAIL },
      subject: msg.sujet,
      htmlContent: msg.html,
      textContent: msg.texte,
    }),
  });
  if (!r.ok) throw new Error(`Brevo ${r.status} : ${(await r.text()).slice(0, 300)}`);
  return "brevo";
}

/**
 * Envoie un courriel et le journalise.
 *
 * `type` est unique par demande : la contrainte de base refuse le second
 * envoi du même type. C'est volontaire, et c'est ce qui rend les relances
 * rejouables sans risque — un cron qui repasse deux fois dans la journée
 * n'écrit rien la seconde fois.
 *
 * @returns {Promise<boolean>} true si le courriel est parti maintenant.
 */
export async function envoyer(env, demandeId, type, msg) {
  const maintenant = new Date().toISOString();

  // Réservation de la place dans le journal, avant l'envoi. Deux chemins :
  //   — la ligne n'existe pas : on la crée, on est seul à la tenir ;
  //   — elle existe en échec et n'a pas épuisé ses tentatives : on la reprend.
  // Dans tous les autres cas (déjà partie, déjà en cours, trop d'échecs), on
  // renonce sans rien envoyer. C'est ce qui rend les passes rejouables.
  let reserve = false;
  try {
    await env.DB.prepare(
      `INSERT INTO courriels (demande_id, type, envoye_le, destinataire, statut, tentatives)
       VALUES (?, ?, ?, ?, 'en_cours', 1)`
    ).bind(demandeId, type, maintenant, msg.a).run();
    reserve = true;
  } catch {
    const r = await env.DB.prepare(
      `UPDATE courriels
          SET statut = 'en_cours', tentatives = tentatives + 1,
              envoye_le = ?, destinataire = ?
        WHERE demande_id = ? AND type = ? AND statut = 'erreur'
          AND tentatives < ?`
    ).bind(maintenant, msg.a, demandeId, type, MAX_TENTATIVES).run();
    reserve = ((r.meta && r.meta.changes) || 0) > 0;
  }
  if (!reserve) return false;

  let resultat = "ok";
  let detail = null;
  try {
    if (env.RESEND_API_KEY) detail = await viaResend(env, msg);
    else if (env.BREVO_API_KEY) detail = await viaBrevo(env, msg);
    else throw new Error("aucune clé d'envoi configurée (RESEND_API_KEY ou BREVO_API_KEY)");
  } catch (err) {
    resultat = "erreur";
    detail = String(err && err.message ? err.message : err).slice(0, 500);
  }

  await env.DB.prepare(
    `UPDATE courriels SET statut = ?, detail = ? WHERE demande_id = ? AND type = ?`
  ).bind(resultat, detail, demandeId, type).run();

  return resultat === "ok";
}

/**
 * Remet à zéro le compteur d'un envoi en échec, pour le forcer à repartir.
 * Appelé depuis la console, quand on vient de corriger la cause.
 */
export async function reprendre(env, demandeId, type) {
  const ou = type ? `AND type = ?` : ``;
  const req = env.DB.prepare(
    `UPDATE courriels SET tentatives = 0
      WHERE demande_id = ? AND statut = 'erreur' ${ou}`
  );
  await (type ? req.bind(demandeId, type) : req.bind(demandeId)).run();
}
