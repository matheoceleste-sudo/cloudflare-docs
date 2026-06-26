import type { Metadata } from "next";
import Link from "next/link";
import { MapPin, ArrowRight } from "lucide-react";
import { buildMeta } from "@/lib/seo";

export const metadata: Metadata = buildMeta({
  title: "Zones d'intervention — Côte d'Azur et PACA",
  description: "MathClean intervient sur toute la Côte d'Azur : Antibes, Cannes, Nice, Monaco, Saint-Tropez, Toulon, Marseille. Nettoyage bateaux, voitures, locaux.",
  path: "/zones-intervention",
});

const ZONES = [
  { ville: "Antibes / Juan-les-Pins", detail: "Port Vauban, Port Gallice, secteur résidentiel" },
  { ville: "Cannes", detail: "Vieux-Port, Port Canto, Palm Beach" },
  { ville: "Nice", detail: "Port de Nice, Promenade des Anglais" },
  { ville: "Monaco", detail: "Port Hercule, Fontvieille" },
  { ville: "Saint-Tropez", detail: "Port de Saint-Tropez, Port Grimaud" },
  { ville: "Juan-les-Pins", detail: "Golfe-Juan, Vallauris" },
  { ville: "Menton", detail: "Port de Menton, Garavan" },
  { ville: "Beaulieu-sur-Mer", detail: "Port de Beaulieu" },
  { ville: "Villefranche-sur-Mer", detail: "Rade de Villefranche" },
  { ville: "Saint-Jean-Cap-Ferrat", detail: "Port de Plaisance" },
  { ville: "Toulon", detail: "Port de Toulon, Bandol" },
  { ville: "Marseille", detail: "Vieux-Port, Frioul, Estaque" },
];

export default function ZonesPage() {
  return (
    <>
      <section className="relative pt-36 pb-20 bg-navy">
        <div className="absolute inset-0 bg-gradient-to-br from-navy-dark to-navy" />
        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <h1 className="font-display text-5xl font-bold text-white mb-5">Zones d&apos;intervention</h1>
          <p className="text-white/60 text-lg">Côte d&apos;Azur, PACA et alentours. Nous nous déplaçons chez vous, au port ou sur site.</p>
        </div>
      </section>
      <section className="section bg-pearl-warm">
        <div className="max-w-5xl mx-auto px-6">
          <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-4 mb-12">
            {ZONES.map((z) => (
              <div key={z.ville} className="bg-white border border-pearl-cream rounded-xl p-5 shadow-sm flex items-start gap-3">
                <MapPin size={16} className="text-gold shrink-0 mt-0.5" />
                <div>
                  <p className="font-semibold text-navy text-sm">{z.ville}</p>
                  <p className="text-xs text-muted-foreground mt-0.5">{z.detail}</p>
                </div>
              </div>
            ))}
          </div>
          <div className="bg-navy rounded-2xl p-8 text-center text-white">
            <h2 className="font-display text-2xl font-bold mb-3">Votre ville n&apos;est pas listée ?</h2>
            <p className="text-white/60 mb-6 text-sm">Contactez-nous, nous étudions toutes les demandes en dehors de notre zone habituelle.</p>
            <Link href="/contact" className="btn-gold">Nous contacter <ArrowRight size={16} /></Link>
          </div>
        </div>
      </section>
    </>
  );
}
