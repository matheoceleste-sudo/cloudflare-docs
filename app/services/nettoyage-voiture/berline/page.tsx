import type { Metadata } from "next";
import Link from "next/link";
import { Car, CheckCircle2, ArrowRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage berline — Formule & Tarif",
  description: "Nettoyage professionnel de berline par MathClean. BMW, Mercedes, Audi... Detailing complet à partir de 110 €. Côte d'Azur.",
  path: "/services/nettoyage-voiture/berline",
});

const ITEMS = ["Aspiration complète intérieur et coffre","Nettoyage vapeur tableau de bord","Traitement et conditionnement cuir","Polissage vitres intérieur/extérieur","Lavage carrosserie + décontamination","Protection céramique (option)","Nettoyage jantes et pneus laqués"];

export default function BerlinePage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-slate-900 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <span className="label-chip mb-6 inline-flex"><Car size={12} /> Berline</span>
          <h1 className="font-display text-5xl font-bold text-white mb-4">Nettoyage berline premium<br /><span className="text-gold-gradient">à partir de 110 €</span></h1>
          <p className="text-white/70 text-lg max-w-2xl mb-8">BMW, Mercedes, Audi, Volvo... Vos berlines méritent un traitement à leur hauteur.</p>
          <Link href="/devis" className="btn-gold">Réserver <ArrowRight size={16} /></Link>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="font-display text-3xl font-bold text-navy mb-6">Formule berline</h2>
            <ul className="space-y-3 mb-8">{ITEMS.map((i) => (<li key={i} className="flex items-center gap-3 text-sm text-navy"><CheckCircle2 size={15} className="text-gold shrink-0" />{i}</li>))}</ul>
            <div className="bg-gold/10 border border-gold/30 rounded-xl p-5 mb-6">
              <p className="text-lg font-bold text-navy">Formule complète</p>
              <p className="text-3xl font-display font-bold text-gold mt-1">À partir de 110 €</p>
              <p className="text-xs text-muted-foreground mt-1">Durée : 3 à 4 heures</p>
            </div>
            <Link href="/devis" className="btn-navy w-full justify-center">Réserver maintenant</Link>
          </div>
          <BeforeAfterSlider beforeBg="from-gray-700 to-gray-900" afterBg="from-slate-100 to-white" aspectRatio="aspect-[4/3]" />
        </div>
      </section>
    </>
  );
}
