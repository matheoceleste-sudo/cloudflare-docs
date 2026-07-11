# Flyers Mathclean

Deux flyers pour Mathclean — *« L'art du nettoyage à Paris »* — service de
nettoyage haut de gamme (particuliers & professionnels, bateaux/yachts, jets privés).

Style éditorial épuré : bleu marine profond, or discret, typographie Cormorant
Garamond + Jost, filets fins.

## Fichiers

| Fichier | Description |
|---------|-------------|
| `print-flyer.html` | Flyer papier (format A5 portrait, ratio 1240×1754 → export 300 dpi) |
| `print-flyer.png` | Rendu du flyer papier, prêt à imprimer |
| `animated-flyer.html` | Flyer animé pour le web (carré 1080×1080) : halo, apparitions en cascade, particules dorées |
| `animated-flyer-frame.png` | Aperçu statique de la version animée |

## Intégration web

La version animée est un fichier HTML autonome (Google Fonts en `<link>`).
Intégration sur mathclean.fr par exemple en `<iframe>` :

```html
<iframe src="animated-flyer.html" width="1080" height="1080"
        style="border:0; max-width:100%;" title="Mathclean"></iframe>
```

## Personnalisation

Coordonnées et textes sont éditables directement dans le HTML :
- Slogan, services, descriptions
- Téléphone : `06 23 07 52 59`
- Email : `Matheoceleste@gmail.com`
- Site : `mathclean.fr`
- Zone : Paris et alentours — déplacement dans toute la France
