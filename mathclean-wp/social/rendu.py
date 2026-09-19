# -*- coding: utf-8 -*-
"""Capture les visuels sociaux définis dans les gabarits HTML de ce dossier.

    python3 social/rendu.py

Chaque élément .slide du gabarit devient un PNG dans social/out/, à sa taille
réelle de publication : 1080 × 1350 pour un carrousel Instagram, 1080 × 1920
pour une couverture TikTok. On capture l'élément lui-même plutôt que la
fenêtre, ce qui évite d'avoir à régler le cadrage à la main.
"""
import os
import sys
from playwright.sync_api import sync_playwright

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "out")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

GABARITS = [("carrousel-canape.html", "canape")]


def main():
    os.makedirs(SORTIE, exist_ok=True)
    faits = []
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME if os.path.exists(CHROME) else None)
        page = nav.new_page(viewport={"width": 1180, "height": 1400})
        for gabarit, prefixe in GABARITS:
            page.goto("file://" + os.path.join(ICI, gabarit))
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(400)
            for i, el in enumerate(page.query_selector_all(".slide"), 1):
                nom = el.get_attribute("id") or ("slide%d" % i)
                chemin = os.path.join(SORTIE, "%s-%s.png" % (prefixe, nom))
                el.screenshot(path=chemin)
                faits.append(chemin)
        nav.close()
    for f in faits:
        print("%-52s %7d o" % (os.path.relpath(f, ICI), os.path.getsize(f)))
    print("%d visuels dans %s" % (len(faits), os.path.relpath(SORTIE, ICI)))


if __name__ == "__main__":
    sys.exit(main())
