import type { Metadata } from "next";
import Link from "next/link";
import { Car, ArrowRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Réalisations nettoyage automobile — Avant/après",
  description: "Galerie avant/après de nos prestations de detailing automobile. Berlines, SUV, 4×4 et vans nettoyés par MathClean sur la Côte d'Azur.",
  path: "/realisations/voitures",
});

const CASES = [
  { model: "BMW M5 · Cannes", beforeBg: "from-gray-700 to-gray-900", afterBg: "from-slate-100 to-white", desc: "Detailing complet berline sportive" },
  { model: "Range Rover · Monaco", beforeBg: "from-slate-700 to-slate-900", afterBg: "from-stone-100 to-white", desc: "SUV premium — remise en état" },
  { model: "Porsche 911 · Antibes", beforeBg: "from-zinc-700 to-zinc-900", afterBg: "from-white to-slate-50", desc: "Polissage et protection céramique" },
  { model: "Mercedes Vito · Nice", beforeBg: "from-neutral-700 to-neutral-900", afterBg: "from-gray-50 to-white", desc: "Van utilitaire — désinfection complète" },
];

export default function RealisationsVoituresPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-slate-900 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <span className="label-chip mb-6 inline-flex"><Car size={12} /> Automobile</span>
          <h1 className="font-display text-5xl font-bold text-white mb-5">Réalisations automobile<br /><span className="text-gold-gradient">avant / après</span></h1>
          <p className="text-white/60 text-lg max-w-2xl">150+ véhicules traités. Des berlines aux SUV de luxe, retrouvez nos interventions les plus marquantes.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-6xl mx-auto px-6 grid md:grid-cols-2 gap-8">
          {CASES.map((c) => (
            <div key={c.model}>
              <BeforeAfterSlider beforeLabel="Avant" afterLabel="Après" beforeBg={c.beforeBg} afterBg={c.afterBg} aspectRatio="aspect-video" />
              <div className="mt-3"><p className="text-xs font-semibold text-gold">{c.model}</p><p className="text-sm text-navy mt-0.5">{c.desc}</p></div>
            </div>
          ))}
        </div>
      </section>
      <section className="py-14 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Votre véhicule mérite ce traitement</h2>
          <Link href="/devis" className="btn-navy">Réserver mon detailing <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
