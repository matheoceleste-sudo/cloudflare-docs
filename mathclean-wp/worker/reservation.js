/* Réception des formulaires du site.
 *
 *   POST /api/reservation  configurateur : porte une sélection chiffrable
 *   POST /api/devis        demande de devis libre : toujours chiffrée à la main
 *   POST /api/contact      message : notifié et accusé, sans cycle de devis
 *
 * Enchaînement commun : validation, chiffrage serveur, enregistrement, puis
 * envois. Les envois passent par waitUntil — le visiteur est redirigé tout de
 * suite et n'attend pas l'API du fournisseur de courriel.
 */

import {
  propre, emailValide, telephoneValide, jeton, empreinteIp,
  prochaineReference, versPage,
} from "./commun.js";
import { chiffrer } from "./chiffrage.js";
import { TARIFS } from "./tarifs.js";
import { envoyer } from "./courriel.js";
import { devisFerme, accuseSurDevis, notifArtisan } from "./modeles.js";

const MAX_PAR_HEURE = 4;

/** Identité de l'entreprise, injectée dans les gabarits. */
export function identite(env) {
  return {
    nom: "MathClean",
    url: env.SITE_URL || "https://mathclean.fr",
    tel: "06 23 07 52 59",
    tel_lien: "+33623075259",
    adresse: "2 rue Poussin",
    cp: "93150",
    ville: "Le Blanc-Mesnil",
    siret: "924 565 990 00010",
    avis_url: "https://g.page/r/CaK1p63WHA51EBM/review",
    contact: env.CONTACT_EMAIL || "matheoceleste@gmail.com",
  };
}

const RETOUR = {
  reservation: "/reservation",
  devis: "/devis",
  contact: "/contact",
};

/** Un seul champ pour « Code postal et ville » sur le formulaire de devis. */
function scinderCpVille(valeur) {
  const m = String(valeur || "").match(/\b(\d{5})\b/);
  const cp = m ? m[1] : "";
  const ville = String(valeur || "").replace(/\b\d{5}\b/, "").replace(/^[\s,–-]+|[\s,–-]+$/g, "");
  return { cp, ville };
}

function lire(form, ...noms) {
  for (const n of noms) {
    const v = form.get(n);
    if (v) return v;
  }
  return "";
}

function champs(form, source) {
  const brut = {
    nom: propre(lire(form, "Nom"), 120),
    email: propre(lire(form, "Email"), 160).toLowerCase(),
    telephone: propre(lire(form, "Téléphone", "Telephone"), 40),
    adresse: propre(lire(form, "Adresse"), 200),
    acces: propre(lire(form, "Accès", "Acces"), 300),
    type_client: propre(lire(form, "Type de client"), 40),
    creneau: propre(lire(form, "Créneau", "Creneau"), 60),
    message: propre(lire(form, "Message"), 2000),
    consentement: propre(lire(form, "Consentement"), 20),
    piege: propre(lire(form, "_honey"), 100),
    selection: propre(lire(form, "Sélection", "Selection"), 2000),
    prestation_libre: propre(lire(form, "Prestation"), 120),
    sujet: propre(lire(form, "Sujet"), 120),
  };

  if (source === "devis") {
    const { cp, ville } = scinderCpVille(lire(form, "Code postal et ville"));
    brut.code_postal = cp;
    brut.ville = ville;
    brut.date_souhaitee = "";
    brut.delai = propre(lire(form, "Délai souhaité", "Delai souhaite"), 80);
  } else {
    brut.code_postal = propre(lire(form, "Code postal"), 10);
    brut.ville = propre(lire(form, "Ville"), 100);
    brut.date_souhaitee = propre(lire(form, "Date souhaitée", "Date souhaitee"), 20);
    brut.delai = "";
  }
  return brut;
}

/** Retrouve la prestation, par slug (configurateur) ou par libellé (devis). */
function trouverService(slug, libelle) {
  if (slug) {
    const s = TARIFS.services.find((x) => x.slug === slug);
    if (s) return s;
  }
  const l = String(libelle || "").trim().toLowerCase();
  if (l) {
    const s = TARIFS.services.find(
      (x) => x.nav.toLowerCase() === l || x.slug === l
    );
    if (s) return s;
  }
  return null;
}

export async function recevoirDemande(request, env, ctx, source) {
  const site = identite(env);
  const retour = RETOUR[source] || "/reservation";
  const retourErreur = (motif) =>
    versPage(`${site.url}${retour}?erreur=${encodeURIComponent(motif)}`);

  let form;
  try {
    form = await request.formData();
  } catch {
    return retourErreur("formulaire illisible");
  }
  const c = champs(form, source);

  // Le piège à robots : un champ invisible qu'un humain ne remplit jamais.
  // On répond comme si tout s'était bien passé, sans rien enregistrer.
  if (c.piege) return versPage(`${site.url}/merci`);

  if (!c.nom || c.nom.length < 2) return retourErreur("nom manquant");
  if (!emailValide(c.email)) return retourErreur("adresse électronique invalide");
  if (source !== "contact" && !telephoneValide(c.telephone)) {
    return retourErreur("téléphone invalide");
  }
  if (c.telephone && !telephoneValide(c.telephone)) {
    return retourErreur("téléphone invalide");
  }
  if (!c.consentement) return retourErreur("consentement requis");

  const ip = request.headers.get("cf-connecting-ip") || "";
  const ipHash = await empreinteIp(ip, env.SEL_IP);

  // Quatre demandes par heure et par adresse. Au-delà on s'arrête avant
  // d'écrire et avant d'envoyer quoi que ce soit.
  const ilYAUneHeure = new Date(Date.now() - 3600e3).toISOString();
  const recentes = await env.DB.prepare(
    `SELECT COUNT(*) AS n FROM demandes WHERE ip_hash = ? AND cree_le > ?`
  ).bind(ipHash, ilYAUneHeure).first();
  if (recentes && recentes.n >= MAX_PAR_HEURE) {
    return retourErreur("trop de demandes en peu de temps — appelez-nous");
  }

  let selection = {};
  if (source === "reservation") {
    try {
      selection = JSON.parse(c.selection || "{}");
    } catch {
      selection = {};
    }
  }

  const chiffrage =
    source === "reservation"
      ? chiffrer(selection, c.code_postal)
      : { lignes: [], total: null, regime: "surdevis", km: 0, deplacement: 0, service: null };

  const service =
    source === "contact"
      ? { slug: "contact", nav: c.sujet || "Message depuis le site" }
      : trouverService(selection.service, c.prestation_libre) || chiffrage.service;

  if (!service) return retourErreur("prestation inconnue");

  // Le délai souhaité du formulaire de devis n'est pas une date : il rejoint
  // le message, où il sera lu, plutôt qu'un champ date qu'il ne remplit pas.
  const message = [c.delai ? `Délai souhaité : ${c.delai}` : "", c.message]
    .filter(Boolean)
    .join("\n\n");

  const maintenant = new Date().toISOString();
  const lien = jeton();
  const statutInitial =
    source === "contact"
      ? "clos"
      : chiffrage.regime === "ferme"
        ? "devis_envoye"
        : "nouveau";

  // La référence vient d'un compte : deux demandes simultanées peuvent viser
  // le même numéro. L'unicité est garantie par la base, donc on retente.
  let demandeId = null;
  let reference = null;
  for (let essai = 0; essai < 5 && demandeId === null; essai++) {
    reference = await prochaineReference(env.DB);
    try {
      const r = await env.DB.prepare(
        `INSERT INTO demandes (
           reference, jeton, cree_le, nom, email, telephone, adresse,
           code_postal, ville, acces, type_client, prestation, prestation_nom,
           regime, date_souhaitee, creneau, message, lignes, deplacement_eur,
           deplacement_km, total_eur, statut, ip_hash, agent
         ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)`
      ).bind(
        reference, lien, maintenant, c.nom, c.email, c.telephone, c.adresse,
        c.code_postal, c.ville, c.acces, c.type_client, service.slug,
        service.nav, source === "contact" ? "contact" : chiffrage.regime,
        c.date_souhaitee, c.creneau, message,
        JSON.stringify(chiffrage.lignes), chiffrage.deplacement,
        Math.round(chiffrage.km * 10) / 10, chiffrage.total,
        statutInitial, ipHash, propre(request.headers.get("user-agent"), 200)
      ).run();
      demandeId = r.meta.last_row_id;
    } catch (err) {
      if (!String(err).includes("UNIQUE")) throw err;
    }
  }
  if (demandeId === null) return retourErreur("enregistrement impossible, réessayez");

  const demande = {
    id: demandeId, reference, jeton: lien, cree_le: maintenant,
    nom: c.nom, email: c.email, telephone: c.telephone, adresse: c.adresse,
    code_postal: c.code_postal, ville: c.ville, acces: c.acces,
    type_client: c.type_client, prestation: service.slug,
    prestation_nom: service.nav, regime: chiffrage.regime,
    date_souhaitee: c.date_souhaitee, creneau: c.creneau, message,
    total_eur: chiffrage.total,
  };

  const urlDevis = `${site.url}/devis/${lien}`;
  const urlAdmin = `${site.url}/admin?demande=${demandeId}`;

  // Le visiteur part maintenant ; les courriels suivent en arrière-plan.
  ctx.waitUntil(
    (async () => {
      if (source === "contact") {
        await envoyer(env, demandeId, "accuse", {
          a: c.email,
          sujet: "Votre message est bien arrivé — MathClean",
          html: `<p>Bonjour ${demande.nom},</p><p>Votre message est bien arrivé.
                 Je vous réponds sous 24 h. Pour une urgence, appelez le
                 ${site.tel} : c'est moi qui réponds.</p>
                 <p>Mathéo Céleste — MathClean</p>`,
          texte: `Bonjour ${demande.nom},\n\nVotre message est bien arrive. Je vous reponds sous 24 h.\nPour une urgence, appelez le ${site.tel} : c'est moi qui reponds.\n\nMatheo Celeste - MathClean`,
        });
      } else if (chiffrage.regime === "ferme") {
        await envoyer(env, demandeId, "devis", {
          a: c.email,
          ...devisFerme(site, demande, chiffrage.lignes, urlDevis),
        });
      } else {
        await envoyer(env, demandeId, "accuse", {
          a: c.email,
          ...accuseSurDevis(site, demande, urlDevis),
        });
      }
      await envoyer(env, demandeId, "notif", {
        a: site.contact,
        ...notifArtisan(site, demande, chiffrage.lignes, urlAdmin),
      });
    })()
  );

  return versPage(`${site.url}/merci?ref=${encodeURIComponent(reference)}`);
}
