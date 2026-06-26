import type { Metadata } from "next";
import Link from "next/link";
import { Warehouse, CheckCircle2, ArrowRight } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage de locaux professionnels",
  description: "Nettoyage de locaux professionnels sur la Côte d'Azur. MathClean intervient dans les commerces, cabinets, hôtels, restaurants, entrepôts. Prestation sur mesure.",
  path: "/services/nettoyage-locaux",
});

export default function NettoyageLocauxPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-indigo-950 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <span className="label-chip mb-6 inline-flex"><Warehouse size={12} /> Locaux</span>
          <h1 className="font-display text-5xl font-bold text-white mb-6">
            Locaux professionnels<br />
            <span className="text-gold-gradient">toujours impeccables</span>
          </h1>
          <p className="text-white/70 text-lg max-w-2xl mb-8">
            Commerce, cabinet médical, hôtel, restaurant, entrepôt ou espace événementiel — nous adaptons notre intervention à chaque type de local et à vos contraintes.
          </p>
          <Link href="/devis" className="btn-gold">Devis gratuit <ArrowRight size={16} /></Link>
        </div>
      </section>

      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6">
          <h2 className="font-display text-3xl font-bold text-navy text-center mb-10">Types de locaux</h2>
          <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-4">
            {["Commerce & boutique", "Cabinet médical / dentaire", "Restaurant & cuisine", "Hôtel & résidence", "Entrepôt & logistique", "Espace événementiel", "Salle de sport / spa", "Établissement scolaire", "Résidence de standing"].map((local) => (
              <div key={local} className="bg-white border border-pearl-cream rounded-xl p-5 flex items-center gap-3 shadow-sm hover:shadow-md transition-shadow">
                <CheckCircle2 size={16} className="text-gold shrink-0" />
                <span className="text-sm font-medium text-navy">{local}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-14 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Vos locaux, notre expertise</h2>
          <Link href="/devis" className="btn-navy">Demander un devis personnalisé <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
