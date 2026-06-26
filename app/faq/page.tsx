import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "FAQ — Questions fréquentes sur nos services",
  description: "Toutes les réponses à vos questions sur les services MathClean. Délais, tarifs, produits, zones d'intervention, nettoyage bateau et automobile.",
  path: "/faq",
});

const FAQS = [
  { q: "Combien de temps prend un nettoyage de bateau ?", r: "Selon la taille et l'état du bateau, une intervention complète dure entre 4h et 2 jours. Pour un voilier de 10m en état correct, comptez une journée." },
  { q: "Intervenez-vous sur les ports de Monaco et Cannes ?", r: "Oui, nous intervenons sur tous les ports de la Côte d'Azur : Antibes, Cannes, Nice, Monaco, Juan-les-Pins, Beaulieu, Saint-Tropez et leurs environs." },
  { q: "Vos produits sont-ils respectueux de l'environnement marin ?", r: "Absolument. Tous nos produits sont certifiés et conformes aux réglementations environnementales portuaires. Nous utilisons des détergents biodégradables et des méthodes de travail respectueuses." },
  { q: "Proposez-vous des contrats d'entretien régulier ?", r: "Oui, nous proposons des contrats d'entretien mensuel, bi-mensuel ou trimestriel pour bateaux, véhicules et locaux. Tarif préférentiel pour les contrats annuels." },
  { q: "Quel est votre délai d'intervention ?", r: "Sous 48 heures pour la plupart des interventions. En urgence, nous faisons notre possible pour intervenir le jour même ou le lendemain." },
  { q: "Le devis est-il vraiment gratuit ?", r: "Oui, totalement. Nous vous envoyons un devis détaillé sans engagement, en ligne ou sur site selon vos préférences." },
  { q: "Puis-je confier mes clés de véhicule ou de bateau ?", r: "Oui, nous sommes habitués à travailler en toute discrétion avec les propriétaires absents. Une procédure de remise de clés sécurisée est prévue." },
  { q: "Nettoyez-vous les camping-cars et mobil-homes ?", r: "Oui, notre formule Van/Utilitaire couvre aussi les camping-cars. Pour les mobil-homes ou chalets, contactez-nous pour un devis personnalisé." },
];

export default function FaqPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <h1 className="font-display text-5xl font-bold text-white mb-5">Questions fréquentes</h1>
          <p className="text-white/60 text-lg">Tout ce que vous devez savoir avant de nous contacter.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-3xl mx-auto px-6 space-y-4">
          {FAQS.map((faq, i) => (
            <div key={i} className="bg-white border border-pearl-cream rounded-xl p-6 shadow-sm">
              <h2 className="font-display text-base font-semibold text-navy mb-3">{faq.q}</h2>
              <p className="text-sm text-muted-foreground leading-relaxed">{faq.r}</p>
            </div>
          ))}
        </div>
        <div className="max-w-3xl mx-auto px-6 mt-10 text-center">
          <p className="text-muted-foreground mb-4">Une question non listée ? Contactez-nous directement.</p>
          <Link href="/contact" className="btn-navy">Nous contacter <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
