# Clairvent — site de nettoyage de hottes et de cuisines

Site vitrine statique (style WordPress : barre d'infos, menu déroulant, fil d'Ariane, articles avec barre latérale et widgets, pied de page en colonnes), dédié uniquement au nettoyage de hottes et de cuisines en Île-de-France.

## Contenu généré

| Type | Nombre | Dossier |
| --- | --- | --- |
| Pages principales (accueil, savoir-faire, méthode, réglementation, certificat, diagnostic, FAQ, réservation, devis, contact, où nous trouver…) | 23 | `/` |
| Prestations | 16 | `/prestations/` |
| Secteurs d'activité | 12 | `/secteurs/` |
| Conseils (articles) | 44 | `/conseils/` |
| Départements | 8 | `/zones/` |
| Villes | 98 | `/villes/` |
| **Total** | **199 pages, dont 197 indexables** | |

`merci.html` et `404.html` sont en `noindex`. `sitemap.xml`, `robots.txt` et `llms.txt` sont générés automatiquement.

## Fonctionnalités

- **Réservation en ligne** en 5 étapes (établissement et prestations, installation, calendrier et créneau, coordonnées, récapitulatif), pré-remplie depuis les pages prestations et villes (`?prestation=…&ville=…`).
- **Appel** : numéro cliquable partout, barre « Appeler / Réserver » fixe sur mobile, bouton flottant « Être rappelé » sur ordinateur.
- **Devis gratuit** avec envoi de photos. Tous les prix sont **sur devis**.
- **Où nous trouver** : carte OpenStreetMap, carte de la zone d'intervention (cercles à 10, 25 et 40 km) et tableau des distances.
- **Schéma interactif** du circuit d'extraction (hotte, filtres, plénum, conduit, tourelle).
- **Outils gratuits** : calcul de la fréquence de dégraissage et auto-diagnostic de conformité.
- **Référencement** : balise canonical, Open Graph, données structurées (LocalBusiness, Service, FAQPage, Article, BreadcrumbList), maillage interne entre prestations, conseils et villes.

## Modifier et régénérer

Toutes les informations de l'entreprise se trouvent dans l'objet `SITE`, en haut de `build.mjs` (nom, domaine, téléphone, adresse, SIRET, adresse de réception des formulaires). Les textes sont dans `src/data/` :

- `services.mjs` : les prestations
- `guides1.mjs`, `guides2.mjs` : les articles de conseils
- `sectors.mjs` : les secteurs
- `places.mjs` : les départements et les villes

Pour régénérer le site (Node.js 18 ou plus récent, aucune dépendance) :

```bash
node build.mjs
```

Le site prêt à publier se trouve dans `dist/`. Envoyez tout le contenu de ce dossier chez n'importe quel hébergeur (o2switch, OVH, Netlify, Cloudflare Pages…).

## À vérifier avant la mise en ligne

1. **Domaine** : remplacez `https://www.clairvent.fr` dans `SITE.url`.
2. **Formulaires** : ils passent par FormSubmit vers l'adresse de `SITE.form`. Le premier envoi déclenche un e-mail d'activation à confirmer.
3. **Mentions légales** : complétez le bloc « Hébergement » et vérifiez les informations de l'éditeur (reprises de votre site MathClean).
4. **Diplômes et formations** : les pages « Savoir-faire » citent le CAP Agent de propreté et d'hygiène, le Bac pro HPS, le travail en hauteur, le risque chimique, le risque électrique, l'HACCP et le SST. Ne gardez que ceux que votre équipe détient réellement.
5. **Assurance RC Pro** : la FAQ indique que l'entreprise est assurée. Vérifiez-le.
6. **Photos** : les photos avant / après viennent de vos interventions MathClean (cuisine, inox, réfrigération). Ajoutez des photos de hottes dès que possible.
