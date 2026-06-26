import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Réalisations & avant/après — Nos interventions",
  description: "Découvrez les réalisations MathClean : avant/après bateaux, voitures, chantiers. Photos et témoignages de nos interventions sur la Côte d'Azur.",
  path: "/realisations",
});

const CATEGORIES = [
  { label: "Bateaux & yachts", href: "/realisations/bateaux", count: "30+ interventions", color: "from-blue-900 to-blue-950" },
  { label: "Automobiles", href: "/realisations/voitures", count: "150+ véhicules", color: "from-slate-800 to-slate-900" },
  { label: "Chantiers", href: "/realisations/chantiers", count: "80+ chantiers", color: "from-amber-900 to-amber-950" },
];

export default function RealisationsPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <h1 className="font-display text-5xl font-bold text-white mb-5">Nos réalisations</h1>
          <p className="text-white/60 text-lg max-w-2xl mx-auto">
            Chaque intervention est une démonstration de notre savoir-faire. Parcourez nos avant/après et jugez par vous-même.
          </p>
        </div>
      </section>

      <section className="section bg-pearl-warm">
        <div className="max-w-6xl mx-auto px-6">
          <div className="grid md:grid-cols-3 gap-6 mb-16">
            {CATEGORIES.map((c) => (
              <Link key={c.href} href={c.href} className="service-card group">
                <div className={`h-40 bg-gradient-to-br ${c.color} flex items-center justify-center`}>
                  <span className="text-white/30 text-5xl font-display font-bold group-hover:text-gold/50 transition-colors">A/A</span>
                </div>
                <div className="p-5">
                  <h2 className="font-display text-lg font-semibold text-navy mb-1">{c.label}</h2>
                  <p className="text-sm text-gold font-medium mb-3">{c.count}</p>
                  <span className="text-xs text-gold font-semibold flex items-center gap-1 group-hover:gap-2 transition-all">
                    Voir les photos <ArrowRight size={12} />
                  </span>
                </div>
              </Link>
            ))}
          </div>

          <h2 className="font-display text-3xl font-bold text-navy text-center mb-10">Sélection avant / après</h2>
          <div className="grid md:grid-cols-2 gap-8">
            <div>
              <BeforeAfterSlider beforeLabel="Bateau avant" afterLabel="Bateau après" beforeBg="from-green-800 to-green-950" afterBg="from-blue-50 to-white" aspectRatio="aspect-video" />
              <p className="text-center text-xs text-muted-foreground mt-2 font-medium">Nettoyage carène · Antibes</p>
            </div>
            <div>
              <BeforeAfterSlider beforeLabel="Voiture avant" afterLabel="Voiture après" beforeBg="from-gray-700 to-gray-900" afterBg="from-slate-100 to-white" aspectRatio="aspect-video" />
              <p className="text-center text-xs text-muted-foreground mt-2 font-medium">Detailing berline · Cannes</p>
            </div>
            <div>
              <BeforeAfterSlider beforeLabel="Chantier avant" afterLabel="Chantier après" beforeBg="from-amber-800 to-amber-950" afterBg="from-stone-100 to-white" aspectRatio="aspect-video" />
              <p className="text-center text-xs text-muted-foreground mt-2 font-medium">Fin de chantier villa · Nice</p>
            </div>
            <div>
              <BeforeAfterSlider beforeLabel="Intérieur avant" afterLabel="Intérieur après" beforeBg="from-slate-700 to-slate-900" afterBg="from-blue-50 to-sky-50" aspectRatio="aspect-video" />
              <p className="text-center text-xs text-muted-foreground mt-2 font-medium">Intérieur voilier · Monaco</p>
            </div>
          </div>
        </div>
      </section>

      <section className="py-14 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Votre réalisation sera la prochaine</h2>
          <Link href="/devis" className="btn-navy">Demander un devis gratuit <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
