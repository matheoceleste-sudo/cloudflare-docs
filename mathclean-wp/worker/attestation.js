/* L'attestation de nettoyage et d'entretien de hotte, servie depuis la console.
 *
 * Le document n'est pas réécrit ici : c'est le même fichier que celui que
 * Mathéo garde sur son téléphone, importé tel quel
 * (documents/attestation-hotte.html). On lui ajoute seulement un bloc JSON
 * que la page lit au chargement pour remplir les champs qu'on connaît déjà.
 *
 * Ce choix est le coeur de l'affaire : un gabarit recopié dans le Worker
 * aurait dérivé du fichier autonome au premier changement, et personne ne
 * s'en serait aperçu avant qu'un client reçoive la mauvaise version.
 */

import modele from "../documents/attestation-hotte.html";

/** Date du jour à Paris, au format AAAA-MM-JJ attendu par un champ date. */
function jourParis(decalageJours) {
  const d = new Date(Date.now() + (decalageJours || 0) * 864e5);
  return new Intl.DateTimeFormat("fr-CA", {
    timeZone: "Europe/Paris",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(d);
}

/**
 * Numéro d'attestation, dérivé de la référence du devis quand il y en a une.
 *
 * MC-2026-0042 donne AT-2026-0042 : les deux pièces d'un même dossier portent
 * le même numéro, ce qui évite d'avoir à les rapprocher plus tard.
 */
function numero(reference) {
  const m = String(reference || "").match(/^MC-(\d{4})-(\d+)$/);
  if (m) return `AT-${m[1]}-${m[2]}`;
  const annee = new Intl.DateTimeFormat("fr-FR", {
    timeZone: "Europe/Paris",
    year: "numeric",
  }).format(new Date());
  return `AT-${annee}-`;
}

/**
 * Ce que la console connaît déjà, et qu'il serait absurde de retaper.
 *
 * Volontairement limité à l'identité du client et aux dates. Rien de ce qui
 * relève du constat — longueur de conduit, trappes ouvertes, état avant,
 * réserves — n'est pré-rempli : ces champs-là ne se devinent pas depuis une
 * fiche de réservation, et un document qui les proposerait tout faits
 * inciterait à les valider sans les avoir regardés.
 */
function valeurs(d) {
  if (!d) return {};
  const cpVille = [d.code_postal, d.ville].filter(Boolean).join(" ");
  return {
    "a-num": numero(d.reference),
    "a-raison": d.nom || "",
    "a-adresse": d.adresse || "",
    "a-cpville": cpVille,
    // Pas d'interlocuteur : le champ attend une personne et sa qualité
    // (« M. Dubois, gérant »). Y recopier la raison sociale ferait imprimer
    // une mention qui ne veut rien dire, et qu'il faudrait effacer.
    "a-devis": d.reference || "",
    "d-etablie": jourParis(0),
    "d-interv": d.date_intervention || d.date_souhaitee || jourParis(0),
  };
}

/** Le document, pré-rempli si une demande est fournie. */
export function rendreAttestation(demande) {
  const v = valeurs(demande);
  if (!Object.keys(v).length) return modele;

  // Le bloc est posé AVANT le script de la page, pas avant </body> : le
  // script de la page est la dernière chose du document, et un JSON inséré
  // après lui n'existerait pas encore au moment où il le cherche.
  const bloc =
    '<script id="mc-prefill" type="application/json">' +
    JSON.stringify(v).replace(/</g, "\\u003c") +
    "<\/script>\n";
  const ancre = "\n<script>\n";
  if (!modele.includes(ancre)) {
    // Le gabarit a changé de forme : mieux vaut servir le document vierge
    // que de risquer un pré-remplissage posé au mauvais endroit.
    console.error("attestation : ancre de pré-remplissage introuvable");
    return modele;
  }
  return modele.replace(ancre, "\n" + bloc + ancre.slice(1));
}
