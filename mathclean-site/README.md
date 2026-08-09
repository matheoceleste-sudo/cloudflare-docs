# Site MathClean — nettoyage premium à Paris & Île-de-France

Site vitrine statique (HTML/CSS/JS pur, sans dépendance), construit avec le
même gabarit visuel « MATCLEANING » mais avec les **vraies informations de
mathclean.fr** : nom, slogan, coordonnées, adresse, 10 prestations, avis
clients, FAQ et photos réelles.

## Informations reprises du vrai site mathclean.fr

- **Nom** : MathClean — slogan « Une exigence de roi »
- **Téléphone** : 06 23 07 52 59 (7j/7, 8h–20h)
- **E-mail** : matheoceleste@gmail.com
- **Adresse** : 4 Rue Nicolas Copernic, 93290 Tremblay-en-France
- **Zone d'intervention** : Paris (75) et les 7 départements d'Île-de-France
  (77, 78, 91, 92, 93, 94, 95), déplacement gratuit
- **10 prestations** : automobile, canapé, matelas, tapis, bateau, avion,
  terrasse, locaux, bureau, fin de chantier
- **Photos réelles** : photo du fondateur (Mathéo), 3 paires avant/après
  (siège auto, plan de travail, réfrigérateur professionnel), 3 photos
  d'intervention — toutes reprises du zip fourni

## Structure

| Fichier | Rôle |
|---|---|
| `index.html` | Accueil : présentation, avant/après, engagements, 10 services, zones, avis, FAQ, contact |
| `nettoyage-automobile.html` | Detailing automobile, tarifs (49 à 79 €), options |
| `nettoyage-canape.html` | Nettoyage de canapé |
| `nettoyage-matelas.html` | Nettoyage de matelas |
| `nettoyage-tapis.html` | Nettoyage de tapis |
| `nettoyage-bateau.html` | Entretien nautique |
| `nettoyage-avion.html` | Nettoyage d'avion / jet privé |
| `nettoyage-terrasse.html` | Nettoyage de terrasse |
| `nettoyage-locaux.html` | Nettoyage de locaux commerciaux |
| `nettoyage-bureau.html` | Nettoyage de bureau |
| `nettoyage-fin-de-chantier.html` | Nettoyage fin de chantier |
| `contact.html` | Coordonnées + formulaire de devis + carte |
| `mentions-legales.html` | Mentions légales (SIRET à compléter) |
| `css/style.css` | Feuille de style (couleurs dans les variables `:root`) |
| `js/main.js` | Menu mobile + année automatique |
| `images/` | Photos réelles + logo lion (`lion.svg`) |

## À compléter avant la mise en ligne

1. **SIRET** : à renseigner dans `mentions-legales.html` (champ signalé `[…]`).
2. **Formulaire de contact** : utilise déjà `formsubmit.co` vers
   matheoceleste@gmail.com, comme le site d'origine — aucune action requise,
   mais la première soumission demande une validation par e-mail
   (lien de confirmation envoyé par FormSubmit).
3. **Nom de marque** : si un autre nom est souhaité, un rechercher/remplacer
   sur « MathClean » dans les fichiers `.html` suffit.

## Mise en ligne (Cloudflare Pages, gratuit)

1. Dézippez l'archive — tous les fichiers doivent être **à la racine**
   (pas dans un sous-dossier).
2. Dashboard Cloudflare → **Workers & Pages → Create → Pages → Upload
   assets**.
3. Glissez-déposez le contenu du dossier (pas le zip lui-même).
4. Dans **Custom domains**, ajoutez mathclean.fr.

Fonctionne aussi sur Netlify, OVH, o2switch ou tout hébergement classique.
