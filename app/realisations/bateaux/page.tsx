import type { Metadata } from "next";
import Link from "next/link";
import { Anchor, ArrowRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Réalisations nettoyage bateaux — Photos avant/après",
  description: "Photos avant/après de nos interventions de nettoyage nautique. Voiliers, yachts, bateaux à moteur sur la Côte d'Azur. MathClean, spécialiste reconnu.",
  path: "/realisations/bateaux",
});

const BEFORE_AFTERS = [
  { lieu: "Port Vauban · Antibes",    beforeBg: "from-green-800 to-green-950",   afterBg: "from-blue-50 to-white",   desc: "Voilier 12m — nettoyage carène & polissage" },
  { lieu: "Port Pierre Canto · Cannes", beforeBg: "from-teal-800 to-teal-950",  afterBg: "from-sky-50 to-white",    desc: "Yacht à moteur 16m — remise à neuf complète" },
  { lieu: "Port Hercule · Monaco",    beforeBg: "from-slate-700 to-slate-900",   afterBg: "from-white to-blue-50",   desc: "Intérieur yacht 20m — nettoyage cabines" },
  { lieu: "Port de Nice",             beforeBg: "from-gray-700 to-gray-900",     afterBg: "from-slate-50 to-white",  desc: "Semi-rigide — nettoyage complet" },
  { lieu: "Port Gallice · Juan",      beforeBg: "from-emerald-900 to-emerald-950", afterBg: "from-cyan-50 to-white", desc: "Voilier 9m — désincrustage et cire" },
  { lieu: "Port de Beaulieu",         beforeBg: "from-blue-900 to-blue-950",     afterBg: "from-indigo-50 to-white", desc: "Bateau à moteur — teck et inox" },
];

export default function RealisationsBateauxPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-950 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <div className="flex items-center gap-2 text-white/40 text-sm mb-6">
            <Link href="/" className="hover:text-gold transition-colors">Accueil</Link>
            <span>/</span>
            <Link href="/realisations" className="hover:text-gold transition-colors">Réalisations</Link>
            <span>/</span>
            <span className="text-white/70">Bateaux</span>
          </div>
          <span className="label-chip mb-6 inline-flex"><Anchor size={12} /> Nautisme</span>
          <h1 className="font-display text-5xl font-bold text-white mb-5">
            Réalisations bateaux<br />
            <span className="text-gold-gradient">avant / après</span>
          </h1>
          <p className="text-white/60 text-lg max-w-2xl">30+ interventions réalisées sur les plus beaux ports de la Côte d&apos;Azur. Chaque photo est une intervention réelle MathClean.</p>
        </div>
      </section>

      <section className="section bg-pearl-warm">
        <div className="max-w-6xl mx-auto px-6">
          <div className="grid md:grid-cols-2 gap-8">
            {BEFORE_AFTERS.map((item) => (
              <div key={item.lieu}>
                <BeforeAfterSlider
                  beforeLabel="Avant"
                  afterLabel="Après MathClean"
                  beforeBg={item.beforeBg}
                  afterBg={item.afterBg}
                  aspectRatio="aspect-video"
                />
                <div className="mt-3">
                  <p className="text-xs font-semibold text-gold">{item.lieu}</p>
                  <p className="text-sm text-navy mt-0.5">{item.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-14 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Confiez-nous votre bateau</h2>
          <Link href="/devis" className="btn-navy">Demander un devis <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
