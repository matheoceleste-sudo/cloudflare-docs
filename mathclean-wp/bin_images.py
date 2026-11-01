#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les variantes responsives des photos du site.

Le site servait une seule taille par photo : une image de 1125 × 1500 px et
345 Ko arrivait telle quelle sur un téléphone qui l'affiche dans 346 px de
large. C'est quatre fois plus de pixels que nécessaire, payés par le
visiteur sur sa connexion mobile — et la vitesse de chargement est un
critère de classement.

Pour chaque photo, on produit des variantes de largeur fixe. `build.py` les
déclare ensuite en srcset et laisse le navigateur choisir : il prend la plus
petite qui couvre son besoin réel, densité d'écran comprise.

    python3 bin_images.py          # génère ce qui manque
    python3 bin_images.py --force  # régénère tout

Les variantes sont écrites à côté de l'original, suffixées par leur largeur
(canape-nettoyage-640.webp). L'original reste la source et sert de repli.
"""
import os
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "site", "assets", "photos")

# Largeurs utiles. 400 couvre un téléphone à densité 1, 800 un téléphone à
# densité 2 et une demi-colonne de bureau, 1200 une grande image de bureau.
# Au-delà, le site n'affiche jamais rien d'assez grand pour le justifier.
LARGEURS = (400, 800, 1200)
QUALITE = 78          # au-dessus, le gain visuel est nul et le poids monte
SEUIL_OCTETS = 40_000  # en dessous, une variante ne ferait pas gagner grand-chose


def variantes(nom):
    """Largeurs à produire pour une photo, selon sa largeur d'origine."""
    base, _ext = os.path.splitext(nom)
    chemin = os.path.join(SRC, nom)
    with Image.open(chemin) as im:
        w, h = im.size
    if os.path.getsize(chemin) < SEUIL_OCTETS:
        return w, h, []
    # Jamais d'agrandissement : une variante plus large que l'original
    # serait plus lourde pour une image plus floue.
    return w, h, [l for l in LARGEURS if l < w]


def main():
    force = "--force" in sys.argv
    faits = 0
    economie = 0
    for nom in sorted(os.listdir(SRC)):
        if not nom.endswith(".webp") or "-" in nom.rsplit("-", 1)[-1][:4] and nom.rsplit("-", 1)[-1][:-5].isdigit():
            pass
        if not nom.endswith(".webp"):
            continue
        racine = nom[:-5]
        if racine.rsplit("-", 1)[-1].isdigit() and int(racine.rsplit("-", 1)[-1]) in LARGEURS:
            continue  # c'est déjà une variante
        w, h, larg = variantes(nom)
        for l in larg:
            cible = os.path.join(SRC, "%s-%d.webp" % (racine, l))
            if os.path.exists(cible) and not force:
                continue
            with Image.open(os.path.join(SRC, nom)) as im:
                im = im.convert("RGB")
                im.thumbnail((l, 10 ** 6), Image.LANCZOS)
                im.save(cible, "WEBP", quality=QUALITE, method=6)
            faits += 1
            economie += os.path.getsize(os.path.join(SRC, nom)) - os.path.getsize(cible)
    print("%d variantes générées" % faits)
    if faits:
        print("économie cumulée face à l'original : %.0f Ko" % (economie / 1024))


if __name__ == "__main__":
    main()
