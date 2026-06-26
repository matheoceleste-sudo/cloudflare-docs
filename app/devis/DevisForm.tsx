"use client";
import { useState } from "react";
import { CheckCircle2, Send } from "lucide-react";

interface Props { phone: string; email: string; }

const SERVICES = ["Nettoyage de bateau", "Nettoyage automobile", "Fin de chantier", "Nettoyage bureau", "Locaux professionnels", "Autre"];

export default function DevisForm({ phone, email }: Props) {
  const [sent, setSent] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSent(true);
  };

  if (sent) {
    return (
      <div className="bg-white border border-pearl-cream rounded-2xl p-10 text-center shadow-sm">
        <CheckCircle2 size={48} className="text-gold mx-auto mb-4" />
        <h2 className="font-display text-2xl font-bold text-navy mb-3">Demande reçue !</h2>
        <p className="text-muted-foreground">Nous vous répondrons dans les 2 heures ouvrées.</p>
        <p className="text-sm text-muted-foreground mt-2">
          En urgence : <a href={`tel:${phone}`} className="text-gold font-medium">{phone}</a>
        </p>
      </div>
    );
  }

  return (
    <div className="bg-white border border-pearl-cream rounded-2xl p-8 shadow-sm">
      <form onSubmit={handleSubmit} className="space-y-5">
        <div className="grid sm:grid-cols-2 gap-4">
          <div>
            <label className="block text-xs font-semibold text-navy mb-1.5 uppercase tracking-wider">Prénom *</label>
            <input required type="text" placeholder="Jean" className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm text-navy focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition" />
          </div>
          <div>
            <label className="block text-xs font-semibold text-navy mb-1.5 uppercase tracking-wider">Nom *</label>
            <input required type="text" placeholder="Dupont" className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm text-navy focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition" />
          </div>
        </div>
        <div className="grid sm:grid-cols-2 gap-4">
          <div>
            <label className="block text-xs font-semibold text-navy mb-1.5 uppercase tracking-wider">Téléphone *</label>
            <input required type="tel" placeholder="+33 6 00 00 00 00" className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm text-navy focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition" />
          </div>
          <div>
            <label className="block text-xs font-semibold text-navy mb-1.5 uppercase tracking-wider">Email *</label>
            <input required type="email" placeholder={email} className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm text-navy focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition" />
          </div>
        </div>
        <div>
          <label className="block text-xs font-semibold text-navy mb-1.5 uppercase tracking-wider">Service souhaité *</label>
          <select required className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm text-navy focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition bg-white">
            <option value="">Sélectionnez un service</option>
            {SERVICES.map((s) => <option key={s} value={s}>{s}</option>)}
          </select>
        </div>
        <div>
          <label className="block text-xs font-semibold text-navy mb-1.5 uppercase tracking-wider">Description</label>
          <textarea rows={4} placeholder="Décrivez votre besoin (type de bateau, marque de voiture, superficie, état actuel...)" className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm text-navy focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition resize-none" />
        </div>
        <div>
          <label className="block text-xs font-semibold text-navy mb-1.5 uppercase tracking-wider">Localisation</label>
          <input type="text" placeholder="Antibes, Cannes, Nice..." className="w-full border border-pearl-cream rounded-lg px-4 py-3 text-sm text-navy focus:outline-none focus:ring-2 focus:ring-gold/30 focus:border-gold transition" />
        </div>
        <button type="submit" className="btn-gold w-full justify-center py-4 text-base">
          <Send size={18} />
          Envoyer ma demande
        </button>
        <p className="text-xs text-muted-foreground text-center">Sans engagement · Réponse sous 2 heures · Vos données sont protégées</p>
      </form>
    </div>
  );
}
