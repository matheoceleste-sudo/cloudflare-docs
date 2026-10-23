/* Les relances : une passe par jour, déclenchée par le cron du Worker.
 *
 * Tout est rejouable. Si le cron tourne deux fois, s'il est relancé à la
 * main, ou s'il reprend après une panne, rien n'est envoyé en double :
 * l'unicité (demande, type de courriel) est garantie par la base, pas par
 * la logique d'ici.
 *
 * Le rythme est volontairement lent. Trois relances espacées, puis on classe
 * et on se tait — un prospect qui ne répond pas a répondu.
 */

import { envoyer } from "./courriel.js";
import {
  relance, veilleIntervention, demandeAvis, devisFerme, accuseSurDevis,
  notifArtisan, accepteClient, accepteArtisan,
} from "./modeles.js";
import { identite } from "./reservation.js";

/** Date du jour à Paris, décalée de `jours`, au format AAAA-MM-JJ. */
function jourParis(jours) {
  const d = new Date(Date.now() + (jours || 0) * 864e5);
  const p = new Intl.DateTimeFormat("fr-CA", {
    timeZone: "Europe/Paris",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(d);
  return p; // fr-CA donne AAAA-MM-JJ
}

function ilYA(jours) {
  return new Date(Date.now() - jours * 864e5).toISOString();
}

/** Le barème : rang de relance, délai depuis le dernier contact, en jours. */
const CADENCE = [
  { rang: 1, apres: 3, depuis: "cree_le" },
  { rang: 2, apres: 5, depuis: "derniere_relance" },
  { rang: 3, apres: 7, depuis: "derniere_relance" },
];

const CLOTURE_APRES = 7; // jours après la troisième relance

/**
 * Reconstruit un courriel à partir de son type et de la demande.
 *
 * Sert à la reprise : un envoi raté n'est pas conservé quelque part sous
 * forme de texte, il est refabriqué à l'identique depuis la base. C'est plus
 * sûr que de stocker le corps du message — et cela fait profiter les reprises
 * des corrections apportées aux gabarits entre-temps.
 */
function construire(type, site, d, lignes, urlDevis, urlAdmin) {
  switch (type) {
    case "devis":
      return d.total_eur != null
        ? { a: d.email, ...devisFerme(site, d, lignes, urlDevis) } : null;
    case "accuse":
      return { a: d.email, ...accuseSurDevis(site, d, urlDevis) };
    case "notif":
      return { a: site.contact, ...notifArtisan(site, d, lignes, urlAdmin) };
    case "relance1":
      return { a: d.email, ...relance(site, d, 1, urlDevis) };
    case "relance2":
      return { a: d.email, ...relance(site, d, 2, urlDevis) };
    case "relance3":
      return { a: d.email, ...relance(site, d, 3, urlDevis) };
    case "veille":
      return { a: d.email, ...veilleIntervention(site, d) };
    case "avis":
      return { a: d.email, ...demandeAvis(site, d) };
    case "accepte_client":
      return { a: d.email, ...accepteClient(site, d, lignes) };
    case "accepte_notif":
      return { a: site.contact, ...accepteArtisan(site, d, urlAdmin) };
    default:
      return null; // alerte_chiffrage et consorts : non rejoués
  }
}

/**
 * Reprise des envois ratés.
 *
 * C'est la première chose que fait la passe, et la plus importante. Sans
 * elle, un devis qui n'est pas parti — clé absente, panne du fournisseur,
 * quota atteint — ne partirait jamais, et le client recevrait des relances
 * sur un devis qu'il n'a pas reçu. Le compteur de tentatives borne la boucle.
 */
async function reprendreEchecs(env, site) {
  const rows = await env.DB.prepare(
    `SELECT c.id, c.type, c.demande_id
       FROM courriels c
      WHERE c.statut = 'erreur' AND c.tentatives < 5
      ORDER BY c.id LIMIT 60`
  ).all();

  let repartis = 0;
  for (const c of rows.results || []) {
    const d = await env.DB.prepare(`SELECT * FROM demandes WHERE id = ?`)
      .bind(c.demande_id).first();
    if (!d) continue;
    let lignes = [];
    try {
      lignes = JSON.parse(d.lignes || "[]");
    } catch {
      lignes = [];
    }
    const msg = construire(
      c.type, site, d, lignes,
      `${site.url}/devis/${d.jeton}`, `${site.url}/admin?demande=${d.id}`
    );
    if (!msg) continue;
    if (await envoyer(env, d.id, c.type, msg)) repartis++;
  }
  return repartis;
}

export async function passeQuotidienne(env) {
  const site = identite(env);
  const journal = {
    repris: 0, relances: 0, veilles: 0, avis: 0, clos: 0, alertes: 0,
  };

  /* 0. Avant tout : renvoyer ce qui n'était pas parti ---------------------- */
  journal.repris = await reprendreEchecs(env, site);

  /* 1. Les relances sur devis sans réponse ------------------------------- */
  for (const etape of CADENCE) {
    const limite = ilYA(etape.apres);
    const rows = await env.DB.prepare(
      `SELECT * FROM demandes
        WHERE statut IN ('devis_envoye','vu')
          AND relances = ?
          AND ${etape.depuis} IS NOT NULL
          AND ${etape.depuis} < ?
        LIMIT 40`
    ).bind(etape.rang - 1, limite).all();

    for (const d of rows.results || []) {
      const parti = await envoyer(env, d.id, `relance${etape.rang}`, {
        a: d.email,
        ...relance(site, d, etape.rang, `${site.url}/devis/${d.jeton}`),
      });
      if (parti) {
        await env.DB.prepare(
          `UPDATE demandes SET relances = ?, derniere_relance = ? WHERE id = ?`
        ).bind(etape.rang, new Date().toISOString(), d.id).run();
        journal.relances++;
      }
    }
  }

  /* 2. La clôture, sans courriel : on ne annonce pas qu'on abandonne ------ */
  const aClore = await env.DB.prepare(
    `UPDATE demandes SET statut = 'clos', clos_le = ?
      WHERE statut IN ('devis_envoye','vu') AND relances >= 3
        AND derniere_relance < ?`
  ).bind(new Date().toISOString(), ilYA(CLOTURE_APRES)).run();
  journal.clos = (aClore.meta && aClore.meta.changes) || 0;

  /* 3. Les sur-devis que l'artisan n'a pas chiffrés ----------------------- */
  const oublis = await env.DB.prepare(
    `SELECT * FROM demandes
      WHERE statut = 'nouveau' AND total_eur IS NULL AND cree_le < ?
      LIMIT 20`
  ).bind(ilYA(2)).all();
  for (const d of oublis.results || []) {
    const parti = await envoyer(env, d.id, "alerte_chiffrage", {
      a: site.contact,
      sujet: `À chiffrer depuis 2 jours — ${d.nom} (${d.reference})`,
      html: `<p>La demande <strong>${d.reference}</strong> de ${d.nom}
             (${d.prestation_nom}) attend un chiffrage depuis deux jours.</p>
             <p>Le client a reçu un accusé de réception qui annonçait un rappel
             sous 24 h.</p>
             <p><a href="${site.url}/admin?demande=${d.id}">Ouvrir dans la console</a></p>`,
      texte: `La demande ${d.reference} de ${d.nom} (${d.prestation_nom}) attend un
chiffrage depuis deux jours. Le client a recu un accuse qui annoncait un
rappel sous 24 h.

${site.url}/admin?demande=${d.id}`,
    });
    if (parti) journal.alertes++;
  }

  /* 4. Le rappel de la veille -------------------------------------------- */
  const demain = jourParis(1);
  const veilles = await env.DB.prepare(
    `SELECT * FROM demandes
      WHERE date_intervention = ? AND statut IN ('accepte','planifie')
      LIMIT 40`
  ).bind(demain).all();
  for (const d of veilles.results || []) {
    const parti = await envoyer(env, d.id, "veille", {
      a: d.email,
      ...veilleIntervention(site, d),
    });
    if (parti) journal.veilles++;
  }

  /* 5. La demande d'avis, trois jours après ------------------------------- */
  const ilYATroisJours = jourParis(-3);
  const apres = await env.DB.prepare(
    `SELECT * FROM demandes
      WHERE date_intervention = ? AND statut IN ('accepte','planifie','realise')
      LIMIT 40`
  ).bind(ilYATroisJours).all();
  for (const d of apres.results || []) {
    const parti = await envoyer(env, d.id, "avis", {
      a: d.email,
      ...demandeAvis(site, d),
    });
    if (parti) {
      await env.DB.prepare(
        `UPDATE demandes SET statut = 'realise' WHERE id = ? AND statut != 'realise'`
      ).bind(d.id).run();
      journal.avis++;
    }
  }

  return journal;
}
