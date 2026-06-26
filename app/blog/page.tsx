import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Blog — Conseils nettoyage professionnel",
  description: "Conseils d'experts MathClean : entretien de bateaux, detailing automobile, nettoyage fin de chantier. Guides et astuces pour des surfaces impeccables.",
  path: "/blog",
});

const ARTICLES = [
  { slug: "nettoyage-bateau-professionnel", titre: "Comment entretenir son bateau entre deux nettoyages professionnels", date: "2024-11-10", cat: "Nautisme", resume: "Découvrez les gestes simples pour maintenir votre bateau propre entre nos interventions." },
  { slug: "entretien-voiture-luxe", titre: "Detailing voiture de luxe : les étapes clés", date: "2024-10-22", cat: "Automobile", resume: "Un véhicule de luxe nécessite des soins spécifiques. Voici comment nous procédons." },
  { slug: "nettoyage-fin-chantier-guide", titre: "Nettoyage fin de chantier : pourquoi faire appel à un professionnel ?", date: "2024-09-15", cat: "Chantier", resume: "Les résidus de chantier nécessitent du matériel professionnel. Explications." },
];

export default function BlogPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <h1 className="font-display text-5xl font-bold text-white mb-5">Blog & Conseils</h1>
          <p className="text-white/60 text-lg">Guides, astuces et retours d&apos;expérience de nos experts.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-4xl mx-auto px-6 space-y-6">
          {ARTICLES.map((a) => (
            <Link key={a.slug} href={`/blog/${a.slug}`} className="service-card flex flex-col sm:flex-row overflow-hidden bg-white">
              <div className="sm:w-1/3 bg-navy flex items-center justify-center min-h-[140px]">
                <span className="text-gold/50 text-xs font-semibold uppercase tracking-widest">{a.cat}</span>
              </div>
              <div className="p-6 flex-1">
                <p className="text-xs text-gold font-semibold mb-2">{a.cat} · {new Date(a.date).toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric" })}</p>
                <h2 className="font-display text-lg font-semibold text-navy mb-2">{a.titre}</h2>
                <p className="text-sm text-muted-foreground mb-4">{a.resume}</p>
                <span className="text-xs text-gold font-semibold flex items-center gap-1 group-hover:gap-2 transition-all">Lire l&apos;article <ArrowRight size={12} /></span>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </>
  );
}
