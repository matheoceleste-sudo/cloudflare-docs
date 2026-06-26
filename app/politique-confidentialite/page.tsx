import type { Metadata } from "next";
import { buildMeta } from "@/lib/seo";
import { SITE } from "@/lib/constants";

export const metadata: Metadata = buildMeta({
  title: "Politique de confidentialité",
  description: "Politique de confidentialité de MathClean. Comment nous collectons, utilisons et protégeons vos données personnelles.",
  path: "/politique-confidentialite",
});

export default function PolitiqueConfidentialitePage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6">
          <h1 className="font-display text-5xl font-bold text-white">Politique de confidentialité</h1>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-3xl mx-auto px-6 space-y-8">
          {[
            { titre: "Données collectées", contenu: "Nous collectons uniquement les données que vous nous transmettez volontairement via nos formulaires de contact ou de devis : nom, prénom, email, téléphone et description de votre besoin." },
            { titre: "Utilisation des données", contenu: "Vos données sont utilisées exclusivement pour vous répondre et établir votre devis. Elles ne sont ni vendues, ni transmises à des tiers." },
            { titre: "Conservation", contenu: "Vos données sont conservées pendant 3 ans à compter du dernier contact, conformément à la réglementation française." },
            { titre: "Vos droits (RGPD)", contenu: `Conformément au RGPD, vous disposez d'un droit d'accès, de rectification et de suppression de vos données. Pour exercer ces droits, contactez-nous à : ${SITE.email}` },
            { titre: "Cookies", contenu: "Ce site utilise des cookies techniques nécessaires au bon fonctionnement. Aucun cookie publicitaire ou de tracking n'est utilisé sans votre consentement explicite." },
          ].map((s) => (
            <div key={s.titre} className="bg-white border border-pearl-cream rounded-xl p-6 shadow-sm">
              <h2 className="font-display text-xl font-semibold text-navy mb-3">{s.titre}</h2>
              <p className="text-sm text-muted-foreground leading-relaxed">{s.contenu}</p>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}
