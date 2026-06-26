import type { Metadata } from "next";
import Link from "next/link";
import { Car, CheckCircle2, ArrowRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import { buildMeta } from "@/lib/seo";
import { CAR_TYPES } from "@/lib/constants";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage automobile & detailing professionnel",
  description: "Nettoyage et detailing automobile professionnel par MathClean. Citadine, berline, SUV, 4×4, van. Nettoyage vapeur, polissage, traitement cuir. Devis gratuit.",
  path: "/services/nettoyage-voiture",
});

export default function NettoyageVoiturePage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-slate-900 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <div className="flex items-center gap-2 text-white/40 text-sm mb-6">
            <Link href="/" className="hover:text-gold transition-colors">Accueil</Link>
            <span>/</span>
            <Link href="/services" className="hover:text-gold transition-colors">Services</Link>
            <span>/</span>
            <span className="text-white/70">Nettoyage automobile</span>
          </div>
          <span className="label-chip mb-6 inline-flex"><Car size={12} /> Automobile</span>
          <h1 className="font-display text-5xl font-bold text-white mb-6">
            Detailing automobile<br />
            <span className="text-gold-gradient">tous types de véhicules</span>
          </h1>
          <p className="text-white/70 text-lg max-w-2xl leading-relaxed mb-8">
            De la citadine au 4×4 de luxe, nous proposons un nettoyage complet bien au-delà du simple lavage. Nettoyage vapeur, aspiration profonde, traitement des plastiques, polissage de la carrosserie.
          </p>
          <Link href="/devis" className="btn-gold">Devis gratuit <ArrowRight size={16} /></Link>
        </div>
      </section>

      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6">
          <h2 className="font-display text-3xl font-bold text-navy text-center mb-10">Par type de véhicule</h2>
          <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-4">
            {CAR_TYPES.map((c) => (
              <Link key={c.slug} href={`/services/nettoyage-voiture/${c.slug}`}
                className="service-card p-6 flex flex-col gap-3 bg-white">
                <h3 className="font-display text-lg font-semibold text-navy">{c.label}</h3>
                <p className="text-gold text-sm font-medium">{c.price}</p>
                <span className="text-xs text-gold flex items-center gap-1 group-hover:gap-2 transition-all font-semibold">
                  Voir la formule <ArrowRight size={12} />
                </span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      <section className="section bg-pearl">
        <div className="max-w-5xl mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="font-display text-3xl font-bold text-navy mb-5">La différence du vrai detailing</h2>
            <ul className="space-y-3">
              {[
                "Aspiration complète intérieur (sièges, tapis, coffre)",
                "Nettoyage vapeur tableaux de bord et plastiques",
                "Traitement et conditionnement cuir",
                "Polissage carrosserie et vitrages",
                "Lustrage et protection céramique optionnelle",
                "Désodorisation par ozone",
              ].map((item) => (
                <li key={item} className="flex items-start gap-3 text-sm text-navy">
                  <CheckCircle2 size={15} className="text-gold shrink-0 mt-0.5" />{item}
                </li>
              ))}
            </ul>
            <Link href="/devis" className="mt-8 btn-navy inline-flex">Demander un devis <ArrowRight size={16} /></Link>
          </div>
          <BeforeAfterSlider
            beforeLabel="Avant"
            afterLabel="Après"
            beforeBg="from-gray-600 to-gray-900"
            afterBg="from-slate-100 to-white"
            aspectRatio="aspect-[4/3]"
          />
        </div>
      </section>
    </>
  );
}
