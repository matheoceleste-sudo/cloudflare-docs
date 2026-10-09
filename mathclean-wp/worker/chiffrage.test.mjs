/* Contrôle du chiffrage serveur.
 *
 *   node worker/chiffrage.test.mjs
 *
 * Ce que ces cas vérifient, dans l'ordre d'importance : qu'un montant envoyé
 * par le navigateur ne change jamais le prix, qu'un indice hors grille ne
 * fabrique pas de ligne, et que les frais de déplacement ne peuvent pas être
 * minorés depuis la page.
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

console.log("\nAuto — pack seul");
{
  const r = chiffrer({ service: "nettoyage-automobile-paris", univers: "auto", pack: 0 }, "93150");
  verifie("un pack donne une ligne", r.lignes.length >= 1, true);
  verifie("au prix de la grille", r.lignes[0].total, TARIFS.packs[0].prix);
  verifie("régime ferme", r.regime, "ferme");
}

console.log("\nAuto — pack et options, sans doublon");
{
  const r = chiffrer(
    { service: "nettoyage-automobile-paris", univers: "auto", pack: 3, options: [0, 1, 0, 1] },
    "93150"
  );
  const attendu = TARIFS.packs[3].prix + TARIFS.options[0].prix + TARIFS.options[1].prix;
  const sansDep = r.lignes.filter((l) => !l.deplacement).reduce((s, l) => s + l.total, 0);
  verifie("une option cochée deux fois ne compte qu'une fois", sansDep, attendu);
}

console.log("\nLe prix posté par le navigateur est ignoré");
{
  const r = chiffrer(
    {
      service: "nettoyage-automobile-paris", univers: "auto", pack: 0,
      prix: 1, total: 1, montant: 1,
      packs: [{ nom: "Gratuit", prix: 0 }],
    },
    "93150"
  );
  verifie("le pack garde son prix de grille", r.lignes[0].total, TARIFS.packs[0].prix);
}

console.log("\nIndices hors grille");
{
  const r = chiffrer({ service: "nettoyage-automobile-paris", univers: "auto", pack: 99 }, "93150");
  verifie("pack inexistant : aucune ligne", r.lignes.length, 0);
  verifie("et donc pas de prix ferme", r.total, null);

  const r2 = chiffrer(
    { service: "nettoyage-automobile-paris", univers: "auto", pack: 0, options: [99, -1, "a"] },
    "93150"
  );
  verifie("options invalides : ignorées", r2.lignes.filter((l) => !l.deplacement).length, 1);
}

console.log("\nTextile — quantités");
{
  const r = chiffrer({ service: "nettoyage-textile-paris", univers: "textile", textile: { 0: 3 } }, "93150");
  const l = r.lignes.find((x) => !x.deplacement);
  verifie("trois articles au tarif unitaire", l.total, TARIFS.textile[0].prix * 3);
  verifie("la quantité est reportée", l.qte, 3);

  const r2 = chiffrer(
    { service: "nettoyage-textile-paris", univers: "textile", textile: { 0: 9999, 1: 0, 2: -5 } },
    "93150"
  );
  verifie("quantité aberrante : ligne écartée", r2.lignes.filter((x) => !x.deplacement).length, 0);
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

  const honnete = kilometres("93150", 2.5);
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
