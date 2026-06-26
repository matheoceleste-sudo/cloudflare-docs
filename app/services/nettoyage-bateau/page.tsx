import type { Metadata } from "next";
import Link from "next/link";
import { Anchor, CheckCircle2, ArrowRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage de bateaux, yachts & voiliers — Côte d'Azur",
  description: "Nettoyage professionnel de bateaux sur la Côte d'Azur. MathClean intervient sur voiliers, yachts, bateaux à moteur : carène, pont, cockpit, intérieur. Résultats garantis.",
  path: "/services/nettoyage-bateau",
});

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "Service",
  name: "Nettoyage de bateaux et yachts",
  provider: { "@type": "LocalBusiness", name: "MathClean" },
  areaServed: "Côte d'Azur, PACA",
  description: "Service expert de nettoyage nautique : voiliers, yachts, bateaux à moteur.",
};

const PRESTATIONS = [
  { titre: "Nettoyage extérieur", items: ["Carène et coque", "Pont et plat-bord", "Cockpit", "Winches et manilles", "Bimini et capote"] },
  { titre: "Nettoyage intérieur", items: ["Carré et cabines", "Cuisine de bord (cuisine)", "Sanitaires", "Couchettes", "Rangements"] },
  { titre: "Traitements spéciaux", items: ["Anti-algues longue durée", "Polissage gelcoat", "Cire de protection UV", "Anti-oxydation inox", "Traitement teck"] },
];

export default function NettoyageBateauPage() {
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />

      {/* Hero */}
      <section className="relative pt-36 pb-20 bg-navy overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-950 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <div className="flex items-center gap-2 text-white/40 text-sm mb-6">
            <Link href="/" className="hover:text-gold transition-colors">Accueil</Link>
            <span>/</span>
            <Link href="/services" className="hover:text-gold transition-colors">Services</Link>
            <span>/</span>
            <span className="text-white/70">Nettoyage de bateaux</span>
          </div>
          <span className="label-chip mb-6 inline-flex"><Anchor size={12} /> Nautisme</span>
          <h1 className="font-display text-5xl md:text-6xl font-bold text-white mb-6">
            Nettoyage de bateaux<br />
            <span className="text-gold-gradient">& yachts professionnels</span>
          </h1>
          <p className="text-white/70 text-lg max-w-2xl leading-relaxed mb-8">
            Spécialiste reconnu sur la Côte d&apos;Azur, MathClean prend en charge tous types d&apos;embarcations : voiliers, yachts, bateaux à moteur, semi-rigides. Un résultat digne des plus grands ports de plaisance.
          </p>
          <div className="flex gap-4">
            <Link href="/devis" className="btn-gold">Devis gratuit <ArrowRight size={16} /></Link>
            <Link href="/realisations/bateaux" className="btn-outline-white">Voir les réalisations</Link>
          </div>
        </div>
      </section>

      {/* Avant/Après */}
      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6">
          <div className="text-center mb-10">
            <h2 className="font-display text-3xl font-bold text-navy">Résultats avant / après</h2>
            <p className="text-muted-foreground mt-2">Glissez pour comparer — interventions réelles</p>
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <BeforeAfterSlider beforeLabel="Coque avant" afterLabel="Coque après" beforeBg="from-green-900 to-green-950" afterBg="from-white to-blue-50" aspectRatio="aspect-video" />
              <p className="text-center text-xs text-muted-foreground mt-2">Nettoyage carène & polissage coque</p>
            </div>
            <div>
              <BeforeAfterSlider beforeLabel="Intérieur avant" afterLabel="Intérieur après" beforeBg="from-gray-700 to-gray-900" afterBg="from-slate-50 to-white" aspectRatio="aspect-video" />
              <p className="text-center text-xs text-muted-foreground mt-2">Remise en état intérieur</p>
            </div>
          </div>
        </div>
      </section>

      {/* Prestations */}
      <section className="section bg-pearl">
        <div className="max-w-5xl mx-auto px-6">
          <h2 className="font-display text-3xl font-bold text-navy text-center mb-12">Nos prestations nautiques</h2>
          <div className="grid md:grid-cols-3 gap-6">
            {PRESTATIONS.map((p) => (
              <div key={p.titre} className="bg-white border border-pearl-cream rounded-xl p-6 shadow-sm">
                <h3 className="font-display text-lg font-semibold text-navy mb-4">{p.titre}</h3>
                <ul className="space-y-2">
                  {p.items.map((item) => (
                    <li key={item} className="flex items-center gap-2.5 text-sm text-muted-foreground">
                      <CheckCircle2 size={14} className="text-gold shrink-0" />
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pourquoi nous */}
      <section className="section bg-navy">
        <div className="max-w-5xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-white mb-4">Pourquoi choisir MathClean ?</h2>
          <p className="text-white/60 max-w-xl mx-auto mb-12">Nous côtoyons une clientèle exigeante et nous nous engageons sur des standards de qualité qui n&apos;ont rien à envier aux professionnels du grand large.</p>
          <div className="grid sm:grid-cols-2 md:grid-cols-4 gap-6">
            {[
              { n: "8+", l: "Ans d'expérience" },
              { n: "200+", l: "Bateaux nettoyés" },
              { n: "48h", l: "Délai d'intervention" },
              { n: "5★", l: "Note moyenne" },
            ].map((s) => (
              <div key={s.l} className="bg-white/5 border border-white/10 rounded-xl p-6">
                <p className="font-display text-4xl font-bold text-gold mb-2">{s.n}</p>
                <p className="text-white/60 text-sm">{s.l}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Votre bateau mérite le meilleur</h2>
          <p className="text-navy/70 mb-8">Devis gratuit en ligne — réponse sous 2 heures.</p>
          <Link href="/devis" className="btn-navy">Demander mon devis gratuit <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
