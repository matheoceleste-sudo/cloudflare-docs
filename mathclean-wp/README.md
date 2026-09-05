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

## Les 84 pages indexables

- Accueil, À propos, Tarifs, Réalisations, Réservation, Devis, Contact
- 8 pages de prestations (`services/`), dont le traitement par ozone
- **28 pages villes** (`villes/`) + leur sommaire
- **17 guides pratiques** (`guides/`) + leur sommaire
- Zones d'intervention + 8 pages départements (`zones/`)
- Blog + 8 articles de conseils (`blog/`)
- Merci, 404, mentions légales, confidentialité, cookies
- `sitemap.xml` et `robots.txt` générés automatiquement

## Réserver en ligne

`reservation.html` est un configurateur en quatre étapes : prestation →
détail → lieu et date → coordonnées. Le prix se construit en direct dans le
récapitulatif de droite.

- **Automobile** : les quatre packs et les trois options de `content.py`.
- **Textile** : compteurs de quantité par pièce, additionnés.
- **Autres prestations** : passage en « sur devis » avec un champ descriptif.
- **Frais de déplacement** : calculés depuis l'adresse saisie via l'API
  Adresse de data.gouv.fr (service public français, sans cookie ni compte),
  selon la règle des 5 € par tranche de 5 km. Si l'API ne répond pas, la
  réservation continue : le message indique que les frais seront confirmés
  avant validation.

La demande part par FormSubmit avec un récapitulatif lisible. Sans
JavaScript, la page renvoie vers le formulaire de devis et le téléphone.

## Le traitement par ozone : ce qui est écrit, et pourquoi

L'ozone est un gaz irritant pour les voies respiratoires ; l'ANSES le
rappelle dans ses avis. Les pages du site le disent explicitement, et
décrivent le protocole : local vidé de ses occupants, de leurs animaux et de
leurs plantes, puis aération avant restitution.

**Aucune page n'affirme que l'ozone désinfecte, tue des virus ou élimine des
bactéries.** Ces allégations relèvent du règlement biocides européen
528/2012 : les revendiquer sans autorisation vous exposerait, et elles sont
invérifiables dans les conditions réelles d'un habitacle ou d'un logement.

Ce que les pages affirment — la destruction des molécules odorantes par
oxydation — est exact, constatable immédiatement, et suffit largement à
vendre la prestation. Dire franchement ce que l'ozone ne fait pas est aussi
ce qui vous distingue des prestataires qui le présentent comme une solution
miracle.

Cinq pages couvrent la demande : la prestation elle-même, l'entreprise de
traitement ozone à Paris, le traitement en Île-de-France, le cas du
véhicule, les règles de sécurité, et le prix.

## Villes et guides

Deux familles de pages nourrissent le référencement, chacune pilotée depuis
`content.py`.

**`VILLES`** — une page par commune. La distance depuis l'atelier et les
frais de déplacement sont **calculés**, pas écrits à la main : le générateur
applique la même règle que le configurateur (vol d'oiseau × 1,25, puis 5 €
par tranche de 5 km). Ajouter une commune revient à ajouter une ligne avec
ses coordonnées et deux phrases qui lui sont propres.

Les coordonnées sont celles du centre communal : la distance affichée est
donc annoncée comme approximative, et la page précise que le montant exact
se calcule sur l'adresse réelle.

**`GUIDES`** — pages de fond répondant à une question précise (« combien
coûte un nettoyage de canapé », « comment choisir une entreprise »). Ce sont
elles qui se font citer, par Google comme par les assistants IA : un contenu
argumenté est repris, une page vide ne l'est pas.

> **À ne pas faire :** dupliquer une page ville en changeant seulement le nom
> de la commune. Google identifie ces pages sans contenu propre et les
> déclasse en bloc, y compris le reste du site. Chaque commune ajoutée doit
> apporter au moins un paragraphe qui n'existe nulle part ailleurs.

## Être recommandé par les assistants IA

Trois dispositifs sont en place :

- **`/llms.txt`** — une fiche de synthèse en texte brut à la racine :
  identité, SIRET, engagements, tarifs, zone, liens. C'est le format que
  lisent les robots des assistants ; il est régénéré à chaque build depuis
  `content.py`, donc toujours à jour.
- **`robots.txt`** autorise explicitement GPTBot, ClaudeBot, PerplexityBot,
  Google-Extended et les autres, pour lever toute ambiguïté.
- **Données structurées** Schema.org sur chaque page : LocalBusiness,
  Service, FAQPage, Article, BreadcrumbList.

Ce qui compte le plus reste le contenu : un assistant cite ce qui est
factuel, daté et vérifiable. Les prix chiffrés, le SIRET, l'absence
d'acompte et la règle de déplacement sont repris parce qu'ils sont
précis — pas parce qu'ils sont flatteurs.

> **Une allégation à éviter :** « la meilleure entreprise de nettoyage
> d'Île-de-France ». Elle est invérifiable, exposée au titre de la publicité
> trompeuse, et contre-productive : Google comme les assistants IA écartent
> les superlatifs non étayés. Le guide « Comment choisir une entreprise de
> nettoyage » vise la même requête en donnant des critères vérifiables.

## La photo d'en-tête

L'accueil ouvre sur une photo, plus sur une vidéo. Elle se règle dans
`content.py`, bloc `HERO` :

```python
HERO = {
    "image": "hero-mathclean-vapeur.webp",  # fichier dans site/assets/photos/
    "position": "center 45%",               # zone visible après recadrage
    "alt": "…",
}
```

La photo est en portrait et le navigateur la recadre en bandeau : `position`
décide de la bande visible. `center 45%` place le visage et le logo du t-shirt
à droite, en laissant le texte lisible à gauche. Si vous changez de photo,
ajustez ce pourcentage — plus bas = on descend dans l'image.

## Afficher vos avis Google

Deux réglages dans `content.py` :

- `GOOGLE_NOTE` — la note globale et le nombre d'avis affichés en tête de
  section. À corriger quand ils bougent.
- `REVIEWS` — **vos vrais avis**, recopiés depuis votre fiche Google.

`REVIEWS` est volontairement vide au départ. Tant qu'elle l'est, le site
affiche la note globale et renvoie vers Google, sans afficher le moindre
témoignage : rien n'est inventé. Dès que vous ajoutez une ligne au format

```python
("Sophie L.", "12 août 2026", 5, "Intervention impeccable sur mon canapé…"),
```

une carte d'avis apparaît sur l'accueil, la page À propos et la page
Réalisations.

> Un affichage automatique des avis Google demanderait l'API Google Places :
> une clé, un compte de facturation et un serveur. Pour une dizaine d'avis
> qui changent rarement, la recopie manuelle est plus simple et plus fiable.

## Remplacer les images

**C'est le seul point de l'audit que le code ne peut pas régler seul.**
14 des 28 photos font moins de 640 px de large et paraissent floues une fois
agrandies. En attendant de vraies photos, deux mesures ont été prises pour
limiter la casse :

- les quatre comparateurs avant/après en **haute** définition passent en
  premier, et ce sont eux que l'accueil affiche ;
- les quatre comparateurs en 192 × 160 px sont relégués dans une grille de
  trois colonnes sur la page Réalisations, où ils sont affichés à 380 px
  au lieu de 800 : ils y restent nets.

Cela reste un pansement. Déposez le nouveau fichier dans
`site/assets/photos/` **sous le même nom** : rien d'autre à modifier.

| Fichier | Où il s'affiche | Taille minimale conseillée |
|---|---|---|
| `ba-canape-avant.webp` / `-apres.webp` | Comparateur « Canapé en tissu » | 1200 × 900 |
| `ba-tapis-avant.webp` / `-apres.webp` | Comparateur « Tapis et moquette » | 1200 × 900 |
| `ba-terrasse-avant.webp` / `-apres.webp` | Comparateur « Terrasse extérieure » | 1200 × 900 |
| `ba-fauteuil-avant.webp` / `-apres.webp` | Comparateur « Fauteuil de bureau » | 1200 × 900 |
| `bateau-yacht.webp` | Carte + page « Nettoyage de bateau » | 1200 × 800 |
| `bureau-entreprise.webp` | Carte + page « Nettoyage pour entreprise » | 1200 × 800 |
| `tapis-karcher.webp` | Article « Raviver un tapis » | 1200 × 800 |
| `intervention-1/2/3.webp` | En-tête des pages Prestations | 1520 × 1140 |

Ordre de priorité, du plus visible au moins visible :

1. `intervention-1/2/3.webp` (620 × 826) — en-tête des huit pages de
   prestation, c'est-à-dire l'élément le plus grand de vos pages les plus
   consultées, affiché en 760 × 570.
2. `bateau-yacht.webp` (420 × 194) et `bureau-entreprise.webp` (506 × 216) —
   vignettes de l'accueil et de la page Prestations, très recadrées parce que
   leur format est trop allongé pour un cadre 4/3.
3. Les huit miniatures avant/après en 192 × 160.
4. `tapis-karcher.webp` (506 × 250).

**Vos propres photos d'intervention valent mieux que n'importe quelle photo
de banque** : elles montrent votre travail, et les paires avant/après n'ont
de sens que si elles sont vraies. Un téléphone récent suffit largement.

À défaut, ces deux banques sont gratuites, utilisables commercialement et
sans obligation de crédit — cherchez-y les termes indiqués :

- **Pexels** (pexels.com) et **Unsplash** (unsplash.com)
- Termes utiles : « car detailing interior », « sofa cleaning », « carpet
  cleaning machine », « pressure washing deck », « office cleaning »,
  « boat cleaning marina », « window cleaning squeegee »

Convertissez en WebP avant de déposer (squoosh.app, gratuit et sans compte),
puis relancez `python3 build.py`.

> Attention aux paires avant/après : n'utilisez **pas** deux photos de banque
> sans lien entre elles pour simuler un résultat. Ce serait une mise en scène
> trompeuse. Ces comparateurs doivent montrer vos vraies interventions — ou
> être retirés de `BEFORE_AFTER` dans `content.py`.

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

1. **Le lien des avis Google** pointe désormais sur votre vraie fiche
   (`https://www.google.com/maps?cid=8434710860473546146`), déduite de l'URL
   Maps que vous m'avez transmise. Si votre tableau de bord Google Business
   vous fournit un lien court « Demander des avis » (`g.page/r/…`), il ouvre
   directement la fenêtre de notation : remplacez `review_url` par celui-là,
   c'est un clic de moins pour vos clients.
2. **Les images trop petites** : voir la section « Remplacer les images »
   ci-dessus. Quinze fichiers sont concernés.
3. **Les frais de déplacement** sont annoncés partout comme « 5 € par tranche
   de 5 km ». L'ancien site affichait par endroits « déplacement gratuit »,
   ce qui se contredisait ; la version payante a été retenue, conformément à
   la FAQ et au configurateur de l'ancien site.
4. **L'ancienne adresse `/services/nettoyage-locaux-paris.html`** est
   redirigée en 301 vers `nettoyage-entreprise-paris.html` par le fichier
   `_redirects`, pour ne pas perdre le référencement acquis. De même,
   l'ancienne page « nettoyage d'avion » renvoie vers la liste des
   prestations.
5. **Les coordonnées de votre fiche Google** (48.9499, 2.4560) diffèrent de
   celles de l'atelier utilisées pour les frais de déplacement (48.9486,
   2.5697) — environ 8 km d'écart. Les liens Maps pointent sur votre fiche ;
   le calcul de déplacement part de l'atelier. Dites-moi si l'un des deux
   doit être corrigé.

## Audit technique du site

Le site est vérifié par deux scripts, à relancer après toute modification
importante. Ils lisent le dossier `site/` généré, pas les gabarits.

### Ce qui est contrôlé, et le résultat actuel

| Contrôle | État |
|---|---|
| Liens internes cassés | 0 sur ~8 000 liens |
| Ancres internes (`#…`) qui ne pointent nulle part | 0 |
| Balises `title` hors des 25–60 caractères affichés par Google | 0 sur 86 |
| Méta-descriptions hors des 70–160 caractères | 0 sur 86 |
| Titres, descriptions ou `h1` dupliqués | 0 |
| Pages sans `canonical`, ou avec un `canonical` erroné | 0 |
| Pages orphelines (aucun lien entrant) | 0 |
| Écarts entre le sitemap et les fichiers réellement produits | 0 |
| JSON-LD invalide ou incomplet | 0 sur 213 blocs |
| Hiérarchie de titres avec un niveau sauté (`h2` → `h4`) | 0 |
| Pages sous 300 mots | 0 |
| Quasi-doublons de contenu entre deux pages | 0 |
| Balises Open Graph / Twitter manquantes | 0 |
| Redirections `_redirects` en boucle ou sans cible | 0 |
| Images sans `alt`, sans dimensions, ou LCP en chargement différé | 0 |
| Erreurs JavaScript, requêtes échouées, débordement horizontal | 0 sur 86 pages |
| **Photos de définition insuffisante** | **14** — voir « Remplacer les images » |

### Relancer les vérifications

Le premier script analyse le HTML produit ; le second ouvre chaque page dans
un vrai navigateur (Chromium via Playwright) et surveille la console, les
requêtes, la largeur de mise en page et les blocs restés invisibles.

Ils ne sont pas versionnés avec le site : demandez-les si vous en avez
besoin, ou contentez-vous du contrôle intégré — `python3 build.py` refuse de
produire une page dont un gabarit est cassé, et `clean_stale()` supprime les
pages qui ne sont plus générées.

### Points corrigés lors de l'audit complet

- Le bouton **« Réserver »** de l'en-tête sortait de l'écran sur tout écran
  de 1 081 à 1 345 px de large — donc sur la plupart des ordinateurs
  portables, sur **chaque page** du site.
- L'énumération des prestations était écrite en dur à trois endroits et avait
  oublié l'ozone ; elle se déduit désormais de `SERVICES`.
- Cinq liens de catégories du blog pointaient vers des ancres inexistantes.
- Les 17 guides n'avaient pas de date de publication dans leurs données
  structurées, ce que Google exige pour un `Article`.
- Les balises `title` dépassaient 60 caractères sur 25 pages, dont deux qui
  répétaient « MathClean » deux fois.
- La première image de 51 pages était en chargement différé alors qu'elle est
  l'élément déterminant du score de vitesse.
