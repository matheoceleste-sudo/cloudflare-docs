import type { Metadata } from "next";
import { SITE } from "./constants";

export function buildMeta(opts: {
  title: string;
  description: string;
  path?: string;
  noIndex?: boolean;
}): Metadata {
  const url = opts.path ? `${SITE.url}${opts.path}` : SITE.url;
  const fullTitle = `${opts.title} | ${SITE.name}`;
  return {
    title: fullTitle,
    description: opts.description,
    metadataBase: new URL(SITE.url),
    alternates: { canonical: url },
    openGraph: {
      title: fullTitle,
      description: opts.description,
      url,
      siteName: SITE.name,
      locale: "fr_FR",
      type: "website",
    },
    twitter: {
      card: "summary_large_image",
      title: fullTitle,
      description: opts.description,
    },
    robots: opts.noIndex
      ? { index: false, follow: false }
      : { index: true, follow: true, googleBot: { index: true, follow: true } },
  };
}

export const jsonLdOrganization = {
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": `${SITE.url}/#business`,
  name: SITE.name,
  url: SITE.url,
  logo: `${SITE.url}/logo.png`,
  image: `${SITE.url}/og-image.jpg`,
  description: SITE.description,
  telephone: SITE.phone,
  email: SITE.email,
  priceRange: "€€€",
  address: {
    "@type": "PostalAddress",
    streetAddress: SITE.address.street,
    addressLocality: SITE.address.city,
    postalCode: SITE.address.zip,
    addressCountry: "FR",
    addressRegion: SITE.address.region,
  },
  geo: { "@type": "GeoCoordinates", latitude: "43.5804", longitude: "7.1251" },
  openingHoursSpecification: [
    {
      "@type": "OpeningHoursSpecification",
      dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      opens: "08:00",
      closes: "19:00",
    },
    {
      "@type": "OpeningHoursSpecification",
      dayOfWeek: ["Saturday"],
      opens: "09:00",
      closes: "17:00",
    },
  ],
  hasOfferCatalog: {
    "@type": "OfferCatalog",
    name: "Services de nettoyage MathClean",
    itemListElement: [
      { "@type": "Offer", itemOffered: { "@type": "Service", name: "Nettoyage de bateaux et yachts" } },
      { "@type": "Offer", itemOffered: { "@type": "Service", name: "Nettoyage automobile (detailing)" } },
      { "@type": "Offer", itemOffered: { "@type": "Service", name: "Nettoyage fin de chantier" } },
      { "@type": "Offer", itemOffered: { "@type": "Service", name: "Nettoyage de bureaux et locaux professionnels" } },
    ],
  },
  sameAs: [SITE.socials.instagram, SITE.socials.facebook, SITE.socials.linkedin],
};
