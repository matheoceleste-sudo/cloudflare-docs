# Contenu de la Maison — à personnaliser

Ce fichier centralise **tout le texte modifiable** du site. Remplace les valeurs
ici, puis reporte-les dans les pages HTML (les mêmes libellés y sont réutilisés).
Tout est en placeholder : rien n'est réel.

---

## Identité

| Élément | Valeur actuelle (placeholder) |
|--------|-------------------------------|
| Nom de la maison | **Maison Céleste** |
| Baseline | *L'art du sillage, à la française* |
| Ville | Paris |
| Fondée en | 2019 |
| Email | contact@maison-celeste.fr |
| Téléphone | +33 1 42 00 00 00 |
| Adresse boutique | 12 rue Saint-Honoré, 75001 Paris |
| Horaires | Lundi – Samedi · 10h – 19h |
| Instagram / Pinterest / LinkedIn | @maisonceleste |

## Récit de marque (accueil / La Maison)

> Née d'une obsession pour la matière rare, Maison Céleste compose des parfums
> comme on écrit un poème : quelques mots justes, une émotion durable. Chaque
> fragrance est élaborée à Paris, à partir d'essences sourcées auprès de
> producteurs qui partagent notre exigence.

## Les 5 parfums

Chaque parfum : **nom · famille olfactive · notes de tête / cœur / fond · prix (70 ml)**.
Le champ `famille` sert aussi de filtre sur la page Collection
(valeurs : `florale`, `boisee`, `orientale`, `chypree`, `cuir`).

### 1. Nuit d'Ambre — `orientale`
- **Famille affichée** : Orientale ambrée
- **Tête** : Bergamote de Calabre, Safran
- **Cœur** : Rose de Damas, Ambre gris
- **Fond** : Oud, Vanille de Madagascar, Musc
- **Prix** : 185 €
- **Flacon** : `assets/flacon-ambre.svg`
- **Récit** : Un sillage nocturne et enveloppant, entre chaleur ambrée et profondeur boisée.

### 2. Fleur de Sel — `florale`
- **Famille affichée** : Florale marine
- **Tête** : Néroli, Sel marin
- **Cœur** : Jasmin, Freesia
- **Fond** : Musc blanc, Bois flotté
- **Prix** : 165 €
- **Flacon** : `assets/flacon-marine.svg`
- **Récit** : La fraîcheur d'un matin en bord de mer, lumineuse et salée.

### 3. Bois Céleste — `boisee`
- **Famille affichée** : Boisée
- **Tête** : Cardamome, Poivre rose
- **Cœur** : Cèdre, Iris
- **Fond** : Santal, Vétiver
- **Prix** : 175 €
- **Flacon** : `assets/flacon-boise.svg`
- **Récit** : Une élégance boisée et poudrée, à la fois vibrante et sereine.

### 4. Rose Impériale — `chypree`
- **Famille affichée** : Florale chyprée
- **Tête** : Litchi, Bergamote
- **Cœur** : Rose de mai, Pivoine
- **Fond** : Patchouli, Ambre
- **Prix** : 195 €
- **Flacon** : `assets/flacon-rose.svg`
- **Récit** : La rose dans toute sa majesté, sublimée par un fond chypré.

### 5. Cuir Blanc — `cuir`
- **Famille affichée** : Cuir
- **Tête** : Safran, Cassis
- **Cœur** : Cuir, Violette
- **Fond** : Bois de bouleau, Musc
- **Prix** : 210 €
- **Flacon** : `assets/flacon-cuir.svg`
- **Récit** : Un cuir clair et raffiné, adouci par une note florale inattendue.

## Parfum signature (mis en avant sur l'accueil)
**Nuit d'Ambre** — c'est aussi le contenu de la fiche produit `parfum.html`.

## Piliers savoir-faire (accueil / La Maison)
1. **Matières rares** — Essences sourcées auprès de producteurs d'exception.
2. **Création parisienne** — Composées à la main dans notre atelier du 1er arrondissement.
3. **Éco-responsable** — Flacons rechargeables, formules sans composants controversés.

## Chiffres (La Maison)
- **5** créations
- **28** essences naturelles
- **100 %** composé à Paris

---

### Comment remplacer le contenu
1. Modifie les valeurs ci-dessus.
2. Ouvre les fichiers `.html` et remplace le texte correspondant (les noms de
   parfums, prix et notes apparaissent tels quels dans le HTML).
3. Pour de vraies photos, dépose tes images dans `assets/img/` et remplace les
   balises `<img src="assets/flacon-*.svg">` par tes fichiers.
