# Animation 3D au défilement — Nettoyage vapeur & lavage auto

Animation 3D interactive (Three.js / WebGL) pilotée par le scroll, prête à intégrer
sur un site web. Aucune dépendance externe : Three.js est embarqué dans `vendor/`.

## Déroulé de l'animation

1. **Vue large** : un canapé 3 places de face dans un salon chic (parquet, moulures,
   fenêtre lumineuse, tableaux, plante, lampadaire). Une personne se tient à côté
   avec l'injecteur-extracteur à vapeur relié à la machine posée au sol.
2. **Zoom progressif** : en défilant, la caméra s'approche du canapé pendant que la
   personne passe l'embout sur les coussins. L'embout est vu de 3/4 : on distingue
   la fine injection de produit à l'avant et la crasse aspirée à travers la tête
   transparente. Les taches sur les coussins s'effacent au passage.
3. **Plongée dans la vapeur** : plus on défile, plus on zoome sur l'aspiration ;
   la vapeur envahit l'écran jusqu'au blanc complet.
4. **Révélation** : la vapeur se dissipe sur une voiture en train d'être lavée à la
   main (éponge, mousse, seau, étincelles de propreté), avec un recul de caméra final.

## Tester en local

Les modules ES exigent un serveur HTTP (ne pas ouvrir le fichier en `file://`) :

```bash
cd animation-nettoyage-3d
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

Astuce debug : ajouter `#p=0.5` à l'URL pour sauter directement à 50 % du défilement.

## Intégrer au site

### Option A — page ou section dédiée (le plus simple)

Copier le dossier `animation-nettoyage-3d/` tel quel sur le site et pointer vers
`index.html` (page d'accueil, page « Nos prestations », etc.).

### Option B — au milieu d'une page existante

Le canvas utilise `position: sticky` à l'intérieur d'une piste `.cv-track` : le bloc
fonctionne donc aussi inséré entre d'autres sections d'une page. Copier dans votre
page :

1. le bloc `<div class="cv-track" id="cvTrack">…</div>` ;
2. les styles CSS (préfixés `cv-`, pas de conflit probable) ;
3. la balise `<script type="module">…</script>` en ajustant le chemin
   `./vendor/three.module.min.js`.

Le pourcentage d'avancement est calculé par rapport à la piste `#cvTrack`, pas par
rapport à la page : l'animation démarre quand la section arrive à l'écran et se
termine quand on l'a traversée.

### Éviter l'iframe

Une iframe capture la molette : le visiteur serait « piégé » dans le cadre.
Préférer les options A ou B.

## Personnalisation rapide

| Réglage | Où |
| --- | --- |
| Durée du scroll | CSS `--cv-track-height` (700vh par défaut — augmenter = animation plus lente) |
| Textes des légendes | Les `<div class="cv-caption">` (attributs `data-from`/`data-to` = fenêtre d'affichage en % du scroll) |
| Couleur du canapé | `M.fabric` / `M.fabric2` dans le script |
| Couleur de la voiture | `carPaint` (`color: 0x8a1f2b`) |
| Moment de la bascule salon → voiture | Constante `SWITCH_P` (0.78) |
| Trajectoire caméra | Tableaux `KEYS_A` (salon) et `KEYS_B` (voiture) |
| Densité de vapeur | Fonction `updateSteam` (constantes `cleaning` et `dive`) |

## Pour aller plus loin

Tous les objets sont modélisés procéduralement (aucun asset à charger, léger et
rapide). Pour un rendu encore plus réaliste, chaque groupe (`sofa`, `nozzle`, `car`…)
peut être remplacé par un modèle GLTF via `GLTFLoader` sans toucher à la logique
de scroll, de caméra ni de particules.
