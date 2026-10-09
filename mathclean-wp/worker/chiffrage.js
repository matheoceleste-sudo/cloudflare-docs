/* Chiffrage d'une demande, côté serveur.
 *
 * Règle unique et non négociable : aucun montant n'est repris du formulaire.
 * Le navigateur envoie ce que le client a *choisi* — un numéro de pack, des
 * numéros d'options, des quantités — et le serveur applique sa propre grille.
 * Un prix posté depuis la page n'est jamais lu.
 *
 * La grille, elle, est produite par build.py à partir des mêmes données que
 * les pages du site (worker/tarifs.js, fichier généré). Le configurateur et
 * le devis ne peuvent donc pas diverger : il n'y a qu'une source.
 */

import { TARIFS, COMMUNES, DEPARTEMENTS } from "./tarifs.js";

/** Distance routière approchée depuis l'atelier, en kilomètres. */
export function distanceAtelier(lat, lon) {
  const d = TARIFS.deplacement;
  const r = Math.PI / 180;
  const dla = (lat - d.lat) * r;
  const dlo = (lon - d.lon) * r;
  const a =
    Math.sin(dla / 2) ** 2 +
    Math.cos(d.lat * r) * Math.cos(lat * r) * Math.sin(dlo / 2) ** 2;
  return 6371 * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a)) * d.coef_route;
}

/**
 * Kilomètres retenus pour le déplacement.
 *
 * Le code postal décide, pas le navigateur. Le configurateur interroge l'IGN
 * et affiche une distance routière réelle, plus juste ; mais elle arrive par
 * le formulaire, donc elle est modifiable par le visiteur. On la prend comme
 * indication et on la borne : elle ne peut pas descendre sous la distance à
 * vol d'oiseau majorée de la commune déclarée.
 */
export function kilometres(codePostal, kmAnnonce) {
  const cp = String(codePostal || "").trim();
  const point = COMMUNES[cp] || DEPARTEMENTS[cp.slice(0, 2)];
  const plancher = point ? distanceAtelier(point[0], point[1]) : 0;

  const annonce = Number(kmAnnonce);
  const utilisable = Number.isFinite(annonce) && annonce > 0 && annonce < 300;
  if (!utilisable) return { km: plancher, source: point ? "code postal" : "inconnu" };
  if (annonce < plancher - 1) return { km: plancher, source: "code postal" };
  return { km: annonce, source: "itinéraire" };
}

/** Frais de déplacement : un palier entamé est un palier dû. */
export function fraisDeplacement(km) {
  const d = TARIFS.deplacement;
  if (!(km > 0)) return 0;
  return Math.ceil(km / d.palier_km) * d.palier_eur;
}

function entier(v, min, max) {
  const n = parseInt(v, 10);
  if (!Number.isFinite(n) || n < min || n > max) return null;
  return n;
}

/**
 * Recalcule les lignes et le total d'une demande.
 *
 * @param {object} selection  ce que le client a choisi (jamais des montants)
 * @param {string} codePostal pour borner le déplacement
 * @returns {{lignes: Array, total: number|null, regime: string, km: number,
 *            deplacement: number, service: object|null}}
 */
export function chiffrer(selection, codePostal) {
  const sel = selection && typeof selection === "object" ? selection : {};
  const service =
    TARIFS.services.find((s) => s.slug === sel.service) || null;

  const lignes = [];
  let total = 0;
  let aPrixFixe = false;

  if (sel.univers === "auto") {
    const ip = entier(sel.pack, 0, TARIFS.packs.length - 1);
    if (ip !== null) {
      const p = TARIFS.packs[ip];
      lignes.push({ libelle: p.nom, qte: 1, pu: p.prix, total: p.prix });
      total += p.prix;
      aPrixFixe = true;

      const vues = new Set();
      for (const o of Array.isArray(sel.options) ? sel.options : []) {
        const io = entier(o, 0, TARIFS.options.length - 1);
        if (io === null || vues.has(io)) continue;
        vues.add(io);
        const opt = TARIFS.options[io];
        lignes.push({ libelle: opt.nom, qte: 1, pu: opt.prix, total: opt.prix });
        total += opt.prix;
      }
    }
  } else if (sel.univers === "textile") {
    const q = sel.textile && typeof sel.textile === "object" ? sel.textile : {};
    for (const cle of Object.keys(q)) {
      const it = entier(cle, 0, TARIFS.textile.length - 1);
      const n = entier(q[cle], 1, 20);
      if (it === null || n === null) continue;
      const a = TARIFS.textile[it];
      lignes.push({ libelle: a.nom, qte: n, pu: a.prix, total: a.prix * n });
      total += a.prix * n;
      aPrixFixe = true;
    }
  }

  const d = kilometres(codePostal, sel.km);
  const frais = aPrixFixe ? fraisDeplacement(d.km) : 0;
  if (aPrixFixe && frais > 0) {
    lignes.push({
      libelle: `Déplacement (${Math.round(d.km)} km depuis Le Blanc-Mesnil)`,
      qte: 1,
      pu: frais,
      total: frais,
      deplacement: true,
    });
    total += frais;
  }

  return {
    lignes,
    total: aPrixFixe ? total : null,
    regime: aPrixFixe ? "ferme" : "surdevis",
    km: d.km,
    source_km: d.source,
    deplacement: frais,
    service,
  };
}
