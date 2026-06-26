import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, Car } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Detailing voiture de luxe : les étapes clés",
  description: "Guide complet du detailing automobile pour voitures de luxe. Polissage, traitement cuir, céramique — les étapes que réalise MathClean pour vos véhicules.",
  path: "/blog/entretien-voiture-luxe",
});

export default function ArticleVoiturePage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-slate-900 to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6">
          <div className="flex items-center gap-2 text-white/40 text-sm mb-6">
            <Link href="/blog" className="hover:text-gold transition-colors">Blog</Link>
            <span>/</span>
            <span className="text-white/70">Automobile</span>
          </div>
          <span className="label-chip mb-6 inline-flex"><Car size={12} /> Automobile</span>
          <h1 className="font-display text-4xl md:text-5xl font-bold text-white mb-5">
            Detailing voiture de luxe :<br />
            <span className="text-gold-gradient">les étapes clés</span>
          </h1>
          <p className="text-white/60">22 octobre 2024 · 7 min de lecture</p>
        </div>
      </section>
      <section className="py-16 bg-pearl-warm">
        <div className="max-w-3xl mx-auto px-6">
          <div className="bg-white border border-pearl-cream rounded-xl p-8 shadow-sm space-y-6 text-navy">
            <h2 className="font-display text-2xl font-bold">Étape 1 : La décontamination</h2>
            <p className="text-muted-foreground leading-relaxed">Avant tout polissage, il est indispensable de décontaminer la carrosserie. Particules ferreuses, goudron, résines — ces contaminants doivent être éliminés avec des produits chimiques adaptés avant tout contact mécanique.</p>
            <h2 className="font-display text-2xl font-bold">Étape 2 : Le polissage</h2>
            <p className="text-muted-foreground leading-relaxed">Le polissage élimine les micro-rayures, les swirls et les traces d&apos;oxydation. Selon l&apos;état de la peinture, nous choisissons l&apos;abrasif adapté — du polissage léger à la correction de peinture complète.</p>
            <h2 className="font-display text-2xl font-bold">Étape 3 : La protection céramique</h2>
            <p className="text-muted-foreground leading-relaxed">La céramique professionnelle offre une protection de 2 à 5 ans selon le produit. Elle rend la carrosserie hydrophobe, résistante aux rayures légères et facilite l&apos;entretien quotidien.</p>
          </div>
          <div className="mt-10 bg-navy rounded-2xl p-8 text-center text-white">
            <h2 className="font-display text-2xl font-bold mb-3">Réservez votre detailing</h2>
            <Link href="/services/nettoyage-voiture" className="btn-gold">Voir nos formules <ArrowRight size={16} /></Link>
          </div>
        </div>
      </section>
    </>
  );
}
