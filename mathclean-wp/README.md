# MathClean — site « style WordPress »

Refonte du site MathClean avec l'allure d'un thème WordPress d'entreprise
(Astra / Kadence / GeneratePress) : fond clair, en-tête collant avec menus
déroulants, cartes de services, blog avec colonne latérale, pied de page à
colonnes.

Techniquement, c'est un **site statique** : que du HTML, du CSS et du
JavaScript. Aucun PHP, aucune base de données, aucune mise à jour de sécurité
à faire. Il se dépose tel quel chez n'importe quel hébergeur.

## Ce qu'il y a dans le dossier

```
mathclean-wp/
├── site/          ← LE SITE. C'est ce dossier que vous mettez en ligne.
├── content.py     ← Tout le texte, les tarifs, les villes, les articles.
├── theme/         ← Le style (theme.css) et les scripts (theme.js).
├── build.py       ← Le générateur : assemble theme/ + content.py → site/
└── README.md
```

## Mettre le site en ligne

### Cloudflare Workers, depuis ce dépôt (ce qui est configuré ici)

Le fichier `wrangler.jsonc` de ce dossier décrit un Worker « assets seuls » :
aucun code serveur, Cloudflare se contente de servir les fichiers de `site/`.

Dans le tableau de bord Cloudflare, ouvrez le projet **mathclean** →
*Settings* → *Build*, et renseignez :

| Réglage | Valeur |
|---|---|
| Root directory | `mathclean-wp` |
| Build command | *(vide — le site est déjà généré)* |
| Deploy command | `npx wrangler deploy` |

Le **Root directory est le réglage indispensable**. Sans lui, le build lit le
`wrangler.toml` de la racine du dépôt, qui appartient au projet
`cloudflare-docs` et vise un autre compte Cloudflare : il échoue en une
fraction de seconde, sans même compiler.

### Sans passer par ce dépôt

Envoyez **le contenu du dossier `site/`** (pas le dossier lui-même) à la
racine de votre hébergement. `index.html` doit se retrouver à la racine du
domaine.

- **Cloudflare Pages** : créez un projet, « Direct upload », déposez le
  contenu de `site/`. C'est le chemin le plus court si vous ne voulez pas
  lier le dépôt.
- **Netlify** : glissez le dossier `site/` sur app.netlify.com/drop.
- **OVH / o2switch / hébergement FTP classique** : copiez le contenu de
  `site/` dans `www/` ou `public_html/`.

Le site fonctionne aussi en local : ouvrez `site/index.html` dans un
navigateur, ou lancez `python3 -m http.server 8000` depuis `site/`.

## Modifier le contenu

Tout le texte est dans **`content.py`**. Vous y modifiez ce que vous voulez
(un tarif, une description, une ville, un article), puis vous régénérez :

```bash
python3 build.py
```

Le dossier `site/` est reconstruit. C'est le principe d'un thème : l'en-tête,
le pied de page et le menu sont écrits **une seule fois** dans `build.py` et
appliqués aux 38 pages. Pas besoin de modifier 38 fichiers pour changer un
numéro de téléphone.

Quelques repères dans `content.py` :

| Ce que vous voulez changer | Où |
|---|---|
| Téléphone, e-mail, adresse, SIRET | `SITE` |
| Les 8 prestations (texte, FAQ, méthode) | `SERVICES` |
| Packs auto, options, tarifs textile | `PACKS_AUTO`, `OPTIONS_AUTO`, `TARIFS_TEXTILE` |
| Départements et listes de villes | `ZONES` |
| Articles de conseils | `POSTS` |
| FAQ de l'accueil | `FAQ` |
| Photos avant / après | `BEFORE_AFTER` |

Les couleurs se règlent en haut de `theme/theme.css`, dans le bloc `:root`
(`--brand` pour le bleu, `--gold` pour le doré).

## Les 38 pages

- Accueil, À propos, Tarifs, Réalisations, Devis, Contact
- 8 pages de prestations (`services/`)
- Zones d'intervention + 8 pages départements (`zones/`)
- Blog + 8 articles de conseils (`blog/`)
- Merci, 404, mentions légales, confidentialité, cookies
- `sitemap.xml` et `robots.txt` générés automatiquement

## Ce qui est déjà en place

- **Référencement** : titres et descriptions uniques sur chaque page, balises
  canoniques, Open Graph, et données structurées Schema.org (LocalBusiness,
  Service, FAQPage, BlogPosting, BreadcrumbList) pour les résultats enrichis
  Google.
- **Formulaires** : ils passent par FormSubmit vers `matheoceleste@gmail.com`,
  comme sur l'ancien site, avec un piège à robots et une redirection vers
  `merci.html`. **À la première demande reçue, FormSubmit vous enverra un
  e-mail d'activation à valider** — sans quoi les messages n'arrivent pas.
- **Mobile** : menu en tiroir, barre d'appel fixe en bas de l'écran.
- **Sans JavaScript** : le site reste entièrement lisible ; seules les
  animations d'apparition sont désactivées.
- **RGPD** : aucun outil de traçage, aucune police ni ressource chargée depuis
  un serveur tiers. Le seul stockage local sert à mémoriser la fermeture du
  bandeau d'information.

## À vérifier avant la mise en ligne

1. **Le lien des avis Google** (`SITE["review_url"]` dans `content.py`) est un
   lien générique : remplacez-le par le vrai lien « Rédiger un avis » de votre
   fiche Google Business.
2. **La photo `ba-canape-avant/apres.webp`** est en 192 × 160 px : elle est
   floue une fois agrandie. Une photo plus grande améliorerait nettement le
   rendu du comparateur.
3. **Les frais de déplacement** sont annoncés partout comme « 5 € par tranche
   de 5 km ». L'ancien site affichait par endroits « déplacement gratuit »,
   ce qui se contredisait ; la version payante a été retenue, conformément à
   la FAQ et au configurateur de l'ancien site.
