// Shared site-wide constants — update these with real info before going live
export const SITE = {
  name:        "MathClean",
  tagline:     "L'excellence du nettoyage professionnel",
  url:         "https://mathclean.fr",
  description: "MathClean — Expert en nettoyage professionnel de bateaux, véhicules, chantiers et locaux. Service premium pour une clientèle exigeante.",
  phone:       "+33 6 00 00 00 00",
  email:       "contact@mathclean.fr",
  address: {
    street:  "00 Rue de l'Exemple",
    city:    "Antibes",
    zip:     "06600",
    country: "France",
    region:  "Provence-Alpes-Côte d'Azur",
  },
  socials: {
    instagram: "https://instagram.com/mathclean",
    facebook:  "https://facebook.com/mathclean",
    linkedin:  "https://linkedin.com/company/mathclean",
  },
} as const;

export const SERVICES = [
  {
    slug:        "nettoyage-bateau",
    label:       "Nettoyage de bateaux",
    shortLabel:  "Bateaux",
    description: "Nettoyage intérieur et extérieur de voiliers, yachts, bateaux de plaisance.",
    icon:        "Anchor",
    href:        "/services/nettoyage-bateau",
    featured:    true,
  },
  {
    slug:        "nettoyage-voiture",
    label:       "Nettoyage automobile",
    shortLabel:  "Véhicules",
    description: "Detailing complet pour citadines, berlines, SUV, 4×4 et vans.",
    icon:        "Car",
    href:        "/services/nettoyage-voiture",
    featured:    true,
  },
  {
    slug:        "nettoyage-fin-chantier",
    label:       "Fin de chantier",
    shortLabel:  "Chantier",
    description: "Remise en état complète après travaux de construction ou rénovation.",
    icon:        "HardHat",
    href:        "/services/nettoyage-fin-chantier",
    featured:    false,
  },
  {
    slug:        "nettoyage-bureau",
    label:       "Bureaux",
    shortLabel:  "Bureaux",
    description: "Nettoyage régulier ou ponctuel de bureaux et espaces de travail.",
    icon:        "Building2",
    href:        "/services/nettoyage-bureau",
    featured:    false,
  },
  {
    slug:        "nettoyage-locaux",
    label:       "Locaux professionnels",
    shortLabel:  "Locaux",
    description: "Entretien de commerces, entrepôts, cabinets et tout local professionnel.",
    icon:        "Warehouse",
    href:        "/services/nettoyage-locaux",
    featured:    false,
  },
] as const;

export const CAR_TYPES = [
  { slug: "citadine", label: "Citadine",      price: "À partir de 80 €" },
  { slug: "berline",  label: "Berline",        price: "À partir de 110 €" },
  { slug: "suv",      label: "SUV",            price: "À partir de 140 €" },
  { slug: "4x4",      label: "4×4",            price: "À partir de 150 €" },
  { slug: "van",      label: "Van / Utilitaire", price: "À partir de 180 €" },
] as const;

export const STATS = [
  { value: 8,    suffix: "+", label: "Ans d'expérience" },
  { value: 500,  suffix: "+", label: "Clients satisfaits" },
  { value: 1200, suffix: "+", label: "Interventions réalisées" },
  { value: 100,  suffix: "%", label: "Satisfaction garantie" },
] as const;

export const TESTIMONIALS = [
  {
    name:    "Charles M.",
    role:    "Propriétaire de yacht",
    content: "MathClean a transformé mon voilier. Résultat impeccable, équipe discrète et professionnelle. Je ne fais confiance qu'à eux.",
    stars:   5,
  },
  {
    name:    "Sophie L.",
    role:    "Dirigeante d'entreprise",
    content: "Pour nos locaux et nos véhicules de société, MathClean est notre partenaire depuis 3 ans. Toujours au rendez-vous, toujours parfait.",
    stars:   5,
  },
  {
    name:    "Marc D.",
    role:    "Promoteur immobilier",
    content: "Les nettoyages de fin de chantier sont d'une qualité rare. Livraison toujours dans les délais, résultat digne des plus grandes maisons.",
    stars:   5,
  },
] as const;
