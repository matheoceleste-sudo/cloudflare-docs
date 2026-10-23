/* Contrôle du chiffrage serveur.
 *
 *   node worker/chiffrage.test.mjs
 *
 * Ce que ces cas vérifient, dans l'ordre d'importance : qu'une grille ou un
 * montant envoyés par le navigateur ne fabriquent jamais de prix, qu'un indice
 * hors grille ne crée pas de ligne, et que les frais de déplacement ne peuvent
 * pas être minorés depuis la page.
 *
 * Le catalogue ne compte plus de prestation à prix fixe : la grille est vide
 * côté packs, options et textile. Les cas ci-dessous le vérifient plutôt que
 * de supposer des tarifs qui n'existent plus.
 */

import { chiffrer, fraisDeplacement, kilometres } from "./chiffrage.js";
import { TARIFS } from "./tarifs.js";

let echecs = 0;
let total = 0;

function verifie(nom, obtenu, attendu) {
  total++;
  const a = JSON.stringify(obtenu);
  const b = JSON.stringify(attendu);
  if (a === b) {
    console.log(`  ok   ${nom}`);
  } else {
    echecs++;
    console.log(`  ÉCHEC ${nom}\n        obtenu  : ${a}\n        attendu : ${b}`);
  }
}

console.log("\nGrille lue depuis tarifs.js");
console.log(`  ${TARIFS.packs.length} packs, ${TARIFS.options.length} options, ` +
            `${TARIFS.textile.length} articles textile, ${TARIFS.services.length} prestations`);

console.log("\nLe catalogue ne contient plus de prix fixe");
{
  verifie("aucun pack en grille", TARIFS.packs.length, 0);
  verifie("aucune option en grille", TARIFS.options.length, 0);
  verifie("aucun article textile en grille", TARIFS.textile.length, 0);
  verifie("les trois prestations relèvent du devis",
    TARIFS.services.every((s) => s.univers === "devis"), true);
  verifie("et elles sont bien trois", TARIFS.services.length, 3);
}

console.log("\nUne grille fabriquée par le navigateur est ignorée");
{
  // Le cas qui compte vraiment : le visiteur poste sa propre grille, avec ses
  // propres prix, en plus d'un montant tout fait. Rien ne doit en sortir.
  const r = chiffrer(
    {
      service: "nettoyage-fin-de-chantier-paris", univers: "auto", pack: 0,
      prix: 1, total: 1, montant: 1,
      packs: [{ nom: "Offert", prix: 0 }, { nom: "Cher", prix: 999 }],
      options: [{ nom: "Faux", prix: 0 }],
      textile: [{ nom: "Faux", prix: 0 }],
    },
    "93150"
  );
  verifie("aucune ligne fabriquée depuis la requête",
    r.lignes.filter((l) => !l.deplacement).length, 0);
  verifie("aucun total inventé", r.total, null);
}

console.log("\nIndices hors grille");
{
  const r = chiffrer(
    { service: "nettoyage-haute-pression-paris", univers: "auto", pack: 99 }, "93150");
  verifie("pack inexistant : aucune ligne", r.lignes.length, 0);
  verifie("et donc pas de prix ferme", r.total, null);

  const r2 = chiffrer(
    { service: "nettoyage-haute-pression-paris", univers: "textile",
      textile: { 0: 3, 1: -5, 2: "a" } },
    "93150"
  );
  verifie("quantités sur une grille vide : aucune ligne",
    r2.lignes.filter((l) => !l.deplacement).length, 0);
}

console.log("\nPrestations sur devis");
{
  const r = chiffrer({ service: "nettoyage-hottes-paris", univers: "devis" }, "75011");
  verifie("aucun montant inventé", r.total, null);
  verifie("régime sur devis", r.regime, "surdevis");
  verifie("pas de frais de déplacement non plus", r.deplacement, 0);
}

console.log("\nFrais de déplacement");
{
  verifie("toute tranche entamée est due (1 km)", fraisDeplacement(1), TARIFS.deplacement.palier_eur);
  verifie("pile un palier", fraisDeplacement(TARIFS.deplacement.palier_km), TARIFS.deplacement.palier_eur);
  verifie("un mètre de plus, un palier de plus",
    fraisDeplacement(TARIFS.deplacement.palier_km + 0.001), TARIFS.deplacement.palier_eur * 2);
  verifie("distance nulle, rien", fraisDeplacement(0), 0);

  // Le plancher : un visiteur qui annonce 1 km depuis Versailles est corrigé.
  const triche = kilometres("78000", 1);
  verifie("km minoré depuis la page : corrigé par le code postal", triche.source, "code postal");
  verifie("et la distance retenue est réelle", triche.km > 15, true);

  // Le Blanc-Mesnil est à une dizaine de kilomètres de Tremblay : 11 km
  // annoncés par l'itinéraire sont au-dessus du plancher, donc conservés.
  const honnete = kilometres("93150", 11);
  verifie("une distance crédible est conservée", honnete.source, "itinéraire");

  const absurde = kilometres("75011", 99999);
  verifie("une distance absurde est écartée", absurde.source, "code postal");
}

console.log("\nCode postal inconnu");
{
  const r = kilometres("99999", 12);
  verifie("on retombe sur la distance annoncée", Math.round(r.km), 12);
}

console.log(`\n${total - echecs}/${total} vérifications passées.`);
if (echecs) {
  console.log(`${echecs} ÉCHEC(S).`);
  process.exit(1);
}
