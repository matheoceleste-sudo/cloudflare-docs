/* Point d'entrée du Worker MathClean.
 *
 * Le site reste servi en fichiers statiques : Cloudflare sert d'abord l'asset
 * s'il existe, et n'appelle ce code que pour les adresses qui n'en sont pas —
 * /api/..., /devis/..., /admin. Une page du site ne passe donc jamais par ici,
 * et rien de ce qui suit ne peut la ralentir.
 */

import { recevoirDemande } from "./reservation.js";
import { pageDevis, accepterDevis } from "./devis.js";
import { routeAdmin } from "./admin.js";
import { passeQuotidienne } from "./relances.js";

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const chemin = url.pathname.replace(/\/+$/, "") || "/";

    try {
      const formulaire = chemin.match(/^\/api\/(reservation|devis|contact)$/);
      if (formulaire) {
        if (request.method !== "POST") return refus(405);
        return await recevoirDemande(request, env, ctx, formulaire[1]);
      }

      const devis = chemin.match(/^\/devis\/([0-9a-f]{32})$/);
      if (devis) return await pageDevis(env, devis[1]);

      const accepte = chemin.match(/^\/devis\/([0-9a-f]{32})\/accepter$/);
      if (accepte) {
        if (request.method !== "POST") return refus(405);
        return await accepterDevis(request, env, ctx, accepte[1]);
      }

      if (chemin === "/admin" || chemin.startsWith("/admin/")) {
        return await routeAdmin(request, env, ctx, url);
      }

      // Le reste n'appartient pas au Worker : Cloudflare a déjà tenté les
      // fichiers, donc c'est une adresse inconnue.
      return env.ASSETS ? env.ASSETS.fetch(request) : refus(404);
    } catch (err) {
      console.error("worker", chemin, err && err.stack ? err.stack : err);
      return new Response(
        "Une erreur est survenue. Appelez le 06 23 07 52 59, on traite la demande à la main.",
        { status: 500, headers: { "content-type": "text/plain; charset=utf-8" } }
      );
    }
  },

  /** La passe quotidienne de relances (voir « triggers » dans wrangler.jsonc). */
  async scheduled(event, env, ctx) {
    ctx.waitUntil(
      passeQuotidienne(env).then(
        (j) => console.log("relances", JSON.stringify(j)),
        (e) => console.error("relances", e && e.stack ? e.stack : e)
      )
    );
  },
};

function refus(code) {
  return new Response(code === 405 ? "Méthode non autorisée" : "Introuvable", {
    status: code,
    headers: { "content-type": "text/plain; charset=utf-8" },
  });
}
