# Site MATCLEANING — nettoyage professionnel à domicile (Val-d'Oise)

Site vitrine statique (HTML/CSS/JS pur, sans dépendance) reproduisant le design
de matcleaning-95.fr. Il peut être hébergé tel quel sur n'importe quel domaine,
par exemple **mathclean.fr**.

## Structure

| Fichier | Rôle |
|---|---|
| `index.html` | Accueil : présentation, sections canapé / matelas / tapis / voiture, avis Google, carte |
| `nettoyage-canape.html` | Page service canapé |
| `nettoyage-tapis.html` | Page service tapis |
| `nettoyage-matelas.html` | Page service matelas |
| `nettoyage-voiture.html` | Page service intérieur voiture |
| `avant-apres.html` | Galerie avants / après |
| `contact.html` | Coordonnées + formulaire de devis + carte |
| `mentions-legales.html` | Politique de confidentialité et mentions légales (à compléter) |
| `css/style.css` | Feuille de style (couleurs dans les variables `:root` en haut du fichier) |
| `js/main.js` | Menu mobile + année automatique |
| `images/` | Images de remplacement (SVG) à remplacer par vos vraies photos |

## À personnaliser avant la mise en ligne

1. **Photos** : remplacez les fichiers `images/*.svg` par vos vraies photos
   (gardez les mêmes noms, ou mettez à jour les attributs `src` dans les pages).
   Formats conseillés : JPG/WebP, largeur 900 px environ.
2. **Lien « Laissez-nous un avis sur Google »** (`index.html`) : remplacez le
   lien de recherche par le lien direct « Donner un avis » de votre fiche
   Google Business.
3. **Réseaux sociaux** : dans le pied de page de chaque fichier HTML, remplacez
   les `href="#"` par les liens de vos comptes Facebook, Instagram, TikTok et X.
4. **Mentions légales** (`mentions-legales.html`) : complétez les champs entre
   crochets (SIRET, forme juridique, hébergeur, etc.).
5. **Formulaire de contact** (`contact.html`) : il fonctionne en `mailto:`
   (il ouvre la messagerie du visiteur). Pour recevoir les demandes
   directement, créez un formulaire gratuit sur formspree.io et remplacez
   l'attribut `action` du formulaire par l'URL fournie.
6. **Nom de marque** : si le site doit s'appeler autrement (par ex. MATHCLEAN
   au lieu de MATCLEANING), un simple rechercher/remplacer dans les fichiers
   `.html` suffit.

## Mise en ligne (exemple avec Cloudflare Pages, gratuit)

1. Créez un compte sur https://dash.cloudflare.com.
2. Menu **Workers & Pages → Create → Pages → Upload assets**.
3. Glissez-déposez le contenu du dossier `mathclean-site/`.
4. Dans l'onglet **Custom domains**, ajoutez votre domaine (ex. mathclean.fr).

Le site fonctionne aussi sur Netlify, OVH, o2switch ou tout hébergement
classique : il suffit de copier les fichiers à la racine du serveur web.
