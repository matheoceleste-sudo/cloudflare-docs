# Atelier BKR Mods — thème Shopify « Liquid Glass »

Refonte du thème Dawn exporté depuis la boutique, pensée pour un catalogue de
Seiko mod organisé **par famille**, chaque famille contenant **tous ses coloris**.

```
seiko-mods/
├── theme/      le thème Shopify complet, prêt à être zippé et importé
└── preview/    une maquette HTML autonome, sans Shopify, pour juger du rendu
```

---

## 1. La structure du catalogue

| Notion boutique | Objet Shopify | Exemple |
| --- | --- | --- |
| Famille | **Collection** | `Datejust` |
| Coloris | **Produit** | `Datejust 36 mm — Cadran bleu soleillé` |
| Options | **Variantes** | bracelet jubilé / oyster, 36 / 41 mm |

C'est ce découpage qui donne le plus de souplesse : chaque coloris garde son
propre stock, son prix, ses photos et sa page — donc son référencement — pendant
que la famille sert de vitrine.

### La couleur des pastilles

Le nuancier affiché sous chaque montre prend sa couleur, dans l'ordre :

1. le métachamp `custom.dial_color` du produit (type *Couleur*) ;
2. à défaut, un mot-clé reconnu dans le titre du produit — `bleu`, `vert`,
   `champagne`, `bordeaux`, `ivoire`, `anthracite`, `turquoise`… (voir
   `snippets/lg-dial-color.liquid` pour la liste complète) ;
3. à défaut, la teinte réglée sur la famille dans l'éditeur.

Autrement dit : ça fonctionne dès l'import, sans rien configurer, et le
métachamp permet d'être précis quand un cadran mérite sa nuance exacte.

---

## 2. Installer le thème

1. Zipper le contenu du dossier `theme/` — **le contenu, pas le dossier** :
   ```bash
   cd seiko-mods/theme && zip -r ../atelier-bkr-mods.zip . -x '.*'
   ```
2. Dans l'admin Shopify : **Boutique en ligne › Thèmes › Ajouter un thème ›
   Importer un fichier zip**.
3. Prévisualiser, puis publier.

### Après l'import

- **Créer une collection par famille** (Datejust, Diver, Explorer, GMT…).
- **Page d'accueil › section « Verre — Familles »** : dans chaque bloc,
  sélectionner la collection correspondante et régler sa teinte.
- Créer les pages `atelier`, `faq` et `contact` (Pages › Ajouter une page) puis
  leur affecter le modèle `page.atelier`, `page.faq` ou `page.contact`.
- Le menu principal : Familles → `/collections`, Atelier → `/pages/atelier`,
  FAQ → `/pages/faq`, Contact → `/pages/contact`.

---

## 3. Ce qui a été ajouté au thème

### Base

| Fichier | Rôle |
| --- | --- |
| `assets/liquid-glass.css` | Le système visuel : jetons, surfaces de verre, typographie, composants, et les raccords qui reprennent les composants natifs de Dawn (en-tête, cartes, tiroir panier, boutons). |
| `assets/liquid-glass.js` | Le moteur d'animation, sans dépendance : apparitions au défilement, titres mot à mot, inclinaison 3D, boutons magnétiques, halo qui suit le pointeur, compteurs, bandeau infini, sélecteur de coloris. |
| `snippets/lg-dial-color.liquid` | Résout la couleur de cadran d'un produit. |
| `layout/theme.liquid` | Charge les deux fichiers ci-dessus et pose le décor global (nappes de couleur, grain, barre de progression). |

### Sections

| Section | Où | Ce qu'elle fait |
| --- | --- | --- |
| `lg-hero` | Accueil, Atelier | Titre révélé mot à mot, visuel en lévitation, halo tournant, chiffres clés. |
| `lg-families` | Accueil | Une carte par famille, avec le nuancier de ses coloris. **Le cœur du dispositif.** |
| `lg-all-families` | Liste des collections | Toutes les familles, automatiquement. |
| `lg-colorways` | Page de collection | Tous les coloris de la famille, en cartes de verre. |
| `lg-marquee` | Partout | Bandeau défilant des arguments. |
| `lg-specs` | Accueil, Atelier | Chiffres qui se comptent à l'arrivée à l'écran. |
| `lg-steps` | Accueil, Atelier | Les étapes du montage. |
| `lg-faq` | Accueil, FAQ, Contact | Accordéon en verre. |
| `lg-cta` | Fin de page | Bandeau de contact. |

Toutes sont paramétrables dans l'éditeur de thème (textes, couleurs, blocs) et
possèdent un *preset*, donc s'ajoutent à n'importe quelle page.

### Modèles reconfigurés

`index`, `collection`, `list-collections`, `product`, `page.contact`, plus deux
nouveaux : `page.atelier` et `page.faq`.

### Réglages

`config/settings_data.json` passe sur une palette sombre (cinq jeux de couleurs),
des angles arrondis, des boutons en pilule et les animations d'apparition
activées.

---

## 4. Les animations

Toutes sont pilotées par des attributs `data-`, donc réutilisables ailleurs :

| Attribut | Effet |
| --- | --- |
| `data-lg-reveal` | Apparition en fondu, montée et flou levé. |
| `data-lg-stagger="90"` | Cadence l'apparition des enfants, en millisecondes. |
| `data-lg-split` | Titre révélé mot à mot. |
| `data-lg-tilt="6"` | Inclinaison 3D suivant le pointeur. |
| `data-lg-magnetic` | L'élément est attiré par le curseur. |
| `data-lg-parallax="0.1"` | Décalage vertical au défilement. |
| `data-lg-count="200"` | Compte de 0 jusqu'à la valeur. |
| `data-lg-marquee` | Duplique la piste pour une boucle sans couture. |

`prefers-reduced-motion` coupe l'ensemble du mouvement décoratif, et les effets
au pointeur ne s'activent que sur un pointeur fin — rien ne se déclenche au
toucher.

---

## 5. La maquette

`preview/index.html` reprend exactement le même langage visuel avec un catalogue
d'exemple, sans Shopify. Les montres y sont dessinées en SVG et recolorées par
coloris, ce qui permet de juger le dispositif avant d'avoir les photos produit.

Deux détails qui n'existent que là : la montre du hero donne l'heure réelle et sa
trotteuse avance par pas d'un sixième de seconde — la cadence d'un NH35 à
21 600 alternances/heure — et la teinte d'ambiance de toute la page suit le
cadran survolé.

---

## 6. Un point à trancher avant d'ouvrir

Les noms de familles retenus (`Datejust`, `Explorer`, `GMT`…) sont des marques
déposées par leurs horlogers. L'usage est courant dans le milieu du mod, mais il
expose à une demande de retrait. Les noms sont concentrés en un seul endroit —
le titre des collections, plus le champ « Nom affiché » de chaque bloc — donc
basculer vers une nomenclature maison (`Date`, `Plongeur`, `Explorateur`,
`Voyageur`) ne demande que quelques minutes.
