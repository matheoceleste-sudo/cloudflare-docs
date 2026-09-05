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
        "title": "Nettoyage automobile à Paris — dès 40 €",
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
        "title": "Nettoyage canapé et matelas à Paris",
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
        "title": "Nettoyage de bateau à Paris et en IDF",
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
        "title": "Nettoyage de terrasse à Paris — anti-mousse",
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
        "title": "Nettoyage de vitres à Paris — sans trace",
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
        "title": "Nettoyage pour entreprise à Paris",
        "meta": "Nettoyage pour entreprise à Paris et en IDF : bureaux, commerces, restaurants, locaux. Passage ponctuel ou régulier, horaires décalés.",
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
        "slug": "traitement-ozone-paris",
        "short": "Ozone",
        "nav": "Traitement par ozone",
        "name": "Traitement par ozone à Paris",
        "h1": "Traitement par ozone : neutraliser les odeurs à la source",
        "title": "Traitement ozone à Paris — odeurs traitées",
        "meta": "Traitement par ozone à Paris et en IDF : tabac, animaux, humidité, cuisine. Odeurs détruites à la source, pas masquées. Dès 30 €.",
        "price": "dès 30 €",
        "excerpt": "Tabac, animaux, humidité, cuisine, fumée : l'ozone détruit les molécules odorantes au lieu de les masquer. Véhicule, appartement, local ou chambre.",
        "image": "intervention-3.webp",
        "hero": "intervention-3.webp",
        "icon": "ozone",
        "intro": [
            "Un désodorisant masque. L'ozone, lui, oxyde : la molécule responsable de l'odeur est "
            "détruite, elle ne revient pas quand le parfum s'estompe. C'est la différence entre "
            "couvrir une odeur de tabac et la faire disparaître.",
            "Le gaz pénètre partout où l'air circule — mousse de siège, ciel de toit, tissus, "
            "conduits de ventilation, recoins — c'est-à-dire là où aucun nettoyage de surface "
            "n'atteint. Puis il se recombine naturellement en oxygène en quelques heures.",
        ],
        "included_title": "Ce que l'ozone traite réellement",
        "included": [
            "Odeur de <strong>tabac</strong> incrustée dans les textiles et les mousses",
            "Odeurs d'<strong>animaux</strong>, y compris l'urine une fois la source retirée",
            "Odeurs d'<strong>humidité</strong> et de moisissure après dégât des eaux",
            "Odeurs de <strong>cuisine</strong> ou de friture dans un logement ou un local",
            "Odeur de <strong>fumée</strong> après un début d'incendie",
        ],
        "steps": [
            ("Nettoyage préalable",
             "L'ozone ne nettoie pas : il traite l'air et les surfaces qu'il atteint. Si la source "
             "de l'odeur est encore là — un textile imprégné, un tapis souillé — elle doit être "
             "traitée d'abord, sinon l'odeur revient."),
            ("Mise en sécurité",
             "Le local ou le véhicule est vidé : personne à l'intérieur, ni animaux ni plantes. "
             "C'est une règle absolue, sur laquelle nous ne transigeons pas."),
            ("Traitement",
             "Le générateur tourne en espace clos, une heure environ pour un habitacle de voiture, "
             "davantage selon le volume pour une pièce ou un local."),
            ("Aération et restitution",
             "Nous aérons, et nous attendons que l'ozone se soit recombiné en oxygène avant de vous "
             "rendre les lieux. Vous ne récupérez jamais un espace encore chargé."),
        ],
        "faq": [
            ("L'ozone est-il dangereux ?",
             "Oui, pendant le traitement : c'est un gaz irritant pour les voies respiratoires, et "
             "l'ANSES le rappelle régulièrement. C'est précisément pourquoi il se manipule en espace "
             "vide, sans personne, sans animaux et sans plantes, suivi d'une aération. Une fois "
             "recombiné en oxygène, il ne laisse aucun résidu."),
            ("Combien de temps avant de pouvoir réutiliser les lieux ?",
             "Comptez environ deux heures après la fin du traitement pour un habitacle de voiture, "
             "davantage pour une pièce. Nous ne restituons jamais un espace avant que l'aération "
             "soit faite."),
            ("L'ozone remplace-t-il un nettoyage ?",
             "Non, et personne ne devrait vous le vendre ainsi. Il traite les odeurs, pas la "
             "saleté. Sur un habitacle encrassé, le nettoyage vient d'abord, l'ozone ensuite."),
            ("Est-ce que l'odeur peut revenir ?",
             "Seulement si la source est toujours présente. Une moquette imprégnée d'urine "
             "continuera d'émettre tant qu'elle n'aura pas été traitée. C'est pour cela que nous "
             "diagnostiquons avant de proposer l'ozone."),
            ("Traitez-vous les appartements et les locaux ?",
             "Oui : logements, chambres d'hôtel, commerces, restaurants, véhicules. Le tarif dépend "
             "du volume à traiter et s'établit sur devis, sauf pour l'habitacle automobile, "
             "proposé à 30 € en option d'un nettoyage."),
        ],
    },
    {
        "slug": "nettoyage-fin-de-chantier-paris",
        "short": "Fin de chantier",
        "nav": "Fin de chantier",
        "name": "Nettoyage fin de chantier à Paris",
        "h1": "Nettoyage de fin de chantier et remise en état après travaux",
        "title": "Nettoyage fin de chantier à Paris",
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
    ("Traitement par ozone (local, logement)", "Odeurs neutralisées à la source", "traitement-ozone-paris"),
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
    # Les quatre premières sont en haute définition (700 px et plus) : ce sont
    # celles que l'accueil affiche. Les quatre suivantes sont d'anciennes
    # miniatures (192 px) — elles restent visibles sur la page Réalisations,
    # dans une grille plus étroite, en attendant des clichés de meilleure
    # définition. Voir la note « Photos à remplacer » du README.
    ('avant-voiture-siege.webp', 'apres-voiture-siege.webp', 'Siège automobile', 'Shampoing et détachage des tissus'),
    ('ba-terrasse2-avant.webp', 'ba-terrasse2-apres.webp', 'Terrasse en marbre', 'Haute pression : la pierre retrouve sa blancheur'),
    ('avant-frigo.webp', 'apres-frigo.webp', 'Réfrigérateur professionnel', 'Nettoyage complet, hygiène alimentaire'),
    ('avant-plan-travail.webp', 'apres-plan-travail.webp', 'Plan de travail', 'Dégraissage et désinfection en profondeur'),
    ('ba-canape-avant.webp', 'ba-canape-apres.webp', 'Canapé en tissu', 'Injection-extraction et désinfection'),
    ('ba-tapis-avant.webp', 'ba-tapis-apres.webp', 'Tapis et moquette', 'Shampoing et détachage en profondeur'),
    ('ba-terrasse-avant.webp', 'ba-terrasse-apres.webp', 'Terrasse extérieure', 'Haute pression et traitement anti-mousse'),
    ('ba-fauteuil-avant.webp', 'ba-fauteuil-apres.webp', 'Fauteuil de bureau', 'Détachage et assainissement des tissus'),
]

# Nombre de paires en haute définition, affichées en grand.
BEFORE_AFTER_HD = 4

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
            ('h2', 'Les trois gestes qui changent tout'),
            ('p', "Le premier est de traiter immédiatement ce qui est corrosif : fientes d'oiseau, sève d'arbre, insectes écrasés. Ce ne sont pas des salissures ordinaires, ce sont des agents acides qui attaquent le vernis en quelques jours au soleil. Une lingette gardée dans la boîte à gants suffit, à condition de s'en servir le jour même."),
            ('p', "Le deuxième est de ne jamais essuyer une carrosserie sèche et poussiéreuse. C'est l'origine de la quasi-totalité des micro-rayures circulaires qu'on voit au soleil sur les teintes foncées. Sans lubrification, un chiffon promène la poussière sur le vernis comme un abrasif."),
            ('p', "Le troisième est d'aspirer l'habitacle plus souvent qu'on ne le lave. Le sable et le gravier ramenés sous les semelles scient les fibres des tapis et des moquettes à chaque appui du pied. Une voiture dont l'intérieur est aspiré tous les quinze jours vieillit visiblement mieux."),
            ('h2', "La protection, et ce qu'on peut en attendre"),
            ('p', "Une cire ou un scellant appliqué après lavage crée une couche sacrificielle : l'eau perle, la saleté adhère moins, et le lavage suivant demande moins de frottement. C'est là que se trouve le vrai bénéfice — moins d'agression mécanique à chaque entretien, donc un vernis qui garde sa profondeur."),
            ('p', "La durée dépend du produit et de l'exposition : quelques semaines pour une cire classique, plusieurs mois pour un scellant synthétique. Aucune protection ne dispense de laver ; elle rend simplement chaque lavage moins agressif."),
            ('p', "Un mot sur ce qu'elle ne fait pas : une protection ne comble pas une rayure existante et ne protège pas d'un impact. Ce qui a traversé le vernis relève du carrossier, pas de l'entretien."),
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
            ('h2', 'Ce qui use réellement un bateau entre deux sorties'),
            ('p', "Le sel est le premier ennemi, et pas seulement pour la corrosion visible. Il se dépose en cristaux fins qui retiennent l'humidité contre le métal et dans les coutures de la sellerie. Un rinçage à l'eau douce après chaque sortie, même rapide, fait plus pour la longévité du bateau que le meilleur nettoyage annuel."),
            ('p', "Le second est l'ultraviolet. Il craquelle les vinyles de sellerie, ternit le gelcoat et fragilise les cordages. Une taud de mouillage ou une simple bâche coûte peu et repousse l'échéance de plusieurs saisons."),
            ('p', "Le troisième, moins évoqué, est l'humidité confinée. Un bateau fermé sans ventilation développe des moisissures dans les coussins et les équipets, particulièrement pendant l'hivernage. Ouvrir les coffres et laisser circuler l'air lors des visites d'hiver change tout."),
            ('h2', "L'hivernage, moment clé"),
            ('p', "C'est le seul moment où l'on peut travailler sereinement sur la coque hors d'eau. Le nettoyage de la carène, le lustrage du gelcoat et la remise en état de la sellerie se font bien mieux à terre qu'à flot, et sans la contrainte de la météo."),
            ('p', "Un point de méthode : ne rangez jamais une sellerie encore humide. La moisissure qui s'installe dans une mousse fermée tout un hiver ne se rattrape pas au printemps. Nettoyez, séchez complètement à l'air libre, puis remisez."),
            ('p', "Quand une odeur de renfermé persiste malgré tout au printemps, un traitement par ozone la traite efficacement — bateau vide, sans présence humaine ni animale pendant l'opération, puis aération avant utilisation."),
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
# Date de première mise en ligne des guides (elles ont toutes été écrites
# le même jour). Sert de datePublished dans les données structurées.
DATE_GUIDES = "2026-09-05"
DATE_GUIDES_FR = "5 septembre 2026"

GUIDES = [
{
 "slug": "choisir-entreprise-nettoyage-ile-de-france",
 "cat": "Bien choisir",
 "h1": "Comment choisir une entreprise de nettoyage en Île-de-France",
 "title": "Choisir son entreprise de nettoyage en IDF",
 "meta": "Les sept critères d'une entreprise de nettoyage sérieuse en Île-de-France : devis ferme, assurance, matériel, acompte, avis vérifiables.",
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
 "title": "Choisir une entreprise de nettoyage à Paris",
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
 "title": "Entreprise de nettoyage de vitres à Paris",
 "meta": "Ce qui sépare un laveur de vitres généraliste d'une entreprise spécialisée : eau osmosée, perche télescopique, contrôle en lumière rasante.",
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
 "title": "Entreprise professionnelle de nettoyage",
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
 "title": "Prix d'un nettoyage de canapé à Paris",
 "meta": "Prix d'un nettoyage de canapé à domicile à Paris : 39 € le 2 places, 49 € le 3 places, 69 € l'angle. Ce qui fait varier le tarif.",
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
 "title": "Prix d'un nettoyage auto à domicile",
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
 "slug": "entreprise-traitement-ozone-paris",
 "cat": "Ozone",
 "h1": "Entreprise de traitement ozone à Paris : comment choisir",
 "title": "Entreprise de traitement ozone à Paris",
 "meta": "Choisir une entreprise de traitement ozone à Paris : protocole de sécurité, diagnostic préalable, tarifs, durée. Ce qu'un prestataire sérieux doit vous dire.",
 "image": "intervention-3.webp",
 "lead": "Le traitement à l'ozone s'est banalisé, et avec lui les promesses excessives. Voici comment reconnaître une entreprise qui maîtrise réellement le procédé.",
 "sections": [
  ("Elle commence par un diagnostic, pas par le générateur", [
   "L'ozone traite les odeurs, il ne retire pas la source. Une moquette imprégnée d'urine, un textile saturé de nicotine, une zone humide encore active continueront d'émettre une fois le traitement terminé.",
   "Un prestataire sérieux identifie d'abord d'où vient l'odeur, dit ce qui doit être nettoyé ou retiré avant, et n'annonce l'ozone qu'ensuite. Celui qui propose l'ozone au téléphone sans rien avoir vu vend un traitement, pas un résultat."]),
  ("Elle vous parle spontanément de sécurité", [
   "L'ozone est un gaz irritant pour les voies respiratoires ; l'ANSES le rappelle régulièrement dans ses avis sur les épurateurs d'air. Le traitement se fait donc en espace clos et vide : personne à l'intérieur, ni animaux ni plantes.",
   "Une entreprise qui n'aborde pas ce point de sa propre initiative, ou qui vous laisse entendre que vous pouvez rester sur place, ne connaît pas son sujet. C'est le filtre le plus efficace."]),
  ("Elle prévoit l'aération dans le temps d'intervention", [
   "Après le traitement, l'ozone se recombine naturellement en oxygène — mais cela prend du temps. Comptez environ deux heures pour un habitacle de voiture, davantage pour une pièce.",
   "Ce délai fait partie de la prestation. Un prestataire qui vous rend les clés immédiatement après avoir coupé le générateur vous fait prendre un risque inutile."]),
  ("Elle ne promet pas de désinfection", [
   "Les allégations biocides et virucides sont encadrées par le règlement européen 528/2012. Annoncer « élimine 99,9 % des virus » sur une prestation d'ozone est juridiquement exposé, et invérifiable dans les conditions réelles d'un appartement ou d'un habitacle.",
   "Ce que l'ozone fait très bien, en revanche, c'est détruire les molécules odorantes. C'est déjà beaucoup, et cela se constate immédiatement."]),
  ("À Paris : la contrainte du lieu clos", [
   "En appartement, le traitement suppose de quitter les lieux pendant sa durée, aération comprise. En copropriété, mieux vaut prévenir : l'odeur caractéristique de l'ozone peut se percevoir sur un palier.",
   "Pour un véhicule, un parking souterrain fermé convient parfaitement — c'est même le cas le plus simple, et le plus fréquent à Paris."])],
 "faq": [
  ("Combien coûte un traitement ozone à Paris ?",
   "Chez MathClean, 30 € en option d'un nettoyage automobile, pour un traitement d'environ une heure. Pour une pièce, un logement ou un local, le tarif dépend du volume et s'établit sur devis gratuit."),
  ("Faut-il quitter les lieux ?",
   "Oui, sans exception, pendant le traitement et pendant l'aération qui suit. C'est la seule façon de procéder correctement."),
  ("L'odeur peut-elle revenir après le traitement ?",
   "Seulement si la source est toujours en place. C'est pourquoi le diagnostic préalable compte plus que la puissance du générateur.")],
 "service": "traitement-ozone-paris",
},
{
 "slug": "traitement-ozone-ile-de-france",
 "cat": "Ozone",
 "h1": "Traitement ozone en Île-de-France : où, quand, combien de temps",
 "title": "Traitement ozone en Île-de-France",
 "meta": "Traitement par ozone dans les huit départements franciliens : véhicules, logements, chambres, commerces. Durées, délais d'intervention et frais de déplacement.",
 "image": "auto-interieur-vw.webp",
 "lead": "Nous traitons à l'ozone dans les huit départements franciliens. Voici ce que cela suppose selon le type de lieu, et combien de temps il faut y consacrer.",
 "sections": [
  ("Un véhicule : le cas le plus simple", [
   "Une heure de traitement, environ deux heures d'aération. Le véhicule peut rester où il est — devant chez vous, en parking souterrain, sur un parking d'entreprise — puisque nous venons avec notre propre matériel et notre propre alimentation.",
   "C'est le format que nous réalisons le plus souvent, généralement associé à un nettoyage intérieur : le nettoyage retire la source, l'ozone traite ce qui a imprégné les mousses et le ciel de toit."]),
  ("Un logement ou une chambre", [
   "La durée dépend du volume. Une chambre se traite en quelques heures, un appartement entier demande de fractionner ou d'allonger le temps de traitement.",
   "Vous devez pouvoir quitter les lieux sur cette durée, aération comprise. C'est la contrainte principale, et elle se planifie : beaucoup de nos clients font traiter pendant une journée d'absence."]),
  ("Un commerce, un restaurant, une chambre d'hôtel", [
   "Ces lieux se traitent hors des heures d'ouverture, souvent de nuit, ce qui règle la question de l'évacuation. Pour un hôtel, une chambre libérée le matin peut être remise en service dans la journée.",
   "En restauration, l'ozone intervient après le dégraissage : les odeurs de friture imprègnent les textiles et les conduits, que le nettoyage de surface n'atteint pas."]),
  ("Délais et déplacement", [
   "Comptez 24 à 48 h à Paris et en petite couronne, 48 à 72 h en grande couronne. Les frais de déplacement suivent la règle habituelle : 5 € par tranche de 5 km depuis notre atelier de Tremblay-en-France, annoncés avant validation.",
   "Le détail commune par commune figure sur nos pages villes."])],
 "faq": [
  ("Intervenez-vous dans toute l'Île-de-France ?",
   "Oui, dans les huit départements : Paris (75), Hauts-de-Seine (92), Seine-Saint-Denis (93), Val-de-Marne (94), Essonne (91), Yvelines (78), Seine-et-Marne (77) et Val-d'Oise (95)."),
  ("Peut-on traiter un logement occupé ?",
   "Pas pendant le traitement. Le logement doit être vide de ses occupants, de leurs animaux et de leurs plantes, et le rester jusqu'à la fin de l'aération."),
  ("Combien de temps faut-il prévoir en tout ?",
   "Pour un véhicule, une demi-journée en comptant l'aération. Pour un logement, cela se planifie selon le volume : nous vous le disons précisément au devis.")],
 "service": "traitement-ozone-paris",
},
{
 "slug": "traitement-ozone-voiture-odeurs",
 "cat": "Ozone",
 "h1": "Traitement ozone d'une voiture : tabac, animaux, humidité",
 "title": "Traitement ozone voiture — odeur de tabac",
 "meta": "Faire traiter sa voiture à l'ozone : odeur de tabac, d'animal ou d'humidité éliminée à la source. Durée, prix, protocole. À domicile en Île-de-France, dès 30 €.",
 "image": "auto-interieur-vw.webp",
 "lead": "C'est l'usage le plus fréquent de l'ozone, et le plus spectaculaire. Voici pourquoi il fonctionne là où l'aspiration et les désodorisants échouent.",
 "sections": [
  ("Pourquoi l'odeur résiste au nettoyage", [
   "Dans un habitacle, l'odeur ne tient pas seulement aux surfaces. Elle s'est fixée dans la mousse des sièges, dans le ciel de toit, dans la moquette du plancher, et surtout dans le circuit de ventilation — autant d'endroits qu'aucun passage d'aspirateur n'atteint.",
   "C'est ce qui explique le phénomène classique : la voiture sent bon deux jours, puis l'odeur revient dès qu'on met le chauffage."]),
  ("Ce que fait l'ozone", [
   "Le gaz circule partout où l'air circule, y compris dans les conduits de ventilation. Il oxyde les molécules odorantes : elles sont détruites, pas recouvertes.",
   "Une heure suffit pour un habitacle. Nous faisons tourner la ventilation pendant le traitement, précisément pour que le circuit d'air soit traité lui aussi."]),
  ("L'ordre compte : nettoyer d'abord", [
   "Si un tapis est imprégné, si un liquide a coulé sous un siège, la source est toujours là et l'odeur reviendra. Le nettoyage intérieur retire la matière ; l'ozone traite ce qui a imprégné.",
   "C'est pour cela que nous proposons l'ozone en option d'un nettoyage plutôt que seul : dans l'autre ordre, le résultat ne tient pas."]),
  ("Le cas de la revente", [
   "Un acheteur se fait un avis en trois secondes, à l'ouverture de la portière, sur une impression olfactive qu'il ne formulera jamais à voix haute. Une odeur de tabac ou d'animal coûte concrètement en négociation.",
   "L'association nettoyage intérieur plus ozone est, de loin, la préparation à la revente la plus rentable que nous réalisons."])],
 "faq": [
  ("Combien coûte un traitement ozone sur une voiture ?",
   "30 €, en option d'un nettoyage intérieur. Le traitement dure environ une heure, à laquelle s'ajoute l'aération."),
  ("L'odeur de tabac part-elle vraiment ?",
   "Dans la grande majorité des cas, oui, à condition que l'habitacle ait été nettoyé au préalable. Sur un véhicule fumé pendant des années, un second passage est parfois nécessaire."),
  ("Puis-je conduire juste après ?",
   "Non. Il faut laisser l'ozone se recombiner en oxygène et aérer, soit environ deux heures. Nous ne vous rendons jamais le véhicule avant.")],
 "service": "traitement-ozone-paris",
},
{
 "slug": "traitement-ozone-securite",
 "cat": "Ozone",
 "h1": "Traitement ozone : les règles de sécurité à connaître",
 "title": "Traitement ozone : les règles de sécurité",
 "meta": "L'ozone irrite les voies respiratoires. Les règles d'un traitement : local vide, aération, délai avant réoccupation. Ce que dit l'ANSES.",
 "image": "intervention-2.webp",
 "lead": "L'ozone est efficace, et il n'est pas anodin. Ces règles ne sont pas des précautions de confort : elles conditionnent la sécurité du traitement.",
 "sections": [
  ("Ce qu'est l'ozone, et pourquoi il agit", [
   "L'ozone est une molécule d'oxygène instable, composée de trois atomes au lieu de deux. C'est cette instabilité qui le rend efficace : il cède facilement un atome, oxydant au passage les molécules odorantes qu'il rencontre.",
   "La même instabilité explique sa toxicité : ce qu'il oxyde dans une molécule d'odeur, il l'oxyde aussi dans les tissus respiratoires."]),
  ("Personne dans le local, sans exception", [
   "Pendant le traitement, l'espace doit être vide : pas d'occupants, pas d'animaux, pas de plantes. Les animaux de petite taille et les oiseaux y sont particulièrement sensibles.",
   "Cette règle ne souffre aucune exception, quelle que soit la durée. Un prestataire qui vous laisse rester dans une pièce voisine mal isolée fait mal son travail."]),
  ("L'aération fait partie du traitement", [
   "Une fois le générateur arrêté, l'ozone ne disparaît pas instantanément : il se recombine progressivement en oxygène. Comptez environ deux heures pour un habitacle de voiture, davantage pour un volume plus grand.",
   "L'odeur caractéristique — proche de celle de l'air après un orage — est un indicateur utile : tant qu'elle est nette, l'aération n'est pas terminée."]),
  ("Ce que dit l'ANSES", [
   "L'agence a émis à plusieurs reprises des avis prudents sur les appareils émettant de l'ozone en présence humaine, en rappelant son caractère irritant pour les voies respiratoires et l'absence de bénéfice démontré comme purificateur d'air d'ambiance.",
   "Cela ne disqualifie pas l'ozone comme traitement d'odeurs en espace vide et ventilé ensuite — c'est un usage différent, ponctuel et encadré. Mais cela disqualifie l'idée d'un appareil à laisser tourner chez soi au quotidien."]),
  ("Les matériaux sensibles", [
   "L'ozone est un oxydant : à forte concentration et sur des durées longues, il peut altérer certains caoutchoucs, mousses et matières plastiques anciennes.",
   "Sur un véhicule ou un logement en bon état, aux durées usuelles, cela ne pose pas de difficulté. Sur un véhicule de collection ou des matériaux fragiles, cela se discute avant."])],
 "faq": [
  ("Peut-on acheter un générateur et le faire soi-même ?",
   "Techniquement oui, ces appareils sont en vente libre. Le risque n'est pas dans la machine mais dans le protocole : concentration, durée, évacuation des occupants, aération. C'est là que se jouent l'efficacité et la sécurité."),
  ("L'ozone laisse-t-il des résidus ?",
   "Non. Il se recombine en oxygène, sans dépôt ni film résiduel. C'est l'un de ses intérêts par rapport à un produit chimique."),
  ("Est-ce compatible avec la présence d'enfants dans le logement ?",
   "Après aération complète, oui, l'air est redevenu de l'air ordinaire. Pendant le traitement, non, et cela vaut pour tout le monde.")],
 "service": "traitement-ozone-paris",
},
{
 "slug": "prix-traitement-ozone",
 "cat": "Prix",
 "h1": "Combien coûte un traitement à l'ozone ?",
 "title": "Prix d'un traitement ozone — dès 30 €",
 "meta": "Prix d'un traitement ozone : 30 € en option d'un nettoyage automobile, sur devis pour un logement ou un local. Ce qui fait varier le tarif.",
 "image": "intervention-1.webp",
 "lead": "Le tarif dépend d'une seule variable réelle : le volume à traiter, qui détermine la durée.",
 "sections": [
  ("Le véhicule : 30 €", [
   "Chez MathClean, la neutralisation des odeurs par ozone est proposée à 30 €, en option de n'importe quelle formule de nettoyage automobile. Le traitement dure environ une heure, plus l'aération.",
   "Ce prix suppose que l'habitacle soit nettoyé : c'est le nettoyage qui retire la source, l'ozone qui traite ce qui a imprégné. Vendre l'ozone seul sur un habitacle encrassé serait vous facturer un résultat qui ne tiendra pas."]),
  ("Le logement, la chambre, le local : sur devis", [
   "Pour un volume plus important, la durée de traitement augmente, et avec elle le temps d'intervention. Une chambre, un studio et un local de 200 m² n'ont pas de commune mesure.",
   "Le devis est gratuit et s'établit après échange : volume, nature de l'odeur, contraintes d'accès et d'horaires."]),
  ("Ce qui fait vraiment varier le prix", [
   "Le volume, d'abord. L'ancienneté de l'odeur ensuite : un tabagisme de plusieurs années demande parfois deux passages. Et l'accessibilité, enfin — un local qu'on ne peut vider qu'entre minuit et six heures se planifie différemment.",
   "Les frais de déplacement s'ajoutent selon la règle habituelle : 5 € par tranche de 5 km depuis notre atelier, annoncés avant que vous validiez."]),
  ("Le piège du prix bas", [
   "Un traitement annoncé très bas est souvent un traitement trop court, ou réalisé sans le nettoyage préalable. Dans les deux cas, l'odeur revient — et vous avez payé deux fois.",
   "Demandez systématiquement la durée de traitement prévue et ce qui est fait avant. Les réponses vous renseigneront mieux que le prix."])],
 "faq": [
  ("Le traitement ozone est-il vendu seul ?",
   "Sur véhicule, nous le proposons en option d'un nettoyage, parce que c'est la seule façon d'obtenir un résultat durable. Sur logement ou local, il peut se traiter seul si la source de l'odeur a déjà été retirée."),
  ("Faut-il parfois deux passages ?",
   "Sur des odeurs très anciennes et très incrustées, cela arrive. Nous le disons au devis quand nous l'anticipons, plutôt que de le découvrir après."),
  ("Le devis est-il payant ?",
   "Non, il est gratuit et sans engagement, comme pour toutes nos prestations.")],
 "service": "traitement-ozone-paris",
},
{
 "slug": "injection-extraction",
 "cat": "Méthode",
 "h1": "L'injection-extraction expliquée simplement",
 "title": "Injection-extraction : comment ça marche",
 "meta": "L'injection-extraction expliquée : principe, différence avec le shampoing, temps de séchage, matières traitables. À domicile en IDF.",
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
 "title": "Nettoyage vapeur : ce qu'il fait vraiment",
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
 "title": "Eau osmosée pour vitres : pourquoi ça marche",
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
 "title": "Fin de chantier : un ou deux passages ?",
 "meta": "Pourquoi la poussière de chantier revient après le premier nettoyage, et quand prévoir un second passage. Remise en état en IDF.",
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
 "title": "Fréquence de nettoyage des bureaux",
 "meta": "Quotidien, trois fois par semaine ou hebdomadaire : trouver la bonne fréquence d'entretien de bureaux selon l'effectif et l'usage.",
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
 "title": "Devis de nettoyage : les 7 bonnes questions",
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

    # --- Pages issues de l'étude des requêtes les plus demandées en IDF ---
    {
        "slug": 'nettoyage-fin-de-bail-paris',
        "cat": 'Fin de bail',
        "h1": 'Nettoyage de fin de bail à Paris : récupérer sa caution',
        "title": 'Nettoyage de fin de bail à Paris',
        "meta": "Nettoyage de fin de bail à Paris : les points que l'état des lieux contrôle vraiment, ce qui fait retenir une caution, et ce que coûte l'intervention.",
        "image": 'intervention-2.webp',
        "lead": "Un état des lieux de sortie ne se joue pas sur l'impression générale, mais sur une poignée de points que les agences vérifient systématiquement. Voici lesquels, et comment les traiter.",
        "sections": [
            ('Ce que le bailleur peut réellement vous retenir', [
                "La loi du 6 juillet 1989 impose au locataire de rendre le logement « en bon état de propreté ». Le bailleur ne peut pas vous facturer l'usure normale — une moquette défraîchie après six ans, une peinture jaunie — mais il peut retenir sur le dépôt de garantie le coût d'un nettoyage que vous n'avez pas fait.",
                "Dans la pratique, la retenue est presque toujours calculée sur un devis d'entreprise, rarement sur le temps réel passé. C'est ce qui explique l'écart : un ménage que vous auriez fait faire pour 200 € vous est refacturé 400 € parce qu'il a été commandé dans l'urgence, après votre départ, sans que vous puissiez comparer.",
                "L'intérêt de faire nettoyer avant l'état des lieux est donc autant financier que pratique : vous choisissez le prestataire, vous voyez le résultat, et vous n'avez plus à discuter d'un devis établi sans vous.",
            ]),
            ("Les six points qui décident de l'état des lieux", [
                "Les agences parisiennes travaillent avec des grilles assez proches les unes des autres. Six postes reviennent systématiquement, et ce sont eux qui concentrent l'essentiel des retenues.",
                "<strong>Les joints de salle de bain.</strong> Un joint noirci par la moisissure est le premier point relevé. C'est aussi le plus mal traité : frotter à l'éponge ne fait rien, la moisissure est dans l'épaisseur du silicone. Il faut un temps de pose d'un produit adapté, et parfois accepter qu'un joint trop attaqué relève du remplacement, pas du nettoyage.",
                "<strong>La cuisine.</strong> Plaques, four, hotte et plan de travail. La graisse cuite ne part pas au dégraissant ménager : elle demande de la vapeur à haute température, qui la ramollit avant de l'essuyer.",
                "<strong>Les traces sur les murs.</strong> Sur peinture mate blanche, un lessivage mal conduit laisse une auréole plus visible que la trace d'origine. Mieux vaut ne pas y toucher que mal s'y prendre.",
                "<strong>Les vitres.</strong> Contrôlées à contre-jour, ce qui révèle les traces qu'on ne voit pas de face. Notre méthode à l'eau osmosée règle ce point : sans minéraux, l'eau sèche sans rien déposer.",
                "<strong>Les sols.</strong> Un parquet demande un nettoyage à l'humide contrôlé, pas de l'eau. Un carrelage demande surtout un traitement des joints, qui grisent.",
                '<strong>Les grilles de ventilation et les radiateurs.</strong> Oubliés par presque tout le monde, systématiquement regardés.',
            ]),
            ('Ce que coûte un nettoyage de fin de bail', [
                "Les tarifs relevés à Paris en 2026 vont d'environ 100 à 150 € pour un studio, 150 à 300 € pour un deux-pièces et 250 à 500 € pour un trois-pièces. Au-delà, le prix suit la surface et l'état.",
                "Ces fourchettes sont larges parce que deux logements de même surface ne demandent pas le même travail. Ce qui fait varier le prix, dans l'ordre : l'état de la cuisine, la présence de moisissure dans la salle de bain, le nombre de fenêtres, et le fait que le logement soit vide ou encore meublé.",
                "Nous chiffrons sur photos et nous détaillons poste par poste. Un logement déjà vidé et régulièrement entretenu se traite vite ; un logement laissé en l'état après plusieurs années demande une remise en état, ce qui n'est pas le même métier ni le même prix. Nous le disons au devis.",
            ]),
            ('Le bon moment pour intervenir', [
                "Après avoir vidé le logement, avant l'état des lieux. Cela paraît évident et c'est pourtant l'erreur la plus fréquente : faire nettoyer avec les meubles encore en place oblige à repasser derrière une fois qu'ils sont partis, parce que les traces au sol et sur les murs n'apparaissent qu'à ce moment-là.",
                "Prévoyez au moins vingt-quatre heures entre l'intervention et l'état des lieux. Cela laisse le temps aux sols de sécher complètement et vous laisse une marge si un point doit être repris.",
                'Nous intervenons sept jours sur sept, y compris le samedi et le dimanche, précisément parce que les déménagements se font en fin de semaine et que les états des lieux suivent de près.',
            ]),
        ],
        "faq": [
            ('Le nettoyage de fin de bail est-il obligatoire ?',
             "Vous n'êtes pas obligé de faire appel à une entreprise, mais vous devez rendre le logement propre. Si l'état des lieux relève un défaut de propreté, le bailleur peut retenir le coût du nettoyage sur votre dépôt de garantie, sur la base d'un devis que vous n'aurez pas choisi."),
            ('Garantissez-vous que je récupérerai ma caution ?',
             'Non, et méfiez-vous de qui vous le promet. Nous garantissons la propreté du logement, pas la décision du bailleur, qui peut aussi porter sur des dégradations sans rapport avec le nettoyage. Nous vous remettons en revanche le détail de ce qui a été traité, qui vous sert de pièce en cas de désaccord.'),
            ('Traitez-vous les joints de salle de bain noircis ?',
             "Oui, avec un produit à temps de pose, ce qui donne de bons résultats sur une moisissure de surface. Quand le silicone est attaqué en profondeur, aucun nettoyage ne le récupère : il faut le remplacer. Nous vous le disons avant d'intervenir plutôt qu'après."),
            ("Intervenez-vous en urgence, la veille de l'état des lieux ?",
             "Souvent oui, selon nos disponibilités et votre commune. Appelez-nous plutôt que d'utiliser le formulaire : c'est plus rapide. Sachez seulement qu'un sol lavé la veille peut être encore humide le lendemain matin."),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'nettoyage-etat-des-lieux-sortie',
        "cat": 'Fin de bail',
        "h1": 'Nettoyage avant état des lieux de sortie : la liste complète',
        "title": 'Nettoyage avant état des lieux de sortie',
        "meta": "La liste pièce par pièce de ce qu'un état des lieux de sortie contrôle, et l'ordre dans lequel traiter un logement pour ne rien oublier.",
        "image": 'intervention-1.webp',
        "lead": 'Un état des lieux se déroule toujours dans le même ordre : pièce par pièce, du haut vers le bas. Voici la même liste, dans le même ordre, pour ne rien laisser passer.',
        "sections": [
            ("L'ordre qui fait gagner du temps", [
                'Nettoyer un logement dans le désordre revient à le nettoyer deux fois. La règle tient en une phrase : du haut vers le bas, et du fond vers la sortie.',
                "Concrètement : luminaires et grilles de ventilation d'abord, puis murs et interrupteurs, puis fenêtres, puis meubles fixes et plinthes, et les sols en dernier, en reculant vers la porte. La poussière tombe, elle ne remonte pas.",
                "C'est aussi pour cela qu'il faut vider le logement avant. Chaque meuble déplacé après coup redistribue de la poussière sur des surfaces déjà traitées.",
            ]),
            ('Cuisine : le poste le plus regardé', [
                "La cuisine concentre à elle seule une grande part des retenues. Quatre points s'y jouent.",
                "Le four, d'abord, y compris les grilles et la vitre intérieure — qui se démonte sur la plupart des modèles et qu'on oublie presque toujours. Ensuite la hotte : le filtre métallique passe au lave-vaisselle, le caisson se dégraisse à la vapeur. Puis les plaques, où le point critique est le pourtour, pas la surface. Enfin les meubles hauts, dont le dessus n'est jamais nettoyé pendant l'occupation et se couvre d'un film gras.",
                "Un mot d'honnêteté sur les hottes : le dégraissage d'un conduit d'extraction en restaurant relève d'une prestation certifiée, exigée par les assureurs, que nous ne réalisons pas. En logement, c'est un simple dégraissage et nous le faisons.",
            ]),
            ('Salle de bain : moisissure et calcaire', [
                'Deux problèmes différents, deux traitements différents. La moisissure est vivante et logée dans le silicone : elle demande un produit à temps de pose. Le calcaire est un dépôt minéral : il demande un acide doux et de la patience.',
                "Les points contrôlés sont les joints, la robinetterie, la paroi de douche, le siphon et le dessous du lavabo. Les parois de douche en verre relèvent de la même méthode que les vitres : traitées à l'eau osmosée, elles sèchent sans trace.",
                "Le pommeau de douche entartré se démonte et se trempe. C'est cinq minutes, et cela change l'impression générale.",
            ]),
            ('Sols, vitres et finitions', [
                "Les sols se traitent selon leur nature. Le parquet ne supporte pas l'eau : humidité contrôlée uniquement. Le carrelage demande un travail sur les joints, qui grisent et qu'un simple lavage ne récupère pas. Le vinyle ou le lino se lavent normalement mais marquent au produit trop agressif.",
                "La moquette relève de l'injection-extraction : on injecte une solution dans la fibre et on l'aspire immédiatement, avec la saleté dissoute. Un shampoing de surface, lui, laisse un résidu qui refixe la poussière et la moquette se resalit en quelques semaines.",
                "Les vitres se contrôlent à contre-jour. Les plinthes, les portes autour des poignées et les interrupteurs sont les trois finitions qui font qu'un logement paraît soigné ou expédié.",
            ]),
        ],
        "faq": [
            ('Faut-il nettoyer avant ou après avoir vidé le logement ?',
             "Après, sans hésiter. Les traces au sol et sur les murs n'apparaissent qu'une fois les meubles partis, et chaque meuble déplacé redistribue de la poussière sur ce qui vient d'être nettoyé."),
            ('Combien de temps prévoir ?',
             "Pour un deux-pièces vidé et correctement entretenu, comptez une demi-journée à deux personnes. Un logement laissé en l'état après plusieurs années demande souvent une journée complète et relève de la remise en état."),
            ('Les joints de carrelage gris se rattrapent-ils ?',
             "En partie. Un joint grisé par l'encrassement se récupère bien. Un joint poreux teinté dans la masse, non : il faudrait le refaire, ce qui est un travail de carreleur, pas de nettoyage."),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'prix-nettoyage-fin-de-bail',
        "cat": 'Prix',
        "h1": "Prix d'un nettoyage de fin de bail en Île-de-France",
        "title": "Prix d'un nettoyage de fin de bail",
        "meta": 'Tarifs constatés en Île-de-France pour un nettoyage de fin de bail, du studio au cinq-pièces, et les cinq facteurs qui font varier le devis.',
        "image": 'intervention-3.webp',
        "lead": "Les tarifs annoncés vont du simple au triple pour une même surface. Voici les fourchettes réelles du marché francilien, et ce qui explique l'écart.",
        "sections": [
            ('Les fourchettes constatées à Paris et en Île-de-France', [
                "Les prix relevés chez les prestataires franciliens en 2026 s'établissent autour de 100 à 150 € pour un studio, 150 à 300 € pour un deux-pièces, 250 à 500 € pour un trois-pièces, et de 650 à 1 000 € au-delà de quatre pièces.",
                "L'Île-de-France se situe 15 à 25 % au-dessus du reste du pays sur ce type de prestation. Ce n'est pas une marge supplémentaire : c'est le coût du déplacement en zone dense, du stationnement et des créneaux contraints.",
                "Un point à surveiller : beaucoup d'annonces affichent un prix « à partir de » qui correspond à un studio vide et récent. Demandez toujours un devis sur votre logement réel.",
            ]),
            ('Les cinq facteurs qui font le prix', [
                "<strong>L'état de la cuisine.</strong> C'est le premier poste. Un four et une hotte encrassés peuvent à eux seuls représenter deux heures de travail.",
                '<strong>La moisissure en salle de bain.</strong> Elle impose des temps de pose : on applique, on attend, on reprend. Ce temps se facture même si la main ne bouge pas.',
                "<strong>Le nombre d'ouvrants.</strong> Les vitres se comptent en vantaux, pas en fenêtres. Une baie coulissante à quatre vantaux, ce sont huit faces.",
                "<strong>La présence de moquette.</strong> L'injection-extraction est une prestation à part entière, facturée au mètre carré.",
                "<strong>L'accès.</strong> Étage sans ascenseur, absence de stationnement, code d'entrée : cela n'apparaît sur aucune grille tarifaire mais cela pèse sur le temps réel.",
            ]),
            ('Ce que notre devis contient', [
                "Nous détaillons chaque poste séparément : la cuisine, la salle de bain, les sols, les vitres et, s'il y a lieu, la moquette. Vous voyez ce que coûte chaque partie et vous pouvez en retirer une si vous préférez la faire vous-même.",
                'Les frais de déplacement sont calculés depuis notre atelier de Tremblay-en-France, à 5 € par tranche de 5 km, et annoncés avant que vous validiez. Ils figurent sur le devis, pas sur la facture finale en supplément.',
                "Aucun acompte n'est demandé. Vous réglez après l'intervention, une fois le résultat constaté — ce qui est particulièrement pertinent sur une prestation dont l'enjeu est justement le résultat visible.",
            ]),
            ('Faire soi-même ou faire faire', [
                "Le calcul est simple et vaut d'être posé. Si votre dépôt de garantie est de 1 200 € et qu'une retenue pour ménage vous coûterait 400 €, une prestation à 250 € est rentable. S'il s'agit d'un studio que vous avez tenu propre, un week-end de votre temps suffit probablement.",
                "Les deux cas où faire faire s'impose : quand vous n'avez plus accès au logement après le déménagement, et quand la cuisine ou la salle de bain sont au-delà de ce qu'un nettoyage domestique récupère.",
                "Dans le doute, envoyez-nous trois photos — cuisine, salle de bain, sol le plus abîmé. Nous vous dirons franchement si l'intervention se justifie.",
            ]),
        ],
        "faq": [
            ('Le prix est-il au mètre carré ?',
             "Non, pas pour un logement. La surface donne un ordre de grandeur, mais l'état pèse davantage : deux trois-pièces identiques peuvent demander du simple au double selon l'état de la cuisine."),
            ('Les produits et le matériel sont-ils compris ?',
             "Oui, toujours, comme l'eau et l'électricité que nous apportons. Vous n'avez rien à fournir et rien à prévoir sur place."),
            ('Y a-t-il un supplément le week-end ?',
             'Non. Nous intervenons sept jours sur sept au même tarif, parce que les déménagements se font justement le week-end.'),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'nettoyage-copropriete-parties-communes',
        "cat": 'Copropriété',
        "h1": 'Nettoyage des parties communes de copropriété',
        "title": 'Nettoyage des parties communes',
        "meta": 'Entretien des parties communes en copropriété : ce que couvre la prestation, à quelle fréquence, et comment un syndic compare deux devis.',
        "image": 'bureau-entreprise.webp',
        "lead": "La propreté des parties communes relève du syndic et se finance par les charges. C'est aussi le premier motif de plainte en assemblée générale. Voici comment la prestation se construit.",
        "sections": [
            ("Ce que recouvre l'entretien des parties communes", [
                "Le périmètre standard comprend le hall d'entrée, la cage d'escalier et ses paliers, les couloirs de circulation, l'ascenseur, les boîtes aux lettres, le local poubelles et, selon les immeubles, le parking et la cour.",
                "Sur chacun, le travail se décompose en trois niveaux : le passage courant — balayage, lavage des sols, sortie et rentrée des conteneurs — le dépoussiérage périodique des rampes, plinthes, interrupteurs et boîtes aux lettres, et l'entretien approfondi, moins fréquent, qui traite les vitrages, les portes vitrées du hall et le local poubelles.",
                "La désinfection des points de contact — poignées, rampes, boutons d'ascenseur — s'est installée dans les cahiers des charges depuis 2020. Elle relève du nettoyage courant avec un produit adapté, pas d'un traitement biocide réglementé.",
            ]),
            ("La bonne fréquence selon l'immeuble", [
                "Il n'existe pas de norme, seulement des usages qui tiennent au nombre de logements et à la circulation.",
                "En dessous de dix lots, un passage hebdomadaire suffit généralement, avec une sortie de conteneurs calée sur le calendrier de collecte. Entre dix et trente lots, deux passages par semaine deviennent le standard. Au-delà, ou dès qu'il y a des commerces au rez-de-chaussée, on passe à trois passages ou au quotidien.",
                "Le facteur qui change tout n'est pas le nombre de logements mais la présence d'un local poubelles intérieur. Un local mal ventilé impose un rythme que la seule circulation ne justifierait pas.",
                "Un conseil de bon sens : mieux vaut deux passages sérieux qu'un passage quotidien expédié. Sur un immeuble de vingt lots, la différence de perception est nette.",
            ]),
            ('Comment un syndic compare deux devis', [
                "Les devis d'entretien d'immeuble sont difficiles à comparer parce qu'ils n'expriment pas la même chose. Trois vérifications suffisent à les remettre à plat.",
                "<strong>Le temps de présence par passage.</strong> C'est la seule donnée qui compte vraiment. Un prestataire qui annonce un forfait sans dire combien de temps il reste vous laisse sans repère. Demandez-le et faites le rapport avec le prix.",
                "<strong>Ce qui est mensuel et ce qui est ponctuel.</strong> Le lavage des vitrages du hall, le décapage annuel des sols, le nettoyage du local poubelles à la haute pression : ces postes sont parfois inclus, parfois facturés en plus. L'écart entre deux devis vient souvent de là.",
                '<strong>La continuité du service.</strong> Qui passe pendant les congés ? Une entreprise qui ne répond pas à cette question vous laissera un immeuble non entretenu trois semaines en août.',
            ]),
            ('Notre positionnement sur la copropriété', [
                "Nous sommes une entreprise individuelle. C'est une limite qu'il faut dire d'emblée : nous ne sommes pas équipés pour un parc de plusieurs dizaines d'immeubles avec remplacement immédiat en cas d'absence.",
                "Sur un immeuble ou quelques immeubles proches, en revanche, cela devient un avantage. C'est la même personne qui passe à chaque fois, qui connaît l'immeuble, qui remarque qu'une ampoule est grillée ou qu'une fuite marque le mur du sous-sol, et qui le signale au syndic.",
                "Nous intervenons aussi ponctuellement : remise en état d'une cage d'escalier après travaux, nettoyage haute pression d'un local poubelles ou d'une cour, vitrerie du hall. Ce sont des prestations que beaucoup de contrats d'entretien courant ne couvrent pas.",
            ]),
        ],
        "faq": [
            ('Qui décide du prestataire de nettoyage en copropriété ?',
             "Le syndic met en concurrence et le vote intervient en assemblée générale, à la majorité de l'article 24 pour un contrat d'entretien courant. Le conseil syndical peut demander des devis en amont."),
            ('Le nettoyage des parties communes est-il obligatoire ?',
             "L'entretien des parties communes incombe au syndicat des copropriétaires. Rien n'impose de passer par une entreprise — certaines copropriétés emploient un gardien — mais l'entretien lui-même n'est pas optionnel."),
            ('Sortez-vous les conteneurs ?',
             "Oui, quand c'est prévu au contrat, avec un passage calé sur le calendrier de collecte de la commune. C'est souvent le point qui détermine le jour d'intervention plutôt que l'inverse."),
            ('Intervenez-vous ponctuellement, sans contrat ?',
             'Oui. Une remise en état après travaux, un local poubelles à reprendre à la haute pression ou une vitrerie de hall se traitent en intervention unique, sur devis.'),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'nettoyage-cage-escalier-immeuble',
        "cat": 'Copropriété',
        "h1": "Nettoyage de cage d'escalier : méthode et fréquence",
        "title": "Nettoyage de cage d'escalier",
        "meta": "Nettoyage de cage d'escalier en immeuble : traiter la marche et la contremarche, les rampes, les paliers, et le rythme qui tient dans la durée.",
        "image": 'intervention-1.webp',
        "lead": "Une cage d'escalier est la première chose que voit un visiteur et la dernière que l'on entretient sérieusement. Elle demande une méthode précise, parce qu'on y travaille debout, en hauteur et à contretemps.",
        "sections": [
            ("Pourquoi une cage d'escalier se salit autrement", [
                "Un escalier ne se salit pas comme un sol plat. La saleté s'y dépose en trois endroits distincts : sur le nez de marche, où passent les semelles, dans l'angle entre marche et contremarche, où elle s'accumule sans jamais être délogée, et sur les plinthes latérales, que le balai frôle sans les toucher.",
                "C'est cet angle qui trahit un entretien bâclé. Une cage balayée rapidement paraît propre de face et montre un liseré gris dès qu'on regarde de biais.",
                "S'ajoute un phénomène propre aux immeubles : la poussière retombe. Ce qu'on soulève au troisième étage se redépose au premier. D'où la règle du haut vers le bas, sans exception.",
            ]),
            ('La méthode, étage par étage', [
                "On commence par le dernier étage et on descend. Dépoussiérage d'abord — rampe, main courante, plinthes, boîtiers électriques, luminaires — puis balayage humide des marches, angle compris, puis lavage.",
                "Le choix du produit dépend du revêtement, et c'est là qu'on abîme le plus souvent. Le carrelage et la pierre reconstituée acceptent un détergent neutre. Le marbre et la pierre naturelle, très présents dans les immeubles haussmanniens, ne supportent aucun acide : un détartrant classique les mate définitivement. Le bois demande une humidité contrôlée, jamais d'eau.",
                "Les paliers et le hall se traitent en dernier, en reculant vers la sortie. Les portes des logements se limitent au pourtour de la poignée : on ne nettoie pas la porte d'un copropriétaire au-delà de ce qui relève des parties communes.",
            ]),
            ('Le rythme qui tient', [
                "Un rythme trop ambitieux ne tient jamais un an. Mieux vaut un engagement modeste et respecté qu'un contrat quotidien qui s'étiole.",
                'Le schéma qui fonctionne dans la plupart des immeubles franciliens : un passage complet par semaine pour un petit immeuble, deux pour un immeuble de taille moyenne, plus un traitement approfondi trimestriel qui reprend ce que le passage courant ne fait pas — vitrages de la cage, luminaires, dessus des boîtes aux lettres, plinthes en profondeur.',
                'Le décapage complet des sols, lui, se justifie une fois par an au plus, et seulement sur les revêtements qui le supportent.',
            ]),
            ('Les contraintes propres aux immeubles occupés', [
                "On travaille dans un lieu de passage. Cela impose une signalisation du sol mouillé, un séchage rapide et un horaire choisi : tôt le matin ou en milieu de journée, jamais aux heures de sortie d'école ou de retour du travail.",
                "L'absence d'ascenseur change le temps d'intervention plus qu'on ne l'imagine : le matériel monte à la main, et l'eau aussi. Nous en tenons compte au devis plutôt que d'expédier les derniers étages.",
                "Enfin, l'éclairage. Beaucoup de cages sont sur minuterie et mal éclairées : ce qui est propre sous une ampoule de faible intensité ne l'est pas à la lumière du jour. Nous travaillons avec notre propre éclairage quand c'est nécessaire.",
            ]),
        ],
        "faq": [
            ("À quelle fréquence nettoyer une cage d'escalier ?",
             'Une fois par semaine pour un petit immeuble, deux fois pour un immeuble de taille moyenne, avec un traitement approfondi trimestriel. Le nombre de logements compte moins que la circulation réelle et la présence de commerces.'),
            ('Peut-on nettoyer un escalier en marbre au Kärcher ?',
             'Non. La haute pression et les produits acides matent définitivement le marbre et la pierre naturelle. Ces revêtements demandent un détergent neutre et un lavage manuel.'),
            ('Nettoyez-vous aussi les vitrages de la cage ?',
             "Oui, à l'eau osmosée, qui sèche sans laisser de trace. C'est en général une prestation trimestrielle plutôt qu'hebdomadaire."),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'nettoyage-airbnb-paris',
        "cat": 'Location courte durée',
        "h1": 'Nettoyage Airbnb à Paris : entre deux voyageurs',
        "title": 'Nettoyage Airbnb à Paris',
        "meta": 'Nettoyage de logement Airbnb à Paris : le protocole entre deux séjours, les points qui font baisser une note, et la contrainte des créneaux serrés.',
        "image": 'canape-nettoyage.webp',
        "lead": "En location courte durée, la propreté est notée publiquement et la fenêtre d'intervention dure quelques heures. Ce sont deux contraintes qui changent la méthode.",
        "sections": [
            ('Ce que les voyageurs remarquent vraiment', [
                'Les commentaires qui font baisser une note de propreté portent rarement sur le sol. Ils portent sur des détails précis, toujours les mêmes.',
                "Les cheveux — dans la douche, sur le rebord du lavabo, sous le lit. Les traces de calcaire sur la paroi de douche et la robinetterie. L'odeur à l'ouverture de la porte, qu'un logement fermé plusieurs jours développe naturellement. Le réfrigérateur, dont les joints noircissent vite. La poussière sur les surfaces à hauteur d'œil, qu'on ne voit pas en travaillant debout mais qu'un voyageur assis remarque immédiatement.",
                "Aucun de ces points ne demande beaucoup de temps. Ils demandent qu'on sache qu'ils existent et qu'on les traite systématiquement, ce que fait un protocole écrit et que ne fait pas un ménage improvisé.",
            ]),
            ('La contrainte du créneau', [
                "Un départ à 11 h, une arrivée à 15 h : quatre heures, déplacement compris, pour un logement entier. Cela impose de savoir à l'avance ce qu'on va faire et dans quel ordre.",
                "L'ordre qui fonctionne : ouvrir et aérer dès l'arrivée, dépouiller les lits, lancer la machine s'il y en a une sur place, traiter la salle de bain pendant que le linge tourne, puis la cuisine, puis les surfaces, puis les sols en reculant, et refaire les lits en dernier.",
                "Le linge est le point qui fait déraper les plannings. Une rotation avec deux jeux complets par couchage résout le problème une fois pour toutes : on emporte le sale et on repose du propre, sans dépendre d'un cycle de lavage.",
            ]),
            ('Les odeurs, le point faible du meublé', [
                'Un logement fermé entre deux séjours, surtout sans ventilation traversante, développe une odeur de renfermé que le voyageur associe immédiatement au manque de propreté. Un désodorisant la masque une heure et la rend suspecte ensuite.',
                "Quand l'odeur est installée — tabac d'un séjour précédent, humidité, cuisine — nous proposons un traitement par ozone. L'ozone détruit les molécules odorantes au lieu de les recouvrir, et il agit dans les textiles et les recoins que le nettoyage n'atteint pas.",
                "Le protocole est strict : le logement doit être vide de personnes, d'animaux et de plantes pendant le traitement, puis aéré avant la remise des clés. L'ozone est un gaz irritant pour les voies respiratoires ; il ne se pratique pas en présence de qui que ce soit. C'est pour cela qu'il se cale entre deux réservations et pas pendant.",
            ]),
            ('Ce que nous faisons, et ce que nous ne faisons pas', [
                'Nous faisons le nettoyage entre deux séjours, la remise en état saisonnière plus poussée, le traitement des textiles — canapé convertible, matelas, tapis — par injection-extraction, la vitrerie et le traitement des odeurs par ozone.',
                "Nous ne sommes pas une conciergerie. Nous ne gérons pas les annonces, les arrivées, les clés ni la relation avec les voyageurs. Si vous cherchez ce service complet, il vous faut une conciergerie ; nous pouvons travailler pour elle ou à côté d'elle.",
                'Nous intervenons sept jours sur sept, jours fériés compris, ce qui est la condition minimale pour être utile en location courte durée. Pour un logement à rotation régulière, nous calons un créneau récurrent plutôt que de reprendre rendez-vous à chaque fois.',
            ]),
        ],
        "faq": [
            ('Intervenez-vous le dimanche et les jours fériés ?',
             "Oui, sept jours sur sept, sans supplément. C'est indispensable en location courte durée, où les rotations tombent précisément ces jours-là."),
            ('Fournissez-vous le linge ?',
             "Non. Nous nettoyons et nous faisons les lits avec le linge disponible sur place. La gestion du linge relève d'une conciergerie ou d'une blanchisserie, avec qui nous nous coordonnons sans difficulté."),
            ('Combien de temps faut-il entre deux voyageurs ?',
             "Trois heures sur place pour un deux-pièces, davantage si un traitement textile ou un passage à l'ozone est prévu. L'ozone impose en plus une aération avant l'arrivée du voyageur suivant."),
            ('Traitez-vous une odeur de tabac laissée par un voyageur ?',
             "Oui, par ozone, après nettoyage des surfaces et des textiles. Le traitement se fait logement vide et suivi d'une aération. Sur une odeur ancienne et très incrustée, un second passage est parfois nécessaire ; nous le disons au devis quand nous l'anticipons."),
        ],
        "service": 'traitement-ozone-paris',
    },
    {
        "slug": 'nettoyage-matelas-paris',
        "cat": 'Textile',
        "h1": 'Nettoyage de matelas à domicile à Paris',
        "title": 'Nettoyage de matelas à Paris',
        "meta": 'Nettoyage de matelas à domicile à Paris : injection-extraction, traitement des taches et des acariens, temps de séchage et limites réelles.',
        "image": 'intervention-2.webp',
        "lead": "Un matelas absorbe chaque nuit une quantité d'humidité que rien n'évacue. C'est ce qui explique à la fois les auréoles, les odeurs et la population d'acariens qu'il finit par abriter.",
        "sections": [
            ("Ce qu'il y a réellement dans un matelas", [
                "Un dormeur perd entre un tiers et un demi-litre de transpiration par nuit. Une partie s'évapore, le reste descend dans le garnissage, où il ne remonte jamais. Après quelques années, cela représente plusieurs dizaines de litres passés dans la mousse ou le latex.",
                'Cette humidité, associée aux cellules de peau, nourrit les acariens. Ce ne sont pas eux qui provoquent les réactions allergiques mais leurs déjections, très fines, qui se remettent en suspension à chaque mouvement.',
                "Un aspirateur domestique ne les atteint pas : ils sont fixés en profondeur dans la fibre, et un aspirateur sans filtration fine les rejette en partie dans la pièce. C'est la différence essentielle avec l'injection-extraction, qui va les chercher et les évacue dans une cuve.",
            ]),
            ('La méthode : injection-extraction', [
                "On injecte sous pression une solution dans le garnissage, on la laisse agir quelques instants, et on l'aspire immédiatement avec ce qu'elle a dissous. Le point clé est le « immédiatement » : il n'y a pas d'eau qui stagne, donc pas d'auréole en séchant.",
                "C'est ce qui distingue cette méthode d'un shampoing de surface, qui mousse, reste dans la fibre en séchant et refixe la poussière — le matelas paraît propre une semaine puis se resalit plus vite qu'avant.",
                "Les taches identifiées sont traitées avant, une par une, avec un détachant choisi selon leur nature. On ne traite pas une tache de sang comme une tache d'urine ou de transpiration : le sang réagit à froid, la chaleur le fixe définitivement.",
                "Une passe à la vapeur haute température peut compléter le traitement en surface. Nous parlons bien d'assainissement, pas de désinfection au sens réglementaire : nous ne sommes pas un applicateur de produits biocides et nous ne revendiquons aucun taux d'élimination.",
            ]),
            ("Les taches d'urine, et ce qu'on peut en attendre", [
                "C'est la demande la plus fréquente et celle où il faut être le plus honnête. Traitée dans les quarante-huit heures, une tache d'urine s'élimine presque toujours, odeur comprise.",
                "Passé une semaine, l'urine cristallise. Les sels restent dans la fibre et laissent une marque jaunâtre que l'extraction atténue nettement mais n'efface pas toujours. Sur un matelas clair, la marque peut rester visible même après un traitement réussi sur l'odeur.",
                "L'odeur, elle, se traite bien mieux que la couleur. Elle provient de composés que l'extraction évacue, et un passage à l'ozone finit le travail sur les cas anciens. Nous distinguons donc systématiquement les deux au devis : ce que nous pouvons garantir sur l'odeur, ce que nous espérons sur la marque.",
            ]),
            ('Séchage, tarifs et conditions', [
                'Comptez quatre à six heures de séchage avant de refaire le lit, davantage dans une pièce fermée ou humide. Nous laissons le matelas relevé et la pièce aérée en partant. Traiter le matin permet de dormir dessus le soir même.',
                'Nos tarifs partent de 15 € pour un couchage simple et suivent la taille du matelas ; le détail figure sur notre grille tarifaire. Les prix relevés à Paris chez les prestataires spécialisés vont plutôt de 60 à 89 € selon la taille et le nombre de faces traitées.',
                "Traiter les deux faces double le temps mais pas toujours l'intérêt : si le matelas n'a jamais été retourné, la face inférieure est souvent en bien meilleur état. Nous regardons avant de vous le facturer.",
                "Un matelas à mémoire de forme demande plus de précaution : la mousse retient davantage l'humidité et sèche plus lentement. Nous adaptons le débit d'injection en conséquence.",
            ]),
        ],
        "faq": [
            ('Combien de temps le matelas met-il à sécher ?',
             'Quatre à six heures dans une pièce aérée. Nous le laissons relevé en partant. Une intervention le matin permet de se recoucher dessus le soir.'),
            ("Une tache d'urine ancienne part-elle complètement ?",
             "L'odeur, presque toujours. La marque, pas systématiquement : au-delà d'une semaine, les sels cristallisent dans la fibre et laissent une trace jaunâtre que l'extraction atténue sans toujours l'effacer. Nous le disons avant, pas après."),
            ('Éliminez-vous les acariens ?',
             "L'injection-extraction retire une grande part des acariens et de leurs déjections, qui sont la cause réelle des réactions allergiques. Nous n'annonçons pas de pourcentage : nous ne sommes pas un applicateur de biocides et un chiffre non mesuré ne voudrait rien dire."),
            ('Faut-il retirer le matelas du lit ?',
             "Non, nous travaillons sur place. Dégagez simplement l'accès autour du lit et retirez la literie avant notre arrivée."),
        ],
        "service": 'nettoyage-textile-paris',
    },
    {
        "slug": 'prix-nettoyage-matelas',
        "cat": 'Prix',
        "h1": "Prix d'un nettoyage de matelas",
        "title": "Prix d'un nettoyage de matelas",
        "meta": 'Ce que coûte un nettoyage de matelas à domicile en Île-de-France, par taille, et les trois éléments qui font varier le devis.',
        "image": 'canape-nettoyage.webp',
        "lead": "Les tarifs vont de quelques dizaines d'euros à près de cent selon la taille et le prestataire. Voici comment le prix se construit réellement.",
        "sections": [
            ('Nos tarifs, et ceux du marché', [
                'Chez nous, le nettoyage textile démarre à 15 € et suit la taille du couchage. Le tarif exact figure sur notre grille, avec les canapés, fauteuils et tapis.',
                'Les prix relevés chez les prestataires spécialisés en Île-de-France en 2026 se situent autour de 49 à 60 € pour un couchage simple une face, et de 69 à 89 € pour un deux places selon le nombre de faces traitées. À Paris intra-muros, les tarifs affichés démarrent plutôt vers 72 €.',
                "Cet écart s'explique surtout par le modèle : un prestataire qui se déplace pour un seul matelas doit amortir son déplacement sur cette seule prestation. C'est pourquoi traiter le matelas en même temps que le canapé ou les tapis fait chuter le coût par pièce.",
            ]),
            ('Les trois éléments qui font varier le prix', [
                "<strong>La taille et le nombre de faces.</strong> Un 90 × 190 se traite en une fraction du temps d'un 180 × 200. Traiter les deux faces double le temps de travail et le temps de séchage.",
                "<strong>Le détachage.</strong> Une tache identifiée demande un traitement individuel avec un produit choisi selon sa nature et un temps de pose. Trois taches anciennes peuvent représenter autant de temps que l'extraction elle-même.",
                "<strong>Le traitement des odeurs.</strong> Quand l'odeur persiste après extraction, un passage à l'ozone se facture en supplément, à partir de 30 €. Il ne se justifie pas sur tous les matelas : nous ne le proposons que lorsqu'il apportera quelque chose.",
            ]),
            ('Le déplacement, et comment ne pas le payer pour rien', [
                'Nos frais de déplacement sont de 5 € par tranche de 5 km depuis notre atelier de Tremblay-en-France, annoncés avant validation. Sur un seul matelas, ils peuvent représenter une part notable du total.',
                "Le réflexe utile : regrouper. Un matelas seul, c'est une prestation courte pour un déplacement complet. Deux matelas et un canapé traités le même jour, c'est le même déplacement pour trois fois plus de travail — le coût par pièce chute nettement.",
                "Si vous hésitez, dites-nous simplement tout ce qui pourrait être traité chez vous. Nous vous dirons ce qui en vaut la peine et ce qui n'en vaut pas, y compris quand la réponse est « celui-là, laissez-le ».",
            ]),
            ('Quand le nettoyage ne se justifie plus', [
                "Un matelas a une durée de vie. Au-delà d'une dizaine d'années, la mousse s'affaisse et le soutien disparaît : un nettoyage le rendra propre mais pas confortable, et l'argent est mieux placé dans un matelas neuf.",
                "De même, un matelas dont le garnissage est atteint par une moisissure profonde — après un dégât des eaux, par exemple — ne se récupère pas. La moisissure est dans l'épaisseur, l'extraction ne va pas la chercher.",
                "Nous préférons vous le dire au devis, sur photos, plutôt qu'après une intervention facturée. Un refus argumenté vaut mieux qu'une prestation décevante.",
            ]),
        ],
        "faq": [
            ('Le déplacement est-il facturé en plus ?',
             "Oui, 5 € par tranche de 5 km depuis Tremblay-en-France, annoncés avant que vous validiez et figurant sur le devis. Aucun supplément n'apparaît après."),
            ('Est-ce moins cher de traiter plusieurs pièces le même jour ?',
             "Nettement. Le déplacement est unique et le matériel est déjà installé. C'est la seule optimisation vraiment efficace sur ce type de prestation."),
            ('Faut-il payer un acompte ?',
             "Non, jamais. Vous réglez après l'intervention, une fois le résultat constaté."),
        ],
        "service": 'nettoyage-textile-paris',
    },
    {
        "slug": 'nettoyage-moquette-bureau-paris',
        "cat": 'Professionnels',
        "h1": 'Nettoyage de moquette de bureau à Paris',
        "title": 'Nettoyage de moquette de bureau',
        "meta": 'Nettoyage de moquette en bureau à Paris : injection-extraction, traitement des zones de passage, séchage et intervention hors heures ouvrées.',
        "image": 'bureau-entreprise.webp',
        "lead": "Une moquette de bureau ne s'use pas uniformément. Elle noircit d'abord dans les couloirs et devant les postes, et c'est là que se joue l'impression générale du plateau.",
        "sections": [
            ('Pourquoi une moquette de bureau grise par endroits', [
                "La saleté d'une moquette de bureau est essentiellement minérale : de la poussière de rue apportée sous les semelles, qui s'incruste entre les fibres. Elle se concentre là où l'on marche — l'entrée, les couloirs, le mètre carré devant chaque bureau — et laisse le reste presque intact.",
                "Cette poussière est abrasive. À chaque pas, elle scie la fibre à sa base. Une moquette qu'on ne nettoie jamais ne se contente pas de paraître sale : elle s'use réellement plus vite, et c'est un argument budgétaire plus fort que l'esthétique.",
                "L'aspiration quotidienne retire ce qui est en surface. Elle ne va pas chercher ce qui est descendu au pied de la fibre, et c'est cette part-là qui donne l'aspect gris.",
            ]),
            ('Injection-extraction, et pourquoi pas le shampoing', [
                "Le shampoing de surface a longtemps été le standard. Il mousse, on brosse, on laisse sécher, on aspire. Le problème est le résidu : le tensioactif reste dans la fibre et devient collant, la poussière s'y fixe, et la moquette se resalit plus vite qu'avant le nettoyage.",
                "L'injection-extraction injecte la solution sous pression et l'aspire dans le même mouvement. Ce qui ressort dans la cuve est ce qui était dans la fibre. Il ne reste pas de résidu, donc pas d'effet rebond.",
                "Sur les zones de passage très marquées, un prébrossage et un temps de pose précèdent l'extraction. C'est ce qui fait la différence entre une moquette éclaircie et une moquette réellement récupérée.",
            ]),
            ("Séchage et organisation de l'intervention", [
                "Comptez quatre à huit heures de séchage selon l'épaisseur de la moquette et la ventilation du plateau. C'est le paramètre qui commande tout le reste.",
                'Le schéma qui fonctionne : intervention le vendredi soir, plateau récupéré le lundi matin. Sur les grands plateaux, on peut aussi travailler par zones sur plusieurs soirées, en laissant chaque zone sécher pendant la nuit.',
                "Nous intervenons en horaires décalés — tôt le matin, le soir, le week-end — sans supplément. Sur un site occupé, c'est la seule façon de travailler correctement : une extraction faite entre deux réunions n'est pas une extraction.",
            ]),
            ('Prix et fréquence raisonnable', [
                "Les tarifs relevés en Île-de-France pour le shampouinage et l'extraction de moquette professionnelle démarrent autour de 8 € le mètre carré. Le prix baisse nettement avec la surface : un plateau de 300 m² ne se facture pas au même tarif unitaire qu'un bureau de 20 m².",
                "La fréquence utile est d'une extraction par an sur un plateau standard, deux si l'entrée donne directement sur la rue ou si le site reçoit du public. Entre deux, un traitement ponctuel des seules zones de passage coûte peu et repousse l'échéance.",
                "Nous chiffrons sur plan ou sur photos, avec le métrage réel des zones à traiter — pas la surface totale du plateau, dont une partie est sous les meubles et n'a pas besoin d'être extraite.",
            ]),
        ],
        "faq": [
            ('Combien de temps avant de remarcher sur la moquette ?',
             "Quatre à huit heures selon l'épaisseur et la ventilation. En pratique, une intervention le vendredi soir permet de récupérer le plateau le lundi matin sans contrainte."),
            ('Faut-il déplacer les bureaux ?',
             "Pas nécessairement. Nous traitons les zones dégagées et les abords des postes, ce qui couvre l'essentiel de ce qui se voit. Un traitement intégral suppose de dégager, ce qui se planifie plutôt lors d'un déménagement."),
            ('Intervenez-vous le week-end ?',
             "Oui, sept jours sur sept et sans supplément. C'est souvent la meilleure option sur un plateau occupé."),
            ('Une moquette très ancienne se récupère-t-elle ?',
             "En partie. L'extraction retire la saleté, elle ne restaure pas une fibre usée mécaniquement. Sur une moquette dont la fibre est écrasée dans les couloirs, le résultat sera net mais l'usure restera visible. Nous le disons avant."),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'nettoyage-tapis-paris',
        "cat": 'Textile',
        "h1": 'Nettoyage de tapis à domicile à Paris',
        "title": 'Nettoyage de tapis à Paris',
        "meta": 'Nettoyage de tapis à domicile à Paris : méthode selon la matière, traitement des taches, séchage, et les tapis que nous ne traitons pas.',
        "image": 'tapis-karcher.webp',
        "lead": "Un tapis se nettoie selon sa fibre, pas selon son aspect. C'est la seule règle qui compte, et c'est celle qu'on enfreint le plus souvent en voulant bien faire.",
        "sections": [
            ('Identifier la fibre avant tout', [
                "Les tapis synthétiques — polypropylène, polyester, nylon — représentent l'essentiel des tapis vendus aujourd'hui. Ils supportent l'eau, les détergents courants et l'injection-extraction sans difficulté. C'est le cas le plus simple et le plus fréquent.",
                "La laine est une autre histoire. C'est une fibre animale : elle craint l'alcalinité, qui la ternit et la feutre, et elle se rétracte à la chaleur. Elle demande un produit neutre ou légèrement acide, une eau tiède et surtout pas de vapeur.",
                "La viscose est la fibre la plus délicate qui soit. Elle perd sa résistance une fois mouillée et marque définitivement à la moindre goutte. Un tapis en viscose ne se nettoie pas à l'eau, chez vous ou ailleurs : il relève d'un traitement à sec en atelier spécialisé, et nous le disons plutôt que de prendre le risque.",
                "En cas de doute, l'étiquette au dos donne souvent la composition. Sans étiquette, l'aspect et le toucher permettent de trancher dans la plupart des cas — nous le faisons sur place avant de commencer.",
            ]),
            ('La méthode et les taches', [
                'Sur un tapis synthétique ou en laine robuste, la séquence est la même que pour un canapé : aspiration profonde, traitement individuel des taches, injection-extraction, puis brossage du sens du poil.',
                "Le brossage final n'est pas cosmétique. Un poil couché dans le mauvais sens sèche ainsi et le tapis paraît terne par zones même parfaitement propre.",
                "Sur les taches, deux réflexes valent d'être rappelés. Ne frottez jamais : vous étalez la tache et vous cassez la fibre. Tamponnez du bord vers le centre, avec un chiffon blanc — un chiffon coloré peut déteindre.",
                "Et n'appliquez rien avant notre passage. Un produit ménager mal choisi peut fixer la tache définitivement, ou décolorer le tapis autour, ce qui est irréversible et se voit davantage que la tache d'origine.",
            ]),
            ('Séchage et remise en place', [
                "Comptez quatre à six heures pour un tapis synthétique, davantage pour la laine, qui retient plus d'eau. Nous relevons le tapis ou glissons une protection dessous pour éviter que l'humidité ne marque le sol.",
                "Un point important sur les parquets : un tapis humide reposé à plat sur du bois peut laisser une auréole sur le parquet lui-même. Nous ne le remettons pas en place tant qu'il n'est pas sec, et nous vous le disons avant de partir.",
                'Les tapis à franges demandent un traitement à part : elles se nettoient à la main et se peignent au séchage, faute de quoi elles sèchent emmêlées.',
            ]),
            ('Ce que nous traitons, et ce que nous refusons', [
                'Nous traitons à domicile les tapis synthétiques, les tapis de laine courants, les descentes de lit, les tapis de couloir et les moquettes posées.',
                "Nous ne traitons pas les tapis en viscose ni les tapis d'orient noués main de valeur — soie, laine fine teintée végétalement. Ces pièces demandent un lavage en atelier, à plat, avec un contrôle de la migration des couleurs qu'on ne peut pas assurer chez vous. Vous orienter vers un spécialiste nous coûte une prestation ; vous abîmer une pièce vous coûterait bien davantage.",
                "Pour tout le reste, envoyez-nous une photo du tapis et une de l'étiquette au dos. Nous vous dirons en quelques minutes si c'est traitable à domicile.",
            ]),
        ],
        "faq": [
            ('Peut-on nettoyer un tapis en laine à la vapeur ?',
             "Non. La chaleur feutre la laine de manière irréversible et la fait rétrécir. La laine se traite à l'eau tiède avec un produit neutre à légèrement acide."),
            ('Traitez-vous les tapis en viscose ?',
             "Non, et nous le déconseillons à quiconque le proposerait à domicile. La viscose perd sa résistance mouillée et marque définitivement. Elle relève d'un traitement à sec en atelier spécialisé."),
            ('Le tapis rétrécit-il après nettoyage ?',
             'Pas sur les fibres synthétiques. Sur la laine, un léger retrait est possible si le tapis a été traité trop chaud ou trop mouillé — raison pour laquelle nous travaillons tiède et en extraction, sans détremper.'),
            ('Faut-il emporter le tapis ?',
             'Non, nous travaillons chez vous. Il suffit de dégager la surface et, si le tapis est sur parquet, de nous laisser glisser une protection dessous.'),
        ],
        "service": 'nettoyage-textile-paris',
    },
    {
        "slug": 'nettoyage-vitrine-commerce-paris',
        "cat": 'Vitrerie',
        "h1": 'Nettoyage de vitrine de commerce à Paris',
        "title": 'Nettoyage de vitrine à Paris',
        "meta": 'Nettoyage de vitrine de commerce à Paris : fréquence, horaires avant ouverture, traitement des traces de pluie et des affichages collés.',
        "image": 'vitre-controle.webp',
        "lead": "Une vitrine sale annule l'effet de la vitrine elle-même. C'est la seule surface d'un commerce que tous les passants voient, et la seule qui se dégrade en quelques jours.",
        "sections": [
            ('Pourquoi une vitrine se salit si vite', [
                "Une vitrine de rue subit trois agressions simultanées. Les projections de la chaussée, qui montent plus haut qu'on ne l'imagine sur une rue passante. Les pluies chargées de particules urbaines, qui sèchent en laissant un voile minéral. Et les traces de mains, concentrées autour de la poignée et à hauteur d'enfant.",
                "Le voile minéral est le plus insidieux. Il ne se voit pas de face mais casse la lumière : la vitrine paraît terne sans qu'on sache pourquoi, et les produits exposés perdent leur éclat.",
                "C'est exactement ce que règle l'eau osmosée. Débarrassée de ses minéraux, elle sèche sans rien déposer : pas de voile, pas de trace, et aucun produit à essuyer.",
            ]),
            ('La bonne fréquence pour un commerce', [
                "Un commerce de rue passante en centre-ville tient rarement plus d'une semaine. Deux passages hebdomadaires sont fréquents en restauration, où s'ajoutent les traces de mains et les projections de la terrasse.",
                'Un commerce en rue calme ou en galerie couverte tient deux à trois semaines sans que cela se voie.',
                "Le repère simple : regardez votre vitrine de biais, en fin de journée, avec le soleil rasant. C'est ainsi que la voient les passants qui arrivent de la rue, et c'est ce qui révèle le voile.",
            ]),
            ("Travailler avant l'ouverture", [
                "Nous intervenons tôt le matin, avant l'ouverture, ou après la fermeture. Ce n'est pas une facilité commerciale : nettoyer une vitrine pendant que les clients entrent et sortent donne un mauvais résultat et gêne le commerce.",
                "L'intervention est courte — quelques minutes par vitrine avec une perche et de l'eau osmosée — ce qui permet de caler plusieurs commerces d'une même rue sur un seul passage. Si vos voisins sont intéressés, dites-le-nous : cela fait baisser le déplacement pour chacun.",
                "Nous traitons aussi la porte, souvent oubliée alors qu'elle porte l'essentiel des traces de mains, ainsi que le seuil et le bas de vitrine, où les projections se concentrent.",
            ]),
            ('Affichages, adhésifs et cas particuliers', [
                "Le retrait d'un adhésif de vitrine — soldes, promotion, ancien enseigne — laisse une colle qui se traite au solvant doux, jamais à la lame sur un vitrage traité ou teinté, qui se rayerait irrémédiablement.",
                "Sur les vitrages anti-effraction ou à film solaire, la précaution est la même : ce sont des films, ils se rayent. Nous les traitons uniquement à l'eau et à la raclette souple.",
                "Les traces de calcaire anciennes, incrustées après des mois de pluie séchée, demandent parfois un passage préalable au produit avant de repasser à l'eau osmosée. Cela se voit au premier coup d'œil et se chiffre à part : une fois le verre remis à zéro, l'entretien régulier suffit ensuite.",
                "Les tags et rayures profondes, en revanche, relèvent du remplacement ou d'un traitement spécialisé : le nettoyage ne les récupère pas.",
            ]),
        ],
        "faq": [
            ('À quelle fréquence nettoyer une vitrine ?',
             'Une fois par semaine en rue passante, deux fois en restauration, deux à trois semaines en rue calme ou en galerie. Le test : regardez la vitrine de biais en lumière rasante.'),
            ("Intervenez-vous avant l'ouverture du magasin ?",
             "Oui, tôt le matin ou après la fermeture, sans supplément. C'est la seule façon de travailler correctement sans gêner le commerce."),
            ('Retirez-vous les anciens adhésifs de vitrine ?',
             "Oui, au solvant doux. Nous n'utilisons pas de lame sur un vitrage traité, teinté ou filmé, qui se rayerait définitivement."),
        ],
        "service": 'nettoyage-vitres-paris',
    },
    {
        "slug": 'prix-nettoyage-vitres-m2',
        "cat": 'Prix',
        "h1": "Prix d'un nettoyage de vitres au mètre carré",
        "title": "Prix d'un nettoyage de vitres au m²",
        "meta": "Tarifs de nettoyage de vitres en Île-de-France : fourchettes au mètre carré selon la hauteur et l'accès, et pourquoi on compte en vantaux.",
        "image": 'vitre-controle.webp',
        "lead": 'Les tarifs au mètre carré circulent partout, mais une vitre ne se facture pas comme un sol. Voici comment le prix se construit réellement.',
        "sections": [
            ('Les fourchettes du marché francilien', [
                "Les tarifs relevés en Île-de-France en 2026 s'échelonnent de 3 à 8 € le mètre carré. Le bas de la fourchette — 3 à 5 € — correspond à des vitrages de plain-pied, accessibles des deux côtés sans matériel particulier.",
                'Le haut — 6 à 8 € — concerne les vitrages en hauteur, qui demandent une perche télescopique ou une nacelle, et les vitrages à accès contraint : verrière, puits de lumière, baie donnant sur un vide.',
                "L'Île-de-France se situe globalement 15 à 25 % au-dessus des tarifs nationaux sur ce type de prestation, essentiellement à cause des contraintes de déplacement et de stationnement.",
            ]),
            ('Pourquoi on compte en vantaux, pas en fenêtres', [
                "C'est le malentendu le plus fréquent des devis de vitrerie. Une « fenêtre » n'est pas une unité de travail : une fenêtre à deux battants représente quatre faces à traiter, une baie coulissante à quatre vantaux en représente huit.",
                "S'ajoutent les éléments qui ne sont pas du verre mais font partie du travail : les encadrements, les rails de coulissants — où s'accumulent poussière et graviers — et les appuis extérieurs.",
                "Quand vous comparez deux devis, vérifiez d'abord ce qui est compté. Un tarif au mètre carré plus bas qui exclut les encadrements et les rails coûte souvent plus cher au final qu'un tarif plus élevé qui les inclut.",
            ]),
            ('Ce qui fait vraiment varier le devis', [
                "<strong>L'accès extérieur.</strong> Une fenêtre qu'on peut ouvrir et traiter depuis l'intérieur ne coûte pas la même chose qu'une baie fixe donnant sur une cour où il faut installer du matériel.",
                "<strong>La hauteur.</strong> Jusqu'à trois étages, la perche télescopique alimentée en eau osmosée permet de travailler depuis le sol, ce qui est rapide et sûr. Au-delà, il faut une nacelle ou des cordistes, et l'on change de métier et de tarif.",
                "<strong>L'état de départ.</strong> Un vitrage jamais nettoyé depuis des années porte un dépôt minéral incrusté qui demande un traitement préalable. C'est une remise à zéro, facturée une fois ; l'entretien courant qui suit est bien moins cher.",
                "<strong>La fréquence.</strong> Un contrat régulier se facture moins cher au passage qu'une intervention unique, parce que chaque passage est plus rapide et que le déplacement est planifié.",
            ]),
            ('Notre façon de chiffrer', [
                'Nous chiffrons sur photos ou sur place, en comptant les vantaux et en précisant ce qui est inclus : faces intérieures, faces extérieures, encadrements, rails et appuis.',
                "Nous ne travaillons pas en hauteur avec nacelle ni en accès par cordes : ce sont des métiers réglementés qui demandent des habilitations spécifiques. Nous traitons ce qui se fait depuis le sol à la perche ou depuis l'intérieur, ce qui couvre les maisons, les rez-de-chaussée commerciaux, les vérandas et la plupart des immeubles jusqu'à trois niveaux.",
                "Quand votre besoin dépasse ce cadre, nous vous le disons plutôt que d'improviser. C'est une question de sécurité avant d'être une question d'assurance.",
            ]),
        ],
        "faq": [
            ('Pourquoi les devis de vitrerie sont-ils si difficiles à comparer ?',
             "Parce qu'ils ne comptent pas la même chose. Vérifiez systématiquement si les encadrements, les rails et les appuis sont inclus, et si le prix couvre les deux faces."),
            ('Travaillez-vous en hauteur ?',
             "Jusqu'à trois niveaux environ, depuis le sol, avec une perche télescopique alimentée en eau osmosée. Au-delà, il faut une nacelle ou des cordistes : ce sont des métiers réglementés que nous ne pratiquons pas."),
            ('Un contrat régulier revient-il moins cher ?',
             "Oui, nettement. Chaque passage est plus rapide sur un vitrage entretenu, et le déplacement est planifié plutôt qu'improvisé."),
        ],
        "service": 'nettoyage-vitres-paris',
    },
    {
        "slug": 'demoussage-terrasse-ile-de-france',
        "cat": 'Extérieur',
        "h1": 'Démoussage de terrasse en Île-de-France',
        "title": 'Démoussage de terrasse en IDF',
        "meta": 'Démoussage de terrasse en Île-de-France : pourquoi la mousse revient, la pression adaptée à chaque support, et la saison qui donne le meilleur résultat.',
        "image": 'ba-terrasse2-apres.webp',
        "lead": "La mousse n'est pas de la saleté : c'est un végétal vivant, qui a des racines. C'est pourquoi un simple passage à la haute pression la fait disparaître un mois puis revenir.",
        "sections": [
            ('Pourquoi la mousse revient toujours', [
                'La haute pression arrache la partie visible de la mousse. Elle ne touche pas les spores, ni le mycélium logé dans la porosité du support. Trois semaines plus tard, la colonisation repart du même endroit.',
                "C'est pour cela qu'un démoussage sérieux se fait en deux temps : décapage mécanique d'abord, traitement anti-mousse ensuite, avec un temps d'action de plusieurs heures à plusieurs jours selon le produit.",
                "Le traitement seul, sans décapage préalable, ne fonctionne pas mieux : il ne pénètre pas à travers une couche de mousse épaisse. L'ordre compte autant que les deux opérations.",
                "Les terrasses les plus touchées sont celles exposées au nord, sous les arbres, ou mal drainées. Là où l'eau stagne et où le soleil ne sèche pas, la mousse est structurelle : elle reviendra, et l'objectif réaliste est d'espacer les passages, pas de l'éliminer définitivement.",
            ]),
            ('La pression selon le support', [
                "C'est le point où l'on abîme le plus de terrasses, et les dégâts sont irréversibles.",
                '<strong>Le bois</strong> ne supporte pas la haute pression frontale : elle arrache les fibres tendres du printemps et laisse un aspect pelucheux qui grisera plus vite ensuite. Il se traite à pression modérée, en éventail, dans le sens de la fibre.',
                '<strong>La pierre naturelle tendre</strong> — calcaire, pierre de Bourgogne — se creuse. Une pression trop forte laisse des sillons visibles en lumière rasante.',
                '<strong>Le carrelage extérieur</strong> supporte bien la pression, mais ses joints, non : on les déchausse facilement, et un joint parti se refait au ciment, pas au nettoyeur.',
                '<strong>Le béton désactivé et les dalles gravillonnées</strong> acceptent la pression la plus forte, à condition de ne pas insister au même endroit.',
                "Nous réglons la pression et la distance de buse selon le support, et nous faisons un essai sur une zone discrète avant de traiter l'ensemble. C'est une minute qui évite un regret durable.",
            ]),
            ('La bonne saison', [
                "Le printemps et l'automne donnent les meilleurs résultats. Le produit anti-mousse a besoin d'humidité pour agir et de douceur pour ne pas s'évaporer trop vite : en plein été, sur une dalle brûlante, il sèche avant d'avoir pénétré.",
                "L'automne a un avantage supplémentaire : traiter avant l'hiver empêche la mousse de s'installer pendant la période où elle prospère le plus. Une terrasse traitée en octobre traverse l'hiver bien mieux qu'une terrasse traitée en avril.",
                "Évitez de traiter juste avant une forte pluie, qui lessive le produit avant qu'il agisse, et par gel, qui bloque son action.",
            ]),
            ('Hydrofuge : utile ou non', [
                "Un traitement hydrofuge appliqué après le démoussage réduit la porosité du support. L'eau perle au lieu de pénétrer, la mousse s'accroche moins bien, et l'intervalle entre deux démoussages s'allonge nettement.",
                'Il se justifie sur les supports poreux — pierre naturelle, béton, terre cuite — et sur les terrasses exposées au nord. Il se justifie moins sur un carrelage émaillé, déjà peu poreux.',
                "Un point à connaître : un hydrofuge modifie légèrement l'aspect du support, souvent en le fonçant un peu. Nous faisons systématiquement un essai sur une zone cachée avant de traiter l'ensemble, pour que vous voyiez le rendu avant de décider.",
            ]),
        ],
        "faq": [
            ('Combien de temps un démoussage tient-il ?',
             "Un à trois ans selon l'exposition et le drainage. Une terrasse au nord, sous des arbres, se recolonise nettement plus vite qu'une terrasse ensoleillée et bien drainée. Un hydrofuge allonge l'intervalle."),
            ('Peut-on nettoyer une terrasse en bois au Kärcher ?',
             'À pression modérée seulement, en éventail et dans le sens de la fibre. La haute pression frontale arrache les fibres tendres et laisse un bois pelucheux qui grisera plus vite.'),
            ('Le produit anti-mousse est-il dangereux pour les plantes ?',
             'Nous protégeons les végétaux en bordure et nous rinçons les abords. Dites-nous ce qui est planté autour : cela conditionne le produit que nous employons et les précautions que nous prenons.'),
            ('Quelle est la meilleure saison ?',
             "Le printemps et l'automne. En plein été, le produit sèche avant d'avoir pénétré ; par gel, il n'agit pas. L'automne a l'avantage de protéger la terrasse pendant l'hiver."),
        ],
        "service": 'nettoyage-terrasse-paris',
    },
    {
        "slug": 'prix-nettoyage-terrasse-m2',
        "cat": 'Prix',
        "h1": "Prix d'un nettoyage de terrasse au mètre carré",
        "title": "Prix d'un nettoyage de terrasse",
        "meta": 'Ce que coûte un nettoyage de terrasse en Île-de-France : décapage, anti-mousse et hydrofuge, et ce qui fait varier le devis au mètre carré.',
        "image": 'ba-terrasse2-avant.webp',
        "lead": "Le prix d'un nettoyage de terrasse dépend moins de la surface que du support et de ce qu'on y ajoute après le décapage.",
        "sections": [
            ('Trois prestations, trois prix', [
                "Ce qu'on appelle « nettoyage de terrasse » recouvre en réalité trois opérations distinctes, qu'il faut distinguer sur un devis.",
                "<strong>Le décapage seul.</strong> Passage à la pression adaptée au support, évacuation des résidus. C'est la prestation de base, celle qui rend la terrasse propre immédiatement — et celle après laquelle la mousse revient en quelques semaines.",
                "<strong>Le décapage plus anti-mousse.</strong> On ajoute un traitement à temps d'action qui s'attaque aux spores et au mycélium. C'est ce qui fait la différence entre un an et trois mois de tranquillité.",
                "<strong>Le décapage, l'anti-mousse et l'hydrofuge.</strong> On termine par un produit qui réduit la porosité du support. C'est le plus cher et le plus durable, justifié sur pierre naturelle, béton et terre cuite.",
                "Un devis qui n'indique pas laquelle des trois est chiffrée ne veut rien dire. Demandez systématiquement.",
            ]),
            ('Ce qui fait varier le prix', [
                '<strong>Le support.</strong> Un béton désactivé se traite vite. Une terrasse en bois demande un travail dans le sens de la fibre, plus lent. Une pierre tendre impose des précautions qui allongent encore.',
                "<strong>L'état de départ.</strong> Une mousse épaisse installée depuis des années demande souvent deux passages : un premier décapage, un traitement, puis une reprise.",
                "<strong>L'accès à l'eau et à l'électricité.</strong> Nous venons avec notre matériel, notre eau et notre groupe si nécessaire — mais une terrasse accessible depuis un point d'eau se traite plus vite qu'un toit-terrasse où tout monte par l'escalier.",
                '<strong>Les abords.</strong> Une terrasse bordée de plantations demande une protection et un rinçage soigné des abords. Cela prend du temps et ce temps se facture.',
            ]),
            ('Repères et façon de chiffrer', [
                "Nous chiffrons sur devis après photos ou visite, plutôt qu'à un tarif au mètre carré affiché d'avance. Ce n'est pas une réticence commerciale : deux terrasses de 30 m² peuvent demander du simple au triple selon le support et l'état.",
                "Pour vous donner un ordre de grandeur avant même de nous contacter : c'est le support et l'ancienneté de la mousse qui commandent, pas la surface. Une petite terrasse en pierre tendre très encrassée coûte plus qu'une grande dalle béton entretenue.",
                "Les frais de déplacement — 5 € par tranche de 5 km depuis Tremblay-en-France — figurent sur le devis. Aucun acompte n'est demandé : vous réglez après avoir vu le résultat, ce qui est particulièrement pertinent sur une prestation aussi visible.",
            ]),
            ('Quand grouper les prestations', [
                "Une terrasse se nettoie rarement seule. Si vous nous faites venir, regardez ce qui l'entoure : le salon de jardin, les dalles de l'allée, le bas de mur, les volets, la façade accessible depuis le sol.",
                'Le déplacement est le même et le matériel est déjà en place. Le coût par surface traitée chute nettement quand tout se fait le même jour.',
                "Même logique pour la vitrerie : baies vitrées et véranda donnant sur la terrasse se traitent dans la foulée, à l'eau osmosée, sans nouveau déplacement.",
            ]),
        ],
        "faq": [
            ('Le prix est-il au mètre carré ?',
             "Nous chiffrons sur devis. Le support et l'ancienneté de la mousse pèsent plus que la surface : une petite terrasse en pierre tendre très encrassée coûte plus qu'une grande dalle béton entretenue."),
            ("L'hydrofuge vaut-il son prix ?",
             "Sur un support poreux — pierre naturelle, béton, terre cuite — et sur une terrasse exposée au nord, oui : il allonge nettement l'intervalle entre deux démoussages. Sur un carrelage émaillé, il apporte peu."),
            ("Faut-il un point d'eau sur place ?",
             "Non. Nous venons avec notre eau et notre matériel, y compris un groupe électrogène si nécessaire. Cela dit, un accès direct à l'eau accélère l'intervention et se répercute sur le devis."),
        ],
        "service": 'nettoyage-terrasse-paris',
    },
    {
        "slug": 'prix-nettoyage-bureaux-m2',
        "cat": 'Prix',
        "h1": "Prix d'un nettoyage de bureaux au mètre carré",
        "title": "Prix d'un nettoyage de bureaux au m²",
        "meta": "Tarifs d'entretien de bureaux en Île-de-France : fourchettes au m² et par mois, ce que cache un prix bas, et comment comparer deux devis.",
        "image": 'bureau-entreprise.webp',
        "lead": "Le tarif au mètre carré est le repère le plus utilisé et le plus trompeur du nettoyage professionnel. Voici ce qu'il recouvre réellement.",
        "sections": [
            ('Les fourchettes constatées', [
                'Pour un entretien courant de bureaux, les tarifs relevés en France en 2026 se situent entre 1,50 et 4,00 € du mètre carré et par mois. Le cœur de marché, pour des bureaux classiques entretenus plusieurs fois par semaine, tourne autour de 1,50 à 3,00 €.',
                'Sur un plateau de 100 m² avec un passage hebdomadaire, cela représente en pratique 200 à 400 € par mois.',
                "L'Île-de-France se situe 10 à 15 % au-dessus de la moyenne nationale, pour des raisons de coût logistique et de tension sur la main-d'œuvre. Les commerces se situent plutôt entre 2 et 4 € du mètre carré et par mois, à cause de l'exposition au public.",
            ]),
            ("Ce qu'un prix au m² ne dit pas", [
                "Un tarif au mètre carré n'a de sens que rapporté à une fréquence et à un périmètre. Trois devis affichant 2 € du m² peuvent recouvrir des prestations très différentes.",
                '<strong>La fréquence.</strong> Deux euros pour un passage hebdomadaire et deux euros pour trois passages hebdomadaires ne sont évidemment pas la même offre.',
                "<strong>Le périmètre.</strong> Les sanitaires sont-ils inclus ? Les vitres intérieures ? La cuisine ou l'espace café, qui demandent un traitement à part ? Les postes de travail eux-mêmes, ou seulement les circulations ?",
                "<strong>Le temps de présence.</strong> C'est la donnée décisive et celle qu'on ne trouve jamais sur un devis. Un prestataire qui reste quarante minutes sur un plateau de 200 m² ne fait pas le même travail que celui qui y reste deux heures, quel que soit le prix affiché.",
                "Demandez systématiquement le temps de présence par passage. C'est la seule question qui remet trois devis sur la même échelle.",
            ]),
            ("Ce qui n'est presque jamais dans le forfait", [
                'Certains postes sont facturés en supplément par la quasi-totalité des prestataires. Autant le savoir avant de comparer.',
                "L'extraction des moquettes, une à deux fois par an. Le nettoyage des vitres, en particulier extérieures. Le décapage et la remise en cire des sols durs. La remise en état après travaux ou après déménagement. Et la fourniture des consommables — papier, savon, sacs — qui représente un budget réel.",
                "Un devis qui inclut tout cela dans un forfait mensuel bas doit vous alerter : soit ces postes ne seront pas faits, soit ils feront l'objet d'un avenant en cours de contrat.",
            ]),
            ('Notre positionnement', [
                'Nous sommes une entreprise individuelle. Nous ne prenons pas de contrats multi-sites à grande échelle, et nous le disons clairement plutôt que de nous engager sur ce que nous ne pourrons pas tenir.',
                "Sur un site ou quelques sites proches, en revanche, vous avez la même personne à chaque passage. Elle connaît vos locaux, elle sait où sont les points sensibles, et elle remarque ce qui change. C'est une différence réelle par rapport à une rotation d'intervenants.",
                "Nous chiffrons avec le temps de présence indiqué, poste par poste, et nous distinguons ce qui est mensuel de ce qui est ponctuel. Vous n'aurez pas d'avenant en cours de route pour un poste que nous aurions oublié de mentionner.",
                "Nous intervenons en horaires décalés — avant ouverture, après fermeture, week-end — sans supplément, parce que c'est la seule façon de travailler correctement sur un site occupé.",
            ]),
        ],
        "faq": [
            ("Quel est le prix moyen d'un nettoyage de bureaux ?",
             "Entre 1,50 et 4,00 € du m² et par mois selon la fréquence et le périmètre, soit 200 à 400 € mensuels pour 100 m² avec un passage hebdomadaire. L'Île-de-France se situe 10 à 15 % au-dessus de la moyenne nationale."),
            ("Comment comparer deux devis d'entretien ?",
             'Par le temps de présence par passage, pas par le prix au mètre carré. Vérifiez ensuite le périmètre — sanitaires, vitres, espace café — et ce qui est ponctuel plutôt que mensuel.'),
            ('Les consommables sont-ils inclus ?',
             "Chez la plupart des prestataires, non : papier, savon et sacs sont facturés à part. Nous l'indiquons explicitement sur le devis, dans un sens comme dans l'autre."),
            ('Facturez-vous un supplément pour les horaires décalés ?',
             'Non. Avant ouverture, après fermeture ou le week-end, le tarif est le même.'),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'nettoyage-local-commercial-restaurant',
        "cat": 'Professionnels',
        "h1": 'Nettoyage de local commercial et de restaurant',
        "title": 'Nettoyage de local commercial',
        "meta": "Nettoyage de local commercial et de restaurant en Île-de-France : salle, sanitaires, vitrerie et sols, et ce qui relève d'un prestataire certifié.",
        "image": 'bureau-entreprise.webp',
        "lead": "Un commerce recevant du public se juge sur trois points : le sol, les sanitaires et la vitrine. Voici comment ils se traitent, et où s'arrête notre périmètre.",
        "sections": [
            ('Les trois points que voient vos clients', [
                "<strong>Le sol.</strong> C'est ce que l'on regarde en entrant, souvent sans y penser. Dans un commerce alimentaire ou une restauration, le point critique n'est pas la surface mais les joints de carrelage, qui noircissent et que le lavage quotidien n'atteint pas. Ils demandent un traitement périodique séparé, à la brosse et au produit à temps de pose.",
                "<strong>Les sanitaires.</strong> Le poste qui fait le plus de dégâts en avis clients. Les points réellement regardés sont le pied de cuvette, le joint entre la cuvette et le sol, le dessous du lavabo et l'état du distributeur. Une désinfection des points de contact, avec un produit adapté et un temps d'action respecté, fait la différence.",
                "<strong>La vitrine et la porte.</strong> Traitées à l'eau osmosée, elles sèchent sans trace. La porte concentre l'essentiel des traces de mains et s'oublie systématiquement.",
            ]),
            ('La contrainte des horaires', [
                "Un commerce ne se nettoie pas pendant qu'il reçoit du public. En restauration, la fenêtre est encore plus étroite : entre le service du soir et l'ouverture du lendemain, ou entre deux services.",
                "Nous intervenons avant ouverture, après fermeture et le week-end, sans supplément. Sur un restaurant, cela veut dire tard le soir ou tôt le matin, et nous en tenons compte dans le planning plutôt que d'imposer un créneau qui vous arrangerait mal.",
                "Le temps de séchage est le second paramètre. Un sol lavé doit être sec à l'ouverture : cela conditionne l'heure d'intervention autant que vos horaires.",
            ]),
            ('Ce que nous faisons', [
                "Salle et circulations : sols, mobilier, banquettes, vitrages intérieurs, luminaires accessibles. Les banquettes en tissu relèvent de l'injection-extraction et se traitent comme un canapé.",
                'Sanitaires : nettoyage complet, désinfection des points de contact, traitement du calcaire et des joints.',
                "Vitrerie : vitrine, porte, vitrages intérieurs, à l'eau osmosée.",
                'Extérieur accessible : devanture, seuil, terrasse en dur, mobilier de terrasse, à la pression adaptée au support.',
                "Odeurs : traitement par ozone sur un local vide, hors présence de personnes, d'animaux et de plantes, suivi d'une aération. Utile sur une odeur de friture installée ou après un dégât des eaux.",
                "Remise en état : reprise complète d'un local avant ouverture, après travaux ou en fin de bail commercial.",
            ]),
            ('Ce que nous ne faisons pas, et pourquoi', [
                "<strong>Le dégraissage certifié des hottes et conduits d'extraction.</strong> C'est une obligation d'entretien liée au risque incendie, que les assureurs contrôlent et qui donne lieu à un certificat délivré par une entreprise spécialisée. Nous dégraissons les surfaces et les filtres accessibles ; le conduit et le certificat relèvent d'un autre métier.",
                '<strong>La désinsectisation et la dératisation.</strong> Ce sont des activités réglementées, avec agrément et produits biocides soumis à autorisation. Nous ne les pratiquons pas et nous ne masquons pas un problème de nuisibles par un nettoyage.',
                "<strong>Le plan de maîtrise sanitaire HACCP.</strong> Nous pouvons exécuter des tâches qui s'y inscrivent, mais nous ne délivrons pas d'attestation de conformité sanitaire.",
                "Vous dire non sur ces trois points nous coûte des prestations. Cela vous évite surtout de croire couvert un risque qui ne l'est pas.",
            ]),
        ],
        "faq": [
            ('Nettoyez-vous les hottes de cuisine professionnelle ?',
             "Nous dégraissons les surfaces et les filtres accessibles. Le dégraissage du conduit d'extraction avec certificat, exigé par les assureurs au titre du risque incendie, relève d'une entreprise certifiée : ce n'est pas notre métier."),
            ('Intervenez-vous après le service, tard le soir ?',
             "Oui, et tôt le matin, sept jours sur sept, sans supplément. Le temps de séchage des sols conditionne l'heure autant que vos horaires d'ouverture."),
            ('Traitez-vous les banquettes en tissu ?',
             "Oui, par injection-extraction, comme un canapé. C'est souvent le poste le plus rentable d'un restaurant : une banquette reprise transforme la perception de la salle."),
            ('Pouvez-vous traiter une odeur de friture installée ?',
             "Oui, par ozone, après dégraissage des surfaces. Le traitement se fait local vide, hors présence de personnes, d'animaux et de plantes, et suivi d'une aération avant réouverture."),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'prix-nettoyage-fin-de-chantier-m2',
        "cat": 'Prix',
        "h1": "Prix d'un nettoyage de fin de chantier au m²",
        "title": "Prix d'un nettoyage de fin de chantier",
        "meta": 'Tarifs de nettoyage de fin de chantier en Île-de-France au mètre carré, différence entre premier et second passage, et ce qui fait varier le devis.',
        "image": 'intervention-3.webp',
        "lead": "Le nettoyage après travaux se facture au mètre carré, mais la fourchette est large parce qu'elle recouvre deux prestations très différentes.",
        "sections": [
            ('Les fourchettes du marché', [
                "Les tarifs relevés pour un nettoyage de fin de chantier se situent le plus souvent entre 4 et 10 € HT du mètre carré, avec un cœur de marché autour de 5 à 8 €. Certaines grilles montent jusqu'à 15 à 25 € du mètre carré sur des remises en état lourdes.",
                "Cet écart n'est pas un écart de marge : il recouvre des situations très différentes. Un appartement rénové proprement, protégé pendant les travaux, se traite vite. Un chantier où le plâtre a circulé partout demande plusieurs fois le même temps.",
                "En Île-de-France, comptez 15 à 25 % au-dessus des tarifs nationaux, essentiellement pour des raisons d'accès, de stationnement et d'évacuation.",
            ]),
            ('Premier passage et second passage', [
                "C'est la distinction que les devis expliquent mal et qui explique la moitié des malentendus.",
                'Le <strong>premier passage</strong>, ou nettoyage grossier, intervient dès la fin des travaux : évacuation des gravats fins, retrait des protections, décollage des adhésifs, dépoussiérage général. Il rend le chantier praticable.',
                "Le <strong>second passage</strong>, ou nettoyage de finition, intervient vingt-quatre à quarante-huit heures plus tard. Il est indispensable, et voici pourquoi : la poussière de plâtre est extrêmement fine et reste en suspension longtemps après la fin des travaux. Elle retombe pendant une journée entière. Nettoyer une seule fois, c'est nettoyer avant que la poussière ne soit redescendue.",
                "Un devis qui n'annonce qu'un seul passage sur un chantier avec plâtrerie vous laissera un logement à reprendre. Nous le disons systématiquement au devis, quitte à ce que notre chiffrage paraisse plus élevé qu'un concurrent qui ne l'annonce pas.",
            ]),
            ('Ce qui fait varier le prix', [
                '<strong>La nature des travaux.</strong> La plâtrerie et le ponçage génèrent la poussière la plus fine et la plus pénétrante. La peinture laisse des projections ponctuelles, plus faciles. La pose de sol laisse des colles et des joints.',
                "<strong>La protection pendant le chantier.</strong> Un chantier où les artisans ont bâché coûte nettement moins cher à nettoyer. C'est le meilleur investissement possible sur le poste nettoyage.",
                '<strong>Les vitrages.</strong> Les projections de peinture et de plâtre sur le verre demandent un travail à la lame, lent et minutieux, sur les vitrages qui le supportent.',
                "<strong>L'évacuation.</strong> Un chantier avec des déchets à évacuer n'est pas un chantier à nettoyer : c'est un débarras, qui relève d'une prestation et d'une filière différentes.",
                "<strong>L'accès.</strong> Étage sans ascenseur, absence de stationnement, chantier encore actif à côté : cela pèse davantage que la surface.",
            ]),
            ('Notre façon de chiffrer', [
                'Nous chiffrons sur photos ou sur place, en annonçant explicitement le nombre de passages prévus et ce que chacun comprend. Les frais de déplacement figurent au devis, à 5 € par tranche de 5 km depuis Tremblay-en-France.',
                "Nous n'exigeons aucun acompte. Sur une fin de chantier, où le résultat se juge d'un coup d'œil, cela nous paraît la moindre des choses.",
                'Un conseil qui ne nous rapporte rien : faites protéger pendant les travaux. Une bâche posée sur un parquet coûte quelques euros et vous économise une remise en état.',
            ]),
        ],
        "faq": [
            ('Pourquoi faut-il deux passages ?',
             "La poussière de plâtre est si fine qu'elle reste en suspension et retombe pendant vingt-quatre à quarante-huit heures. Nettoyer une seule fois revient à nettoyer avant qu'elle ne soit redescendue."),
            ('Évacuez-vous les gravats ?',
             "Nous évacuons les résidus fins liés au nettoyage. Les gravats, encombrants et déchets de chantier relèvent d'un débarras et d'une filière de traitement différente : c'est un autre métier et un autre devis."),
            ('Retirez-vous la peinture sur les vitres ?',
             'Oui, à la lame sur les vitrages qui le supportent. Nous ne le faisons pas sur un verre traité, teinté ou filmé, qui se rayerait définitivement.'),
        ],
        "service": 'nettoyage-fin-de-chantier-paris',
    },
    {
        "slug": 'nettoyage-siege-voiture-tache',
        "cat": 'Automobile',
        "h1": 'Nettoyage de sièges de voiture et détachage',
        "title": 'Nettoyage de sièges de voiture',
        "meta": 'Nettoyage de sièges de voiture à domicile : méthode selon la matière, taches courantes, temps de séchage et ce qui ne part pas.',
        "image": 'auto-interieur-vw.webp',
        "lead": 'Un siège de voiture cumule tout ce qui complique un détachage : une fibre serrée, une mousse épaisse en dessous, et un habitacle qui sèche mal.',
        "sections": [
            ('Chaque matière, sa méthode', [
                "<strong>Le tissu</strong> est le cas le plus courant et le plus favorable. Il se traite par injection-extraction : on injecte, on aspire immédiatement, la mousse en dessous ne se gorge pas d'eau.",
                "<strong>L'alcantara et les microfibres synthétiques</strong> demandent beaucoup plus de retenue. Trop d'eau les tache en auréole et le poil se couche définitivement s'il sèche mal. On travaille par petites zones, avec un brossage du sens du poil au séchage.",
                "<strong>Le cuir</strong> ne se nettoie pas, il s'entretient. Un nettoyant à pH neutre, puis un nourrissant. Un cuir dégraissé sans être nourri redevient sec et craquelle — le nettoyage l'abîme alors au lieu de le préserver. C'est une prestation en option chez nous, précisément parce qu'elle demande ces deux temps.",
                '<strong>Le simili</strong> se nettoie facilement mais se raye. On évite tout ce qui est abrasif, y compris les éponges à gratter dites « douces ».',
            ]),
            ('Les taches les plus fréquentes', [
                "<strong>Le café et les sodas.</strong> Sucre et tanins. Ils s'extraient bien s'ils sont récents. Le sucre laisse un résidu collant qui refixe la poussière : c'est pour cela qu'une tache de soda « revient » quelques semaines après un nettoyage superficiel.",
                "<strong>Le gras et les cosmétiques.</strong> Fond de teint sur l'appuie-tête, crème solaire sur le dossier. Ils demandent un solvant adapté avant l'extraction ; l'eau seule ne fait rien sur un corps gras.",
                "<strong>Le lait et le vomi.</strong> Sur les sièges enfants surtout. L'urgence n'est pas la tache mais l'odeur, qui vient de la fermentation dans la mousse. Il faut extraire en profondeur, sinon l'odeur revient à la première journée chaude.",
                "<strong>L'encre et le stylo.</strong> Le cas le plus difficile. Un résultat partiel est fréquent, un échec possible. Nous le disons avant de commencer.",
                '<strong>Le sang.</strong> Se traite à froid, exclusivement. La chaleur coagule les protéines et fixe la tache définitivement : une eau chaude bien intentionnée rend la tache irrécupérable.',
            ]),
            ('Le séchage, vrai point critique en voiture', [
                "Un habitacle est un volume clos, mal ventilé, où l'humidité ne s'évacue pas. C'est ce qui différencie un siège auto d'un canapé.",
                "Un siège trop mouillé, dont la mousse s'est gorgée, met plusieurs jours à sécher et développe une odeur de moisi caractéristique. Le remède est alors pire que le mal d'origine.",
                "C'est pourquoi nous travaillons en extraction contrôlée, en aspirant plus que nous n'injectons, et pourquoi nous laissons les portes ouvertes pendant l'intervention. Comptez deux à quatre heures avant de rouler vitres fermées, davantage par temps humide.",
                "Un conseil pratique : faites traiter le matin d'une journée sèche plutôt qu'un soir de pluie. Cela change réellement le résultat.",
            ]),
            ("Quand l'odeur reste malgré tout", [
                "Certaines odeurs ne sont pas dans le tissu mais dans le circuit de ventilation, sous les sièges, ou dans la mousse en profondeur. L'extraction ne les atteint pas.",
                "Dans ces cas, un traitement par ozone finit le travail : le gaz circule dans tout l'habitacle, y compris les conduits d'aération, et détruit les molécules odorantes au lieu de les masquer. C'est la seule méthode efficace sur une odeur de tabac ancienne.",
                "Le protocole est strict : véhicule vide, personne à bord, puis aération avant restitution. L'ozone est un gaz irritant pour les voies respiratoires ; il ne se pratique jamais en présence de quelqu'un. Nous le proposons à partir de 30 €, en complément d'un nettoyage — jamais à sa place, car une odeur dont la source est encore présente reviendra.",
            ]),
        ],
        "faq": [
            ('Combien de temps avant de pouvoir rouler ?',
             'Deux à quatre heures vitres fermées, davantage par temps humide. Nous travaillons en extraction contrôlée pour ne pas gorger la mousse, ce qui est le vrai risque en habitacle clos.'),
            ('Une tache de stylo part-elle ?',
             'Rarement complètement. Nous obtenons souvent une atténuation nette, parfois un échec. Nous le disons avant de commencer plutôt que de vous le facturer après.'),
            ('Que faire immédiatement après avoir renversé quelque chose ?',
             "Tamponnez avec un chiffon blanc, sans frotter, du bord vers le centre. N'appliquez aucun produit : un produit ménager mal choisi peut fixer la tache ou décolorer le tissu autour."),
            ('Traitez-vous les sièges en cuir ?',
             'Oui, en option : nettoyant à pH neutre puis nourrissant. Les deux temps sont indispensables — un cuir dégraissé sans être nourri redevient sec et craquelle.'),
        ],
        "service": 'nettoyage-automobile-paris',
    },
    {
        "slug": 'lavage-auto-domicile-paris',
        "cat": 'Automobile',
        "h1": 'Lavage auto à domicile à Paris et en Île-de-France',
        "title": 'Lavage auto à domicile à Paris',
        "meta": "Lavage auto à domicile à Paris : ce que le lavage sans eau permet, ce qu'il ne permet pas, et l'intérêt d'une intervention sur votre place.",
        "image": 'auto-interieur-vw.webp',
        "lead": 'Faire laver sa voiture là où elle est stationnée supprime le seul vrai coût du lavage : le temps que vous y passez. Encore faut-il savoir ce que cela permet techniquement.',
        "sections": [
            ('Pourquoi le domicile change tout à Paris', [
                "En zone dense, aller au lavage représente facilement une heure entre le trajet, l'attente et le retour — sans compter la place de stationnement qu'on abandonne et qu'on ne retrouve pas.",
                "Une intervention sur place supprime tout cela. Nous venons avec l'eau, l'électricité et le matériel : vous n'avez ni point d'eau ni prise à fournir, ce qui rend l'intervention possible en rue, en parking souterrain ou sur une place d'entreprise.",
                "Le seul prérequis est un accès raisonnable au véhicule, avec assez d'espace pour ouvrir les portes et tourner autour. En parking souterrain, vérifiez la hauteur sous plafond si vous nous prévenez d'un utilitaire.",
            ]),
            ("Lavage sans eau : ce que c'est vraiment", [
                "Le lavage dit « sans eau » n'est pas magique : c'est un produit lubrifiant pulvérisé qui encapsule la poussière pour qu'elle glisse au lieu de rayer, puis un essuyage à la microfibre propre.",
                "Il fonctionne très bien sur un véhicule peu sale — poussière, pollen, traces de pluie. C'est le cas d'une voiture entretenue régulièrement, et c'est la majorité des situations en ville.",
                "Il ne fonctionne pas sur un véhicule réellement encrassé : boue, sable, sel d'hiver, fientes séchées. Sur ces salissures, essuyer sans rincer revient à passer un abrasif sur la peinture. Nous préférons alors un lavage à l'eau, avec la méthode des deux seaux ou au nettoyeur à basse pression.",
                "Autrement dit, la technique dépend de l'état du véhicule et non d'une préférence commerciale. Nous regardons avant de choisir, et nous vous le disons.",
            ]),
            ('Ce qui compte plus que le lavage lui-même', [
                "La façon d'essuyer fait plus de dégâts que le produit employé. Les micro-rayures circulaires visibles au soleil sur les carrosseries foncées viennent presque toutes d'un essuyage avec une microfibre chargée de poussière, ou d'un rouleau de station.",
                "Nous travaillons avec plusieurs microfibres, changées dès qu'elles se salissent, et jamais la même pour les bas de caisse et pour le capot. Ce détail explique l'essentiel de la différence de résultat à un an.",
                "Les jantes se traitent en premier et avec un matériel dédié : la poussière de frein est métallique et abrasive, et une brosse qui a servi aux jantes n'a rien à faire sur la carrosserie.",
            ]),
            ('Formules et ce que nous ne faisons pas', [
                "Nos formules vont de l'extérieur seul à l'intérieur complet, avec un pack combinant les deux. Les tarifs partent de 40 € et figurent sur notre grille tarifaire, avec le détail de ce que chaque formule comprend.",
                "Les options les plus demandées sont le retrait des poils d'animaux, l'entretien du cuir et le traitement des odeurs par ozone.",
                "Ce que nous ne faisons pas : le nettoyage moteur sous pression, qui expose les connectiques et l'électronique à un risque disproportionné au bénéfice ; le polissage correctif à la machine sur peinture abîmée, qui relève du carrossier ; et la rénovation d'optiques oxydées, qui demande un ponçage et un vernis.",
                "Sur une carrosserie très marquée, nous pouvons améliorer nettement l'aspect sans prétendre effacer des rayures qui ont traversé le vernis. Nous le disons au devis, sur photos, avant d'intervenir.",
            ]),
        ],
        "faq": [
            ("Faut-il un point d'eau ou une prise électrique ?",
             "Non. Nous venons avec notre eau, notre électricité et notre matériel. L'intervention est possible en rue, en parking souterrain ou sur une place d'entreprise."),
            ('Le lavage sans eau raye-t-il la peinture ?',
             "Pas sur un véhicule peu sale, pour lequel il est conçu. Sur un véhicule réellement encrassé — boue, sable, sel — il devient risqué : nous passons alors à un lavage à l'eau. C'est l'état du véhicule qui décide, pas une préférence."),
            ('Nettoyez-vous le moteur ?',
             "Pas sous pression. Le risque pour les connectiques et l'électronique est disproportionné par rapport au bénéfice esthétique. Nous nous limitons à un dépoussiérage des abords visibles."),
            ('Combien de temps dure une intervention ?',
             "D'environ une heure pour un extérieur seul à trois heures pour un intérieur complet avec extraction des sièges. Le devis précise la durée estimée."),
        ],
        "service": 'nettoyage-automobile-paris',
    },
    {
        "slug": 'nettoyage-apres-travaux-appartement',
        "cat": 'Chantier',
        "h1": 'Nettoyage après travaux dans un appartement',
        "title": "Nettoyage après travaux d'appartement",
        "meta": "Nettoyage après travaux en appartement : pourquoi la poussière de plâtre revient, l'ordre des opérations et les surfaces à ne pas gratter.",
        "image": 'intervention-3.webp',
        "lead": "La poussière de chantier n'est pas de la poussière ordinaire. Elle est plus fine, elle vole plus longtemps, et elle se dépose une deuxième fois après votre premier nettoyage.",
        "sections": [
            ('Pourquoi elle revient le lendemain', [
                'Une particule de plâtre poncé mesure quelques microns. À cette taille, elle ne tombe pas : elle flotte. Un grain de sable retombe en une seconde, une particule de plâtre met des heures.',
                "Elle est aussi remise en suspension au moindre mouvement d'air — une porte qui s'ouvre, un radiateur qui démarre, quelqu'un qui traverse la pièce. C'est un cycle qui se répète pendant vingt-quatre à quarante-huit heures après la fin des travaux.",
                "D'où la règle : deux passages, espacés d'au moins vingt-quatre heures. Le premier retire l'essentiel, le second récupère ce qui est retombé. Un seul passage donne un logement propre le soir même et poussiéreux le lendemain matin, et c'est le motif de déception numéro un sur ce type de prestation.",
                "Si vous ne pouvez faire qu'un seul passage, faites-le le plus tard possible : deux jours après la fin des travaux plutôt que le jour même.",
            ]),
            ("L'ordre des opérations", [
                'On commence par ce qui est en hauteur et on descend, comme toujours, mais avec deux étapes propres au chantier.',
                "D'abord le retrait des protections et des adhésifs — bâches, films de fenêtre, ruban de masquage. Un adhésif laissé trop longtemps au soleil laisse une colle bien plus difficile à retirer : c'est la première chose à faire.",
                "Ensuite l'aspiration, jamais le balayage. Balayer une poussière de plâtre revient à la remettre en l'air. Il faut un aspirateur à filtration fine, sinon on la rejette par la sortie d'air.",
                "Puis le lavage des surfaces, du haut vers le bas, avec un rinçage fréquent — le plâtre en suspension dans l'eau de lavage laisse un voile blanc en séchant, et c'est ce qui donne cet aspect terne sur les carrelages après travaux.",
                "Les sols en dernier, en reculant vers la sortie, et souvent deux fois : un premier lavage qui charge l'eau, un second qui rince réellement.",
            ]),
            ('Les surfaces à ne pas gratter', [
                'Sur un chantier, on est tenté de gratter tout ce qui accroche. Certaines surfaces ne le supportent pas, et les dégâts sont définitifs.',
                "<strong>Les vitrages traités, teintés ou filmés.</strong> La lame les raye. Nous ne l'utilisons que sur du verre nu, après vérification.",
                "<strong>Les robinetteries et les inox brossés.</strong> Une éponge abrasive raye le chrome et casse le sens du brossage sur l'inox — la trace reste visible sous tous les éclairages.",
                "<strong>Les parquets vitrifiés récents.</strong> Le vernis met plusieurs semaines à durcir complètement. Un lavage trop mouillé ou un produit trop alcalin le mate. Nous travaillons à l'humidité minimale sur un parquet neuf.",
                '<strong>Les peintures fraîches.</strong> Une peinture a besoin de plusieurs semaines pour atteindre sa dureté finale. On dépoussière, on ne lessive pas.',
            ]),
            ("Ce qui relève d'un autre métier", [
                "Le nettoyage de fin de chantier n'est pas un débarras. Nous évacuons les résidus fins liés au nettoyage ; les gravats, les chutes de matériaux et les encombrants relèvent d'une benne et d'une filière de traitement, avec ses propres obligations.",
                "De même, une tache de peinture sur un carrelage poreux ou une coulure d'enduit dans un joint relèvent parfois de la reprise par l'artisan, pas du nettoyage. Nous vous le signalons plutôt que d'insister au risque d'abîmer le support.",
                "Enfin, si votre logement a subi un dégât des eaux pendant les travaux, une odeur d'humidité peut persister après séchage. Un traitement par ozone la traite efficacement, à condition que la source ait été traitée d'abord — sinon elle reviendra.",
            ]),
        ],
        "faq": [
            ('Combien de temps après les travaux faut-il nettoyer ?',
             'Attendez au moins vingt-quatre heures après le dernier ponçage, le temps que la poussière retombe. Idéalement, prévoyez deux passages espacés de vingt-quatre à quarante-huit heures.'),
            ('Peut-on laver un parquet vitrifié neuf ?',
             "Avec une humidité minimale seulement. Le vernis met plusieurs semaines à durcir complètement : trop d'eau ou un produit trop alcalin le mate définitivement."),
            ('Évacuez-vous les gravats ?',
             "Non, uniquement les résidus fins liés au nettoyage. Les gravats et encombrants relèvent d'un débarras avec benne, qui est un autre métier et une autre filière."),
        ],
        "service": 'nettoyage-fin-de-chantier-paris',
    },
    {
        "slug": 'nettoyage-veranda-baie-vitree',
        "cat": 'Vitrerie',
        "h1": 'Nettoyage de véranda et de baie vitrée',
        "title": 'Nettoyage de véranda et baie vitrée',
        "meta": "Nettoyage de véranda et de baie vitrée : toiture inclinée, rails de coulissants, joints et structure, et les vitrages qu'on ne gratte jamais.",
        "image": 'vitre-controle.webp',
        "lead": "Une véranda pose un problème que n'a pas une fenêtre : sa toiture est inclinée, exposée en permanence, et personne ne la voit jusqu'à ce qu'elle assombrisse la pièce.",
        "sections": [
            ('La toiture, la vraie difficulté', [
                "Le vitrage de toiture d'une véranda reçoit tout : pluie chargée de particules, pollen, fientes, feuilles, et le ruissellement des arbres alentour. Il ne s'auto-nettoie pas, contrairement à une vitre verticale que la pluie rince en partie.",
                "Le dépôt s'accumule d'abord dans le bas des panneaux, contre les traverses, puis remonte. Le résultat est progressif et donc peu remarqué : la lumière baisse d'année en année sans qu'on identifie la cause.",
                "Nous traitons ces toitures depuis le sol, avec une perche télescopique alimentée en eau osmosée. C'est plus sûr que de monter dessus — beaucoup de toitures de véranda en polycarbonate ou en verre feuilleté ne sont pas conçues pour supporter un poids — et l'eau osmosée sèche sans laisser de trace, ce qui est décisif sur une surface qu'on ne peut pas essuyer.",
            ]),
            ('Les rails, les joints et la structure', [
                "Les rails de baies coulissantes accumulent de la poussière, du sable et des graviers, qui finissent par gêner le coulissement et user les galets. C'est un point d'entretien mécanique autant que de propreté, et il est presque toujours oublié.",
                "Ils demandent une aspiration fine avant tout lavage : verser de l'eau dans un rail plein de poussière crée une boue qui durcit et empire les choses.",
                "Les joints en caoutchouc, eux, se nettoient sans solvant : un solvant les dessèche et les fait craqueler, ce qui compromet l'étanchéité. Eau et produit neutre suffisent.",
                "La structure — aluminium laqué ou PVC — se lave à l'eau savonneuse. Le PVC jauni par les UV ne se récupère pas au nettoyage : c'est le matériau qui a évolué, pas un encrassement.",
            ]),
            ("Ce qu'on ne gratte jamais", [
                'Le réflexe de la lame sur une trace tenace ruine plus de vitrages que tout le reste.',
                '<strong>Le polycarbonate</strong>, très courant en toiture de véranda, est un plastique : il se raye au moindre grattage et les rayures se voient à contre-jour de façon permanente.',
                "<strong>Les vitrages à couche</strong> — autonettoyants, à contrôle solaire, à isolation renforcée — portent un traitement de surface d'une finesse de quelques nanomètres. Une lame ou une éponge abrasive le retire par plaques, et le vitrage devient irrégulier.",
                '<strong>Les films posés après coup</strong>, solaires ou anti-effraction, se rayent et se décollent.',
                "En pratique, nous partons du principe qu'un vitrage est traité tant que le contraire n'est pas établi. Sur une trace résistante, nous passons du temps plutôt que d'employer la force.",
            ]),
            ('La bonne fréquence', [
                "Deux passages par an conviennent à la plupart des vérandas : un au printemps, après la saison des pluies et avant les pollens, un à l'automne, après la chute des feuilles.",
                'Une véranda sous des arbres demande davantage, surtout si des résineux la surplombent : la résine se fixe et devient difficile à retirer si on la laisse cuire au soleil tout un été.',
                "L'intérieur suit un rythme différent : c'est la condensation qui commande. Une véranda mal ventilée développe des traces de condensation et des moisissures dans les angles bas des vitrages, qu'il vaut mieux traiter avant qu'elles ne s'installent dans les joints.",
            ]),
        ],
        "faq": [
            ('Montez-vous sur la toiture de la véranda ?',
             'Non. Beaucoup de toitures en polycarbonate ou en verre feuilleté ne supportent pas un poids. Nous travaillons depuis le sol, à la perche télescopique alimentée en eau osmosée.'),
            ('Peut-on gratter une trace sur un vitrage de véranda ?',
             'Nous ne le faisons pas. Le polycarbonate se raye définitivement et les vitrages à couche perdent leur traitement de surface. Nous privilégions le temps de pose à la force.'),
            ('À quelle fréquence nettoyer une véranda ?',
             "Deux fois par an, au printemps et à l'automne. Davantage si des arbres la surplombent, en particulier des résineux."),
        ],
        "service": 'nettoyage-vitres-paris',
    },
    {
        "slug": 'nettoyage-canape-cuir-alcantara',
        "cat": 'Textile',
        "h1": 'Nettoyage de canapé en cuir et en alcantara',
        "title": 'Nettoyage de canapé cuir et alcantara',
        "meta": "Entretien d'un canapé en cuir ou en alcantara : pourquoi l'eau ne suffit pas, les produits à éviter, et ce qui ne se rattrape plus.",
        "image": 'canape-nettoyage.webp',
        "lead": "Le cuir et l'alcantara sont les deux matières où un nettoyage mal conduit fait plus de dégâts que l'encrassement qu'il prétend traiter.",
        "sections": [
            ("Le cuir ne se nettoie pas, il s'entretient", [
                "Un cuir de canapé est une peau tannée, recouverte le plus souvent d'une finition pigmentée. Ce qui l'abîme n'est pas la saleté mais le dessèchement : les huiles de tannage migrent lentement, la fibre perd sa souplesse et finit par craqueler aux points de flexion — l'assise, les accoudoirs.",
                "Un nettoyage dégraissant accélère ce processus s'il n'est pas suivi d'un nourrissant. C'est l'erreur la plus fréquente : on nettoie, le cuir paraît net, et six mois plus tard il est plus sec qu'avant.",
                "L'entretien correct se fait donc en deux temps : un nettoyant à pH neutre qui retire le film de sébum et de poussière, puis un lait nourrissant qui restitue la souplesse. Les deux, systématiquement.",
                "Ce qui est à proscrire : les lingettes ménagères, les nettoyants multi-usages alcalins, l'alcool, et tout ce qui contient un solvant. Ils dissolvent la finition pigmentée, ce qui se voit d'abord comme un éclaircissement puis comme une usure irrégulière.",
            ]),
            ('Le cas particulier du cuir aniline', [
                "Il existe deux grandes familles. Le cuir pigmenté, majoritaire, porte une couche de finition qui le protège : il tolère un nettoyage aqueux léger. Le cuir aniline ou semi-aniline, plus haut de gamme, est teinté dans la masse sans couche protectrice — c'est ce qui lui donne son toucher et sa patine.",
                "Sur un aniline, une goutte d'eau laisse une auréole. Un produit aqueux appliqué sur toute la surface en laisse partout.",
                "Le test qui les distingue, à faire dans un endroit caché : déposez une goutte d'eau. Si elle perle, le cuir est pigmenté. Si elle pénètre et fonce immédiatement, il est aniline et relève d'un entretien à sec, avec des produits spécifiques.",
                'Nous faisons ce test avant toute intervention. Un canapé aniline mal traité perd sa valeur, et cela ne se rattrape pas.',
            ]),
            ("L'alcantara et les microfibres", [
                "L'alcantara est une microfibre synthétique dont l'aspect vient de la façon dont le poil accroche la lumière. Deux choses le dégradent : trop d'eau, qui laisse une auréole nette au séchage, et un poil couché qui sèche dans cette position.",
                "On y travaille donc par petites zones, avec une extraction très contrôlée — on aspire beaucoup plus qu'on n'injecte — et un brossage du sens du poil pendant le séchage. Un séchage sans brossage donne des zones mates et des zones brillantes qui se voient sous tous les éclairages.",
                "Une tache grasse sur alcantara demande un solvant adapté avant l'extraction. L'eau seule n'a aucun effet sur un corps gras, et insister à l'eau ne fait qu'étendre l'auréole.",
            ]),
            ('Ce qui ne se rattrape plus', [
                "Autant le dire clairement, parce que c'est ce que les gens espèrent le plus.",
                "Un cuir craquelé aux points de flexion ne revient pas. Les fibres sont cassées ; un nourrissant assouplit la zone autour mais ne recolle rien. Cela relève d'une réfection en atelier, voire d'un remplacement de panneau.",
                "Une finition pigmentée usée jusqu'à laisser apparaître la couleur naturelle du cuir — fréquent sur les accoudoirs — relève d'une retouche de teinte, qui est un métier de sellier.",
                'Un alcantara dont le poil a été arraché par un frottement répété ne se redresse pas.',
                'Nous regardons ces points sur vos photos avant de vous proposer une intervention. Quand nous estimons que le résultat vous décevra, nous le disons plutôt que de le facturer.',
            ]),
        ],
        "faq": [
            ('Comment savoir si mon cuir est aniline ?',
             "Déposez une goutte d'eau dans un endroit caché. Si elle perle, le cuir est pigmenté. Si elle pénètre et fonce aussitôt, il est aniline : il demande un entretien à sec et ne tolère pas les produits aqueux."),
            ('Peut-on nettoyer un canapé en cuir avec une lingette ménagère ?',
             "Non. Les lingettes multi-usages sont alcalines et dessèchent la finition. À terme, elles font davantage de dégâts que la saleté qu'elles retirent."),
            ('Un canapé en alcantara peut-il être traité à domicile ?',
             "Oui, avec une extraction très contrôlée et un brossage du poil au séchage. C'est la maîtrise de la quantité d'eau qui fait tout le résultat sur cette matière."),
            ('Un cuir craquelé se répare-t-il par nettoyage ?',
             "Non. Les fibres sont cassées : un nourrissant assouplit les abords mais ne reconstitue rien. Cela relève d'une réfection en atelier."),
        ],
        "service": 'nettoyage-textile-paris',
    },
    {
        "slug": 'nettoyage-fauteuil-chaise-bureau',
        "cat": 'Professionnels',
        "h1": 'Nettoyage de fauteuils et chaises de bureau',
        "title": 'Nettoyage de fauteuils de bureau',
        "meta": 'Nettoyage de sièges et fauteuils de bureau en entreprise : assise, dossier, accoudoirs et roulettes, avec un séchage compatible avec la reprise.',
        "image": 'bureau-entreprise.webp',
        "lead": 'Un fauteuil de bureau est utilisé sept heures par jour, cinq jours par semaine, par la même personne. Aucun textile domestique ne subit cela.',
        "sections": [
            ('Où se concentre réellement la saleté', [
                "Trois zones, et elles ne sont pas celles qu'on croit.",
                "<strong>L'assise</strong> reçoit la transpiration et le sébum, en continu. C'est la zone qui fonce le plus, de manière uniforme, si progressivement que personne ne le remarque avant de comparer avec un siège neuf.",
                "<strong>Le haut du dossier</strong> reçoit le contact des cheveux et des produits capillaires. C'est là qu'apparaît le film gras le plus net, et c'est la zone la plus visible quand on entre dans un open space.",
                "<strong>Les accoudoirs</strong>, souvent en polyuréthane, deviennent collants. Ce n'est pas de la saleté déposée : c'est le matériau lui-même qui se dégrade par hydrolyse. Un accoudoir vraiment poisseux ne se nettoie pas, il se remplace.",
                "S'ajoutent les roulettes, où s'enroulent cheveux et fibres de moquette au point de bloquer la rotation. Cela se démonte et se dégage, et c'est cinq minutes qui rendent le siège à nouveau confortable.",
            ]),
            ('La méthode et la contrainte de séchage', [
                "Le tissu d'un siège de bureau est en général un polyester serré, robuste, qui supporte bien l'injection-extraction. La difficulté n'est pas la matière, c'est la mousse dessous : épaisse, elle retient l'eau et sèche lentement.",
                "On travaille donc en extraction franche, en aspirant nettement plus qu'on n'injecte, avec un prétraitement des zones grasses. Comptez trois à cinq heures de séchage, ce qui impose de traiter en fin de journée ou le vendredi.",
                "Le mesh, ces dossiers en résille tendue très répandus, se traite différemment : il ne retient pas la saleté en profondeur mais l'accumule sur le cadre et dans la tension du maillage. Un dépoussiérage et un nettoyage de surface suffisent, et une extraction serait inutile.",
                "Les piètements et vérins se dépoussièrent et se dégraissent : c'est là que se voit la différence entre un siège nettoyé et un siège remis à neuf.",
            ]),
            ("Organiser l'intervention sur un plateau", [
                'Traiter cinquante sièges un par un pendant les heures de bureau ne fonctionne pas : chaque personne perd son poste pendant plusieurs heures.',
                'Le schéma qui marche : intervention le vendredi après-midi ou le vendredi soir, sièges regroupés par zone, séchage pendant le week-end, plateau récupéré le lundi. Sur les grands plateaux, on procède par zones sur plusieurs semaines.',
                "Nous traitons volontiers les sièges en même temps que l'extraction de la moquette : le matériel est le même, le déplacement est unique, et le coût par siège baisse nettement. C'est le regroupement le plus rentable sur ce type de prestation.",
            ]),
            ('Remplacer ou nettoyer', [
                "Un siège de bureau correct coûte plusieurs centaines d'euros. Le nettoyer en coûte une fraction, et prolonge son usage de plusieurs années. Le calcul est presque toujours favorable au nettoyage.",
                "Sauf dans trois cas. Un accoudoir en polyuréthane poisseux, comme dit plus haut : c'est le matériau qui se décompose. Une mousse d'assise affaissée, qui ne soutient plus : c'est un enjeu de confort et de santé au travail, pas de propreté. Et un vérin à gaz qui ne tient plus la hauteur, qui est une pièce d'usure à remplacer.",
                "Dans ces cas, nettoyer ne sert à rien et nous vous le disons. Le reste du temps, un plateau de sièges repris change l'impression générale des locaux pour un budget sans rapport avec un renouvellement.",
            ]),
        ],
        "faq": [
            ('Combien de temps un fauteuil de bureau met-il à sécher ?',
             "Trois à cinq heures. La mousse d'assise est épaisse et retient l'eau : nous travaillons en extraction franche et nous privilégions une intervention le vendredi."),
            ('Traitez-vous les dossiers en résille ?',
             "Oui, mais différemment. Le mesh ne retient pas la saleté en profondeur : un dépoussiérage et un nettoyage de surface suffisent, une extraction n'apporterait rien."),
            ('Un accoudoir collant se nettoie-t-il ?',
             "Non. Un polyuréthane poisseux se décompose par hydrolyse : c'est le matériau lui-même qui se dégrade. Il se remplace, il ne se nettoie pas."),
            ('Peut-on traiter les sièges en même temps que la moquette ?',
             "Oui, et c'est la solution la plus économique : même matériel, même déplacement, coût par siège nettement réduit."),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'nettoyage-salon-jardin-mobilier-exterieur',
        "cat": 'Extérieur',
        "h1": 'Nettoyage de salon de jardin et mobilier extérieur',
        "title": 'Nettoyage de salon de jardin',
        "meta": "Nettoyage de mobilier de jardin : résine tressée, teck, aluminium et coussins d'extérieur, avec la méthode adaptée à chaque matériau.",
        "image": 'ba-terrasse2-apres.webp',
        "lead": "Le mobilier d'extérieur passe l'hiver dehors ou dans un abri humide. Ce qu'il faut en retirer au printemps n'est pas de la poussière : c'est un dépôt vivant.",
        "sections": [
            ("Ce qui s'installe pendant l'hiver", [
                "Sur un salon laissé dehors, trois choses se déposent. Un film vert d'algues microscopiques, qui apparaît d'abord sur les faces nord. Des lichens, sur les surfaces rugueuses et poreuses. Et un dépôt gras de pollution atmosphérique, particulièrement marqué en zone urbaine et près des axes routiers.",
                'Sous un abri, le problème est différent mais pas moindre : la condensation sans ventilation favorise les moisissures, surtout sur les textiles et les mousses de coussins.',
                "Aucun de ces dépôts ne part au jet d'eau seul. Ils demandent un produit et un temps d'action, ce qui est exactement l'inverse de ce que l'on fait spontanément avec un nettoyeur haute pression.",
            ]),
            ('Chaque matériau, sa méthode', [
                "<strong>La résine tressée</strong> se nettoie à la brosse souple et au produit neutre. La haute pression casse les brins, et un brin cassé s'effiloche et se propage. C'est le matériau le plus souvent abîmé par excès de zèle.",
                "<strong>Le teck</strong> grise naturellement sous les UV : ce n'est pas de la saleté, c'est la lignine de surface qui évolue. Si le gris vous convient, un lavage doux suffit. Si vous voulez retrouver le miel d'origine, il faut un dégriseur puis un saturateur — deux produits, deux temps.",
                "<strong>L'aluminium laqué</strong> se lave à l'eau savonneuse. Rien d'abrasif : la laque se raye et l'aluminium s'oxyde ensuite par ces micro-rayures.",
                "<strong>Le plastique et le PVC</strong> supportent bien un nettoyage franc, mais un PVC jauni par les UV ne se récupère pas : le matériau a changé, ce n'est plus un encrassement.",
                "<strong>Le fer forgé</strong> demande de surveiller les points de rouille naissante, à traiter avant qu'ils ne s'étendent sous la peinture.",
            ]),
            ("Coussins et textiles d'extérieur", [
                "C'est le poste le plus négligé et celui qui sent le plus mauvais au printemps.",
                'Les housses déhoussables se lavent selon leur étiquette, généralement à basse température, sans sèche-linge : la chaleur détruit les traitements déperlants.',
                "Les coussins non déhoussables relèvent de l'injection-extraction, avec une contrainte forte : la mousse d'extérieur est épaisse et sèche lentement. Il faut extraire beaucoup et sécher à l'air libre, en plein soleil si possible, pendant une journée complète. Un coussin remisé encore humide développe une moisissure interne qui ne se rattrape plus.",
                "Quand l'odeur d'humidité persiste après nettoyage et séchage, un traitement par ozone la traite efficacement — sur mobilier sorti, hors présence de personnes, d'animaux et de plantes, puis aération.",
            ]),
            ('Le bon moment et le regroupement', [
                "Le meilleur moment est le début du printemps, avant la première utilisation, par temps sec et doux. Les produits anti-mousse ont besoin d'humidité pour agir mais pas de pluie battante, et les coussins ont besoin de soleil pour sécher.",
                'Un second passage en fin de saison, avant remisage, prolonge nettement la durée de vie du mobilier — surtout pour les textiles, qui ne devraient jamais être rangés sales ni humides.',
                "Le mobilier se traite naturellement en même temps que la terrasse : même déplacement, même matériel, et la terrasse doit de toute façon être dégagée pour être nettoyée. C'est le regroupement évident.",
            ]),
        ],
        "faq": [
            ('Peut-on nettoyer de la résine tressée au Kärcher ?',
             "Non. La haute pression casse les brins, qui s'effilochent ensuite de proche en proche. Brosse souple et produit neutre uniquement."),
            ("Comment retrouver la couleur d'origine du teck ?",
             "Avec un dégriseur puis un saturateur. Le gris n'est pas de la saleté mais l'évolution naturelle de la lignine sous les UV : un simple lavage ne le retire pas."),
            ("Que faire des coussins d'extérieur ?",
             "Housses déhoussables au lavage selon l'étiquette, sans sèche-linge. Coussins fixes en injection-extraction avec un séchage complet à l'air libre — un coussin remisé humide moisit de l'intérieur."),
        ],
        "service": 'nettoyage-terrasse-paris',
    },
    {
        "slug": 'nettoyage-parking-local-poubelles',
        "cat": 'Copropriété',
        "h1": 'Nettoyage de parking et de local poubelles',
        "title": 'Nettoyage de parking et local poubelles',
        "meta": "Nettoyage de parking souterrain et de local poubelles en copropriété : traces d'huile, odeurs, fréquence, et contraintes d'un espace fermé.",
        "image": 'intervention-3.webp',
        "lead": "Ce sont les deux endroits d'un immeuble dont personne ne parle en assemblée générale, jusqu'au jour où l'odeur remonte dans la cage d'escalier.",
        "sections": [
            ('Le local poubelles : traiter la cause', [
                "L'odeur d'un local poubelles ne vient pas des conteneurs mais du sol et des parois. Les jus qui s'écoulent des sacs pénètrent dans la porosité du béton, y fermentent, et continuent de sentir longtemps après que les conteneurs ont été sortis.",
                "Un lavage de surface ne fait donc rien de durable. Il faut une haute pression avec eau chaude si possible, un dégraissant alcalin sur le sol, un temps de pose, puis un rinçage complet vers l'évacuation.",
                "Les parois se traitent aussi, jusqu'à hauteur d'homme au minimum : les projections montent plus haut qu'on ne l'imagine lors des manipulations de conteneurs.",
                "Quand l'odeur persiste après le lavage — parce qu'elle est descendue dans le béton ou installée dans la ventilation — un traitement par ozone la traite en profondeur. Le local est fermé pendant l'opération, sans présence humaine ni animale, puis ventilé avant réouverture. C'est le seul moyen d'atteindre ce que l'eau ne touche pas.",
            ]),
            ('Le parking souterrain', [
                "Deux problèmes distincts s'y cumulent.",
                "<strong>Les traces d'huile et de carburant.</strong> Elles pénètrent dans le béton et deviennent glissantes quand elles sont humides — c'est un enjeu de sécurité autant que d'aspect. Elles se traitent au dégraissant avec temps de pose, puis à la haute pression. Une tache ancienne ne disparaît jamais totalement : le béton est teinté dans son épaisseur. On retire le gras, pas la coloration.",
                "<strong>La poussière de frein et de pneu.</strong> Un dépôt noirâtre, très fin, qui se dépose partout, y compris sur les murs et les portes de box. Il se lave mais revient : c'est un entretien périodique, pas une opération unique.",
                "S'ajoutent les grilles d'évacuation, à curer, et le marquage au sol, qui s'efface et relève d'une reprise en peinture — pas du nettoyage.",
            ]),
            ("Les contraintes d'un espace fermé", [
                "Un parking souterrain est un volume clos, mal ventilé, où l'on travaille à l'eau et à l'électricité. Cela impose plusieurs précautions.",
                "L'évacuation de l'eau de lavage doit être identifiée avant de commencer. Un parking dont les grilles sont obstruées se transforme en piscine, et l'eau chargée de dégraissant ne doit pas partir n'importe où.",
                "La ventilation conditionne l'usage des produits : un dégraissant alcalin en espace confiné demande une aération active pendant et après l'intervention.",
                "Enfin, l'accès : il faut que les places soient libérées. C'est le point d'organisation le plus délicat en copropriété, et il vaut mieux le traiter par zones successives, avec un affichage plusieurs jours à l'avance, que de tenter de vider tout le parking le même jour.",
            ]),
            ('Fréquence raisonnable', [
                "Le local poubelles gagne à être traité en profondeur deux à quatre fois par an, en plus du passage courant de l'entretien hebdomadaire. En été, la fréquence doit augmenter : la fermentation est bien plus rapide.",
                'Le parking se traite une à deux fois par an. Une fois suffit sur un parking de résidence peu circulé ; deux fois se justifient si des commerces ou des livraisons y accèdent.',
                "Ce sont des prestations ponctuelles, qui ne figurent presque jamais dans un contrat d'entretien courant. Elles se chiffrent séparément, et c'est souvent l'écart entre deux devis d'entretien d'immeuble : l'un les inclut, l'autre non.",
            ]),
        ],
        "faq": [
            ("Une tache d'huile ancienne part-elle du béton ?",
             "Le gras se retire, la coloration non. Le béton est teinté dans son épaisseur : on récupère l'adhérence et l'aspect général, pas la couleur d'origine. Nous le disons avant d'intervenir."),
            ('Comment traiter une odeur de local poubelles ?',
             "En traitant le sol et les parois, pas les conteneurs : les jus ont pénétré le béton. Quand l'odeur persiste après lavage, un traitement par ozone l'atteint en profondeur, local fermé et sans présence, puis ventilé."),
            ('Faut-il vider le parking entièrement ?',
             "Non, et c'est déconseillé. Mieux vaut procéder par zones successives, avec un affichage plusieurs jours à l'avance, que de tenter de libérer toutes les places le même jour."),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
    {
        "slug": 'nettoyage-urgent-7j-7-ile-de-france',
        "cat": 'Bien choisir',
        "h1": 'Nettoyage urgent 7j/7 en Île-de-France',
        "title": 'Nettoyage urgent 7j/7 en Île-de-France',
        "meta": "Besoin d'un nettoyage en urgence en Île-de-France : ce qui se traite vraiment dans la journée, ce qui demande du temps, et comment nous joindre.",
        "image": 'intervention-1.webp',
        "lead": "Certaines situations ne peuvent pas attendre trois jours. D'autres, contrairement à ce qu'on croit, ne gagnent rien à être traitées dans la précipitation. Voici comment distinguer les deux.",
        "sections": [
            ('Ce qui se traite réellement en urgence', [
                'Les situations où intervenir vite change le résultat sont celles où la matière évolue.',
                "<strong>Une tache fraîche sur un textile.</strong> C'est le cas le plus net. Une tache de vin, de café ou d'urine traitée dans les quarante-huit heures s'élimine presque toujours ; la même tache une semaine plus tard peut être définitive. Ici, l'urgence n'est pas du confort, c'est la différence entre réussite et échec.",
                "<strong>Un état des lieux ou une visite le lendemain.</strong> L'échéance est imposée de l'extérieur et ne se négocie pas.",
                "<strong>Une rotation de location courte durée.</strong> Un voyageur arrive à 15 h, il n'y a pas d'autre créneau.",
                '<strong>Une réouverture de commerce.</strong> Chaque jour de fermeture coûte, et le nettoyage ne doit pas être ce qui retarde.',
                "Dans ces cas, appelez-nous plutôt que d'écrire : le téléphone est le seul canal réellement rapide. Nous décrochons sept jours sur sept, de 8 h à 20 h.",
            ]),
            ('Ce qui ne gagne rien à être précipité', [
                "Il faut aussi savoir dire quand l'urgence dessert.",
                '<strong>Un nettoyage de fin de chantier.</strong> Intervenir le jour même du dernier ponçage garantit de devoir repasser : la poussière de plâtre retombe pendant vingt-quatre à quarante-huit heures. Attendre un jour donne un meilleur résultat pour le même prix.',
                "<strong>Un traitement de terrasse.</strong> L'anti-mousse a besoin d'un temps d'action de plusieurs heures à plusieurs jours. Le presser revient à ne pas le faire.",
                "<strong>Un traitement par ozone.</strong> Il impose un local vide pendant l'opération puis une aération avant réoccupation. Ce délai n'est pas négociable : l'ozone est un gaz irritant pour les voies respiratoires, et écourter l'aération serait dangereux.",
                "<strong>Tout ce qui doit sécher.</strong> Un matelas, une moquette, un fauteuil de bureau : le séchage prend le temps qu'il prend. On peut avancer l'intervention, pas raccourcir le séchage.",
            ]),
            ('Nos délais réels', [
                "Nous répondons à toute demande sous vingt-quatre heures, week-ends compris. L'intervention suit généralement sous vingt-quatre à soixante-douze heures selon votre département.",
                "Le délai est le plus court en Seine-Saint-Denis et dans le Val-d'Oise, où se trouve notre atelier de Tremblay-en-France, ainsi qu'à Paris et en proche couronne. Il s'allonge dans les Yvelines, en Seine-et-Marne et en grande couronne sud.",
                'Pour une intervention le jour même, tout dépend de notre planning et de votre commune. Nous vous répondons franchement : soit nous pouvons, soit nous vous le disons tout de suite pour que vous cherchiez ailleurs sans perdre une demi-journée.',
                "Nous intervenons le samedi, le dimanche et les jours fériés au même tarif. Il n'y a pas de majoration de week-end chez nous, parce que les urgences ne choisissent pas leur jour.",
            ]),
            ("Ce qu'il faut nous dire pour aller vite", [
                'Une demande urgente traitée vite est une demande précise. Trois éléments suffisent presque toujours.',
                "Une ou deux photos de ce qu'il faut traiter, prises de près. C'est ce qui nous renseigne le mieux et le plus vite.",
                'Votre adresse exacte, pour que nous calculions immédiatement le déplacement et le délai réel.',
                "Votre échéance : l'heure à laquelle cela doit être fini, pas seulement le jour. Cela conditionne le créneau et parfois la méthode — sur une échéance très courte, nous choisirons une technique qui sèche plus vite quand c'est possible.",
                "Nous vous répondons avec un devis ferme, sans acompte. Vous réglez après l'intervention, y compris en urgence.",
            ]),
        ],
        "faq": [
            ('Intervenez-vous le jour même ?',
             "Parfois, selon notre planning et votre commune. Appelez-nous plutôt que d'utiliser le formulaire : nous vous dirons tout de suite si c'est possible, plutôt que de vous faire perdre une demi-journée."),
            ('Y a-t-il une majoration le week-end ou les jours fériés ?',
             'Non. Le tarif est identique sept jours sur sept. Les urgences ne choisissent pas leur jour.'),
            ('Que faire en attendant sur une tache fraîche ?',
             "Tamponnez avec un chiffon blanc, du bord vers le centre, sans frotter. N'appliquez aucun produit ménager : mal choisi, il peut fixer la tache définitivement ou décolorer le support autour."),
            ('Quel est votre délai habituel ?',
             "Réponse sous vingt-quatre heures, intervention sous vingt-quatre à soixante-douze heures selon le département. Le plus court en Seine-Saint-Denis, dans le Val-d'Oise, à Paris et en proche couronne."),
        ],
        "service": 'nettoyage-entreprise-paris',
    },
]


# Contenu éditorial propre à chaque département, affiché sur les pages de zone.
# Chaque entrée décrit ce qui distingue réellement le terrain : type de bâti,
# demandes dominantes, contraintes d'accès. Rédigé par département pour éviter
# huit pages interchangeables.
ZONES_DETAIL = {
    "75": [
        ("Le bâti parisien impose ses contraintes", [
            "Paris se travaille en étage, sans ascenseur une fois sur deux, avec un stationnement "
            "qui se compte en minutes. Cela conditionne tout : nous venons avec un matériel "
            "transportable à la main, autonome en eau et en électricité, parce qu'un immeuble "
            "haussmannien n'offre ni point d'eau au palier ni prise dans la cage d'escalier.",
            "Les demandes dominantes suivent le bâti. Le textile en premier — canapés d'angle "
            "et matelas qu'on ne peut pas descendre. Les vitres ensuite, sur des fenêtres à "
            "petits carreaux qui se comptent en vantaux et non en fenêtres. Les locaux "
            "professionnels enfin, en horaires décalés, parce qu'un bureau parisien est occupé "
            "de 8 h à 20 h.",
        ]),
        ("Ce qui change d'un arrondissement à l'autre", [
            "Les arrondissements centraux concentrent les commerces et la restauration : "
            "vitrines à entretenir chaque semaine, banquettes en tissu, sols carrelés dont les "
            "joints noircissent. Les arrondissements de l'ouest et du nord-ouest sont davantage "
            "résidentiels, avec des parquets anciens et des textiles de valeur qui demandent "
            "une humidité contrôlée plutôt que de l'eau.",
            "L'est parisien mêle logements récents et locaux reconvertis, où les fins de "
            "chantier sont fréquentes. Nous y intervenons souvent en deux passages, la poussière "
            "de plâtre retombant pendant vingt-quatre à quarante-huit heures.",
        ]),
    ],
    "92": [
        ("Bureaux et résidentiel haut de gamme", [
            "Les Hauts-de-Seine cumulent deux terrains très différents. Au nord et au centre, "
            "les quartiers d'affaires : de grands plateaux, des moquettes de bureau à extraire, "
            "des sièges à reprendre, et une contrainte horaire absolue — on n'intervient pas "
            "pendant les heures ouvrées.",
            "Au sud et sur les communes résidentielles, un habitat plus cossu où les demandes "
            "portent sur les textiles de qualité, les cuirs, les vitrages de grande surface et "
            "les terrasses. C'est là que la distinction entre cuir pigmenté et cuir aniline "
            "prend son importance : le second ne tolère aucun produit aqueux.",
        ]),
        ("Accès et organisation", [
            "Le stationnement en heures ouvrées est le vrai sujet, davantage que la distance. "
            "Nous privilégions les créneaux de début de matinée et de fin de journée, et nous "
            "travaillons volontiers en parking souterrain, où nous sommes autonomes en eau "
            "comme en électricité.",
            "Sur les sites tertiaires, nous groupons ce qui peut l'être : extraction de moquette "
            "et reprise des sièges le même week-end, vitrerie intérieure dans la foulée. Le "
            "déplacement est unique et le coût par poste en profite.",
        ]),
    ],
    "93": [
        ("Notre département d'attache", [
            "Notre atelier est à Tremblay-en-France. La Seine-Saint-Denis est donc le "
            "département où nos délais sont les plus courts et nos frais de déplacement les "
            "plus faibles — parfois nuls sur les communes les plus proches.",
            "C'est aussi le département où nous pouvons le plus souvent caler une intervention "
            "le jour même, et où un second passage sur une fin de chantier ne pose aucune "
            "difficulté d'organisation.",
        ]),
        ("Un terrain d'activité autant que d'habitat", [
            "Le 93 concentre des zones d'activité, des entrepôts, des locaux reconvertis et un "
            "habitat collectif dense. Les demandes s'y répartissent entre l'entretien de locaux "
            "professionnels, les fins de chantier — nombreuses, avec les programmes de "
            "rénovation — et le textile en logement.",
            "Les copropriétés y sont une part importante de notre activité : parties communes, "
            "cages d'escalier, locaux poubelles et parkings souterrains, avec la contrainte "
            "d'un espace fermé où l'évacuation de l'eau de lavage doit être identifiée avant "
            "de commencer.",
        ]),
    ],
    "94": [
        ("Pavillonnaire, collectif et bords de Marne", [
            "Le Val-de-Marne alterne pavillons avec jardin, collectif récent et communes de "
            "bord de Marne. Cette diversité explique la répartition de nos interventions : "
            "beaucoup d'extérieurs — terrasses, dallages, mobilier de jardin — dans le "
            "pavillonnaire, du textile et de la vitrerie dans le collectif.",
            "Les bords de Marne apportent une demande plus rare ailleurs : l'entretien de "
            "bateaux de plaisance, coque, pont et sellerie, y compris hors d'eau pendant "
            "l'hivernage.",
        ]),
        ("Le facteur végétal", [
            "C'est le département où la question de la mousse se pose le plus souvent. Les "
            "terrasses ombragées, sous les arbres et mal drainées, se recolonisent en une "
            "saison. Un décapage seul ne tient pas : il faut un traitement anti-mousse à temps "
            "d'action, et un hydrofuge sur les supports poreux si l'on veut espacer réellement "
            "les passages.",
            "Nous conseillons le printemps ou l'automne, jamais le plein été : sur une dalle "
            "brûlante, le produit sèche avant d'avoir pénétré.",
        ]),
    ],
    "91": [
        ("Grande couronne sud : espace et accès faciles", [
            "L'Essonne offre ce que Paris n'a pas : de la place. Les interventions y sont "
            "matériellement plus simples — on se gare devant, on déploie le matériel, on "
            "travaille sans contrainte de créneau.",
            "Les demandes suivent l'habitat : pavillonnaire dominant, donc beaucoup "
            "d'automobile à domicile, de terrasses, de mobilier de jardin et de vitrages de "
            "grande surface, vérandas comprises.",
        ]),
        ("Grouper, parce que le trajet compte", [
            "L'Essonne est éloignée de notre atelier de Tremblay-en-France. Nous nous y "
            "déplaçons volontiers, mais nous vous conseillons de regrouper : la voiture et la "
            "terrasse, les matelas et le canapé, les vitres et la véranda.",
            "Le déplacement est unique, le matériel est déjà en place, et le coût par "
            "prestation baisse nettement. C'est le conseil le plus utile que nous puissions "
            "donner sur ce département, et il ne va pas dans le sens de notre facturation.",
        ]),
    ],
    "78": [
        ("Un patrimoine qui impose de la prudence", [
            "Les Yvelines concentrent un bâti ancien et des matériaux qui ne pardonnent pas "
            "l'erreur : pierre de taille, pierre tendre, tomettes, parquets anciens, ferronnerie. "
            "La haute pression y fait plus de dégâts qu'ailleurs.",
            "Notre règle sur ce type de support est simple : essai sur une zone discrète avant "
            "toute intervention, pression et distance de buse réglées au cas par cas, et refus "
            "assumé quand le support ne le permet pas. Une pierre creusée par une pression trop "
            "forte ne se rattrape pas.",
        ]),
        ("Vitrages et extérieurs", [
            "Le bâti individuel des Yvelines apporte beaucoup de vitrage : vérandas, baies de "
            "grande dimension, verrières. Nous les traitons à l'eau osmosée depuis le sol, à la "
            "perche, jusqu'à trois niveaux environ — au-delà, il faut une nacelle et ce n'est "
            "plus notre métier.",
            "Les toitures de véranda méritent une attention particulière : personne ne les "
            "regarde, elles s'encrassent progressivement, et la pièce s'assombrit d'année en "
            "année sans qu'on identifie la cause.",
        ]),
    ],
    "77": [
        ("Le département le plus étendu", [
            "La Seine-et-Marne représente à elle seule près de la moitié de la superficie "
            "francilienne. D'un bout à l'autre, les temps de trajet n'ont rien de comparable, "
            "et nos délais varient en conséquence : proches sur l'ouest du département, plus "
            "longs vers l'est et le sud.",
            "Nous intervenons partout, mais nous sommes francs sur le délai plutôt que de "
            "promettre une réactivité que le kilométrage rend impossible.",
        ]),
        ("Pavillonnaire, artisanat et locaux d'activité", [
            "Le terrain mêle habitat individuel avec extérieurs — terrasses, allées, mobilier "
            "de jardin — et un tissu de locaux d'activité et d'entrepôts. Les fins de chantier "
            "y sont fréquentes, portées par la construction neuve.",
            "Comme en Essonne, le conseil qui compte est de grouper. Une venue qui traite la "
            "terrasse, les vitres, le mobilier de jardin et la voiture vaut mieux que quatre "
            "déplacements successifs, pour nous comme pour votre facture.",
        ]),
    ],
    "95": [
        ("Proche de notre atelier", [
            "Le Val-d'Oise jouxte notre atelier de Tremblay-en-France. C'est, avec la "
            "Seine-Saint-Denis, le département où nous intervenons le plus vite et où les "
            "frais de déplacement sont les plus bas.",
            "Sur les communes de l'est du département, nous sommes souvent à moins de quinze "
            "minutes. Cela rend possible ce qui est difficile ailleurs : une intervention le "
            "jour même, ou un retour rapide pour reprendre un point resté en suspens.",
        ]),
        ("Habitat mixte et zones d'activité", [
            "Le 95 alterne collectif dense au sud-est, pavillonnaire au nord et à l'ouest, et "
            "de vastes zones logistiques autour des plateformes aéroportuaires. Les demandes "
            "s'y répartissent entre textile en logement, entretien de locaux professionnels et "
            "remise en état après travaux.",
            "Les copropriétés y sont nombreuses et les prestations ponctuelles fréquentes : "
            "reprise d'une cage d'escalier, local poubelles à traiter à la haute pression, "
            "parking souterrain à dégraisser. Ce sont des postes que les contrats d'entretien "
            "courant ne couvrent presque jamais.",
        ]),
    ],
}
