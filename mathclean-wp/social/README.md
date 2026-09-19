# Visuels et textes pour les réseaux

Chaque post a un gabarit HTML (les images) et un fichier Markdown (les
légendes, les hashtags, le script vidéo).

    python3 social/rendu.py     # regénère les PNG de social/out/

Formats produits : 1080 × 1350 pour un carrousel Instagram, 1080 × 1920 pour
une couverture TikTok ou une story.

Deux règles tenues ici comme sur le site :

- **Aucun avant/après reconstitué.** Deux photos ne sont présentées comme une
  paire que si elles montrent le même objet, avant et après la même
  intervention. Sinon la légende dit ce que chaque photo est vraiment.
- **Les chiffres viennent de `content.py`.** Tarifs, délais et frais de
  déplacement sont recopiés depuis la grille, jamais réinventés pour le
  besoin d'une accroche. Un post qui annonce un autre prix que le site fait
  exactement le dégât que l'audit avait relevé.

## Posts

| Sujet | Gabarit | Textes |
|---|---|---|
| Nettoyage de canapé | `carrousel-canape.html` | `canape-textes.md` |
