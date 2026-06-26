import type { Metadata } from "next";
import { buildMeta } from "@/lib/seo";
import { SITE } from "@/lib/constants";
import DevisForm from "./DevisForm";

export const metadata: Metadata = buildMeta({
  title: "Demande de devis gratuit",
  description: "Demandez votre devis gratuit en ligne. MathClean vous répond sous 2 heures. Nettoyage bateau, voiture, chantier ou locaux sur la Côte d'Azur.",
  path: "/devis",
});

export default function DevisPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-3xl mx-auto px-6 text-center">
          <h1 className="font-display text-5xl font-bold text-white mb-4">Devis gratuit<br /><span className="text-gold-gradient">réponse sous 2 heures</span></h1>
          <p className="text-white/60 text-lg">Décrivez votre besoin, nous vous envoyons un devis précis et sans engagement.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-2xl mx-auto px-6">
          <DevisForm phone={SITE.phone} email={SITE.email} />
        </div>
      </section>
    </>
  );
}
