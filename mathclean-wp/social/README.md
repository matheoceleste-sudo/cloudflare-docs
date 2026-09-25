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

| Sujet | Gabarit | Textes | Visuels |
|---|---|---|---|
| Nettoyage de canapé | `carrousel-canape.html` | `canape-textes.md` | 7 pour le carrousel, 2 pour TikTok (couverture et carte de fin) |

## L'appel à l'action

Un post se termine par **une** action, pas par une liste de moyens de contact.
Le carrousel sépare les deux : l'avant-dernier visuel est la preuve (on vient
chez vous, avec notre matériel), le dernier est l'action — le configurateur,
qui donne un prix en deux minutes sans avoir à parler à quelqu'un. Le
téléphone et le message privé restent dessous, en plus petit, pour ceux que
le formulaire rebute.

Le lien en bio pointe vers `mathclean.fr/reservation`, pas vers l'accueil :
quelqu'un qui arrive depuis un post a déjà vu le prix, le renvoyer le chercher
une deuxième fois est le meilleur moyen de le perdre.
