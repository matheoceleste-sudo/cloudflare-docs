import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, Anchor } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Comment entretenir son bateau entre deux nettoyages",
  description: "Conseils experts pour maintenir votre bateau propre entre les interventions professionnelles. Carène, pont, inox, teck — les bons gestes au quotidien.",
  path: "/blog/nettoyage-bateau-professionnel",
});

export default function ArticleBateauPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-950 to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6">
          <div className="flex items-center gap-2 text-white/40 text-sm mb-6">
            <Link href="/blog" className="hover:text-gold transition-colors">Blog</Link>
            <span>/</span>
            <span className="text-white/70">Nettoyage bateau</span>
          </div>
          <span className="label-chip mb-6 inline-flex"><Anchor size={12} /> Nautisme</span>
          <h1 className="font-display text-4xl md:text-5xl font-bold text-white mb-5">
            Comment entretenir son bateau<br />
            <span className="text-gold-gradient">entre deux nettoyages professionnels</span>
          </h1>
          <p className="text-white/60">10 novembre 2024 · 6 min de lecture</p>
        </div>
      </section>
      <section className="py-16 bg-pearl-warm">
        <div className="max-w-3xl mx-auto px-6">
          <article className="prose prose-lg max-w-none">
            <div className="bg-white border border-pearl-cream rounded-xl p-8 shadow-sm space-y-6 text-navy">
              <h2 className="font-display text-2xl font-bold">Le rinçage après chaque sortie : le geste essentiel</h2>
              <p className="text-muted-foreground leading-relaxed">L&apos;eau de mer contient du sel, des algues microscopiques et des minéraux qui s&apos;accumulent sur toutes les surfaces. Rincer à l&apos;eau douce après chaque sortie est le geste numéro un pour éviter une dégradation prématurée de votre bateau.</p>
              <h2 className="font-display text-2xl font-bold">Les surfaces à surveiller en priorité</h2>
              <p className="text-muted-foreground leading-relaxed">Les pièces inox sont les plus sensibles à la corrosion. Nettoyez-les régulièrement avec un produit spécifique inox. Le teck doit être brossé dans le sens des fibres et protégé avec une huile adaptée. La coque, enfin, doit être inspectée régulièrement pour détecter tout début d&apos;osmose.</p>
              <h2 className="font-display text-2xl font-bold">Quand faire appel à MathClean ?</h2>
              <p className="text-muted-foreground leading-relaxed">Une intervention professionnelle est recommandée toutes les 6 à 8 semaines en saison active, et avant l&apos;hivernage. Nous traitons les zones inaccessibles, effectuons le polissage de la gelcoat et appliquons des produits de protection longue durée.</p>
            </div>
          </article>
          <div className="mt-10 bg-navy rounded-2xl p-8 text-center text-white">
            <h2 className="font-display text-2xl font-bold mb-3">Planifiez votre prochain nettoyage</h2>
            <Link href="/devis" className="btn-gold">Demander un devis <ArrowRight size={16} /></Link>
          </div>
        </div>
      </section>
    </>
  );
}
