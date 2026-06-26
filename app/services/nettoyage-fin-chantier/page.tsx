import type { Metadata } from "next";
import Link from "next/link";
import { HardHat, CheckCircle2, ArrowRight } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage fin de chantier professionnel",
  description: "Nettoyage fin de chantier par MathClean. Remise en état complète après construction ou rénovation : poussières, résidus ciment, vitres, sols. Côte d'Azur.",
  path: "/services/nettoyage-fin-chantier",
});

export default function FinChantierPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-amber-950 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <div className="flex items-center gap-2 text-white/40 text-sm mb-6">
            <Link href="/" className="hover:text-gold transition-colors">Accueil</Link>
            <span>/</span>
            <Link href="/services" className="hover:text-gold transition-colors">Services</Link>
            <span>/</span>
            <span className="text-white/70">Fin de chantier</span>
          </div>
          <span className="label-chip mb-6 inline-flex"><HardHat size={12} /> Chantier</span>
          <h1 className="font-display text-5xl font-bold text-white mb-6">
            Nettoyage fin de chantier<br />
            <span className="text-gold-gradient">remise en état complète</span>
          </h1>
          <p className="text-white/70 text-lg max-w-2xl leading-relaxed mb-8">
            Après des travaux de construction ou de rénovation, nous prenons en charge la remise en état complète : poussières de plâtre, résidus de ciment, peinture, vitres, sols. Livraison impeccable.
          </p>
          <Link href="/devis" className="btn-gold">Devis gratuit <ArrowRight size={16} /></Link>
        </div>
      </section>

      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6 grid md:grid-cols-2 gap-12">
          <div>
            <h2 className="font-display text-3xl font-bold text-navy mb-6">Ce que nous nettoyons</h2>
            <ul className="space-y-3">
              {["Poussières de plâtre et ciment", "Résidus de colle et joint", "Vitres et menuiseries", "Sols (carrelage, parquet, béton)", "Plafonds et murs", "Sanitaires et cuisine", "Façades extérieures", "Parkings et garages"].map((item) => (
                <li key={item} className="flex items-center gap-3 text-sm text-navy">
                  <CheckCircle2 size={15} className="text-gold shrink-0" />{item}
                </li>
              ))}
            </ul>
          </div>
          <div className="space-y-4">
            <div className="bg-white border border-pearl-cream rounded-xl p-6 shadow-sm">
              <h3 className="font-display text-lg font-semibold text-navy mb-2">Construction neuve</h3>
              <p className="text-sm text-muted-foreground">Premier nettoyage après gros-œuvre, second passage avant livraison. Résultat clé en main.</p>
            </div>
            <div className="bg-white border border-pearl-cream rounded-xl p-6 shadow-sm">
              <h3 className="font-display text-lg font-semibold text-navy mb-2">Rénovation</h3>
              <p className="text-sm text-muted-foreground">Après travaux de rénovation, nous remettons les lieux en état d&apos;habitation ou d&apos;exploitation.</p>
            </div>
            <div className="bg-white border border-pearl-cream rounded-xl p-6 shadow-sm">
              <h3 className="font-display text-lg font-semibold text-navy mb-2">Logement ou local</h3>
              <p className="text-sm text-muted-foreground">Villa, appartement, local commercial, entrepôt ou hôtel — chaque surface est traitée.</p>
            </div>
          </div>
        </div>
      </section>

      <section className="py-14 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Chantier terminé ? Nous prenons le relais.</h2>
          <p className="text-navy/70 mb-8">Devis sur mesure selon la superficie et l&apos;état du chantier.</p>
          <Link href="/devis" className="btn-navy">Demander mon devis <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
