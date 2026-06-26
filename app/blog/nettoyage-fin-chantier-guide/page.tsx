import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, HardHat } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage fin de chantier : pourquoi confier à un pro ?",
  description: "Les raisons de faire appel à MathClean pour le nettoyage fin de chantier. Sécurité, efficacité, matériel professionnel — tout ce qu'un nettoyage particulier ne peut pas faire.",
  path: "/blog/nettoyage-fin-chantier-guide",
});

export default function ArticleChantierPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-amber-950 to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6">
          <div className="flex items-center gap-2 text-white/40 text-sm mb-6">
            <Link href="/blog" className="hover:text-gold transition-colors">Blog</Link>
            <span>/</span>
            <span className="text-white/70">Chantier</span>
          </div>
          <span className="label-chip mb-6 inline-flex"><HardHat size={12} /> Chantier</span>
          <h1 className="font-display text-4xl md:text-5xl font-bold text-white mb-5">
            Nettoyage fin de chantier :<br />
            <span className="text-gold-gradient">pourquoi confier à un professionnel ?</span>
          </h1>
          <p className="text-white/60">15 septembre 2024 · 5 min de lecture</p>
        </div>
      </section>
      <section className="py-16 bg-pearl-warm">
        <div className="max-w-3xl mx-auto px-6">
          <div className="bg-white border border-pearl-cream rounded-xl p-8 shadow-sm space-y-6 text-navy">
            <h2 className="font-display text-2xl font-bold">La poussière de chantier : un ennemi tenace</h2>
            <p className="text-muted-foreground leading-relaxed">La poussière de plâtre, de ciment ou de béton contient des micro-particules qui s&apos;infiltrent partout : ventilation, joints, vitrages, parquets. Un simple aspirateur domestique est insuffisant — il faut du matériel professionnel avec filtration HEPA.</p>
            <h2 className="font-display text-2xl font-bold">La maîtrise des produits</h2>
            <p className="text-muted-foreground leading-relaxed">Chaque surface nécessite un produit spécifique : dégraissant puissant pour les sols en béton, nettoyant acide pour les résidus de ciment sur le carrelage, produit spécial pour les vitrages tachés de mortier. Utiliser le mauvais produit peut endommager irrémédiablement une surface neuve.</p>
            <h2 className="font-display text-2xl font-bold">Rapidité et fiabilité</h2>
            <p className="text-muted-foreground leading-relaxed">Nos équipes interviennent avec le matériel complet et peuvent nettoyer 100m² en une seule journée. Pour un promoteur immobilier ou un architecte d&apos;intérieur, c&apos;est la garantie de tenir les délais de livraison.</p>
          </div>
          <div className="mt-10 bg-navy rounded-2xl p-8 text-center text-white">
            <h2 className="font-display text-2xl font-bold mb-3">Prêt pour la livraison ?</h2>
            <Link href="/services/nettoyage-fin-chantier" className="btn-gold">Voir notre service <ArrowRight size={16} /></Link>
          </div>
        </div>
      </section>
    </>
  );
}
