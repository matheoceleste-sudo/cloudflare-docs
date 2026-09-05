# -*- coding: utf-8 -*-
"""
Contenu éditorial du site MathClean.

Tout le texte, les tarifs et les listes de villes vivent ici : `build.py` ne
contient que les gabarits. Pour modifier le site, on édite ce fichier puis on
relance `python3 build.py`.
"""

# --- Identité de l'entreprise ---------------------------------------------
SITE = {
    "name": "MathClean",
    "slogan": "Une exigence de roi",
    "baseline": "Entreprise de nettoyage à Paris & en Île-de-France",
    "url": "https://mathclean.fr",
    "phone": "06 23 07 52 59",
    "phone_link": "+33623075259",
    "email": "matheoceleste@gmail.com",
    "form_action": "https://formsubmit.co/matheoceleste@gmail.com",
    "address": "5 Rue Nicolas Copernic",
    "postcode": "93290",
    "city": "Tremblay-en-France",
    "lat": 48.9486,
    "lon": 2.5697,
    "siret": "924 565 990 00010",
    "siren": "924 565 990",
    "manager": "Mathéo Céleste",
    "hours": "7j/7, de 8h à 20h",
    # Fiche Google Business (CID issu de l'URL Maps fournie par le client).
    "google_cid": "8434710860473546146",
    "maps_url": "https://www.google.com/maps/place/MathClean/@48.9499461,2.4559529,17z",
    "review_url": "https://www.google.com/maps?cid=8434710860473546146",
    "directions_url": "https://www.google.com/maps/dir/?api=1&destination=MathClean&destination_place_id=",
    "travel_fee": "5 € par tranche de 5 km depuis notre atelier de Tremblay-en-France (93)",
}

# --- Prestations ----------------------------------------------------------
# Chaque entrée génère une page dans /services/ et une carte sur l'accueil.
SERVICES = [
    {
        "slug": "nettoyage-automobile-paris",
        "short": "Automobile",
        "nav": "Nettoyage automobile",
        "name": "Nettoyage automobile à Paris",
        "h1": "Nettoyage automobile à domicile à Paris & en Île-de-France",
        "title": "Nettoyage automobile à Paris — detailing à domicile dès 40 € | MathClean",
        "meta": "Detailing automobile intérieur et extérieur à domicile à Paris et en Île-de-France. Aspiration, shampoing des sièges, vapeur, cuir. Dès 40 €, 7j/7.",
        "price": "dès 40 €",
        "excerpt": "Detailing intérieur et extérieur à domicile. Aspiration, shampoing des sièges, vapeur haute température, plastiques et vitres — votre voiture retrouve son aspect showroom.",
        "image": "auto-interieur-vw.webp",
        "hero": "auto-interieur-vw.webp",
        "icon": "car",
        "intro": [
            "Nous nous déplaçons avec notre matériel, notre eau et notre électricité : rien à fournir de votre côté. "
            "L'intervention se fait devant chez vous, en parking souterrain, sur votre place de résidence ou sur votre lieu de travail, "
            "à Paris comme dans les huit départements franciliens.",
            "Le nettoyage automobile, ou <em>detailing</em>, n'est pas un lavage de station. Chaque matière — cuir pleine fleur, alcantara, "
            "tissu, plastique moussé, vernis — appelle un produit et un geste différents. C'est ce diagnostic préalable qui évite "
            "les auréoles sur un tissu clair, les traces blanches sur un plastique noir ou le dessèchement d'un cuir.",
        ],
        "included_title": "Ce que comprend une prestation sans option",
        "included": [
            "Aspiration complète de l'habitacle <strong>et du coffre</strong>, sans supplément",
            "Shampoing des tapis et des moquettes",
            "Désinfection des allergènes et acariens par vapeur haute température",
            "Traitement des sièges, du volant, des tapis et de toutes les surfaces planes",
            "Nettoyage des vitres intérieures, sans trace",
        ],
        "steps": [
            ("Diagnostic", "Nous faisons le tour du véhicule avec vous : nature des salissures, matériaux, points sensibles, et le pack qui correspond réellement à votre besoin."),
            ("Préparation", "Décontamination et pré-traitement des taches. Les zones fragiles — écrans, boiseries, garnitures — sont protégées avant toute projection."),
            ("Traitement", "Aspiration, injection-extraction sur les textiles, vapeur sèche sur les surfaces dures, produits adaptés aux cuirs et à l'alcantara."),
            ("Contrôle", "Nous refaisons le tour du véhicule avec vous avant de partir. Le règlement se fait après l'intervention, une fois le résultat constaté."),
        ],
        "faq": [
            ("Combien de temps dure un nettoyage automobile ?",
             "Comptez 1 h 30 pour un Extérieur Éclat ou un Intérieur Essentiel, 3 h pour un Intérieur Prestige et jusqu'à 4 h pour un Intégral sur un grand véhicule. Les durées exactes figurent sur notre page tarifs."),
            ("Avez-vous besoin d'une prise électrique ou d'un point d'eau ?",
             "Non. Nous venons entièrement autonomes en eau et en électricité, ce qui nous permet d'intervenir en parking souterrain, en pied d'immeuble ou sur un parking d'entreprise."),
            ("Faites-vous le nettoyage avant une revente ?",
             "C'est une de nos demandes les plus fréquentes. Le pack Intérieur Prestige, associé à l'option de neutralisation des odeurs par ozone, permet de présenter un véhicule sans odeur d'animal ni de tabac — un point qui pèse lourd à la revente."),
            ("Le prix dépend-il de la taille du véhicule ?",
             "Oui. Chaque pack affiche une fourchette : le bas correspond à une citadine, le haut à un SUV ou un monospace. Le tarif exact vous est confirmé avant l'intervention."),
        ],
    },
    {
        "slug": "nettoyage-textile-paris",
        "short": "Textile",
        "nav": "Nettoyage textile (canapé, matelas, tapis)",
        "name": "Nettoyage textile à Paris",
        "h1": "Nettoyage de canapé, matelas et tapis à domicile",
        "title": "Nettoyage canapé, matelas & tapis à Paris — injection-extraction | MathClean",
        "meta": "Nettoyage de canapé, matelas, tapis et fauteuil à domicile à Paris et en Île-de-France. Injection-extraction, détachage, anti-acariens. Dès 15 €.",
        "price": "dès 15 €",
        "excerpt": "Canapé, matelas, tapis, fauteuil et moquette : injection-extraction, détachage ciblé et traitement anti-acariens, directement chez vous.",
        "image": "canape-nettoyage.webp",
        "hero": "canape-nettoyage.webp",
        "icon": "sofa",
        "intro": [
            "Un canapé d'angle ne se démonte pas et ne part pas au pressing. C'est précisément pour cela que nous venons chez vous, "
            "avec des machines professionnelles d'injection-extraction qui traitent la fibre en profondeur sans détremper la mousse.",
            "Le principe : une solution nettoyante est injectée sous pression au cœur du textile, puis immédiatement réaspirée avec la "
            "saleté dissoute. Le tissu ressort nettoyé, pas gorgé d'eau — c'est ce qui évite les auréoles au séchage. Comptez 4 à 6 h "
            "de séchage selon la ventilation de la pièce.",
        ],
        "included_title": "Ce que nous traitons",
        "included": [
            "Canapés en tissu et en cuir, du 2 places au canapé d'angle",
            "Fauteuils, chaises et chaises de bureau",
            "Matelas 1 et 2 places, traités <strong>sur les deux faces</strong>",
            "Tapis et moquettes, avec test des couleurs préalable",
            "Détachage ciblé : café, gras, vin, encre, urine, sang",
        ],
        "steps": [
            ("Test de la fibre", "Laine, soie, viscose, synthétique ou cuir : nous identifions la matière et testons la solidité des couleurs sur une zone cachée avant de commencer."),
            ("Pré-traitement", "Aspiration profonde, puis application ciblée sur les taches, avec un temps de pause pour dissoudre les corps gras."),
            ("Injection-extraction", "Passages croisés jusqu'à ce que l'eau réaspirée ressorte claire. Sur les matelas, les deux faces sont traitées."),
            ("Anti-acariens & séchage", "Traitement haute température des allergènes, puis ventilation. Le textile est réutilisable après 4 à 6 h."),
        ],
        "faq": [
            ("Mon canapé sera-t-il trempé après l'intervention ?",
             "Non. L'injection-extraction réaspire immédiatement la solution injectée : le textile ressort humide, pas mouillé. Il est de nouveau utilisable après 4 à 6 h selon la ventilation de la pièce."),
            ("Les taches anciennes partent-elles ?",
             "Souvent oui, mais nous ne le promettons jamais à l'aveugle. Une tache incrustée depuis des mois, une auréole déjà créée par un détachant ménager ou une décoloration ne réagissent pas comme une tache fraîche. Nous vous disons ce qui est réaliste avant de commencer."),
            ("Les produits sont-ils sans danger pour mes enfants et mes animaux ?",
             "Oui. Nous choisissons des produits sûrs pour les enfants et les animaux domestiques, et nous nous en passons complètement quand la vapeur haute température suffit."),
            ("Intervenez-vous sur le cuir ?",
             "Oui, avec un protocole différent : nettoyage doux puis nourrissage du cuir. L'injection-extraction est réservée aux textiles."),
        ],
    },
    {
        "slug": "nettoyage-bateau-paris",
        "short": "Bateau",
        "nav": "Nettoyage de bateau",
        "name": "Nettoyage de bateau à Paris",
        "h1": "Nettoyage de bateau à quai, en Île-de-France et en mer",
        "title": "Nettoyage de bateau à Paris & Île-de-France — coque, pont, sellerie | MathClean",
        "meta": "Nettoyage et lustrage de bateau à quai : coque, pont et sellerie. Seine, Marne et ports de plaisance. Devis gratuit, produits biodégradables.",
        "price": "sur devis",
        "excerpt": "Coque lustrée, pont lavé, sellerie nettoyée et protégée : votre bateau retrouve son éclat, sur la Seine, la Marne comme en mer.",
        "image": "bateau-yacht.webp",
        "hero": "bateau-yacht.webp",
        "icon": "boat",
        "intro": [
            "Un bateau vit dehors toute l'année : dépôts verts sur le gelcoat, ligne de flottaison marquée, sellerie qui grise, teck qui noircit. "
            "Nous intervenons directement à quai, sur la Seine, la Marne et dans les ports de plaisance franciliens.",
            "Nous travaillons exclusivement avec des produits biodégradables : ce qui part à l'eau lors du rinçage finit dans le milieu aquatique. "
            "C'est une contrainte technique autant qu'une règle, et elle conditionne le choix des solutions employées sur la coque.",
        ],
        "included_title": "Ce que couvre une intervention nautique",
        "included": [
            "Lavage de la coque et traitement de la ligne de flottaison",
            "Lustrage et protection du gelcoat",
            "Pont, passavants et cockpit dégraissés",
            "Sellerie extérieure nettoyée, désinfectée et protégée",
            "Aménagement intérieur, carré et cabines sur demande",
        ],
        "steps": [
            ("Visite", "Nous passons voir le bateau à quai, ou vous nous envoyez des photos. C'est ce qui permet un devis ferme plutôt qu'une fourchette."),
            ("Devis ferme", "Le devis est détaillé poste par poste — coque, pont, sellerie, intérieur — et nous nous y tenons."),
            ("Intervention", "À quai, avec notre propre matériel et des produits biodégradables adaptés au gelcoat, à l'inox et au teck."),
            ("Protection", "Application d'une protection sur le gelcoat et la sellerie pour espacer les nettoyages suivants."),
        ],
        "faq": [
            ("Intervenez-vous en dehors de l'Île-de-France ?",
             "Notre zone habituelle couvre la Seine, la Marne et les ports franciliens. Pour un déplacement en bord de mer, parlons-en : c'est possible, mais cela se chiffre au cas par cas."),
            ("Faut-il sortir le bateau de l'eau ?",
             "Non pour le pont, la sellerie et l'intérieur. Pour un traitement complet de la carène sous la ligne de flottaison, un passage au sec est nécessaire."),
            ("Pourquoi n'y a-t-il pas de tarif affiché ?",
             "Parce qu'un semi-rigide de 6 mètres et un bateau habitable de 12 mètres n'ont rien à voir. Nous établissons un devis gratuit après avoir vu le bateau ou des photos."),
        ],
    },
    {
        "slug": "nettoyage-terrasse-paris",
        "short": "Terrasse",
        "nav": "Nettoyage de terrasse",
        "name": "Nettoyage de terrasse à Paris",
        "h1": "Nettoyage de terrasse : haute pression maîtrisée & anti-mousse",
        "title": "Nettoyage de terrasse à Paris — haute pression, anti-mousse, bois | MathClean",
        "meta": "Nettoyage de terrasse à Paris et en Île-de-France : haute pression maîtrisée, anti-mousse, saturateur bois. Dalles, pierre, béton, carrelage. Devis gratuit.",
        "price": "sur devis",
        "excerpt": "Terrasses, dalles, pierre et bois : haute pression réglée selon le support, traitement anti-mousse et hydrofuge en finition.",
        "image": "ba-terrasse2-apres.webp",
        "hero": "ba-terrasse2-apres.webp",
        "icon": "deck",
        "intro": [
            "Sur une terrasse, la pression n'est pas un réglage unique : c'est la variable la plus importante du chantier. Le béton, la pierre "
            "et le carrelage encaissent une pression élevée. Le bois, non — une lance trop puissante ouvre la fibre, la rend pelucheuse et "
            "accélère durablement le grisaillement.",
            "Nous adaptons donc le geste au support : haute pression maîtrisée sur les surfaces minérales, brossage doux suivi d'un anti-mousse "
            "sur le bois, puis saturateur ou hydrofuge en finition pour espacer la repousse et limiter la reprise d'humidité.",
        ],
        "included_title": "Les supports que nous traitons",
        "included": [
            "Dalles, pavés, béton désactivé et béton lissé",
            "Pierre naturelle, marbre et travertin",
            "Carrelage extérieur et grès cérame",
            "Bois exotique et pin traité, en brossage doux",
            "Murets, escaliers et abords, inclus dans le devis",
        ],
        "steps": [
            ("Identification du support", "Nous déterminons le matériau et son état. C'est ce qui fixe la pression, la buse et le produit — pas l'inverse."),
            ("Anti-mousse", "Application d'un traitement qui tue la mousse et le lichen à la racine, avec un temps de pose avant rinçage."),
            ("Nettoyage", "Haute pression réglée sur les surfaces minérales, brossage doux sur le bois, rinçage complet des abords."),
            ("Protection", "Saturateur sur le bois, hydrofuge sur la pierre poreuse : la terrasse reste propre plus longtemps."),
        ],
        "faq": [
            ("La haute pression abîme-t-elle une terrasse en bois ?",
             "Oui, si elle est mal réglée : elle ouvre la fibre et la lame devient rugueuse. C'est pour cette raison que nous privilégions le brossage doux sur bois, suivi d'un anti-mousse puis d'un saturateur."),
            ("À quelle fréquence faut-il nettoyer une terrasse ?",
             "Un passage annuel, idéalement au printemps, suffit dans la plupart des cas. Sur une terrasse ombragée ou sous des arbres, deux passages par an évitent que la mousse ne s'installe."),
            ("Faut-il un point d'eau chez moi ?",
             "Non, nous venons avec notre propre réserve d'eau et notre groupe électrogène."),
        ],
    },
    {
        "slug": "nettoyage-vitres-paris",
        "short": "Vitres",
        "nav": "Nettoyage de vitres",
        "name": "Nettoyage de vitres à Paris",
        "h1": "Nettoyage de vitres à l'eau osmosée, sans trace",
        "title": "Nettoyage de vitres à Paris — eau osmosée, sans trace | MathClean",
        "meta": "Nettoyage de vitres, baies vitrées, vérandas et vitrines à Paris et en Île-de-France. Eau osmosée, résultat sans trace. Devis gratuit, 7j/7.",
        "price": "sur devis",
        "excerpt": "Fenêtres, baies vitrées, vérandas et vitrines nettoyées à l'eau osmosée : sans minéraux, l'eau sèche sans rien déposer.",
        "image": "vitre-controle.webp",
        "hero": "vitre-controle.webp",
        "icon": "window",
        "intro": [
            "Les traces sur une vitre viennent presque toujours de trois choses : l'eau du robinet, très calcaire en Île-de-France, qui dépose "
            "un voile blanc en séchant ; les produits ménagers, dont les tensioactifs laissent un film qui resalit vite ; et le plein soleil, "
            "qui fait sécher l'eau avant qu'on ait pu la racler.",
            "L'eau osmosée règle le problème à la source. Débarrassée de ses minéraux, elle sèche sans rien déposer : aucun produit n'est "
            "nécessaire, donc aucun film résiduel. C'est la méthode que nous employons sur les grandes surfaces, les vérandas et les vitrines.",
        ],
        "included_title": "Ce que nous nettoyons",
        "included": [
            "Fenêtres, ouvrants et dormants, intérieur et extérieur",
            "Baies vitrées et grandes surfaces sans reprise de trace",
            "Vérandas et verrières, y compris en toiture",
            "Vitrines de commerce, en passage ponctuel ou régulier",
            "Encadrements, rails et appuis dégraissés",
        ],
        "steps": [
            ("Repérage", "Nombre d'ouvrants, hauteur, accessibilité : ces trois points déterminent le matériel et le devis."),
            ("Dégraissage", "Encadrements, rails et appuis d'abord — nettoyer la vitre avant le cadre revient à la resalir aussitôt."),
            ("Eau osmosée", "Brossage et rinçage à l'eau pure, sans détergent, y compris sur perche télescopique en hauteur."),
            ("Contrôle en lumière rasante", "Le seul contrôle fiable : on regarde la vitre de biais, à contre-jour, pour vérifier qu'aucun voile ne subsiste."),
        ],
        "faq": [
            ("Qu'est-ce que l'eau osmosée ?",
             "De l'eau filtrée par osmose inverse, débarrassée de son calcaire et de ses minéraux. En séchant, elle ne dépose rien : c'est ce qui permet de se passer de produit et d'obtenir une vitre sans trace."),
            ("Intervenez-vous en hauteur ?",
             "Oui, à la perche télescopique jusqu'à plusieurs étages. Au-delà, ou en cas d'accès difficile, nous vous le disons franchement lors du devis."),
            ("À quelle fréquence pour une vitrine de commerce ?",
             "Un passage hebdomadaire ou bimensuel selon l'exposition à la rue. Nous établissons un forfait pour les passages réguliers."),
        ],
    },
    {
        "slug": "nettoyage-entreprise-paris",
        "short": "Entreprise",
        "nav": "Nettoyage pour entreprise",
        "name": "Nettoyage pour entreprise à Paris",
        "h1": "Nettoyage pour entreprise : bureaux, commerces et locaux",
        "title": "Nettoyage pour entreprise à Paris — bureaux, commerces, locaux | MathClean",
        "meta": "Nettoyage pour entreprise à Paris et en Île-de-France : bureaux, commerces, restaurants et locaux d'activité. Passage ponctuel ou régulier, horaires décalés, facturation entreprise.",
        "price": "sur devis",
        "excerpt": "Bureaux, commerces, restaurants et locaux d'activité : désinfection, moquettes, sanitaires et vitrerie, en passage ponctuel ou régulier.",
        "image": "bureau-entreprise.webp",
        "hero": "bureau-entreprise.webp",
        "icon": "building",
        "intro": [
            "Un local professionnel ne se nettoie pas aux mêmes heures qu'un logement. Nous intervenons tôt le matin, tard le soir ou de nuit "
            "pour les commerces et les restaurants qui ne peuvent pas fermer en journée — l'espace est opérationnel dès l'ouverture.",
            "Nous travaillons en passage ponctuel, par exemple pour une remise à niveau avant un contrôle d'hygiène, comme en passage régulier "
            "avec un protocole écrit et une facturation entreprise.",
        ],
        "included_title": "Nos interventions professionnelles",
        "included": [
            "Postes de travail, espaces d'accueil et salles de réunion",
            "Sanitaires : désinfection complète et réapprovisionnement",
            "Moquettes et sols durs, en injection-extraction ou monobrosse",
            "Vitrerie intérieure et extérieure",
            "Cuisines professionnelles : dégraissage vapeur, plancha, hottes, joints",
        ],
        "steps": [
            ("Visite des locaux", "Nous venons sur place mesurer les surfaces et repérer les contraintes d'accès et d'horaires."),
            ("Protocole écrit", "Fréquence, zones, produits et créneaux : tout est écrit avant de commencer, pour que chacun sache ce qui est fait."),
            ("Intervention", "En horaires décalés si nécessaire, sans gêner votre activité ni vos clients."),
            ("Suivi", "Un interlocuteur unique, joignable après chaque passage, et un ajustement du protocole si vos besoins changent."),
        ],
        "faq": [
            ("Proposez-vous un contrat régulier ?",
             "Oui, en passage quotidien, hebdomadaire ou mensuel, avec un protocole écrit et une facturation entreprise. Le devis est établi après visite des locaux."),
            ("Intervenez-vous en dehors des heures d'ouverture ?",
             "Oui. C'est même la règle pour les commerces et les restaurants : nous travaillons tôt le matin, tard le soir ou de nuit."),
            ("Faites-vous le dégraissage de cuisine professionnelle ?",
             "Oui, à la vapeur haute température : elle décolle la graisse cuite sans produit chimique agressif, ce qui est un avantage réel dans un environnement alimentaire."),
        ],
    },
    {
        "slug": "nettoyage-fin-de-chantier-paris",
        "short": "Fin de chantier",
        "nav": "Fin de chantier",
        "name": "Nettoyage fin de chantier à Paris",
        "h1": "Nettoyage de fin de chantier et remise en état après travaux",
        "title": "Nettoyage fin de chantier à Paris — remise en état après travaux | MathClean",
        "meta": "Nettoyage de fin de chantier à Paris et en Île-de-France : dépoussiérage, retrait des résidus, vitres, sols. Logement ou local prêt à livrer. Devis gratuit.",
        "price": "sur devis",
        "excerpt": "Dépoussiérage complet, évacuation des résidus, lavage des vitres et des sols : votre bien est prêt à vivre ou à livrer après travaux.",
        "image": "intervention-1.webp",
        "hero": "intervention-1.webp",
        "icon": "tools",
        "intro": [
            "La poussière de chantier ne se comporte pas comme la poussière domestique : fine, chargée de plâtre et de silice, elle se redépose "
            "en continu pendant plusieurs jours. Un seul passage ne suffit jamais, et c'est ce qui distingue un vrai nettoyage de fin de chantier "
            "d'un coup de balai.",
            "Nous travaillons de haut en bas et par pièces closes, avec des aspirateurs à filtration fine, pour éviter de remettre en suspension "
            "ce qui vient d'être retiré. Résidus de colle, projections de peinture, étiquettes et films de protection sont traités un par un.",
        ],
        "included_title": "Le déroulé d'une remise en état",
        "included": [
            "Retrait des résidus, gravats fins et protections de chantier",
            "Dépoussiérage haut : plafonds, luminaires, conduits, angles",
            "Décollage des projections de peinture, colle, silicone et étiquettes",
            "Vitres, encadrements et rails intégralement nettoyés",
            "Sols lavés en profondeur, sanitaires et cuisine désinfectés",
        ],
        "steps": [
            ("État des lieux", "Nous chiffrons sur place : surface, nature des travaux et volume de résidus déterminent le devis."),
            ("Gros nettoyage", "Évacuation des résidus et dépoussiérage haut, pièce par pièce, en travaillant toujours de haut en bas."),
            ("Détail", "Décollage des projections, traitement des menuiseries, des vitres et de la robinetterie."),
            ("Finition", "Lavage des sols, désinfection des points d'eau et contrôle final avec vous ou avec le maître d'ouvrage."),
        ],
        "faq": [
            ("Intervenez-vous pour les artisans et les agences ?",
             "Oui, régulièrement : entreprises du bâtiment, architectes d'intérieur, agences immobilières et syndics. Facturation entreprise, devis ferme."),
            ("Faut-il un ou deux passages ?",
             "Sur un chantier important, deux passages sont souvent nécessaires : un gros nettoyage, puis une finition quelques jours plus tard, une fois la poussière résiduelle retombée. Nous vous le disons dès le devis."),
            ("Évacuez-vous les gravats ?",
             "Nous évacuons les résidus fins et les protections de chantier. L'évacuation de gravats lourds relève d'une benne, à prévoir séparément."),
        ],
    },
]

# --- Tarifs ---------------------------------------------------------------
PACKS_AUTO = [
    ("Extérieur Éclat", 40, 90, "Extérieur", "La carrosserie retrouve sa brillance", False,
     ["Lavage complet de la carrosserie", "Jantes et passages de roues", "Brillant pneus",
      "Vitres extérieures", "Séchage sans trace"]),
    ("Intérieur Essentiel", 50, 120, "Intérieur", "Idéal pour un coup de propre régulier (hors cuir et alcantara)", False,
     ["Aspiration de l'habitacle et du coffre", "Nettoyage du tableau de bord", "Nettoyage des plastiques",
      "Vitres intérieures", "Désinfection complète à la vapeur", "Parfum d'ambiance"]),
    ("Intérieur Prestige", 90, 180, "Intérieur", "Le détail poussé jusqu'au moindre recoin, cuir compris", True,
     ["Tout l'Intérieur Essentiel", "Sièges cuir nettoyés ou pressing des sièges tissu",
      "Pressing des tapis et moquettes", "Protection des plastiques", "Traitement des cuirs",
      "Battements de portes", "Ciel de toit", "Compartiment de la roue de secours"]),
    ("Intégral", 120, 240, "Intérieur + Extérieur", "Le véhicule entier, dedans comme dehors", False,
     ["Tout l'Intérieur Prestige", "Lavage complet de la carrosserie", "Jantes et brillant pneus",
      "Vitres intérieures et extérieures", "Séchage sans trace", "Parfum d'ambiance"]),
]

OPTIONS_AUTO = [
    ("Retrait des poils d'animaux", 10, "Sièges, tapis et moquettes"),
    ("Traitement cuir & alcantara", 20, "Nettoyage puis nourrissage des cuirs et de l'alcantara"),
    ("Neutralisation des odeurs par ozone", 30, "Traitement d'1 h : odeurs, bactéries et moisissures éliminées"),
]

TARIFS_TEXTILE = [
    ("Chaise / chaise de bureau", 15, "Assise et dossier"),
    ("Fauteuil", 25, "Assise, dossier et accoudoirs"),
    ("Canapé 2 places", 39, "Injection-extraction et détachage"),
    ("Canapé 3 places", 49, "Injection-extraction et détachage"),
    ("Canapé d'angle", 69, "Injection-extraction et détachage"),
    ("Matelas 1 place", 39, "Deux faces, traitement anti-acariens"),
    ("Matelas 2 places", 49, "Deux faces, traitement anti-acariens"),
    ("Tapis jusqu'à 6 m²", 39, "Lavage des fibres en profondeur"),
    ("Tapis de plus de 6 m²", 59, "Lavage des fibres en profondeur"),
]

TARIFS_DEVIS = [
    ("Nettoyage de bateau", "Coque, pont et sellerie", "nettoyage-bateau-paris"),
    ("Nettoyage de terrasse", "Haute pression et anti-mousse", "nettoyage-terrasse-paris"),
    ("Nettoyage de vitres", "Vitres, baies vitrées et vitrines", "nettoyage-vitres-paris"),
    ("Nettoyage pour entreprise", "Bureaux, commerces, locaux et vitrerie", "nettoyage-entreprise-paris"),
    ("Nettoyage de fin de chantier", "Remise en état après travaux", "nettoyage-fin-de-chantier-paris"),
]

# --- Zones d'intervention -------------------------------------------------
ZONES = [
    {
        "slug": "paris-75", "num": "75", "name": "Paris",
        "intro": "Du 1er au 20e arrondissement, nous intervenons à domicile comme en entreprise. "
                 "Cours d'immeuble, parkings souterrains et rues étroites : notre matériel autonome en eau "
                 "et en électricité nous permet de travailler là où un centre de lavage ne peut pas.",
        "focus": "À Paris intra-muros, l'essentiel de notre activité tourne autour du textile — canapés d'angle "
                 "qu'on ne peut ni démonter ni transporter, matelas et tapis — et du nettoyage automobile en "
                 "parking résidentiel. Côté professionnels, nous entretenons bureaux, commerces et restaurants "
                 "en horaires décalés.",
        "cities": ["Paris 1er", "Paris 6e", "Paris 7e", "Paris 8e", "Paris 9e", "Paris 11e",
                   "Paris 12e", "Paris 14e", "Paris 15e", "Paris 16e", "Paris 17e", "Paris 20e"],
    },
    {
        "slug": "hauts-de-seine-92", "num": "92", "name": "Hauts-de-Seine",
        "intro": "De Boulogne-Billancourt à Nanterre, en passant par Neuilly-sur-Seine et Levallois-Perret, "
                 "nous couvrons l'ensemble du département, pavillons comme immeubles de bureaux.",
        "focus": "Le 92 concentre une forte demande en detailing automobile à domicile et en entretien de "
                 "bureaux. La Défense et les pôles tertiaires d'Issy-les-Moulineaux ou de Courbevoie nous "
                 "sollicitent régulièrement pour la vitrerie et l'entretien des moquettes.",
        "cities": ["Boulogne-Billancourt", "Neuilly-sur-Seine", "Levallois-Perret", "Courbevoie",
                   "Nanterre", "Issy-les-Moulineaux", "Rueil-Malmaison", "Clamart", "Antony",
                   "Asnières-sur-Seine", "Suresnes", "Meudon"],
    },
    {
        "slug": "seine-saint-denis-93", "num": "93", "name": "Seine-Saint-Denis",
        "intro": "C'est notre département : notre atelier se trouve à Tremblay-en-France. De Saint-Denis à "
                 "Montreuil, d'Aubervilliers à Noisy-le-Grand, nous y sommes les plus réactifs — et les frais "
                 "de déplacement y sont, mécaniquement, les plus faibles.",
        "focus": "Le 93 est un territoire en pleine transformation, avec de nombreux programmes immobiliers "
                 "neufs, bureaux et ateliers. Notre prestation de fin de chantier accompagne cette dynamique. "
                 "À domicile, l'injection-extraction sur canapés, matelas et tapis et le detailing automobile "
                 "constituent l'essentiel des demandes.",
        "cities": ["Saint-Denis", "Montreuil", "Aubervilliers", "Aulnay-sous-Bois", "Drancy",
                   "Noisy-le-Grand", "Bobigny", "Bondy", "Le Blanc-Mesnil", "Pantin",
                   "Rosny-sous-Bois", "Épinay-sur-Seine", "Tremblay-en-France"],
    },
    {
        "slug": "val-de-marne-94", "num": "94", "name": "Val-de-Marne",
        "intro": "De Créteil à Vincennes, de Vitry-sur-Seine à Saint-Maur-des-Fossés, nous intervenons dans "
                 "tout le Val-de-Marne, chez les particuliers comme dans les locaux professionnels.",
        "focus": "Les bords de Marne nous amènent une part notable de nos interventions nautiques, à quai. "
                 "Côté domicile, les pavillons de Saint-Maur, Nogent et Le Perreux sollicitent surtout le "
                 "nettoyage de terrasse et le textile.",
        "cities": ["Créteil", "Vitry-sur-Seine", "Champigny-sur-Marne", "Saint-Maur-des-Fossés",
                   "Ivry-sur-Seine", "Villejuif", "Vincennes", "Maisons-Alfort",
                   "Fontenay-sous-Bois", "Nogent-sur-Marne", "Charenton-le-Pont", "Le Perreux-sur-Marne"],
    },
    {
        "slug": "essonne-91", "num": "91", "name": "Essonne",
        "intro": "D'Évry-Courcouronnes à Massy, de Palaiseau à Corbeil-Essonnes, nous nous déplaçons dans "
                 "tout le département. Les délais y sont généralement de 48 à 72 h.",
        "focus": "L'habitat pavillonnaire de l'Essonne fait la part belle au nettoyage de terrasse — bois, "
                 "dalles et pierre — et au detailing automobile à domicile, souvent avant une revente.",
        "cities": ["Évry-Courcouronnes", "Massy", "Savigny-sur-Orge", "Sainte-Geneviève-des-Bois",
                   "Athis-Mons", "Palaiseau", "Viry-Châtillon", "Corbeil-Essonnes", "Draveil",
                   "Yerres", "Brunoy", "Montgeron"],
    },
    {
        "slug": "yvelines-78", "num": "78", "name": "Yvelines",
        "intro": "De Versailles à Mantes-la-Jolie, de Saint-Germain-en-Laye à Montigny-le-Bretonneux, nous "
                 "couvrons les Yvelines pour les particuliers et les entreprises.",
        "focus": "Les Yvelines nous sollicitent particulièrement pour le nettoyage de terrasse en pierre et "
                 "en bois exotique, le textile de belle facture — tapis de laine, selleries cuir — et "
                 "l'entretien de locaux professionnels sur les pôles de Saint-Quentin-en-Yvelines.",
        "cities": ["Versailles", "Sartrouville", "Mantes-la-Jolie", "Saint-Germain-en-Laye", "Poissy",
                   "Conflans-Sainte-Honorine", "Montigny-le-Bretonneux", "Trappes", "Les Mureaux",
                   "Houilles", "Chatou", "Le Chesnay-Rocquencourt"],
    },
    {
        "slug": "seine-et-marne-77", "num": "77", "name": "Seine-et-Marne",
        "intro": "De Chelles à Meaux, de Melun à Fontainebleau, nous intervenons dans tout le département, "
                 "y compris sur les villes nouvelles de Marne-la-Vallée.",
        "focus": "Le 77 est le plus vaste département francilien : nous y groupons volontiers plusieurs "
                 "interventions sur une même journée, ce qui reste le meilleur moyen de contenir les frais "
                 "de déplacement. Terrasses, textile et fin de chantier y dominent.",
        "cities": ["Chelles", "Meaux", "Melun", "Pontault-Combault", "Champs-sur-Marne", "Torcy",
                   "Bussy-Saint-Georges", "Lagny-sur-Marne", "Roissy-en-Brie", "Ozoir-la-Ferrière",
                   "Fontainebleau", "Provins"],
    },
    {
        "slug": "val-doise-95", "num": "95", "name": "Val-d'Oise",
        "intro": "D'Argenteuil à Cergy, de Sarcelles à Pontoise, le Val-d'Oise fait partie de notre zone "
                 "proche : notre atelier de Tremblay-en-France se trouve à quelques kilomètres.",
        "focus": "Proximité oblige, nous y intervenons souvent sous 24 à 48 h. Detailing automobile à "
                 "domicile, injection-extraction sur textile et remise en état après travaux constituent "
                 "l'essentiel de nos passages dans le 95.",
        "cities": ["Argenteuil", "Sarcelles", "Cergy", "Garges-lès-Gonesse", "Franconville", "Pontoise",
                   "Ermont", "Bezons", "Herblay-sur-Seine", "Eaubonne", "Goussainville", "Gonesse"],
    },
]

# --- Engagements ----------------------------------------------------------
ENGAGEMENTS = [
    ("calendar", "Intervention 7j/7",
     "Week-ends et jours fériés compris. Pour les commerces et les restaurants, nous travaillons aussi en soirée ou de nuit, sans gêner votre activité."),
    ("quote", "Devis gratuit et ferme",
     "Une estimation claire, détaillée poste par poste, gratuite et sans engagement. Le tarif annoncé est celui que vous payez."),
    ("clock", "Intervention rapide",
     "Sous 24 à 48 h à Paris et en petite couronne, sous 48 à 72 h en grande couronne. Délais confirmés lors de la prise de rendez-vous."),
    ("shield", "Produits sans danger",
     "Choisis pour ne pas agresser les matériaux, et sûrs pour les enfants comme pour les animaux. Quand la vapeur suffit, nous nous en passons."),
    ("truck", "Nous venons équipés",
     "Machines, produits, eau et électricité. Vous n'avez ni prise ni point d'eau à fournir : nous intervenons en parking, en pied d'immeuble ou à quai."),
    ("wallet", "Aucun acompte",
     "Vous réglez après l'intervention, une fois le résultat constaté avec vous. Espèces, carte bancaire ou virement."),
]

# --- Avant / après --------------------------------------------------------
BEFORE_AFTER = [
    ("avant-voiture-siege.webp", "apres-voiture-siege.webp", "Siège automobile", "Shampoing et détachage des tissus"),
    ("ba-canape-avant.webp", "ba-canape-apres.webp", "Canapé en tissu", "Injection-extraction et désinfection"),
    ("ba-terrasse2-avant.webp", "ba-terrasse2-apres.webp", "Terrasse en marbre", "Haute pression : la pierre retrouve sa blancheur"),
    ("avant-plan-travail.webp", "apres-plan-travail.webp", "Plan de travail", "Dégraissage et désinfection en profondeur"),
    ("avant-frigo.webp", "apres-frigo.webp", "Réfrigérateur professionnel", "Nettoyage complet, hygiène alimentaire"),
    ("ba-tapis-avant.webp", "ba-tapis-apres.webp", "Tapis et moquette", "Shampoing et détachage en profondeur"),
    ("ba-terrasse-avant.webp", "ba-terrasse-apres.webp", "Terrasse extérieure", "Haute pression et traitement anti-mousse"),
    ("ba-fauteuil-avant.webp", "ba-fauteuil-apres.webp", "Fauteuil de bureau", "Détachage et assainissement des tissus"),
]

# --- FAQ générale ---------------------------------------------------------
FAQ = [
    ("Combien coûte un nettoyage automobile ?",
     "Les packs démarrent à 40 € pour un Extérieur Éclat sur citadine et vont jusqu'à 240 € pour un Intégral sur "
     "un grand véhicule. Le détail des quatre packs et des options figure sur notre page tarifs."),
    ("Intervenez-vous à domicile ?",
     "Oui, c'est notre mode d'intervention principal, partout en Île-de-France. Nous venons avec notre matériel, "
     "notre eau et notre électricité : vous n'avez ni prise ni point d'eau à fournir."),
    ("Combien de temps dure une intervention ?",
     "Entre 1 h et 4 h selon la prestation. Un canapé 3 places demande environ 1 h, un Intérieur Prestige "
     "automobile près de 3 h, une remise en état après travaux une journée complète."),
    ("Que contient un nettoyage automobile sans option ?",
     "Aspiration complète de l'habitacle et du coffre, shampoing des tapis et moquettes, puis désinfection des "
     "allergènes et acariens par vapeur haute température sur les sièges, le volant, les tapis et les surfaces "
     "planes. Le coffre est compris, sans supplément."),
    ("Les frais de déplacement sont-ils inclus ?",
     "Non, ils s'ajoutent au prix de la prestation : 5 € par tranche de 5 km entre notre atelier de "
     "Tremblay-en-France (93) et votre adresse. Le montant vous est annoncé avant que vous validiez. "
     "Aucune surprise à l'arrivée."),
    ("Utilisez-vous des produits écologiques ?",
     "Nous privilégions des produits respectueux de l'environnement et de votre santé, sans danger pour les "
     "enfants ni les animaux. La vapeur haute température nous permet en outre de désinfecter de nombreuses "
     "surfaces sans aucun produit chimique."),
    ("Faut-il verser un acompte ?",
     "Non. Vous réglez après l'intervention, une fois le résultat constaté avec vous. Nous acceptons les "
     "espèces, la carte bancaire et le virement."),
    ("Intervenez-vous pour les professionnels ?",
     "Oui : bureaux, locaux commerciaux, restaurants et commerces, en passage ponctuel ou régulier, avec "
     "facturation entreprise. Nous réalisons également le nettoyage de fin de chantier pour les artisans "
     "et les agences."),
    ("Quelles sont vos zones d'intervention ?",
     "Les huit départements franciliens : Paris (75), Hauts-de-Seine (92), Seine-Saint-Denis (93), "
     "Val-de-Marne (94), Essonne (91), Yvelines (78), Seine-et-Marne (77) et Val-d'Oise (95)."),
    ("Comment obtenir un devis gratuit ?",
     "Par le formulaire de notre page devis, ou par téléphone au 06 23 07 52 59. Nous répondons sous 24 h "
     "et intervenons 7j/7 en Île-de-France."),
]

# --- Articles du blog -----------------------------------------------------
POSTS = [
    {
        "slug": "nettoyer-entretenir-canape-tissu",
        "title": "Nettoyer et entretenir son canapé en tissu",
        "cat": "Textile",
        "date": "2026-08-28",
        "date_fr": "28 août 2026",
        "image": "canape-nettoyage.webp",
        "excerpt": "Aspirer chaque semaine, tamponner sans frotter, ne jamais détremper : les trois réflexes qui évitent les auréoles et espacent les nettoyages en profondeur.",
        "meta": "Comment nettoyer et entretenir un canapé en tissu sans faire d'auréole : gestes hebdomadaires, détachage d'urgence et limites du fait-maison.",
        "body": [
            ("p", "Un canapé en tissu encaisse tout : les repas devant la télévision, les enfants, l'animal qui s'installe sur l'accoudoir. La bonne nouvelle, c'est que l'essentiel de son entretien tient à deux gestes très simples — et à une erreur à ne pas commettre."),
            ("h2", "Aspirer chaque semaine, coussins compris"),
            ("p", "La poussière n'est pas seulement inesthétique : c'est le garde-manger des acariens. Passez l'aspirateur une fois par semaine sur l'assise, le dossier et les accoudoirs, en retirant les coussins pour atteindre les plis et le fond du caisson. C'est là que tout s'accumule."),
            ("p", "Ce geste hebdomadaire évite que les particules ne s'incrustent au cœur de la fibre, là où l'aspirateur ne va plus les chercher. Un canapé aspiré régulièrement se nettoie ensuite bien mieux en profondeur."),
            ("h2", "Sur une tache : agir vite, tamponner, jamais frotter"),
            ("p", "Une tache fraîche part presque toujours ; une tache incrustée depuis trois mois, rarement en totalité. Dès l'accident, tamponnez avec un chiffon propre légèrement humide et un savon doux, <strong>toujours du bord vers le centre</strong> pour ne pas étaler l'auréole."),
            ("blockquote", "Frotter étale la tache et abîme la fibre. Tamponner l'absorbe. C'est toute la différence entre une tache qui part et une tache qui s'installe."),
            ("h2", "L'erreur qui crée les auréoles : trop d'eau"),
            ("p", "C'est de loin la plus fréquente. En versant de l'eau sur un tissu, on dissout la saleté… et on la repousse vers les bords, où elle sèche en formant un cerne bien visible. Le canapé paraît alors plus sale après le nettoyage qu'avant."),
            ("p", "Deux précautions : testez toujours sur une zone cachée — sous un coussin, à l'arrière du caisson — et humidifiez, ne détrempez jamais. Si la tache résiste, mieux vaut s'arrêter là que d'insister."),
            ("h2", "Quand le fait-maison ne suffit plus"),
            ("p", "Pour les taches anciennes, les odeurs installées ou un tissu clair qui a perdu sa teinte d'origine, l'injection-extraction reste la seule méthode qui traite le cœur de la fibre sans la détremper. La solution est injectée sous pression puis immédiatement réaspirée avec la saleté dissoute : le canapé ressort humide, pas mouillé, et sèche en 4 à 6 h sans auréole."),
        ],
        "cta": "Un canapé à traiter en profondeur ?",
        "service": "nettoyage-textile-paris",
    },
    {
        "slug": "eliminer-acariens-matelas",
        "title": "Éliminer les acariens de son matelas",
        "cat": "Textile",
        "date": "2026-08-22",
        "date_fr": "22 août 2026",
        "image": "intervention-2.webp",
        "excerpt": "Nous passons près d'un tiers de notre vie sur notre matelas. Aération, protège-matelas et traitement haute température : ce qui marche vraiment contre les allergènes.",
        "meta": "Comment éliminer les acariens d'un matelas : aération, protège-matelas lavable, bicarbonate et nettoyage anti-acariens à haute température.",
        "body": [
            ("p", "Un matelas accumule chaque nuit transpiration, cellules mortes et humidité — exactement le milieu dont les acariens ont besoin. Comme nous y passons près d'un tiers de notre vie, c'est probablement le textile le plus important de la maison, et le plus négligé."),
            ("h2", "Aérer la chambre chaque matin"),
            ("p", "Les acariens ont besoin d'humidité pour se développer. Dix minutes de fenêtre ouverte chaque matin, en rabattant la couette plutôt qu'en la refaisant immédiatement, font baisser l'hygrométrie du lit de façon significative. C'est le geste le plus efficace, et il est gratuit."),
            ("h2", "Un protège-matelas lavable, changé régulièrement"),
            ("p", "Le protège-matelas fait barrière entre vous et le matelas : c'est lui qui prend la transpiration, et lui qu'on peut laver à 60 °C. Sans protection, tout part directement dans la mousse, où plus rien ne se lave."),
            ("h2", "Retourner le matelas et neutraliser les odeurs"),
            ("p", "Retournez le matelas tous les trois à six mois : cela répartit l'usure et permet à la face inférieure de sécher. Contre les odeurs, saupoudrez un peu de bicarbonate de soude, laissez agir quelques heures, puis aspirez soigneusement."),
            ("h2", "Le traitement haute température, pour les allergiques"),
            ("p", "Le bicarbonate masque, il ne détruit pas. Pour éliminer réellement les allergènes, il faut de la chaleur : un nettoyage anti-acariens à haute température, appliqué <strong>sur les deux faces</strong>, traite en profondeur les allergènes, les taches et les odeurs. C'est la solution que nous recommandons systématiquement aux personnes asthmatiques ou allergiques."),
        ],
        "cta": "Un matelas à assainir ?",
        "service": "nettoyage-textile-paris",
    },
    {
        "slug": "raviver-un-tapis",
        "title": "Raviver un tapis sans le faire dégorger",
        "cat": "Textile",
        "date": "2026-08-14",
        "date_fr": "14 août 2026",
        "image": "tapis-karcher.webp",
        "excerpt": "Laine, soie ou synthétique : la fibre décide de la méthode.",
        "meta": "Comment raviver un tapis sans le faire dégorger : aspiration des deux côtés, rotation, détachage et test des couleurs selon la fibre.",
        "body": [
            ("p", "Un tapis se dégrade de deux façons : par l'usure localisée, là où l'on marche toujours, et par l'accumulation de particules abrasives à la base de la fibre, qui scient la laine de l'intérieur. Les deux se combattent facilement."),
            ("h2", "Aspirer des deux côtés"),
            ("p", "L'envers d'un tapis n'est pas décoratif, mais c'est par là que les particules lourdes redescendent. Passez l'aspirateur au dos du tapis, puis à l'endroit : vous ferez tomber ce que le passage direct n'atteint pas."),
            ("h2", "Changer le tapis de place"),
            ("p", "Une simple rotation à 180° tous les six mois répartit le piétinement et l'exposition à la lumière. Sans elle, un tapis développe un couloir d'usure visible et une différence de teinte entre la zone exposée au soleil et le reste."),
            ("h2", "Traiter une tache sans détremper"),
            ("p", "Le réflexe est le même que sur un canapé : tamponner, jamais frotter, et surtout ne pas noyer la fibre. Sur une laine ou une soie, frotter feutre la surface de façon irréversible."),
            ("h2", "Pourquoi le test des couleurs est indispensable"),
            ("p", "Certaines teintures — les rouges et les indigos naturels en particulier — dégorgent au contact de l'eau et migrent vers les fibres claires voisines. Une fois la couleur partie, elle ne revient pas."),
            ("p", "C'est pour cette raison que nous testons systématiquement la solidité des couleurs sur une zone cachée avant tout lavage, et que nous adaptons la méthode à la fibre : laine, soie et synthétique n'appellent ni les mêmes produits, ni la même quantité d'eau. Les pièces précieuses peuvent être traitées en atelier plutôt qu'à domicile."),
        ],
        "cta": "Un tapis à faire revivre ?",
        "service": "nettoyage-textile-paris",
    },
    {
        "slug": "garder-voiture-propre-plus-longtemps",
        "title": "Garder sa voiture propre plus longtemps",
        "cat": "Automobile",
        "date": "2026-08-06",
        "date_fr": "6 août 2026",
        "image": "auto-interieur-vw.webp",
        "excerpt": "Les habitudes simples qui espacent les nettoyages en profondeur — et ce qui fait vraiment la différence avant une revente.",
        "meta": "Comment garder l'intérieur de sa voiture propre plus longtemps : habitudes quotidiennes, protection du cuir, odeurs et préparation avant revente.",
        "body": [
            ("p", "L'intérieur d'une voiture se salit lentement, puis d'un coup. Entre les deux, quelques habitudes suffisent à repousser franchement l'échéance du nettoyage complet."),
            ("h2", "Vider l'habitacle, secouer les tapis"),
            ("p", "Les tapis de sol retiennent l'essentiel des particules abrasives que l'on ramène sous les chaussures. Les secouer une fois par semaine évite qu'elles ne s'enfoncent dans la moquette du plancher, où elles ne repartiront plus qu'en injection-extraction."),
            ("p", "Même logique pour les déchets : une bouteille oubliée sous un siège, un emballage dans le vide-poche, et l'odeur s'installe en quelques jours d'été."),
            ("h2", "Protéger le cuir de la chaleur"),
            ("p", "Le pire ennemi d'une sellerie cuir, c'est le soleil direct à travers un pare-brise. La chaleur assèche la fleur du cuir, qui se rétracte, se craquelle, et finit par se fendre aux points de tension. Un pare-soleil coûte quelques euros ; une réfection de sellerie, plusieurs centaines."),
            ("h2", "Avant une revente : l'odeur avant tout"),
            ("p", "C'est le point que la plupart des vendeurs sous-estiment. Un acheteur potentiel ouvre la portière et se fait un avis en trois secondes, sur une impression olfactive qu'il ne formulera même pas."),
            ("p", "Un detailing intérieur complet — shampoing des sièges, vapeur, rénovation des plastiques — associé à une neutralisation des odeurs par ozone permet de présenter un véhicule sans trace d'animal ni de tabac. Sur une annonce, cela se traduit très concrètement dans le prix accepté."),
        ],
        "cta": "Une voiture à préparer ?",
        "service": "nettoyage-automobile-paris",
    },
    {
        "slug": "entretenir-son-bateau",
        "title": "Entretenir son bateau entre deux sorties",
        "cat": "Nautique",
        "date": "2026-07-29",
        "date_fr": "29 juillet 2026",
        "image": "bateau-yacht.webp",
        "excerpt": "Rincer à l'eau douce, protéger la sellerie, traiter les dépôts verts — et pourquoi le choix des produits n'est pas seulement une question d'écologie.",
        "meta": "Entretien de bateau : rinçage à l'eau douce, protection de la sellerie, dépôts verts et produits biodégradables pour préserver le milieu aquatique.",
        "body": [
            ("p", "Un bateau passe l'essentiel de son temps à l'arrêt, exposé. C'est justement là qu'il se dégrade : dépôts verts sur le gelcoat, sellerie qui grise, ligne de flottaison qui se marque."),
            ("h2", "Rincer à l'eau douce après chaque sortie"),
            ("p", "En mer, le sel qui sèche sur le pont et les inox est corrosif. En eau douce, ce sont les dépôts organiques qui s'installent. Dans les deux cas, un rinçage systématique après la sortie est le geste le plus rentable de tout l'entretien d'un bateau."),
            ("h2", "Protéger la sellerie"),
            ("p", "Les selleries extérieures encaissent les UV toute l'année. Une protection appliquée en début de saison ralentit nettement le grisaillement et évite que le skaï ne durcisse puis ne craquelle aux coutures."),
            ("h2", "Traiter les dépôts verts sans attendre"),
            ("p", "Mousses, algues et moisissures s'installent d'abord dans les zones d'ombre et les recoins d'écoulement. Traités tôt, ils partent au lavage ; laissés en place une saison, ils pénètrent le gelcoat et laissent une marque durable."),
            ("h2", "Des produits biodégradables, par obligation autant que par principe"),
            ("p", "Tout ce qui sert au rinçage part directement dans l'eau. Ce n'est pas seulement un choix écologique : c'est ce qui conditionne les produits utilisables à quai. Nous travaillons exclusivement en biodégradable sur nos interventions nautiques, du lavage de coque au lustrage du gelcoat."),
        ],
        "cta": "Un bateau à remettre en état ?",
        "service": "nettoyage-bateau-paris",
    },
    {
        "slug": "nettoyer-terrasse-sans-abimer",
        "title": "Nettoyer sa terrasse sans l'abîmer",
        "cat": "Extérieur",
        "date": "2026-07-18",
        "date_fr": "18 juillet 2026",
        "image": "ba-terrasse2-apres.webp",
        "excerpt": "La haute pression fait des merveilles sur la pierre — et des dégâts irréversibles sur le bois. Comment régler le geste selon le support.",
        "meta": "Nettoyer une terrasse sans l'abîmer : pourquoi la haute pression détruit le bois, comment traiter la pierre et le béton, anti-mousse et saturateur.",
        "body": [
            ("p", "Le nettoyeur haute pression est l'outil le plus satisfaisant du jardin, et le plus dangereux pour une terrasse. Toute la difficulté tient en une question : de quel matériau est faite la vôtre ?"),
            ("h2", "Sur la pierre, le béton et le carrelage : la pression fait le travail"),
            ("p", "Ces supports minéraux encaissent une pression élevée sans dommage. C'est même la seule façon de déloger la crasse incrustée dans la porosité d'un béton désactivé ou les joints d'un carrelage extérieur. Le résultat est spectaculaire, comme le montrent nos avant/après sur terrasse en marbre."),
            ("h2", "Sur le bois : jamais de haute pression"),
            ("p", "C'est l'erreur la plus courante et la plus coûteuse. Une lance trop puissante <strong>ouvre la fibre du bois</strong> : la lame devient pelucheuse, retient davantage l'eau et la saleté, et grisaille beaucoup plus vite ensuite. Le dommage est irréversible — il faudrait poncer."),
            ("p", "Sur bois, la bonne méthode est le brossage doux, dans le sens de la fibre, avec un dégriseur si nécessaire."),
            ("h2", "L'anti-mousse préventif"),
            ("p", "Balayez régulièrement, surtout à l'automne : les feuilles qui restent en place gardent l'humidité et nourrissent la mousse. Un anti-mousse appliqué une à deux fois par an tue le lichen à la racine et ralentit fortement la repousse."),
            ("h2", "Finir par une protection"),
            ("p", "Un saturateur sur le bois, un hydrofuge sur la pierre poreuse : dans les deux cas, la protection limite la pénétration de l'eau et des salissures. C'est ce qui permet de passer d'un nettoyage tous les six mois à un nettoyage annuel."),
        ],
        "cta": "Une terrasse à remettre à neuf ?",
        "service": "nettoyage-terrasse-paris",
    },
    {
        "slug": "vitres-sans-traces",
        "title": "Des vitres sans traces : les trois vraies causes",
        "cat": "Extérieur",
        "date": "2026-07-09",
        "date_fr": "9 juillet 2026",
        "image": "vitre-controle.webp",
        "excerpt": "L'eau calcaire, les produits ménagers et le plein soleil. Comprendre d'où viennent les traces, c'est déjà les avoir supprimées.",
        "meta": "Pourquoi les vitres gardent des traces : eau calcaire, tensioactifs des produits ménagers, séchage au soleil. Méthode et intérêt de l'eau osmosée.",
        "body": [
            ("p", "Vous nettoyez, vous séchez, et le voile revient dès que la lumière passe de biais. Ce n'est ni une question de chiffon, ni de tour de main : les traces viennent presque toujours de trois causes identifiables."),
            ("h2", "1. L'eau du robinet"),
            ("p", "L'eau d'Île-de-France est particulièrement calcaire. En séchant sur une vitre, elle laisse ses minéraux sur place — c'est ce voile blanchâtre que l'on prend pour de la saleté et que l'on tente de frotter davantage, ce qui ne fait que le redistribuer."),
            ("h2", "2. Les produits ménagers"),
            ("p", "Les nettoyants vitres du commerce contiennent des tensioactifs. Ils décollent la saleté, mais laissent un film mince sur le verre. Ce film attire la poussière : la vitre se resalit plus vite qu'avant, ce qui donne l'impression que le produit « ne tient pas »."),
            ("h2", "3. Le plein soleil"),
            ("p", "Sur une vitre chaude, l'eau s'évapore avant que vous ayez pu passer la raclette. Elle sèche donc en place, avec tout ce qu'elle contient. Travaillez par temps couvert ou tôt le matin, jamais en plein soleil."),
            ("h2", "La bonne méthode, et la solution radicale"),
            ("p", "De haut en bas, en essuyant la lame de la raclette à chaque passage — sinon on redépose ce qu'on vient de retirer. Dégraissez d'abord les encadrements et les rails : nettoyer la vitre avant le cadre revient à la resalir immédiatement."),
            ("p", "Sur les grandes surfaces, les vérandas et les vitrines, nous employons de l'<strong>eau osmosée</strong> : filtrée par osmose inverse, elle ne contient plus de minéraux et sèche donc sans rien déposer. Aucun produit n'est nécessaire, donc aucun film résiduel."),
        ],
        "cta": "Des vitres ou une vitrine à traiter ?",
        "service": "nettoyage-vitres-paris",
    },
    {
        "slug": "trois-regles-or-detachage",
        "title": "Les trois règles d'or du détachage",
        "cat": "Conseils",
        "date": "2026-06-27",
        "date_fr": "27 juin 2026",
        "image": "intervention-2.webp",
        "excerpt": "Agir vite, tamponner sans frotter, tester avant de traiter. Trois règles qui s'appliquent à tous les textiles, sans exception.",
        "meta": "Les trois règles du détachage textile : agir vite, tamponner sans frotter, tester sur une zone cachée. Erreurs à éviter et mélanges dangereux.",
        "body": [
            ("p", "Que ce soit sur un canapé, un tapis, un siège de voiture ou une sellerie de bateau, le détachage obéit toujours aux mêmes règles. Les connaître évite la plupart des dégâts que nous sommes appelés à rattraper."),
            ("h2", "1. Agir vite"),
            ("p", "Une tache fraîche est en surface ; une tache sèche a migré au cœur de la fibre et, pour certaines, a commencé à réagir chimiquement avec la teinture. Les premières minutes comptent davantage que le produit utilisé."),
            ("p", "Le premier geste est toujours d'absorber : un chiffon propre, une pression franche, sans étaler."),
            ("h2", "2. Tamponner, jamais frotter"),
            ("p", "Frotter fait deux choses, toutes deux mauvaises : cela élargit la tache et cela casse la fibre en surface, créant une zone mate qui restera visible même une fois la tache partie. Sur une laine ou une soie, le feutrage est irréversible."),
            ("h2", "3. Tester avant de traiter"),
            ("p", "Toujours sur une zone cachée : sous un coussin, derrière un pied de fauteuil, à l'envers d'un tapis. Vous vérifiez deux choses — que la couleur ne dégorge pas, et que le produit n'attaque pas la fibre."),
            ("blockquote", "Et ne mélangez jamais deux produits entre eux. Certaines associations — eau de Javel et détartrant, notamment — dégagent des vapeurs dangereuses."),
            ("h2", "En cas de doute, ne prenez pas de risque"),
            ("p", "Sur un textile de valeur, une tache ancienne ou une matière que vous n'identifiez pas, l'essai raté coûte plus cher que l'intervention. Un professionnel commence de toute façon par identifier la fibre — c'est ce diagnostic, plus que le produit, qui fait la différence."),
        ],
        "cta": "Une tache que vous n'osez pas traiter ?",
        "service": "nettoyage-textile-paris",
    },
]


# --- Avis clients ---------------------------------------------------------
# Note globale affichée. À corriger dès qu'elle bouge sur votre fiche Google.
GOOGLE_NOTE = {"score": "5,0", "nombre": 10}

# IMPORTANT — n'inscrivez ici que de VRAIS avis, recopiés mot pour mot depuis
# votre fiche Google, avec le prénom et la date affichés par Google.
# Format : (auteur, date affichée, note sur 5, texte de l'avis)
#
# Tant que cette liste reste vide, la page affiche la note globale et renvoie
# vers Google : aucun témoignage n'est inventé. Dès que vous ajoutez une
# entrée, elle apparaît sous forme de carte. Exemple de ligne à recopier :
#
#     ("Sophie L.", "12 août 2026", 5, "Intervention impeccable sur mon canapé…"),
#
REVIEWS = []

# --- Réservation en ligne -------------------------------------------------
# Frais de déplacement : mêmes règles que l'ancien configurateur.
DEPLACEMENT = {
    "lat": 48.9486,          # atelier, 5 rue Nicolas Copernic
    "lon": 2.5697,
    "palier_km": 5,          # tranche facturée
    "palier_eur": 5,         # montant par tranche
    "coef_route": 1.25,      # majoration du vol d'oiseau vers la distance routière
}

CRENEAUX = [
    "Matin — 8h à 12h",
    "Après-midi — 12h à 17h",
    "Fin de journée — 17h à 20h",
]


# --- Photo d'en-tête de l'accueil ------------------------------------------
# "image"    : fichier dans site/assets/photos/
# "position" : cadrage CSS object-position — la photo est rognée par le
#              navigateur, ce réglage décide de la zone visible.
HERO = {
    "image": "hero-mathclean-vapeur.webp",
    "position": "center 45%",
    "alt": "Technicien MathClean en intervention de nettoyage vapeur, à Paris",
}


# --- Villes couvertes -----------------------------------------------------
# Une page par ville, avec la distance réelle calculée depuis l'atelier
# (48.9486, 2.5697). Les coordonnées sont celles du centre communal : la
# distance affichée est donc « environ », et le montant exact du déplacement
# reste celui que calcule le configurateur à partir de l'adresse précise.
#
# [slug, nom, code postal, département, lat, lon, angle éditorial, prestations mises en avant]
VILLES = [
    ("boulogne-billancourt", "Boulogne-Billancourt", "92100", "92", 48.8352, 2.2409,
     "Première commune d'Île-de-France par la population après Paris, Boulogne-Billancourt "
     "mêle immeubles haussmanniens, résidences récentes et un tissu dense de sièges sociaux. "
     "Deux demandes y dominent : le textile en appartement — canapés d'angle qu'on ne peut ni "
     "démonter ni descendre — et l'entretien de bureaux en horaires décalés.",
     ["nettoyage-textile-paris", "nettoyage-entreprise-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("neuilly-sur-seine", "Neuilly-sur-Seine", "92200", "92", 48.8846, 2.2697,
     "À Neuilly, l'essentiel de nos interventions concerne des selleries cuir, des tapis de "
     "laine et des moquettes de belle facture — des matières qui ne pardonnent pas l'erreur de "
     "produit. Le diagnostic de la fibre y compte davantage qu'ailleurs.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris", "nettoyage-terrasse-paris"]),

    ("levallois-perret", "Levallois-Perret", "92300", "92", 48.8939, 2.2874,
     "Levallois concentre bureaux et logements sur un territoire très compact. Le stationnement "
     "y étant difficile, notre autonomie en eau et en électricité change tout : nous intervenons "
     "en parking souterrain, sans avoir à tirer un tuyau depuis la rue.",
     ["nettoyage-entreprise-paris", "nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris"]),

    ("nanterre", "Nanterre", "92000", "92", 48.8924, 2.2069,
     "Entre la préfecture, les campus et la proximité immédiate de La Défense, Nanterre nous "
     "sollicite surtout pour l'entretien de locaux professionnels et la remise en état après "
     "travaux, deux prestations qui se planifient hors des heures d'activité.",
     ["nettoyage-entreprise-paris", "nettoyage-fin-de-chantier-paris", "nettoyage-vitres-paris", "nettoyage-textile-paris"]),

    ("issy-les-moulineaux", "Issy-les-Moulineaux", "92130", "92", 48.8239, 2.2730,
     "Pôle tertiaire dense, Issy-les-Moulineaux nous appelle principalement pour la vitrerie de "
     "grandes surfaces et l'entretien de moquettes de bureaux. L'eau osmosée y prend tout son "
     "sens sur les façades vitrées.",
     ["nettoyage-vitres-paris", "nettoyage-entreprise-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris"]),

    ("saint-denis", "Saint-Denis", "93200", "93", 48.9362, 2.3574,
     "Saint-Denis est en chantier permanent : programmes neufs, réhabilitations, bureaux livrés "
     "en continu. Notre prestation de fin de chantier y représente une part importante de "
     "l'activité, souvent en deux passages à quelques jours d'intervalle.",
     ["nettoyage-fin-de-chantier-paris", "nettoyage-entreprise-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris"]),

    ("montreuil", "Montreuil", "93100", "93", 48.8638, 2.4485,
     "Montreuil alterne pavillons, lofts d'anciens ateliers et immeubles récents. Les grands "
     "volumes reconvertis y posent une question précise : des moquettes et des textiles en "
     "quantité, dans des espaces qu'on ne peut pas vider.",
     ["nettoyage-textile-paris", "nettoyage-fin-de-chantier-paris", "nettoyage-automobile-paris", "nettoyage-terrasse-paris"]),

    ("aulnay-sous-bois", "Aulnay-sous-Bois", "93600", "93", 48.9386, 2.4938,
     "Aulnay est à quelques minutes de notre atelier : c'est l'une des communes où nous "
     "intervenons le plus rapidement, souvent dans la journée en cas d'urgence. L'habitat "
     "pavillonnaire y appelle surtout du textile et du detailing automobile à domicile.",
     ["nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-terrasse-paris", "nettoyage-entreprise-paris"]),

    ("tremblay-en-france", "Tremblay-en-France", "93290", "93", 48.9486, 2.5697,
     "C'est notre commune : l'atelier se trouve au 5 rue Nicolas Copernic. Les frais de "
     "déplacement y sont nuls ou symboliques, et nous pouvons intervenir dans des délais que "
     "nous ne tenons nulle part ailleurs.",
     ["nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-terrasse-paris", "nettoyage-fin-de-chantier-paris"]),

    ("pantin", "Pantin", "93500", "93", 48.8944, 2.4090,
     "Pantin s'est couverte de bureaux et d'ateliers reconvertis le long du canal. Nous y "
     "traitons beaucoup de locaux professionnels, avec la contrainte habituelle des sites "
     "occupés : intervenir tôt le matin ou après la fermeture.",
     ["nettoyage-entreprise-paris", "nettoyage-fin-de-chantier-paris", "nettoyage-vitres-paris", "nettoyage-textile-paris"]),

    ("creteil", "Créteil", "94000", "94", 48.7904, 2.4556,
     "Préfecture du Val-de-Marne, Créteil combine grands ensembles, zones d'activité et "
     "équipements publics. Les demandes y sont partagées entre entretien de locaux et textile "
     "à domicile.",
     ["nettoyage-entreprise-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris"]),

    ("vincennes", "Vincennes", "94300", "94", 48.8478, 2.4390,
     "Vincennes est un tissu résidentiel serré, aux appartements souvent anciens. Canapés, "
     "matelas et tapis y constituent l'essentiel des interventions, avec la contrainte "
     "récurrente des escaliers étroits — qui ne nous gêne pas, puisque nous travaillons sur place.",
     ["nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris", "nettoyage-entreprise-paris"]),

    ("saint-maur-des-fosses", "Saint-Maur-des-Fossés", "94100", "94", 48.7994, 2.4934,
     "Dans la boucle de la Marne, Saint-Maur aligne pavillons avec jardin et terrasses. La "
     "remise en état des terrasses y suit les saisons, et les bords de Marne nous amènent une "
     "part de nos interventions nautiques.",
     ["nettoyage-terrasse-paris", "nettoyage-bateau-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris"]),

    ("massy", "Massy", "91300", "91", 48.7262, 2.2825,
     "Massy conjugue quartiers d'affaires, gares et logements neufs. Nous y intervenons pour "
     "l'entretien de bureaux et la remise en état après travaux, les livraisons de programmes "
     "y étant fréquentes.",
     ["nettoyage-entreprise-paris", "nettoyage-fin-de-chantier-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris"]),

    ("evry-courcouronnes", "Évry-Courcouronnes", "91000", "91", 48.6238, 2.4297,
     "Évry-Courcouronnes est l'un des points les plus éloignés de notre atelier : nous y "
     "groupons volontiers plusieurs interventions sur une même journée, ce qui reste le meilleur "
     "moyen de contenir les frais de déplacement.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-entreprise-paris", "nettoyage-terrasse-paris"]),

    ("versailles", "Versailles", "78000", "78", 48.8014, 2.1301,
     "À Versailles, nous traitons beaucoup de matières nobles — parquets, tapis de laine, "
     "selleries cuir — et de terrasses en pierre. Sur ces supports, la question n'est jamais la "
     "puissance mais le réglage.",
     ["nettoyage-textile-paris", "nettoyage-terrasse-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("saint-germain-en-laye", "Saint-Germain-en-Laye", "78100", "78", 48.8987, 2.0940,
     "Maisons anciennes, jardins et terrasses en pierre : Saint-Germain-en-Laye appelle surtout "
     "du nettoyage extérieur au printemps et du textile de valeur le reste de l'année.",
     ["nettoyage-terrasse-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("chelles", "Chelles", "77500", "77", 48.8797, 2.5928,
     "Chelles est l'une des communes de Seine-et-Marne les plus proches de notre atelier, à "
     "quelques minutes seulement. Habitat pavillonnaire dominant : terrasses, textile et "
     "automobile à domicile.",
     ["nettoyage-terrasse-paris", "nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-entreprise-paris"]),

    ("meaux", "Meaux", "77100", "77", 48.9601, 2.8785,
     "Meaux marque la limite est de notre zone habituelle. Nous y intervenons volontiers, en "
     "planifiant la journée autour du déplacement — plusieurs prestations groupées plutôt qu'un "
     "aller-retour pour une seule.",
     ["nettoyage-textile-paris", "nettoyage-terrasse-paris", "nettoyage-entreprise-paris", "nettoyage-automobile-paris"]),

    ("argenteuil", "Argenteuil", "95100", "95", 48.9474, 2.2467,
     "Argenteuil est la plus peuplée du Val-d'Oise, avec un habitat très varié. Textile à "
     "domicile et detailing automobile y constituent l'essentiel de nos passages.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris", "nettoyage-entreprise-paris"]),

    ("cergy", "Cergy", "95000", "95", 49.0361, 2.0631,
     "Ville nouvelle et pôle universitaire, Cergy nous sollicite pour des locaux professionnels "
     "et des logements étudiants en remise en état, souvent entre deux occupations.",
     ["nettoyage-entreprise-paris", "nettoyage-fin-de-chantier-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris"]),

    ("sarcelles", "Sarcelles", "95200", "95", 48.9959, 2.3785,
     "Sarcelles est proche de notre atelier, ce qui maintient les frais de déplacement bas. "
     "Nous y intervenons surtout en textile à domicile et en entretien de commerces.",
     ["nettoyage-textile-paris", "nettoyage-entreprise-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris"]),

    ("paris-8", "Paris 8e", "75008", "75", 48.8721, 2.3120,
     "Le 8e concentre sièges sociaux, hôtels et commerces de luxe. Vitrines, selleries cuir et "
     "moquettes de bureaux y forment le gros de nos interventions, presque toujours en horaires "
     "décalés pour ne pas gêner l'activité.",
     ["nettoyage-vitres-paris", "nettoyage-entreprise-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris"]),

    ("paris-11", "Paris 11e", "75011", "75", 48.8580, 2.3792,
     "Le 11e est un arrondissement dense, très résidentiel et très restauré. Nous y traitons "
     "beaucoup de canapés et de matelas en appartement, et des cuisines professionnelles en "
     "intervention nocturne.",
     ["nettoyage-textile-paris", "nettoyage-entreprise-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("paris-12", "Paris 12e", "75012", "75", 48.8409, 2.3876,
     "Entre Bercy, la Bastille et le bois de Vincennes, le 12e alterne immeubles récents et "
     "bâti ancien. Textile à domicile et entretien de locaux s'y partagent nos passages.",
     ["nettoyage-textile-paris", "nettoyage-entreprise-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris"]),

    ("paris-15", "Paris 15e", "75015", "75", 48.8412, 2.3003,
     "Le 15e est le plus peuplé des arrondissements parisiens. Grands appartements familiaux, "
     "donc grands canapés et moquettes : c'est l'arrondissement où l'injection-extraction à "
     "domicile prend le plus de sens.",
     ["nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris", "nettoyage-entreprise-paris"]),

    ("paris-16", "Paris 16e", "75016", "75", 48.8637, 2.2769,
     "Le 16e nous amène des matières exigeantes : tapis d'Orient, parquets anciens, selleries "
     "cuir. Le test de solidité des couleurs y est systématique avant tout lavage.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris", "nettoyage-terrasse-paris"]),

    ("paris-17", "Paris 17e", "75017", "75", 48.8872, 2.3220,
     "Des Batignolles à la plaine Monceau, le 17e mêle résidentiel haussmannien et bureaux "
     "récents. Vitrerie, textile et entretien de locaux s'y répartissent assez également.",
     ["nettoyage-vitres-paris", "nettoyage-textile-paris", "nettoyage-entreprise-paris", "nettoyage-automobile-paris"]),
]


# --- Guides -----------------------------------------------------------------
# Pages de fond, écrites pour répondre réellement à une question. Ce sont
# elles qui se font citer par les moteurs et par les assistants IA : un
# contenu argumenté est repris, une page vide ne l'est pas.
#
# Chaque guide : slug, h1, title, meta, rubrique, chapô, sections, FAQ,
# prestation liée, photo.
GUIDES = [
{
 "slug": "choisir-entreprise-nettoyage-ile-de-france",
 "cat": "Bien choisir",
 "h1": "Comment choisir une entreprise de nettoyage en Île-de-France",
 "title": "Choisir une entreprise de nettoyage en Île-de-France — 7 critères | MathClean",
 "meta": "Les sept critères qui distinguent une entreprise de nettoyage sérieuse en Île-de-France : devis ferme, assurance, matériel, acompte, avis vérifiables. Guide pratique.",
 "image": "intervention-1.webp",
 "lead": "Toutes les entreprises de nettoyage annoncent le même résultat. Voici les sept points sur lesquels elles se différencient réellement — et comment les vérifier avant de signer.",
 "sections": [
  ("1. Un devis ferme, pas une fourchette ouverte", [
   "Une fourchette large (« entre 100 et 400 € ») signifie que le prestataire n'a pas évalué votre besoin. Un devis sérieux détaille chaque poste et s'engage sur un montant, quitte à demander des photos ou une visite préalable.",
   "Méfiez-vous surtout des devis qui ne mentionnent pas les frais de déplacement : c'est le poste qui réapparaît le jour de l'intervention. Demandez systématiquement s'ils sont inclus, et sinon comment ils se calculent."]),
  ("2. Un numéro SIRET vérifiable", [
   "Toute entreprise déclarée en France possède un SIRET, consultable gratuitement sur l'annuaire des entreprises. Un prestataire qui ne l'affiche pas sur son site ou ses devis vous expose : en cas de dommage, vous n'avez aucun recours.",
   "Vérifiez aussi que l'activité déclarée correspond bien au nettoyage."]),
  ("3. Une assurance responsabilité civile professionnelle", [
   "Un canapé décoloré, un parquet marqué, une vitre rayée : ces incidents existent. La question n'est pas de savoir s'ils sont rares, mais qui paie s'ils surviennent. Demandez l'attestation d'assurance, elle se fournit en une minute."]),
  ("4. Le matériel, et l'autonomie", [
   "Une entreprise qui vous demande une prise et un point d'eau vous transfère une contrainte. Celles qui viennent avec leur propre eau et leur propre électricité peuvent intervenir en parking, en pied d'immeuble ou à quai — et cela change ce qu'elles peuvent traiter.",
   "Sur le textile, exigez de savoir la méthode : injection-extraction, vapeur, ou simple shampoing de surface. Ce n'est pas le même résultat, ni la même durée de séchage."]),
  ("5. L'acompte", [
   "Un acompte n'a rien d'illégal, mais il déplace le risque sur vous. Un prestataire confiant dans son résultat accepte d'être réglé après l'intervention, une fois le travail constaté. C'est un signal simple et fiable."]),
  ("6. Des avis vérifiables, pas des témoignages", [
   "Les témoignages recopiés sur un site sont invérifiables : n'importe qui peut écrire « Sophie, très satisfaite ». Les avis Google, eux, portent un nom, une date, et un historique de compte.",
   "Regardez moins la note que le contenu : un avis détaillé qui décrit la prestation vaut mieux que dix « super, je recommande »."]),
  ("7. La personne qui répond au téléphone", [
   "Dans le nettoyage à domicile, la sous-traitance en cascade est fréquente : vous appelez une plateforme, un intermédiaire prend la commande, un exécutant que personne n'a briefé se présente chez vous.",
   "Demandez simplement : « est-ce vous qui interviendrez ? ». La réponse vous en dira long."])],
 "faq": [
  ("Quel est le prix moyen d'un nettoyage en Île-de-France ?",
   "Cela dépend entièrement de la prestation. À titre de repère : un canapé 2 places se traite à partir de 39 €, un detailing automobile à partir de 40 €, et les prestations professionnelles se chiffrent sur devis après visite. Un prix annoncé sans connaître le besoin n'a aucune valeur."),
  ("Faut-il choisir une grande entreprise ou un indépendant ?",
   "La taille ne dit rien de la qualité. Ce qui compte, c'est de savoir qui intervient réellement chez vous, avec quel matériel, et qui est responsable en cas de problème. Une structure petite mais directe apporte souvent plus de continuité qu'une chaîne de sous-traitance."),
  ("Les frais de déplacement sont-ils négociables ?",
   "Rarement dans leur principe, mais on peut souvent les réduire en groupant plusieurs prestations sur une même intervention : le déplacement n'est alors facturé qu'une fois.")],
 "service": "nettoyage-entreprise-paris",
},
{
 "slug": "choisir-entreprise-nettoyage-paris",
 "cat": "Bien choisir",
 "h1": "Entreprise de nettoyage à Paris : ce qui change intra-muros",
 "title": "Choisir une entreprise de nettoyage à Paris — les contraintes propres à la capitale | MathClean",
 "meta": "Stationnement, ascenseurs, horaires de commerce, copropriétés : les contraintes parisiennes qui doivent guider le choix d'une entreprise de nettoyage.",
 "image": "intervention-2.webp",
 "lead": "Les critères généraux valent partout. Mais Paris ajoute quatre contraintes matérielles qui éliminent, en pratique, une bonne partie des prestataires.",
 "sections": [
  ("Le stationnement décide de tout", [
   "Un prestataire qui doit se garer à proximité immédiate pour tirer un tuyau ou une rallonge ne peut pas intervenir dans la plupart des rues parisiennes. C'est la raison, rarement dite, pour laquelle certaines demandes sont refusées ou reportées.",
   "Une équipe autonome en eau et en électricité s'affranchit du problème : elle porte son matériel, se gare où elle peut, et travaille dans l'appartement ou le parking."]),
  ("Les escaliers et les ascenseurs", [
   "Beaucoup d'immeubles parisiens n'ont pas d'ascenseur, ou un ascenseur trop étroit pour un canapé. C'est précisément pourquoi le nettoyage textile se fait sur place : rien ne descend, rien ne remonte.",
   "Vérifiez que le prestataire traite à domicile plutôt qu'en atelier — sinon la logistique devient votre problème."]),
  ("Les horaires, pour les commerces", [
   "Un restaurant ou une boutique ne ferme pas pour un nettoyage. Les interventions se font avant l'ouverture, après la fermeture, ou de nuit. Toutes les entreprises ne le proposent pas ; celles qui le font l'annoncent clairement."]),
  ("Les règles de copropriété", [
   "Certaines copropriétés interdisent les travaux bruyants à certaines heures, ou l'usage des parties communes. Un prestataire habitué à Paris anticipe ces questions au lieu de les découvrir sur place."])],
 "faq": [
  ("Peut-on faire nettoyer un canapé sans le sortir de l'appartement ?",
   "Oui, c'est même la règle. L'injection-extraction se pratique sur place : la solution est injectée dans la fibre puis immédiatement réaspirée. Le canapé ressort humide, pas trempé, et sèche en 4 à 6 h."),
  ("Intervenez-vous dans tous les arrondissements ?",
   "Oui, du 1er au 20e. Les délais sont généralement de 24 à 48 h à Paris et en petite couronne."),
  ("Faut-il être présent pendant l'intervention ?",
   "C'est préférable au début, pour le diagnostic, et à la fin pour le contrôle. Entre les deux, vous n'êtes pas obligé de rester.")],
 "service": "nettoyage-textile-paris",
},
{
 "slug": "entreprise-nettoyage-vitres-specialisee",
 "cat": "Vitrerie",
 "h1": "Entreprise spécialisée en nettoyage de vitres : ce qui la distingue",
 "title": "Entreprise de nettoyage de vitres spécialisée à Paris — méthode et matériel | MathClean",
 "meta": "Ce qui sépare un laveur de vitres généraliste d'une entreprise spécialisée : eau osmosée, perche télescopique, contrôle en lumière rasante. Devis gratuit en Île-de-France.",
 "image": "vitre-controle.webp",
 "lead": "Nettoyer une vitre est facile. La nettoyer sans laisser de trace, sur une véranda ou une façade de six mètres, relève d'un autre métier. Voici ce qui sépare les deux.",
 "sections": [
  ("L'eau osmosée, et pourquoi elle change le résultat", [
   "L'eau d'Île-de-France est très calcaire. En séchant sur une vitre, elle abandonne ses minéraux : c'est ce voile blanchâtre que l'on prend pour de la saleté et que l'on frotte en vain.",
   "L'osmose inverse retire ces minéraux. L'eau sèche alors sans rien déposer, ce qui permet de se passer totalement de détergent — donc de film résiduel, donc de resalissement accéléré. C'est le marqueur le plus fiable d'une entreprise spécialisée."]),
  ("Le travail en hauteur", [
   "La perche télescopique alimentée en eau pure permet de traiter plusieurs étages depuis le sol, sans nacelle ni cordiste. Cela réduit le coût et le risque, et rend accessibles des vérandas et verrières qu'on ne nettoie autrement qu'à grands frais.",
   "Au-delà d'une certaine hauteur ou en cas d'accès impossible, une entreprise honnête vous le dit avant le devis."]),
  ("L'ordre des opérations", [
   "Les encadrements, rails et appuis se dégraissent avant la vitre. L'inverse — nettoyer la vitre puis le cadre — la resalit immédiatement. C'est un détail de méthode, mais il se voit sur le résultat."]),
  ("Le contrôle en lumière rasante", [
   "Une vitre se contrôle de biais, à contre-jour, jamais de face. C'est le seul angle qui révèle un voile résiduel. Un professionnel termine toujours par ce contrôle ; un généraliste range son matériel."])],
 "faq": [
  ("À quelle fréquence nettoyer une vitrine de commerce ?",
   "Hebdomadaire ou bimensuel selon l'exposition à la rue et au trafic. Un forfait de passage régulier revient nettement moins cher que des interventions ponctuelles."),
  ("L'eau osmosée abîme-t-elle les joints ?",
   "Non. C'est de l'eau pure, sans additif ni détergent : elle est moins agressive pour les joints et les menuiseries que la plupart des produits vitres du commerce."),
  ("Pourquoi mes vitres se resalissent-elles si vite ?",
   "Le plus souvent à cause du film laissé par les tensioactifs des nettoyants ménagers, qui retient la poussière. Sans produit, ce film n'existe pas.")],
 "service": "nettoyage-vitres-paris",
},
{
 "slug": "entreprise-nettoyage-professionnelle",
 "cat": "Professionnels",
 "h1": "Entreprise de nettoyage professionnelle : ce que couvre vraiment un contrat",
 "title": "Entreprise professionnelle de nettoyage à Paris — contrat, fréquence, protocole | MathClean",
 "meta": "Ce que doit contenir un contrat d'entretien de locaux : protocole écrit, fréquence, zones, horaires, interlocuteur. Guide pour les entreprises d'Île-de-France.",
 "image": "bureau-entreprise.webp",
 "lead": "La plupart des litiges d'entretien de locaux viennent du même point : personne n'a écrit ce qui devait être fait, ni à quelle fréquence. Voici ce que doit contenir un contrat sérieux.",
 "sections": [
  ("Un protocole écrit, zone par zone", [
   "« Nettoyage des bureaux » ne veut rien dire. Un protocole utile liste les zones — postes de travail, salles de réunion, sanitaires, cuisine, accueil, circulations — et pour chacune ce qui est fait, et à quelle fréquence.",
   "C'est ce document qui permet, six mois plus tard, de dire objectivement si la prestation est conforme."]),
  ("La fréquence, définie par l'usage", [
   "Des sanitaires dans un open space de cinquante personnes n'ont pas le même besoin que ceux d'un cabinet de trois. La fréquence se déduit du nombre de passages, pas d'un forfait standard.",
   "Certains postes se traitent en profondeur une à deux fois par an : moquettes en injection-extraction, vitrerie complète, dégraissage de cuisine. Ils doivent apparaître séparément."]),
  ("Les horaires, et leur coût réel", [
   "Intervenir hors des heures d'activité est souvent indispensable, mais ce n'est pas neutre. Un contrat clair précise les créneaux et ce qu'ils impliquent, plutôt que de laisser la question se régler au cas par cas."]),
  ("Un interlocuteur identifié", [
   "Savoir qui appeler quand quelque chose ne va pas vaut mieux que n'importe quelle clause. Un interlocuteur unique, joignable après chaque passage, règle en pratique la majorité des désaccords avant qu'ils ne deviennent des litiges."])],
 "faq": [
  ("Faut-il un contrat annuel ?",
   "Pas nécessairement. Le passage ponctuel a du sens pour une remise à niveau, un contrôle d'hygiène ou une fin de chantier. Le contrat régulier se justifie dès que la fréquence devient prévisible."),
  ("Qui fournit les consommables ?",
   "Cela se décide au contrat. Papier, savon et sacs peuvent être fournis par le prestataire ou par l'entreprise : l'essentiel est que ce soit écrit."),
  ("Comment est facturée une prestation professionnelle ?",
   "Sur devis, après visite des locaux et mesure des surfaces, avec facturation entreprise. Un prix au mètre carré annoncé sans visite est un prix approximatif.")],
 "service": "nettoyage-entreprise-paris",
},
{
 "slug": "prix-nettoyage-canape-paris",
 "cat": "Prix",
 "h1": "Combien coûte un nettoyage de canapé à Paris ?",
 "title": "Prix d'un nettoyage de canapé à Paris — tarifs 2026 par taille | MathClean",
 "meta": "Prix d'un nettoyage de canapé à domicile à Paris : 39 € le 2 places, 49 € le 3 places, 69 € le canapé d'angle. Ce qui fait varier le tarif, frais de déplacement compris.",
 "image": "canape-nettoyage.webp",
 "lead": "Le prix dépend de trois choses : la taille, la matière, et l'état. Voici les tarifs de référence et ce qui les fait bouger.",
 "sections": [
  ("Les tarifs par taille", [
   "Chez MathClean, un canapé 2 places se traite à 39 €, un 3 places à 49 €, un canapé d'angle à 69 €. Un fauteuil est à 25 €, une chaise à 15 €. Ces prix couvrent l'injection-extraction et le détachage.",
   "S'y ajoutent les frais de déplacement : 5 € par tranche de 5 km depuis notre atelier de Tremblay-en-France. Ils sont annoncés avant que vous validiez, jamais découverts à l'arrivée."]),
  ("Ce qui fait varier le prix", [
   "La matière d'abord : un tissu synthétique se traite en injection-extraction, un cuir demande un nettoyage doux puis un nourrissage — ce n'est ni le même temps ni les mêmes produits.",
   "L'état ensuite. Des taches fraîches partent au passage habituel ; des taches incrustées depuis des mois demandent un pré-traitement et un temps de pause. Un professionnel honnête vous dit ce qui est réaliste avant de commencer."]),
  ("Faire plusieurs pièces le même jour", [
   "C'est le levier le plus efficace. Le déplacement n'étant facturé qu'une fois, traiter le canapé, un matelas et un tapis dans la même intervention revient bien moins cher que trois passages séparés."]),
  ("Ce qu'un prix trop bas cache généralement", [
   "En dessous d'une vingtaine d'euros pour un canapé, la prestation est presque toujours un shampoing de surface : la mousse est appliquée puis aspirée à sec, sans traitement du cœur de la fibre. Le résultat est visible une semaine, puis les taches remontent."])],
 "faq": [
  ("Combien de temps sèche un canapé après nettoyage ?",
   "De 4 à 6 h selon la ventilation de la pièce. L'injection-extraction réaspire immédiatement la solution injectée : le textile ressort humide, pas trempé."),
  ("Les taches anciennes partent-elles ?",
   "Souvent, mais pas systématiquement. Une auréole déjà créée par un détachant ménager ou une décoloration ne se rattrapent pas. Nous vous le disons avant l'intervention plutôt qu'après."),
  ("Les produits sont-ils sans danger pour les enfants et les animaux ?",
   "Oui, ils sont choisis pour cela. Quand la vapeur haute température suffit, nous nous passons complètement de produit.")],
 "service": "nettoyage-textile-paris",
},
{
 "slug": "prix-nettoyage-voiture-domicile",
 "cat": "Prix",
 "h1": "Combien coûte un nettoyage de voiture à domicile ?",
 "title": "Prix d'un nettoyage auto à domicile à Paris — de 40 à 240 € | MathClean",
 "meta": "Tarifs du detailing automobile à domicile en Île-de-France : 4 formules de 40 à 240 € selon le véhicule. Options, durée et ce qui est inclus.",
 "image": "auto-interieur-vw.webp",
 "lead": "Quatre formules, de la carrosserie seule au véhicule entier. Le prix varie surtout selon la taille du véhicule et la présence de cuir.",
 "sections": [
  ("Les quatre formules", [
   "Extérieur Éclat, de 40 à 90 € : lavage complet, jantes, brillant pneus, vitres extérieures, séchage sans trace. Intérieur Essentiel, de 50 à 120 € : aspiration habitacle et coffre, tableau de bord, plastiques, vitres, désinfection vapeur.",
   "Intérieur Prestige, de 90 à 180 € : tout l'Essentiel, plus le traitement des cuirs ou le pressing des sièges tissu, les tapis, le ciel de toit, les battements de portes. Intégral, de 120 à 240 € : le véhicule entier, dedans comme dehors."]),
  ("Pourquoi une fourchette et pas un prix fixe", [
   "Le bas de chaque fourchette correspond à une citadine, le haut à un SUV ou un monospace. Ce n'est ni la même surface ni le même temps. Le montant exact vous est confirmé avant l'intervention, jamais après."]),
  ("Les options", [
   "Retrait des poils d'animaux : 10 €. Traitement cuir et alcantara : 20 €. Neutralisation des odeurs par ozone : 30 €, pour un traitement d'une heure qui élimine odeurs, bactéries et moisissures.",
   "C'est cette dernière option qui fait la différence avant une revente : l'odeur est ce qui se juge en trois secondes à l'ouverture de la portière."]),
  ("Ce que comprend une prestation sans option", [
   "Aspiration complète de l'habitacle et du coffre — le coffre est toujours compris, sans supplément —, shampoing des tapis et moquettes, puis désinfection des allergènes et acariens par vapeur haute température."])],
 "faq": [
  ("Faut-il une prise électrique ou un point d'eau ?",
   "Non. Nous venons autonomes en eau et en électricité, ce qui permet d'intervenir en parking souterrain, en pied d'immeuble ou sur un parking d'entreprise."),
  ("Combien de temps dure l'intervention ?",
   "De 1 h 30 pour un Extérieur Éclat à environ 4 h pour un Intégral sur grand véhicule."),
  ("Est-ce rentable avant une revente ?",
   "C'est l'usage le plus fréquent de nos clients. Un habitacle assaini et sans odeur pèse concrètement sur le prix accepté par l'acheteur.")],
 "service": "nettoyage-automobile-paris",
},
{
 "slug": "injection-extraction",
 "cat": "Méthode",
 "h1": "L'injection-extraction expliquée simplement",
 "title": "Injection-extraction : comment ça marche et pourquoi ça ne fait pas d'auréole | MathClean",
 "meta": "L'injection-extraction expliquée : principe, différence avec le shampoing de surface, temps de séchage, matières traitables. Nettoyage textile à domicile en Île-de-France.",
 "image": "tapis-karcher.webp",
 "lead": "C'est la méthode de référence pour le textile. Son principe tient en une phrase, et il explique pourquoi elle ne laisse pas d'auréole.",
 "sections": [
  ("Le principe", [
   "Une solution nettoyante est injectée sous pression au cœur de la fibre, puis immédiatement réaspirée avec la saleté qu'elle vient de dissoudre. Injection et extraction se font dans le même geste, à quelques centimètres d'écart.",
   "C'est cette simultanéité qui fait tout : le textile n'a jamais le temps de se gorger d'eau."]),
  ("Pourquoi les auréoles n'apparaissent pas", [
   "Une auréole se forme quand l'eau migre vers les bords de la zone humide en emportant la saleté dissoute, puis sèche sur place en laissant un cerne. C'est le mécanisme de tout nettoyage trop mouillé.",
   "En réaspirant immédiatement, l'injection-extraction supprime la migration. Le textile ressort humide, pas trempé, et sèche en 4 à 6 h selon la ventilation."]),
  ("La différence avec un shampoing de surface", [
   "Le shampoing applique une mousse qu'on laisse sécher avant d'aspirer. Il nettoie ce qui se voit, en surface, et laisse des résidus de détergent dans la fibre — résidus qui retiennent la poussière et font remonter les taches en une à deux semaines.",
   "C'est la raison pour laquelle un canapé « nettoyé » à bas prix redevient sale très vite."]),
  ("Ce qui se traite, et ce qui ne se traite pas ainsi", [
   "Canapés en tissu, matelas, tapis, moquettes, fauteuils, sièges de voiture, selleries textiles : oui. Le cuir, non — il demande un nettoyage doux suivi d'un nourrissage.",
   "Sur laine et sur soie, un test de solidité des couleurs sur zone cachée est indispensable avant tout passage : certaines teintures dégorgent au contact de l'eau."])],
 "faq": [
  ("Puis-je louer une machine et le faire moi-même ?",
   "C'est possible, mais deux écueils reviennent : un mauvais dosage laisse du détergent dans la fibre, et une extraction insuffisante laisse le textile trop humide, donc auréolé. Sur un textile de valeur, l'essai raté coûte souvent plus que l'intervention."),
  ("Faut-il aspirer avant ?",
   "Oui, systématiquement, et c'est fait dans la prestation. Injecter sur une fibre chargée de poussière revient à transformer cette poussière en boue."),
  ("Combien de passages faut-il ?",
   "Autant que nécessaire pour que l'eau réaspirée ressorte claire. Sur un canapé très encrassé, cela peut demander plusieurs passages croisés.")],
 "service": "nettoyage-textile-paris",
},
{
 "slug": "nettoyage-vapeur-desinfection",
 "cat": "Méthode",
 "h1": "Nettoyage vapeur : ce qu'il désinfecte vraiment",
 "title": "Nettoyage vapeur : ce qu'il désinfecte vraiment, et ses limites | MathClean",
 "meta": "Ce que la vapeur haute température désinfecte réellement, sur quelles surfaces, et où elle ne suffit pas. Sans produit chimique, à Paris et en Île-de-France.",
 "image": "intervention-3.webp",
 "lead": "La vapeur désinfecte par la chaleur seule, sans aucun produit. C'est un atout réel — à condition de savoir où elle s'applique et où elle ne suffit pas.",
 "sections": [
  ("Le principe : la chaleur, pas le produit", [
   "La vapeur sèche est projetée à haute température. Ce sont la chaleur et la pression qui décollent les corps gras et détruisent une grande partie des micro-organismes de surface, sans qu'aucune molécule chimique n'intervienne.",
   "L'avantage est direct : aucun résidu. C'est ce qui la rend précieuse en environnement alimentaire, sur les surfaces que touchent les enfants, et là où quelqu'un est sensible aux produits."]),
  ("Où elle excelle", [
   "La graisse cuite d'une plancha ou d'une hotte, que les dégraissants peinent à décoller. Les joints de carrelage. Les sanitaires. L'habitacle d'une voiture — sièges, volant, plastiques — où elle assainit sans détremper.",
   "Sur les textiles, elle élimine acariens et allergènes par la chaleur, ce qui en fait le complément naturel de l'injection-extraction sur un matelas."]),
  ("Ses limites, qu'il faut connaître", [
   "La vapeur ne remplace pas une extraction : elle assainit, elle n'évacue pas la saleté du cœur d'une fibre. Sur un canapé encrassé, la vapeur seule assainit sans nettoyer.",
   "Elle ne convient pas non plus à toutes les surfaces : certains bois, certains vernis et certains plastiques fins supportent mal la chaleur. Le diagnostic préalable n'est pas une formalité."]),
  ("Vapeur ou produit : comment on tranche", [
   "La règle que nous appliquons est simple : quand la vapeur suffit, nous nous passons de produit. Quand elle ne suffit pas, nous employons un produit adapté à la matière, et nous le disons."])],
 "faq": [
  ("La vapeur tue-t-elle vraiment les bactéries ?",
   "Elle réduit fortement la charge microbienne des surfaces par la chaleur. Ce n'est pas une stérilisation au sens médical, et aucun prestataire sérieux ne l'annoncera comme telle."),
  ("Peut-on utiliser la vapeur sur un parquet ?",
   "Avec prudence. Sur un parquet vitrifié en bon état, oui, en passage rapide. Sur un parquet huilé, ancien ou dont les joints sont ouverts, l'humidité pose problème."),
  ("La vapeur laisse-t-elle de l'humidité ?",
   "Très peu : la vapeur sèche contient une faible proportion d'eau liquide. Les surfaces sont sèches en quelques minutes.")],
 "service": "nettoyage-automobile-paris",
},
{
 "slug": "eau-osmosee-vitres",
 "cat": "Vitrerie",
 "h1": "Eau osmosée : pourquoi elle supprime les traces sur les vitres",
 "title": "Eau osmosée pour vitres : pourquoi elle ne laisse aucune trace | MathClean",
 "meta": "Pourquoi l'eau osmosée sèche sans laisser de trace sur une vitre, et pourquoi les produits vitres du commerce font resalir plus vite. Explication et méthode.",
 "image": "vitre-controle.webp",
 "lead": "Une vitre garde des traces pour trois raisons, et l'eau osmosée en supprime deux d'un coup.",
 "sections": [
  ("Les trois causes des traces", [
   "L'eau du robinet, très calcaire en Île-de-France : en séchant, elle abandonne ses minéraux sur le verre. Les produits ménagers, dont les tensioactifs laissent un film mince. Et le plein soleil, qui fait sécher l'eau avant qu'on ait pu la racler.",
   "Les deux premières se règlent par l'eau osmosée. La troisième se règle en choisissant son moment."]),
  ("Ce qu'est l'osmose inverse", [
   "L'eau est poussée à travers une membrane qui retient les minéraux dissous. Ce qui en ressort est une eau pure, dépourvue de calcaire.",
   "En séchant, cette eau ne dépose rien du tout — puisqu'elle ne contient rien. C'est aussi simple que cela."]),
  ("Pourquoi on peut alors se passer de produit", [
   "L'eau pure a une forte capacité à capter les salissures : elle « cherche » à se recharger en particules. Associée au brossage, elle nettoie sans détergent.",
   "Et sans détergent, pas de film résiduel : la vitre reste propre plus longtemps qu'après un nettoyage classique."]),
  ("Où cela change tout", [
   "Sur les grandes surfaces, les vérandas, les verrières et les vitrines, où la reprise à la raclette est impossible ou trop lente. Et en hauteur, où la perche télescopique alimentée en eau pure permet de travailler depuis le sol."])],
 "faq": [
  ("L'eau osmosée est-elle plus écologique ?",
   "Sur le principe, oui : aucun détergent ne part à l'égout. La production d'eau osmosée consomme en revanche un volume d'eau supérieur à ce qu'elle produit."),
  ("Peut-on en faire chez soi ?",
   "Des osmoseurs domestiques existent, mais le débit nécessaire pour laver des vitres suppose un matériel professionnel."),
  ("Faut-il essuyer après ?",
   "Non, et c'est tout l'intérêt : on laisse sécher. Essuyer reviendrait à réintroduire des fibres et des traces.")],
 "service": "nettoyage-vitres-paris",
},
{
 "slug": "nettoyage-fin-chantier-combien-de-passages",
 "cat": "Chantier",
 "h1": "Nettoyage de fin de chantier : un ou deux passages ?",
 "title": "Nettoyage de fin de chantier : un ou deux passages ? | MathClean",
 "meta": "Pourquoi la poussière de chantier revient après le premier nettoyage, et quand prévoir un second passage. Remise en état après travaux à Paris et en Île-de-France.",
 "image": "intervention-1.webp",
 "lead": "C'est la question que posent tous les artisans et toutes les agences. La réponse dépend d'un phénomène simple : la poussière de chantier ne retombe pas en une journée.",
 "sections": [
  ("Pourquoi la poussière revient", [
   "La poussière de chantier n'est pas de la poussière domestique. Fine, chargée de plâtre et de silice, elle reste en suspension longtemps et se redépose progressivement pendant plusieurs jours après la fin des travaux.",
   "Un nettoyage effectué le lendemain de la dernière intervention d'un corps de métier sera donc suivi d'un redépôt visible — ce n'est pas un défaut de prestation, c'est de la physique."]),
  ("Un seul passage : dans quels cas", [
   "Sur un chantier léger — rafraîchissement, peinture d'une pièce, pose de sol sans découpe — un passage unique suffit, à condition de le programmer au moins 48 h après la fin des travaux.",
   "C'est aussi le choix raisonnable quand la livraison n'est pas immédiate : le bien restera fermé, la poussière retombera, un coup d'aspirateur suffira."]),
  ("Deux passages : dans quels cas", [
   "Sur une rénovation lourde, avec dépose de cloisons, ponçage ou découpe, deux passages sont la norme : un gros nettoyage, puis une finition quelques jours plus tard.",
   "C'est impératif si le bien est livré, visité ou photographié juste après. Un logement dont les plinthes reblanchissent le jour de la remise des clés fait mauvais effet."]),
  ("Comment on travaille pour limiter le redépôt", [
   "De haut en bas, systématiquement, et pièce par pièce en fermant derrière soi. Avec des aspirateurs à filtration fine, pour ne pas remettre en suspension ce qui vient d'être retiré.",
   "Les résidus de colle, projections de peinture, étiquettes et films de protection se traitent un par un — c'est ce qui distingue une remise en état d'un simple balayage."])],
 "faq": [
  ("Évacuez-vous les gravats ?",
   "Nous évacuons les résidus fins et les protections de chantier. Les gravats lourds relèvent d'une benne, à prévoir séparément."),
  ("Combien de temps prend une remise en état ?",
   "Une journée complète est courante pour un appartement après rénovation lourde. Le devis est établi après état des lieux, selon la surface et la nature des travaux."),
  ("Intervenez-vous pour les artisans et les agences ?",
   "Régulièrement : entreprises du bâtiment, architectes d'intérieur, agences immobilières et syndics, avec facturation entreprise et devis ferme.")],
 "service": "nettoyage-fin-de-chantier-paris",
},
{
 "slug": "frequence-nettoyage-bureaux",
 "cat": "Professionnels",
 "h1": "À quelle fréquence faire nettoyer ses bureaux ?",
 "title": "Fréquence de nettoyage des bureaux : le bon rythme selon l'effectif | MathClean",
 "meta": "Quotidien, trois fois par semaine ou hebdomadaire : comment déterminer la bonne fréquence d'entretien de bureaux selon l'effectif et l'usage. Devis gratuit en Île-de-France.",
 "image": "bureau-entreprise.webp",
 "lead": "La fréquence ne se déduit pas de la surface mais du nombre de passages. Voici comment la calculer, poste par poste.",
 "sections": [
  ("Les sanitaires donnent le rythme", [
   "Ce sont eux qui déterminent la fréquence minimale, pas les bureaux. Au-delà d'une vingtaine de personnes, un passage quotidien devient difficile à éviter ; en dessous de dix, trois passages hebdomadaires suffisent généralement.",
   "C'est aussi le poste sur lequel les remarques remontent le plus vite en interne."]),
  ("Les postes de travail et les circulations", [
   "Un dépoussiérage et un passage sur les sols deux à trois fois par semaine couvrent la plupart des situations en bureau classique. Le quotidien se justifie surtout en open space dense ou en accueil de public."]),
  ("La cuisine et les espaces de pause", [
   "Ils se salissent vite et se voient beaucoup. Un passage quotidien y est presque toujours pertinent, même quand le reste des locaux est traité moins souvent."]),
  ("Les prestations périodiques, à ne pas oublier", [
   "Certaines opérations ne relèvent pas de la fréquence courante : moquettes en injection-extraction une à deux fois par an, vitrerie complète deux à quatre fois par an, dégraissage de cuisine professionnelle selon l'activité.",
   "Elles doivent figurer séparément au contrat, sinon elles ne sont jamais faites."])],
 "faq": [
  ("Intervenez-vous en dehors des heures d'ouverture ?",
   "Oui, tôt le matin, après la fermeture ou de nuit. C'est même la règle pour les commerces et les restaurants."),
  ("Peut-on commencer par un passage ponctuel ?",
   "Oui, et c'est souvent le bon point de départ : une remise à niveau permet de voir le résultat avant de s'engager sur un rythme régulier."),
  ("Comment est établi le devis ?",
   "Après visite des locaux : surfaces, zones, contraintes d'accès et d'horaires. Un devis fait sans visite reste une approximation.")],
 "service": "nettoyage-entreprise-paris",
},
{
 "slug": "devis-nettoyage-questions-a-poser",
 "cat": "Bien choisir",
 "h1": "Devis de nettoyage : les 7 questions à poser avant de signer",
 "title": "Devis de nettoyage : les 7 questions à poser avant de signer | MathClean",
 "meta": "Les sept questions qui révèlent la qualité d'un devis de nettoyage : méthode, déplacement, acompte, assurance, durée, intervenant, garantie.",
 "image": "intervention-2.webp",
 "lead": "Un devis se juge moins à son montant qu'à ce qu'il précise. Sept questions suffisent à faire le tri.",
 "sections": [
  ("1. Quelle méthode exactement ?", [
   "« Nettoyage de canapé » ne dit rien. Injection-extraction, shampoing de surface, vapeur : ce ne sont ni les mêmes résultats, ni les mêmes durées de séchage, ni les mêmes prix. Faites préciser."]),
  ("2. Les frais de déplacement sont-ils inclus ?", [
   "C'est le poste qui réapparaît le plus souvent le jour de l'intervention. S'ils ne sont pas inclus, demandez la règle de calcul et le montant pour votre adresse."]),
  ("3. Y a-t-il un acompte ?", [
   "Un règlement après intervention, une fois le résultat constaté, est un signal de confiance dans la prestation."]),
  ("4. Êtes-vous assuré, et pouvez-vous me le prouver ?", [
   "L'attestation de responsabilité civile professionnelle se fournit en une minute. Une hésitation sur ce point est une réponse en soi."]),
  ("5. Combien de temps cela va-t-il prendre ?", [
   "Une estimation de durée engage. Elle vous permet aussi d'organiser votre journée, et de repérer les prestations expédiées."]),
  ("6. Qui interviendra ?", [
   "La sous-traitance en cascade est fréquente. Savoir si votre interlocuteur sera aussi l'exécutant change la continuité de l'information — et le résultat."]),
  ("7. Que se passe-t-il si je ne suis pas satisfait ?", [
   "La réponse importe moins que la franchise : un prestataire sérieux vous dit avant l'intervention ce qui partira et ce qui ne partira pas, plutôt que de promettre l'impossible."])],
 "faq": [
  ("Un devis de nettoyage est-il payant ?",
   "Il ne devrait jamais l'être pour une prestation courante. Chez MathClean, le devis est gratuit et sans engagement."),
  ("Combien de temps un devis reste-t-il valable ?",
   "La durée de validité doit être écrite sur le document. Un mois est une pratique courante."),
  ("Peut-on obtenir un devis à distance ?",
   "Pour les prestations à domicile, oui : quelques photos suffisent le plus souvent. Pour les locaux professionnels, une visite reste préférable.")],
 "service": "nettoyage-entreprise-paris",
},
]
