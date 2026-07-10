"use client";

import { useRef } from "react";
import Link from "next/link";
import { useScroll, useTransform, useMotionTemplate, motion } from "framer-motion";
import { Anchor, ArrowRight, ChevronDown } from "lucide-react";

/* ────────────────────────────────────────────────────────────
   SmoothScrollHero — parallax scroll hero for MathClean.
   Pure framer-motion + CSS smooth scroll (no external deps).
   ──────────────────────────────────────────────────────────── */

const SECTION_HEIGHT = 1200;

export function SmoothScrollHero() {
  return (
    <div className="bg-navy">
      <Hero />
    </div>
  );
}

function Hero() {
  return (
    <div
      style={{ height: `calc(${SECTION_HEIGHT}px + 100vh)` }}
      className="relative w-full"
    >
      <CenterImage />
      <ParallaxContent />
      <div className="absolute bottom-0 left-0 right-0 h-40 bg-gradient-to-b from-transparent to-navy" />
    </div>
  );
}

function CenterImage() {
  const { scrollY } = useScroll();

  const clip1 = useTransform(scrollY, [0, 1500], [25, 0]);
  const clip2 = useTransform(scrollY, [0, 1500], [75, 100]);
  const clipPath = useMotionTemplate`polygon(${clip1}% ${clip1}%, ${clip2}% ${clip1}%, ${clip2}% ${clip2}%, ${clip1}% ${clip2}%)`;

  const backgroundSize = useTransform(scrollY, [0, SECTION_HEIGHT + 500], ["170%", "100%"]);
  const opacity = useTransform(scrollY, [SECTION_HEIGHT, SECTION_HEIGHT + 500], [1, 0]);

  return (
    <motion.div
      className="sticky top-0 h-screen w-full"
      style={{
        clipPath,
        backgroundSize,
        opacity,
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        // Luxury navy → ocean gradient placeholder. Swap for a real yacht photo:
        // backgroundImage: "url(/images/hero-yacht.jpg)"
        backgroundImage:
          "linear-gradient(135deg, #08111f 0%, #0D1B35 40%, #0e2a52 70%, #123a6b 100%)",
      }}
    >
      {/* Gold sun glow */}
      <div
        className="absolute inset-0"
        style={{
          backgroundImage:
            "radial-gradient(circle at 70% 30%, rgba(212,175,55,0.35) 0%, transparent 45%)",
        }}
      />
    </motion.div>
  );
}

function ParallaxContent() {
  return (
    <div className="mx-auto max-w-5xl px-4 pt-[200px]">
      <ParallaxHeadline />
      <ParallaxBadges />
    </div>
  );
}

function ParallaxHeadline() {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });

  const y = useTransform(scrollYProgress, [0, 1], [0, -120]);
  const opacity = useTransform(scrollYProgress, [0, 0.5, 1], [1, 1, 0]);

  return (
    <motion.div ref={ref} style={{ y, opacity }} className="relative z-10 text-center">
      <span className="mb-8 inline-flex items-center gap-2 rounded-full border border-gold/30 bg-gold-muted/10 px-4 py-1.5 text-xs font-semibold uppercase tracking-widest text-gold">
        <Anchor size={12} />
        Spécialiste nautique · Côte d&apos;Azur
      </span>

      <h1 className="font-display text-5xl font-bold leading-tight text-white md:text-7xl">
        L&apos;excellence du<br />
        <span className="bg-gold-gradient bg-clip-text text-transparent">
          nettoyage de luxe
        </span>
      </h1>

      <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-white/70">
        Yachts, voiliers et véhicules d&apos;exception. MathClean redonne à chaque
        surface l&apos;éclat du premier jour, avec un souci du détail digne des plus
        grands ports de plaisance.
      </p>

      <div className="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row">
        <Link
          href="/devis"
          className="inline-flex items-center gap-2 rounded bg-gold-gradient px-7 py-3.5 text-sm font-semibold tracking-wide text-navy transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_4px_24px_rgba(184,149,42,0.4)]"
        >
          Demander un devis gratuit
          <ArrowRight size={16} />
        </Link>
        <Link
          href="/realisations"
          className="inline-flex items-center gap-2 rounded border border-white/60 px-7 py-3.5 text-sm font-semibold tracking-wide text-white transition-all duration-300 hover:border-white hover:bg-white/10"
        >
          Voir nos réalisations
        </Link>
      </div>

      <div className="mt-16 flex flex-col items-center gap-2 text-xs text-white/30">
        <span>Découvrir</span>
        <ChevronDown size={16} className="animate-bounce" />
      </div>
    </motion.div>
  );
}

function ParallaxBadges() {
  const badges = [
    "8+ ans d'expérience",
    "500+ clients satisfaits",
    "Intervention sous 48h",
    "Résultats garantis",
  ];

  return (
    <div className="relative z-10 mt-32 grid grid-cols-2 gap-4 md:grid-cols-4">
      {badges.map((label, i) => (
        <ParallaxBadge key={label} label={label} index={i} />
      ))}
    </div>
  );
}

function ParallaxBadge({ label, index }: { label: string; index: number }) {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });

  // Staggered parallax — alternating badges drift at different speeds.
  const y = useTransform(scrollYProgress, [0, 1], [0, index % 2 === 0 ? -60 : -100]);

  return (
    <motion.div
      ref={ref}
      style={{ y }}
      className="rounded-xl border border-white/10 bg-white/5 p-5 text-center backdrop-blur-sm"
    >
      <p className="text-sm font-medium text-white/80">{label}</p>
    </motion.div>
  );
}
