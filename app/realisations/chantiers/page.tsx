import type { Metadata } from "next";
import Link from "next/link";
import { HardHat, ArrowRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Réalisations nettoyage fin de chantier — Avant/après",
  description: "Photos avant/après de nos nettoyages fin de chantier. Villas, appartements, locaux commerciaux sur la Côte d'Azur. MathClean, résultats garantis.",
  path: "/realisations/chantiers",
});

const CASES = [
  { lieu: "Villa · Mougins", beforeBg: "from-amber-800 to-amber-950", afterBg: "from-stone-100 to-white", desc: "Villa 400m² — remise en état post-rénovation" },
  { lieu: "Appartement · Nice Centre", beforeBg: "from-yellow-800 to-yellow-950", afterBg: "from-amber-50 to-white", desc: "Appartement 120m² — construction neuve" },
  { lieu: "Local commercial · Cannes", beforeBg: "from-orange-800 to-orange-950", afterBg: "from-orange-50 to-white", desc: "Commerce 200m² — nettoyage livraison" },
  { lieu: "Résidence · Antibes", beforeBg: "from-amber-900 to-amber-950", afterBg: "from-yellow-50 to-white", desc: "5 appartements neufs — programme immobilier" },
];

export default function RealisationsChantierPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-amber-950 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <span className="label-chip mb-6 inline-flex"><HardHat size={12} /> Chantier</span>
          <h1 className="font-display text-5xl font-bold text-white mb-5">Réalisations fin de chantier<br /><span className="text-gold-gradient">avant / après</span></h1>
          <p className="text-white/60 text-lg max-w-2xl">80+ chantiers remis en état. Villas, appartements, commerces — la preuve en images.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-6xl mx-auto px-6 grid md:grid-cols-2 gap-8">
          {CASES.map((c) => (
            <div key={c.lieu}>
              <BeforeAfterSlider beforeLabel="Avant" afterLabel="Après" beforeBg={c.beforeBg} afterBg={c.afterBg} aspectRatio="aspect-video" />
              <div className="mt-3"><p className="text-xs font-semibold text-gold">{c.lieu}</p><p className="text-sm text-navy mt-0.5">{c.desc}</p></div>
            </div>
          ))}
        </div>
      </section>
      <section className="py-14 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Chantier terminé ? On s&apos;occupe du reste.</h2>
          <Link href="/devis" className="btn-navy">Demander mon devis <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
