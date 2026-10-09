/* Fichier GÉNÉRÉ par build.py — ne pas modifier à la main.
   Toute correction se fait dans content.py, puis `python3 build.py`.
   C'est la grille que le Worker applique pour chiffrer un devis. */

export const TARIFS = {
  "packs": [
    {
      "nom": "Extérieur Éclat",
      "prix": 50
    },
    {
      "nom": "Intérieur Essentiel",
      "prix": 55
    },
    {
      "nom": "Intérieur Prestige",
      "prix": 100
    },
    {
      "nom": "Intégral",
      "prix": 130
    }
  ],
  "options": [
    {
      "nom": "Retrait des poils d'animaux",
      "prix": 10
    },
    {
      "nom": "Traitement cuir & alcantara",
      "prix": 20
    },
    {
      "nom": "Neutralisation des odeurs par ozone",
      "prix": 30
    }
  ],
  "textile": [
    {
      "nom": "Chaise / chaise de bureau",
      "prix": 15
    },
    {
      "nom": "Fauteuil",
      "prix": 25
    },
    {
      "nom": "Canapé 2 places",
      "prix": 39
    },
    {
      "nom": "Canapé 3 places",
      "prix": 49
    },
    {
      "nom": "Canapé d'angle",
      "prix": 69
    },
    {
      "nom": "Matelas 1 place",
      "prix": 39
    },
    {
      "nom": "Matelas 2 places",
      "prix": 49
    },
    {
      "nom": "Tapis jusqu'à 6 m²",
      "prix": 39
    },
    {
      "nom": "Tapis de plus de 6 m²",
      "prix": 59
    }
  ],
  "services": [
    {
      "slug": "nettoyage-hottes-paris",
      "nav": "Dégraissage de hottes",
      "univers": "devis"
    },
    {
      "slug": "nettoyage-regulier-paris",
      "nav": "Nettoyage d'entreprise",
      "univers": "devis"
    },
    {
      "slug": "nettoyage-appartement-paris",
      "nav": "Nettoyage d'appartement",
      "univers": "devis"
    },
    {
      "slug": "nettoyage-haute-pression-paris",
      "nav": "Nettoyage haute pression",
      "univers": "devis"
    },
    {
      "slug": "nettoyage-automobile-paris",
      "nav": "Nettoyage automobile",
      "univers": "auto"
    },
    {
      "slug": "nettoyage-textile-paris",
      "nav": "Nettoyage textile (canapé, matelas, tapis)",
      "univers": "textile"
    },
    {
      "slug": "nettoyage-vitres-paris",
      "nav": "Nettoyage de vitres",
      "univers": "devis"
    }
  ],
  "deplacement": {
    "lat": 48.9499461,
    "lon": 2.4559529,
    "palier_km": 5,
    "palier_eur": 5,
    "coef_route": 1.25
  }
};

export const COMMUNES = {"92200":[48.8846,2.2697],"92100":[48.8352,2.2409],"92300":[48.8939,2.288],"92800":[48.8846,2.2386],"92210":[48.8456,2.2189],"92500":[48.8768,2.1801],"78000":[48.8014,2.1301],"78100":[48.8989,2.0942],"92330":[48.7789,2.29],"78110":[48.8925,2.133],"93200":[48.9362,2.3574],"93300":[48.9146,2.3822],"93100":[48.8638,2.4485],"93500":[48.8944,2.409],"93000":[48.9106,2.4396],"93600":[48.9386,2.4938],"93150":[48.9386,2.4644],"93700":[48.9227,2.4453],"93160":[48.8486,2.5527],"92400":[48.8975,2.2567],"92130":[48.8239,2.273],"92000":[48.8924,2.2069],"94300":[48.8478,2.439],"94000":[48.7904,2.4556],"94200":[48.8133,2.3875],"75008":[48.8721,2.312],"75011":[48.858,2.3792],"75012":[48.8409,2.3876],"75015":[48.8412,2.3003],"75016":[48.8637,2.2769],"75017":[48.8872,2.322],"94100":[48.7994,2.4934],"93290":[48.9486,2.5697],"77500":[48.8797,2.5928],"77100":[48.9601,2.8785],"95100":[48.9474,2.2467],"95200":[48.9959,2.3785],"95000":[49.0361,2.0631],"91300":[48.7262,2.2825],"91000":[48.6238,2.4297],"92600":[48.905,2.285],"93400":[48.91,2.333],"93260":[48.879,2.419]};

export const DEPARTEMENTS = {"92":[48.86531,2.2498],"78":[48.86427,2.1191],"93":[48.90881,2.44288],"94":[48.81273,2.44388],"75":[48.86052,2.32967],"77":[48.9199,2.73565],"95":[48.99313,2.22943],"91":[48.675,2.3561]};
