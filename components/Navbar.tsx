"use client";
import { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Menu, X, ChevronDown, Phone, Anchor } from "lucide-react";
import { cn } from "@/lib/utils";
import { SITE } from "@/lib/constants";

const NAV = [
  { label: "Accueil", href: "/" },
  {
    label: "Services",
    href: "/services",
    children: [
      { label: "Nettoyage de bateaux", href: "/services/nettoyage-bateau", icon: "⚓" },
      { label: "Nettoyage automobile", href: "/services/nettoyage-voiture", icon: "🚗" },
      { label: "Fin de chantier",       href: "/services/nettoyage-fin-chantier", icon: "🏗️" },
      { label: "Bureaux",               href: "/services/nettoyage-bureau", icon: "🏢" },
      { label: "Locaux professionnels", href: "/services/nettoyage-locaux", icon: "🏭" },
    ],
  },
  {
    label: "Réalisations",
    href: "/realisations",
    children: [
      { label: "Bateaux", href: "/realisations/bateaux", icon: "⛵" },
      { label: "Véhicules", href: "/realisations/voitures", icon: "🚘" },
      { label: "Chantiers", href: "/realisations/chantiers", icon: "🏗️" },
    ],
  },
  { label: "Tarifs",  href: "/tarifs" },
  { label: "Blog",    href: "/blog" },
  { label: "À propos", href: "/a-propos" },
  { label: "Contact", href: "/contact" },
];

export default function Navbar() {
  const [scrolled,     setScrolled]     = useState(false);
  const [menuOpen,     setMenuOpen]     = useState(false);
  const setActiveDropdown = useState<string | null>(null)[1];
  const pathname = usePathname();

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => { setMenuOpen(false); setActiveDropdown(null); }, [pathname]);

  return (
    <header
      className={cn(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-300",
        scrolled
          ? "bg-navy/98 backdrop-blur-md shadow-[0_2px_20px_rgba(0,0,0,0.3)]"
          : "bg-transparent"
      )}
    >
      {/* Top bar */}
      <div className={cn("hidden md:block border-b border-white/10 transition-all duration-300", scrolled ? "h-0 overflow-hidden" : "h-auto")}>
        <div className="max-w-7xl mx-auto px-6 py-2 flex items-center justify-between text-xs text-white/60">
          <span>Service premium · Côte d&apos;Azur &amp; Région PACA</span>
          <a href={`tel:${SITE.phone}`} className="flex items-center gap-1.5 text-gold hover:text-gold-light transition-colors">
            <Phone size={11} />
            {SITE.phone}
          </a>
        </div>
      </div>

      {/* Main nav */}
      <nav className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-2.5 group">
          <div className="w-8 h-8 bg-gold-gradient rounded flex items-center justify-center shadow-md group-hover:shadow-gold/40 transition-all">
            <Anchor size={16} className="text-navy" />
          </div>
          <span className="font-display text-xl font-bold text-white tracking-wide">
            Math<span className="text-gold">Clean</span>
          </span>
        </Link>

        {/* Desktop nav */}
        <ul className="hidden lg:flex items-center gap-0.5">
          {NAV.map((item) => (
            <li key={item.href} className="relative group">
              {item.children ? (
                <>
                  <button
                    className={cn(
                      "flex items-center gap-1 px-3.5 py-2 text-sm font-medium rounded transition-colors",
                      pathname.startsWith(item.href) ? "text-gold" : "text-white/80 hover:text-white"
                    )}
                    onMouseEnter={() => setActiveDropdown(item.href)}
                    onMouseLeave={() => setActiveDropdown(null)}
                  >
                    {item.label}
                    <ChevronDown size={13} className="opacity-60 group-hover:rotate-180 transition-transform duration-200" />
                  </button>
                  {/* Dropdown */}
                  <div
                    className="absolute top-full left-1/2 -translate-x-1/2 pt-2 min-w-[220px] invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all duration-200"
                    onMouseEnter={() => setActiveDropdown(item.href)}
                    onMouseLeave={() => setActiveDropdown(null)}
                  >
                    <div className="bg-navy border border-white/10 rounded-lg shadow-2xl overflow-hidden">
                      {item.children.map((child) => (
                        <Link
                          key={child.href}
                          href={child.href}
                          className="flex items-center gap-3 px-4 py-3 text-sm text-white/80 hover:bg-navy-light hover:text-gold transition-colors border-b border-white/5 last:border-0"
                        >
                          <span>{child.icon}</span>
                          {child.label}
                        </Link>
                      ))}
                    </div>
                  </div>
                </>
              ) : (
                <Link
                  href={item.href}
                  className={cn(
                    "px-3.5 py-2 text-sm font-medium rounded transition-colors",
                    pathname === item.href ? "text-gold" : "text-white/80 hover:text-white"
                  )}
                >
                  {item.label}
                </Link>
              )}
            </li>
          ))}
        </ul>

        {/* CTA */}
        <Link href="/devis" className="hidden lg:inline-flex btn-gold text-xs px-5 py-2.5">
          Devis gratuit
        </Link>

        {/* Mobile hamburger */}
        <button
          className="lg:hidden text-white p-1"
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label="Menu"
        >
          {menuOpen ? <X size={22} /> : <Menu size={22} />}
        </button>
      </nav>

      {/* Mobile menu */}
      {menuOpen && (
        <div className="lg:hidden bg-navy border-t border-white/10 pb-6 px-6 max-h-screen overflow-y-auto">
          {NAV.map((item) => (
            <div key={item.href}>
              <Link
                href={item.href}
                className={cn(
                  "block py-3 text-sm font-medium border-b border-white/10",
                  pathname === item.href ? "text-gold" : "text-white/80"
                )}
              >
                {item.label}
              </Link>
              {item.children?.map((child) => (
                <Link
                  key={child.href}
                  href={child.href}
                  className="block py-2.5 pl-5 text-xs text-white/60 border-b border-white/5 hover:text-gold transition-colors"
                >
                  {child.icon} {child.label}
                </Link>
              ))}
            </div>
          ))}
          <Link href="/devis" className="mt-5 btn-gold w-full justify-center">
            Devis gratuit
          </Link>
        </div>
      )}
    </header>
  );
}
