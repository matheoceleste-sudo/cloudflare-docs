import Link from "next/link";
import { Phone, Mail, MapPin, Anchor } from "lucide-react";
import { SITE, SERVICES } from "@/lib/constants";

export default function Footer() {
  return (
    <footer className="bg-navy text-white">
      {/* Main footer */}
      <div className="max-w-7xl mx-auto px-6 py-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
        {/* Brand */}
        <div className="lg:col-span-1">
          <Link href="/" className="flex items-center gap-2.5 mb-4">
            <div className="w-8 h-8 bg-gold-gradient rounded flex items-center justify-center">
              <Anchor size={16} className="text-navy" />
            </div>
            <span className="font-display text-xl font-bold">Math<span className="text-gold">Clean</span></span>
          </Link>
          <p className="text-white/60 text-sm leading-relaxed mb-5">
            Expert en nettoyage professionnel depuis plus de 8 ans. Spécialiste du nautisme, de l&apos;automobile et des locaux professionnels sur la Côte d&apos;Azur.
          </p>
          <div className="flex items-center gap-3">
            <a href={SITE.socials.instagram} target="_blank" rel="noopener noreferrer" aria-label="Instagram" className="w-9 h-9 bg-white/10 rounded-full flex items-center justify-center hover:bg-gold transition-colors">
              <span className="text-xs font-bold">IG</span>
            </a>
            <a href={SITE.socials.facebook} target="_blank" rel="noopener noreferrer" aria-label="Facebook" className="w-9 h-9 bg-white/10 rounded-full flex items-center justify-center hover:bg-gold transition-colors">
              <span className="text-xs font-bold">FB</span>
            </a>
            <a href={SITE.socials.linkedin} target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" className="w-9 h-9 bg-white/10 rounded-full flex items-center justify-center hover:bg-gold transition-colors">
              <span className="text-xs font-bold">LI</span>
            </a>
          </div>
        </div>

        {/* Services */}
        <div>
          <h3 className="font-display text-sm font-semibold uppercase tracking-widest text-gold mb-4">Nos services</h3>
          <ul className="space-y-2.5">
            {SERVICES.map((s) => (
              <li key={s.slug}>
                <Link href={s.href} className="text-sm text-white/60 hover:text-gold transition-colors">
                  {s.label}
                </Link>
              </li>
            ))}
            <li>
              <Link href="/services/nettoyage-voiture/citadine" className="text-sm text-white/60 hover:text-gold transition-colors">Nettoyage citadine</Link>
            </li>
            <li>
              <Link href="/services/nettoyage-voiture/berline" className="text-sm text-white/60 hover:text-gold transition-colors">Nettoyage berline</Link>
            </li>
            <li>
              <Link href="/services/nettoyage-voiture/suv" className="text-sm text-white/60 hover:text-gold transition-colors">Nettoyage SUV</Link>
            </li>
            <li>
              <Link href="/services/nettoyage-voiture/4x4" className="text-sm text-white/60 hover:text-gold transition-colors">Nettoyage 4×4</Link>
            </li>
          </ul>
        </div>

        {/* Liens utiles */}
        <div>
          <h3 className="font-display text-sm font-semibold uppercase tracking-widest text-gold mb-4">Liens utiles</h3>
          <ul className="space-y-2.5">
            {[
              { label: "Réalisations",          href: "/realisations" },
              { label: "Avant / Après bateaux", href: "/realisations/bateaux" },
              { label: "Tarifs",                href: "/tarifs" },
              { label: "Devis gratuit",         href: "/devis" },
              { label: "Blog & conseils",       href: "/blog" },
              { label: "FAQ",                   href: "/faq" },
              { label: "Zones d'intervention",  href: "/zones-intervention" },
              { label: "À propos",              href: "/a-propos" },
            ].map((l) => (
              <li key={l.href}>
                <Link href={l.href} className="text-sm text-white/60 hover:text-gold transition-colors">{l.label}</Link>
              </li>
            ))}
          </ul>
        </div>

        {/* Contact */}
        <div>
          <h3 className="font-display text-sm font-semibold uppercase tracking-widest text-gold mb-4">Contact</h3>
          <ul className="space-y-3.5">
            <li className="flex items-start gap-3 text-sm text-white/60">
              <MapPin size={15} className="text-gold mt-0.5 shrink-0" />
              <span>{SITE.address.city}, {SITE.address.zip}<br />{SITE.address.region}</span>
            </li>
            <li>
              <a href={`tel:${SITE.phone}`} className="flex items-center gap-3 text-sm text-white/60 hover:text-gold transition-colors">
                <Phone size={15} className="text-gold shrink-0" />
                {SITE.phone}
              </a>
            </li>
            <li>
              <a href={`mailto:${SITE.email}`} className="flex items-center gap-3 text-sm text-white/60 hover:text-gold transition-colors">
                <Mail size={15} className="text-gold shrink-0" />
                {SITE.email}
              </a>
            </li>
          </ul>
          <div className="mt-6 p-4 bg-white/5 rounded-lg border border-white/10">
            <p className="text-xs text-white/50 mb-1">Lun.–Ven. 8h–19h</p>
            <p className="text-xs text-white/50">Samedi 9h–17h</p>
            <Link href="/devis" className="mt-3 btn-gold text-xs px-4 py-2 w-full justify-center">
              Demander un devis
            </Link>
          </div>
        </div>
      </div>

      {/* SEO paragraph */}
      <div className="border-t border-white/10">
        <div className="max-w-7xl mx-auto px-6 py-6">
          <p className="text-xs text-white/30 leading-relaxed text-center max-w-4xl mx-auto">
            MathClean — Expert en nettoyage professionnel sur la Côte d&apos;Azur. Nettoyage de bateaux, yachts et voiliers à Antibes, Cannes, Nice, Monaco et Juan-les-Pins.
            Detailing automobile, nettoyage fin de chantier, bureaux et locaux professionnels. Intervention rapide, résultats garantis.
          </p>
        </div>
      </div>

      {/* Bottom bar */}
      <div className="border-t border-white/10">
        <div className="max-w-7xl mx-auto px-6 py-4 flex flex-col sm:flex-row items-center justify-between gap-3">
          <p className="text-xs text-white/30">&copy; {new Date().getFullYear()} MathClean. Tous droits réservés.</p>
          <div className="flex items-center gap-4 text-xs text-white/30">
            <Link href="/mentions-legales" className="hover:text-gold transition-colors">Mentions légales</Link>
            <span>·</span>
            <Link href="/politique-confidentialite" className="hover:text-gold transition-colors">Confidentialité</Link>
            <span>·</span>
            <Link href="/sitemap.xml" className="hover:text-gold transition-colors">Plan du site</Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
