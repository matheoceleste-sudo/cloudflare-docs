import type { Metadata } from "next";
import Link from "next/link";
import { Anchor, Car, HardHat, Building2, Warehouse, Star, CheckCircle2, ArrowRight, Phone, ChevronRight } from "lucide-react";
import BeforeAfterSlider from "@/components/BeforeAfterSlider";
import AnimatedCounter from "@/components/AnimatedCounter";
import { STATS, TESTIMONIALS, SERVICES } from "@/lib/constants";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage professionnel bateaux, voitures & locaux",
  description: "MathClean — Expert en nettoyage professionnel sur la Côte d'Azur. Bateaux, yachts, automobiles, fin de chantier et locaux professionnels. Devis gratuit, intervention rapide.",
  path: "/",
});

const ICON_MAP: Record<string, React.ElementType> = {
  Anchor, Car, HardHat, Building2, Warehouse,
};

const serviceColors = [
  "from-blue-900 to-blue-950",
  "from-slate-800 to-slate-900",
  "from-amber-900 to-amber-950",
  "from-teal-900 to-teal-950",
  "from-indigo-900 to-indigo-950",
];

export default function HomePage() {
  return (
    <>
      {/* ──────────────────────────── HERO ──────────────────────────── */}
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-navy">
        {/* Background gradient (swap for real photo with object-cover img) */}
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark via-navy to-blue-950" />
        <div
          className="absolute inset-0 opacity-20"
          style={{ backgroundImage: "radial-gradient(circle at 30% 60%, rgba(184,149,42,0.3) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(22,36,68,0.8) 0%, transparent 40%)" }}
        />
        {/* Gold decorative lines */}
        <div className="absolute top-1/3 left-0 w-32 h-px bg-gradient-to-r from-transparent to-gold/40" />
        <div className="absolute top-1/3 right-0 w-32 h-px bg-gradient-to-l from-transparent to-gold/40" />

        <div className="relative z-10 max-w-5xl mx-auto px-6 text-center pt-32 pb-20">
          <span className="label-chip mb-8 inline-flex">
            <Anchor size={12} />
            Spécialiste nautique · Côte d&apos;Azur
          </span>

          <h1 className="font-display text-5xl md:text-7xl font-bold text-white leading-tight mb-6">
            L&apos;excellence du<br />
            <span className="text-gold-gradient">nettoyage professionnel</span>
          </h1>

          <p className="text-white/70 text-lg md:text-xl max-w-2xl mx-auto mb-10 leading-relaxed">
            De votre bateau à votre véhicule, en passant par vos locaux professionnels —
            MathClean transforme chaque surface en chef-d&apos;œuvre de propreté.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16">
            <Link href="/devis" className="btn-gold">
              Demander un devis gratuit
              <ArrowRight size={16} />
            </Link>
            <Link href="/realisations" className="btn-outline-white">
              Voir nos réalisations
            </Link>
          </div>

          {/* Trust badges */}
          <div className="flex flex-wrap items-center justify-center gap-6 text-white/50 text-xs">
            {["8+ ans d'expérience", "500+ clients satisfaits", "Intervention sous 48h", "Devis gratuit"].map((t) => (
              <span key={t} className="flex items-center gap-2">
                <CheckCircle2 size={13} className="text-gold" />
                {t}
              </span>
            ))}
          </div>
        </div>

        {/* Scroll indicator */}
        <div className="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 text-white/30 text-xs animate-bounce">
          <span>Découvrir</span>
          <ChevronRight size={14} className="rotate-90" />
        </div>
      </section>

      {/* ──────────────────────────── SERVICES ──────────────────────────── */}
      <section className="section bg-pearl-warm">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center mb-14">
            <span className="label-chip">Nos prestations</span>
            <h2 className="font-display text-4xl md:text-5xl font-bold text-navy mt-5 mb-4">
              Tous vos besoins,<br />un seul expert
            </h2>
            <p className="text-muted-foreground max-w-xl mx-auto">
              De la plaisance au professionnel, nous prenons en charge chaque type de surface avec le même souci du détail.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {SERVICES.map((service, i) => {
              const Icon = ICON_MAP[service.icon] ?? Anchor;
              return (
                <Link key={service.slug} href={service.href} className="service-card">
                  <div className={`h-40 bg-gradient-to-br ${serviceColors[i]} flex items-center justify-center`}>
                    <Icon size={40} className="text-white/30 group-hover:text-gold/60 transition-colors" strokeWidth={1.5} />
                  </div>
                  <div className="p-6">
                    <h3 className="font-display text-lg font-semibold text-navy mb-2">{service.label}</h3>
                    <p className="text-sm text-muted-foreground leading-relaxed mb-4">{service.description}</p>
                    <span className="text-xs font-semibold text-gold flex items-center gap-1 group-hover:gap-2 transition-all">
                      Découvrir <ArrowRight size={13} />
                    </span>
                  </div>
                  {service.featured && (
                    <span className="absolute top-3 right-3 bg-gold/90 text-navy text-xs font-bold px-2.5 py-1 rounded">
                      Phare
                    </span>
                  )}
                </Link>
              );
            })}

            {/* CTA card */}
            <Link href="/devis" className="service-card bg-navy border-navy hover:shadow-[0_8px_40px_rgba(13,27,53,0.3)]">
              <div className="h-40 bg-gradient-to-br from-gold/20 to-gold/5 flex items-center justify-center">
                <span className="text-gold text-5xl font-display font-bold">?</span>
              </div>
              <div className="p-6">
                <h3 className="font-display text-lg font-semibold text-white mb-2">Besoin d&apos;un devis ?</h3>
                <p className="text-sm text-white/50 leading-relaxed mb-4">Décrivez votre besoin, nous vous répondons sous 2h.</p>
                <span className="text-xs font-semibold text-gold flex items-center gap-1 group-hover:gap-2 transition-all">
                  Devis gratuit <ArrowRight size={13} />
                </span>
              </div>
            </Link>
          </div>
        </div>
      </section>

      {/* ──────────────────────────── STATS ──────────────────────────── */}
      <section className="py-20 bg-navy">
        <div className="max-w-5xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          {STATS.map((s) => (
            <div key={s.label}>
              <p className="font-display text-4xl md:text-5xl font-bold text-white mb-2">
                <AnimatedCounter value={s.value} suffix={s.suffix} />
              </p>
              <p className="text-white/50 text-sm">{s.label}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ──────────────────────────── AVANT/APRÈS BATEAU ──────────────────────────── */}
      <section className="section bg-pearl">
        <div className="max-w-6xl mx-auto px-6">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <span className="label-chip mb-5 inline-flex">
                <Anchor size={12} />
                Spécialité bateaux
              </span>
              <h2 className="font-display text-4xl md:text-5xl font-bold text-navy mb-5">
                Vos bateaux méritent<br />
                <span className="text-gold-gradient">le meilleur traitement</span>
              </h2>
              <p className="text-muted-foreground leading-relaxed mb-6">
                Du voilier au yacht de luxe, nous redonnons vie à chaque embarcation. Carène, pont, cockpit, intérieur : chaque centimètre est traité avec des produits professionnels spécifiques au nautisme.
              </p>
              <ul className="space-y-3 mb-8">
                {[
                  "Nettoyage complet extérieur / intérieur",
                  "Traitement anti-algues et anti-osmose",
                  "Polissage coque et gelcoat",
                  "Entretien régulier ou ponctuel",
                  "Préparation hivernage / désarmement",
                ].map((item) => (
                  <li key={item} className="flex items-center gap-3 text-sm text-navy">
                    <CheckCircle2 size={16} className="text-gold shrink-0" />
                    {item}
                  </li>
                ))}
              </ul>
              <Link href="/services/nettoyage-bateau" className="btn-navy">
                En savoir plus
                <ArrowRight size={16} />
              </Link>
            </div>
            <div>
              <BeforeAfterSlider
                beforeLabel="Avant nettoyage"
                afterLabel="Après MathClean"
                beforeBg="from-slate-600 via-slate-700 to-slate-800"
                afterBg="from-sky-100 via-blue-50 to-white"
                aspectRatio="aspect-[4/3]"
              />
              <p className="text-center text-xs text-muted-foreground mt-3">
                Glissez le curseur pour comparer — résultat réel MathClean
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ──────────────────────────── AVANT/APRÈS VOITURE ──────────────────────────── */}
      <section className="section bg-navy-dark">
        <div className="max-w-6xl mx-auto px-6">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className="order-2 lg:order-1">
              <BeforeAfterSlider
                beforeLabel="Avant"
                afterLabel="Après"
                beforeBg="from-gray-700 via-gray-800 to-gray-900"
                afterBg="from-slate-100 via-white to-slate-50"
                aspectRatio="aspect-[4/3]"
              />
            </div>
            <div className="order-1 lg:order-2">
              <span className="label-chip mb-5 inline-flex">
                <Car size={12} />
                Detailing automobile
              </span>
              <h2 className="font-display text-4xl font-bold text-white mb-5">
                Citadine, berline, SUV,<br />
                <span className="text-gold-gradient">4×4 ou van</span>
              </h2>
              <p className="text-white/60 leading-relaxed mb-6">
                Un véhicule immaculé reflète votre image. Notre service de detailing complet va bien au-delà du lavage : nettoyage vapeur, aspiration profonde, traitement cuir, polissage.
              </p>
              <div className="grid grid-cols-2 gap-3 mb-8">
                {["Citadine", "Berline", "SUV", "4×4", "Van"].map((type) => (
                  <Link
                    key={type}
                    href={`/services/nettoyage-voiture/${type.toLowerCase().replace("×", "x")}`}
                    className="px-4 py-2.5 bg-white/5 border border-white/10 rounded text-sm text-white/70 hover:bg-gold/10 hover:border-gold/30 hover:text-gold transition-all text-center"
                  >
                    {type}
                  </Link>
                ))}
              </div>
              <Link href="/services/nettoyage-voiture" className="btn-gold">
                Voir les formules
                <ArrowRight size={16} />
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* ──────────────────────────── TESTIMONIALS ──────────────────────────── */}
      <section className="section bg-pearl-warm">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-14">
            <span className="label-chip">Avis clients</span>
            <h2 className="font-display text-4xl font-bold text-navy mt-5">
              Ce que disent nos clients
            </h2>
          </div>
          <div className="grid md:grid-cols-3 gap-6">
            {TESTIMONIALS.map((t) => (
              <div key={t.name} className="bg-white border border-pearl-cream rounded-xl p-7 shadow-sm hover:shadow-md transition-shadow">
                <div className="flex gap-0.5 mb-4">
                  {Array.from({ length: t.stars }).map((_, i) => (
                    <Star key={i} size={14} className="fill-gold text-gold" />
                  ))}
                </div>
                <p className="text-navy text-sm leading-relaxed mb-5 italic">&ldquo;{t.content}&rdquo;</p>
                <div className="flex items-center gap-3 border-t border-pearl-cream pt-4">
                  <div className="w-9 h-9 rounded-full bg-navy-light flex items-center justify-center text-gold font-display font-bold text-sm">
                    {t.name.charAt(0)}
                  </div>
                  <div>
                    <p className="text-sm font-semibold text-navy">{t.name}</p>
                    <p className="text-xs text-muted-foreground">{t.role}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ──────────────────────────── CTA FINAL ──────────────────────────── */}
      <section className="section bg-navy relative overflow-hidden">
        <div className="absolute inset-0 opacity-10" style={{ backgroundImage: "radial-gradient(circle at 50% 50%, rgba(184,149,42,0.5) 0%, transparent 60%)" }} />
        <div className="relative z-10 max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-4xl md:text-5xl font-bold text-white mb-5">
            Prêt à retrouver l&apos;éclat du neuf ?
          </h2>
          <p className="text-white/60 text-lg mb-10">
            Contactez-nous pour un devis gratuit et sans engagement. Nous intervenons sous 48h sur la Côte d&apos;Azur.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link href="/devis" className="btn-gold">
              Demander mon devis
              <ArrowRight size={16} />
            </Link>
            <a href="tel:+33600000000" className="btn-outline-white">
              <Phone size={16} />
              Appeler maintenant
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
