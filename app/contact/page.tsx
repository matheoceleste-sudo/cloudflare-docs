import type { Metadata } from "next";
import { Phone, Mail, MapPin, Clock } from "lucide-react";
import { buildMeta } from "@/lib/seo";
import { SITE } from "@/lib/constants";

export const metadata: Metadata = buildMeta({
  title: "Contact — Nettoyage professionnel MathClean",
  description: "Contactez MathClean pour un nettoyage professionnel sur la Côte d'Azur. Téléphone, email, formulaire de contact. Réponse rapide garantie.",
  path: "/contact",
});

export default function ContactPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <h1 className="font-display text-5xl font-bold text-white mb-5">Contactez-nous</h1>
          <p className="text-white/60 text-lg">Nous répondons sous 2 heures. Du lundi au samedi.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6 grid md:grid-cols-2 gap-10">
          <div className="space-y-6">
            {[
              { icon: Phone, label: "Téléphone", value: SITE.phone, href: `tel:${SITE.phone}` },
              { icon: Mail, label: "Email", value: SITE.email, href: `mailto:${SITE.email}` },
              { icon: MapPin, label: "Zone d'intervention", value: `${SITE.address.city} et Côte d'Azur`, href: null },
              { icon: Clock, label: "Horaires", value: "Lun–Ven 8h–19h · Sam 9h–17h", href: null },
            ].map((c) => (
              <div key={c.label} className="flex items-start gap-4 bg-white border border-pearl-cream rounded-xl p-5 shadow-sm">
                <div className="w-10 h-10 bg-navy rounded-lg flex items-center justify-center shrink-0">
                  <c.icon size={18} className="text-gold" />
                </div>
                <div>
                  <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-1">{c.label}</p>
                  {c.href ? (
                    <a href={c.href} className="text-navy font-medium hover:text-gold transition-colors">{c.value}</a>
                  ) : (
                    <p className="text-navy font-medium">{c.value}</p>
                  )}
                </div>
              </div>
            ))}
          </div>
          <div className="bg-white border border-pearl-cream rounded-2xl p-8 shadow-sm">
            <h2 className="font-display text-2xl font-bold text-navy mb-6">Message rapide</h2>
            <form className="space-y-4">
              <input type="text" placeholder="Votre nom" className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition" />
              <input type="email" placeholder="Email" className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition" />
              <textarea rows={4} placeholder="Votre message..." className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition resize-none" />
              <button type="submit" className="btn-gold w-full justify-center">Envoyer</button>
            </form>
          </div>
        </div>
      </section>
    </>
  );
}
