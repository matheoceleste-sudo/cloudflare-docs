# Maison Céleste — Site vitrine

Site vitrine de luxe pour une maison de parfum, en HTML / CSS / JS statique.
Esthétique éditoriale **crème & or** (Playfair Display + Inter). Contenu en
français, entièrement en **placeholder** — prêt à recevoir votre vraie marque.

> Réalisé avec l'intelligence de design **UI/UX Pro Max** (tokens, typographie,
> palette luxe, checklist accessibilité).

## Aperçu local

Aucune installation, aucun build. Il suffit d'un petit serveur statique :

```bash
cd maison-celeste
python3 -m http.server 8080
# puis ouvrez http://localhost:8080
```

(ou ouvrez simplement `index.html` dans le navigateur — un serveur est
toutefois recommandé pour que les liens relatifs fonctionnent partout.)

## Pages

| Fichier | Contenu |
|--------|---------|
| `index.html` | Accueil : hero, collections en vedette, parfum signature, savoir-faire, newsletter |
| `collections.html` | La collection : filtres par famille olfactive + 5 parfums |
| `parfum.html` | Fiche parfum (Nuit d'Ambre) : pyramide olfactive, récit, suggestions |
| `maison.html` | La Maison : histoire, savoir-faire, valeurs, chiffres |
| `contact.html` | Contact : formulaire (validation front) + coordonnées |

## Structure

```
maison-celeste/
├── index.html · collections.html · parfum.html · maison.html · contact.html
├── css/styles.css     # tokens, styles éditoriaux, animations, responsive
├── js/main.js         # menu mobile, header au scroll, reveals, filtres, formulaires
├── assets/            # flacons SVG (par famille), logo, favicon ; img/ pour vos photos
├── data.md            # ⭐ tout le contenu à personnaliser (noms, notes, prix, coordonnées)
└── README.md
```

## Personnaliser (votre marque)

1. Ouvrez **`data.md`** : il liste tout ce qui est modifiable (nom de la maison,
   baseline, 5 parfums avec notes olfactives et prix, coordonnées, chiffres).
2. Reportez vos valeurs dans les fichiers `.html` (les noms de parfums, prix et
   notes apparaissent tels quels dans le code — un simple rechercher/remplacer suffit).
3. **Vraies photos** : déposez vos images dans `assets/img/` et remplacez les
   `<img src="assets/flacon-*.svg">` par vos fichiers. Les flacons livrés sont des
   illustrations SVG (une teinte de liquide par famille olfactive).
4. **Couleurs & polices** : tout est centralisé dans les variables `:root` en haut
   de `css/styles.css`.

## Notes techniques

- **Tailwind** est chargé via le *Play CDN* (utilitaire optionnel, extensible).
  Le design ne dépend **pas** de Tailwind : tout le style vit dans `css/styles.css`,
  donc le site reste correct même si le CDN est indisponible. Pour la production,
  vous pouvez migrer vers un build Tailwind (`tailwindcss` en dépendance) afin de
  supprimer l'avertissement console de développement.
- **Polices** : Playfair Display + Inter via Google Fonts (`display=swap`).
- **Accessibilité** : navigation clavier, focus visibles, `aria-*`, contrastes
  soignés, `prefers-reduced-motion` respecté, responsive 375 / 768 / 1024 / 1440.
- **Formulaires** : validation côté client uniquement (aucun backend). Pour recevoir
  réellement les messages, branchez l'action du formulaire à un service
  (Formspree, Netlify Forms, votre API…).

## Héberger

Site 100 % statique → déployable tel quel sur Cloudflare Pages, Netlify, Vercel,
GitHub Pages ou tout hébergeur de fichiers.
