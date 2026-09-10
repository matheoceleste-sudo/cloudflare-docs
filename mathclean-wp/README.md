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

## Les 26 pages issues de l'étude des requêtes

Ces pages visent des demandes réellement exprimées en Île-de-France que le site
ne couvrait pas. La méthode et ses limites sont dites franchement plus bas.

| Créneau | Pages |
|---|---|
| Fin de bail et état des lieux | `nettoyage-fin-de-bail-paris`, `nettoyage-etat-des-lieux-sortie`, `prix-nettoyage-fin-de-bail` |
| Copropriété et immeuble | `nettoyage-copropriete-parties-communes`, `nettoyage-cage-escalier-immeuble`, `nettoyage-parking-local-poubelles` |
| Location courte durée | `nettoyage-airbnb-paris` |
| Textile | `nettoyage-matelas-paris`, `prix-nettoyage-matelas`, `nettoyage-tapis-paris`, `nettoyage-canape-cuir-alcantara`, `nettoyage-moquette-bureau-paris`, `nettoyage-fauteuil-chaise-bureau` |
| Vitrerie | `nettoyage-vitrine-commerce-paris`, `prix-nettoyage-vitres-m2`, `nettoyage-veranda-baie-vitree` |
| Extérieur | `demoussage-terrasse-ile-de-france`, `prix-nettoyage-terrasse-m2`, `nettoyage-salon-jardin-mobilier-exterieur` |
| Professionnels | `prix-nettoyage-bureaux-m2`, `nettoyage-local-commercial-restaurant` |
| Chantier | `prix-nettoyage-fin-de-chantier-m2`, `nettoyage-apres-travaux-appartement` |
| Automobile | `nettoyage-siege-voiture-tache`, `lavage-auto-domicile-paris` |
| Urgence | `nettoyage-urgent-7j-7-ile-de-france` |

### Comment ces sujets ont été choisis

**Ce qui n'a pas été fait :** aucun volume de recherche mensuel exact n'a pu être
mesuré. Ces chiffres ne sont pas publics — ils viennent de Google Keyword Planner
ou d'outils payants (Semrush, Ahrefs, Haloscan, Ranxplorer), auxquels cette
session n'a pas accès. Toute personne qui vous annonce « 4 800 recherches par
mois » sans montrer sa source invente.

**Ce qui a été fait :** une étude des pages qui se positionnent déjà sur ces
requêtes en Île-de-France, des services que les concurrents mettent en avant, et
des fourchettes de prix réellement pratiquées. Les repères tarifaires cités dans
les pages en viennent, et ils sont datés de 2026.

**Le filtre appliqué :** chaque page correspond à une prestation que MathClean
réalise vraiment. Plusieurs demandes fortes ont été écartées pour cette raison —
dégraissage certifié des conduits d'extraction, désinsectisation, dératisation,
nettoyage après décès. Elles relèvent d'activités réglementées ou d'agréments que
l'entreprise n'a pas. Les pages le disent explicitement plutôt que de laisser
croire le contraire.

**Pour aller plus loin :** si vous voulez les volumes réels, ouvrez un compte
Google Ads (gratuit) et utilisez le Keyword Planner sur ces mots-clés, ciblage
Île-de-France. Vous saurez alors lesquelles de ces 26 pages méritent d'être
étoffées en priorité.

## La vidéo de méthode

Un film de 59 secondes tourné sur une intervention réelle — matelas, canapé,
puis vitres — est intégré au site. C'est la pièce la plus convaincante dont
vous disposez : on y voit la personne qui viendra, faisant le geste décrit
dans les textes.

### Ce qui a été produit

| Fichier | Durée | Poids | Où |
|---|---|---|---|
| `methode-mathclean.mp4` | 59 s | 4,5 Mo | Accueil, Réalisations |
| `methode-textile.mp4` | 37 s | 3,1 Mo | Prestation textile, 4 guides |
| `methode-vitres.mp4` | 22 s | 1,6 Mo | Prestation vitres, 4 guides |

Chacun a son affiche `.webp` (22 à 34 Ko), tirée de l'encodage final pour que
les couleurs correspondent exactement.

### Traitements appliqués

- **Conversion HDR → SDR.** L'original est filmé en HLG (HDR). Servi tel quel,
  il apparaît délavé sur la plupart des écrans. Un tone-mapping *mobius* le
  ramène en bt709 avec un rattrapage léger de saturation et de contraste.
- **Compression.** 30 Mo à l'origine, 4,5 Mo pour la version complète, en
  640 × 1138. Le texte incrusté reste net.
- **`preload="none"`** sur chaque balise : rien n'est téléchargé tant que le
  visiteur n'a pas cliqué. Le poids des vidéos ne pèse donc pas sur la vitesse
  d'affichage des pages.
- **Format vertical maîtrisé.** Une vidéo 9/16 affichée pleine largeur sur un
  écran d'ordinateur serait démesurée. Le bloc `.video-split` la contraint à
  300 px et place le texte à côté ; sur mobile, tout s'empile.

### Ce que cela apporte au référencement

Douze pages portent désormais un balisage `VideoObject`, et le `sitemap.xml`
déclare les vidéos avec l'extension vidéo de Google (titre, description,
vignette, durée). Google peut afficher une vignette vidéo dans ses résultats,
ce qui augmente nettement le taux de clic. Le fichier `llms.txt` mentionne la
vidéo dans une section « Preuves consultables », pour que les assistants IA
sachent qu'elle existe et où elle se trouve.

### Ce que la vidéo ne peut pas remplacer

Des images extraites de la vidéo ont été testées pour combler le manque de
photos. **Le résultat n'est pas utilisable** : le film est vertical, et le
recadrer en paysage coupe le sujet ; les images sont par ailleurs plus molles
qu'une photo, et chaque plan porte un filigrane ou un sous-titre incrusté.
Les 14 photos listées plus haut restent à remplacer par de vraies photos.

### Si vous refaites une vidéo

Ce qui rendrait le prochain film encore plus utile :

- **Quelques plans en format paysage** en plus du vertical. Ils serviraient
  d'images de page, ce que le vertical ne permet pas.
- **Des plans fixes de deux à trois secondes** sans mouvement de caméra : ce
  sont eux qui donnent des images nettes exploitables.
- **Un plan sur la cuve d'eau sale** en fin d'extraction, tenu plus longtemps.
  C'est la preuve la plus parlante du métier, et elle passe vite dans le
  montage actuel.

## La page 404, et pourquoi ses chemins sont absolus

Cloudflare renvoie `404.html` **à l'adresse demandée** : si un visiteur ouvre
`/services/une-page-disparue.html`, il reçoit le contenu de la page 404 mais
l'adresse affichée reste `/services/une-page-disparue.html`.

Conséquence : avec des chemins relatifs, le navigateur cherche la feuille de
style dans `/services/assets/css/` — qui n'existe pas. La page s'affiche alors
**entièrement sans style**, en HTML brut, avec des icônes géantes et des liens
bleus soulignés. Tous ses liens de navigation sont cassés en prime.

C'est pour cela que `build_404()` utilise `base = "/"` et que ses liens sont
écrits en absolu. Une seule page du site a besoin de ce traitement, parce
qu'elle est la seule à être servie à une adresse qui n'est pas la sienne.

> **Effet de bord à connaître :** si vous ouvrez `404.html` en double-cliquant
> dessus depuis votre disque, elle apparaîtra sans style — un chemin absolu
> pointe alors vers la racine du disque. C'est normal et sans conséquence :
> en ligne, servie par un serveur web, elle s'affiche correctement.

### Les anciennes adresses

Les 31 pages de l'ancien site sont toutes couvertes : soit la page existe
encore, soit une redirection 301 la remplace. `_redirects` liste chaque
ancienne adresse **avec et sans l'extension `.html`**, parce qu'un lien
partagé ou recopié perd souvent son extension.

## Les dates dans les données structurées

Google exige un **fuseau horaire** sur les propriétés de date et heure des
données structurées. Une date nue comme `2026-09-05` est refusée : il faut
`2026-09-05T12:00:00+02:00`.

C'est ce que la Search Console a signalé sur `uploadDate` — la date de mise en
ligne des vidéos — le 7 septembre 2026. Deux avertissements pour un seul
défaut : « fuseau horaire manquant » et « valeur de date et heure incorrecte ».

La fonction `horodatage()` de `build.py` convertit toute date du fichier
`content.py` au format attendu, avec le décalage de Paris correspondant à la
saison (+02:00 en été, +01:00 en hiver). Elle s'applique à `uploadDate`,
`datePublished`, `dateModified`, aux balises Open Graph `article:*` et à la
date de publication des vidéos dans le sitemap — **114 propriétés au total**.

L'heure retenue est **midi**, à dessein : quel que soit le fuseau du lecteur,
la date affichée reste la même.

> Le calcul repose sur `zoneinfo`, mais un repli applique la règle européenne
> à la main (dernier dimanche de mars au dernier dimanche d'octobre) si les
> données de fuseau manquent sur la machine qui reconstruit le site. Les deux
> méthodes ont été vérifiées identiques sur les dates de bascule, de 2025 à 2027.

Les dates **visibles** sur les pages restent en `<time datetime="…">` au format
court : c'est valide en HTML et plus lisible.

## Les produits : le pH plutôt que la marque

Le site explique désormais **sur quel critère un produit est choisi**, parce
que c'est ce qui distingue une intervention professionnelle d'un passage de
chiffon — et parce que c'est un sujet sur lequel personne d'autre n'écrit
sérieusement en local.

Une page de fond, `guides/ph-produits-nettoyage-professionnel.html`, développe
en dix sections :

| Sujet | Ce qui est expliqué |
| --- | --- |
| L'échelle de pH | 0 à 14, ce que chaque plage dissout et ce qu'elle abîme |
| Le cuir | Tanné en milieu acide : d'où l'obligation du pH neutre, gammes de detailing citées |
| Le mousseur | Peu d'eau, beaucoup de volume — pourquoi une peau saturée craquelle au séchage |
| L'alcalin | Saponification des corps gras, application localisée, neutralisation obligatoire |
| L'acide | Calcaire et dépôts minéraux, et les supports sur lesquels il est proscrit |
| L'inox (1) | Les chlorures percent la couche passive : la Javel fait rouiller l'inox |
| L'inox (2) | Sens du brossage, et contamination ferreuse par la laine d'acier |
| Les hottes | Vapeur avant produit, et le piège des filtres aluminium face aux décapants four |
| Laine et soie | Fibres protéiniques dégradées au-delà de pH 8 |
| Biodégradable | Ce que le mot recouvre, et ce qu'il ne garantit pas |

Un bloc **« Nos produits »** apparaît en plus sur quatre pages de prestation —
automobile, textile, entreprise, bateau — sous la forme de six cartes chacune.
Il se pilote par la clé `chimie` de `content.py` : une prestation qui ne la
déclare pas n'affiche pas la section.

### Trois points de vocabulaire à connaître

- **« Bio » n'est pas écrit sur le site, volontairement.** Le terme est réservé
  aux produits certifiés par un organisme agréé. Sans label vérifiable
  (Écolabel européen, Ecocert), le mot juste est « biodégradable », et c'est
  celui qui est employé partout. Si vous obtenez une certification, dites-le
  et les pages seront modifiées en conséquence.
- **Koch Chemie est cité comme fabricant utilisé**, pas comme partenariat.
  La page précise d'ailleurs que ce n'est pas une question de marque mais de
  gammes qui affichent leur pH — ce qu'aucun produit de grande surface ne fait.
- **Le périmètre des hottes est rappelé** dans le bloc entreprise comme dans la
  page de fond : surfaces, caissons et filtres accessibles oui, dégraissage
  certifié du conduit d'extraction non.

## Audit technique du site

Le site est vérifié par deux scripts, à relancer après toute modification
importante. Ils lisent le dossier `site/` généré, pas les gabarits.

### Ce qui est contrôlé, et le résultat actuel

| Contrôle | État |
|---|---|
| Liens internes cassés | 0 sur ~13 000 liens |
| Ancres internes (`#…`) qui ne pointent nulle part | 0 |
| Balises `title` hors des 25–60 caractères affichés par Google | 0 sur 112 |
| Méta-descriptions hors des 70–160 caractères | 0 sur 112 |
| Titres, descriptions ou `h1` dupliqués | 0 |
| Pages sans `canonical`, ou avec un `canonical` erroné | 0 |
| Pages orphelines (aucun lien entrant) | 0 |
| Écarts entre le sitemap et les fichiers réellement produits | 0 |
| JSON-LD invalide ou incomplet | 0 sur 303 blocs |
| Hiérarchie de titres avec un niveau sauté (`h2` → `h4`) | 0 |
| Pages sous 500 mots | 0 sur 112 |
| Quasi-doublons de contenu (hors gabarit partagé) | 0 |
| Balises Open Graph / Twitter manquantes | 0 |
| Redirections `_redirects` en boucle ou sans cible | 0 |
| Images sans `alt`, sans dimensions, ou LCP en chargement différé | 0 |
| Erreurs JavaScript, requêtes échouées, débordement horizontal | 0 sur 112 pages |
| Balisage vidéo (`VideoObject` + sitemap vidéo) | 12 pages |
| **Photos de définition insuffisante** | **14** — voir « Remplacer les images » |

Le site compte **110 pages indexables**, plus `404.html` et `merci.html` en
`noindex`. La page la plus courte fait 500 mots, la médiane 668.

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
