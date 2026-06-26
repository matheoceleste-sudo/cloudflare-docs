import type { Metadata } from "next";
import Link from "next/link";
import { Building2, CheckCircle2, ArrowRight } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Nettoyage de bureaux professionnel",
  description: "Nettoyage et entretien de bureaux par MathClean. Espaces de travail, salles de réunion, sanitaires. Intervention discrète en dehors des heures d'ouverture. Côte d'Azur.",
  path: "/services/nettoyage-bureau",
});

export default function NettoyageBureauPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-teal-950 to-navy" />
        <div className="relative z-10 max-w-5xl mx-auto px-6">
          <span className="label-chip mb-6 inline-flex"><Building2 size={12} /> Bureaux</span>
          <h1 className="font-display text-5xl font-bold text-white mb-6">
            Nettoyage de bureaux<br />
            <span className="text-gold-gradient">discret et régulier</span>
          </h1>
          <p className="text-white/70 text-lg max-w-2xl mb-8">
            Un environnement de travail propre est un gage de professionnalisme et de bien-être. Nous intervenons avant ou après les heures d&apos;ouverture, sans perturber votre activité.
          </p>
          <Link href="/devis" className="btn-gold">Devis gratuit <ArrowRight size={16} /></Link>
        </div>
      </section>

      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6 grid md:grid-cols-2 gap-10">
          <div>
            <h2 className="font-display text-3xl font-bold text-navy mb-6">Nos prestations bureaux</h2>
            <ul className="space-y-3">
              {["Dépoussiérage meubles et écrans", "Aspiration et lavage des sols", "Nettoyage des sanitaires", "Cuisine / espace pause", "Vitres et cloisons vitrées", "Vidage et nettoyage poubelles", "Désinfection des surfaces de contact", "Entretien terrasses / balcons"].map((item) => (
                <li key={item} className="flex items-center gap-3 text-sm text-navy">
                  <CheckCircle2 size={15} className="text-gold shrink-0" />{item}
                </li>
              ))}
            </ul>
          </div>
          <div className="space-y-4">
            {[
              { t: "Contrat régulier", d: "Nettoyage quotidien, hebdomadaire ou bi-mensuel selon vos besoins. Tarif préférentiel." },
              { t: "Intervention ponctuelle", d: "Grande remise en état, déménagement, événement. Disponibilité sous 48h." },
              { t: "Grand nettoyage annuel", d: "Nettoyage approfondi complet une fois par an. Karcher, vitres, faux plafonds." },
            ].map((s) => (
              <div key={s.t} className="bg-white border border-pearl-cream rounded-xl p-5 shadow-sm">
                <h3 className="font-display font-semibold text-navy mb-1">{s.t}</h3>
                <p className="text-sm text-muted-foreground">{s.d}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-14 bg-gold-gradient">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="font-display text-3xl font-bold text-navy mb-4">Un bureau propre, une image soignée</h2>
          <Link href="/devis" className="btn-navy">Demander un devis <ArrowRight size={16} /></Link>
        </div>
      </section>
    </>
  );
}
