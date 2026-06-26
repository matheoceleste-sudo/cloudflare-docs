import type { Metadata } from "next";
import Link from "next/link";
import { Anchor, Car, HardHat, Building2, Warehouse, ArrowRight } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Tous nos services de nettoyage professionnel",
  description: "Découvrez toutes les prestations MathClean : nettoyage de bateaux, detailing automobile, fin de chantier, bureaux et locaux professionnels sur la Côte d'Azur.",
  path: "/services",
});

const SERVICES_FULL = [
  { icon: Anchor, label: "Nettoyage de bateaux & yachts", description: "Voiliers, yachts à moteur, semi-rigides. Intérieur/extérieur, polissage carène, traitement teck.", href: "/services/nettoyage-bateau", color: "from-blue-900 to-blue-950", badge: "Service phare" },
  { icon: Car, label: "Detailing automobile", description: "Citadine, berline, SUV, 4×4, van. Nettoyage vapeur, traitement cuir, polissage, protection.", href: "/services/nettoyage-voiture", color: "from-slate-800 to-slate-900", badge: null },
  { icon: HardHat, label: "Nettoyage fin de chantier", description: "Remise en état après travaux. Poussières, résidus, vitres, sols. Prêt à livrer.", href: "/services/nettoyage-fin-chantier", color: "from-amber-900 to-amber-950", badge: null },
  { icon: Building2, label: "Nettoyage de bureaux", description: "Entretien quotidien ou ponctuel. Espaces de travail, salles de réunion, sanitaires.", href: "/services/nettoyage-bureau", color: "from-teal-900 to-teal-950", badge: null },
  { icon: Warehouse, label: "Locaux professionnels", description: "Commerces, cabinets médicaux, entrepôts, hôtels, restaurants. Sur mesure.", href: "/services/nettoyage-locaux", color: "from-indigo-900 to-indigo-950", badge: null },
];

export default function ServicesPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <h1 className="font-display text-5xl font-bold text-white mb-5">Nos services</h1>
          <p className="text-white/60 text-lg max-w-2xl mx-auto">
            Une offre complète pour particuliers et professionnels exigeants. Chaque intervention est réalisée avec des produits professionnels et une attention portée aux moindres détails.
          </p>
        </div>
      </section>

      <section className="section bg-pearl-warm">
        <div className="max-w-6xl mx-auto px-6 grid md:grid-cols-2 gap-6">
          {SERVICES_FULL.map((s) => {
            const Icon = s.icon;
            return (
              <Link key={s.href} href={s.href} className="service-card group flex gap-0">
                <div className={`w-1/3 bg-gradient-to-br ${s.color} flex items-center justify-center min-h-[180px]`}>
                  <Icon size={36} className="text-white/30 group-hover:text-gold/50 transition-colors" strokeWidth={1.5} />
                </div>
                <div className="p-6 flex-1">
                  {s.badge && <span className="text-xs bg-gold/10 text-gold-dark px-2 py-0.5 rounded font-medium mb-2 inline-block">{s.badge}</span>}
                  <h2 className="font-display text-lg font-semibold text-navy mb-2">{s.label}</h2>
                  <p className="text-sm text-muted-foreground mb-4 leading-relaxed">{s.description}</p>
                  <span className="text-xs text-gold font-semibold flex items-center gap-1 group-hover:gap-2 transition-all">
                    En savoir plus <ArrowRight size={12} />
                  </span>
                </div>
              </Link>
            );
          })}
          <Link href="/devis" className="service-card bg-navy border-navy p-8 flex flex-col items-center justify-center text-center min-h-[180px]">
            <p className="font-display text-5xl font-bold text-gold mb-3">?</p>
            <p className="font-semibold text-white mb-2">Besoin d&apos;un devis ?</p>
            <p className="text-white/50 text-sm mb-4">Décrivez votre besoin, réponse sous 2h.</p>
            <span className="btn-gold text-xs px-5 py-2">Devis gratuit</span>
          </Link>
        </div>
      </section>
    </>
  );
}
