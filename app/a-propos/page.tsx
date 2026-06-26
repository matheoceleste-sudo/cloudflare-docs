import type { Metadata } from "next";
import Link from "next/link";
import { CheckCircle2, ArrowRight, Award, Users, Clock, Star } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "À propos — L'histoire de MathClean",
  description: "Découvrez MathClean, expert en nettoyage professionnel sur la Côte d'Azur depuis plus de 8 ans. Notre histoire, nos valeurs, notre engagement qualité.",
  path: "/a-propos",
});

export default function AProposPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <h1 className="font-display text-5xl font-bold text-white mb-5">Notre histoire,<br /><span className="text-gold-gradient">notre passion</span></h1>
          <p className="text-white/60 text-lg max-w-2xl">MathClean est né d&apos;une conviction simple : tout mérite d&apos;être traité avec le plus grand soin. Cette philosophie guide chacune de nos interventions depuis plus de 8 ans.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6 grid lg:grid-cols-2 gap-14 items-center">
          <div>
            <h2 className="font-display text-3xl font-bold text-navy mb-5">Une expertise forgée sur le terrain</h2>
            <p className="text-muted-foreground leading-relaxed mb-5">Fondée sur la Côte d&apos;Azur, MathClean s&apos;est spécialisée dans les environnements exigeants : ports de plaisance, yachts, véhicules de luxe, villas et propriétés haut de gamme. Notre clientèle, composée de professionnels et de particuliers fortunés, attend l&apos;excellence — et nous la livrons.</p>
            <p className="text-muted-foreground leading-relaxed mb-8">Nous utilisons exclusivement des produits professionnels certifiés, respectueux de l&apos;environnement marin. Chaque technicien est formé aux spécificités de chaque surface : gelcoat, teck, cuir, carrosserie, cloisons de chantier.</p>
            <ul className="space-y-3">
              {["Produits professionnels certifiés CE","Équipe formée et assurée","Respect de l'environnement marin","Disponibilité 6j/7","Résultat garanti ou intervention gratuite"].map((v) => (
                <li key={v} className="flex items-center gap-3 text-sm text-navy"><CheckCircle2 size={15} className="text-gold shrink-0" />{v}</li>
              ))}
            </ul>
          </div>
          <div className="grid grid-cols-2 gap-4">
            {[
              { icon: Award, label: "8+ ans d'expérience", sub: "Sur la Côte d'Azur" },
              { icon: Users, label: "500+ clients", sub: "Particuliers & pros" },
              { icon: Clock, label: "1200+ interventions", sub: "Réalisées à ce jour" },
              { icon: Star, label: "5 étoiles", sub: "Note moyenne clients" },
            ].map((s) => (
              <div key={s.label} className="bg-white border border-pearl-cream rounded-xl p-6 text-center shadow-sm">
                <s.icon size={24} className="text-gold mx-auto mb-3" />
                <p className="font-display font-bold text-navy text-sm">{s.label}</p>
                <p className="text-xs text-muted-foreground mt-1">{s.sub}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
      <section className="py-14 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Faites confiance à notre expérience</h2>
          <Link href="/devis" className="btn-navy">Demander un devis <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
