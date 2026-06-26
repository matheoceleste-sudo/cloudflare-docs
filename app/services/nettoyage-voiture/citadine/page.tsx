import type { Metadata } from "next";
import Link from "next/link";
import { Car, CheckCircle2, ArrowRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage citadine — Formule & Tarif",
  description: "Nettoyage professionnel de citadine par MathClean. Aspiration, nettoyage vapeur, polissage, traitement plastiques. Formule complète à partir de 80 €.",
  path: "/services/nettoyage-voiture/citadine",
});

export default function CitadinePage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-slate-900 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <div className="flex items-center gap-2 text-white/40 text-sm mb-6">
            <Link href="/" className="hover:text-gold transition-colors">Accueil</Link>
            <span>/</span>
            <Link href="/services/nettoyage-voiture" className="hover:text-gold transition-colors">Nettoyage voiture</Link>
            <span>/</span>
            <span className="text-white/70">Citadine</span>
          </div>
          <span className="label-chip mb-6 inline-flex"><Car size={12} /> Citadine</span>
          <h1 className="font-display text-5xl font-bold text-white mb-4">
            Nettoyage citadine<br />
            <span className="text-gold-gradient">à partir de 80 €</span>
          </h1>
          <p className="text-white/70 text-lg max-w-2xl mb-8">Polo, Clio, 208, Twingo... Nos formules s&apos;adaptent à tous les modèles de citadines. Résultat showroom garanti.</p>
          <Link href="/devis" className="btn-gold">Réserver <ArrowRight size={16} /></Link>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="font-display text-3xl font-bold text-navy mb-6">Formule citadine complète</h2>
            <ul className="space-y-3 mb-8">
              {["Aspirateur professionnel intérieur complet", "Nettoyage vapeur tableau de bord", "Traitement plastiques et vinyles", "Nettoyage vitres intérieur/extérieur", "Lavage et séchage carrosserie", "Lustrage et protection cire", "Nettoyage jantes et pneus"].map((i) => (
                <li key={i} className="flex items-center gap-3 text-sm text-navy">
                  <CheckCircle2 size={15} className="text-gold shrink-0" />{i}
                </li>
              ))}
            </ul>
            <div className="bg-gold/10 border border-gold/30 rounded-xl p-5 mb-6">
              <p className="text-lg font-bold text-navy">Formule complète</p>
              <p className="text-3xl font-display font-bold text-gold mt-1">À partir de 80 €</p>
              <p className="text-xs text-muted-foreground mt-1">Durée : 2 à 3 heures · Déplacement inclus (zone)</p>
            </div>
            <Link href="/devis" className="btn-navy w-full justify-center">Réserver maintenant</Link>
          </div>
          <BeforeAfterSlider beforeBg="from-gray-700 to-gray-900" afterBg="from-slate-100 to-white" aspectRatio="aspect-[4/3]" />
        </div>
      </section>
    </>
  );
}
