import type { Metadata } from "next";
import { buildMeta } from "@/lib/seo";
import { SITE } from "@/lib/constants";

export const metadata: Metadata = buildMeta({
  title: "Mentions légales",
  description: "Mentions légales de MathClean. Informations sur l'éditeur, l'hébergeur et les conditions d'utilisation du site mathclean.fr.",
  path: "/mentions-legales",
  noIndex: false,
});

export default function MentionsLegalesPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6">
          <h1 className="font-display text-5xl font-bold text-white">Mentions légales</h1>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-3xl mx-auto px-6 space-y-8">
          {[
            { titre: "Éditeur du site", contenu: `${SITE.name} — ${SITE.address.street}, ${SITE.address.zip} ${SITE.address.city}\nTéléphone : ${SITE.phone}\nEmail : ${SITE.email}\nSIRET : [Numéro SIRET à compléter]` },
            { titre: "Hébergement", contenu: "Ce site est hébergé par Vercel Inc., 340 Pine Street Suite 701, San Francisco, CA 94104, États-Unis." },
            { titre: "Propriété intellectuelle", contenu: "L'ensemble des contenus présents sur ce site (textes, images, logos) est la propriété exclusive de MathClean, sauf mention contraire. Toute reproduction est interdite sans autorisation préalable." },
            { titre: "Responsabilité", contenu: "MathClean s'efforce d'assurer l'exactitude des informations diffusées sur ce site. Cependant, nous ne pouvons garantir l'exhaustivité ni l'absence d'erreur." },
          ].map((s) => (
            <div key={s.titre} className="bg-white border border-pearl-cream rounded-xl p-6 shadow-sm">
              <h2 className="font-display text-xl font-semibold text-navy mb-3">{s.titre}</h2>
              <p className="text-sm text-muted-foreground leading-relaxed whitespace-pre-line">{s.contenu}</p>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}
