import type { Metadata } from "next";
import Link from "next/link";
import { CheckCircle2, ArrowRight } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Tarifs — Nettoyage professionnel MathClean",
  description: "Grille tarifaire MathClean : nettoyage bateaux, automobiles, fin de chantier, bureaux. Tarifs transparents, devis gratuit sur mesure.",
  path: "/tarifs",
});

const GRILLES = [
  {
    cat: "Bateaux & yachts",
    color: "from-blue-900 to-blue-950",
    items: [
      { label: "Voilier jusqu'à 8m", price: "À partir de 200 €" },
      { label: "Voilier 8 à 12m", price: "À partir de 350 €" },
      { label: "Yacht 12 à 18m", price: "Sur devis" },
      { label: "Grand yacht 18m+", price: "Sur devis" },
      { label: "Semi-rigide", price: "À partir de 120 €" },
    ],
  },
  {
    cat: "Automobile",
    color: "from-slate-800 to-slate-900",
    items: [
      { label: "Citadine (Clio, 208...)", price: "À partir de 80 €" },
      { label: "Berline (BMW, Mercedes...)", price: "À partir de 110 €" },
      { label: "SUV / Crossover", price: "À partir de 140 €" },
      { label: "4×4 (Range, Cayenne...)", price: "À partir de 150 €" },
      { label: "Van / Utilitaire", price: "À partir de 180 €" },
    ],
  },
  {
    cat: "Fin de chantier",
    color: "from-amber-900 to-amber-950",
    items: [
      { label: "Appartement jusqu'à 50m²", price: "À partir de 180 €" },
      { label: "Appartement 50 à 100m²", price: "À partir de 280 €" },
      { label: "Villa 100 à 200m²", price: "À partir de 480 €" },
      { label: "Local commercial", price: "Sur devis" },
      { label: "Programme neuf (multi-lots)", price: "Sur devis" },
    ],
  },
  {
    cat: "Bureaux & locaux",
    color: "from-teal-900 to-teal-950",
    items: [
      { label: "Bureau jusqu'à 50m²", price: "À partir de 80 €" },
      { label: "Bureau 50 à 150m²", price: "À partir de 180 €" },
      { label: "Contrat mensuel", price: "Sur devis" },
      { label: "Restaurant / cuisine", price: "Sur devis" },
      { label: "Hôtel / résidence", price: "Sur devis" },
    ],
  },
];

export default function TarifsPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <h1 className="font-display text-5xl font-bold text-white mb-5">Tarifs</h1>
          <p className="text-white/60 text-lg max-w-2xl mx-auto">Des prix justes pour un service d&apos;exception. Chaque devis est personnalisé selon vos besoins réels.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-6xl mx-auto px-6 grid md:grid-cols-2 gap-6">
          {GRILLES.map((g) => (
            <div key={g.cat} className="bg-white border border-pearl-cream rounded-xl overflow-hidden shadow-sm">
              <div className={`px-6 py-4 bg-gradient-to-br ${g.color}`}>
                <h2 className="font-display text-lg font-semibold text-white">{g.cat}</h2>
              </div>
              <div className="p-6 space-y-3">
                {g.items.map((item) => (
                  <div key={item.label} className="flex items-center justify-between py-2 border-b border-pearl-cream last:border-0">
                    <span className="text-sm text-navy flex items-center gap-2"><CheckCircle2 size={13} className="text-gold shrink-0" />{item.label}</span>
                    <span className="text-sm font-semibold text-gold whitespace-nowrap ml-4">{item.price}</span>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
        <div className="max-w-2xl mx-auto px-6 mt-12 text-center">
          <div className="bg-navy rounded-2xl p-8 text-white">
            <h2 className="font-display text-2xl font-bold mb-3">Devis personnalisé gratuit</h2>
            <p className="text-white/60 mb-6 text-sm">Les tarifs ci-dessus sont indicatifs. Le prix final dépend de l&apos;état, de la surface et des prestations choisies. Devis précis en ligne, réponse sous 2h.</p>
            <Link href="/devis" className="btn-gold">Demander mon devis <ArrowRight size={16} /></Link>
          </div>
        </div>
      </section>
    </>
  );
}
