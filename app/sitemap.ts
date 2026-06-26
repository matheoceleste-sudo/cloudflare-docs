import type { MetadataRoute } from "next";
import { SITE } from "@/lib/constants";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = SITE.url;
  const now = new Date();

  const pages: MetadataRoute.Sitemap = [
    { url: base,                                               lastModified: now, changeFrequency: "weekly",  priority: 1.0 },
    { url: `${base}/services`,                                 lastModified: now, changeFrequency: "weekly",  priority: 0.9 },
    { url: `${base}/services/nettoyage-bateau`,                lastModified: now, changeFrequency: "monthly", priority: 0.9 },
    { url: `${base}/services/nettoyage-voiture`,               lastModified: now, changeFrequency: "monthly", priority: 0.9 },
    { url: `${base}/services/nettoyage-voiture/citadine`,      lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/services/nettoyage-voiture/berline`,       lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/services/nettoyage-voiture/suv`,           lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/services/nettoyage-voiture/4x4`,           lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/services/nettoyage-voiture/van`,           lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/services/nettoyage-fin-chantier`,          lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/services/nettoyage-bureau`,                lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/services/nettoyage-locaux`,                lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/realisations`,                             lastModified: now, changeFrequency: "weekly",  priority: 0.8 },
    { url: `${base}/realisations/bateaux`,                     lastModified: now, changeFrequency: "weekly",  priority: 0.8 },
    { url: `${base}/realisations/voitures`,                    lastModified: now, changeFrequency: "weekly",  priority: 0.8 },
    { url: `${base}/realisations/chantiers`,                   lastModified: now, changeFrequency: "weekly",  priority: 0.7 },
    { url: `${base}/a-propos`,                                 lastModified: now, changeFrequency: "monthly", priority: 0.7 },
    { url: `${base}/contact`,                                  lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/devis`,                                    lastModified: now, changeFrequency: "monthly", priority: 0.9 },
    { url: `${base}/tarifs`,                                   lastModified: now, changeFrequency: "monthly", priority: 0.8 },
    { url: `${base}/faq`,                                      lastModified: now, changeFrequency: "monthly", priority: 0.7 },
    { url: `${base}/zones-intervention`,                       lastModified: now, changeFrequency: "monthly", priority: 0.7 },
    { url: `${base}/blog`,                                     lastModified: now, changeFrequency: "weekly",  priority: 0.7 },
    { url: `${base}/blog/nettoyage-bateau-professionnel`,      lastModified: now, changeFrequency: "monthly", priority: 0.6 },
    { url: `${base}/blog/entretien-voiture-luxe`,              lastModified: now, changeFrequency: "monthly", priority: 0.6 },
    { url: `${base}/blog/nettoyage-fin-chantier-guide`,        lastModified: now, changeFrequency: "monthly", priority: 0.6 },
    { url: `${base}/mentions-legales`,                         lastModified: now, changeFrequency: "yearly",  priority: 0.3 },
    { url: `${base}/politique-confidentialite`,                lastModified: now, changeFrequency: "yearly",  priority: 0.3 },
  ];

  return pages;
}
