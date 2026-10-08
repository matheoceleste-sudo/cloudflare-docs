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
    # Reprise de la fiche INSEE (SIREN 924 565 990), pour que le site, la fiche
    # Google et le registre désignent la même adresse.
    "address": "2 rue Poussin",
    "postcode": "93150",
    "city": "Le Blanc-Mesnil",
    # Position de la fiche Google Business, pour que le site et la fiche
    # désignent exactement le même point.
    "lat": 48.9499461,
    "lon": 2.4559529,
    "siret": "924 565 990 00010",
    "siren": "924 565 990",
    "manager": "Mathéo Céleste",
    "hours": "7j/7, de 8h à 20h",
    # Fiche Google Business (CID issu de l'URL Maps fournie par le client).
    "google_cid": "8434710860473546146",
    "maps_url": "https://www.google.com/maps/place/MathClean/@48.9499461,2.4559529,17z",
    # Lien court fourni par Google : il ouvre directement le formulaire
    # d'avis, sans passer par la fiche. C'est celui à mettre sur un flyer,
    # dans une signature ou derrière un QR code.
    "review_url": "https://g.page/r/CaK1p63WHA51EBM/review",
    "directions_url": "https://www.google.com/maps/dir/?api=1&destination=MathClean&destination_place_id=",
    "travel_fee": "5 € par tranche de 5 km depuis notre atelier du Blanc-Mesnil (93)",
    # Règle complète, écrite une seule fois : toute page qui parle du
    # déplacement la reprend telle quelle, pour qu'aucune formulation ne
    # diverge d'une page à l'autre.
    "travel_rule": (
        "La distance comptée est celle de l'aller simple, par la route, entre notre atelier "
        "et votre adresse d'intervention : le retour n'est pas facturé. Toute tranche de "
        "5 km entamée est due — 12 km font donc trois tranches, soit 15 €. Il n'y a pas de "
        "plafond, mais le montant vous est annoncé avant que vous validiez, et il ne bouge "
        "plus ensuite."
    ),
}

# --- Délais ----------------------------------------------------------------
# Deux délais distincts, que le site ne doit jamais confondre : celui de la
# RÉPONSE à une demande, et celui de l'INTERVENTION elle-même. L'audit avait
# relevé trois formulations concurrentes sur le site ; elles viennent
# désormais toutes d'ici.
DELAIS = {
    "reponse": "24 h",
    "proche": "24 à 48 h",
    "loin": "48 à 72 h",
    "depts_proches": ("75", "92", "93", "94"),
}

# --- Prestations ----------------------------------------------------------
# Chaque entrée génère une page dans /services/ et une carte sur l'accueil.
SERVICES = [
    {
        "slug": "nettoyage-hottes-paris",
        "audience": "pro",
        "local": {"court": "Dégraissage hotte", "slug": "degraissage-hotte",
                  "nom": "Dégraissage de hotte", "kw": "dégraissage hotte"},
        "short": "Hottes",
        "nav": "Dégraissage de hottes",
        "name": "Dégraissage de hottes à Paris",
        "h1": "Dégraissage de hotte et de conduits d'extraction",
        "title": "Dégraissage de hotte professionnelle à Paris",
        "meta": "Dégraissage de hotte, filtres et conduits d'extraction pour restaurants et boulangeries à Paris et en IDF. Ramonage annuel exigé par l'arrêté du 25 juin 1980.",
        "price": "sur devis",
        "excerpt": "Hotte, filtres, bac à graisse et conduits d'extraction jusqu'au ventilateur : le circuit complet, dégraissé en une intervention de nuit.",
        "image": "bureau-entreprise.webp",
        "hero": "bureau-entreprise.webp",
        "icon": "tools",
        "intro": [
            "La graisse de cuisson ne reste pas sur la hotte. Elle est aspirée, se condense en remontant dans le conduit, et s'y dépose en une couche "
            "qui s'épaissit chaque service. Cette couche est combustible : c'est elle qui transforme un départ de feu sur un piano en feu de conduit, "
            "lequel se propage dans les gaines à travers les planchers. La plupart des incendies de restaurant ne partent pas de la cuisine, ils y passent.",
            "Le second effet est quotidien et moins spectaculaire : un conduit encrassé perd sa section utile. L'extraction tire moins, les buées restent "
            "en salle, les odeurs s'installent dans les textiles et le personnel travaille dans une cuisine plus chaude. Une extraction qui faiblit "
            "progressivement ne se remarque pas — jusqu'au jour où l'on compare avant et après.",
        ],
        "included_title": "Ce que couvre l'intervention",
        "included": [
            "<strong>Hotte</strong> : intérieur, extérieur, soudures et angles, dégraissage à l'alcalin puis rinçage",
            "<strong>Filtres à chocs ou à cassettes</strong> : démontage, trempage, rinçage haute pression, remontage",
            "<strong>Bac à graisse et gouttières</strong> : vidange et nettoyage complet",
            "<strong>Plafond filtrant</strong> le cas échéant, module par module",
            "<strong>Conduits d'extraction</strong> : gaines accessibles jusqu'au ventilateur, par les trappes de visite",
            "<strong>Ventilateur d'extraction</strong> : turbine et volute dégraissées",
        ],
        "steps": [
            ("Repérage et protection", "Relevé du circuit, repérage des trappes de visite, et bâchage du piano, des plans de travail et des sols. Rien ne doit recevoir de produit ni de dépôt."),
            ("Démontage", "Filtres, gouttières et bac à graisse sont déposés et mis à tremper dans un bain alcalin pendant que le reste est traité."),
            ("Dégraissage alcalin", "Produit à temps de pose sur la hotte et les parois du conduit, puis action mécanique. La graisse polymérisée par la chaleur ne part pas au chiffon : c'est la chimie et le temps qui la décollent, pas la force."),
            ("Conduits et ventilateur", "Progression par les trappes de visite jusqu'au ventilateur, turbine et volute comprises. Les zones sans trappe sont signalées plutôt que contournées en silence."),
            ("Rinçage, remontage, contrôle", "Rinçage complet, remontage, essai de l'extraction, et photos avant/après de chaque zone traitée. Vous notez la date dans votre livret d'entretien."),
        ],
        "faq": [
            ("À quelle fréquence la loi impose-t-elle ce nettoyage ?",
             "Pour un établissement recevant du public, l'article GC 21 de l'arrêté du 25 juin 1980 impose un ramonage des conduits d'évacuation et une vérification de leur vacuité <strong>au moins une fois par an</strong>, et un nettoyage ou remplacement des filtres <strong>au moins une fois par semaine</strong>. Le circuit d'extraction lui-même doit être nettoyé aussi souvent que nécessaire. Un livret d'entretien, annexé au registre de sécurité, consigne les dates."),
            ("Faut-il fermer la cuisine ?",
             "Non. Nous intervenons après le dernier service ou avant l'ouverture, de nuit si besoin, sans supplément. La cuisine est rendue propre et opérationnelle pour le service suivant."),
            ("Combien de temps dure une intervention ?",
             "De trois à huit heures selon la longueur du conduit, l'accessibilité des trappes et l'ancienneté du dépôt. Une première intervention sur une installation jamais traitée prend toujours plus longtemps qu'un passage d'entretien."),
            ("Et s'il n'y a pas de trappe de visite sur le conduit ?",
             "Nous traitons ce qui est accessible et nous vous le disons par écrit, avec les zones non atteintes repérées sur un schéma. La pose de trappes relève d'un installateur : nous ne perçons pas une gaine, et nous ne faisons pas semblant d'avoir nettoyé ce que nous n'avons pas vu."),
            ("Que remettez-vous après l'intervention ?",
             "Un jeu de photos avant/après par zone traitée, et le détail de ce qui a été fait et de ce qui ne l'a pas été. Vous reportez la date dans votre livret d'entretien, qui est le document que vous présentez en cas de contrôle."),
        ],
    },
    {
        "slug": "nettoyage-regulier-paris",
        "audience": "pro",
        "local": {"court": "Nettoyage entreprise", "slug": "menage-regulier",
                  "nom": "Nettoyage d'entreprise", "kw": "nettoyage d'entreprise"},
        "short": "Ménage régulier",
        "nav": "Nettoyage d'entreprise",
        "name": "Nettoyage d'entreprise à Paris",
        "h1": "Nettoyage d'entreprise : bureaux, commerces et locaux",
        "title": "Nettoyage d'entreprise à Paris et en Île-de-France",
        "meta": "Nettoyage d'entreprise à Paris et en Île-de-France : bureaux, commerces, restaurants, parties communes. Passage avant l'ouverture ou après la fermeture.",
        "price": "sur devis",
        "excerpt": "Bureaux, commerces, salles de restaurant et parties communes, en passage quotidien, hebdomadaire ou mensuel, aux horaires qui vous arrangent.",
        "image": "bureau-entreprise.webp",
        "hero": "bureau-entreprise.webp",
        "icon": "building",
        "intro": [
            "Un contrat d'entretien se juge sur une seule donnée : le temps de présence réel par passage. C'est la seule qui remette deux devis sur la "
            "même échelle, et c'est celle que presque personne n'écrit. Nous l'indiquons systématiquement, avec la liste des postes couverts à chaque "
            "fréquence — ce qui est fait tous les jours, ce qui l'est une fois par semaine, ce qui l'est au trimestre.",
            "L'autre point qui fait la différence est la continuité. C'est la même personne qui revient, qui sait où est le local technique, quel sol "
            "ne supporte pas l'autolaveuse et à quelle heure la salle de réunion se libère. Un prestataire qui change d'intervenant chaque mois "
            "recommence son apprentissage à vos frais.",
        ],
        "included_title": "Ce que recouvre un passage",
        "included": [
            "Bureaux, espaces d'accueil et salles de réunion",
            "Sanitaires : désinfection complète et réapprovisionnement des consommables",
            "Sols durs et moquettes, de l'entretien courant à l'injection-extraction périodique",
            "Cuisines, coins repas et distributeurs",
            "Parties communes : halls, cages d'escalier, ascenseurs, locaux poubelles",
            "Vitrerie intérieure, et extérieure jusqu'à trois niveaux",
        ],
        "steps": [
            ("Visite et relevé", "Nous passons sur site, relevons les surfaces, les revêtements et les contraintes d'accès. Un devis au jugé sur plan ne tient jamais."),
            ("Cahier des charges écrit", "Qui fait quoi, à quelle fréquence, en combien de temps. Le document liste aussi ce qui n'est pas inclus, pour qu'il n'y ait pas de discussion au troisième mois."),
            ("Passages réguliers", "Avant l'ouverture, après la fermeture ou le week-end, sans supplément. Même intervenant d'un passage à l'autre."),
            ("Points de contrôle", "Un échange à un mois puis au trimestre pour ajuster les fréquences : certains postes se révèlent inutiles, d'autres méritent un passage de plus."),
        ],
        "faq": [
            ("Faut-il s'engager sur une durée ?",
             "Non. Le passage ponctuel et le contrat régulier existent tous les deux. Un rythme se cale après quelques passages, quand il devient prévisible — pas avant."),
            ("Intervenez-vous hors des heures d'ouverture ?",
             "Oui, avant l'ouverture, après la fermeture ou le week-end, sans supplément. C'est la seule façon de travailler correctement sur un site occupé."),
            ("Comment comparer votre devis à un autre ?",
             "Regardez le temps de présence par passage, pas le prix au mètre carré. Deux devis au même montant peuvent recouvrir une heure ou trois heures de travail, et c'est là que tout se joue."),
        ],
    },
    {
        "slug": "nettoyage-appartement-paris",
        "audience": "particulier",
        "local": {"court": "Nettoyage appartement", "slug": "nettoyage-appartement",
                  "nom": "Nettoyage d'appartement", "kw": "nettoyage appartement"},
        "short": "Appartement",
        "nav": "Nettoyage d'appartement",
        "name": "Nettoyage d'appartement à Paris",
        "h1": "Nettoyage complet d'appartement, de fond en comble",
        "title": "Nettoyage d'appartement à Paris et en IDF",
        "meta": "Nettoyage complet d'appartement à Paris et en Île-de-France : grand ménage, après travaux, avant état des lieux ou entre deux locations. Devis gratuit.",
        "price": "sur devis",
        "excerpt": "Grand ménage de printemps, remise en état avant un état des lieux, ou nettoyage complet entre deux locations : l'appartement entier, pièce par pièce.",
        "image": "intervention-1.webp",
        "hero": "intervention-1.webp",
        "icon": "sofa",
        "intro": [
            "Un nettoyage d'appartement n'est pas un ménage en plus grand. Le ménage courant entretient ce qui est propre ; ici, on reprend ce qui ne "
            "l'a pas été depuis longtemps — le calcaire au pied des robinets, le gras au-dessus des meubles de cuisine, les plinthes, les rails de "
            "fenêtre, l'intérieur des placards. Ce sont des postes qui demandent du temps de pose et de l'huile de coude, pas de la vitesse.",
            "Trois situations reviennent : le grand nettoyage qu'on repousse depuis deux ans, la remise en état avant un état des lieux de sortie — où "
            "chaque poste oublié se paie sur le dépôt de garantie — et le passage entre deux locataires ou deux séjours. Le contenu change dans chaque "
            "cas, et le devis le dit.",
        ],
        "included_title": "Ce que recouvre un nettoyage complet",
        "included": [
            "<strong>Cuisine</strong> : dégraissage des meubles hauts, plan de travail, crédence, électroménager intérieur et extérieur",
            "<strong>Salle de bains</strong> : détartrage des robinetteries, parois de douche, joints, WC",
            "<strong>Sols</strong> : aspiration et lavage adapté au revêtement, plinthes comprises",
            "<strong>Vitres</strong> : intérieur, rails et appuis de fenêtre",
            "<strong>Dépoussiérage complet</strong> : dessus de meubles, luminaires, interrupteurs, portes",
            "<strong>Placards</strong> : intérieur vidé et nettoyé, sur demande",
        ],
        "steps": [
            ("Nous faisons le tour", "Pièce par pièce, pour établir ce qui demande du temps de pose et ce qui relève du courant. C'est ce tour qui fait le devis, pas une surface au mètre carré."),
            ("Du haut vers le bas", "Luminaires et dessus de meubles d'abord, sols en dernier. L'ordre inverse oblige à repasser deux fois, et c'est le temps que paient les devis bâclés."),
            ("Temps de pose là où il en faut", "Calcaire, gras de cuisine et joints ne partent pas au premier passage. Le produit travaille pendant qu'on avance ailleurs."),
            ("Contrôle avec vous", "Tour final ensemble avant notre départ. On reprend ce qui doit l'être sur place, pas après coup."),
        ],
        "faq": [
            ("Faut-il que l'appartement soit vide ?",
             "Non, sauf pour un nettoyage avant état des lieux, où un logement vide permet de traiter les sols et les placards en entier. Sinon, nous travaillons autour des meubles."),
            ("Combien de temps faut-il prévoir ?",
             "Comptez une demi-journée pour un studio ou un deux-pièces en entretien courant, une journée complète pour un trois-pièces jamais repris en profondeur. Nous l'annonçons au devis."),
            ("Faut-il fournir les produits ou le matériel ?",
             "Non. Machines, produits, eau et électricité sont fournis. Vous n'avez rien à préparer."),
            ("Est-ce que cela remplace un ménage régulier ?",
             "Non, c'est l'inverse : un nettoyage complet remet à zéro, un ménage régulier maintient. Après une remise à niveau, un passage courant suffit à tenir le résultat."),
        ],
    },
    {
        "slug": "nettoyage-haute-pression-paris",
        "audience": "mixte",
        "local": {"court": "Haute pression", "slug": "haute-pression",
                  "nom": "Nettoyage haute pression", "kw": "nettoyage haute pression"},
        "short": "Haute pression",
        "nav": "Nettoyage haute pression",
        "name": "Nettoyage haute pression à Paris",
        "h1": "Nettoyage haute pression : terrasses, sols et façades",
        "title": "Nettoyage haute pression à Paris et en IDF",
        "meta": "Nettoyage haute pression de terrasses, allées, cours, parkings et façades à "
                "Paris et en Île-de-France. Eau chaude, pression adaptée au support. Devis au m².",
        "price": "sur devis",
        "excerpt": "Terrasses, allées, cours, parkings et façades accessibles depuis le sol : "
                   "la pression réglée sur le support, jamais l'inverse.",
        "image": "ba-terrasse2-apres.webp",
        "hero": "ba-terrasse2-apres.webp",
        "icon": "deck",
        "intro": [
            "Le nettoyage haute pression est la prestation où l'on fait le plus de dégâts quand "
            "on la croit simple. Ce qui décolle la salissure, ce n'est pas la pression mais le "
            "débit : la pression détache, le débit évacue. Une machine réglée trop fort sur une "
            "pierre tendre ou un bois de terrasse ne nettoie pas mieux — elle creuse la surface, "
            "et le défaut est définitif.",
            "Nous réglons donc la pression sur le support, nous travaillons à l'hydro-brosse "
            "rotative plutôt qu'à la lance sur les grandes surfaces — c'est ce qui évite les "
            "zébrures —, et nous passons à l'eau chaude quand le dépôt est gras. Les supports "
            "que nous ne traitons pas, nous le disons avant le devis.",
        ],
        "included_title": "Ce que nous traitons",
        "included": [
            "Terrasses : dallage, pierre, carrelage, béton, bois et composite",
            "Allées, cours, descentes de garage et escaliers extérieurs",
            "Parkings et sous-sols, à l'eau chaude pour les traces d'hydrocarbures",
            "Quais de livraison, locaux poubelles et abords de bennes",
            "Murs de clôture, murets et façades accessibles depuis le sol",
            "Mobilier de jardin, pergolas et garde-corps",
            "Rejointoiement de sable des dallages après lavage, si nécessaire",
        ],
        "steps": [
            ("Identification du support",
             "Pierre naturelle, béton désactivé, grès cérame, bois, composite ou enrobé : chacun "
             "a sa pression maximale et son produit. C'est ce diagnostic qui décide du reste."),
            ("Essai sur une zone cachée",
             "Avant de traiter la surface entière, un essai dans un angle peu visible. Il montre "
             "le résultat réel et révèle une fragilité que l'œil ne voyait pas."),
            ("Lavage à la pression adaptée",
             "Hydro-brosse rotative sur les grandes surfaces pour un résultat régulier, lance "
             "pour les angles et les bordures. Eau chaude quand le dépôt est gras."),
            ("Rinçage et remise en état",
             "Rinçage complet, évacuation des résidus, et rejointoiement de sable si le lavage "
             "l'a entamé. Nous ne laissons pas un dallage déchaussé."),
        ],
        "faq": [
            ("Le nettoyage haute pression peut-il abîmer ma terrasse ?",
             "Oui, et c'est le risque principal de cette prestation. Une pierre tendre se creuse, "
             "un bois pelucherait si on le prenait à contre-fil, un béton désactivé perd ses "
             "granulats, un enrobé perd son liant. Le dommage est irréversible. C'est pour cela "
             "que nous identifions le support et faisons un essai sur une zone cachée avant de "
             "traiter l'ensemble."),
            ("Les mousses vont-elles revenir ?",
             "Oui. Le lavage retire ce qui est visible, pas ce qui est installé dans la porosité "
             "du support : sur une surface exposée au nord ou à l'ombre, la repousse se voit en "
             "une à deux saisons. Nous le disons plutôt que de laisser croire à un résultat "
             "durable. Les produits de traitement destinés à retarder cette repousse relèvent "
             "d'une réglementation à part, et nous n'en appliquons pas."),
            ("Traitez-vous les toitures ?",
             "Non, dans aucun cas. C'est du travail en hauteur, qui demande des compétences et "
             "des équipements que nous n'avons pas. Et les plaques en fibrociment posées avant "
             "1997 peuvent contenir de l'amiante : le nettoyage haute pression y est à proscrire, "
             "parce qu'il libère des fibres. Nous refusons ces chantiers sans discuter."),
        ],
    },
    {
        "slug": "nettoyage-automobile-paris",
        "audience": "particulier",
        "local": {"court": "Nettoyage voiture", "slug": "nettoyage-voiture", "nom": "Nettoyage de voiture", "kw": "nettoyage voiture"},
        "short": "Automobile",
        "nav": "Nettoyage automobile",
        "name": "Nettoyage automobile à Paris",
        "h1": "Nettoyage automobile à domicile à Paris & en Île-de-France",
        "title": "Nettoyage automobile à Paris — dès 50 €",
        "meta": "Detailing automobile intérieur et extérieur à domicile à Paris et en Île-de-France. Aspiration, shampoing des sièges, vapeur, cuir. Dès 50 €, 7j/7.",
        "price": "dès 50 €",
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
        "chimie": {
            "titre": 'Un produit par matière, choisi sur son pH',
            "lead": "Dans un habitacle, cuir, alcantara, tissu, plastique moussé et vitrage n'appellent ni le même produit ni le même geste. Le pH est ce qui commande le choix.",
            "points": [
            ("Cuir : pH neutre, jamais d'alcalin",
             "Une peau tannée est stabilisée en milieu acide. Un nettoyant alcalin attaque sa finition pigmentée et rigidifie la fibre, qui craquelle ensuite aux points de flexion. Nous restons sur des gammes professionnelles à pH neutre &mdash; <strong>Koch Chemie</strong> et équivalents &mdash; suivies systématiquement d'un lait nourrissant."),
            ('Application au mousseur',
             "Un cuir saturé d'eau gonfle puis se rétracte au séchage, et la finition se micro-fissure. Le mousseur dépose beaucoup de volume et très peu d'eau : le produit travaille en surface, là où est la salissure, sans pénétrer dans la peau."),
            ('Alcalin en localisé sur les taches',
             "Le gras, le sébum et l'alimentaire ne partent pas à l'eau : ils demandent un détachant alcalin, appliqué uniquement sur la tache, avec un temps de pose contrôlé puis une extraction immédiate. Jamais en plein, jamais sans rinçage."),
            ("Textiles de sellerie : on aspire plus qu'on n'injecte",
             "L'injection-extraction traite la fibre en profondeur, mais c'est le taux de reprise qui évite l'auréole. Sur alcantara et sur tissu clair, nous travaillons par petites zones avec une extraction très contrôlée."),
            ('Plastiques et écrans : neutre et sans solvant',
             "Les plastiques moussés du tableau de bord et les écrans tactiles portent des traitements de surface qu'un produit alcalin ou solvanté ternit définitivement. Nettoyant neutre, microfibre, aucun rinçage à l'eau à proximité de l'électronique."),
            ('Vapeur quand elle suffit',
             "Sur les plastiques durs, les seuils, les grilles d'aération et les joints, la vapeur haute température décolle le gras par la chaleur et assainit sans laisser le moindre résidu. Quand elle fait le travail, nous n'ajoutons pas de chimie."),
        ],
        },
        "faq": [
            ("Combien de temps dure un nettoyage automobile ?",
             "Comptez 1 h 30 pour un Extérieur Éclat ou un Intérieur Essentiel, 3 h pour un Intérieur Prestige et jusqu'à 4 h pour un Intégral sur un grand véhicule. Les durées exactes figurent sur notre page tarifs."),
            ("Avez-vous besoin d'une prise électrique ou d'un point d'eau ?",
             "Non. Nous venons entièrement autonomes en eau et en électricité, ce qui nous permet d'intervenir en parking souterrain, en pied d'immeuble ou sur un parking d'entreprise."),
            ("Faites-vous le nettoyage avant une revente ?",
             "C'est une de nos demandes les plus fréquentes. Le pack Intérieur Prestige, associé à l'option de neutralisation des odeurs par ozone, permet de présenter un véhicule sans odeur d'animal ni de tabac — un point qui pèse lourd à la revente."),
            ("Le prix dépend-il de la taille du véhicule ?",
             "Non. Chaque pack est à prix fixe, citadine comme SUV : le montant affiché est celui que vous réglez. Seules les options que vous ajoutez et les frais de déplacement s'ajoutent, et ils vous sont annoncés avant validation."),
        ],
    },
    {
        "slug": "nettoyage-textile-paris",
        "audience": "particulier",
        "local": {"court": "Nettoyage canapé", "slug": "nettoyage-canape", "nom": "Nettoyage de canapé", "kw": "nettoyage canapé"},
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
            ("Désinfection haute température", "Passage à la vapeur sur toute la surface : la chaleur seule assainit et traite les acariens, sans produit. La laine et la soie font exception — la vapeur les rétracte."),
            ("Produit adapté à la matière", "Tissu, microfibre, alcantara ou cuir n'appellent pas le même produit. Nous identifions la matière, testons la solidité des couleurs sur une zone cachée, puis appliquons."),
            ("Brossage", "Le produit est travaillé dans la fibre à la brosse. C'est ce passage qui décolle la saleté au lieu de la laisser remonter en surface."),
            ("Injection-extraction", "La solution est injectée au cœur de la fibre puis réaspirée aussitôt avec la saleté dissoute. Passages croisés jusqu'à ce que l'eau ressorte claire ; sur les matelas, les deux faces."),
            ("Repassage si nécessaire", "Tous les tissus ne le demandent pas. Quand c'est le cas, c'est le geste qui finit le travail. Le textile est réutilisable après 4 à 6 h."),
        ],
        "chimie": {
            "titre": 'La fibre décide du produit',
            "lead": "Coton, synthétique, laine, soie, viscose ou cuir : chaque fibre a une plage de pH qu'elle tolère. En sortir laisse une marque que le nettoyage suivant ne rattrapera pas.",
            "points": [
            ('Synthétiques et coton : alcalinité modérée',
             "Polyester, polypropylène, nylon, coton et lin supportent un détergent faiblement alcalin sans difficulté. C'est le cas le plus fréquent, et celui où l'injection-extraction donne son plein rendement."),
            ('Laine et soie : neutre ou légèrement acide',
             "Ce sont des fibres protéiniques. Au-delà de pH 8, la laine ternit et se feutre, la soie perd son brillant de façon définitive. Nous les traitons en neutre, à l'eau tiède, et jamais à la vapeur qui les rétracte."),
            ('Détachage alcalin, puis neutralisation',
             "Gras, sang, alimentaire : ces salissures organiques demandent un alcalin en application localisée. L'extraction finale se fait avec une solution légèrement acide qui neutralise le résidu &mdash; sans quoi la fibre jaunit et refixe la poussière."),
            ('Cuir : nettoyant neutre puis nourrissant',
             "Sur un canapé en cuir, le protocole est celui de l'automobile : produit à pH neutre appliqué au mousseur, brosse souple, reprise à la microfibre, puis nourrissage. L'injection-extraction est réservée aux textiles."),
            ("Zéro résidu, c'est la règle",
             "Un shampoing de surface laisse son tensioactif dans la fibre : il devient collant, capte la poussière et le textile se resalit plus vite qu'avant. L'extraction se poursuit jusqu'à ce que l'eau reprise ressorte claire."),
            ('Produits biodégradables, et sans danger à sec',
             "Nous privilégions des produits biodégradables et sûrs pour les enfants et les animaux une fois le textile sec. Un produit biodégradable n'est pas pour autant inoffensif pour votre matière : c'est le pH, pas l'étiquette, qui garantit qu'il convient."),
        ],
        },
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
        "slug": "nettoyage-vitres-paris",
        "audience": "mixte",
        "local": {"court": "Nettoyage vitres", "slug": "nettoyage-vitres", "nom": "Nettoyage de vitres", "kw": "nettoyage vitres"},
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
]

# --- Tarifs ---------------------------------------------------------------
PACKS_AUTO = [
    ("Extérieur Éclat", 50, "Extérieur", "La carrosserie retrouve sa brillance", False,
     ["Lavage complet de la carrosserie", "Jantes et passages de roues", "Brillant pneus",
      "Vitres extérieures", "Séchage sans trace"]),
    ("Intérieur Essentiel", 55, "Intérieur", "Idéal pour un coup de propre régulier (hors cuir et alcantara)", False,
     ["Aspiration de l'habitacle et du coffre", "Nettoyage du tableau de bord", "Nettoyage des plastiques",
      "Vitres intérieures", "Désinfection complète à la vapeur", "Parfum d'ambiance"]),
    ("Intérieur Prestige", 100, "Intérieur", "Le détail poussé jusqu'au moindre recoin, cuir compris", True,
     ["Tout l'Intérieur Essentiel", "Sièges cuir nettoyés ou pressing des sièges tissu",
      "Pressing des tapis et moquettes", "Protection des plastiques", "Traitement des cuirs",
      "Battements de portes", "Ciel de toit", "Compartiment de la roue de secours"]),
    ("Intégral", 130, "Intérieur + Extérieur", "Le véhicule entier, dedans comme dehors", False,
     ["Tout l'Intérieur Prestige", "Lavage complet de la carrosserie", "Jantes et brillant pneus",
      "Vitres intérieures et extérieures", "Séchage sans trace", "Parfum d'ambiance"]),
]

OPTIONS_AUTO = [
    ("Retrait des poils d'animaux", 10, "Sièges, tapis et moquettes"),
    ("Traitement cuir & alcantara", 20, "Nettoyage puis nourrissage des cuirs et de l'alcantara"),
    ("Neutralisation des odeurs par ozone", 30, "Traitement d'1 h : les molécules odorantes sont détruites, pas masquées"),
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
    ("Nettoyage de vitres", "Vitres, baies vitrées et vitrines", "nettoyage-vitres-paris"),
    ("Nettoyage pour entreprise", "Bureaux, commerces, locaux et vitrerie", "nettoyage-regulier-paris"),
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
        "intro": "C'est notre département : notre atelier se trouve au Blanc-Mesnil. De Saint-Denis à "
                 "Montreuil, d'Aubervilliers à Noisy-le-Grand, nous y sommes les plus réactifs — et les frais "
                 "de déplacement y sont, mécaniquement, les plus faibles.",
        "focus": "Le 93 est un territoire en pleine transformation, avec de nombreux programmes immobiliers "
                 "neufs, bureaux et ateliers : l'entretien de locaux professionnels et la vitrerie de "
                 "façade y pèsent lourd. À domicile, l'injection-extraction sur canapés, matelas et tapis "
                 "et le detailing automobile constituent l'essentiel des demandes.",
        "cities": ["Saint-Denis", "Montreuil", "Aubervilliers", "Aulnay-sous-Bois", "Drancy",
                   "Noisy-le-Grand", "Bobigny", "Bondy", "Le Blanc-Mesnil", "Pantin",
                   "Rosny-sous-Bois", "Épinay-sur-Seine", "Tremblay-en-France"],
    },
    {
        "slug": "val-de-marne-94", "num": "94", "name": "Val-de-Marne",
        "intro": "De Créteil à Vincennes, de Vitry-sur-Seine à Saint-Maur-des-Fossés, nous intervenons dans "
                 "tout le Val-de-Marne, chez les particuliers comme dans les locaux professionnels.",
        "focus": "Les pavillons de Saint-Maur, Nogent et Le Perreux sollicitent surtout le textile — "
                 "canapés d'angle et tapis — et les grandes surfaces vitrées côté jardin, souvent "
                 "difficiles à atteindre sans perche.",
        "cities": ["Créteil", "Vitry-sur-Seine", "Champigny-sur-Marne", "Saint-Maur-des-Fossés",
                   "Ivry-sur-Seine", "Villejuif", "Vincennes", "Maisons-Alfort",
                   "Fontenay-sous-Bois", "Nogent-sur-Marne", "Charenton-le-Pont", "Le Perreux-sur-Marne"],
    },
    {
        "slug": "essonne-91", "num": "91", "name": "Essonne",
        "intro": "D'Évry-Courcouronnes à Massy, de Palaiseau à Corbeil-Essonnes, nous nous déplaçons dans "
                 "tout le département. Les délais y sont généralement de 48 à 72 h.",
        "focus": "L'habitat pavillonnaire de l'Essonne fait la part belle au detailing automobile à "
                 "domicile — souvent avant une revente — et au nettoyage des baies et vérandas, que la "
                 "poussière des axes routiers marque vite.",
        "cities": ["Évry-Courcouronnes", "Massy", "Savigny-sur-Orge", "Sainte-Geneviève-des-Bois",
                   "Athis-Mons", "Palaiseau", "Viry-Châtillon", "Corbeil-Essonnes", "Draveil",
                   "Yerres", "Brunoy", "Montgeron"],
    },
    {
        "slug": "yvelines-78", "num": "78", "name": "Yvelines",
        "intro": "De Versailles à Mantes-la-Jolie, de Saint-Germain-en-Laye à Montigny-le-Bretonneux, nous "
                 "couvrons les Yvelines pour les particuliers et les entreprises.",
        "focus": "Les Yvelines nous sollicitent particulièrement pour le textile de belle facture — tapis "
                 "de laine, selleries cuir — les grands vitrages des maisons anciennes, et l'entretien de "
                 "locaux professionnels sur les pôles de Saint-Quentin-en-Yvelines.",
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
                 "de déplacement. Le textile, l'automobile à domicile et la vitrerie y dominent.",
        "cities": ["Chelles", "Meaux", "Melun", "Pontault-Combault", "Champs-sur-Marne", "Torcy",
                   "Bussy-Saint-Georges", "Lagny-sur-Marne", "Roissy-en-Brie", "Ozoir-la-Ferrière",
                   "Fontainebleau", "Provins"],
    },
    {
        "slug": "val-doise-95", "num": "95", "name": "Val-d'Oise",
        "intro": "D'Argenteuil à Cergy, de Sarcelles à Pontoise, le Val-d'Oise fait partie de notre zone "
                 "proche : notre atelier du Blanc-Mesnil n'en est séparé que par quelques kilomètres.",
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
    ('ba-terrasse2-avant.webp', 'ba-terrasse2-apres.webp', 'Terrasse en pierre',
     'Lavage haute pression, hydro-brosse rotative'),
    # Les trois premières sont en haute définition (700 px et plus) : ce sont
    # celles que l'accueil affiche. Les trois suivantes sont d'anciennes
    # miniatures (192 px) — elles restent visibles sur la page Réalisations,
    # dans une grille plus étroite, en attendant des clichés de meilleure
    # définition. Voir la note « Photos à remplacer » du README.
    # Les avant/après de terrasse ont été retirés avec la prestation : montrer
    # un résultat que nous ne vendons plus appelle des demandes que nous
    # refusons.
    ('avant-voiture-siege.webp', 'apres-voiture-siege.webp', 'Siège automobile', 'Shampoing et détachage des tissus'),
    ('avant-frigo.webp', 'apres-frigo.webp', 'Réfrigérateur professionnel', 'Nettoyage complet, hygiène alimentaire'),
    ('avant-plan-travail.webp', 'apres-plan-travail.webp', 'Plan de travail', 'Dégraissage et désinfection en profondeur'),
    ('ba-canape-avant.webp', 'ba-canape-apres.webp', 'Canapé en tissu', 'Injection-extraction et désinfection'),
    ('ba-tapis-avant.webp', 'ba-tapis-apres.webp', 'Tapis et moquette', 'Shampoing et détachage en profondeur'),
    ('ba-fauteuil-avant.webp', 'ba-fauteuil-apres.webp', 'Fauteuil de bureau', 'Détachage et assainissement des tissus'),
]

# Nombre de paires en haute définition, affichées en grand.
BEFORE_AFTER_HD = 3

# --- FAQ générale ---------------------------------------------------------
FAQ = [
    ("Combien coûte un nettoyage automobile ?",
     "Quatre packs à prix fixe : Extérieur Éclat 50 €, Intérieur Essentiel 55 €, Intérieur Prestige 100 € et "
     "Intégral 130 €, quelle que soit la taille du véhicule. Le détail de chaque pack et des options figure sur "
     "notre page tarifs."),
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
     "Non, ils s'ajoutent au prix de la prestation : 5 € par tranche de 5 km entre notre atelier "
     "du Blanc-Mesnil (93) et votre adresse. La distance comptée est celle de l'aller simple, par "
     "la route ; le retour n'est pas facturé. Toute tranche de 5 km entamée est due : 12 km font "
     "trois tranches, soit 15 €. Il n'y a pas de plafond, mais le montant vous est annoncé avant "
     "que vous validiez et il ne bouge plus ensuite."),
    ("Utilisez-vous des produits écologiques ?",
     "Nous privilégions des produits respectueux de l'environnement et de votre santé, sans danger pour les "
     "enfants ni les animaux. La vapeur haute température nous permet en outre de désinfecter de nombreuses "
     "surfaces sans aucun produit chimique."),
    ("Faut-il verser un acompte ?",
     "Non. Vous réglez après l'intervention, une fois le résultat constaté avec vous. Nous acceptons les "
     "espèces, la carte bancaire et le virement."),
    ("Intervenez-vous pour les professionnels ?",
     "Oui : bureaux, locaux commerciaux, restaurants et commerces, en passage ponctuel ou régulier, avec "
     "facturation entreprise. Vitrines et façades vitrées comprises, avant l'ouverture ou après la "
     "fermeture pour ne pas gêner votre activité."),
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
        "hors_offre": "le nettoyage de bateau",
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
        "service": "nettoyage-automobile-paris",
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
        "service": "nettoyage-haute-pression-paris",
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
    "lat": 48.9499461,       # atelier du Blanc-Mesnil (position de la fiche Google)
    "lon": 2.4559529,
    "palier_km": 5,          # tranche facturée
    "palier_eur": 5,         # montant par tranche

    # Distance routière réelle, calculée par le service d'itinéraire de
    # l'IGN (Géoplateforme) : gratuit, sans clé, couverture française.
    # `start` et `end` se passent en « longitude,latitude », dans cet ordre.
    # L'itinéraire demandé est le plus rapide, celui que l'on emprunte
    # vraiment — autoroute comprise — et non le plus court sur la carte.
    "routage": {
        "url": "https://data.geopf.fr/navigation/itineraire",
        "params": "resource=bdtopo-osrm&profile=car&optimization=fastest"
                  "&geometryFormat=geojson&getSteps=false",
    },

    # Repli si le service d'itinéraire ne répond pas : vol d'oiseau majoré.
    # Le configurateur dit alors explicitement qu'il s'agit d'une estimation,
    # et le récapitulatif envoyé le précise aussi.
    "coef_route": 1.25,
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
# du Blanc-Mesnil. Les coordonnées sont celles du centre communal : la
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
     ["nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("neuilly-sur-seine", "Neuilly-sur-Seine", "92200", "92", 48.8846, 2.2697,
     "À Neuilly, l'essentiel de nos interventions concerne des selleries cuir, des tapis de "
     "laine et des moquettes de belle facture — des matières qui ne pardonnent pas l'erreur de "
     "produit. Le diagnostic de la fibre y compte davantage qu'ailleurs.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris", "nettoyage-regulier-paris"]),

    ("levallois-perret", "Levallois-Perret", "92300", "92", 48.8939, 2.2874,
     "Levallois concentre bureaux et logements sur un territoire très compact. Le stationnement "
     "y étant difficile, notre autonomie en eau et en électricité change tout : nous intervenons "
     "en parking souterrain, sans avoir à tirer un tuyau depuis la rue.",
     ["nettoyage-regulier-paris", "nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris"]),

    ("nanterre", "Nanterre", "92000", "92", 48.8924, 2.2069,
     "Entre la préfecture, les campus et la proximité immédiate de La Défense, Nanterre nous "
     "sollicite surtout pour l'entretien de locaux professionnels et la remise en état après "
     "travaux, deux prestations qui se planifient hors des heures d'activité.",
     ["nettoyage-regulier-paris", "nettoyage-vitres-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris"]),

    ("issy-les-moulineaux", "Issy-les-Moulineaux", "92130", "92", 48.8239, 2.2730,
     "Pôle tertiaire dense, Issy-les-Moulineaux nous appelle principalement pour la vitrerie de "
     "grandes surfaces et l'entretien de moquettes de bureaux. L'eau osmosée y prend tout son "
     "sens sur les façades vitrées.",
     ["nettoyage-vitres-paris", "nettoyage-regulier-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris"]),

    ("saint-denis", "Saint-Denis", "93200", "93", 48.9362, 2.3574,
     "Saint-Denis est en chantier permanent : programmes neufs, réhabilitations, bureaux livrés "
     "en continu. L'entretien de locaux et la vitrerie de façade y représentent une part "
     "importante de l'activité, le plus souvent en passage régulier.",
     ["nettoyage-regulier-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("montreuil", "Montreuil", "93100", "93", 48.8638, 2.4485,
     "Montreuil alterne pavillons, lofts d'anciens ateliers et immeubles récents. Les grands "
     "volumes reconvertis y posent une question précise : des moquettes et des textiles en "
     "quantité, dans des espaces qu'on ne peut pas vider.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris", "nettoyage-regulier-paris"]),

    ("aulnay-sous-bois", "Aulnay-sous-Bois", "93600", "93", 48.9386, 2.4938,
     "Aulnay est à quelques minutes de notre atelier : c'est l'une des communes où nous "
     "intervenons le plus rapidement, souvent dans la journée en cas d'urgence. L'habitat "
     "pavillonnaire y appelle surtout du textile et du detailing automobile à domicile.",
     ["nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-vitres-paris"]),

    ("le-blanc-mesnil", "Le Blanc-Mesnil", "93150", "93", 48.9386, 2.4644,
     "C'est notre commune : l'atelier s'y trouve. Les frais de déplacement y sont nuls ou "
     "symboliques, et nous pouvons intervenir dans des délais que nous ne tenons nulle part "
     "ailleurs — souvent le jour même.",
     ["nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-vitres-paris"]),

    ("tremblay-en-france", "Tremblay-en-France", "93290", "93", 48.9486, 2.5697,
     "Tremblay-en-France est à une quinzaine de minutes de notre atelier du Blanc-Mesnil, par "
     "l'A104 ou la N2. Pavillons, résidences récentes et zones d'activité proches de Roissy : "
     "les demandes y vont du detailing automobile au nettoyage de locaux.",
     ["nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-regulier-paris"]),

    ("pantin", "Pantin", "93500", "93", 48.8944, 2.4090,
     "Pantin s'est couverte de bureaux et d'ateliers reconvertis le long du canal. Nous y "
     "traitons beaucoup de locaux professionnels, avec la contrainte habituelle des sites "
     "occupés : intervenir tôt le matin ou après la fermeture.",
     ["nettoyage-regulier-paris", "nettoyage-vitres-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris"]),

    ("creteil", "Créteil", "94000", "94", 48.7904, 2.4556,
     "Préfecture du Val-de-Marne, Créteil combine grands ensembles, zones d'activité et "
     "équipements publics. Les demandes y sont partagées entre entretien de locaux et textile "
     "à domicile.",
     ["nettoyage-regulier-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris"]),

    ("vincennes", "Vincennes", "94300", "94", 48.8478, 2.4390,
     "Vincennes est un tissu résidentiel serré, aux appartements souvent anciens. Canapés, "
     "matelas et tapis y constituent l'essentiel des interventions, avec la contrainte "
     "récurrente des escaliers étroits — qui ne nous gêne pas, puisque nous travaillons sur place.",
     ["nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris", "nettoyage-regulier-paris"]),

    ("saint-maur-des-fosses", "Saint-Maur-des-Fossés", "94100", "94", 48.7994, 2.4934,
     "Dans la boucle de la Marne, Saint-Maur aligne pavillons avec jardin, vérandas et grandes "
     "baies côté sud. Le nettoyage des vitrages y suit les saisons, et le textile d'intérieur "
     "occupe le reste de l'année.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris", "nettoyage-regulier-paris"]),

    ("massy", "Massy", "91300", "91", 48.7262, 2.2825,
     "Massy conjugue quartiers d'affaires, gares et logements neufs. Nous y intervenons pour "
     "l'entretien de bureaux et la remise en état après travaux, les livraisons de programmes "
     "y étant fréquentes.",
     ["nettoyage-regulier-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("evry-courcouronnes", "Évry-Courcouronnes", "91000", "91", 48.6238, 2.4297,
     "Évry-Courcouronnes est l'un des points les plus éloignés de notre atelier : nous y "
     "groupons volontiers plusieurs interventions sur une même journée, ce qui reste le meilleur "
     "moyen de contenir les frais de déplacement.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-regulier-paris", "nettoyage-vitres-paris"]),

    ("versailles", "Versailles", "78000", "78", 48.8014, 2.1301,
     "À Versailles, nous traitons beaucoup de matières nobles — tapis de laine, selleries cuir — "
     "et de grands vitrages anciens. Sur ces supports, la question n'est jamais la puissance "
     "mais le réglage.",
     ["nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris", "nettoyage-regulier-paris"]),

    ("saint-germain-en-laye", "Saint-Germain-en-Laye", "78100", "78", 48.8987, 2.0940,
     "Maisons anciennes, grandes fenêtres à petits bois et vérandas : Saint-Germain-en-Laye "
     "appelle surtout de la vitrerie au printemps et du textile de valeur le reste de l'année.",
     ["nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris", "nettoyage-regulier-paris"]),

    ("chelles", "Chelles", "77500", "77", 48.8797, 2.5928,
     "Chelles est l'une des communes de Seine-et-Marne les plus proches de notre atelier, à "
     "quelques minutes seulement. Habitat pavillonnaire dominant : automobile à domicile, "
     "textile et grandes surfaces vitrées.",
     ["nettoyage-automobile-paris", "nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-vitres-paris"]),

    ("meaux", "Meaux", "77100", "77", 48.9601, 2.8785,
     "Meaux marque la limite est de notre zone habituelle. Nous y intervenons volontiers, en "
     "planifiant la journée autour du déplacement — plusieurs prestations groupées plutôt qu'un "
     "aller-retour pour une seule.",
     ["nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris"]),

    ("argenteuil", "Argenteuil", "95100", "95", 48.9474, 2.2467,
     "Argenteuil est la plus peuplée du Val-d'Oise, avec un habitat très varié. Textile à "
     "domicile et detailing automobile y constituent l'essentiel de nos passages.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris", "nettoyage-regulier-paris"]),

    ("cergy", "Cergy", "95000", "95", 49.0361, 2.0631,
     "Ville nouvelle et pôle universitaire, Cergy nous sollicite pour des locaux professionnels "
     "et des logements étudiants en remise en état, souvent entre deux occupations.",
     ["nettoyage-regulier-paris", "nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("sarcelles", "Sarcelles", "95200", "95", 48.9959, 2.3785,
     "Sarcelles est proche de notre atelier, ce qui maintient les frais de déplacement bas. "
     "Nous y intervenons surtout en textile à domicile et en entretien de commerces.",
     ["nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris"]),

    ("paris-8", "Paris 8e", "75008", "75", 48.8721, 2.3120,
     "Le 8e concentre sièges sociaux, hôtels et commerces de luxe. Vitrines, selleries cuir et "
     "moquettes de bureaux y forment le gros de nos interventions, presque toujours en horaires "
     "décalés pour ne pas gêner l'activité.",
     ["nettoyage-vitres-paris", "nettoyage-regulier-paris", "nettoyage-textile-paris", "nettoyage-automobile-paris"]),

    ("paris-11", "Paris 11e", "75011", "75", 48.8580, 2.3792,
     "Le 11e est un arrondissement dense, très résidentiel et très restauré. Nous y traitons "
     "beaucoup de canapés et de matelas en appartement, et des cuisines professionnelles en "
     "intervention nocturne.",
     ["nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris"]),

    ("paris-12", "Paris 12e", "75012", "75", 48.8409, 2.3876,
     "Entre Bercy, la Bastille et le bois de Vincennes, le 12e alterne immeubles récents et "
     "bâti ancien. Textile à domicile et entretien de locaux s'y partagent nos passages.",
     ["nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris"]),

    ("paris-15", "Paris 15e", "75015", "75", 48.8412, 2.3003,
     "Le 15e est le plus peuplé des arrondissements parisiens. Grands appartements familiaux, "
     "donc grands canapés et moquettes : c'est l'arrondissement où l'injection-extraction à "
     "domicile prend le plus de sens.",
     ["nettoyage-textile-paris", "nettoyage-vitres-paris", "nettoyage-automobile-paris", "nettoyage-regulier-paris"]),

    ("paris-16", "Paris 16e", "75016", "75", 48.8637, 2.2769,
     "Le 16e nous amène des matières exigeantes : tapis d'Orient, parquets anciens, selleries "
     "cuir. Le test de solidité des couleurs y est systématique avant tout lavage.",
     ["nettoyage-textile-paris", "nettoyage-automobile-paris", "nettoyage-vitres-paris", "nettoyage-regulier-paris"]),

    ("paris-17", "Paris 17e", "75017", "75", 48.8872, 2.3220,
     "Des Batignolles à la plaine Monceau, le 17e mêle résidentiel haussmannien et bureaux "
     "récents. Vitrerie, textile et entretien de locaux s'y répartissent assez également.",
     ["nettoyage-vitres-paris", "nettoyage-textile-paris", "nettoyage-regulier-paris", "nettoyage-automobile-paris"]),
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
   "Cela dépend entièrement de la prestation. À titre de repère : un canapé 2 places se traite à partir de 39 €, un detailing automobile à partir de 50 €, un traitement à l'ozone à 4 € le m², et les prestations professionnelles se chiffrent sur devis après visite. Un prix annoncé sans connaître le besoin n'a aucune valeur."),
  ("Faut-il choisir une grande entreprise ou un indépendant ?",
   "La taille ne dit rien de la qualité. Ce qui compte, c'est de savoir qui intervient réellement chez vous, avec quel matériel, et qui est responsable en cas de problème. Une structure petite mais directe apporte souvent plus de continuité qu'une chaîne de sous-traitance."),
  ("Les frais de déplacement sont-ils négociables ?",
   "Rarement dans leur principe, mais on peut souvent les réduire en groupant plusieurs prestations sur une même intervention : le déplacement n'est alors facturé qu'une fois.")],
 "service": "nettoyage-regulier-paris",
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
 "video": 'vitres',
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
   "Pas nécessairement. Le passage ponctuel a du sens pour une remise à niveau, un contrôle d'hygiène ou une ouverture. Le contrat régulier se justifie dès que la fréquence devient prévisible."),
  ("Qui fournit les consommables ?",
   "Cela se décide au contrat. Papier, savon et sacs peuvent être fournis par le prestataire ou par l'entreprise : l'essentiel est que ce soit écrit."),
  ("Comment est facturée une prestation professionnelle ?",
   "Sur devis, après visite des locaux et mesure des surfaces, avec facturation entreprise. Un prix au mètre carré annoncé sans visite est un prix approximatif.")],
 "service": "nettoyage-regulier-paris",
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
   "S'y ajoutent les frais de déplacement : 5 € par tranche de 5 km depuis notre atelier du Blanc-Mesnil. Ils sont annoncés avant que vous validiez, jamais découverts à l'arrivée."]),
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
 "meta": "Tarifs du detailing automobile à domicile en Île-de-France : 4 formules à prix fixe, de 50 à 130 €. Options, durée et ce qui est inclus.",
 "image": "auto-interieur-vw.webp",
 "lead": "Quatre formules à prix fixe, de la carrosserie seule au véhicule entier. Le même montant pour une citadine et pour un SUV : ce qui change le prix, c'est le contenu de la formule, pas la taille du véhicule.",
 "sections": [
  ("Les quatre formules", [
   "Extérieur Éclat, 50 € : lavage complet, jantes, brillant pneus, vitres extérieures, séchage sans trace. Intérieur Essentiel, 55 € : aspiration habitacle et coffre, tableau de bord, plastiques, vitres, désinfection vapeur.",
   "Intérieur Prestige, 100 € : tout l'Essentiel, plus le traitement des cuirs ou le pressing des sièges tissu, les tapis, le ciel de toit, les battements de portes. Intégral, 130 € : le véhicule entier, dedans comme dehors."]),
  ("Un prix fixe, quelle que soit la voiture", [
   "Nous avons renoncé aux fourchettes. Une citadine et un SUV ne demandent pas exactement le même temps, mais l'écart ne justifie pas de laisser un client dans le flou jusqu'à l'intervention : le montant affiché est celui que vous réglez.",
   "Seules deux choses s'ajoutent, et elles sont connues d'avance : les options que vous choisissez et les frais de déplacement, calculés sur votre adresse et annoncés avant que vous validiez."]),
  ("Les options", [
   "Retrait des poils d'animaux : 10 €. Traitement cuir et alcantara : 20 €. Neutralisation des odeurs par ozone : 30 €, pour un traitement d'une heure qui détruit les molécules odorantes au lieu de les masquer.",
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
 "hors_offre": "le traitement par ozone d'un local ou d'un logement",
 "hors_offre_note": "ozone",
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
 "service": "nettoyage-regulier-paris",
},
{
 "slug": "traitement-ozone-ile-de-france",
 "hors_offre": "le traitement par ozone d'un local ou d'un logement",
 "hors_offre_note": "ozone",
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
   "Comptez 24 à 48 h à Paris et en petite couronne, 48 à 72 h en grande couronne. Les frais de déplacement suivent la règle habituelle : 5 € par tranche de 5 km depuis notre atelier du Blanc-Mesnil, annoncés avant validation.",
   "Le détail commune par commune figure sur nos pages villes."])],
 "faq": [
  ("Intervenez-vous dans toute l'Île-de-France ?",
   "Oui, dans les huit départements : Paris (75), Hauts-de-Seine (92), Seine-Saint-Denis (93), Val-de-Marne (94), Essonne (91), Yvelines (78), Seine-et-Marne (77) et Val-d'Oise (95)."),
  ("Peut-on traiter un logement occupé ?",
   "Pas pendant le traitement. Le logement doit être vide de ses occupants, de leurs animaux et de leurs plantes, et le rester jusqu'à la fin de l'aération."),
  ("Combien de temps faut-il prévoir en tout ?",
   "Pour un véhicule, une demi-journée en comptant l'aération. Pour un logement, cela se planifie selon le volume : nous vous le disons précisément au devis.")],
 "service": "nettoyage-automobile-paris",
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
 "service": "nettoyage-automobile-paris",
},
{
 "slug": "traitement-ozone-securite",
 "hors_offre": "le traitement par ozone d'un local ou d'un logement",
 "hors_offre_note": "ozone",
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
 "service": "nettoyage-automobile-paris",
},
{
 "slug": "prix-traitement-ozone",
 "hors_offre": "le traitement par ozone d'un local ou d'un logement",
 "hors_offre_note": "ozone",
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
 "service": "nettoyage-automobile-paris",
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
 "video": 'textile',
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
 "video": 'vitres',
        "service": "nettoyage-vitres-paris",
},
{
 "slug": "nettoyage-fin-chantier-combien-de-passages",
 "hors_offre": "le nettoyage de fin de chantier",
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
 "service": "nettoyage-regulier-paris",
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
 "service": "nettoyage-regulier-paris",
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
 "service": "nettoyage-regulier-paris",
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
                'Les frais de déplacement sont calculés depuis notre atelier du Blanc-Mesnil, à 5 € par tranche de 5 km, et annoncés avant que vous validiez. Ils figurent sur le devis, pas sur la facture finale en supplément.',
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
        "hors_offre": "le nettoyage complet d'un meublé entre deux séjours",
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
        "service": "nettoyage-textile-paris",
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
        "video": 'textile',
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
                'Nos frais de déplacement sont de 5 € par tranche de 5 km depuis notre atelier du Blanc-Mesnil, annoncés avant validation. Sur un seul matelas, ils peuvent représenter une part notable du total.',
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
             "Oui, 5 € par tranche de 5 km depuis Le Blanc-Mesnil, annoncés avant que vous validiez et figurant sur le devis. Aucun supplément n'apparaît après."),
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
        "video": 'textile',
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
                "La laine est une autre histoire. C'est une fibre animale : elle craint l'alcalinité, qui la ternit et la feutre, et elle se rétracte à la chaleur. Elle demande un produit neutre ou légèrement acide, une eau tiède et surtout pas de vapeur — c'est tout <a href='ph-produits-nettoyage-professionnel.html'>le rôle du pH dans le choix des produits</a>.",
                "La viscose est la fibre la plus délicate qui soit. Elle perd sa résistance une fois mouillée et marque définitivement à la moindre goutte. Un tapis en viscose ne se nettoie pas à l'eau, chez vous ou ailleurs : il relève d'un traitement à sec en atelier spécialisé, et nous le disons plutôt que de prendre le risque.",
                "En cas de doute, l'étiquette au dos donne souvent la composition. Sans étiquette, l'aspect et le toucher permettent de trancher dans la plupart des cas — nous le faisons sur place avant de commencer.",
            ]),
            ('La méthode et les taches', [
                "Sur un tapis synthétique, la séquence est la même que pour un canapé : "
                "désinfection à la vapeur haute température, produit choisi selon la fibre, "
                "brossage, puis injection-extraction. Sur un tapis de laine, la vapeur saute — "
                "elle rétracte la fibre — et le produit neutre fait le travail seul.",
                "Le geste final change, lui : là où un canapé demande parfois un repassage, un "
                "tapis se termine au brossage du sens du poil.",
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
        "video": 'textile',
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
        "video": 'vitres',
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
        "service": "nettoyage-haute-pression-paris",
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
                "Les frais de déplacement — 5 € par tranche de 5 km depuis Le Blanc-Mesnil — figurent sur le devis. Aucun acompte n'est demandé : vous réglez après avoir vu le résultat, ce qui est particulièrement pertinent sur une prestation aussi visible.",
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
        "service": "nettoyage-haute-pression-paris",
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
                "<strong>La vérification annuelle des installations de cuisson.</strong> L'article GC 22 de l'arrêté du 25 juin 1980 la confie à un technicien compétent ou à un organisme agréé. Nous dégraissons la hotte, les filtres et les conduits, et nous en délivrons l'attestation ; cette vérification-là est une autre prestation, et elle ne se remplace pas par un nettoyage.",
                '<strong>La désinsectisation et la dératisation.</strong> Ce sont des activités réglementées, avec agrément et produits biocides soumis à autorisation. Nous ne les pratiquons pas et nous ne masquons pas un problème de nuisibles par un nettoyage.',
                "<strong>Le plan de maîtrise sanitaire HACCP.</strong> Nous pouvons exécuter des tâches qui s'y inscrivent, mais nous ne délivrons pas d'attestation de conformité sanitaire.",
                "Vous dire non sur ces trois points nous coûte des prestations. Cela vous évite surtout de croire couvert un risque qui ne l'est pas.",
            ]),
        ],
        "faq": [
            ('Nettoyez-vous les hottes de cuisine professionnelle ?',
             "Oui, c'est devenu l'une de nos prestations principales : hotte, filtres et conduits d'extraction, par les trappes de visite, avec remontage et essai d'extraction. Vous recevez une attestation de nettoyage et d'entretien datée, à ranger dans le livret annexé à votre registre de sécurité."),
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
        "hors_offre": "le nettoyage de fin de chantier",
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
                'Nous chiffrons sur photos ou sur place, en annonçant explicitement le nombre de passages prévus et ce que chacun comprend. Les frais de déplacement figurent au devis, à 5 € par tranche de 5 km depuis Le Blanc-Mesnil.',
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
        "service": "nettoyage-regulier-paris",
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
                "Nos formules vont de l'extérieur seul à l'intérieur complet, avec un pack combinant les deux. Les tarifs sont fixes, de 50 à 130 €, et figurent sur notre grille tarifaire avec le détail de ce que chaque formule comprend.",
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
        "hors_offre": "le nettoyage de fin de chantier",
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
        "service": "nettoyage-regulier-paris",
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
        "video": 'vitres',
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
                "L'entretien correct se fait donc en deux temps : un nettoyant à pH neutre qui retire le film de sébum et de poussière, puis un lait nourrissant qui restitue la souplesse. Les deux, systématiquement. Nous détaillons ailleurs <a href='ph-produits-nettoyage-professionnel.html'>le rôle du pH dans le choix des produits</a>.",
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
        "hors_offre": "le nettoyage de mobilier d'extérieur",
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
        "service": "nettoyage-textile-paris",
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
                "Le délai est le plus court en Seine-Saint-Denis, où se trouve notre atelier du Blanc-Mesnil, ainsi qu'à Paris, en proche couronne et dans le sud du Val-d'Oise. Il s'allonge dans les Yvelines, en Seine-et-Marne et en grande couronne sud.",
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
    {
        "slug": 'ph-produits-nettoyage-professionnel',
        "cat": 'Méthode',
        "h1": 'pH et produits : la chimie qui décide du résultat',
        "title": 'pH et produits de nettoyage professionnel',
        "meta": "pH neutre, alcalin, acide : quel produit pour quelle salissure et quelle matière. Cuir, textile, laine, plastique — la logique d'un protocole professionnel.",
        "image": 'auto-interieur-vw.webp',
        "lead": "Un nettoyage professionnel ne se joue pas sur la force du produit mais sur son pH. C'est lui qui détermine ce qu'on dissout, et surtout ce qu'on risque d'abîmer au passage.",
        "sections": [
            ("L'échelle de pH, en deux minutes", [
                "Le pH mesure l'acidité d'une solution sur une échelle de 0 à 14. En dessous de 7, on est en milieu acide ; à 7, neutre ; au-dessus, alcalin. Chaque unité représente un facteur dix : un produit à pH 12 est cent fois plus alcalin qu'un produit à pH 10.",
                "Cette échelle commande deux choses à la fois. D'un côté ce que le produit est capable de dissoudre : l'alcalin attaque le gras et les matières organiques, l'acide dissout le minéral. De l'autre ce qu'il abîme : chaque matière a une plage de tolérance, et en sortir laisse une marque définitive.",
                "Un nettoyant universel n'existe donc pas. Un produit qui décolle une trace de gras sur un plastique de tableau de bord est exactement celui qui va ternir un cuir et feutrer une laine. C'est la raison pour laquelle nous arrivons avec une gamme, pas avec un bidon.",
                "Concrètement, nous travaillons avec quatre familles : neutre (pH 6 à 8) pour tout ce qui est fragile, faiblement alcalin (pH 8 à 10) pour l'entretien courant, alcalin (pH 10 à 12) pour les corps gras, et acide (pH 2 à 5) pour le calcaire et les dépôts minéraux.",
            ]),
            ('Le cuir : pH neutre, et rien au-dessus', [
                "Un cuir est une peau tannée. Le tannage la stabilise dans une plage acide — un cuir au chrome se situe autour de pH 4 à 5 — et c'est cet équilibre qui maintient la souplesse de la fibre de collagène.",
                "Un produit alcalin fait deux choses à un cuir. Il attaque la finition pigmentée en surface, qui est un vernis polyuréthane, et il déplace le pH de la peau elle-même. Le cuir paraît propre le jour même, puis se rigidifie sur les mois qui suivent et craquelle aux points de flexion : bourrelet d'assise, joue de siège côté conducteur, accoudoir.",
                "Nous utilisons donc exclusivement des nettoyants à pH neutre à légèrement acide sur le cuir, dans des gammes professionnelles de detailing comme <strong>Koch Chemie</strong>, un fabricant allemand dont les produits sont la référence dans les ateliers de préparation automobile. Ce n'est pas une question de marque : c'est que ces gammes affichent leur pH, ce que ne fait aucun produit de grande surface.",
                "Le nettoyage est systématiquement suivi d'un nourrissant. Un cuir dégraissé et laissé tel quel est un cuir qu'on a asséché. Les deux étapes vont ensemble, toujours.",
            ]),
            ("La mousse : pourquoi on ne mouille pas un cuir", [
                "Le second facteur de dégradation du cuir n'est pas chimique, il est hydrique. Une peau saturée d'eau gonfle, ses fibres s'écartent, et en séchant elles se resserrent de façon irrégulière. La finition, elle, ne suit pas ce mouvement : elle se micro-fissure. C'est ce qu'on retrouve sur les sièges nettoyés au jet ou à l'éponge gorgée d'eau.",
                "Nous appliquons donc les produits au <strong>mousseur</strong>. Un mousseur transforme la solution en mousse aérée : le volume apparent est important, la quantité d'eau réellement déposée sur la peau est faible. Le tensioactif reste en surface, là où se trouve la salissure, au lieu de migrer dans l'épaisseur du cuir.",
                "L'application se fait ensuite à la brosse à poils souples, en petits mouvements circulaires qui font remonter la crasse dans la mousse, puis la mousse est reprise à la microfibre sèche. À aucun moment le cuir n'est rincé à l'eau courante.",
                "La même logique vaut sur les tissus de sellerie et sur l'alcantara. La règle de l'atelier est simple : on aspire toujours plus qu'on n'injecte. C'est ce qui évite l'auréole au séchage, et c'est aussi ce qui distingue une extraction d'un shampoing.",
            ]),
            ("L'alcalin sur les taches : puissant, donc encadré", [
                "Une tache de gras, de sébum, de nourriture ou de sang ne part pas à l'eau. Ce sont des salissures organiques, et elles se traitent en milieu alcalin : l'alcalinité saponifie les corps gras, c'est-à-dire qu'elle les transforme en composés solubles que l'extraction peut emporter.",
                "Nous réservons ces produits aux zones concernées, jamais à l'ensemble d'une surface. Un détachant alcalin s'applique en localisé, avec un temps de pose contrôlé — le temps est ce qui travaille, pas le frottement — puis il est immédiatement extrait.",
                "Le point critique est le rinçage. Un résidu alcalin laissé dans une fibre continue d'agir après notre départ : il jaunit les textiles clairs, il rend le toucher collant, et sur une moquette il refixe la poussière plus vite qu'avant l'intervention. Sur les fibres sensibles, l'extraction finale se fait avec une solution légèrement acide qui neutralise ce qui reste.",
                "Sur cuir, un détachant alcalin ne s'utilise que ponctuellement, sur une tache identifiée, sur un cuir pigmenté, et toujours suivi d'un nettoyant neutre et d'un nourrissant sur la zone entière du panneau — pour ne pas laisser une zone plus claire que le reste.",
            ]),
            ("L'acide sur le minéral : calcaire, auréoles, traces d'eau", [
                "Les dépôts minéraux relèvent de la chimie inverse. Le calcaire d'une paroi de douche, les traces d'eau dure séchées sur une vitre ou une carrosserie, les traces de rouille sur un textile : aucun produit alcalin ne les enlève, quelle que soit sa concentration.",
                "Ils se dissolvent en milieu acide, généralement entre pH 2 et 5. Là encore, le temps de pose fait le travail. Et là encore, un rinçage complet est obligatoire : un résidu acide laissé sur un joint, un chrome ou un alliage attaque le support.",
                "L'acide est proscrit sur les surfaces calcaires elles-mêmes — pierre naturelle, marbre, travertin, certains bétons cirés. Le produit qui dissout le dépôt dissout aussi le support : la surface devient mate et rugueuse par endroits, ce qui est irréversible.",
                "C'est le type d'erreur qu'on voit régulièrement sur des sols en pierre traités avec un anticalcaire de grande surface. Le diagnostic de la matière passe donc toujours avant le choix du produit.",
            ]),
            ("L'inox : ce qui le fait rouiller, c'est le produit", [
                "L'inox n'est pas un métal qui ne rouille pas : c'est un acier qui contient au moins 10,5 % de chrome, et ce chrome forme en surface une couche d'oxyde invisible de quelques nanomètres, la couche passive. C'est elle qui protège, et elle se reconstitue seule au contact de l'oxygène de l'air.",
                "Une seule famille de produits détruit cette couche : les <strong>chlorures</strong>. L'eau de Javel, l'acide chlorhydrique et une bonne partie des détartrants et des désinfectants de grande surface en contiennent. Ils percent la couche passive en un point, et la corrosion s'installe dessous. C'est la corrosion par piqûres : de petites taches brunes ou orangées, en creux, qui apparaissent quelques jours après le nettoyage et ne partent plus.",
                "L'erreur est extrêmement courante en cuisine, où l'on désinfecte à la Javel un plan de travail ou une crédence en inox en pensant bien faire. Le lendemain il n'y a rien ; au bout d'une semaine, la surface est piquée.",
                "Nous n'utilisons donc <strong>aucun produit chloré sur l'inox</strong>. Le dégraissage se fait à l'alcalin sans chlorure, la désinfection à la vapeur haute température ou à l'alcool, et le détartrage à l'acide citrique ou phosphorique — jamais chlorhydrique.",
                "Le rinçage et l'essuyage complets font partie du protocole, pas de la finition. Une goutte d'eau dure laissée à sécher sur de l'inox concentre en s'évaporant les sels qu'elle contient : c'est le même mécanisme, en plus lent.",
            ]),
            ("Le geste sur l'inox : sens du brossage et contamination ferreuse", [
                "Le second facteur est mécanique. Un inox brossé a un sens : les micro-rayures du satinage sont toutes parallèles. Nettoyer perpendiculairement à ce sens laisse un voile croisé qui accroche la lumière et se voit sous tous les éclairages, même sur une surface parfaitement propre. Nous travaillons toujours dans le sens du brossage, y compris pour l'essuyage.",
                "Plus grave : la laine d'acier et les éponges abrasives déposent dans la surface des particules d'acier ordinaire. Ces particules-là, elles, rouillent normalement. On obtient alors une surface constellée de points de rouille qui ne viennent pas de l'inox mais de ce qu'on a laissé dedans — c'est la contamination ferreuse, et elle impose un décontaminant spécifique pour être retirée.",
                "Sur inox, nous travaillons donc à la microfibre et à la brosse non métallique. Quand une surface est déjà piquée ou contaminée, il existe une remise en état par décontamination puis passivation, mais elle relève de la rénovation métallique : nous le disons plutôt que de frotter plus fort.",
                "En finition, un film d'huile alimentaire neutre passé à la microfibre uniformise l'aspect et retarde la reprise des traces de doigts. C'est ce qui fait la différence visuelle entre un inox propre et un inox présentable.",
            ]),
            ('Les hottes et les filtres : le piège de l\'aluminium', [
                "La graisse de cuisson est un corps gras polymérisé par la chaleur : elle ne se dissout ni à l'eau ni au dégraissant ménager. Elle demande un alcalin, de la température et du temps de pose. C'est la température qui fait l'essentiel du travail, raison pour laquelle nous traitons les caissons et les surfaces à la vapeur haute température avant tout produit.",
                "Le point que presque personne ne connaît concerne les filtres. La plupart des filtres à chocs de hotte sont en <strong>aluminium</strong>, et l'aluminium est un métal amphotère : il est attaqué aussi bien par les acides forts que par les bases fortes. Un dégraissant four très alcalin — au-delà de pH 11, souvent à base de soude — noircit un filtre aluminium, le pique et le rend friable. Le filtre ressort propre et détruit.",
                "Nous traitons donc les filtres aluminium avec un dégraissant modérément alcalin et un trempage tiède, pas avec un décapant four. Les filtres inox, eux, tolèrent un alcalin plus soutenu, et c'est encore un cas où identifier le métal commande le produit.",
                "Sur la hotte elle-même, le caisson et la surface visible sont presque toujours en inox : tout ce qui précède s'applique, et notamment l'interdiction du chloré. Un dégraissant chloré sur une hotte revient à la faire rouiller pour la nettoyer.",
                "Le conduit d'extraction obéit aux mêmes règles de produit, avec une difficulté en plus : on y travaille à l'aveugle, par les trappes de visite. Sur un dépôt polymérisé par des années de chaleur, un alcalin à temps de pose ne suffit pas en une passe, et la suie d'un four à bois ne se dissout pas du tout — elle se décolle à la brosse. C'est la raison pour laquelle dégraissage chimique et ramonage mécanique sont deux opérations distinctes, et pourquoi une cuisine au feu de bois a besoin des deux.",
            ]),
            ('Les fibres qui ne tolèrent pas l\'alcalinité', [
                "La laine et la soie sont des fibres protéiniques, faites de kératine et de fibroïne. Au-delà de pH 8, la structure de la fibre se dégrade : la laine ternit, se feutre et perd sa résistance ; la soie perd son brillant de façon définitive.",
                "Ces fibres se traitent en neutre ou en légèrement acide, à l'eau tiède et jamais à la vapeur, qui les rétracte. C'est vrai d'un tapis en laine comme d'un canapé en velours de laine.",
                "La viscose est un cas à part, non pas pour son pH mais pour sa résistance : elle perd sa tenue une fois mouillée et marque à la moindre goutte, quel que soit le produit. Elle relève d'un traitement à sec en atelier, et nous le disons plutôt que d'essayer.",
                "Le coton, le lin et l'ensemble des synthétiques — polyester, polypropylène, nylon — tolèrent une alcalinité modérée sans difficulté. Ce sont les matières les plus simples, et de loin les plus fréquentes.",
            ]),
            ('Produits biodégradables : ce que le mot veut dire', [
                "Nous privilégions des produits biodégradables, c'est-à-dire dont les tensioactifs se dégradent en milieu naturel plutôt que de s'accumuler. C'est un critère de choix réel, et c'est ce que nous pouvons affirmer honnêtement.",
                "En revanche, un produit biodégradable n'est pas un produit inoffensif. Un dégraissant alcalin biodégradable reste un dégraissant alcalin : il abîme une laine exactement de la même façon. La biodégradabilité concerne ce qui se passe après le rejet, pas la compatibilité avec votre matière.",
                "Il faut aussi être précis sur le vocabulaire, parce qu'il est encadré. Le terme « bio » est réservé aux produits certifiés par un organisme agréé. Un détergent ne peut s'en prévaloir que s'il porte un label vérifiable — Écolabel européen, Ecocert. En dehors de cela, le mot juste est « biodégradable » ou « écologique », et il engage celui qui l'emploie.",
                "La meilleure façon de réduire la chimie reste de ne pas en utiliser. Sur beaucoup de surfaces dures, la vapeur haute température fait le travail seule : elle décolle le gras par la chaleur et désinfecte par la température, sans aucun résidu. Quand elle suffit, nous n'ajoutons rien.",
            ]),
        ],
        "faq": [
            ('Peut-on nettoyer de l\'inox à l\'eau de Javel ?',
             "Non, et c'est l'erreur la plus dommageable. La Javel contient des chlorures, qui percent la couche passive de chrome protégeant l'inox. La corrosion s'installe dessous et donne des piqûres brunes en creux, visibles quelques jours plus tard et définitives. La désinfection se fait à la vapeur ou à l'alcool."),
            ('Pourquoi ne pas utiliser un décapant four sur un filtre de hotte ?',
             "Parce que les filtres à chocs sont généralement en aluminium, un métal attaqué par les bases fortes autant que par les acides. Un décapant à base de soude le noircit, le pique et le fragilise. Nous utilisons un dégraissant modérément alcalin et un trempage tiède, qui nettoient sans détruire le filtre."),
            ('D\'où viennent les points de rouille sur mon inox ?',
             "Le plus souvent d'une éponge abrasive ou d'une laine d'acier : elles déposent dans la surface des particules d'acier ordinaire qui, elles, rouillent. C'est une contamination ferreuse, pas une défaillance de l'inox. Elle se retire par décontamination, puis on repasse à la microfibre et à la brosse non métallique."),
            ('Pourquoi utiliser un produit à pH neutre sur le cuir ?',
             "Parce qu'un cuir tanné est stabilisé en milieu acide, autour de pH 4 à 5. Un produit alcalin attaque sa finition pigmentée et déplace l'équilibre de la peau : le cuir se rigidifie sur les mois qui suivent et craquelle aux points de flexion. Un nettoyant neutre à légèrement acide retire le sébum sans toucher à cet équilibre."),
            ('Pourquoi appliquer les produits en mousse plutôt qu\'au chiffon mouillé ?',
             "Pour limiter la quantité d'eau déposée. Une peau saturée gonfle puis se rétracte au séchage, et la finition se micro-fissure. Le mousseur donne du volume avec peu d'eau : le produit agit en surface, là où est la salissure, sans pénétrer dans l'épaisseur du cuir."),
            ('Quand utilisez-vous un produit alcalin ?',
             "Sur les salissures organiques — gras, sébum, alimentaire, sang — qui ne partent pas à l'eau. Toujours en application localisée, avec un temps de pose contrôlé, puis une extraction immédiate et un rinçage. Un résidu alcalin laissé dans une fibre jaunit les textiles clairs et refixe la poussière."),
            ('Utilisez-vous des produits écologiques ?',
             "Nous privilégions des produits biodégradables et nous nous en passons quand la vapeur haute température suffit. Nous ne revendiquons pas le terme « bio », qui est réservé aux produits certifiés par un organisme agréé, et nous préférons dire précisément ce que nous utilisons."),
            ('Un produit plus fort nettoie-t-il mieux ?',
             "Non, il abîme plus vite. Sur une salissure donnée, c'est le pH adapté et le temps de pose qui font le résultat, pas la concentration. Une gamme professionnelle sert précisément à disposer du bon pH pour chaque matière plutôt qu'à monter en puissance."),
        ],
        "video": 'mathclean',
        "service": 'nettoyage-automobile-paris',
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
            "L'est parisien mêle logements récents et locaux reconvertis : grandes verrières "
            "d'anciens ateliers, plateaux ouverts, moquettes de bureau. Les vitrages y sont "
            "souvent hauts, ce qui se travaille à la perche depuis le sol.",
        ]),
    ],
    "92": [
        ("Bureaux et résidentiel haut de gamme", [
            "Les Hauts-de-Seine cumulent deux terrains très différents. Au nord et au centre, "
            "les quartiers d'affaires : de grands plateaux, des moquettes de bureau à extraire, "
            "des sièges à reprendre, et une contrainte horaire absolue — on n'intervient pas "
            "pendant les heures ouvrées.",
            "Au sud et sur les communes résidentielles, un habitat plus cossu où les demandes "
            "portent sur les textiles de qualité, les cuirs et les vitrages de grande "
            "surface. C'est là que la distinction entre cuir pigmenté et cuir aniline "
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
            "Notre atelier est au Blanc-Mesnil. La Seine-Saint-Denis est donc le "
            "département où nos délais sont les plus courts et nos frais de déplacement les "
            "plus faibles — parfois nuls sur les communes les plus proches.",
            "C'est aussi le département où nous pouvons le plus souvent caler une intervention "
            "le jour même, et où un second passage sur une tache qui demande un temps d'action "
            "ne pose aucune difficulté d'organisation.",
        ]),
        ("Un terrain d'activité autant que d'habitat", [
            "Le 93 concentre des zones d'activité, des entrepôts, des locaux reconvertis et un "
            "habitat collectif dense. Les demandes s'y répartissent entre l'entretien de locaux "
            "professionnels, la vitrerie de façade et de vitrine, et le textile en logement.",
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
            "beaucoup de vitrages — baies côté jardin, vérandas — dans le pavillonnaire, du "
            "textile et de l'entretien de parties communes dans le collectif.",
            "Les pavillons de bord de Marne ont souvent une véranda ou une grande baie "
            "exposée plein sud, que la pluie et le pollen marquent en quelques semaines.",
        ]),
        ("Le facteur végétal", [
            "C'est le département le plus arboré de la petite couronne, et cela se voit sur "
            "les vitres : pollen au printemps, sève et poussière l'été, feuilles collées par "
            "la pluie à l'automne. Une eau ordinaire laisse alors des traces en séchant, parce "
            "que ses minéraux restent sur le verre une fois l'eau partie.",
            "Nous travaillons à l'eau osmosée, privée de ces minéraux : elle sèche sans rien "
            "déposer, y compris sur de grandes surfaces qu'on ne peut pas essuyer d'un geste.",
        ]),
    ],
    "91": [
        ("Grande couronne sud : espace et accès faciles", [
            "L'Essonne offre ce que Paris n'a pas : de la place. Les interventions y sont "
            "matériellement plus simples — on se gare devant, on déploie le matériel, on "
            "travaille sans contrainte de créneau.",
            "Les demandes suivent l'habitat : pavillonnaire dominant, donc beaucoup "
            "d'automobile à domicile et de vitrages de grande surface, vérandas comprises.",
        ]),
        ("Grouper, parce que le trajet compte", [
            "L'Essonne est éloignée de notre atelier du Blanc-Mesnil. Nous nous y "
            "déplaçons volontiers, mais nous vous conseillons de regrouper : la voiture et les "
            "vitres, les matelas et le canapé, la véranda et la baie du salon.",
            "Le déplacement est unique, le matériel est déjà en place, et le coût par "
            "prestation baisse nettement. C'est le conseil le plus utile que nous puissions "
            "donner sur ce département, et il ne va pas dans le sens de notre facturation.",
        ]),
    ],
    "78": [
        ("Un patrimoine qui impose de la prudence", [
            "Les Yvelines concentrent un bâti ancien et des matières qui ne pardonnent pas "
            "l'erreur : tapis de laine, selleries cuir, rideaux anciens, menuiseries à petits "
            "bois. Trop d'eau ou un produit trop alcalin y font des dégâts définitifs.",
            "Notre règle sur ce type de support est simple : essai sur une zone discrète avant "
            "toute intervention, dosage et température réglés au cas par cas, et refus assumé "
            "quand la matière relève d'un atelier spécialisé. Une laine feutrée par une eau "
            "trop chaude ne se rattrape pas.",
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
            "Le terrain mêle habitat individuel avec de grandes surfaces vitrées et un tissu "
            "de locaux d'activité et d'entrepôts. L'entretien de ces locaux y est fréquent, "
            "porté par la construction neuve.",
            "Comme en Essonne, le conseil qui compte est de grouper. Une venue qui traite les "
            "vitres, le canapé et la voiture vaut mieux que trois déplacements successifs, "
            "pour nous comme pour votre facture.",
        ]),
    ],
    "95": [
        ("Proche de notre atelier", [
            "Le Val-d'Oise commence à quelques kilomètres de notre atelier du Blanc-Mesnil. "
            "C'est, avec la Seine-Saint-Denis et Paris, le secteur où nous intervenons le plus "
            "vite et où les frais de déplacement sont les plus bas.",
            "Sur les communes du sud-est du département — Garges, Sarcelles, Villiers-le-Bel, "
            "Gonesse — nous sommes souvent à moins de quinze "
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


# --- Pages « prestation × commune » ----------------------------------------
# Dix communes parmi les plus aisées d'Île-de-France, croisées avec chaque
# prestation. Une page par couple, avec un angle qui lui est propre : sans
# cela on obtiendrait quatre-vingts variantes du même texte, ce qu'un moteur
# traite comme des pages satellites et non comme du contenu utile.
#
# Chaque commune porte :
#   profil  — le tissu réel de la commune (habitat, activité)
#   acces   — la contrainte pratique d'intervention (stationnement, accès)
#   angles  — par prestation : deux paragraphes, une question, sa réponse
PREMIUM_VILLES = [
    {
        "slug": "neuilly-sur-seine", "nom": "Neuilly-sur-Seine", "cp": "92200",
        "dept": "92", "lat": 48.8846, "lon": 2.2697,
        "profil": "Neuilly-sur-Seine aligne de part et d'autre de l'avenue Charles-de-Gaulle des "
                  "immeubles haussmanniens et Art déco aux appartements familiaux généreux : "
                  "parquets anciens, moulures, mobilier de valeur. La commune compte aussi une "
                  "forte proportion de professions libérales qui reçoivent à domicile ou en cabinet, "
                  "et un bord de Seine résidentiel autour de l'île de la Jatte.",
        "acces": "Le stationnement est payant et tendu presque partout, et une grande partie des "
                 "immeubles n'ont qu'un parking souterrain à hauteur limitée. Nous intervenons en "
                 "véhicule léger, capable de descendre en sous-sol, et nous travaillons sur place "
                 "sans avoir à déplacer quoi que ce soit.",
        "angles": {
            "nettoyage-voiture": (
                "À Neuilly, la plupart des véhicules dorment en parking souterrain et ne voient "
                "jamais une station de lavage. L'habitacle vieillit pourtant plus vite qu'ailleurs : "
                "peu d'aération, beaucoup de trajets courts, et des cuirs clairs — beiges, crème, "
                "gris perle — qui marquent au moindre transfert de teinture depuis un jean.",
                "Nous venons sur votre place de parking, y compris en sous-sol, avec notre eau et "
                "notre électricité. Les cuirs sont traités à pH neutre et au mousseur, jamais "
                "détrempés : c'est ce qui évite la craquelure sur les sièges clairs, qui est le "
                "défaut le plus coûteux à rattraper sur ce type de véhicule.",
                "Pouvez-vous descendre dans un parking souterrain à Neuilly ?",
                "Oui, c'est même le cas le plus fréquent ici. Notre véhicule passe sous les "
                "1,90 m qui limitent la plupart des sous-sols neuillyséens. Nous apportons l'eau "
                "et l'électricité : aucun branchement n'est demandé à la copropriété, et votre "
                "voiture ne bouge pas de sa place."),
            "nettoyage-canape": (
                "Les salons neuillyséens sont grands, et les canapés qui les meublent aussi : "
                "angles de trois mètres, tissus clairs, lin, coton épais et velours. Sur ces "
                "matières, la salissure ne se voit pas d'un coup — elle s'installe par un "
                "grisaillement progressif des assises et des accoudoirs, que l'œil finit par ne "
                "plus remarquer.",
                "Nous travaillons à l'injection-extraction : la solution est envoyée dans la fibre "
                "puis immédiatement réaspirée, sans eau stagnante donc sans auréole. Sur un velours "
                "ou un lin, le sens du poil est relevé avant de commencer et respecté au séchage. "
                "Les canapés cuir relèvent d'un autre protocole, à pH neutre.",
                "Un canapé en lin clair supporte-t-il l'injection-extraction ?",
                "Oui, à condition de doser l'eau et de tester au préalable sur une zone cachée. Le "
                "lin rétrécit s'il est détrempé : nous travaillons donc avec un temps de contact "
                "court et une extraction complète. Sur une housse déhoussable ancienne, nous "
                "préférons parfois vous le dire franchement et ne pas intervenir."),
            "nettoyage-vitres": (
                "Les immeubles neuillyséens ont conservé beaucoup de fenêtres anciennes à petits "
                "bois et de hauteurs sous plafond de trois mètres. Ce sont les vitrages les plus "
                "longs à faire correctement : chaque carreau demande son passage, et les mastics "
                "anciens retiennent la poussière que le lavage fait ensuite couler sur la vitre.",
                "Nous travaillons à l'eau osmosée, déminéralisée : elle sèche sans laisser la trace "
                "blanche que laisse l'eau du robinet, riche en calcaire en Île-de-France. Les "
                "encadrements et les appuis sont repris dans le même passage — c'est là que se "
                "loge la saleté qui salit à nouveau la vitre à la première pluie.",
                "Comment comptez-vous une fenêtre à petits bois ?",
                "Au vantail, pas au mètre carré. Une fenêtre à six carreaux demande plusieurs fois "
                "le temps d'une baie de même surface, et un tarif au mètre carré serait trompeur "
                "dans un sens comme dans l'autre. Nous comptons les vantaux sur photos, et le "
                "devis est ferme avant que nous venions."),
            "menage-regulier": (
                "Neuilly concentre des cabinets — médicaux, dentaires, d'avocats — et des sièges "
                "sociaux installés dans d'anciens appartements. Ce sont des locaux de petite "
                "surface mais à forte exigence : salle d'attente très fréquentée, moquettes "
                "claires, et une image qui se juge dès la porte franchie.",
                "Nous intervenons avant l'ouverture, après la fermeture ou le week-end, sans "
                "supplément — c'est la seule façon de traiter correctement une moquette, qui "
                "demande plusieurs heures de séchage. Passage ponctuel ou régulier, avec "
                "facturation entreprise et un interlocuteur unique : celui qui intervient.",
                "Pouvez-vous intervenir dans un cabinet médical en dehors des consultations ?",
                "Oui, et c'est ce que nous recommandons. Nous travaillons tôt le matin, en soirée "
                "ou le week-end sans majoration. Précisons un point : nous réalisons un nettoyage "
                "professionnel soigné, pas une désinfection réglementée de bloc ou de dispositif "
                "médical, qui relève d'un protocole et d'une certification que nous n'avons pas."),
        },
    },
    {
        "slug": "boulogne-billancourt", "nom": "Boulogne-Billancourt", "cp": "92100",
        "dept": "92", "lat": 48.8352, "lon": 2.2409,
        "profil": "Boulogne-Billancourt est la plus peuplée des communes des Hauts-de-Seine, et "
                  "l'une des plus contrastées : immeubles modernes du Trapèze et de l'île "
                  "Seguin d'un côté, maisons d'architecte et immeubles Art déco du vieux "
                  "Boulogne de l'autre. Beaucoup d'actifs en horaires étendus, et un tissu de "
                  "sociétés de production et de bureaux hérité des studios.",
        "acces": "Les programmes récents du Trapèze disposent de parkings accessibles et de locaux "
                 "de service, ce qui simplifie l'intervention. Dans le vieux Boulogne, le "
                 "stationnement est plus tendu : nous prévoyons le créneau en conséquence et nous "
                 "venons autonomes en eau et en électricité.",
        "angles": {
            "nettoyage-voiture": (
                "Boulogne cumule les deux situations qui abîment un habitacle : des trajets "
                "courts et répétés dans un trafic dense, et un stationnement en sous-sol où la "
                "voiture ne sèche jamais complètement. Résultat, une odeur de renfermé qui "
                "s'installe et des plastiques qui grisent sans que la voiture soit sale au sens "
                "où on l'entend.",
                "Nous nettoyons sur votre place, en surface comme en sous-sol. La vapeur haute "
                "température traite les sièges tissu et les surfaces de contact sans produit "
                "agressif, et les plastiques reçoivent une protection qui les empêche de "
                "reblanchir au premier soleil. L'option ozone règle le reste de l'odeur.",
                "Combien de temps faut-il prévoir sur place ?",
                "De une à trois heures selon la formule : environ une heure pour un extérieur, "
                "près de trois pour un Intérieur Prestige avec cuir. Nous n'avons besoin ni de "
                "votre prise ni d'un point d'eau, et la voiture reste sur sa place du début à "
                "la fin de l'intervention."),
            "nettoyage-canape": (
                "Dans les appartements du Trapèze, les canapés sont souvent en tissu déperlant "
                "de facture récente ; dans le vieux Boulogne, on trouve davantage de pièces "
                "anciennes retapissées. Les deux demandent une méthode différente, et c'est "
                "l'erreur la plus fréquente : appliquer à un velours ancien ce qui convient à "
                "une microfibre moderne.",
                "Nous relevons la composition et l'étiquette d'entretien avant de commencer, et "
                "nous testons sur une zone cachée. L'injection-extraction convient à la grande "
                "majorité des tissus ; sur une viscose ou une soie, qui perdent leur résistance "
                "une fois mouillées, nous le disons et nous ne forçons pas.",
                "Vous déplacez-vous pour un seul fauteuil ?",
                "Oui, mais le déplacement pèse alors lourd dans le total : il n'est facturé "
                "qu'une fois, quel que soit le nombre de pièces. Si vous avez un canapé, des "
                "chaises ou un matelas à traiter, regroupez-les sur la même intervention — "
                "c'est nettement plus avantageux qu'un fauteuil seul."),
            "nettoyage-vitres": (
                "Le Trapèze et les immeubles récents de Boulogne ont de grandes surfaces vitrées "
                "et des garde-corps toute hauteur. Elles se salissent vite — pluie, poussière "
                "urbaine, proximité du périphérique — et se voient d'autant plus qu'elles sont "
                "grandes : une trace sur une baie de trois mètres ne passe pas inaperçue.",
                "L'eau osmosée que nous utilisons ne contient plus de calcaire : elle sèche sans "
                "dépôt, ce qui permet de ne pas essuyer et donc de ne pas laisser de trace de "
                "raclette. Jusqu'à trois niveaux, nous travaillons depuis le sol à la perche. "
                "Au-delà, il faut une nacelle ou des cordistes, métiers que nous ne pratiquons pas.",
                "Travaillez-vous les vitres des garde-corps en verre ?",
                "Oui, elles font partie du même passage. Ce sont souvent elles qui donnent "
                "l'impression que la terrasse est sale : traces de pluie, marques de mains, "
                "dépôt calcaire au bas du panneau. Nous les comptons comme des vantaux dans le devis."),
            "menage-regulier": (
                "Boulogne accueille beaucoup de sociétés de production, d'agences et de bureaux "
                "de taille moyenne, souvent installés dans des plateaux ouverts avec moquette. "
                "La moquette est précisément ce qui vieillit le plus visiblement dans un bureau : "
                "les couloirs de passage grisent et finissent par dessiner la circulation au sol.",
                "Nous traitons les moquettes à l'injection-extraction, en dehors des heures "
                "d'ouverture, avec plusieurs heures de séchage devant nous. Vitrerie, sanitaires, "
                "cuisines et surfaces de contact peuvent entrer dans le même passage. Facturation "
                "entreprise, en ponctuel ou en régulier.",
                "Une moquette de plateau peut-elle être traitée un week-end ?",
                "C'est même la meilleure fenêtre : l'extraction demande quatre à six heures de "
                "séchage en pièce aérée, ce qui est incompatible avec un plateau occupé. Nous "
                "intervenons le samedi ou le dimanche sans supplément, et vos équipes retrouvent "
                "le lundi une moquette sèche."),
        },
    },
    {
        "slug": "levallois-perret", "nom": "Levallois-Perret", "cp": "92300",
        "dept": "92", "lat": 48.8939, "lon": 2.2880,
        "profil": "Levallois-Perret est l'une des communes les plus densément peuplées d'Europe : "
                  "des immeubles serrés, beaucoup d'appartements de deux à quatre pièces, une "
                  "population jeune et active, et un tissu de sièges sociaux concentré autour du "
                  "front de Seine. Les logements y tournent vite, à la location comme à la vente.",
        "acces": "La densité se paie au stationnement : peu de places en surface, des parkings "
                 "souterrains étroits et des ascenseurs de petite capacité. Nous venons en "
                 "véhicule léger avec un matériel qui passe en ascenseur, et nous calons le "
                 "créneau en dehors des heures de pointe quand c'est possible.",
        "angles": {
            "nettoyage-voiture": (
                "À Levallois, la voiture sert surtout le week-end et passe la semaine en "
                "sous-sol. C'est le pire régime pour un habitacle : l'humidité ne s'évacue pas, "
                "les odeurs s'installent dans les mousses, et la carrosserie reçoit la poussière "
                "de freinage du parking sans jamais recevoir de pluie pour la rincer.",
                "Nous intervenons sur votre place de parking, sans que le véhicule ait à sortir. "
                "L'aspiration, la vapeur et le traitement des plastiques se font en autonomie "
                "complète : ni prise, ni point d'eau à fournir. Sur un habitacle qui sent le "
                "renfermé, l'option ozone à 30 € règle ce que le nettoyage seul ne règle pas.",
                "Faut-il que je sois présent pendant l'intervention ?",
                "Non, si vous nous laissez l'accès au parking et les clés du véhicule. Beaucoup "
                "de clients levalloisiens nous ouvrent le matin et récupèrent la voiture le soir. "
                "Nous vous envoyons des photos à la fin, et le règlement se fait après, une fois "
                "le résultat constaté."),
            "nettoyage-canape": (
                "Dans des appartements de cette taille, le canapé est le meuble le plus sollicité "
                "de la maison : on y mange, on y travaille, on y dort parfois. Sur un deux-pièces "
                "levalloisien, il encaisse en trois ans ce qu'un canapé de maison encaisse en dix, "
                "et l'assise s'affaisse en même temps qu'elle grise.",
                "L'injection-extraction retire ce que l'aspirateur laisse : la poussière logée au "
                "cœur de la fibre, les transferts de teinture, les auréoles de boisson. Le "
                "traitement anti-acariens qui suit a un intérêt réel dans un logement dense et peu "
                "aéré, davantage que dans une maison avec de grandes ouvertures.",
                "Combien de temps un canapé met-il à sécher dans un petit appartement ?",
                "Quatre à six heures en pièce aérée, un peu plus si l'assise est épaisse. Dans un "
                "logement peu ventilé, ouvrez en grand pendant deux heures après notre départ : "
                "c'est ce qui fait la différence. Nous n'utilisons pas de shampouineuse à eau "
                "stagnante, justement parce que le séchage y serait interminable."),
            "nettoyage-vitres": (
                "À Levallois, les vis-à-vis sont proches et les fenêtres nombreuses. Une vitre "
                "sale s'y remarque davantage qu'ailleurs, simplement parce qu'on la regarde de "
                "près. Les façades exposées aux axes de circulation reçoivent en plus un film "
                "gras de particules, que le lave-vitre du commerce étale sans retirer.",
                "L'eau osmosée retire ce film sans laisser de trace en séchant, puisqu'elle ne "
                "contient plus de calcaire. Les appuis et les encadrements sont repris dans le "
                "même geste : c'est de là que repart la coulure qui salit la vitre à la première "
                "pluie, et c'est ce que la plupart des passages rapides oublient.",
                "À quelle fréquence faire laver ses vitres ici ?",
                "Deux à trois fois par an pour un appartement en étage, davantage sur une façade "
                "donnant sur un axe passant. Ce n'est pas une question d'esthétique seule : le "
                "film de particules attaque les joints à la longue. Sur une vitrine commerciale, "
                "le rythme est mensuel, voire hebdomadaire."),
            "menage-regulier": (
                "Levallois concentre des sièges sociaux et des plateaux tertiaires sur un "
                "territoire réduit. Les prestataires y sont nombreux, et les entreprises passent "
                "souvent d'un contrat d'entretien à un besoin ponctuel : une remise à niveau avant "
                "un déménagement, une visite client, un audit.",
                "C'est exactement le type d'intervention que nous prenons : ponctuelle, chiffrée "
                "d'avance, réalisée hors des heures d'ouverture. Moquettes en injection-extraction, "
                "vitrerie intérieure et extérieure jusqu'à trois niveaux, sanitaires, cuisines et "
                "surfaces de contact. Sans engagement de durée.",
                "Faites-vous de l'entretien régulier ou seulement du ponctuel ?",
                "Les deux. Beaucoup de clients commencent par une remise à niveau ponctuelle puis "
                "passent en régulier — hebdomadaire ou mensuel — quand ils ont vu le résultat. "
                "Nous n'imposons pas d'engagement de durée : si le service ne convient pas, vous "
                "arrêtez."),
        },
    },
    {
        "slug": "puteaux", "nom": "Puteaux", "cp": "92800",
        "dept": "92", "lat": 48.8846, "lon": 2.2386,
        "profil": "Puteaux porte la moitié du quartier d'affaires de La Défense, et bascule en "
                  "quelques rues vers un tissu résidentiel plus calme, entre le vieux village et "
                  "l'île de Puteaux. Deux mondes qui ne se nettoient pas de la même façon : des "
                  "tours de bureaux d'un côté, des maisons et des immeubles familiaux de l'autre.",
        "acces": "À La Défense, tout passe par la logistique du site : badge, quai de livraison, "
                 "créneau imposé. Nous nous y plions et nous demandons ces éléments au devis. "
                 "Côté résidentiel, le stationnement est plus simple, sauf aux abords immédiats "
                 "de la dalle.",
        "angles": {
            "nettoyage-voiture": (
                "Une voiture garée dans les parkings de La Défense encaisse un régime particulier : "
                "poussière de freinage en suspension, ventilation permanente, et aucune exposition "
                "à la pluie. La carrosserie se couvre d'un voile qui s'incruste, et l'habitacle "
                "accumule sans jamais se rincer.",
                "Nous intervenons directement sur la place de parking, en surface comme en "
                "sous-sol, avec notre eau et notre électricité. Pour un salarié de La Défense, "
                "c'est l'occasion de faire nettoyer la voiture pendant la journée de travail, "
                "sans y consacrer une minute de son week-end.",
                "Intervenez-vous dans les parkings de La Défense ?",
                "Oui, sous réserve que l'accès nous soit ouvert : la plupart des parkings du "
                "quartier demandent un badge ou un accompagnement. Dites-nous le niveau et la "
                "place à la réservation, et prévenez le gardiennage. Notre véhicule passe les "
                "hauteurs limitées habituelles."),
            "nettoyage-canape": (
                "Côté résidentiel, Puteaux mélange des maisons de ville anciennes et des "
                "appartements familiaux. Les canapés y vivent longtemps et se transmettent : "
                "beaucoup de pièces de qualité, parfois retapissées, sur lesquelles une méthode "
                "trop agressive coûte plus cher que la salissure qu'elle enlève.",
                "Nous relevons la matière et l'étiquette avant de commencer, et nous testons sur "
                "une zone cachée. Le cuir et l'alcantara relèvent d'un protocole à pH neutre "
                "appliqué au mousseur, jamais d'une injection-extraction : l'eau en excès est ce "
                "qui craquelle un cuir, pas le produit.",
                "Un canapé en cuir se nettoie-t-il comme un canapé en tissu ?",
                "Non, c'est même l'opposé. Le tissu se traite à l'eau, en injection-extraction. Le "
                "cuir est une peau tannée stabilisée en milieu acide : un produit alcalin attaque "
                "sa finition, et l'eau en excès le raidit. Nous y appliquons un nettoyant à pH "
                "neutre au mousseur, puis un nourrissage."),
            "nettoyage-vitres": (
                "La Défense, ce sont des façades vitrées à perte de vue — mais l'essentiel se "
                "traite en nacelle ou en cordiste, deux métiers réglementés que nous ne pratiquons "
                "pas. Ce que nous faisons, ce sont les rez-de-chaussée, les halls, les vitrines "
                "et les bureaux jusqu'à trois niveaux, depuis le sol.",
                "Nous le disons franchement plutôt que de prendre un chantier que nous ne pourrions "
                "pas tenir. Sur les surfaces accessibles, l'eau osmosée et la perche télescopique "
                "donnent un résultat sans trace, y compris sur les grandes surfaces vitrées des "
                "halls d'immeuble et des commerces de la dalle.",
                "Lavez-vous les vitres des tours de La Défense ?",
                "Non, pas en hauteur : au-delà de trois niveaux il faut une nacelle ou des "
                "cordistes, qui relèvent d'habilitations que nous n'avons pas. Nous prenons en "
                "revanche tout ce qui se traite depuis le sol — halls, rez-de-chaussée, vitrines, "
                "bureaux bas — et nous vous le disons avant, pas pendant."),
            "menage-regulier": (
                "La Défense est le premier quartier d'affaires européen, et la plupart des tours y "
                "ont un prestataire d'entretien en titre. Le besoin que nous couvrons est autre : "
                "l'intervention ponctuelle et rapide qu'un contrat-cadre traite mal — une "
                "moquette de salle de réunion, un plateau avant une visite, une remise à niveau "
                "après un déménagement.",
                "Nous intervenons hors des heures d'ouverture, badge et créneau de livraison "
                "réglés d'avance, avec facturation entreprise. Moquettes en injection-extraction, "
                "sanitaires, cuisines, surfaces de contact et vitrerie accessible. Devis ferme, "
                "sans engagement de durée.",
                "Travaillez-vous avec les contraintes d'accès de La Défense ?",
                "Oui : badge visiteur, quai de livraison, créneau imposé, accompagnement par le "
                "gardiennage. Nous demandons ces éléments au moment du devis pour ne pas les "
                "découvrir sur place. C'est la principale cause de rendez-vous manqué sur ce "
                "quartier, et elle est facile à éviter."),
        },
    },
    {
        "slug": "saint-cloud", "nom": "Saint-Cloud", "cp": "92210",
        "dept": "92", "lat": 48.8456, "lon": 2.2189,
        "profil": "Saint-Cloud est une commune de coteau : des maisons et des hôtels particuliers "
                  "étagés au-dessus de la Seine, de grands jardins, des propriétés anciennes en "
                  "pierre meulière et un parc domanial qui borde la ville. L'habitat individuel "
                  "y domine, avec des extérieurs qui pèsent autant que l'intérieur.",
        "acces": "Les accès sont en pente et souvent étroits, avec des entrées de propriété en "
                 "chicane. Nous venons en véhicule léger et nous déroulons nos tuyaux depuis la "
                 "rue quand l'entrée ne se franchit pas. Prévenez-nous si l'accès est particulier, "
                 "nous adaptons le matériel.",
        "angles": {
            "nettoyage-voiture": (
                "À Saint-Cloud, les voitures dorment souvent dehors ou sous un auvent, à proximité "
                "immédiate d'arbres. C'est la configuration qui produit le plus de dégâts "
                "discrets : résine de platane et de tilleul, fientes, pollen, sève. Autant de "
                "dépôts acides qui marquent le vernis s'ils restent en place.",
                "Nous intervenons à domicile, dans l'allée ou devant le portail, en autonomie "
                "complète. La résine et les fientes se retirent avec un produit dédié et du temps "
                "de pose, jamais au grattage. Un dépôt laissé plusieurs semaines peut avoir "
                "marqué le vernis de façon définitive : nous vous le dirons avant, pas après.",
                "Les taches de résine partent-elles complètement ?",
                "Le plus souvent oui, si elles n'ont pas séjourné des mois. La résine s'enlève au "
                "solvant doux avec un temps de pose, pas à la force du bras. Quand elle a gravé le "
                "vernis — cela arrive après un été entier sous un tilleul — il reste une marque "
                "que seul un polissage peut atténuer. Nous le disons au diagnostic."),
            "nettoyage-canape": (
                "Les maisons clodoaldiennes ont de grands séjours, souvent avec des canapés "
                "anciens ou de bonne facture, et fréquemment des animaux. Le poil et l'odeur "
                "s'installent dans les assises bien avant que le tissu paraisse sale, et "
                "l'aspirateur domestique n'en retire que la couche de surface.",
                "L'injection-extraction va chercher ce qui est logé au cœur de la fibre. Le "
                "retrait des poils est traité en amont, mécaniquement, car ils encrassent "
                "l'extraction. Sur une maison avec animaux, l'association textile plus ozone "
                "donne un résultat que ni l'un ni l'autre n'obtient seul.",
                "Que faire d'un canapé qui sent le chien ?",
                "Deux étapes, dans cet ordre. D'abord l'injection-extraction, qui retire la "
                "matière — sébum, poils, salissure — car tant qu'elle est là, l'odeur revient. "
                "Ensuite seulement l'ozone, qui détruit les molécules odorantes ayant imprégné les "
                "mousses. L'inverse ne tient pas plus de quelques jours."),
            "nettoyage-vitres": (
                "Les maisons de coteau ont souvent de grandes baies orientées vers la vue, des "
                "vérandas et des fenêtres de toit. Ce sont les vitrages les plus exposés : pluie, "
                "poussière, chute de feuilles, et une saleté qui se remarque immédiatement puisque "
                "toute la pièce est tournée vers eux.",
                "L'eau osmosée sèche sans dépôt calcaire, donc sans trace. La perche télescopique "
                "permet de traiter depuis le sol jusqu'à trois niveaux, y compris des vérandas et "
                "des baies difficiles d'accès. Au-delà, ou sur une toiture praticable, nous "
                "renvoyons vers des métiers habilités.",
                "Nettoyez-vous les vérandas et les fenêtres de toit ?",
                "Les vérandas, oui, à l'intérieur comme à l'extérieur, toiture comprise quand elle "
                "se traite depuis le sol à la perche. Les fenêtres de toit se font depuis "
                "l'intérieur, et depuis l'extérieur seulement si l'accès est sûr sans matériel "
                "d'élévation. Nous jugeons sur photos avant de nous engager."),
            "menage-regulier": (
                "Saint-Cloud compte peu de plateaux tertiaires mais beaucoup de professions "
                "libérales installées en maison ou en rez-de-chaussée : cabinets, études, petites "
                "structures. Le local y est souvent l'extension de l'habitation, et se juge avec "
                "la même exigence.",
                "Nous intervenons hors des heures d'ouverture, en ponctuel ou en régulier, avec "
                "facturation entreprise. Moquettes, sols durs, vitrerie, sanitaires et surfaces "
                "de contact. La taille réduite de ces locaux rend le passage régulier "
                "particulièrement efficace : peu de temps, à intervalle court.",
                "Quel rythme pour un cabinet de deux personnes ?",
                "Un passage hebdomadaire suffit généralement, avec une remise à niveau complète "
                "deux fois par an sur les moquettes et la vitrerie. Nous préférons un rythme "
                "tenable à un contrat surdimensionné : c'est plus honnête, et vous gardez du "
                "budget pour les interventions qui comptent vraiment."),
        },
    },
    {
        "slug": "rueil-malmaison", "nom": "Rueil-Malmaison", "cp": "92500",
        "dept": "92", "lat": 48.8768, "lon": 2.1801,
        "profil": "Rueil-Malmaison est l'une des plus vastes communes des Hauts-de-Seine : "
                  "quartiers pavillonnaires étendus, grandes propriétés autour du parc de "
                  "Malmaison, bord de Seine à Bougival et un pôle tertiaire important à "
                  "Rueil-sur-Seine. Beaucoup de maisons avec jardin, garage et extérieurs à "
                  "entretenir.",
        "acces": "L'accès y est le plus simple de notre zone premium : allées privatives, places "
                 "devant la maison, garages. Nous nous garons au plus près et nous travaillons "
                 "sur place. La contrainte est ailleurs : la commune est étendue, il vaut mieux "
                 "regrouper plusieurs prestations sur une même venue.",
        "angles": {
            "nettoyage-voiture": (
                "Les foyers rueillois ont souvent deux véhicules, dont un qui sert peu et reste au "
                "garage ou dans l'allée. C'est celui-là qui pose problème : un habitacle fermé et "
                "peu utilisé développe une odeur de renfermé, et une carrosserie sous les arbres "
                "accumule résine et fientes sans jamais être rincée.",
                "Nous nettoyons les deux voitures sur la même venue, sans que le déplacement soit "
                "facturé deux fois. Intérieur à la vapeur et au pH adapté, extérieur avec séchage "
                "sans trace, et l'option ozone pour le véhicule qui sent le renfermé. Tout se fait "
                "dans votre allée, en autonomie complète.",
                "Peut-on faire nettoyer deux voitures le même jour ?",
                "Oui, et c'est ce que nous recommandons ici : les frais de déplacement ne sont "
                "comptés qu'une fois. Deux Intérieur Essentiel enchaînés tiennent dans une "
                "demi-journée. Nous prévoyons le créneau en conséquence quand vous nous le dites "
                "à la réservation."),
            "nettoyage-canape": (
                "Les maisons rueilloises ont de grands séjours et souvent plusieurs assises : "
                "canapé, fauteuils, banquette, sans compter les matelas à l'étage. Traiter "
                "l'ensemble d'un coup a un intérêt économique direct, puisque le déplacement n'est "
                "compté qu'une fois.",
                "Nous chiffrons à la pièce : chaise 15 €, fauteuil 25 €, canapé 2 places 39 €, "
                "3 places 49 €, angle 69 €, matelas 39 à 49 €. L'injection-extraction et le "
                "traitement anti-acariens s'enchaînent sur la même venue, avec quatre à six heures "
                "de séchage en pièce aérée.",
                "Traitez-vous aussi les matelas des chambres ?",
                "Oui, sur les deux faces, avec un traitement anti-acariens. C'est même l'ajout le "
                "plus fréquent quand nous venons pour un canapé : le matelas est le textile le "
                "plus chargé d'un logement, et il est celui auquel on pense en dernier. Comptez "
                "39 € pour une place, 49 € pour deux."),
            "nettoyage-vitres": (
                "Les maisons rueilloises ont beaucoup d'ouvertures : baies sur jardin, vérandas, "
                "portes-fenêtres, parfois une serre ou un abri de piscine. Le volume vitré y est "
                "sans commune mesure avec un appartement, et un lavage complet représente une "
                "vraie demi-journée.",
                "Nous travaillons à l'eau osmosée, sans calcaire donc sans trace au séchage, avec "
                "une perche télescopique qui couvre jusqu'à trois niveaux depuis le sol. Les "
                "encadrements et les appuis sont repris dans le même passage : c'est de là que "
                "repart la coulure qui salit la vitre à la pluie suivante.",
                "Comment est calculé le prix sur une maison ?",
                "Au vantail, après photos : c'est la seule façon d'être juste, parce qu'une "
                "fenêtre à petits bois demande plusieurs fois le temps d'une baie de même surface. "
                "Nous comptons les ouvrants, nous annonçons un montant ferme, et nous nous y "
                "tenons le jour de l'intervention."),
            "menage-regulier": (
                "Rueil-sur-Seine accueille des sièges et des plateaux tertiaires en bord de Seine, "
                "à côté d'un tissu de PME et de professions libérales réparties dans la commune. "
                "Deux besoins différents : le plateau qui demande une remise à niveau ponctuelle, "
                "et le petit local qui a besoin d'un passage régulier.",
                "Nous prenons les deux, hors des heures d'ouverture, avec facturation entreprise "
                "et sans engagement de durée. Moquettes en injection-extraction, sols durs, "
                "vitrerie jusqu'à trois niveaux, sanitaires, cuisines et surfaces de contact. "
                "Devis ferme établi après visite ou photos.",
                "Faites-vous le nettoyage des vitres d'un bâtiment de bureaux ?",
                "Jusqu'à trois niveaux depuis le sol, oui, à la perche et à l'eau osmosée. "
                "Au-delà, il faut une nacelle ou des cordistes : ce sont des métiers réglementés "
                "que nous ne pratiquons pas, et nous préférons vous le dire au devis plutôt que "
                "de découvrir le problème le jour même."),
        },
    },
    {
        "slug": "versailles", "nom": "Versailles", "cp": "78000",
        "dept": "78", "lat": 48.8014, "lon": 2.1301,
        "profil": "Versailles est une ville de pierre et d'histoire : hôtels particuliers du "
                  "quartier Saint-Louis, immeubles anciens à parquets et cheminées, maisons de "
                  "ville à Montreuil et à Clagny. Beaucoup de biens classés ou en secteur "
                  "protégé, avec les contraintes d'intervention qui vont avec, et un tissu de "
                  "commerces et de professions libérales dense en centre-ville.",
        "acces": "Le centre versaillais est contraint : rues étroites, stationnement réglementé, "
                 "cours intérieures fermées. Nous venons en véhicule léger et nous déroulons "
                 "depuis la rue quand la cour ne s'ouvre pas. Dites-nous si l'immeuble est en "
                 "secteur protégé, cela conditionne le matériel que nous sortons.",
        "angles": {
            "nettoyage-voiture": (
                "À Versailles, beaucoup de véhicules stationnent en rue ou en cour, sous les "
                "arbres des avenues. C'est la configuration qui laisse le plus de traces : "
                "résine, fientes, pollen au printemps, et une carrosserie qui ne sèche jamais "
                "proprement entre deux averses.",
                "Nous intervenons là où le véhicule est garé, y compris en rue, avec notre eau et "
                "notre électricité — aucun branchement à demander à personne. Les dépôts acides "
                "se retirent avec un produit dédié et un temps de pose, jamais au grattage, qui "
                "marquerait le vernis plus sûrement que la fiente elle-même.",
                "Pouvez-vous nettoyer une voiture garée dans la rue ?",
                "Oui, c'est fréquent ici. Il nous faut simplement assez d'espace pour ouvrir les "
                "portes et tourner autour du véhicule. Nous sommes autonomes en eau et en "
                "électricité, et nous travaillons sans écoulement sur la chaussée. Prévoyez que "
                "la place reste libre pendant la durée de l'intervention."),
            "nettoyage-canape": (
                "Les intérieurs versaillais conservent beaucoup de mobilier ancien : canapés à "
                "structure bois, fauteuils tapissés, velours et tissus d'ameublement d'époque. Ce "
                "sont précisément les pièces sur lesquelles une méthode standard fait des dégâts "
                "coûteux — auréoles, rétrécissement, marque de poil.",
                "Nous relevons la matière avant toute chose, et nous testons sur une zone cachée. "
                "Sur un velours ancien, le sens du poil est repéré et respecté au séchage. Sur "
                "une soie ou une viscose, qui perdent leur résistance mouillées, nous préférons "
                "refuser plutôt que de prendre le risque — et nous le disons.",
                "Traitez-vous les fauteuils anciens et les tissus d'époque ?",
                "Avec prudence, et après examen. Beaucoup de tissus anciens supportent une "
                "extraction douce ; certains non, en particulier les soies et les tissus dont la "
                "teinture n'est pas stable. Nous testons systématiquement sur une zone cachée, et "
                "si le test est mauvais, nous nous arrêtons là. Un refus argumenté vaut mieux "
                "qu'une pièce abîmée."),
            "nettoyage-vitres": (
                "Le patrimoine versaillais a conservé énormément de fenêtres à petits bois, de "
                "croisées anciennes et de grandes hauteurs sous plafond. C'est le vitrage le plus "
                "long à traiter correctement : chaque carreau demande son passage, et les mastics "
                "anciens relâchent une poussière qui coule sur la vitre pendant le lavage.",
                "Nous comptons au vantail et non au mètre carré, parce qu'un tarif à la surface "
                "serait faux dans un sens comme dans l'autre sur ce type de menuiserie. L'eau "
                "osmosée sèche sans trace, et les bois et mastics sont repris avec ménagement, "
                "sans détremper une menuiserie ancienne.",
                "Une croisée ancienne supporte-t-elle un lavage à l'eau ?",
                "Oui, si l'on ne la noie pas. Le risque sur une menuiserie ancienne n'est pas "
                "l'eau mais la stagnation : dans une feuillure, elle fait gonfler le bois et "
                "décoller le mastic. Nous travaillons avec peu d'eau et nous essuyons les "
                "feuillures — c'est plus lent, et c'est ce que le bois ancien demande."),
            "menage-regulier": (
                "Le centre de Versailles concentre des commerces, des cabinets et des études "
                "installés dans des immeubles anciens. Les vitrines y comptent double : la "
                "clientèle est passante, et une devanture ternie se remarque dans une rue de "
                "pierre claire.",
                "Nous intervenons avant l'ouverture ou après la fermeture, sans supplément, en "
                "ponctuel ou en régulier. Vitrines, sols, sanitaires et surfaces de contact, avec "
                "facturation entreprise. Sur une devanture commerciale, un passage hebdomadaire "
                "ou bimensuel tient le résultat mieux qu'un grand nettoyage trimestriel.",
                "À quelle fréquence nettoyer une vitrine de commerce ?",
                "Hebdomadaire sur une rue passante, bimensuel sur une rue calme. Une vitrine se "
                "salit par les mains, la pluie et les projections du caniveau, et ces trois "
                "sources agissent en continu. Un rythme court et régulier coûte moins cher et "
                "rend mieux qu'une remise à niveau espacée."),
        },
    },
    {
        "slug": "saint-germain-en-laye", "nom": "Saint-Germain-en-Laye", "cp": "78100",
        "dept": "78", "lat": 48.8989, "lon": 2.0942,
        "profil": "Saint-Germain-en-Laye combine un centre ancien dense autour du château, des "
                  "quartiers pavillonnaires étendus vers la forêt, et de grandes propriétés sur "
                  "les coteaux dominant la Seine. La forêt domaniale, qui borde la ville sur "
                  "presque tout un côté, pèse directement sur l'entretien des extérieurs et des "
                  "véhicules.",
        "acces": "Le centre est contraint, la périphérie pavillonnaire très accessible. Nous "
                 "adaptons le créneau : centre-ville tôt le matin, quartiers résidentiels dans la "
                 "journée. La commune étant étendue, regrouper plusieurs prestations sur une même "
                 "venue change sensiblement le total.",
        "angles": {
            "nettoyage-voiture": (
                "La proximité immédiate de la forêt se voit sur les carrosseries : sève, résine, "
                "pollen au printemps, feuilles et humidité en automne. Un véhicule garé sous les "
                "arbres à Saint-Germain accumule en une saison ce qu'une voiture de ville met "
                "deux ans à prendre.",
                "Nous intervenons à domicile, allée ou garage, en autonomie complète. Les dépôts "
                "acides se retirent avec un produit dédié et un temps de pose, et la carrosserie "
                "reçoit ensuite une protection qui ralentit l'accrochage suivant. Sur un véhicule "
                "sous arbres, c'est ce dernier point qui fait durer le résultat.",
                "À quelle fréquence nettoyer une voiture garée sous les arbres ?",
                "Deux à trois fois par an au minimum, et impérativement après la chute des "
                "feuilles et la période de sève. Le problème n'est pas l'aspect mais le temps de "
                "contact : une résine laissée plusieurs mois grave le vernis, et la marque devient "
                "définitive. Mieux vaut un passage de plus qu'un polissage de rattrapage."),
            "nettoyage-canape": (
                "Les maisons saint-germanoises sont grandes et souvent habitées par des familles "
                "installées de longue date, avec du mobilier de qualité et fréquemment des "
                "animaux. Les assises accumulent poils, sébum et poussière bien avant de paraître "
                "sales, et l'aspirateur n'en retire que la surface.",
                "Nous retirons les poils mécaniquement avant l'extraction — sinon ils encrassent "
                "le matériel et le résultat s'en ressent — puis nous traitons en "
                "injection-extraction avec anti-acariens. Sur plusieurs pièces, le déplacement "
                "n'est facturé qu'une fois : canapé, fauteuils et matelas se font sur la même venue.",
                "Combien coûte le traitement d'un salon complet ?",
                "Comptez le prix des pièces additionnées, plus un seul déplacement : par exemple "
                "un canapé 3 places à 49 €, deux fauteuils à 25 € et un tapis à 39 €, soit 138 € "
                "plus les frais de déplacement. C'est le regroupement qui rend l'intervention "
                "intéressante sur une maison."),
            "nettoyage-vitres": (
                "Les maisons saint-germanoises ont beaucoup de surfaces vitrées tournées vers le "
                "jardin ou la forêt : baies, vérandas, portes-fenêtres. Elles reçoivent le pollen "
                "au printemps et les projections de terre à la pluie, et se salissent plus vite "
                "qu'un vitrage de ville.",
                "L'eau osmosée, déminéralisée, sèche sans trace : c'est ce qui permet de ne pas "
                "essuyer et donc de ne pas laisser de marque de raclette. Perche télescopique "
                "jusqu'à trois niveaux depuis le sol. Les appuis et les encadrements sont repris "
                "dans le même passage, sinon la coulure salit tout à la pluie suivante.",
                "Le pollen laisse-t-il des traces durables sur les vitres ?",
                "Il ne grave pas le verre, mais mélangé à la pluie il forme un film jaunâtre "
                "tenace que le lave-vitre du commerce étale sans retirer. Il faut un lavage "
                "complet à l'eau pure. Au printemps, deux passages rapprochés valent mieux qu'un "
                "seul : le premier retire, le second finit le travail après la fin de l'émission."),
            "menage-regulier": (
                "Le centre de Saint-Germain concentre commerces, cabinets et professions "
                "libérales dans un bâti ancien, souvent en étage. Les locaux y sont de taille "
                "modeste mais très fréquentés, et la vitrine comme la salle d'attente portent "
                "l'essentiel de l'impression.",
                "Nous intervenons hors des heures d'ouverture, sans supplément, en ponctuel ou en "
                "régulier avec facturation entreprise. Sols, moquettes en injection-extraction, "
                "vitrines, sanitaires et surfaces de contact. Sur un local de centre-ville, le "
                "passage court et régulier tient mieux que la remise à niveau espacée.",
                "Intervenez-vous dans un local en étage sans ascenseur ?",
                "Oui. Notre matériel se porte et se démonte : c'est une contrainte de temps, pas "
                "un obstacle. Dites-le-nous au devis pour que nous prévoyions le créneau en "
                "conséquence — c'est plus honnête que de le découvrir sur place et de bâcler la "
                "fin de l'intervention."),
        },
    },
    {
        "slug": "sceaux", "nom": "Sceaux", "cp": "92330",
        "dept": "92", "lat": 48.7789, "lon": 2.2900,
        "profil": "Sceaux est une petite ville résidentielle organisée autour de son parc : "
                  "maisons de ville, villas de la fin du XIXe, immeubles bas et jardins "
                  "nombreux. Une population de cadres et de professions libérales, beaucoup de "
                  "familles installées, et un centre commerçant compact mais actif autour de la "
                  "rue Houdan.",
        "acces": "Les rues sont calmes et le stationnement praticable, ce qui simplifie "
                 "l'intervention. La commune est petite et notre atelier en est éloigné : "
                 "regrouper plusieurs prestations sur une même venue est ici plus qu'ailleurs la "
                 "bonne façon de procéder.",
        "angles": {
            "nettoyage-voiture": (
                "À Sceaux, la voiture reste souvent devant la maison ou dans une allée bordée "
                "d'arbres — le parc et les rues plantées font que peu de véhicules échappent aux "
                "dépôts végétaux. Sève, pollen, fientes et feuilles s'accumulent, et l'habitacle "
                "suit l'humidité ambiante.",
                "Nous nettoyons sur place, dans l'allée ou devant le portail, en autonomie "
                "complète. Intérieur à la vapeur haute température, cuirs au pH neutre et au "
                "mousseur, extérieur avec retrait des dépôts acides par temps de pose et séchage "
                "sans trace. Aucun branchement ne vous est demandé.",
                "Vous déplacez-vous jusqu'à Sceaux pour une seule voiture ?",
                "Oui, mais Sceaux est loin de notre atelier et le déplacement pèse alors dans le "
                "total. Si un voisin ou un proche a le même besoin, ou si vous avez un canapé à "
                "traiter le même jour, le déplacement n'est compté qu'une fois. C'est ce que nous "
                "proposons systématiquement au devis."),
            "nettoyage-canape": (
                "Les maisons scéennes ont des salons de belle taille et du mobilier qui dure : "
                "canapés en tissu épais, fauteuils anciens, tapis. Ce sont des pièces qu'on "
                "entretient plutôt qu'on ne remplace, ce qui rend le nettoyage en profondeur "
                "économiquement évident.",
                "L'injection-extraction retire ce que l'aspirateur laisse : la poussière au cœur "
                "de la fibre, les transferts, les auréoles. Sur un tapis en laine — fréquent "
                "ici — le produit doit rester neutre : la laine est une fibre protéinique que "
                "l'alcalin abîme, ternit et raidit définitivement.",
                "Un tapis en laine peut-il être nettoyé à domicile ?",
                "Oui, à condition d'employer un produit neutre et de maîtriser l'humidité. La "
                "laine est une protéine, comme un cheveu : un produit alcalin la ternit et la "
                "raidit sans retour possible. Nous travaillons à pH neutre, avec une extraction "
                "complète et un séchage surveillé, tapis relevé si nécessaire."),
            "nettoyage-vitres": (
                "Les maisons scéennes ont des vérandas, des baies sur jardin et des fenêtres "
                "anciennes à petits bois selon les quartiers. Le vis-à-vis végétal les salit "
                "vite : pollen, projections de terre à la pluie, résine. Et elles se remarquent, "
                "puisque toutes les pièces de vie sont tournées vers le jardin.",
                "Eau osmosée, sans calcaire donc sans trace au séchage, et perche télescopique "
                "jusqu'à trois niveaux depuis le sol. Nous comptons au vantail, pas au mètre "
                "carré : sur une maison mêlant baies modernes et croisées anciennes, c'est la "
                "seule façon d'établir un prix juste.",
                "Combien de temps faut-il pour les vitres d'une maison ?",
                "Une demi-journée pour une maison de taille courante avec véranda, une journée "
                "si les ouvrants sont nombreux et anciens. Nous comptons les vantaux sur photos "
                "et nous annonçons un montant ferme : vous savez avant que nous venions ce que "
                "cela coûtera et combien de temps nous resterons."),
            "menage-regulier": (
                "Sceaux a un centre commerçant compact et un tissu de professions libérales "
                "installées en rez-de-chaussée ou en maison. Les surfaces sont petites, la "
                "fréquentation forte, et l'exigence d'aspect élevée dans une ville où tout se "
                "voit.",
                "Nous intervenons avant l'ouverture ou après la fermeture, sans supplément, en "
                "ponctuel ou en régulier avec facturation entreprise. Vitrines, sols, moquettes "
                "en injection-extraction, sanitaires et surfaces de contact. Sans engagement de "
                "durée : si le service ne convient pas, vous arrêtez.",
                "Proposez-vous un contrat d'entretien pour un petit commerce ?",
                "Oui, avec un rythme adapté à la surface plutôt qu'un forfait standard. Sur un "
                "commerce de centre-ville, un passage hebdomadaire sur les vitrines et les sols, "
                "plus une remise à niveau semestrielle sur les moquettes, couvre l'essentiel. "
                "Nous préférons un contrat tenable à un contrat surdimensionné."),
        },
    },
    {
        "slug": "le-vesinet", "nom": "Le Vésinet", "cp": "78110",
        "dept": "78", "lat": 48.8925, "lon": 2.1330,
        "profil": "Le Vésinet est une ville-parc, dessinée au XIXe autour de ses lacs et de ses "
                  "rivières artificielles : des villas sur de grandes parcelles arborées, presque "
                  "pas d'immeubles, et une réglementation qui protège le paysage. Un habitat "
                  "individuel de bout en bout, avec des extérieurs qui pèsent lourd dans "
                  "l'entretien.",
        "acces": "Les propriétés ont des allées privatives et de la place : l'accès est le plus "
                 "confortable de notre zone. En contrepartie, la commune est loin de notre "
                 "atelier et les parcelles sont grandes — le temps sur place et le déplacement "
                 "comptent tous les deux dans le devis.",
        "angles": {
            "nettoyage-voiture": (
                "Au Vésinet, presque toutes les voitures stationnent sous les arbres : c'est le "
                "principe même de la ville-parc. Sève de tilleul et de platane, pollen, fientes, "
                "feuilles en automne — les dépôts sont constants, et ce sont eux, bien plus que "
                "la poussière de route, qui abîment le vernis.",
                "Nous intervenons dans l'allée, en autonomie complète. Les dépôts acides se "
                "retirent avec un produit dédié et un temps de pose, jamais au grattage. La "
                "protection appliquée ensuite ralentit l'accrochage suivant : sur un véhicule "
                "garé en permanence sous les arbres, c'est ce qui fait durer le résultat.",
                "La sève peut-elle marquer définitivement la peinture ?",
                "Oui, si elle reste des mois. La sève est acide : elle attaque le vernis et finit "
                "par le graver, laissant une marque en creux qu'aucun lavage ne retire. Prise à "
                "temps, elle s'enlève entièrement. C'est la raison pour laquelle nous "
                "recommandons ici deux à trois passages par an plutôt qu'un seul."),
            "nettoyage-canape": (
                "Les villas vésigondines ont de grands volumes et du mobilier en conséquence : "
                "canapés d'angle, plusieurs fauteuils, tapis, sans compter les matelas. Traiter "
                "l'ensemble en une venue est ici la seule approche raisonnable, la commune étant "
                "éloignée de notre atelier.",
                "Nous chiffrons à la pièce et le déplacement n'est compté qu'une fois : chaise "
                "15 €, fauteuil 25 €, canapé 2 places 39 €, 3 places 49 €, angle 69 €, matelas "
                "39 à 49 €, tapis 39 à 59 €. Injection-extraction et traitement anti-acariens "
                "s'enchaînent sur la même intervention.",
                "Peut-on traiter tout le mobilier textile d'une maison en une journée ?",
                "Oui dans la plupart des cas : un salon complet et trois ou quatre matelas "
                "tiennent dans une journée. Le facteur limitant n'est pas notre temps mais le "
                "séchage — quatre à six heures par pièce en pièce aérée. Nous organisons l'ordre "
                "des pièces pour que tout soit sec le soir."),
            "nettoyage-vitres": (
                "Les villas du Vésinet ont d'immenses surfaces vitrées tournées vers le parc, "
                "souvent avec des vérandas et des jardins d'hiver. Le couvert végétal les salit "
                "en continu : pollen, sève, projections de terre. Et comme toute la maison est "
                "tournée vers l'extérieur, la moindre trace se voit.",
                "Eau osmosée pour un séchage sans dépôt, perche télescopique jusqu'à trois "
                "niveaux depuis le sol, encadrements et appuis repris dans le même passage. Sur "
                "une véranda, la toiture se traite quand elle est accessible à la perche ; "
                "au-delà, nous renvoyons vers des métiers habilités.",
                "Nettoyez-vous les toitures de véranda ?",
                "Oui quand elles se traitent depuis le sol à la perche télescopique, ce qui "
                "couvre la majorité des vérandas de plain-pied. Si l'accès impose de monter sur "
                "la structure ou d'utiliser une nacelle, nous ne le faisons pas : c'est une "
                "question de sécurité, et nous préférons le dire au devis."),
            "menage-regulier": (
                "Le Vésinet compte peu de bureaux et beaucoup de professions libérales installées "
                "chez elles : cabinets médicaux, praticiens, professions du conseil recevant à "
                "domicile. Le local professionnel y est souvent une partie de la villa, et se "
                "juge avec la même exigence que le reste de la maison.",
                "Nous intervenons hors des heures de consultation, sans supplément, en ponctuel "
                "ou en régulier avec facturation entreprise. Sols, moquettes, vitrerie, "
                "sanitaires et surfaces de contact. Précisons-le : nous faisons du nettoyage "
                "professionnel soigné, pas de la désinfection réglementée de dispositif médical.",
                "Peut-on facturer à l'entreprise une intervention à domicile ?",
                "Oui, sur la partie professionnelle du local, avec une facture au nom de la "
                "structure. C'est un cas courant chez les praticiens installés chez eux. Nous "
                "distinguons alors clairement au devis ce qui relève du professionnel et ce qui "
                "relève du privé, pour que votre comptabilité s'y retrouve."),
        },
    },
]


# --- Porte d'entrée : particulier ou professionnel -------------------------
# Le site s'ouvre sur ce choix. Les deux parcours montrent les mêmes
# prestations, mais ne répondent pas aux mêmes questions : un particulier
# veut savoir s'il peut faire confiance et combien ça coûte, une entreprise
# veut savoir qui vient, quand, et sur quoi elle s'engage.
PORTES = [
    {
        "cle": "particulier",
        "titre": "Un particulier",
        "sous": "Chez vous, à domicile",
        "photo": "canape-nettoyage.webp",
        "taille": (1125, 1500),
        "position": "center 60%",
        "page": "particuliers",
        "points": ["Prix affichés, sans acompte",
                   "Réservation en ligne en 2 minutes",
                   "7 j/7, soirs et week-ends"],
        "bouton": "Voir les prestations et les prix",
    },
    {
        "cle": "professionnel",
        "titre": "Un professionnel",
        "sous": "Bureaux, commerces, restaurants, agences",
        # PHOTO À REMPLACER EN PRIORITÉ : 506 × 216 px, c'est le cliché le
        # plus petit de la photothèque et il ouvre désormais le parcours
        # professionnel. Une photo nette de bureaux ou d'une vitrine, prise
        # en 1500 px de large minimum, changerait la première impression.
        "photo": "bureau-entreprise.webp",
        "taille": (506, 216),
        "position": "center 45%",
        "page": "professionnels",
        "points": ["Un interlocuteur unique, qui exécute lui-même",
                   "Horaires décalés, sans gêner votre activité",
                   "Devis ferme et facturation entreprise"],
        "bouton": "Voir l'offre professionnelle",
    },
]

# Qualification du dirigeant. Elle est mise en avant côté professionnel,
# où elle pèse davantage que n'importe quel argument commercial.
#
# À COMPLÉTER : remplacer "intitule" par le libellé exact du diplôme (CAP ou
# BAC pro hygiène-propreté-stérilisation, CQP agent de propreté, titre
# professionnel…). Un intitulé précis, avec l'année, vaut beaucoup plus
# qu'une mention générique face à un acheteur professionnel, qui peut
# demander le justificatif.
QUALIFICATION = {
    "intitule": "Diplôme d'État",
    "annee": "",
    "resume": "Formation initiale en hygiène et propreté, sanctionnée par un diplôme d'État.",
}

# Secteurs pour lesquels nous sommes déjà intervenus. Les enseignes ne sont
# pas nommées : nous n'avons pas leur autorisation écrite, et une référence
# citée sans accord se retourne contre celui qui la cite.
REFERENCES_PRO = [
    ("building", "Agences immobilières",
     "Remises en état entre deux locataires, états des lieux, vitrines d'agence. "
     "Le délai compte plus que tout : un logement propre est un logement qui se reloue."),
    ("tools", "Chaînes de restauration",
     "Salles, banquettes, vitrines et sols, sur des établissements implantés dans "
     "plusieurs villes de France. Intervention avant l'ouverture ou après la fermeture."),
    ("sofa", "Bureaux et locaux d'activité",
     "Postes de travail, salles de réunion, moquettes en injection-extraction et "
     "sanitaires, en passage régulier ou ponctuel."),
]

# Ce qu'une entreprise demande avant de signer, dans l'ordre où elle le demande.
ARGUMENTS_PRO = [
    ("Vous savez qui vient", "C'est toujours la même personne", "%s intervient lui-même sur chaque chantier. Pas de rotation d'intervenants, pas de sous-traitance en cascade, pas de brief à refaire à chaque passage."),
    ("Vous savez quand", "Avant l'ouverture, après la fermeture, le week-end", "Sans supplément. C'est la seule façon de travailler correctement sur un site occupé — et cela vaut aussi pour une extraction de moquette, qui demande plusieurs heures de séchage."),
    ("Vous savez sur quoi", "Devis ferme, détaillé poste par poste", "Chaque prestation, sa durée estimée, son prix. Le montant annoncé est celui que vous réglez, et nous indiquons le temps de présence par passage — la seule donnée qui remette deux devis sur la même échelle."),
    ("Vous savez avec quoi", "Machines, produits, eau et électricité fournis", "Aucun accès technique à prévoir de votre côté. Nous travaillons en parking souterrain comme en étage, en autonomie complète."),
]


# ===========================================================================
# SECTEURS — dégraissage de hottes
# ===========================================================================
# Chaque métier encrasse sa hotte différemment : ce n'est pas la même graisse,
# ni le même rythme, ni les mêmes horaires d'intervention. Ces différences
# sont réelles et techniques — ce sont elles qui font que ces pages ne sont
# pas quatorze fois la même.
#
# Cadre réglementaire commun, cité tel quel : arrêté du 25 juin 1980,
# article GC 21 (ERP). Ramonage des conduits d'évacuation et vérification de
# leur vacuité au moins une fois par an ; filtres nettoyés ou remplacés au
# moins une fois par semaine ; livret d'entretien annexé au registre de
# sécurité, où l'exploitant note les dates.
SECTEURS_HOTTE = [
    {
        "slug": "boulangerie",
        "nom": "boulangerie",
        "nom_long": "boulangerie-pâtisserie",
        "le": "une boulangerie",
        "dans": "en boulangerie",
        "depot": "Farine et matière grasse mêlées",
        "probleme":
            "Une boulangerie produit un encrassement que les autres métiers ne connaissent pas : la farine en suspension se colle "
            "au gras de beurre vaporisé par les fours et forme une croûte dense, qui durcit en séchant. Ce dépôt ne coule pas comme "
            "une graisse de friture — il s'accroche, et un chiffon passe dessus sans rien enlever.",
        "detail":
            "Le point sensible est la zone au-dessus du four rotatif, là où les buées sucrées condensent. Le sucre caramélise sur les "
            "parois chaudes et se mêle à la croûte de farine : il faut un alcalin à temps de pose, pas un dégraissant ménager.",
        "rythme":
            "Deux passages par an suffisent dans la plupart des boulangeries, le minimum réglementaire étant d'un ramonage annuel. "
            "Les filtres, eux, se nettoient chaque semaine et c'est le fournil qui s'en charge.",
        "contrainte":
            "Le fournil tourne la nuit, la vente le jour : la fenêtre est étroite. Nous intervenons l'après-midi, entre la fin de la "
            "cuisson et la reprise du tour de nuit, ou le jour de fermeture.",
        "faq": ("La farine change-t-elle vraiment quelque chose au nettoyage ?",
                "Oui, et c'est ce que les prestataires généralistes sous-estiment. Mêlée au gras, elle forme une croûte qui ne réagit "
                "pas comme un dépôt de friture : il faut un produit alcalin avec un vrai temps de pose, puis une action mécanique. "
                "Un passage rapide au dégraissant laisse une couche intacte sous la surface nettoyée."),
    },
    {
        "slug": "restaurant",
        "nom": "restaurant",
        "nom_long": "restaurant traditionnel",
        "le": "un restaurant",
        "dans": "en restaurant",
        "depot": "Graisse de cuisson mixte",
        "probleme":
            "Un restaurant traditionnel cumule tous les modes de cuisson : sauteuse, grillade, friteuse d'appoint, four. Le dépôt est "
            "hétérogène, plus gras au-dessus du piano, plus sec vers l'entrée du conduit, et c'est précisément cette variété qui le "
            "rend difficile à traiter d'un seul produit.",
        "detail":
            "La zone critique est le coude de départ du conduit, juste après la hotte. La vitesse d'air y chute, les gouttelettes "
            "condensent, et c'est là que l'épaisseur s'accumule le plus vite — souvent hors de vue, donc hors de contrôle.",
        "rythme":
            "Un à deux passages par an selon le volume de couverts, avec le ramonage annuel des conduits comme plancher réglementaire. "
            "Au-delà de cent couverts par service, deux passages sont le bon rythme.",
        "contrainte":
            "Intervention après le dernier service ou avant l'ouverture, de nuit si besoin. La cuisine doit être opérationnelle pour "
            "le service suivant : le remontage et l'essai d'extraction font partie de l'intervention, pas de la suite.",
        "faq": ("Mon extraction tire moins qu'avant, est-ce lié ?",
                "Très probablement. Un conduit encrassé perd de la section utile, et le débit chute proportionnellement. C'est "
                "progressif, donc invisible au quotidien — jusqu'à ce que les buées restent en salle et que la cuisine devienne "
                "difficilement tenable aux heures de pointe."),
    },
    {
        "slug": "pizzeria",
        "nom": "pizzeria",
        "nom_long": "pizzeria et four à bois",
        "le": "une pizzeria",
        "dans": "en pizzeria",
        "depot": "Suie et graisse combinées",
        "probleme":
            "C'est le cas le plus à risque. Un four à bois produit de la suie, qui vient s'ajouter à la graisse des garnitures : "
            "deux combustibles dans le même conduit, dont l'un s'enflamme à basse température. Un feu de conduit en pizzeria se "
            "propage plus vite qu'ailleurs, et c'est pour cela que l'intervalle entre deux nettoyages doit y être plus court.",
        "detail":
            "Le conduit d'un four à bois demande en outre un vrai ramonage mécanique, pas seulement un dégraissage chimique : la suie "
            "ne se dissout pas, elle se décolle. Les deux opérations sont distinctes et toutes deux nécessaires.",
        "rythme":
            "Deux passages par an au minimum, trois si le four tourne tous les jours. Le ramonage annuel des conduits d'évacuation "
            "est une obligation, pas une recommandation.",
        "contrainte":
            "Le four doit être froid, ce qui impose d'intervenir au moins douze heures après la dernière cuisson. Le jour de "
            "fermeture est presque toujours le bon créneau.",
        "faq": ("Faut-il ramoner le conduit du four à bois séparément ?",
                "Oui. Le conduit de fumée du four et le conduit d'extraction de la hotte sont deux circuits différents, avec deux "
                "encrassements différents. Le premier relève du ramonage, le second du dégraissage. Traiter l'un en croyant avoir "
                "fait l'autre est l'erreur la plus fréquente en pizzeria."),
    },
    {
        "slug": "restaurant-asiatique",
        "nom": "restaurant asiatique",
        "nom_long": "restaurant asiatique et cuisine au wok",
        "le": "un restaurant asiatique",
        "dans": "en cuisine au wok",
        "depot": "Aérosol d'huile à haute température",
        "probleme":
            "Le wok cuit à très haute température, et projette un aérosol d'huile extrêmement fin qui est aspiré avant de pouvoir "
            "retomber. Ce brouillard se dépose loin dans le conduit, bien au-delà de ce qu'un service classique atteint, et il "
            "polymérise sur les parois chaudes en un film dur que seul un alcalin à temps de pose décolle.",
        "detail":
            "Conséquence pratique : sur une cuisine au wok, nettoyer la hotte sans remonter dans le conduit ne sert presque à rien. "
            "L'essentiel du dépôt est à plusieurs mètres de la bouche d'aspiration.",
        "rythme":
            "Trois passages par an sont souvent nécessaires, et c'est le métier où l'écart entre le minimum réglementaire annuel et "
            "le rythme réellement utile est le plus grand.",
        "contrainte":
            "Service continu dans beaucoup d'établissements : l'intervention se cale de nuit, après la fermeture, avec remise en "
            "service le matin.",
        "faq": ("Pourquoi faut-il nettoyer plus souvent qu'un autre restaurant ?",
                "Parce que la température de cuisson au wok transforme l'huile en aérosol au lieu de la laisser en gouttelettes. "
                "Le dépôt se forme plus vite, plus loin dans le circuit, et il durcit en polymérisant. À volume de couverts égal, "
                "une cuisine au wok encrasse un conduit deux à trois fois plus vite."),
    },
    {
        "slug": "kebab-grillades",
        "nom": "kebab et grillades",
        "nom_long": "kebab, grillades et broche verticale",
        "le": "un kebab",
        "dans": "en grillades",
        "depot": "Graisse animale qui fige",
        "probleme":
            "La broche verticale fait fondre une graisse animale qui se vaporise puis refige dès qu'elle rencontre une paroi plus "
            "froide. Le dépôt est épais, cireux, et il s'accumule très vite au-dessus de la broche — c'est l'un des encrassements "
            "les plus rapides de la restauration.",
        "detail":
            "La graisse figée piège en plus les particules de combustion du grill, ce qui donne une couche dense et noire, "
            "franchement combustible. Une intervention tardive demande le double de temps d'une intervention à l'heure.",
        "rythme":
            "Deux à trois passages par an, le ramonage annuel des conduits restant le minimum légal. Les filtres se rincent "
            "chaque semaine et il ne faut pas les sauter.",
        "contrainte":
            "Amplitude horaire large, souvent jusqu'à tard : l'intervention se fait de nuit ou en début de matinée.",
        "faq": ("Les filtres suffisent-ils si on les change souvent ?",
                "Non. Les filtres retiennent une part des grosses gouttelettes, pas la vapeur grasse qui passe à travers et se "
                "condense plus haut. Changer les filtres est nécessaire — l'arrêté l'impose chaque semaine — mais cela ne dispense "
                "jamais du dégraissage du conduit."),
    },
    {
        "slug": "brasserie",
        "nom": "brasserie",
        "nom_long": "brasserie et service continu",
        "le": "une brasserie",
        "dans": "en brasserie",
        "depot": "Volume élevé, service continu",
        "probleme":
            "Ce n'est pas la nature de la graisse qui pose problème en brasserie, c'est la durée d'exposition. Une cuisine qui tourne "
            "de 11 h à 23 h sans interruption encrasse son circuit deux fois plus vite qu'une cuisine à deux services, à carte "
            "équivalente. Le calcul de fréquence se fait sur les heures de cuisson, pas sur les couverts.",
        "detail":
            "Les brasseries ont souvent de longs conduits, parce que la cuisine est en sous-sol ou en arrière-salle. Plus le conduit "
            "est long, plus les trappes de visite comptent : sans elles, la moitié du circuit reste inaccessible.",
        "rythme":
            "Deux passages par an, parfois trois sur les établissements à forte amplitude. Ramonage annuel obligatoire.",
        "contrainte":
            "La fermeture est courte, parfois nulle. Nous intervenons de nuit, et nous découpons si nécessaire le chantier en deux "
            "nuits pour que le service ne soit jamais compromis.",
        "faq": ("Peut-on nettoyer en deux fois pour ne pas fermer ?",
                "Oui, c'est fréquent en brasserie. On traite la hotte et les filtres une nuit, le conduit et le ventilateur la "
                "suivante. Le service n'est jamais interrompu, et le surcoût est nul : c'est le même temps de travail, réparti."),
    },
    {
        "slug": "friterie-snack",
        "nom": "friterie et snack",
        "nom_long": "friterie, snack et restauration rapide",
        "le": "une friterie",
        "dans": "en friterie",
        "depot": "Huile de friture vaporisée",
        "probleme":
            "Une friteuse en service continu vaporise de l'huile en permanence. Le dépôt est liquide à chaud, et se fige en film "
            "collant en refroidissant : il coule le long des parois et s'accumule au point bas du conduit, où il forme une réserve "
            "qui s'enflamme particulièrement bien.",
        "detail":
            "Le point bas du conduit et le bac à graisse sont les deux zones à vérifier en priorité. Un bac plein qui déborde "
            "renvoie la graisse dans la gaine, et annule le bénéfice du dernier nettoyage.",
        "rythme":
            "Deux à trois passages par an. Le bac à graisse, lui, se vide beaucoup plus souvent — c'est une opération d'exploitation, "
            "pas d'entretien annuel.",
        "contrainte":
            "Amplitude large et fermeture tardive : intervention de nuit ou le jour de repos hebdomadaire.",
        "faq": ("À quoi sert exactement le bac à graisse ?",
                "À recueillir ce qui se condense dans la hotte avant que cela ne parte dans le conduit. Quand il est plein, il ne "
                "recueille plus rien : la graisse poursuit sa route et se dépose dans la gaine. Un bac négligé coûte toujours plus "
                "cher en nettoyage de conduit qu'il n'aurait coûté en vidanges."),
    },
    {
        "slug": "boucherie-charcuterie",
        "nom": "boucherie-charcuterie",
        "nom_long": "boucherie, charcuterie et rôtissoire",
        "le": "une boucherie",
        "dans": "en boucherie",
        "depot": "Graisse de rôtissage",
        "probleme":
            "La rôtissoire produit une graisse animale très fluide à chaud qui se dépose en nappes. Elle se charge des jus de "
            "cuisson et devient rapidement odorante : l'odeur de rance au-dessus d'un rayon est presque toujours le signe d'un "
            "circuit d'extraction saturé, pas d'un produit en vitrine.",
        "detail":
            "La proximité du rayon vente impose une contrainte supplémentaire : aucun produit ne doit se retrouver à proximité des "
            "denrées. Le bâchage et le rinçage sont ici aussi importants que le dégraissage lui-même.",
        "rythme":
            "Deux passages par an si la rôtissoire tourne en continu, un seul sinon, le ramonage annuel restant obligatoire.",
        "contrainte":
            "Intervention après fermeture, avec protection complète du rayon et des plans de découpe.",
        "faq": ("L'odeur de rance peut-elle venir de la hotte ?",
                "Oui, et c'est le cas le plus fréquent. La graisse déposée dans le circuit s'oxyde avec le temps et dégage une "
                "odeur caractéristique que la ventilation redistribue dans le magasin. Nettoyer le circuit règle le problème que "
                "ni les désodorisants ni un nettoyage de surface ne traitent."),
    },
    {
        "slug": "traiteur",
        "nom": "traiteur",
        "nom_long": "traiteur et laboratoire de production",
        "le": "un traiteur",
        "dans": "en laboratoire",
        "depot": "Production concentrée",
        "probleme":
            "Un laboratoire de traiteur cuisine par séries : des journées très chargées, des journées creuses. L'encrassement se "
            "fait par à-coups, et une fréquence calée sur un calendrier fixe tombe souvent à côté. Le bon repère est le volume "
            "produit, pas le nombre de semaines écoulées.",
        "detail":
            "Les laboratoires ont souvent plusieurs postes de cuisson sous une même extraction. Le circuit reçoit alors la somme "
            "des dépôts, et vieillit plus vite que ce que chaque poste laisserait supposer pris isolément.",
        "rythme":
            "Deux passages par an sur une production régulière, avec un passage supplémentaire après une grosse saison.",
        "contrainte":
            "Pas de service en salle, donc une liberté d'horaires rare dans ce métier : nous intervenons en journée creuse, ce qui "
            "simplifie tout.",
        "faq": ("Comment savoir si la fréquence est la bonne ?",
                "En regardant l'épaisseur relevée au passage précédent. Nous photographions les mêmes points à chaque "
                "intervention : si le dépôt revient plus vite que prévu, on rapproche ; s'il est léger, on espace. C'est une "
                "donnée mesurée, pas une estimation commerciale."),
    },
    {
        "slug": "restauration-collective",
        "nom": "restauration collective",
        "nom_long": "cantine et restauration collective",
        "le": "une cantine",
        "dans": "en restauration collective",
        "depot": "Gros volumes, créneaux courts",
        "probleme":
            "Une cuisine de collectivité produit beaucoup en très peu de temps, souvent sur des équipements puissants : marmites, "
            "sauteuses basculantes, fours mixtes. L'extraction est dimensionnée en conséquence, et le circuit est long. C'est le "
            "cas où l'accessibilité des trappes de visite détermine la qualité réelle du nettoyage.",
        "detail":
            "Les établissements scolaires et les structures d'accueil ont un avantage : les vacances offrent des fenêtres "
            "d'intervention longues, pendant lesquelles un circuit entier se traite d'un seul tenant.",
        "rythme":
            "Un à deux passages par an selon les volumes, calés sur les périodes de fermeture. Ramonage annuel obligatoire.",
        "contrainte":
            "Intervention pendant les vacances ou les jours de fermeture. Le planning se cale plusieurs semaines à l'avance, et "
            "nous le tenons.",
        "faq": ("Peut-on intervenir pendant les vacances scolaires ?",
                "C'est même le meilleur moment : la cuisine est vide, le circuit se traite d'un bout à l'autre sans contrainte "
                "d'horaire, et la remise en service se fait tranquillement avant la rentrée. Ces créneaux se réservent tôt."),
    },
    {
        "slug": "hotel-restaurant",
        "nom": "hôtel-restaurant",
        "nom_long": "hôtel avec restaurant",
        "le": "un hôtel-restaurant",
        "dans": "en hôtellerie",
        "depot": "Service étalé, clients sur place",
        "probleme":
            "La difficulté n'est pas technique mais logistique : des clients dorment au-dessus de la cuisine. Le bruit du nettoyage "
            "haute pression et les odeurs de produit sont incompatibles avec des chambres occupées, et aucune fenêtre n'est "
            "vraiment libre.",
        "detail":
            "La solution tient au séquençage : les opérations bruyantes en fin de soirée, le travail silencieux de nuit, le "
            "remontage au petit matin avant le service du petit-déjeuner.",
        "rythme":
            "Un à deux passages par an selon l'activité de la table, le ramonage annuel restant le socle.",
        "contrainte":
            "Chantier découpé pour tenir compte des chambres occupées, et planning validé avec la réception avant intervention.",
        "faq": ("Le nettoyage dérange-t-il les chambres ?",
                "Pas si l'on découpe correctement. Nous plaçons les opérations bruyantes avant la nuit, et nous gardons pour les "
                "heures creuses ce qui se fait sans bruit. C'est une question d'organisation, et elle se règle au moment du devis."),
    },
    {
        "slug": "creperie",
        "nom": "crêperie",
        "nom_long": "crêperie et billig",
        "le": "une crêperie",
        "dans": "en crêperie",
        "depot": "Beurre vaporisé",
        "probleme":
            "Le billig travaille à température constante et vaporise du beurre en continu. Le dépôt est fin mais régulier, et il "
            "s'accompagne de particules de pâte brûlée qui s'y collent. Le mélange devient brun et dur en quelques mois.",
        "detail":
            "Les crêperies ont souvent plusieurs billigs alignés sous une même hotte courte, ce qui concentre tout le dépôt sur un "
            "faible linéaire. La hotte sature avant le conduit, et un nettoyage de hotte seul peut suffire plus longtemps "
            "qu'ailleurs — mais jamais au-delà du ramonage annuel du conduit.",
        "rythme":
            "Un à deux passages par an, avec le ramonage annuel des conduits comme obligation.",
        "contrainte":
            "Fermeture hebdomadaire généralement respectée : c'est le créneau naturel.",
        "faq": ("Le beurre encrasse-t-il moins que l'huile ?",
                "Il encrasse différemment. Le beurre laisse un dépôt plus fin mais qui brunit et durcit en cuisant sur les parois "
                "chaudes. Après quelques mois, il demande autant de temps de pose qu'une graisse de friture — simplement, il se "
                "voit moins venir."),
    },
    {
        "slug": "food-truck",
        "nom": "food truck",
        "nom_long": "food truck et cuisine mobile",
        "le": "un food truck",
        "dans": "en cuisine mobile",
        "depot": "Extraction compacte et saturée",
        "probleme":
            "Une cuisine mobile concentre une puissance de cuisson réelle dans un volume minuscule, avec une extraction courte et "
            "sous-dimensionnée par construction. Le circuit sature vite, et le moindre dépôt ampute un débit déjà juste.",
        "detail":
            "L'avantage est que tout est accessible : pas de gaine encastrée, pas de trappe à chercher. Une intervention complète "
            "prend beaucoup moins de temps que sur une cuisine fixe, et coûte donc moins cher.",
        "rythme":
            "Deux à trois passages par an selon le nombre de services, le circuit étant court et donc vite saturé.",
        "contrainte":
            "Intervention sur votre lieu de stationnement, en autonomie complète d'eau et d'électricité : nous n'avons besoin "
            "d'aucun raccordement sur place. À noter : une cuisine installée dans un module ou un "
            "conteneur spécialisé relève de l'article GC 18 de l'arrêté du 25 juin 1980 pour ses "
            "conditions d'installation — un article distinct de GC 21 et GC 22, qui eux portent "
            "sur l'entretien et la vérification.",
        "faq": ("Faut-il amener le camion quelque part ?",
                "Non. Nous venons là où il stationne, avec notre eau et notre électricité. C'est précisément le mode de travail "
                "que nous pratiquons sur toutes nos autres prestations."),
    },
    {
        "slug": "dark-kitchen",
        "nom": "dark kitchen",
        "nom_long": "dark kitchen et cuisine de livraison",
        "le": "une dark kitchen",
        "dans": "en cuisine de livraison",
        "depot": "Plusieurs cuisines, un seul conduit",
        "probleme":
            "Une dark kitchen fait tourner plusieurs enseignes, parfois plusieurs modes de cuisson, sur un circuit d'extraction "
            "souvent mutualisé. Le conduit reçoit la somme de tous les dépôts, et personne ne se sent responsable de son entretien "
            "— chaque exploitant pensant que c'est l'affaire du voisin ou du bailleur.",
        "detail":
            "La première question à régler n'est pas technique mais contractuelle : qui entretient le circuit commun. Tant qu'elle "
            "n'est pas tranchée, le conduit n'est nettoyé par personne, et c'est l'un des cas les plus dégradés que l'on rencontre.",
        "rythme":
            "Deux à trois passages par an sur un circuit mutualisé, avec un relevé partagé entre les exploitants.",
        "contrainte":
            "Activité quasi continue, pics le soir et le week-end : intervention de nuit en semaine, coordonnée entre les enseignes.",
        "faq": ("Qui doit payer le nettoyage d'un conduit partagé ?",
                "Cela dépend du bail, et c'est à vérifier avant tout. En pratique, le plus simple est une intervention unique "
                "refacturée au prorata entre exploitants : le circuit est traité d'un bout à l'autre, ce qui est la seule façon "
                "efficace de le faire, et chacun paie sa part."),
    },
]


# ---------------------------------------------------------------------------
# VITRERIE PAR SECTEUR D'ACTIVITÉ
# ---------------------------------------------------------------------------
# Même principe que SECTEURS_HOTTE : ce qui distingue ces pages, c'est le
# problème technique propre au métier, pas une variation de vocabulaire. Une
# vitrine de boulangerie et une vitrine de pharmacie ne se salissent pas de la
# même façon, ne se nettoient pas au même rythme et ne se comptent pas pareil.
#
# Deux faits techniques reviennent partout et sont vrais partout :
# l'eau du réseau francilien est calcaire, et c'est le calcaire — non la
# saleté — qui laisse la trace blanche au séchage ; et une vitrine de rue
# reçoit en plus les particules de freinage et les hydrocarbures du trafic,
# qui sont grasses et ne partent pas à l'eau claire.
SECTEURS_VITRES = [
    {
        "slug": "boulangerie",
        "nom": "boulangerie",
        "nom_long": "boulangerie-pâtisserie",
        "le": "une boulangerie",
        "dans": "en boulangerie",
        "enjeu": "La vitrine vend avant le pain",
        "probleme":
            "Une vitrine de boulangerie se salit des deux côtés, et le côté intérieur est le plus "
            "difficile. Les buées de cuisson déposent un film de gras sucré sur le verre : il est "
            "invisible de face, mais il diffuse la lumière et éteint la couleur des produits en "
            "vitrine. C'est la raison pour laquelle une boulangerie propre peut paraître terne.",
        "detail":
            "Ce film gras ne part pas à la raclette seule : il demande un dégraissage préalable, puis "
            "un rinçage à l'eau déminéralisée. À l'extérieur, les traces de doigts à hauteur de "
            "poignée et les projections au ras du trottoir reviennent en deux jours — ce sont les "
            "deux zones à reprendre entre deux passages complets.",
        "rythme_court": "Hebdomadaire",
        "rythme":
            "Un passage hebdomadaire ou bimensuel sur la vitrine, mensuel sur l'ensemble des "
            "surfaces vitrées, y compris la façade haute et l'enseigne.",
        "contrainte":
            "Nous intervenons avant l'ouverture, entre 6 h et 7 h 30 : le verre est encore froid, le "
            "séchage est régulier, et aucun client ne traverse le chantier.",
        "faq": ("Pourquoi ma vitrine reste-t-elle voilée après nettoyage ?",
                "Parce que le film gras intérieur n'a pas été dégraissé avant d'être lavé. Un produit "
                "à vitres classique l'étale au lieu de le dissoudre : le verre paraît propre de près "
                "et reste voilé de loin. Il faut un dégraissant alcalin, puis un rinçage à l'eau "
                "déminéralisée qui sèche sans dépôt."),
    },
    {
        "slug": "restaurant",
        "nom": "restaurant",
        "nom_long": "restaurant et brasserie",
        "le": "un restaurant",
        "dans": "en restaurant",
        "enjeu": "Ce que le passant voit avant d'entrer",
        "probleme":
            "Une devanture de restaurant cumule la condensation intérieure des heures de service, les "
            "traces de mains sur les portes vitrées et, en terrasse, les projections de boissons au "
            "bas des vitrages. Les baies de grande hauteur ajoutent un problème de séchage : lavées "
            "en plein soleil, elles sèchent plus vite que la raclette ne descend.",
        "detail":
            "Les menuiseries aluminium noires, très répandues sur les devantures récentes, sont la "
            "difficulté réelle : elles gardent la trace d'eau calcaire comme aucune autre finition. "
            "Les reprendre à sec après lavage fait plus pour l'aspect de la façade que le verre "
            "lui-même.",
        "rythme_court": "Hebdo. à bimensuel",
        "rythme":
            "Hebdomadaire sur une devanture de rue passante, bimensuel dans une rue calme. "
            "Les vitrages intérieurs et les séparations de salle, une fois par mois.",
        "contrainte":
            "Intervention le matin avant la mise en place, ou l'après-midi entre les deux services. "
            "Nous apportons l'eau et l'électricité : aucun point d'eau ne vous est demandé en pleine "
            "préparation.",
        "faq": ("Pouvez-vous laver la devanture sans gêner le service ?",
                "Oui. Le créneau le plus simple reste le matin avant la mise en place, ou le milieu "
                "d'après-midi. L'intervention dure de vingt minutes à une heure selon la surface, et "
                "nous travaillons de l'extérieur pour tout ce qui peut l'être."),
    },
    {
        "slug": "pharmacie",
        "nom": "pharmacie",
        "nom_long": "pharmacie et parapharmacie",
        "le": "une pharmacie",
        "dans": "en pharmacie",
        "enjeu": "Une vitrine qui doit inspirer le soin",
        "probleme":
            "Une pharmacie a souvent la plus grande surface vitrée du quartier et le plus de "
            "mobilier de vitrine : présentoirs, croix lumineuse, film publicitaire adhésif. Le verre "
            "n'est donc pas lavable d'un seul geste, et les adhésifs imposent une limite nette — un "
            "racloir les entame, un produit trop alcalin en décolle les bords.",
        "detail":
            "La croix et l'enseigne lumineuse sont presque toujours oubliées. Elles s'encrassent de "
            "poussière grasse et perdent en luminosité de façon progressive, donc imperceptible. "
            "Nous les reprenons dans le même passage, à la perche et à l'eau déminéralisée.",
        "rythme_court": "Bimensuel",
        "rythme":
            "Bimensuel sur la vitrine principale, mensuel sur l'ensemble façade, enseigne et "
            "vitrages intérieurs du comptoir.",
        "contrainte":
            "L'officine reçoit en continu : nous intervenons avant 9 h, ou pendant la pause de "
            "milieu de journée quand elle existe.",
        "faq": ("Le lavage abîme-t-il les films adhésifs et les vitrophanies ?",
                "Pas si l'on s'arrête à ce qu'ils supportent. Nous les lavons à la mouillette et au "
                "produit neutre, sans racloir et sans jet dirigé sur les bords : c'est le bord "
                "soulevé qui finit par décoller tout l'adhésif. Un film déjà entamé avant notre "
                "passage, nous vous le signalons avant de commencer."),
    },
    {
        "slug": "agence-immobiliere",
        "nom": "agence immobilière",
        "nom_long": "agence immobilière",
        "le": "une agence immobilière",
        "dans": "en agence immobilière",
        "enjeu": "La vitrine est le premier argument de vente",
        "probleme":
            "Une agence immobilière vit de sa vitrine : les mandats y sont affichés, et c'est le seul "
            "support que le passant lit en s'arrêtant. Les écrans rétroéclairés et les porte-affiches "
            "posés derrière le verre rendent toute trace lisible à contre-jour, bien plus que sur une "
            "vitrine ordinaire.",
        "detail":
            "La difficulté est le reflet. Un verre lavé à l'eau du robinet garde un voile calcaire "
            "qui ne se voit que lorsqu'une source lumineuse est placée derrière — c'est-à-dire "
            "exactement la configuration d'une vitrine d'agence. L'eau déminéralisée n'est pas un "
            "argument commercial ici, c'est la seule méthode qui tienne.",
        "rythme_court": "Hebdomadaire",
        "rythme":
            "Hebdomadaire en rue commerçante, bimensuel ailleurs. Les bureaux et les cloisons vitrées "
            "intérieures, une fois par mois.",
        "contrainte":
            "Intervention avant l'ouverture ou le samedi en fin de journée. Nous travaillons pour "
            "plusieurs agences parisiennes sur ce rythme, avec un planning fixe annoncé à l'avance.",
        "faq": ("Intervenez-vous sur plusieurs agences d'un même réseau ?",
                "Oui, et c'est le cas le plus courant : un planning unique, un interlocuteur, une "
                "facture par agence ou une facture groupée selon ce qui vous arrange. Les horaires "
                "sont fixés une fois pour toutes, ce qui évite d'avoir à reprendre contact chaque mois."),
    },
    {
        "slug": "commerce-pret-a-porter",
        "nom": "boutique de prêt-à-porter",
        "nom_long": "boutique de prêt-à-porter",
        "le": "une boutique de prêt-à-porter",
        "dans": "en boutique de prêt-à-porter",
        "enjeu": "Du verre qui doit disparaître",
        "probleme":
            "Dans le prêt-à-porter, la vitrine réussie est celle qu'on ne voit pas : le regard doit "
            "aller au produit, pas au verre. Les grandes surfaces vitrées sans menuiserie "
            "intermédiaire sont les plus exigeantes, parce que le moindre défaut de séchage traverse "
            "toute la hauteur et devient une rayure lumineuse sous les spots.",
        "detail":
            "Les traces de mains d'enfants à mi-hauteur et les marques de sacs au bas du vitrage "
            "reviennent chaque jour en rue passante. Un nettoyage complet hebdomadaire plus une "
            "reprise rapide de la zone basse tient mieux qu'un seul grand passage mensuel.",
        "rythme_court": "Hebdomadaire",
        "rythme":
            "Hebdomadaire sur la vitrine, mensuel sur les miroirs de cabine, les cloisons et la "
            "façade haute.",
        "contrainte":
            "Avant l'ouverture, en général entre 8 h et 10 h. En centre commercial, nous nous "
            "alignons sur les horaires de livraison imposés par la galerie.",
        "faq": ("Nettoyez-vous aussi les miroirs de cabine ?",
                "Oui, ils font partie du même passage et c'est souvent ce qui se remarque le plus : "
                "un miroir de cabine marqué par les doigts et les aérosols de parfum donne une "
                "impression de négligence au moment précis où le client décide d'acheter."),
    },
    {
        "slug": "opticien",
        "nom": "opticien",
        "nom_long": "magasin d'optique",
        "le": "un magasin d'optique",
        "dans": "chez un opticien",
        "enjeu": "La cohérence du métier",
        "probleme":
            "Un opticien vend de la clarté : une vitrine voilée le contredit à l'entrée. Le magasin "
            "cumule en outre plus de verre au mètre carré que presque tout autre commerce — vitrine, "
            "présentoirs vitrés, miroirs d'essayage, vitrines murales fermées.",
        "detail":
            "Les présentoirs intérieurs demandent plus de temps que la vitrine : ils sont manipulés "
            "en permanence, et les montures y laissent des marques de contact. Ils se nettoient au "
            "chiffon microfibre et au produit neutre, sans aérosol près des verres traités.",
        "rythme_court": "Bimensuel",
        "rythme":
            "Bimensuel sur la vitrine, hebdomadaire sur les présentoirs et les miroirs d'essayage.",
        "contrainte":
            "Avant l'ouverture. Les présentoirs sont refermés comme nous les avons trouvés : nous ne "
            "déplaçons pas les montures, nous nettoyons autour et dessous quand l'accès le permet.",
        "faq": ("Le produit utilisé peut-il abîmer les verres des montures exposées ?",
                "Nous ne pulvérisons jamais près des montures. Les présentoirs sont essuyés au "
                "chiffon microfibre préalablement humidifié, à l'écart du mobilier : le produit ne "
                "circule pas en aérosol dans le magasin. C'est une précaution simple et elle évite "
                "tout risque sur les traitements antireflet."),
    },
    {
        "slug": "hotel",
        "nom": "hôtel",
        "nom_long": "hôtel",
        "le": "un hôtel",
        "dans": "en hôtel",
        "enjeu": "La première minute du séjour",
        "probleme":
            "Un hôtel se juge dans les dix premiers mètres : porte à tambour, sas d'entrée, vitrage "
            "du lobby. Ce sont aussi les surfaces les plus touchées de l'établissement, et elles se "
            "marquent en quelques heures. Les étages posent un autre problème : les fenêtres de "
            "chambre ne peuvent être lavées qu'entre deux départs.",
        "detail":
            "Le sas d'entrée est le point qui décide de l'impression générale, et il demande deux "
            "passages par semaine là où le reste s'accommode d'un passage mensuel. Pour les chambres, "
            "nous travaillons par lots, sur la liste des chambres libres communiquée le matin même.",
        "rythme_court": "2 × / semaine",
        "rythme":
            "Deux passages hebdomadaires sur le sas et le lobby, mensuel sur les vitrages communs, "
            "par campagnes pour les chambres.",
        "contrainte":
            "Les horaires sont ceux de la faible fréquentation : tôt le matin pour le lobby, milieu "
            "de journée pour les chambres, entre le départ et l'arrivée suivante.",
        "faq": ("Pouvez-vous laver les fenêtres des chambres sans bloquer les réservations ?",
                "Oui, en travaillant sur les chambres libérées le matin. Vous nous donnez la liste à "
                "l'arrivée, nous suivons le rythme du ménage et nous passons avant la remise en "
                "vente. Aucune chambre n'est immobilisée plus longtemps que pour son nettoyage habituel."),
    },
    {
        "slug": "bureaux",
        "nom": "bureaux",
        "nom_long": "immeuble de bureaux",
        "le": "un plateau de bureaux",
        "dans": "en bureaux",
        "enjeu": "La lumière du plateau",
        "probleme":
            "Sur un plateau de bureaux, le verre encrassé coûte de la lumière naturelle avant de "
            "coûter de l'allure : un vitrage sale réduit sensiblement l'apport lumineux, et les "
            "éclairages compensent. Les cloisons vitrées intérieures, elles, portent les traces de "
            "mains à hauteur de poignée sur toute leur longueur.",
        "detail":
            "La question réelle est l'accès. Jusqu'à trois niveaux, la perche télescopique à eau "
            "déminéralisée suffit depuis le sol et c'est la solution la plus économique. Au-delà, "
            "ou sur une façade sans recul, il faut un moyen d'accès que nous ne mettons pas en "
            "œuvre : nous vous le disons avant le devis, pas après.",
        "rythme_court": "Trimestriel",
        "rythme":
            "Trimestriel sur les façades accessibles depuis le sol, mensuel sur les cloisons "
            "intérieures et les portes vitrées.",
        "contrainte":
            "Hors heures d'activité : tôt le matin, en soirée, ou le week-end. Les plateaux occupés "
            "ne sont jamais traités en pleine journée de travail.",
        "faq": ("Jusqu'à quelle hauteur pouvez-vous intervenir ?",
                "Depuis le sol, à la perche, nous atteignons sans difficulté les trois premiers "
                "niveaux. Au-delà, l'intervention relève du travail en hauteur avec nacelle ou "
                "cordiste, que nous ne réalisons pas : nous le disons franchement plutôt que de "
                "prendre le chantier et de vous laisser avec un étage non fait."),
    },
    {
        "slug": "salle-de-sport",
        "nom": "salle de sport",
        "nom_long": "salle de sport et studio",
        "le": "une salle de sport",
        "dans": "en salle de sport",
        "enjeu": "Des miroirs qui ne pardonnent rien",
        "probleme":
            "Une salle de sport est faite de miroirs sur toute la longueur des murs, et c'est la "
            "surface la plus exigeante qui existe : la transpiration en aérosol s'y dépose en "
            "continu, et un miroir mal séché se voit depuis l'autre bout de la salle, ce qui n'est "
            "pas le cas d'une vitre.",
        "detail":
            "Le point à surveiller n'est pas le miroir mais son bas : l'eau qui coule stagne au joint "
            "inférieur et attaque le tain par l'arrière. C'est irréversible et cela se voit comme une "
            "frange noire sur le bord. Nous travaillons donc avec peu d'eau et un séchage immédiat du "
            "bas vers le haut.",
        "rythme_court": "Hebdomadaire",
        "rythme":
            "Hebdomadaire sur les miroirs de plateau, bimensuel sur la façade vitrée et les "
            "cloisons de studio.",
        "contrainte":
            "Les salles ouvrent tôt et ferment tard : nous intervenons en milieu de matinée ou en "
            "début d'après-midi, aux heures creuses, zone par zone sans fermer la salle.",
        "faq": ("Comment évitez-vous d'abîmer le tain des miroirs ?",
                "En limitant l'eau et en séchant le bord bas en premier. Le tain ne s'abîme pas par "
                "la face, il s'abîme par l'arrière, là où l'eau s'infiltre au joint inférieur. C'est "
                "la raison pour laquelle un miroir de salle lavé au jet se piquette de noir en "
                "quelques mois sur toute sa base."),
    },
    {
        "slug": "cabinet-medical",
        "nom": "cabinet médical",
        "nom_long": "cabinet médical et paramédical",
        "le": "un cabinet médical",
        "dans": "en cabinet médical",
        "enjeu": "Ce que la salle d'attente dit du soin",
        "probleme":
            "Dans un cabinet, le verre n'est pas commercial : il est lu comme un indice de rigueur. "
            "Les portes vitrées de salle d'attente, les cloisons de secrétariat et les fenêtres "
            "donnant sur rue sont les trois surfaces que tout patient regarde en attendant, souvent "
            "longtemps et de très près.",
        "detail":
            "La contrainte propre au secteur est la discrétion : nous ne nettoyons que les parties "
            "communes et les surfaces désignées, jamais un bureau pendant une consultation, et aucun "
            "document n'est déplacé. Les produits sont sans parfum marqué, ce qui compte en salle "
            "d'attente fermée.",
        "rythme_court": "Mensuel",
        "rythme":
            "Mensuel sur l'ensemble des vitrages, avec une reprise des portes et des cloisons de "
            "secrétariat toutes les deux semaines.",
        "contrainte":
            "En dehors des plages de consultation : tôt le matin, en fin de journée, ou le jour de "
            "fermeture hebdomadaire du cabinet.",
        "faq": ("Intervenez-vous sans être présents pendant les consultations ?",
                "Oui, c'est la règle. Nous venons avant l'ouverture ou après la dernière "
                "consultation. Si un créneau de journée est le seul possible, nous nous limitons aux "
                "parties communes et nous nous arrêtons dès qu'un patient entre."),
    },
]


# ---------------------------------------------------------------------------
# MÉNAGE RÉGULIER PAR TYPE DE SITE
# ---------------------------------------------------------------------------
# Le ménage régulier n'est pas une prestation unique répétée : chaque type de
# site a un point de contrôle qui décide du résultat, et c'est lui qu'il faut
# nommer. Une copropriété se juge sur sa cage d'escalier, un cabinet médical
# sur ses points de contact, un commerce sur son sol au ras des portes.
SECTEURS_MENAGE = [
    {
        "slug": "bureaux",
        "nom": "bureaux",
        "nom_long": "plateau de bureaux",
        "le": "un plateau de bureaux",
        "dans": "en bureaux",
        "enjeu": "Les sanitaires décident de la réputation du prestataire",
        "probleme":
            "Sur un plateau de bureaux, l'entretien n'est jamais jugé sur les bureaux eux-mêmes mais "
            "sur deux endroits : les sanitaires et la tisanerie. Un plateau impeccable avec des "
            "sanitaires moyens est perçu comme mal entretenu, et l'inverse est vrai aussi.",
        "perimetre": ("Sanitaires : cuvettes, robinetterie, miroirs, réapprovisionnement",
                      "Tisanerie et point café : plans de travail, évier, micro-ondes, sol",
                      "Bureaux et postes de travail : poussière des surfaces dégagées, corbeilles",
                      "Circulations : sols, poignées, interrupteurs, portes vitrées",
                      "Salles de réunion : table, chaises, tableau, cloisons vitrées"),
        "rythme":
            "Trois à cinq passages par semaine selon l'effectif, avec les sanitaires et la tisanerie "
            "à chaque passage et les surfaces vitrées une fois par mois.",
        "contrainte":
            "Avant 8 h 30 ou après 18 h 30. Nous ne déplaçons aucun document et nous ne touchons "
            "pas aux bureaux encombrés : la poussière est faite sur les surfaces dégagées, ce qui "
            "est la seule façon honnête de l'annoncer.",
        "faq": ("Faut-il nous fournir les produits et le matériel ?",
                "Non, nous venons avec tout. Les consommables sanitaires — papier, savon, sacs — "
                "peuvent être inclus dans la prestation ou restés à votre charge selon ce que vous "
                "préférez ; dans les deux cas, c'est écrit sur le devis."),
    },
    {
        "slug": "cabinet-medical",
        "nom": "cabinet médical",
        "nom_long": "cabinet médical et paramédical",
        "le": "un cabinet médical",
        "dans": "en cabinet médical",
        "enjeu": "Les points de contact, pas la surface",
        "probleme":
            "Dans un cabinet, ce qui compte n'est pas le nombre de mètres carrés traités mais le "
            "nombre de points de contact repris : poignées, accoudoirs de salle d'attente, "
            "interrupteurs, comptoir d'accueil, boutons d'ascenseur. Ce sont eux que tout le monde "
            "touche et que la plupart des prestations oublient.",
        "perimetre": ("Salle d'attente : sièges, accoudoirs, tables, sol",
                      "Points de contact : poignées, interrupteurs, comptoir, rampes",
                      "Sanitaires : à chaque passage, sans exception",
                      "Sols : lavage avec un produit sans parfum marqué",
                      "Vitrages et portes vitrées : reprise à chaque passage"),
        "rythme":
            "Un passage quotidien ou tous les deux jours, hors plages de consultation.",
        "contrainte":
            "Nous n'entrons jamais dans une salle de soins occupée et nous ne manipulons aucun "
            "dispositif médical. La gestion des déchets de soins reste la vôtre : ce n'est pas notre "
            "métier et nous ne nous en chargeons pas.",
        "faq": ("Prenez-vous en charge la désinfection réglementaire des salles de soins ?",
                "Non. Nous assurons l'entretien courant — sols, points de contact, sanitaires, "
                "salle d'attente, vitrages. Les protocoles de désinfection propres aux salles de "
                "soins et la filière des déchets d'activités de soins relèvent du praticien et de "
                "prestataires spécialisés. Nous préférons le dire d'emblée."),
    },
    {
        "slug": "copropriete",
        "nom": "copropriété",
        "nom_long": "copropriété et cage d'escalier",
        "le": "une copropriété",
        "dans": "en copropriété",
        "enjeu": "La cage d'escalier est le seul critère des résidents",
        "probleme":
            "Une copropriété se juge sur trois choses : le hall, la cage d'escalier et le local "
            "poubelles. Les deux premières décident de l'impression — et de la valeur perçue des "
            "lots ; la troisième décide des réclamations au conseil syndical. Le reste passe "
            "largement inaperçu.",
        "perimetre": ("Hall d'entrée : sol, boîtes aux lettres, porte vitrée, miroir",
                      "Escaliers et paliers : marches, nez de marche, rampe, plinthes",
                      "Local poubelles : sol, bacs, désodorisation",
                      "Ascenseur : sol, parois, miroir, boutons d'appel",
                      "Sous-sol et parkings : balayage des circulations"),
        "rythme":
            "Un à trois passages par semaine selon le nombre de lots, avec la sortie et la rentrée "
            "des bacs calées sur le calendrier de collecte de la commune.",
        "contrainte":
            "Les horaires sont fixes et connus des résidents : c'est ce qui fait la différence entre "
            "un prestataire jugé fiable et un prestataire soupçonné de ne pas être passé. Un relevé "
            "de passage est laissé dans le hall.",
        "faq": ("Gérez-vous la sortie et la rentrée des conteneurs ?",
                "Oui, c'est presque toujours inclus. Nous suivons le calendrier de collecte de la "
                "commune, qui n'est pas le même d'une ville à l'autre en Île-de-France, et nous "
                "rentrons les bacs le jour même — c'est le point sur lequel les copropriétés "
                "changent le plus souvent de prestataire."),
    },
    {
        "slug": "commerce",
        "nom": "commerce",
        "nom_long": "commerce de détail",
        "le": "un commerce",
        "dans": "en commerce",
        "enjeu": "Le mètre carré d'entrée",
        "probleme":
            "Dans un commerce, la saleté entre par la porte et ne va pas loin : les trois premiers "
            "mètres reçoivent l'essentiel de ce que les chaussures apportent de la rue. C'est aussi "
            "la zone que le client voit en premier, et celle qui demande le plus de passages.",
        "perimetre": ("Zone d'entrée : sol, tapis de propreté, seuil, porte vitrée",
                      "Surface de vente : sol, poussière des linéaires et des présentoirs",
                      "Cabines et miroirs quand il y en a",
                      "Réserve et arrière-boutique : sol, évacuation des cartons",
                      "Sanitaires du personnel"),
        "rythme":
            "Quotidien ou cinq fois par semaine en rue passante, trois fois ailleurs. La zone "
            "d'entrée est reprise à chaque passage.",
        "contrainte":
            "Avant l'ouverture, ou après la fermeture pour les commerces qui ferment tard. En "
            "centre commercial, nous nous alignons sur les plages d'accès livraison de la galerie.",
        "faq": ("Intervenez-vous avant l'ouverture, même tôt ?",
                "Oui. Le créneau le plus demandé se situe entre 6 h 30 et 9 h, et c'est celui sur "
                "lequel nous construisons les tournées. Un commerce qui ouvre à 10 h peut être "
                "traité à 8 h sans que personne de l'équipe n'ait à être présent, si vous nous "
                "confiez un accès."),
    },
    {
        "slug": "agence-immobiliere",
        "nom": "agence immobilière",
        "nom_long": "agence immobilière",
        "le": "une agence immobilière",
        "dans": "en agence immobilière",
        "enjeu": "Recevoir des clients dans ses locaux",
        "probleme":
            "Une agence immobilière reçoit toute la journée des gens qui s'apprêtent à engager des "
            "sommes importantes, assis dans ses bureaux. Le niveau d'entretien des locaux est lu "
            "comme un indice de sérieux, et les surfaces qui le trahissent sont toujours les mêmes : "
            "la vitrine, la table de réunion et les sièges visiteurs.",
        "perimetre": ("Vitrine et porte vitrée : à chaque passage",
                      "Espace d'accueil et sièges visiteurs",
                      "Bureaux et table de réunion : surfaces dégagées",
                      "Sols : aspiration et lavage selon le revêtement",
                      "Point café et sanitaires"),
        "rythme":
            "Deux à trois passages par semaine, avec la vitrine reprise à chaque fois et un "
            "nettoyage textile des sièges et de la moquette une à deux fois par an.",
        "contrainte":
            "Avant l'ouverture, ou le samedi en fin de journée pour les agences ouvertes en "
            "semaine jusqu'à 19 h. Planning fixe, communiqué à l'avance.",
        "faq": ("Pouvez-vous suivre plusieurs agences d'un même réseau ?",
                "Oui, c'est l'essentiel de ce que nous faisons côté professionnels : un planning "
                "commun, un interlocuteur unique, et une facturation par agence ou groupée selon "
                "votre organisation comptable."),
    },
    {
        "slug": "restaurant",
        "nom": "restaurant",
        "nom_long": "restaurant et chaîne de restauration",
        "le": "un restaurant",
        "dans": "en restaurant",
        "enjeu": "Ce que le ménage courant ne couvre pas",
        "probleme":
            "En restauration, l'équipe assure déjà le nettoyage quotidien : la question n'est donc "
            "pas de le refaire mais de traiter ce qu'un service ne permet pas de faire. Les sols en "
            "profondeur, les joints de carrelage gras, les plinthes, les dessous d'équipements et "
            "les surfaces en hauteur relèvent d'un passage dédié.",
        "perimetre": ("Sols de cuisine en profondeur, joints de carrelage inclus",
                      "Plinthes, bas de murs, dessous et arrières d'équipements mobiles",
                      "Surfaces en hauteur : étagères, grilles de ventilation, luminaires",
                      "Salle : banquettes et chaises en textile, vitrages, sols",
                      "Sanitaires clients : reprise complète"),
        "rythme":
            "Un passage hebdomadaire ou bimensuel en complément du nettoyage quotidien de "
            "l'équipe, plus une remise à niveau complète deux à quatre fois par an.",
        "contrainte":
            "La nuit ou le jour de fermeture. La cuisine doit être opérationnelle au service "
            "suivant : c'est une contrainte que nous intégrons au planning, pas une réserve que "
            "nous découvrons sur place.",
        "faq": ("Faites-vous aussi le dégraissage de la hotte lors de ce passage ?",
                "C'est une prestation distincte, que nous assurons également — hotte, filtres et "
                "conduits d'extraction. Les deux se planifient souvent ensemble pour ne mobiliser "
                "la cuisine qu'une fois, mais elles se chiffrent séparément parce qu'elles "
                "n'emploient ni le même matériel ni le même temps."),
    },
    {
        "slug": "coworking",
        "nom": "espace de coworking",
        "nom_long": "espace de coworking",
        "le": "un espace de coworking",
        "dans": "en coworking",
        "enjeu": "Des surfaces partagées par cent personnes",
        "probleme":
            "Un espace de coworking a la fréquentation d'un bureau de cent personnes et le mobilier "
            "d'un café : tables partagées, canapés, cuisine commune. Rien n'est attribué, donc "
            "personne ne se sent responsable d'une surface, et l'usure visible arrive beaucoup plus "
            "vite qu'en bureau classique.",
        "perimetre": ("Cuisine commune : plans, évier, lave-vaisselle, micro-ondes, frigo",
                      "Tables partagées et postes en flex : désinfection des surfaces",
                      "Salles de réunion et cabines téléphoniques",
                      "Canapés et assises textiles : aspiration, détachage ponctuel",
                      "Sanitaires et circulations : plusieurs reprises par jour"),
        "rythme":
            "Un passage quotidien, souvent doublé d'une reprise en milieu de journée sur la cuisine "
            "et les sanitaires. Nettoyage textile des assises deux fois par an.",
        "contrainte":
            "Le site est occupé presque sans interruption : nous travaillons tôt le matin pour le "
            "gros, et la reprise de milieu de journée se fait zone par zone, sans fermer d'espace.",
        "faq": ("Le nettoyage des canapés et des assises est-il compris ?",
                "L'aspiration et le détachage ponctuel, oui. Le nettoyage en profondeur par "
                "injection-extraction est une intervention séparée, à programmer une à deux fois "
                "par an : c'est elle qui rattrape le grisaillement des assises, qu'un passage "
                "quotidien ne traite pas."),
    },
    {
        "slug": "salle-de-sport",
        "nom": "salle de sport",
        "nom_long": "salle de sport et studio",
        "le": "une salle de sport",
        "dans": "en salle de sport",
        "enjeu": "Vestiaires et contact machine",
        "probleme":
            "Une salle de sport a deux zones qui décident de tout : les vestiaires, où l'humidité "
            "permanente favorise les odeurs et les moisissures de joints, et les poignées de "
            "machines, que des dizaines de mains touchent chaque heure. Le reste du plateau est "
            "secondaire en comparaison.",
        "perimetre": ("Vestiaires et douches : sols, joints, bancs, casiers",
                      "Poignées et surfaces de contact des appareils",
                      "Tapis de sol, sol de plateau, zone de poids libres",
                      "Miroirs et vitrages",
                      "Sanitaires et accueil"),
        "rythme":
            "Un passage quotidien, avec une reprise des vestiaires en fin de journée, et un "
            "traitement des joints de douche une fois par mois.",
        "contrainte":
            "Les salles ouvrent tôt et ferment tard : l'intervention se place en heures creuses, "
            "milieu de matinée ou début d'après-midi, zone par zone.",
        "faq": ("Que faire des odeurs persistantes dans les vestiaires ?",
                "Elles viennent presque toujours des joints de douche et des siphons, pas de l'air. "
                "Un désodorisant les masque quelques heures. Le traitement des joints et le "
                "détartrage des évacuations les font disparaître durablement : c'est plus long à "
                "faire, et c'est la seule chose qui marche."),
    },
]


# ---------------------------------------------------------------------------
# COMMUNES — ANGLE PROFESSIONNEL (hottes et vitrerie)
# ---------------------------------------------------------------------------
# Une page par couple commune × prestation professionnelle. Ce qui change
# réellement d'une commune à l'autre : le tissu commercial — un boulevard de
# restaurants ne pose pas le même problème qu'une zone de bureaux —, l'accès
# et le stationnement, et la distance depuis l'atelier, qui décide du délai.
# Sans ces trois éléments, la page n'aurait aucune raison d'exister.
VILLES_PRO = [
    {
        "slug": "saint-denis", "nom": "Saint-Denis", "cp": "93200", "dept": "93",
        "lat": 48.9362, "lon": 2.3574,
        "tissu":
            "Saint-Denis concentre trois tissus commerciaux distincts : le centre ancien autour de "
            "la basilique et de son marché, l'un des plus fréquentés d'Île-de-France ; les abords du "
            "Stade de France, où la restauration rapide travaille par pics ; et la Plaine, devenue "
            "en vingt ans un quartier de bureaux livrés en continu. Les trois appellent des "
            "interventions à des heures opposées.",
        "acces":
            "Le centre ancien est en grande partie piéton, avec des plages de livraison limitées au "
            "matin. Nous y arrivons avant 7 h, ce qui est aussi le moment où les commerces de bouche "
            "sont ouverts et où personne ne traverse le chantier.",
        "hotte":
            "La restauration dionysienne est dense et très diverse : boulangeries du centre, "
            "restaurants de cuisine du monde autour du marché, restauration rapide près du stade. "
            "Les cuisines y sont souvent petites, avec un conduit court mais coudé, et c'est dans "
            "ces coudes que la graisse s'accumule le plus vite. Beaucoup de locaux ont changé "
            "plusieurs fois d'enseigne sans que le circuit d'extraction ait jamais été repris : nous "
            "le constatons régulièrement à la première ouverture des trappes.",
        "vitres":
            "Deux chantiers très différents cohabitent. En centre-ville, des vitrines de commerce de "
            "bouche exposées à un trafic piéton intense, à reprendre chaque semaine. Dans la Plaine, "
            "des façades de bureaux récentes, en grande partie accessibles depuis le sol à la perche "
            "— c'est là que l'eau déminéralisée fait la différence la plus visible, parce que les "
            "menuiseries sombres de ces immeubles gardent la trace calcaire.",
        "faq_hotte": ("Mon local a déjà changé d'enseigne : le conduit a-t-il été nettoyé ?",
                      "C'est la question à poser avant la reprise, et presque personne ne la pose. "
                      "Un conduit encrassé par l'activité précédente reste encrassé après les "
                      "travaux : la peinture neuve ne change rien à ce qui est à l'intérieur. Nous "
                      "ouvrons les trappes et nous vous montrons l'état avant de chiffrer."),
        "faq_vitres": ("Intervenez-vous dans le centre piéton de Saint-Denis ?",
                       "Oui, avant 7 h, dans la plage de livraison autorisée. C'est le créneau où "
                       "le verre est froid, ce qui donne un séchage régulier, et où la rue est "
                       "encore vide."),
    },
    {
        "slug": "aubervilliers", "nom": "Aubervilliers", "cp": "93300", "dept": "93",
        "lat": 48.9146, "lon": 2.3822,
        "tissu":
            "Aubervilliers vit du commerce de gros et de la logistique autant que du commerce de "
            "détail. Les grossistes du quartier de la Haie-Coq, les entrepôts reconvertis du canal "
            "et un tissu dense de restauration de quartier forment une clientèle professionnelle qui "
            "travaille tôt et qui n'a pas de temps mort en journée.",
        "acces":
            "La circulation de poids lourds rend les abords difficiles en milieu de matinée. Nous "
            "intervenons avant 7 h ou en fin de journée, et nous sommes à moins de dix kilomètres de "
            "notre atelier : c'est l'une des communes où nous pouvons nous engager sur un créneau "
            "serré.",
        "hotte":
            "Les cuisines albertivillariennes sont souvent installées dans des locaux anciens, avec "
            "des conduits longs qui traversent plusieurs niveaux avant de ressortir en toiture. "
            "C'est la configuration la plus exigeante : la longueur multiplie les points "
            "d'accumulation, et un dégraissage limité à la hotte y laisse l'essentiel du dépôt en "
            "place. Nous travaillons par trappes successives sur toute la ligne.",
        "vitres":
            "Les vitrines de grossistes sont grandes, hautes et peu démontables. L'enjeu y est moins "
            "esthétique que fonctionnel : un vitrage voilé éteint la marchandise exposée. À côté, "
            "les locaux du canal reconvertis en bureaux ont des verrières d'atelier à petits bois, "
            "les surfaces les plus longues à faire correctement, qui se comptent au carreau et non "
            "au mètre carré.",
        "faq_hotte": ("Pouvez-vous traiter un conduit qui monte sur trois étages ?",
                      "Oui, à condition que des trappes de visite existent ou puissent être "
                      "posées. Sans accès intermédiaire, un conduit vertical long ne peut pas être "
                      "nettoyé sur toute sa hauteur, et nous vous le dirons plutôt que de facturer "
                      "un dégraissage partiel présenté comme complet."),
        "faq_vitres": ("Comment chiffrez-vous une verrière d'atelier ?",
                       "Au carreau. Une verrière à petits bois demande plusieurs fois le temps "
                       "d'une baie de même surface : un prix au mètre carré serait trompeur. Nous "
                       "comptons sur photos, et le devis est ferme avant notre venue."),
    },
    {
        "slug": "montreuil", "nom": "Montreuil", "cp": "93100", "dept": "93",
        "lat": 48.8638, "lon": 2.4485,
        "tissu":
            "Montreuil a l'un des tissus de restauration indépendante les plus denses de la petite "
            "couronne, concentré autour de la Croix-de-Chavaux et de la mairie, avec beaucoup de "
            "petites salles et de cuisines ouvertes. S'y ajoutent les anciens ateliers des Hauts "
            "reconvertis en bureaux et en espaces de travail partagés.",
        "acces":
            "Les rues du bas Montreuil sont étroites et le stationnement y est tendu. Notre "
            "véhicule est léger et autonome en eau et en électricité : nous n'avons besoin ni d'un "
            "point d'eau ni d'une place à proximité immédiate.",
        "hotte":
            "La cuisine ouverte, très répandue à Montreuil, change la nature du problème : la hotte "
            "est visible depuis la salle, donc son aspect compte autant que son état intérieur, et "
            "les buées non captées se déposent sur le plafond et les luminaires de la salle. Nous "
            "traitons la hotte, les filtres et le conduit, et nous signalons la zone de plafond "
            "quand elle est manifestement touchée — c'est un indice fiable d'une extraction "
            "insuffisante.",
        "vitres":
            "Les grandes verrières d'anciens ateliers sont la signature de Montreuil. Elles sont "
            "magnifiques et très exigeantes : beaucoup de petits bois, souvent des mastics anciens "
            "qui retiennent la poussière, et des hauteurs qui demandent la perche. Les devantures de "
            "restaurant du bas Montreuil, elles, se reprennent chaque semaine à cause du trafic.",
        "faq_hotte": ("Ma cuisine est ouverte sur la salle : l'intervention salit-elle le "
                      "restaurant ?",
                      "Non, parce que tout est bâché avant la première ouverture de trappe. Le "
                      "point de vigilance en cuisine ouverte est le plafond de salle : s'il est "
                      "jauni au-dessus du piano, l'extraction ne capte pas assez et le dégraissage "
                      "seul n'y changera rien. Nous vous le disons."),
        "faq_vitres": ("Nettoyez-vous les verrières d'atelier en hauteur ?",
                       "Depuis le sol, à la perche télescopique et à l'eau déminéralisée, nous "
                       "atteignons les trois premiers niveaux. Une verrière de toit ou une façade "
                       "sans recul relève du travail en hauteur avec nacelle, que nous ne réalisons "
                       "pas : nous le disons avant le devis."),
    },
    {
        "slug": "pantin", "nom": "Pantin", "cp": "93500", "dept": "93",
        "lat": 48.8944, "lon": 2.4090,
        "tissu":
            "Pantin s'est transformée le long du canal de l'Ourcq : sièges d'entreprises, ateliers "
            "reconvertis, et une restauration nouvelle qui accompagne cette installation de bureaux. "
            "Le centre ancien autour de l'église et du marché garde en parallèle son commerce de "
            "bouche traditionnel.",
        "acces":
            "Les quais du canal sont accessibles et le stationnement y est praticable en dehors des "
            "heures de bureau. Pantin est à une douzaine de kilomètres de notre atelier : nous y "
            "intervenons habituellement sous 24 à 48 h.",
        "hotte":
            "Deux profils : les restaurants d'entreprise et de quartier du canal, aux cuisines "
            "récentes et bien conçues, où un passage annuel suffit ; et les commerces de bouche du "
            "centre, dans des locaux anciens, où le conduit est souvent plus court mais bien plus "
            "chargé. Les premiers se planifient à l'année, les seconds demandent un constat avant "
            "de pouvoir être chiffrés sérieusement.",
        "vitres":
            "Les immeubles de bureaux récents du canal ont de grandes façades vitrées, lisibles de "
            "loin et donc impitoyables au défaut de séchage. Les rez-de-chaussée commerciaux sont "
            "accessibles depuis le sol et c'est l'essentiel de la surface visible. En centre ancien, "
            "le travail est celui d'une rue commerçante classique : vitrine hebdomadaire, façade "
            "haute mensuelle.",
        "faq_hotte": ("Peut-on signer un contrat annuel plutôt qu'appeler chaque fois ?",
                      "Oui, et c'est la formule la plus simple pour un restaurant d'entreprise : "
                      "un ou deux passages programmés à date fixe, le relevé de chaque "
                      "intervention qui vient compléter votre livret d'entretien, et plus rien à "
                      "suivre dans l'année."),
        "faq_vitres": ("Pouvez-vous intervenir en dehors des heures de bureau ?",
                       "Oui, et c'est la règle sur les immeubles occupés : tôt le matin, en soirée "
                       "ou le week-end. Un plateau en activité n'est jamais traité en pleine "
                       "journée de travail."),
    },
    {
        "slug": "bobigny", "nom": "Bobigny", "cp": "93000", "dept": "93",
        "lat": 48.9106, "lon": 2.4396,
        "tissu":
            "Préfecture de la Seine-Saint-Denis, Bobigny réunit administrations, tribunal, hôpital "
            "et un centre commercial de centre-ville. La restauration y est largement tournée vers "
            "le midi : brasseries, restauration rapide, traiteurs qui travaillent sur un créneau "
            "court et intense.",
        "acces":
            "Le centre administratif est bien desservi et le stationnement praticable en dehors des "
            "heures de bureau. Bobigny est à six kilomètres de notre atelier, ce qui en fait l'une "
            "des communes où nous intervenons le plus vite, souvent dans la journée.",
        "hotte":
            "Une cuisine qui ne travaille qu'au déjeuner produit un encrassement concentré : deux "
            "heures de production intense par jour, souvent en friture ou en grillade, dans un "
            "volume réduit. Le dépôt s'accumule aussi vite que dans une cuisine ouverte en continu, "
            "et c'est un calcul que beaucoup d'exploitants font à l'envers en pensant qu'un service "
            "unique espace les nettoyages.",
        "vitres":
            "Les surfaces sont ici majoritairement tertiaires et administratives : halls, cloisons "
            "vitrées, portes à grande fréquentation. Les portes vitrées d'un bâtiment recevant du "
            "public se marquent en une demi-journée, et c'est la seule surface qui justifie un "
            "passage rapproché ; le reste tient au trimestre.",
        "faq_hotte": ("Je ne sers qu'au déjeuner, faut-il nettoyer aussi souvent ?",
                      "Oui, parce que ce qui compte est la quantité de matière grasse vaporisée, "
                      "pas le nombre d'heures d'ouverture. Un service unique mais intense, en "
                      "friture ou en grillade, charge un conduit aussi vite qu'un service continu. "
                      "Le ramonage annuel des conduits reste par ailleurs le plancher réglementaire."),
        "faq_vitres": ("Pouvez-vous ne traiter que les portes et les halls ?",
                       "Oui, et c'est souvent le bon arbitrage. Les portes et les halls portent "
                       "l'essentiel de ce que les visiteurs voient ; les façades peuvent rester au "
                       "trimestre sans que cela se remarque."),
    },
    {
        "slug": "aulnay-sous-bois", "nom": "Aulnay-sous-Bois", "cp": "93600", "dept": "93",
        "lat": 48.9386, "lon": 2.4938,
        "tissu":
            "Aulnay-sous-Bois aligne un centre commerçant traditionnel autour de la gare, des zones "
            "d'activité à l'est et un habitat pavillonnaire étendu. Le commerce de bouche de "
            "proximité — boulangeries, boucheries, restaurants de quartier — y est particulièrement "
            "présent.",
        "acces":
            "Aulnay est à cinq kilomètres de notre atelier, soit dix minutes par la N2 ou l'A104. "
            "C'est la commune où nos délais sont les plus courts après Le Blanc-Mesnil : souvent le "
            "jour même en cas d'urgence.",
        "hotte":
            "Les boulangeries et les boucheries-charcuteries aulnaysiennes posent le cas le plus "
            "technique du commerce de bouche : farine mêlée au gras pour les unes, graisses animales "
            "qui figent en refroidissant pour les autres. Ni l'un ni l'autre ne part au dégraissant "
            "ménager. Notre proximité permet d'intervenir sur le créneau étroit entre la fin de "
            "production et la reprise.",
        "vitres":
            "Le centre commerçant demande un travail classique de vitrine, à rythme hebdomadaire. "
            "Les zones d'activité, elles, présentent des façades vitrées de locaux d'activité, "
            "grandes et simples, accessibles depuis le sol : c'est la configuration la plus "
            "économique à entretenir, et un passage trimestriel suffit généralement.",
        "faq_hotte": ("À quelle heure pouvez-vous venir dans un fournil ?",
                      "L'après-midi, entre la fin de la cuisson et la reprise du tour de nuit, ou "
                      "le jour de fermeture. Depuis Le Blanc-Mesnil nous sommes chez vous en dix "
                      "minutes, ce qui permet de tenir un créneau serré sans marge de sécurité "
                      "inutile."),
        "faq_vitres": ("Quel est le délai pour une intervention à Aulnay ?",
                       "Habituellement 24 à 48 h, et souvent le jour même en cas d'urgence : nous "
                       "sommes à cinq kilomètres. Les frais de déplacement y sont de 5 €, "
                       "annoncés avant que vous validiez."),
    },
    {
        "slug": "le-blanc-mesnil", "nom": "Le Blanc-Mesnil", "cp": "93150", "dept": "93",
        "lat": 48.9386, "lon": 2.4644,
        "tissu":
            "C'est notre commune : l'atelier s'y trouve, au 2 rue Poussin. Le Blanc-Mesnil réunit un "
            "centre commerçant, des zones d'activité le long de l'ex-RN2 et la proximité immédiate "
            "de la zone aéroportuaire, qui amène une restauration tournée vers les équipes et les "
            "horaires décalés.",
        "acces":
            "Nous sommes sur place. Les frais de déplacement sont nuls ou symboliques et nous "
            "pouvons intervenir dans des délais que nous ne tenons nulle part ailleurs — souvent le "
            "jour même, y compris sur un créneau de nuit.",
        "hotte":
            "Être à quelques minutes change la nature du service : un dégraissage de hotte "
            "s'organise sur le créneau que votre cuisine peut libérer, même court, même tardif, sans "
            "que le trajet n'oblige à élargir la plage. C'est la commune où nous intervenons le plus "
            "souvent en urgence, après un constat d'extraction défaillante ou avant une visite.",
        "vitres":
            "Le centre commerçant et les locaux d'activité se traitent au rythme habituel, avec un "
            "avantage réel : un passage de reprise entre deux nettoyages complets ne coûte presque "
            "rien en déplacement. C'est ce qui permet, ici, de tenir une vitrine impeccable sans "
            "payer un passage complet chaque semaine.",
        "faq_hotte": ("Pouvez-vous intervenir de nuit au Blanc-Mesnil ?",
                      "Oui, et c'est fréquent : l'atelier est dans la commune, le trajet ne pèse "
                      "rien dans l'organisation. Une intervention de nuit après le dernier service "
                      "se planifie sans contrainte particulière."),
        "faq_vitres": ("Facturez-vous des frais de déplacement au Blanc-Mesnil ?",
                       "Non, ou de façon symbolique : notre atelier est au 2 rue Poussin. C'est le "
                       "seul endroit où la question ne se pose pas."),
    },
    {
        "slug": "drancy", "nom": "Drancy", "cp": "93700", "dept": "93",
        "lat": 48.9227, "lon": 2.4453,
        "tissu":
            "Drancy est une commune de commerce de proximité : avenue Henri-Barbusse, marché, "
            "commerces de bouche de quartier. La restauration y est indépendante, en petites salles, "
            "avec des cuisines compactes et des conduits souvent anciens.",
        "acces":
            "Drancy est à trois kilomètres de notre atelier. Le stationnement en centre est "
            "praticable tôt le matin, qui est aussi le créneau des commerces de bouche.",
        "hotte":
            "Les petites cuisines drancéennes cumulent deux difficultés : un volume réduit, donc une "
            "concentration de buées élevée, et un circuit d'extraction rarement documenté. Dans la "
            "plupart des cas, personne ne sait quand le conduit a été nettoyé pour la dernière fois. "
            "Nous commençons par ouvrir et constater, puis nous chiffrons : c'est la seule façon de "
            "ne pas se tromper sur un conduit ancien.",
        "vitres":
            "Vitrines de commerce de proximité, à rythme hebdomadaire ou bimensuel selon le "
            "passage. La particularité locale est l'exposition au trafic de l'avenue : les "
            "particules de freinage et les hydrocarbures forment un film gras sur le verre, qui "
            "demande un dégraissage et non un simple lavage.",
        "faq_hotte": ("Je ne sais pas quand mon conduit a été nettoyé la dernière fois.",
                      "C'est le cas le plus fréquent, et ce n'est pas un problème : nous ouvrons "
                      "les trappes de visite et nous vous montrons l'état réel. Le devis se fait "
                      "sur ce constat, pas sur une estimation à l'aveugle. C'est aussi le moment "
                      "d'ouvrir le livret d'entretien qui doit être annexé à votre registre de "
                      "sécurité."),
        "faq_vitres": ("Ma vitrine est sur une avenue passante, pourquoi se salit-elle si vite ?",
                       "Parce que ce qui s'y dépose n'est pas de la poussière mais un film gras : "
                       "particules de freinage et résidus d'hydrocarbures. L'eau claire l'étale, "
                       "elle ne l'enlève pas. Il faut un dégraissage, puis un rinçage à l'eau "
                       "déminéralisée."),
    },
    {
        "slug": "noisy-le-grand", "nom": "Noisy-le-Grand", "cp": "93160", "dept": "93",
        "lat": 48.8486, "lon": 2.5527,
        "tissu":
            "Noisy-le-Grand réunit le quartier d'affaires du Mont d'Est, un centre commercial "
            "régional et des quartiers résidentiels étendus. La restauration y est largement "
            "tertiaire : restauration collective d'entreprise, chaînes, brasseries du midi.",
        "acces":
            "Noisy est à une vingtaine de kilomètres de notre atelier, par l'A3 puis l'A86 ou "
            "l'A4. Le délai habituel y est de 48 à 72 h, et le stationnement est aisé dans les "
            "parkings du quartier d'affaires.",
        "hotte":
            "La restauration collective est le cas le plus encadré et le plus volumineux : plusieurs "
            "lignes de cuisson, un circuit d'extraction dimensionné en conséquence, et une "
            "obligation de traçabilité que l'exploitant doit pouvoir présenter. Nous intervenons "
            "pendant les vacances scolaires ou les fermetures d'établissement, et nous laissons un "
            "relevé daté de ce qui a été fait, zone par zone.",
        "vitres":
            "Les façades du Mont d'Est sont hautes : seuls les premiers niveaux sont accessibles "
            "depuis le sol, et nous le disons avant le devis. L'essentiel du travail utile se "
            "concentre sur les halls, les sas d'entrée et les cloisons vitrées intérieures, qui sont "
            "ce que les occupants voient réellement de près.",
        "faq_hotte": ("Comment prouver que l'entretien a été fait lors d'un contrôle ?",
                      "Par le livret d'entretien annexé à votre registre de sécurité : c'est lui "
                      "qui porte les dates, et c'est à l'exploitant de le tenir. Nous vous "
                      "remettons un relevé daté et détaillé de l'intervention, zone par zone, qui "
                      "s'y range directement."),
        "faq_vitres": ("Traitez-vous les tours du Mont d'Est en entier ?",
                       "Non, et nous préférons le dire tout de suite : au-delà de trois niveaux, "
                       "il faut une nacelle ou un cordiste, ce que nous ne faisons pas. Nous "
                       "traitons les rez-de-chaussée, les halls, les sas et l'intérieur."),
    },
    {
        "slug": "boulogne-billancourt", "nom": "Boulogne-Billancourt", "cp": "92100",
        "dept": "92", "lat": 48.8352, "lon": 2.2409,
        "tissu":
            "Première commune d'Île-de-France après Paris par la population, Boulogne-Billancourt "
            "réunit un commerce de centre-ville dense — rue du Vieux-Pont-de-Sèvres, rue d'Aguesseau, "
            "marché Escudier — et un tissu considérable de sièges sociaux et d'agences immobilières.",
        "acces":
            "Le stationnement est payant et tendu partout, et beaucoup d'immeubles n'ont qu'un "
            "parking souterrain à hauteur limitée. Notre véhicule est léger et autonome : nous "
            "descendons en sous-sol et nous travaillons sans point d'eau sur place.",
        "hotte":
            "La restauration boulonnaise est nombreuse et installée dans des immeubles d'habitation, "
            "ce qui ajoute une contrainte que l'on sous-estime : les nuisances d'odeurs vers les "
            "logements du dessus sont la première cause de plainte en copropriété, et elles signalent "
            "presque toujours un circuit d'extraction encrassé plutôt qu'un défaut de conception. Un "
            "dégraissage complet du conduit règle souvent ce que des mois de discussion n'avaient pas "
            "réglé.",
        "vitres":
            "Les vitrines du centre et les agences immobilières forment l'essentiel de la demande. "
            "Les agences sont le cas le plus exigeant : les mandats sont rétroéclairés derrière le "
            "verre, et un voile calcaire invisible de face devient parfaitement lisible à "
            "contre-jour. L'eau déminéralisée n'y est pas un supplément, c'est la condition du "
            "résultat.",
        "faq_hotte": ("Les voisins se plaignent des odeurs de ma cuisine, est-ce lié ?",
                      "Très souvent, oui. Un conduit chargé perd de la section, l'extraction tire "
                      "moins, et les buées trouvent un autre chemin. Avant d'envisager des travaux "
                      "sur le réseau, faites dégraisser le circuit complet et mesurez à nouveau : "
                      "c'est l'hypothèse la moins coûteuse et la plus fréquente."),
        "faq_vitres": ("Nous avons plusieurs agences à Boulogne, pouvez-vous les suivre ?",
                       "Oui. Un planning unique, un interlocuteur, des horaires fixes avant "
                       "ouverture, et une facture par agence ou groupée selon votre organisation. "
                       "C'est le format sur lequel nous travaillons avec des agences parisiennes."),
    },
    {
        "slug": "levallois-perret", "nom": "Levallois-Perret", "cp": "92300", "dept": "92",
        "lat": 48.8939, "lon": 2.2874,
        "tissu":
            "Levallois est la commune la plus densément bâtie de France, et son tissu est pour "
            "l'essentiel tertiaire : sièges sociaux, agences, cabinets, avec une restauration "
            "entièrement calée sur le déjeuner des salariés.",
        "acces":
            "Le stationnement de surface est pratiquement impossible aux heures ouvrables. Nous "
            "intervenons tôt le matin, ou en sous-sol quand l'immeuble en dispose : notre autonomie "
            "en eau et en électricité rend cela possible.",
        "hotte":
            "Les cuisines levalloisiennes sont petites, insérées dans des immeubles tertiaires, et "
            "elles produisent sur un créneau de deux heures. La conséquence est toujours la même : "
            "un encrassement rapide dans un conduit court, et un exploitant persuadé qu'un service "
            "unique autorise un nettoyage espacé. Le ramonage annuel des conduits reste obligatoire, "
            "quel que soit le nombre de services.",
        "vitres":
            "Du verre partout, et presque tout en intérieur : cloisons de bureaux, portes vitrées, "
            "salles de réunion. C'est là que se joue l'impression de propreté d'un plateau, bien "
            "plus que sur la façade. Les cloisons portent les traces de mains à hauteur de poignée "
            "sur toute leur longueur et demandent un passage mensuel.",
        "faq_hotte": ("Ma cuisine est minuscule, l'intervention est-elle possible ?",
                      "Oui, c'est le cas le plus courant en tertiaire. Nous travaillons avec un "
                      "matériel compact et nous bâchons avant d'ouvrir. Le facteur limitant n'est "
                      "pas la taille de la cuisine mais l'accès aux trappes du conduit, que nous "
                      "vérifions au premier rendez-vous."),
        "faq_vitres": ("Nettoyez-vous les cloisons vitrées intérieures ?",
                       "Oui, et c'est souvent plus utile que la façade : ce sont elles que les "
                       "occupants voient de près toute la journée. Un passage mensuel sur les "
                       "cloisons et les portes vitrées suffit à tenir un plateau."),
    },
    {
        "slug": "neuilly-sur-seine", "nom": "Neuilly-sur-Seine", "cp": "92200", "dept": "92",
        "lat": 48.8846, "lon": 2.2697,
        "tissu":
            "Neuilly réunit un commerce de bouche de qualité le long de l'avenue de Neuilly et de la "
            "rue de Chartres, une forte densité de professions libérales recevant en cabinet, et des "
            "agences immobilières nombreuses sur un marché de standing.",
        "acces":
            "Stationnement payant et tendu, parkings souterrains à hauteur limitée. Notre véhicule "
            "passe sous les 1,90 m qui limitent la plupart des sous-sols neuilléens, et nous "
            "apportons eau et électricité.",
        "hotte":
            "Les cuisines neuilléennes sont souvent installées dans des immeubles anciens de "
            "standing, où la contrainte dominante est la copropriété : horaires encadrés, parties "
            "communes à protéger, nuisances d'odeurs surveillées de près. Le travail technique est "
            "classique — hotte, filtres, conduit — mais l'organisation doit être irréprochable, et "
            "c'est souvent là que les prestataires achoppent.",
        "vitres":
            "Beaucoup de fenêtres anciennes à petits bois et de hauteurs sous plafond de trois "
            "mètres, en cabinet comme en commerce. Ce sont les vitrages les plus longs à faire "
            "correctement : chaque carreau demande son passage, et les mastics anciens retiennent la "
            "poussière que le lavage fait ensuite couler sur la vitre. Nous comptons au vantail.",
        "faq_hotte": ("La copropriété impose des horaires, est-ce compatible ?",
                      "Oui, nous travaillons dans la plage autorisée et nous protégeons les "
                      "parties communes traversées. C'est une contrainte d'organisation, pas une "
                      "contrainte technique : il faut simplement la connaître avant, pas la "
                      "découvrir sur place."),
        "faq_vitres": ("Comment comptez-vous une fenêtre à petits bois ?",
                       "Au vantail, pas au mètre carré. Une fenêtre à six carreaux demande "
                       "plusieurs fois le temps d'une baie de même surface. Nous comptons les "
                       "vantaux sur photos et le devis est ferme avant que nous venions."),
    },
    {
        "slug": "courbevoie", "nom": "Courbevoie", "cp": "92400", "dept": "92",
        "lat": 48.8975, "lon": 2.2567,
        "tissu":
            "Courbevoie vit à l'ombre immédiate de La Défense : une partie du quartier d'affaires "
            "est sur son territoire, et la restauration y sert des milliers de salariés sur un "
            "créneau de deux heures. Le centre ancien et le quartier Bécon gardent par ailleurs un "
            "commerce de proximité actif.",
        "acces":
            "Les dalles et les parkings du quartier d'affaires imposent des accès réglementés, à "
            "organiser avec le gestionnaire du site. En centre ancien, l'accès est celui d'une "
            "commune ordinaire.",
        "hotte":
            "La restauration de flux du quartier d'affaires produit un encrassement massif et "
            "concentré : friteuses et grillades à plein régime sur deux heures, cinq jours par "
            "semaine. C'est le profil qui demande le rythme le plus soutenu — deux passages par an "
            "au minimum, et un suivi hebdomadaire des filtres par l'équipe, ce que le texte "
            "réglementaire prévoit explicitement.",
        "vitres":
            "Façades hautes, verre partout, et une limite nette : seuls les premiers niveaux sont "
            "accessibles à la perche depuis le sol. Nous nous concentrons sur les rez-de-chaussée "
            "commerciaux, les halls, les sas et l'intérieur, et nous le disons clairement avant le "
            "devis plutôt que de laisser un étage non fait.",
        "faq_hotte": ("À quel rythme nettoyer une cuisine de restauration rapide ?",
                      "Deux passages par an au minimum sur la hotte et le conduit, et un nettoyage "
                      "ou un remplacement des filtres au moins une fois par semaine par votre "
                      "équipe — c'est ce que prévoit la réglementation applicable aux grandes "
                      "cuisines. À très fort volume, trois passages annuels sont plus réalistes."),
        "faq_vitres": ("Intervenez-vous sur les tours de La Défense ?",
                       "Pas en façade au-delà de trois niveaux : cela demande une nacelle ou un "
                       "cordiste, et ce n'est pas notre métier. Nous traitons les commerces de "
                       "pied d'immeuble, les halls et les surfaces intérieures."),
    },
    {
        "slug": "issy-les-moulineaux", "nom": "Issy-les-Moulineaux", "cp": "92130",
        "dept": "92", "lat": 48.8239, "lon": 2.2730,
        "tissu":
            "Issy-les-Moulineaux est l'un des pôles tertiaires les plus denses d'Île-de-France, avec "
            "une concentration de sièges de médias et de technologies, et une restauration "
            "d'entreprise dimensionnée en conséquence.",
        "acces":
            "Les immeubles récents disposent de parkings accessibles et de quais de livraison, ce "
            "qui simplifie l'intervention. Les horaires, eux, sont strictement hors activité.",
        "hotte":
            "La restauration collective d'entreprise domine : plusieurs lignes de cuisson, un "
            "circuit d'extraction long, et une exigence de traçabilité portée par le service "
            "sécurité du site. Nous intervenons sur fermeture programmée et nous remettons un relevé "
            "daté, zone par zone, destiné à être rangé dans le livret d'entretien de "
            "l'établissement.",
        "vitres":
            "Les grandes façades vitrées d'Issy sont la vitrine des entreprises qui les occupent, et "
            "l'eau déminéralisée y prend tout son sens : sur ces surfaces lisses et très étendues, "
            "le moindre voile calcaire se lit de loin. Les premiers niveaux et l'ensemble des "
            "surfaces intérieures sont de notre ressort ; au-delà, non.",
        "faq_hotte": ("Pouvez-vous intervenir pendant une fermeture d'entreprise ?",
                      "C'est le créneau que nous préférons : site vide, aucune contrainte de "
                      "service, et le temps de faire la ligne d'extraction complète. Les semaines "
                      "de fermeture d'août et de fin d'année se réservent plusieurs mois à "
                      "l'avance."),
        "faq_vitres": ("Pourquoi l'eau déminéralisée plutôt qu'un produit à vitres ?",
                       "Parce que la trace blanche qui reste au séchage n'est pas de la saleté, "
                       "c'est le calcaire de l'eau du réseau, particulièrement présent en "
                       "Île-de-France. Une eau privée de ses minéraux sèche sans rien laisser : il "
                       "n'y a pas de produit à repasser, donc pas de film à voiler la vitre."),
    },
    {
        "slug": "nanterre", "nom": "Nanterre", "cp": "92000", "dept": "92",
        "lat": 48.8924, "lon": 2.2069,
        "tissu":
            "Nanterre combine la préfecture des Hauts-de-Seine, l'université, la frange ouest de La "
            "Défense et des zones d'activité étendues. La restauration y est largement collective ou "
            "tournée vers le midi des salariés et des étudiants.",
        "acces":
            "Les zones d'activité et les campus sont faciles d'accès et de stationnement. Nanterre "
            "est à une trentaine de kilomètres de notre atelier : le délai habituel y est de 48 à "
            "72 h, et nous regroupons les interventions de l'ouest sur une même tournée.",
        "hotte":
            "La restauration collective d'université et d'administration fonctionne par calendrier : "
            "des périodes de production intense, puis des fermetures longues. C'est la configuration "
            "la plus confortable pour un dégraissage complet, à condition de réserver le créneau à "
            "l'avance — les vacances scolaires sont demandées par tout le monde en même temps.",
        "vitres":
            "Façades de bureaux récentes, halls administratifs, bâtiments universitaires : des "
            "surfaces grandes, régulières, et pour partie accessibles depuis le sol. Les portes et "
            "les halls à forte fréquentation sont les seules surfaces qui demandent un passage "
            "rapproché.",
        "faq_hotte": ("Faut-il réserver longtemps à l'avance pour les vacances scolaires ?",
                      "Oui, deux à trois mois. Tous les établissements visent les mêmes semaines, "
                      "et le nombre de créneaux de nuit ou de fermeture est limité. Une date fixée "
                      "en début d'année scolaire évite de se retrouver sans solution."),
        "faq_vitres": ("Quel est le délai d'intervention à Nanterre ?",
                       "Habituellement 48 à 72 h : nous sommes à une trentaine de kilomètres, et "
                       "nous regroupons les interventions de l'ouest francilien sur une même "
                       "tournée. Les frais de déplacement sont annoncés avant que vous validiez."),
    },
    {
        "slug": "vincennes", "nom": "Vincennes", "cp": "94300", "dept": "94",
        "lat": 48.8478, "lon": 2.4390,
        "tissu":
            "Vincennes a un commerce de centre-ville exceptionnellement dense pour sa taille : rue "
            "du Midi, avenue de Paris, marché couvert. Boulangeries, pâtisseries, fromageries, "
            "restaurants de quartier s'y succèdent sur quelques centaines de mètres.",
        "acces":
            "Les rues commerçantes sont étroites et le stationnement très contraint, avec des "
            "plages de livraison limitées au matin. Nous intervenons avant 7 h 30, qui est de toute "
            "façon le bon créneau pour un commerce de bouche.",
        "hotte":
            "La densité de commerces de bouche fait de Vincennes un cas particulier : beaucoup de "
            "petits fournils et de cuisines de restaurant dans des immeubles d'habitation anciens, "
            "avec des conduits partagés ou mitoyens. La question de savoir qui entretient quoi se "
            "pose souvent, et elle doit être tranchée avant l'intervention plutôt qu'après.",
        "vitres":
            "Vitrines de commerce de bouche, à reprendre chaque semaine : le film gras intérieur des "
            "buées de cuisson est ici le vrai sujet, bien plus que la poussière extérieure. C'est "
            "lui qui éteint la couleur des produits en vitrine, et il demande un dégraissage avant "
            "lavage.",
        "faq_hotte": ("Mon conduit est mitoyen avec le commerce voisin, que faire ?",
                      "Il faut d'abord établir qui est responsable de quoi, ce qui se lit dans les "
                      "baux et le règlement de copropriété. En pratique, la solution la plus "
                      "efficace est une intervention unique sur le circuit complet, refacturée au "
                      "prorata : un conduit partagé nettoyé par moitié ne sert à rien."),
        "faq_vitres": ("Pourquoi ma vitrine de pâtisserie reste-t-elle voilée ?",
                       "À cause du film de gras sucré que les buées de cuisson déposent à "
                       "l'intérieur du verre. Un produit à vitres l'étale sans le dissoudre : la "
                       "vitre paraît propre de près et reste voilée de loin. Il faut un dégraissant "
                       "alcalin, puis un rinçage à l'eau déminéralisée."),
    },
    {
        "slug": "creteil", "nom": "Créteil", "cp": "94000", "dept": "94",
        "lat": 48.7904, "lon": 2.4556,
        "tissu":
            "Préfecture du Val-de-Marne, Créteil réunit administrations, centre hospitalier "
            "universitaire, université et un centre commercial régional. La restauration y est "
            "majoritairement collective ou de chaîne.",
        "acces":
            "Les grands équipements disposent de quais de livraison et de parkings, ce qui facilite "
            "l'intervention. Créteil est à une vingtaine de kilomètres de notre atelier, pour un "
            "délai habituel de 48 à 72 h.",
        "hotte":
            "Les cuisines de restauration collective de Créteil sont parmi les plus volumineuses que "
            "nous rencontrions, et les plus encadrées. L'enjeu n'y est pas la technique mais la "
            "méthode : une ligne complète, trappe par trappe, un essai d'extraction après remontage, "
            "et un relevé daté qui permette à l'exploitant de tenir son livret d'entretien à jour.",
        "vitres":
            "Halls, circulations, cloisons vitrées et portes à très forte fréquentation. Dans un "
            "équipement recevant du public, les portes vitrées se marquent en une demi-journée : "
            "c'est la surface à reprendre souvent, le reste tient au trimestre.",
        "faq_hotte": ("Vérifiez-vous l'extraction après le nettoyage ?",
                      "Oui, systématiquement : le remontage et l'essai d'extraction font partie de "
                      "l'intervention, pas de la suite. Une cuisine doit être opérationnelle au "
                      "service suivant, et c'est aussi la seule façon de constater le gain réel "
                      "obtenu sur le débit."),
        "faq_vitres": ("Comment organiser le nettoyage dans un bâtiment ouvert au public ?",
                       "Zone par zone, aux heures de faible fréquentation, sans jamais fermer un "
                       "accès. Les halls et les portes se font tôt le matin ; les cloisons "
                       "intérieures peuvent se traiter en journée sans gêner personne."),
    },
    {
        "slug": "ivry-sur-seine", "nom": "Ivry-sur-Seine", "cp": "94200", "dept": "94",
        "lat": 48.8133, "lon": 2.3875,
        "tissu":
            "Ivry-sur-Seine mêle habitat, activité industrielle reconvertie et un tissu de "
            "restauration de quartier dense le long de l'avenue Maurice-Thorez et autour de la "
            "mairie. Les anciens locaux d'activité reconvertis en bureaux et en ateliers y sont "
            "nombreux.",
        "acces":
            "Le stationnement est praticable hors heures de pointe, et les anciens locaux "
            "d'activité disposent souvent d'une cour ou d'un accès véhicule. Ivry est à une "
            "quinzaine de kilomètres de notre atelier.",
        "hotte":
            "Les cuisines ivryennes sont pour beaucoup installées dans du bâti ancien, avec des "
            "conduits qui n'ont pas été conçus pour l'usage actuel du local. C'est la situation où "
            "le dégraissage révèle parfois autre chose : une section insuffisante, une trappe "
            "manquante, un tracé qui multiplie les coudes. Nous le signalons, même quand cela ne "
            "nous concerne pas, parce que c'est l'information utile.",
        "vitres":
            "Vitrines de quartier d'un côté, grandes verrières d'ateliers reconvertis de l'autre. "
            "Les verrières sont le beau travail et le travail long : petits bois nombreux, mastics "
            "anciens, hauteurs qui demandent la perche. Elles se comptent au carreau.",
        "faq_hotte": ("Que se passe-t-il si mon conduit n'est pas conforme ?",
                      "Nous vous le disons, avec ce que nous avons constaté et où. Le dégraissage "
                      "d'un conduit sous-dimensionné ou mal tracé reste utile, mais il ne règle "
                      "pas le défaut de conception : il faut alors un installateur. Nous ne faisons "
                      "pas de travaux sur le réseau et nous n'avons donc aucun intérêt à vous "
                      "annoncer un problème qui n'existe pas."),
        "faq_vitres": ("Nettoyez-vous les verrières d'anciens ateliers ?",
                       "Oui, depuis le sol et jusqu'à trois niveaux, à la perche et à l'eau "
                       "déminéralisée. Au-delà, ou pour une verrière de toit, il faut un moyen "
                       "d'accès en hauteur que nous ne mettons pas en œuvre."),
    },
]


# ---------------------------------------------------------------------------
# COMMUNES — NETTOYAGE D'APPARTEMENT (particuliers)
# ---------------------------------------------------------------------------
# Le nettoyage d'appartement n'est pas du ménage hebdomadaire : c'est un
# passage ponctuel et complet — grand ménage, état des lieux, après
# déménagement, remise en état d'une location courte durée. Ce qui change
# d'une commune à l'autre, c'est le parc de logements : un haussmannien, une
# tour des années 1970 et un loft d'atelier ne demandent ni le même temps ni
# le même matériel.
VILLES_APPART = [
    {
        "slug": "boulogne-billancourt", "nom": "Boulogne-Billancourt", "cp": "92100",
        "dept": "92", "lat": 48.8352, "lon": 2.2409,
        "parc":
            "Boulogne aligne trois générations de logements : l'immeuble de rapport des années 1930, "
            "souvent en bel état mais avec des parquets anciens et des huisseries bois ; les "
            "programmes des années 1970 autour du pont de Sèvres ; et les résidences récentes du "
            "Trapèze, livrées avec des sols lisses et de grandes baies vitrées.",
        "angle":
            "La demande dominante est le grand ménage avant ou après déménagement : un logement "
            "vide se nettoie entièrement, y compris les intérieurs de placards, les plinthes et les "
            "surfaces que les meubles masquaient. C'est aussi la prestation qui pèse le plus dans "
            "un état des lieux de sortie, et où les retenues sur dépôt de garantie se décident.",
        "pratique":
            "Le stationnement est tendu partout et beaucoup d'immeubles n'ont qu'un sous-sol à "
            "hauteur limitée. Notre véhicule est léger et nous apportons l'eau et l'électricité : "
            "aucun accès technique ne vous est demandé, ce qui compte dans un logement déjà vidé.",
        "faq": ("Que comprend un grand ménage avant état des lieux ?",
                "Sols, plinthes, intérieurs de placards, vitres et encadrements, sanitaires "
                "détartrés, cuisine complète four et réfrigérateur compris, interrupteurs et "
                "poignées. C'est la liste que les agences vérifient. Nous la parcourons avec vous "
                "avant de commencer, et nous vous disons franchement ce qui ne se rattrapera pas — "
                "un joint définitivement marqué, par exemple."),
    },
    {
        "slug": "montreuil", "nom": "Montreuil", "cp": "93100", "dept": "93",
        "lat": 48.8638, "lon": 2.4485,
        "parc":
            "Montreuil est la commune où le parc est le plus varié de la petite couronne : pavillons "
            "des Murs à pêches, lofts d'anciens ateliers du bas Montreuil, immeubles récents autour "
            "des stations de métro. Les volumes reconvertis y posent une question précise : de "
            "grandes surfaces, de grandes hauteurs, et beaucoup de verre.",
        "angle":
            "Dans un loft, le nettoyage complet se joue sur deux points que les prestations "
            "standard laissent de côté : les verrières et les parties hautes, et les sols béton ou "
            "résine, qui ne se lavent pas comme un carrelage. Nous venons voir avant de chiffrer "
            "quand la surface dépasse l'appartement classique.",
        "pratique":
            "Les rues du bas Montreuil sont étroites, le stationnement difficile. Notre autonomie "
            "en eau et en électricité nous permet de travailler sans place à proximité immédiate ni "
            "branchement dans le logement.",
        "faq": ("Nettoyez-vous les verrières et les parties hautes d'un loft ?",
                "Depuis le sol et à la perche, jusqu'à une hauteur raisonnable, oui. Au-delà, ou "
                "pour une verrière de toit, il faut un moyen d'accès en hauteur que nous ne mettons "
                "pas en œuvre : nous vous le disons au devis plutôt que de laisser la partie haute "
                "non faite."),
    },
    {
        "slug": "saint-denis", "nom": "Saint-Denis", "cp": "93200", "dept": "93",
        "lat": 48.9362, "lon": 2.3574,
        "parc":
            "Saint-Denis est en renouvellement permanent : programmes neufs livrés en continu dans "
            "la Plaine et autour du stade, réhabilitations du centre ancien, et un parc social "
            "important. Les logements neufs arrivent souvent avec des résidus de chantier que la "
            "livraison n'a pas éliminés.",
        "angle":
            "La demande la plus fréquente est le nettoyage de fin de chantier léger, après la "
            "remise des clés d'un logement neuf : poussière de plâtre dans les gorges de fenêtres, "
            "film de protection sur les sols, étiquettes et traces de colle sur les vitrages. Ce "
            "n'est pas du ménage, c'est un décrassage, et il se fait une seule fois mais bien.",
        "pratique":
            "Saint-Denis est à huit kilomètres de notre atelier : nous y intervenons sous 24 à "
            "48 h. Les résidences neuves disposent presque toujours d'un accès véhicule, ce qui "
            "simplifie l'intervention.",
        "faq": ("Mon appartement est neuf, pourquoi faut-il le nettoyer ?",
                "Parce que la poussière de plâtre et de découpe reste dans les gorges de fenêtres, "
                "les rails de placard et les angles de plinthes, et qu'elle ressort à chaque "
                "ouverture pendant des mois. Un décrassage complet à la livraison évite cela, et "
                "c'est le seul moment où le logement est vide, donc le seul où il peut être fait "
                "entièrement."),
    },
    {
        "slug": "pantin", "nom": "Pantin", "cp": "93500", "dept": "93",
        "lat": 48.8944, "lon": 2.4090,
        "parc":
            "Pantin combine un centre ancien aux immeubles de rapport modestes, des programmes "
            "récents le long du canal de l'Ourcq, et d'anciens locaux industriels reconvertis en "
            "logements atypiques. Les parquets anciens du centre et les sols lisses du canal "
            "demandent des traitements opposés.",
        "angle":
            "Beaucoup de locations courte durée à Pantin, et c'est la prestation la plus exigeante "
            "en régularité : une remise en état entre deux séjours ne tolère ni retard ni "
            "approximation sur la salle de bain et la cuisine, qui sont les deux points que les "
            "voyageurs notent. Nous travaillons sur une liste fixe, toujours la même, ce qui est la "
            "seule façon de ne rien oublier.",
        "pratique":
            "Pantin est à douze kilomètres de notre atelier, pour un délai habituel de 24 à 48 h. "
            "Les remises en état de location se planifient à date et heure fixes, entre le départ "
            "et l'arrivée suivante.",
        "faq": ("Intervenez-vous entre deux locations courte durée ?",
                "Oui, sur créneau fixe. Le point à régler est l'accès : boîte à clés, code ou clé "
                "confiée. Une fois cela établi, l'intervention se fait sans que vous ayez à être "
                "présent, et nous vous envoyons les photos du logement prêt si vous le souhaitez."),
    },
    {
        "slug": "vincennes", "nom": "Vincennes", "cp": "94300", "dept": "94",
        "lat": 48.8478, "lon": 2.4390,
        "parc":
            "Vincennes est faite d'immeubles de rapport de la fin du XIXᵉ et du début du XXᵉ siècle, "
            "très bien tenus : parquets à points de Hongrie, moulures, cheminées de marbre, "
            "huisseries bois à petits bois. C'est un parc où le nettoyage demande de la prudence "
            "plus que de la puissance.",
        "angle":
            "Sur ces logements, l'erreur coûteuse est le produit : un parquet ancien non vitrifié "
            "ne supporte pas l'eau en quantité, et un marbre de cheminée se tache définitivement à "
            "l'acide — y compris celui d'un détartrant ménager courant. Nous identifions les "
            "matériaux avant de commencer, et nous le disons quand une surface relève d'un artisan "
            "plutôt que de nous.",
        "pratique":
            "Stationnement contraint, immeubles souvent sans ascenseur ou avec un ascenseur étroit. "
            "Notre matériel est compact et transportable à la main, ce qui règle la question des "
            "étages.",
        "faq": ("Comment nettoyez-vous un parquet ancien non vitrifié ?",
                "À l'humide très mesuré, sans jamais mouiller, et avec un produit neutre. Un "
                "parquet ancien gonfle et grise à l'eau : la serpillière classique est ce qui "
                "l'abîme le plus sûrement. Si le parquet est déjà très marqué, le nettoyage le "
                "rendra propre mais pas neuf, et nous préférons vous le dire avant."),
    },
    {
        "slug": "levallois-perret", "nom": "Levallois-Perret", "cp": "92300", "dept": "92",
        "lat": 48.8939, "lon": 2.2874,
        "parc":
            "Levallois est la commune la plus densément bâtie de France : des appartements compacts, "
            "souvent récents ou rénovés, avec des cuisines ouvertes et des salles de bains de petite "
            "surface. La densité a une conséquence pratique : tout est petit, y compris les accès.",
        "angle":
            "Dans un appartement compact, le résultat se joue sur la cuisine et la salle de bains, "
            "qui concentrent l'essentiel du travail réel. Le détartrage complet de la robinetterie "
            "et des parois de douche — l'eau francilienne est calcaire — change davantage "
            "l'impression générale que le reste du logement réuni.",
        "pratique":
            "Stationnement de surface quasi impossible en journée. Nous intervenons tôt, ou en "
            "sous-sol quand l'immeuble en dispose. Notre matériel passe dans un ascenseur étroit.",
        "faq": ("Le calcaire sur une paroi de douche peut-il vraiment partir ?",
                "Dans la plupart des cas, oui, avec un détartrant adapté et du temps de pose plutôt "
                "qu'avec de la force. Ce qui ne part pas, c'est le verre déjà attaqué : un dépôt "
                "laissé des années finit par marquer la surface elle-même, et aucun produit ne la "
                "reconstitue. Nous vous le dirons après avoir essayé, pas avant."),
    },
    {
        "slug": "neuilly-sur-seine", "nom": "Neuilly-sur-Seine", "cp": "92200", "dept": "92",
        "lat": 48.8846, "lon": 2.2697,
        "parc":
            "Neuilly aligne de part et d'autre de l'avenue Charles-de-Gaulle des immeubles "
            "haussmanniens et Art déco aux appartements familiaux généreux : parquets anciens, "
            "moulures, parfois du mobilier de valeur, et des hauteurs sous plafond de trois mètres "
            "qui changent le temps de travail sur les murs et les vitrages.",
        "angle":
            "Sur ce type de logement, le nettoyage complet est d'abord un travail de diagnostic : "
            "chaque matière — parquet ancien, marbre, laiton, pierre, textile — a son produit et "
            "ses interdits. Un seul produit universel passé partout est ce qui cause les dommages "
            "les plus durables, et ils ne se voient qu'après séchage.",
        "pratique":
            "Parkings souterrains à hauteur limitée, stationnement payant et tendu. Notre véhicule "
            "passe sous les 1,90 m de la plupart des sous-sols neuilléens, et nous travaillons sans "
            "rien déplacer de lourd.",
        "faq": ("Prenez-vous en charge le nettoyage des textiles et des tapis en même temps ?",
                "Oui, c'est fréquent sur un grand ménage : canapés, fauteuils, matelas et tapis se "
                "traitent par injection-extraction, le même jour que le logement si le planning le "
                "permet. Les tapis de laine relèvent d'un protocole à part, sans vapeur, et nous le "
                "précisons au devis."),
    },
    {
        "slug": "courbevoie", "nom": "Courbevoie", "cp": "92400", "dept": "92",
        "lat": 48.8975, "lon": 2.2567,
        "parc":
            "Courbevoie juxtapose les tours d'habitation de la frange de La Défense, les immeubles "
            "de rapport du centre et le tissu pavillonnaire et de petits collectifs de Bécon. Les "
            "tours ont de grandes surfaces vitrées et des sols lisses ; Bécon, des logements plus "
            "classiques.",
        "angle":
            "Dans un logement en tour, les baies vitrées font la différence : elles représentent "
            "une part importante des surfaces, elles sont exposées, et leur nettoyage intérieur "
            "transforme la luminosité du logement. Nous les traitons à l'eau déminéralisée, "
            "encadrements et rails de coulissant compris — c'est dans les rails que se loge "
            "l'essentiel.",
        "pratique":
            "Les résidences disposent le plus souvent d'un parking visiteurs ou d'un accès livraison. "
            "Courbevoie est à une vingtaine de kilomètres de notre atelier, pour un délai de 48 à "
            "72 h.",
        "faq": ("Nettoyez-vous l'extérieur des baies vitrées en étage ?",
                "Depuis l'intérieur seulement, quand la menuiserie permet d'accéder à la face "
                "extérieure sans se mettre en danger. Une baie fixe en étage élevé ne peut pas être "
                "traitée par l'extérieur sans moyen d'accès en hauteur, ce que nous ne faisons pas, "
                "et nous ne prendrons pas le risque."),
    },
    {
        "slug": "asnieres-sur-seine", "nom": "Asnières-sur-Seine", "cp": "92600",
        "dept": "92", "lat": 48.9050, "lon": 2.2850,
        "parc":
            "Asnières mêle immeubles de rapport du début du XXᵉ siècle, petits collectifs des années "
            "1960 et pavillons, avec un bord de Seine en renouvellement. Beaucoup de logements de "
            "trois à quatre pièces, loués et reloués, donc souvent remis en état.",
        "angle":
            "La rotation locative fait du nettoyage de sortie la demande principale : le logement "
            "est vide, et c'est le seul moment où tout est accessible. L'objectif est précis — "
            "limiter la retenue sur le dépôt de garantie — et il se joue sur des points que le "
            "locataire sortant néglige presque toujours : four, réfrigérateur, joints de salle de "
            "bains, intérieurs de placards.",
        "pratique":
            "Stationnement praticable en dehors des heures de pointe. Asnières est à une vingtaine "
            "de kilomètres de l'atelier, pour un délai de 48 à 72 h ; nous regroupons les "
            "interventions de l'ouest sur une même tournée.",
        "faq": ("Un nettoyage de sortie évite-t-il la retenue sur le dépôt de garantie ?",
                "Il supprime le motif le plus fréquent de retenue, qui est l'état de propreté. Il "
                "ne couvre pas l'usure ni les dégradations, qui relèvent d'une autre discussion "
                "avec le bailleur. Nous vous remettons le détail de ce qui a été fait, ce qui est "
                "utile si l'état des lieux est contesté."),
    },
    {
        "slug": "saint-ouen-sur-seine", "nom": "Saint-Ouen-sur-Seine", "cp": "93400",
        "dept": "93", "lat": 48.9100, "lon": 2.3330,
        "parc":
            "Saint-Ouen s'est largement renouvelée autour des Docks et du nouveau quartier des "
            "puces : logements neufs livrés par tranches, anciens ateliers reconvertis, et un parc "
            "ancien du centre en réhabilitation. Les deux extrêmes se côtoient d'une rue à l'autre.",
        "angle":
            "Deux demandes distinctes : le décrassage de livraison dans le neuf — poussière de "
            "chantier, films de protection, traces de colle sur les vitrages — et le grand ménage "
            "de rénovation dans l'ancien, après des travaux qui ont laissé de la poussière de plâtre "
            "partout. Dans les deux cas, ce n'est pas du ménage : c'est un passage unique et "
            "complet.",
        "pratique":
            "Saint-Ouen est à dix kilomètres de notre atelier, pour un délai de 24 à 48 h. Les "
            "programmes neufs disposent d'un accès véhicule ; en centre ancien, nous travaillons "
            "sans place réservée grâce à notre autonomie.",
        "faq": ("Faites-vous le nettoyage après des travaux de rénovation ?",
                "Oui, sur un logement non occupé et une fois les gravats évacués — cela, c'est "
                "l'affaire de l'entreprise de travaux. Nous prenons la poussière de plâtre, qui "
                "s'infiltre partout et revient plusieurs fois : un nettoyage après travaux demande "
                "toujours deux passes, et c'est prévu dans le devis."),
    },
    {
        "slug": "les-lilas", "nom": "Les Lilas", "cp": "93260", "dept": "93",
        "lat": 48.8790, "lon": 2.4190,
        "parc":
            "Les Lilas est une commune de petite taille et de densité moyenne, avec des immeubles "
            "de rapport, des petits collectifs et un tissu pavillonnaire préservé. Les logements y "
            "sont souvent familiaux et occupés longtemps, ce qui change la nature de la demande.",
        "angle":
            "Un logement occupé depuis dix ou quinze ans accumule ce qu'un ménage courant ne traite "
            "jamais : dessus de placards, arrières de meubles, gorges de fenêtres, joints de "
            "carrelage, intérieur de hotte de cuisine. C'est le grand ménage annuel, celui qui "
            "remet le logement à niveau et qu'on ne fait pas soi-même parce qu'il demande de "
            "déplacer et de démonter.",
        "pratique":
            "Les Lilas est à une dizaine de kilomètres de notre atelier, pour un délai de 24 à "
            "48 h. Le stationnement résidentiel est praticable.",
        "faq": ("Que fait un grand ménage que je ne fais pas moi-même ?",
                "Les surfaces qui demandent de déplacer ou de démonter : arrières et dessus de "
                "meubles, intérieur de la hotte de cuisine, grilles de ventilation, joints de "
                "carrelage, gorges et rails de fenêtres, intérieurs de placards vidés. C'est deux à "
                "quatre heures de travail qu'on ne tient pas sur un week-end, et le résultat se "
                "voit pendant des mois."),
    },
    {
        "slug": "noisy-le-grand", "nom": "Noisy-le-Grand", "cp": "93160", "dept": "93",
        "lat": 48.8486, "lon": 2.5527,
        "parc":
            "Noisy-le-Grand réunit les grands ensembles d'architecture des années 1980 du Mont "
            "d'Est, des résidences récentes et un vaste tissu pavillonnaire. Les logements y sont "
            "généralement spacieux, avec des surfaces vitrées généreuses et des balcons ou "
            "terrasses.",
        "angle":
            "Les grandes surfaces changent l'arbitrage : sur un cinq pièces, un nettoyage complet "
            "demande une demi-journée à deux intervenants, et il vaut mieux cibler que survoler. "
            "Nous définissons les priorités avec vous avant de commencer — en général cuisine, "
            "salles d'eau et vitrages, qui portent les trois quarts de l'effet visible.",
        "pratique":
            "Noisy est à une vingtaine de kilomètres de notre atelier, par l'A3 puis l'A86 ou "
            "l'A4 : délai habituel de 48 à 72 h. Stationnement aisé.",
        "faq": ("Combien de temps faut-il pour un grand appartement ?",
                "Comptez une demi-journée pour un quatre ou cinq pièces, parfois plus s'il est "
                "meublé et occupé. Le devis est ferme : s'il faut davantage de temps que prévu, "
                "c'est notre affaire, pas la vôtre. En revanche nous vous disons à l'avance si la "
                "surface demande deux intervenants."),
    },
    {
        "slug": "le-blanc-mesnil", "nom": "Le Blanc-Mesnil", "cp": "93150", "dept": "93",
        "lat": 48.9386, "lon": 2.4644,
        "parc":
            "C'est notre commune : l'atelier est au 2 rue Poussin. Le parc blanc-mesnilois mêle "
            "pavillons, petits collectifs et résidences, avec beaucoup de logements familiaux "
            "occupés durablement.",
        "angle":
            "Être sur place change ce que nous pouvons proposer : une intervention le jour même, un "
            "passage de reprise qui ne coûte presque rien en déplacement, et la possibilité de "
            "revenir si un point n'a pas été fait à votre satisfaction. C'est le seul endroit où "
            "nous pouvons tenir cela sans conditions.",
        "pratique":
            "Frais de déplacement nuls ou symboliques, délais que nous ne tenons nulle part "
            "ailleurs. Souvent le jour même en cas d'urgence — un état des lieux avancé, un "
            "logement à rendre le lendemain.",
        "faq": ("Pouvez-vous venir aujourd'hui au Blanc-Mesnil ?",
                "Souvent, oui : appelez-nous, nous regardons la tournée du jour. C'est notre "
                "commune, le trajet ne pèse rien dans l'organisation, et c'est la seule où nous "
                "pouvons répondre à une urgence sans réorganiser la journée entière."),
    },
    {
        "slug": "aulnay-sous-bois", "nom": "Aulnay-sous-Bois", "cp": "93600", "dept": "93",
        "lat": 48.9386, "lon": 2.4938,
        "parc":
            "Aulnay est largement pavillonnaire, avec des quartiers de petits collectifs et des "
            "résidences plus récentes. Les maisons individuelles y dominent la demande, ce qui change "
            "la nature du travail : plus de surfaces au sol, plus de vitrages, des escaliers, "
            "souvent un garage ou une véranda.",
        "angle":
            "Dans une maison, le nettoyage complet gagne à être organisé par étage et à inclure ce "
            "que les appartements n'ont pas : véranda, escalier, vitrages de toit accessibles depuis "
            "l'intérieur, et les abords immédiats de l'entrée. Nous commençons par le haut et nous "
            "descendons, pour ne pas repasser derrière nous.",
        "pratique":
            "Aulnay est à cinq kilomètres de notre atelier, soit dix minutes : nous y intervenons "
            "souvent le jour même en cas d'urgence, et les frais de déplacement y sont de 5 €.",
        "faq": ("Intervenez-vous dans les maisons, pas seulement les appartements ?",
                "Oui, et c'est l'essentiel de la demande à Aulnay. Une maison demande plus de temps "
                "qu'un appartement de même nombre de pièces, à cause des escaliers et des surfaces "
                "vitrées. Nous venons voir ou nous travaillons sur photos, puis le devis est ferme."),
    },
]


# ---------------------------------------------------------------------------
# DOSSIERS TECHNIQUES
# ---------------------------------------------------------------------------
# Pages de fond, écrites pour être utiles à quelqu'un qui cherche une réponse
# précise, pas pour aligner des mots-clés. Chacune répond à une question qu'un
# exploitant ou un particulier se pose réellement, et donne la réponse même
# quand elle ne nous arrange pas.
#
# Le cadre réglementaire cité est l'arrêté du 25 juin 1980 portant règlement
# de sécurité contre l'incendie dans les établissements recevant du public,
# article GC 21, applicable aux ERP dotés de grandes cuisines. Les termes
# employés sont les siens : ramonage des conduits d'évacuation, vérification
# de leur vacuité, nettoyage ou remplacement des filtres, livret d'entretien
# annexé au registre de sécurité. Rien n'y est ajouté.
#
# L'attestation remise à l'issue d'une intervention est une attestation de
# nettoyage et d'entretien : elle décrit ce que MathClean a fait, datée et
# détaillée, et se range dans le livret d'entretien que l'exploitant tient.
# Elle ne vaut pas attestation de conformité de l'installation, ni
# vérification annuelle GC 22 — qui relève d'un technicien compétent ou d'un
# organisme agréé. Cette distinction est tenue partout : la confondre serait
# vendre une couverture que le client n'a pas.
DOSSIERS = [
    {
        "slug": "obligation-nettoyage-hotte-restaurant",
        "cat": "Hottes et extraction",
        "audience": "pro",
        "service": "nettoyage-hottes-paris",
        "h1": "Nettoyage de hotte en restaurant : ce que la réglementation impose",
        "title": "Nettoyage de hotte : obligation réglementaire en restaurant",
        "meta": "Ramonage annuel, filtres chaque semaine, livret d'entretien : ce que l'arrêté "
                "du 25 juin 1980 impose réellement à un exploitant.",
        "lead": "Un ramonage par an au minimum, des filtres nettoyés chaque semaine, et un "
                "livret d'entretien que l'exploitant tient lui-même. Voici le texte, ce qu'il "
                "dit exactement, et ce qu'il ne dit pas.",
        "cle": "Ramonage des conduits d'évacuation : au moins une fois par an.",
        "sections": [
            ("Le texte applicable", [
                "L'obligation ne vient pas d'une recommandation de la profession mais d'un texte : "
                "l'arrêté du 25 juin 1980 portant règlement de sécurité contre l'incendie et la "
                "panique dans les établissements recevant du public. Sa section 7, « Entretien et "
                "vérifications », tient en deux articles — GC 21 pour l'entretien, GC 22 pour la "
                "vérification — et s'applique aux établissements dotés de grandes cuisines, "
                "c'est-à-dire dès que la puissance utile totale des appareils de cuisson et de "
                "remise en température dépasse 20 kW. Cela couvre la très grande majorité des "
                "restaurants, brasseries, boulangeries et cuisines collectives recevant du public.",
                "Le texte distingue trois opérations distinctes, et c'est cette distinction qui est "
                "le plus souvent perdue : le nettoyage des filtres, le nettoyage du circuit "
                "d'extraction, et le ramonage des conduits d'évacuation. Elles n'ont ni la même "
                "fréquence ni le même exécutant.",
                "Les voici dans les termes du texte. Les filtres sont nettoyés ou remplacés au "
                "moins une fois par semaine. Les conduits d'évacuation sont ramonés au moins une "
                "fois par an, et leur vacuité est vérifiée à cette occasion. Le circuit d'extraction "
                "est nettoyé aussi souvent que nécessaire — le texte ne fixe pas de chiffre, parce "
                "qu'un conduit de pizzeria et un conduit de salon de thé ne se chargent pas au même "
                "rythme.",
            ]),
            ("Qui fait quoi", [
                "Les filtres relèvent de l'équipe de cuisine. Une fois par semaine au minimum, ils "
                "sont retirés, dégraissés ou remplacés. Ce n'est pas une prestation, c'est une "
                "tâche d'exploitation, et c'est la plus rentable de toutes : un filtre propre "
                "retient la graisse avant qu'elle n'entre dans le conduit, donc il espace les "
                "nettoyages de conduit.",
                "Le ramonage annuel et le nettoyage du circuit relèvent d'un prestataire, parce "
                "qu'ils demandent d'ouvrir les trappes de visite, d'accéder à la ligne complète et "
                "de remonter l'installation en état de fonctionner. C'est cette partie que nous "
                "assurons : hotte, filtres, et conduits d'extraction.",
                "La responsabilité, en revanche, reste entière du côté de l'exploitant. Le texte "
                "prévoit un livret d'entretien annexé au registre de sécurité de l'établissement, "
                "où sont notées les dates des opérations. C'est l'exploitant qui le tient, et c'est "
                "lui qui le présente en cas de contrôle.",
            ]),
            ("L'article GC 22 : la vérification annuelle, qui est autre chose", [
                "C'est le second article de la section 7, et il est régulièrement confondu avec le "
                "premier. Dans les établissements des quatre premières catégories, les "
                "installations de cuisson font l'objet d'une vérification annuelle par un "
                "technicien compétent ou un organisme agréé. Elle porte notamment sur l'état "
                "d'entretien des appareils et sur la ventilation des locaux : évacuation de l'air "
                "vicié, des buées et des graisses, et fonctionnement du dispositif d'extraction. "
                "Elle est consignée au registre de sécurité.",
                "Les établissements classés en 5<sup>e</sup> catégorie — la plupart des petits "
                "restaurants — relèvent d'un autre régime, celui de l'arrêté du 22 juin 1990. "
                "Vérifiez votre catégorie avant d'appliquer l'un ou l'autre : c'est la première "
                "question à poser à votre service de prévention.",
                "Retenez la différence, parce qu'elle décide de qui vous devez appeler. GC 21, "
                "c'est faire nettoyer. GC 22, c'est faire vérifier. Un dégraissage ne remplace pas "
                "une vérification, et une vérification ne nettoie rien.",
            ]),
            ("Ce que nous remettons après l'intervention", [
                "Une attestation de nettoyage et d'entretien de hotte, datée et détaillée : les "
                "zones traitées — hotte, filtres, plénum —, les trappes de visite ouvertes, la "
                "longueur de conduit reprise, l'état constaté avant, et le résultat de l'essai "
                "d'extraction après remontage. Elle se range dans le livret d'entretien annexé à "
                "votre registre de sécurité, et c'est elle que votre assureur demande après un "
                "sinistre.",
                "Cette attestation dit ce que nous avons fait, où et quand. Elle ne vaut pas "
                "attestation de conformité de votre installation : la conformité ne se juge pas "
                "sur un dégraissage, elle se juge sur l'installation elle-même, et ce n'est pas le "
                "métier d'un prestataire de nettoyage. Elle ne vaut pas davantage vérification "
                "annuelle au titre de GC 22, qui revient à un technicien compétent ou à un "
                "organisme agréé.",
                "Un prestataire de nettoyage qui vous promet les trois dans le même document vous "
                "vend une couverture que vous n'avez pas — et c'est après le sinistre que vous "
                "vous en apercevrez.",
            ]),
            ("Le point à vérifier de votre côté", [
                "Votre contrat d'assurance multirisque professionnelle comporte presque "
                "certainement une clause relative à l'entretien des installations de cuisson et "
                "d'extraction. Les formulations varient d'un assureur à l'autre, et les "
                "conséquences d'un entretien non documenté en cas de sinistre aussi. Lisez-la, ou "
                "demandez-la à votre courtier : c'est une lecture de dix minutes qui peut peser "
                "très lourd.",
                "C'est aussi la raison pour laquelle le livret d'entretien n'est pas une formalité "
                "administrative. En cas de départ de feu dans un conduit, la question posée sera "
                "celle des dates, et la réponse ne s'improvise pas après coup.",
            ]),
        ],
        "faq": [
            ("Un nettoyage par an suffit-il ?",
             "C'est le plancher réglementaire pour le ramonage des conduits, pas une "
             "recommandation technique. Le texte demande en outre que le circuit d'extraction soit "
             "nettoyé « aussi souvent que nécessaire », ce qui veut dire deux passages par an dans "
             "la plupart des restaurants, et davantage en friture, grillade ou four à bois."),
            ("Quelle différence entre GC 21 et GC 22 ?",
             "GC 21 impose l'entretien : filtres chaque semaine, ramonage annuel des conduits, "
             "nettoyage du circuit aussi souvent que nécessaire. GC 22 impose une vérification "
             "annuelle des installations de cuisson par un technicien compétent ou un organisme "
             "agréé, consignée au registre de sécurité. Le premier, c'est faire nettoyer ; le "
             "second, faire vérifier. Nous assurons le premier et nous en délivrons l'attestation ; "
             "le second est une prestation distincte, que nous ne réalisons pas."),
            ("Qui peut me demander mon livret d'entretien ?",
             "Les services de contrôle compétents lors d'une visite de sécurité de l'établissement, "
             "et votre assureur en cas de sinistre. Dans les deux cas, ce sont les dates qui sont "
             "regardées : un livret vide a le même effet qu'un entretien non fait."),
            ("Les filtres doivent-ils vraiment être nettoyés chaque semaine ?",
             "C'est ce que prévoit le texte : nettoyés ou remplacés au moins une fois par semaine. "
             "C'est aussi, en pratique, le geste le plus utile de tout le dispositif, parce qu'un "
             "filtre propre arrête la graisse avant le conduit."),
        ],
    },
    {
        "slug": "risque-incendie-graisse-hotte",
        "cat": "Hottes et extraction",
        "audience": "pro",
        "service": "nettoyage-hottes-paris",
        "h1": "Pourquoi la graisse accumulée dans une hotte est un risque d'incendie",
        "title": "Graisse dans une hotte : le mécanisme du risque d'incendie",
        "meta": "Comment la graisse d'un conduit d'extraction devient un combustible, pourquoi "
                "le feu s'y propage vite, et ce qui réduit réellement le risque.",
        "lead": "La graisse qui tapisse un conduit d'extraction n'est pas de la saleté : c'est un "
                "combustible, placé exactement là où passe l'air chaud. Voici le mécanisme, sans "
                "dramatisation inutile.",
        "cle": "Un conduit encrassé est un combustible dans un courant d'air chaud.",
        "sections": [
            ("Ce qui s'accumule, et où", [
                "Toute cuisson à la matière grasse vaporise une partie de cette matière. Les "
                "particules sont entraînées par le flux d'air de la hotte, elles traversent les "
                "filtres — jamais totalement —, puis elles condensent sur les parois dès que la "
                "température de l'air baisse. C'est pour cela que le dépôt est maximal non pas dans "
                "la hotte, qui est la partie visible, mais dans le premier coude du conduit, juste "
                "après.",
                "Le dépôt n'est pas homogène. Frais, il est huileux et coulant. Repris plusieurs "
                "fois par la chaleur, il se polymérise : il devient dur, sec, adhérent, et il ne "
                "part plus au dégraissant. C'est un dépôt ancien qui pose le vrai problème, pas le "
                "film de la semaine.",
            ]),
            ("Le mécanisme de l'incendie", [
                "Trois conditions sont réunies dans un conduit encrassé. Un combustible : le dépôt "
                "de graisse. Un comburant : l'air, en mouvement permanent et en quantité. Et une "
                "source d'allumage possible : une flamme de piano qui monte, un flambage, une "
                "friteuse en surchauffe, une étincelle. Il manque rarement plus d'un élément.",
                "Ce qui rend un feu de conduit particulier, c'est sa propagation. Le conduit est un "
                "volume fermé, étroit, ventilé, et il traverse les structures du bâtiment, souvent "
                "verticalement jusqu'en toiture. Le feu y progresse à l'abri des regards, il "
                "chauffe les parois sur son passage, et il peut ressortir loin de la cuisine. C'est "
                "la raison pour laquelle le texte réglementaire s'intéresse aux conduits et pas "
                "seulement aux hottes.",
                "Un feu de graisse ne s'éteint pas à l'eau : l'eau projetée sur de la graisse "
                "enflammée se vaporise instantanément et disperse le combustible. C'est une donnée "
                "que toute équipe de cuisine devrait avoir en tête avant d'en avoir besoin.",
            ]),
            ("Ce qui réduit réellement le risque", [
                "Par ordre d'efficacité réelle, et non d'apparence. D'abord les filtres, nettoyés "
                "ou remplacés chaque semaine : c'est ce qui limite la quantité de graisse qui entre "
                "dans le conduit, et c'est gratuit. Ensuite le dégraissage du circuit complet, "
                "conduits compris, à un rythme adapté au mode de cuisson. Enfin la vérification de "
                "l'extraction, parce qu'un débit qui chute augmente la condensation et donc le "
                "dépôt.",
                "Ce qui ne réduit pas le risque : nettoyer la partie visible de la hotte. C'est "
                "l'opération la plus fréquente et la plus trompeuse. Une hotte inox brillante "
                "au-dessus d'un conduit tapissé donne exactement la mauvaise impression, et c'est "
                "celle qui rassure le plus.",
            ]),
            ("L'indice à surveiller sans attendre", [
                "Une extraction qui tire moins qu'avant. C'est le signal le plus fiable, et il est "
                "progressif donc facile à ne pas voir : un conduit qui s'encrasse perd de la section "
                "utile, le débit chute, les buées commencent à rester en cuisine, puis à passer en "
                "salle. Le jour où la cuisine devient difficilement tenable aux heures de pointe, "
                "le dépôt est déjà important.",
                "L'autre indice est le plafond : un jaunissement au-dessus des zones de cuisson "
                "signifie que les buées ne sont pas captées. Dans ce cas, le dégraissage est "
                "nécessaire mais il ne suffira pas — il faut aussi regarder le dimensionnement de "
                "l'installation.",
            ]),
        ],
        "faq": [
            ("À partir de quelle épaisseur de dépôt le risque devient-il sérieux ?",
             "Il n'existe pas de seuil universel, et méfiez-vous de qui vous en annonce un au "
             "millimètre près. Ce qui compte autant que l'épaisseur, c'est la nature du dépôt : une "
             "graisse polymérisée, sèche et dure, est plus dangereuse qu'un film huileux plus épais. "
             "Nous ouvrons les trappes et nous vous montrons."),
            ("Mon assurance peut-elle refuser d'indemniser un sinistre ?",
             "C'est une question à poser à votre assureur, pas à nous, et la réponse dépend des "
             "clauses de votre contrat. Ce que nous constatons, c'est que la question des dates "
             "d'entretien arrive systématiquement dans un dossier de sinistre lié à l'extraction. "
             "Vérifiez votre clause d'entretien avant d'en avoir besoin."),
            ("Un extincteur en cuisine suffit-il ?",
             "Un extincteur adapté aux feux de graisse — classe F — est indispensable et doit être "
             "à portée, mais il traite un départ de feu sur l'appareil de cuisson. Il ne peut rien "
             "contre un feu déjà parti dans un conduit, qui est inaccessible. La prévention et "
             "l'intervention sont deux sujets distincts."),
        ],
    },
    {
        "slug": "frequence-nettoyage-hotte-professionnelle",
        "cat": "Hottes et extraction",
        "audience": "pro",
        "service": "nettoyage-hottes-paris",
        "h1": "À quelle fréquence faire nettoyer sa hotte professionnelle",
        "title": "Fréquence de nettoyage d'une hotte professionnelle",
        "meta": "Un, deux ou trois passages par an ? La fréquence dépend du mode de cuisson, pas "
                "du nombre de couverts. Repères par métier et critères de décision.",
        "lead": "Le ramonage annuel est le minimum réglementaire. La bonne fréquence, elle, dépend "
                "de ce que vous cuisinez — et pas du tout de vos heures d'ouverture.",
        "cle": "Ce qui décide du rythme : le mode de cuisson, pas le nombre d'heures.",
        "sections": [
            ("L'erreur de raisonnement la plus courante", [
                "Beaucoup d'exploitants calculent la fréquence sur le temps d'ouverture : un "
                "service unique au déjeuner justifierait un nettoyage plus espacé qu'un service "
                "continu. C'est faux, et c'est une erreur coûteuse.",
                "Ce qui charge un conduit, c'est la quantité de matière grasse vaporisée. Une "
                "cuisine qui fait deux heures de friture et de grillade intensive par jour vaporise "
                "autant, parfois plus, qu'une cuisine ouverte en continu mais travaillant "
                "majoritairement au four et à la sauteuse. Le bon critère est le mode de cuisson "
                "dominant.",
            ]),
            ("Repères par mode de cuisson", [
                "Friture et grillade dominantes — kebab, friterie, snack, restauration rapide : "
                "deux passages par an au minimum, trois à fort volume. C'est le profil qui charge "
                "le plus vite.",
                "Four à bois ou charbon — pizzeria, grillades au feu de bois : deux à trois "
                "passages par an, avec une particularité. La suie ne se dissout pas, elle se "
                "décolle : le conduit demande un ramonage mécanique en plus du dégraissage, et le "
                "conduit de fumée du four est un circuit distinct de celui de la hotte.",
                "Cuisson mixte — restaurant traditionnel, brasserie : un à deux passages par an, "
                "deux au-delà d'une centaine de couverts par service.",
                "Four et buées sucrées — boulangerie, pâtisserie, crêperie : deux passages par an "
                "dans la plupart des cas. Le dépôt est moins abondant mais plus difficile, parce "
                "que la farine et le sucre forment avec le gras une croûte dure qui ne réagit pas "
                "comme une graisse de friture.",
                "Restauration collective : un à deux passages par an selon le nombre de lignes de "
                "cuisson, à caler sur les périodes de fermeture.",
            ]),
            ("Les trois signaux qui disent de ne pas attendre", [
                "L'extraction tire moins qu'avant. C'est le signal le plus fiable et le plus "
                "négligé, parce qu'il s'installe progressivement. Un conduit qui perd de la section "
                "perd du débit, et la cuisine devient peu à peu difficile aux heures de pointe.",
                "Les buées passent en salle, ou le plafond jaunit au-dessus des zones de cuisson. "
                "Les buées non captées se déposent ailleurs, et c'est visible.",
                "Les odeurs se plaignent chez les voisins. En immeuble d'habitation, c'est la "
                "première cause de conflit en copropriété, et c'est presque toujours un circuit "
                "encrassé plutôt qu'un défaut de conception. Un dégraissage complet règle souvent "
                "ce que des mois de discussion n'avaient pas réglé.",
            ]),
            ("Comment arrêter un rythme et s'y tenir", [
                "Le plus simple est de fixer deux dates dans l'année, liées à un repère "
                "d'exploitation — la fermeture annuelle, une période creuse — plutôt qu'à un "
                "calendrier abstrait. Un rendez-vous programmé se tient ; une intervention « à "
                "prévoir » se reporte indéfiniment.",
                "Le premier passage sert aussi à calibrer le suivant : nous ouvrons les trappes, "
                "nous constatons l'état réel, et nous vous disons si six mois est le bon intervalle "
                "ou s'il faut resserrer. C'est un réglage, pas une estimation faite à l'avance.",
            ]),
        ],
        "faq": [
            ("Puis-je espacer les nettoyages si mon équipe entretient bien les filtres ?",
             "Oui, et c'est précisément le levier. Des filtres nettoyés chaque semaine arrêtent une "
             "part importante de la graisse avant le conduit, ce qui allonge réellement "
             "l'intervalle. Le ramonage annuel des conduits reste cependant le plancher "
             "réglementaire, quel que soit le soin apporté aux filtres."),
            ("Faut-il la même fréquence pour la hotte et pour le conduit ?",
             "Non. La hotte et les filtres se traitent plus souvent que le conduit, et une partie "
             "relève de votre équipe. Le conduit, lui, demande une intervention complète avec "
             "ouverture des trappes : c'est ce passage-là qui se compte en nombre de fois par an."),
            ("Comment savoir si mon intervalle actuel est le bon ?",
             "En regardant l'état du conduit à l'ouverture des trappes. S'il est propre, "
             "l'intervalle peut être allongé ; s'il est déjà chargé, il faut le resserrer. C'est le "
             "seul critère sérieux, et il demande d'ouvrir plutôt que de supposer."),
        ],
    },
    {
        "slug": "degraissage-conduit-extraction",
        "cat": "Hottes et extraction",
        "audience": "pro",
        "service": "nettoyage-hottes-paris",
        "h1": "Dégraissage d'un conduit d'extraction : comment cela se passe vraiment",
        "title": "Dégraissage de conduit d'extraction : méthode et étapes",
        "meta": "Trappes de visite, dégraissage, ramonage mécanique, remontage et essai "
                "d'extraction : le déroulé réel d'une intervention en cuisine.",
        "lead": "Une hotte propre ne dit rien du conduit. Voici ce que contient une intervention "
                "complète, étape par étape, et comment reconnaître une prestation qui s'arrête à "
                "la partie visible.",
        "cle": "Sans ouverture des trappes de visite, le conduit n'est pas traité.",
        "sections": [
            ("Le préalable : les trappes de visite", [
                "Un conduit d'extraction ne se nettoie que par ses trappes de visite. Sans accès "
                "intermédiaire, on ne traite que les premiers mètres depuis la hotte, et le reste "
                "de la ligne reste intact. C'est la différence, invisible sur une facture, entre un "
                "dégraissage complet et un dégraissage de façade.",
                "La première chose que nous faisons est donc d'inventorier les trappes existantes "
                "et de repérer ce qui n'est pas accessible. Quand il en manque sur une ligne longue, "
                "nous le disons : la pose relève d'un installateur, pas de nous, et un conduit "
                "vertical de trois étages sans trappe intermédiaire ne peut pas être nettoyé sur "
                "toute sa hauteur. Nous préférons l'annoncer que de facturer un travail partiel "
                "présenté comme complet.",
            ]),
            ("Protection et démontage", [
                "La cuisine est bâchée avant la première ouverture : plans de travail, "
                "équipements, sols. Ce n'est pas une précaution de confort — ce qui sort d'un "
                "conduit chargé est une matière noire et grasse qui tache durablement.",
                "Les filtres sont retirés et traités séparément, par trempage. La hotte est "
                "démontée dans ses parties démontables, y compris le plénum, qui est souvent "
                "l'endroit le plus chargé de l'ensemble et le plus régulièrement oublié.",
            ]),
            ("Dégraissage et ramonage : deux opérations différentes", [
                "Le dégraissage chimique s'attaque à la graisse. Un alcalin est appliqué, on "
                "respecte un temps de pose — c'est lui qui fait le travail, pas la force du bras —, "
                "puis on rince. Sur un dépôt polymérisé, une seule application ne suffit pas et il "
                "faut recommencer.",
                "Le ramonage mécanique s'attaque à ce qui ne se dissout pas : la suie. Un conduit "
                "de four à bois ou à charbon en produit, et aucun produit chimique ne l'enlève. "
                "Elle se décolle à la brosse. Les deux opérations sont distinctes, et une cuisine "
                "qui a un four à bois a besoin des deux.",
                "Les points sur lesquels nous insistons parce qu'ils sont les plus souvent sautés : "
                "le plénum, les coudes de départ — là où la vitesse d'air chute et où le dépôt est "
                "maximal —, et le caisson du moteur d'extraction, dont les pales encrassées "
                "expliquent une bonne partie des pertes de débit.",
            ]),
            ("Remontage et essai : la partie qui n'est pas optionnelle", [
                "Tout est remonté, les trappes refermées, les filtres remis en place propres ou "
                "remplacés. Puis nous mettons l'extraction en marche et nous vérifions qu'elle "
                "fonctionne. Cela paraît évident ; c'est pourtant l'étape que l'on retrouve le plus "
                "souvent absente, et une cuisine rendue non opérationnelle avant un service est un "
                "problème sérieux.",
                "L'essai sert aussi à constater le gain : sur un conduit très chargé, la "
                "différence de débit est immédiatement perceptible. C'est la seule preuve "
                "tangible du travail fait sur une partie que vous ne voyez pas.",
                "Vous recevez ensuite un relevé daté : zones traitées, trappes ouvertes, longueur "
                "de conduit reprise, état constaté avant, résultat de l'essai. Il est fait pour "
                "être rangé dans le livret d'entretien annexé à votre registre de sécurité, que "
                "vous tenez vous-même.",
            ]),
        ],
        "faq": [
            ("Combien de temps la cuisine est-elle immobilisée ?",
             "De trois à six heures pour une cuisine de restaurant de taille courante, davantage "
             "sur une ligne longue ou une cuisine collective. Nous travaillons de nuit, après le "
             "dernier service ou le jour de fermeture, de façon à ce que la cuisine soit "
             "opérationnelle au service suivant."),
            ("Comment savoir si le conduit a vraiment été traité ?",
             "Demandez quelles trappes ont été ouvertes, et faites-vous montrer l'intérieur avant "
             "et après. Un prestataire qui a fait le travail n'a aucune difficulté à répondre. Si "
             "la réponse est vague ou si aucune trappe n'a été ouverte, seule la hotte a été "
             "nettoyée."),
            ("Pouvez-vous poser une trappe de visite manquante ?",
             "Non, c'est une intervention sur le réseau, qui relève d'un installateur. Nous "
             "signalons l'absence et l'endroit où elle serait nécessaire. Nous n'avons aucun "
             "intérêt commercial à vous annoncer des travaux que nous ne réalisons pas, ce qui rend "
             "le constat plus fiable."),
        ],
    },
    {
        "slug": "extraction-cuisine-qui-tire-mal",
        "cat": "Hottes et extraction",
        "audience": "pro",
        "service": "nettoyage-hottes-paris",
        "h1": "Mon extraction de cuisine tire mal : les causes, dans l'ordre",
        "title": "Extraction de cuisine qui tire mal : diagnostic",
        "meta": "Buées en salle, chaleur aux heures de pointe, plaintes d'odeurs : les causes "
                "d'une extraction défaillante, de la moins chère à la plus coûteuse.",
        "lead": "Avant d'envisager des travaux sur le réseau, il y a trois hypothèses à écarter, "
                "et elles coûtent de moins en moins cher à vérifier dans cet ordre.",
        "cle": "Commencez par le moins coûteux : filtres, conduit, moteur, puis l'installation.",
        "sections": [
            ("Les symptômes et ce qu'ils disent", [
                "Les buées restent en cuisine, puis passent en salle. La chaleur devient difficile "
                "à tenir aux heures de pointe. Le plafond jaunit au-dessus des zones de cuisson. "
                "Les voisins se plaignent d'odeurs. Chacun de ces signes dit la même chose : le "
                "débit d'extraction réel est inférieur à ce qu'il devrait être.",
                "Le point important est que cette perte est progressive. Elle s'installe sur des "
                "mois, l'équipe s'y habitue, et le moment où l'on s'en inquiète est toujours bien "
                "après le moment où elle a commencé. C'est pour cela qu'un constat vaut mieux "
                "qu'une impression.",
            ]),
            ("Hypothèse 1 — les filtres", [
                "C'est la première à écarter parce qu'elle est gratuite. Des filtres saturés "
                "réduisent le débit de façon considérable, et ils se saturent en quelques jours en "
                "friture ou en grillade. Le texte réglementaire prévoit un nettoyage ou un "
                "remplacement au moins une fois par semaine ; dans beaucoup de cuisines, c'est plus "
                "souvent qu'il le faudrait réellement.",
                "Retirez-les, dégraissez-les complètement, remettez-les et mesurez la différence. "
                "Si l'extraction redevient correcte, le problème était là, et il reviendra au même "
                "rythme.",
            ]),
            ("Hypothèse 2 — le conduit", [
                "C'est la cause la plus fréquente d'une baisse durable. Un conduit encrassé perd de "
                "la section utile, et la perte de débit est proportionnelle. Comme le dépôt "
                "s'accumule surtout dans les coudes et hors de vue, rien ne le signale : la hotte "
                "peut être impeccable et le conduit à moitié obstrué.",
                "La vérification demande d'ouvrir les trappes de visite. C'est la seule façon de "
                "savoir, et c'est aussi ce qui permet de chiffrer un dégraissage sur un constat "
                "plutôt que sur une estimation.",
            ]),
            ("Hypothèse 3 — le moteur d'extraction", [
                "Le caisson du moteur et ses pales s'encrassent comme le reste, et des pales "
                "chargées de graisse perdent une partie de leur rendement. C'est une cause "
                "régulièrement ignorée parce que le caisson est souvent en toiture ou en gaine "
                "technique, donc jamais ouvert.",
                "Le nettoyage du caisson fait partie d'une intervention complète. Un moteur "
                "fatigué ou sous-dimensionné, en revanche, relève du remplacement, et donc d'un "
                "installateur.",
            ]),
            ("Hypothèse 4 — l'installation elle-même", [
                "Si les trois premières hypothèses sont écartées, le problème est de conception : "
                "section insuffisante, tracé qui multiplie les coudes, compensation d'air absente — "
                "une cuisine ne peut pas extraire si rien ne rentre —, ou moteur sous-dimensionné "
                "pour les appareils installés. C'est fréquent dans les locaux qui ont changé "
                "d'activité sans que le réseau soit repris.",
                "Cela relève d'un installateur, pas de nous. Nous le signalons quand nous le "
                "constatons, avec ce que nous avons vu et où, parce que c'est l'information utile — "
                "et parce que nous ne vendons pas de travaux sur le réseau, ce qui rend le constat "
                "désintéressé.",
            ]),
        ],
        "faq": [
            ("Un dégraissage va-t-il régler mon problème d'extraction ?",
             "Souvent, oui, et c'est l'hypothèse à tester en premier parce qu'elle est la moins "
             "coûteuse. Pas toujours : si l'installation est sous-dimensionnée ou si la "
             "compensation d'air manque, le dégraissage améliorera les choses sans les résoudre. "
             "Nous vous dirons ce que nous avons constaté."),
            ("Les plaintes d'odeurs des voisins viennent-elles de là ?",
             "Dans la grande majorité des cas que nous rencontrons en immeuble d'habitation, oui. "
             "Un circuit encrassé tire moins, les buées trouvent un autre chemin, et les odeurs "
             "sortent où elles peuvent. C'est l'hypothèse à vérifier avant d'engager une discussion "
             "longue avec la copropriété."),
            ("Faites-vous les travaux sur le réseau d'extraction ?",
             "Non. Nous dégraissons et nous ramonons hotte, filtres et conduits ; la modification "
             "du réseau, la pose de trappes et le remplacement d'un moteur relèvent d'un "
             "installateur. Nous constatons et nous orientons, sans intervenir."),
        ],
    },
]

# Suite des dossiers : vitrerie, entretien régulier, appartement. Écrits
# séparément pour que le fichier reste lisible, ajoutés à la même liste.
DOSSIERS += [
    {
        "slug": "nettoyage-vitrine-commerce-frequence",
        "cat": "Vitrerie",
        "audience": "pro",
        "service": "nettoyage-vitres-paris",
        "h1": "Vitrine de commerce : à quelle fréquence la faire nettoyer",
        "title": "Nettoyage de vitrine de commerce : quelle fréquence",
        "meta": "Hebdomadaire, bimensuel ou mensuel : ce qui décide du rythme, et pourquoi la "
                "zone basse et la poignée se reprennent plus souvent que le reste.",
        "lead": "Une vitrine ne se salit pas uniformément. Comprendre où elle se salit permet de "
                "payer moins de passages complets tout en ayant une devanture toujours nette.",
        "cle": "Trois zones, trois rythmes : poignée, bas de vitrage, vitrage complet.",
        "sections": [
            ("Pourquoi une vitrine se salit par zones", [
                "Trois sources, trois endroits. Les mains, à hauteur de poignée et de regard, "
                "laissent des marques en quelques heures en rue passante. Les projections du "
                "trottoir — eau de pluie chargée, poussière, sel en hiver — salissent les trente "
                "premiers centimètres au-dessus du sol. Et le film gras du trafic, fait de "
                "particules de freinage et de résidus d'hydrocarbures, se dépose lentement sur "
                "toute la surface.",
                "Ces trois salissures n'ont ni le même rythme ni le même traitement. Les deux "
                "premières se reprennent en quelques minutes ; la troisième demande un dégraissage "
                "complet. Un commerce qui fait laver sa vitrine entièrement chaque semaine paie "
                "trois fois pour un travail dont une partie seulement était nécessaire.",
            ]),
            ("Le rythme qui fonctionne en pratique", [
                "En rue très passante : un nettoyage complet hebdomadaire, avec la poignée et la "
                "zone basse reprises à chaque passage. En rue moyennement passante : complet toutes "
                "les deux semaines, reprise hebdomadaire des zones de contact. En rue calme ou en "
                "galerie : complet mensuel.",
                "La façade haute, l'enseigne et le bandeau se traitent séparément, au trimestre, et "
                "c'est souvent ce qui est le plus oublié. Une enseigne encrassée perd en luminosité "
                "de façon progressive, donc imperceptible — jusqu'à ce qu'on la nettoie et que la "
                "différence saute aux yeux.",
            ]),
            ("Le cas particulier du commerce de bouche", [
                "Une boulangerie, une pâtisserie ou un restaurant ont un problème que les autres "
                "commerces n'ont pas : le film gras intérieur. Les buées de cuisson déposent sur la "
                "face interne du verre une pellicule de gras, sucrée en pâtisserie, qui ne se voit "
                "pas de face mais diffuse la lumière et éteint la couleur des produits exposés.",
                "C'est la raison pour laquelle une vitrine de boulangerie peut sembler terne alors "
                "qu'elle vient d'être lavée : un produit à vitres étale le film sans le dissoudre. "
                "Il faut un dégraissage alcalin de la face intérieure, puis un rinçage à l'eau "
                "déminéralisée. Une fois par mois suffit, mais il faut le faire.",
            ]),
            ("Ce qu'il faut regarder sur un devis de vitrerie", [
                "Trois points. Premièrement, ce qui est compris exactement : le verre seul, ou le "
                "verre plus les encadrements et les appuis ? Les encadrements sont l'essentiel du "
                "résultat visible, et c'est dans l'appui que se loge la saleté qui salira à nouveau "
                "la vitre à la première pluie.",
                "Deuxièmement, l'eau utilisée. L'eau du réseau francilien est calcaire : elle "
                "laisse au séchage une trace blanche qui n'est pas de la saleté mais du minéral. "
                "Une eau déminéralisée sèche sans rien laisser, et c'est ce qui dispense d'essuyer.",
                "Troisièmement, les deux faces ou une seule. Une vitrine lavée à l'extérieur "
                "seulement reste voilée vue de la rue si la face intérieure est grasse. Cela paraît "
                "évident et c'est pourtant une imprécision fréquente sur les devis.",
            ]),
        ],
        "faq": [
            ("Pourquoi des traces blanches réapparaissent-elles après le nettoyage ?",
             "Parce que l'eau utilisée était calcaire. Ce que vous voyez n'est pas de la saleté "
             "revenue, c'est le minéral laissé par l'eau en séchant. Une eau déminéralisée supprime "
             "le phénomène — et avec lui la nécessité d'essuyer, qui est ce qui laisse des traces "
             "de chiffon."),
            ("Les encadrements et les appuis sont-ils compris ?",
             "Chez nous, oui, dans le même passage. C'est important : un appui chargé de poussière "
             "fait couler une coulure sur la vitre à la première pluie, et le nettoyage du verre "
             "seul ne tient alors que quelques jours."),
            ("Peut-on nettoyer une vitrine en plein soleil ?",
             "Mieux vaut l'éviter. En plein soleil, l'eau sèche plus vite que la raclette ne "
             "descend et le résultat est marqué quelle que soit la méthode. C'est pour cela que "
             "nous intervenons tôt le matin, quand le verre est encore froid."),
        ],
    },
    {
        "slug": "traces-blanches-vitres-calcaire",
        "cat": "Vitrerie",
        "audience": "mixte",
        "service": "nettoyage-vitres-paris",
        "h1": "Traces blanches sur les vitres : d'où elles viennent et comment les supprimer",
        "title": "Traces blanches sur les vitres : la cause et la solution",
        "meta": "La trace blanche qui reste après nettoyage n'est pas de la saleté : c'est le "
                "calcaire de l'eau du réseau. Pourquoi l'eau déminéralisée règle le problème.",
        "lead": "Vous lavez, vous essuyez, et le voile revient en séchant. Ce n'est pas une "
                "question de produit ni de technique : c'est l'eau.",
        "cle": "La trace blanche est du minéral, pas de la saleté.",
        "sections": [
            ("Ce que vous voyez réellement", [
                "L'eau du réseau contient des minéraux dissous, principalement du calcium et du "
                "magnésium. En Île-de-France, elle est nettement calcaire sur la plus grande partie "
                "du territoire. Quand une goutte sèche sur du verre, l'eau s'évapore et les "
                "minéraux restent : ils forment un dépôt blanchâtre, en gouttes ou en voile selon la "
                "façon dont l'eau a séché.",
                "La conséquence est contre-intuitive : plus vous lavez à l'eau du robinet, plus "
                "vous déposez de minéral. Le verre est propre de saleté et sale de calcaire. C'est "
                "exactement ce qui se passe quand une vitre paraît pire après nettoyage qu'avant.",
            ]),
            ("Pourquoi le produit et le chiffon ne règlent pas le problème", [
                "Un produit à vitres contient un solvant et un tensioactif, qui dissolvent les "
                "corps gras et la poussière. Aucun des deux n'enlève le minéral de l'eau de rinçage "
                "— et le produit lui-même, s'il n'est pas complètement retiré, laisse à son tour un "
                "film qui voile le verre à contre-jour.",
                "L'essuyage ne fait que déplacer le problème. Un chiffon, même en microfibre, laisse "
                "des fibres et des marques sur une grande surface, et il étale le minéral plutôt "
                "que de l'enlever. C'est pour cela qu'une baie vitrée essuyée au chiffon est "
                "toujours marquée vue de biais.",
                "Le vinaigre blanc, souvent conseillé, fonctionne partiellement : son acidité "
                "dissout le dépôt déjà formé. Mais il ne change rien à l'eau de rinçage, donc le "
                "voile revient au séchage suivant. Et il est à éviter sur les joints et les "
                "menuiseries anciennes.",
            ]),
            ("L'eau déminéralisée, et pourquoi elle change tout", [
                "Une eau privée de ses minéraux — par osmose inverse ou par résine échangeuse "
                "d'ions — ne laisse rien en séchant. Il n'y a donc plus rien à essuyer : la vitre "
                "est rincée puis laissée sécher seule, et c'est précisément l'absence d'essuyage "
                "qui donne un résultat sans trace.",
                "C'est aussi ce qui permet de travailler à la perche télescopique sur les hauteurs "
                "accessibles depuis le sol : on ne peut pas essuyer à quatre mètres, donc la seule "
                "méthode possible est une eau qui sèche propre.",
                "Sur une vitre très entartrée par des années d'arrosage automatique ou de "
                "ruissellement, l'eau déminéralisée seule ne suffit pas : il faut d'abord dissoudre "
                "le dépôt existant, puis rincer. Et si le verre est déjà attaqué — c'est le cas "
                "après plusieurs années —, le dépôt a marqué la surface elle-même et rien ne la "
                "reconstitue. Nous le disons après avoir essayé, pas avant.",
            ]),
            ("Si vous le faites vous-même", [
                "Trois gestes qui améliorent nettement le résultat sans matériel particulier. "
                "Travaillez à l'ombre ou tôt le matin : au soleil, l'eau sèche avant que vous ayez "
                "fini et la trace est inévitable. Utilisez très peu de produit — un excès de "
                "tensioactif est la première cause de voile. Et terminez à la raclette en "
                "bandes qui se chevauchent, en essuyant la lame à chaque passage, plutôt qu'au "
                "chiffon.",
                "Pour le dernier centimètre en bas du vitrage, où l'eau s'accumule, un chiffon sec "
                "propre passé une seule fois vaut mieux qu'un essuyage général.",
            ]),
        ],
        "faq": [
            ("Le vinaigre blanc est-il une bonne solution ?",
             "Pour dissoudre un dépôt de calcaire déjà formé, oui, ponctuellement. Pas comme "
             "méthode régulière : il ne change rien à l'eau de rinçage, donc le voile revient, et "
             "son acidité est à éviter sur les joints, les mastics et les menuiseries anciennes."),
            ("Un dépôt de calcaire ancien part-il toujours ?",
             "Pas toujours. Un dépôt laissé plusieurs années finit par attaquer la surface du verre "
             "elle-même, et aucun produit ne la reconstitue. Nous essayons, et nous vous disons "
             "franchement si la limite est atteinte plutôt que d'insister au risque de rayer."),
            ("Faut-il de l'eau déminéralisée pour les vitres de chez soi ?",
             "Pas nécessairement pour une fenêtre que vous pouvez essuyer facilement. Cela devient "
             "décisif sur les grandes surfaces, les baies et tout ce qui se travaille à la perche, "
             "c'est-à-dire tout ce qu'on ne peut pas essuyer."),
        ],
    },
    {
        "slug": "nettoyage-vitres-en-hauteur-limites",
        "cat": "Vitrerie",
        "audience": "pro",
        "service": "nettoyage-vitres-paris",
        "h1": "Nettoyage de vitres en hauteur : ce que nous faisons et ce que nous ne faisons pas",
        "title": "Nettoyage de vitres en hauteur : nos limites",
        "meta": "Jusqu'à trois niveaux depuis le sol à la perche et à l'eau déminéralisée. "
                "Au-delà, nacelle ou cordiste : nous ne le faisons pas, et nous le disons avant.",
        "lead": "Une page qui dit surtout ce que nous ne prenons pas. C'est utile : la plupart des "
                "mauvaises surprises en vitrerie viennent d'un étage non fait que personne n'avait "
                "annoncé.",
        "cle": "Trois niveaux depuis le sol. Au-delà, ce n'est pas notre métier.",
        "sections": [
            ("Ce que la perche permet, et jusqu'où", [
                "Une perche télescopique alimentée en eau déminéralisée atteint confortablement les "
                "trois premiers niveaux d'un bâtiment, soit une dizaine de mètres selon les "
                "hauteurs d'étage. L'opérateur reste au sol : il n'y a pas de travail en hauteur, "
                "donc pas de risque de chute, et c'est de loin la solution la plus économique.",
                "Deux conditions. Il faut un recul suffisant au pied de la façade — une perche "
                "s'utilise en oblique, pas à la verticale contre le mur — et un sol stable. Une "
                "façade sur rue étroite, un balcon en surplomb ou une haie dense peuvent empêcher "
                "l'accès alors que la hauteur, elle, serait atteignable.",
            ]),
            ("Ce que nous ne faisons pas, et pourquoi nous le disons", [
                "Au-delà de trois niveaux, ou quand le recul manque, la façade demande un moyen "
                "d'accès en hauteur : nacelle, échafaudage, ou travail sur cordes. Nous ne le "
                "réalisons pas. Ce n'est pas une réserve commerciale, c'est une question de "
                "compétence et d'équipement : ces interventions relèvent d'entreprises spécialisées "
                "avec des opérateurs formés et des assurances adaptées.",
                "Nous le disons avant le devis, pas après l'intervention. C'est le point sur lequel "
                "la plupart des mauvaises expériences se jouent : un prestataire prend le chantier "
                "entier, fait ce qu'il peut depuis le sol, et laisse les étages supérieurs en "
                "l'état sans l'avoir annoncé. Le client découvre le problème une fois payé.",
                "Nous ne travaillons pas non plus sur échelle appuyée pour laver des vitres. C'est "
                "une pratique répandue et c'est une mauvaise idée : une échelle impose d'avoir une "
                "main occupée, ce qui est exactement ce qu'il ne faut pas en hauteur.",
            ]),
            ("Ce qui reste de notre ressort sur un bâtiment haut", [
                "Beaucoup, en réalité, et c'est souvent l'essentiel de ce qui se voit. Les "
                "rez-de-chaussée et les commerces de pied d'immeuble. Les halls et les sas "
                "d'entrée, qui sont les surfaces les plus touchées et les plus regardées. Les "
                "cloisons vitrées intérieures, les portes vitrées, les salles de réunion. Et les "
                "faces intérieures des vitrages, quand la menuiserie permet d'y accéder sans "
                "danger.",
                "Sur un immeuble de bureaux, ce périmètre représente la quasi-totalité de ce que "
                "les occupants voient de près toute la journée. La façade en étage est une question "
                "d'image extérieure, et elle se traite par campagnes, avec un prestataire "
                "spécialisé, une à deux fois par an.",
            ]),
            ("Le cas des fenêtres oscillo-battantes et des baies fixes", [
                "Une fenêtre oscillo-battante se nettoie entièrement depuis l'intérieur, les deux "
                "faces, en toute sécurité : c'est la configuration idéale en étage et nous la "
                "traitons sans difficulté.",
                "Une baie fixe en étage, en revanche, n'offre aucun accès à sa face extérieure "
                "depuis l'intérieur. Nous ne nous penchons pas, nous ne montons pas sur un garde-"
                "corps, et nous ne demanderons jamais à quelqu'un de tenir l'échelle. Si la face "
                "extérieure n'est pas accessible, elle ne sera pas faite, et c'est écrit sur le "
                "devis.",
            ]),
        ],
        "faq": [
            ("Jusqu'à quelle hauteur intervenez-vous exactement ?",
             "Les trois premiers niveaux depuis le sol, à la perche, soit une dizaine de mètres "
             "selon les hauteurs d'étage, et à condition d'avoir du recul au pied de la façade. "
             "Nous le vérifions sur photos avant de chiffrer."),
            ("Pouvez-vous me recommander quelqu'un pour les étages supérieurs ?",
             "Nous pouvons vous orienter vers des entreprises de travail en hauteur, sans "
             "commission ni accord d'apport d'affaires. Beaucoup de bâtiments fonctionnent ainsi : "
             "une campagne de façade annuelle par un spécialiste, et un entretien courant des "
             "parties basses et intérieures."),
            ("Pourquoi refuser un chantier que d'autres acceptent ?",
             "Parce qu'accepter voudrait dire soit prendre un risque pour la personne qui "
             "intervient, soit facturer un travail partiel en laissant croire qu'il est complet. "
             "Les deux nous paraissent pires qu'un devis refusé."),
        ],
    },
    {
        "slug": "cahier-des-charges-nettoyage-bureaux",
        "cat": "Entretien régulier",
        "audience": "pro",
        "service": "nettoyage-regulier-paris",
        "h1": "Nettoyage de bureaux : rédiger un cahier des charges qui tient",
        "title": "Cahier des charges de nettoyage de bureaux",
        "meta": "Fréquences par zone, périmètre, consommables, horaires, contrôle : ce qui "
                "distingue un contrat d'entretien qui tient d'un contrat qu'on résilie.",
        "lead": "La plupart des contrats d'entretien se dégradent pour la même raison : le "
                "périmètre n'était pas écrit. Voici ce qu'il faut y mettre, point par point.",
        "cle": "Une fréquence par zone, pas une fréquence pour le site.",
        "sections": [
            ("L'erreur de départ : une fréquence unique", [
                "Un contrat qui dit « passage trois fois par semaine » ne dit rien d'utile. Les "
                "sanitaires et la tisanerie demandent une reprise à chaque passage ; les surfaces "
                "vitrées intérieures tiennent au mois ; les plinthes et les bouches de ventilation, "
                "au trimestre. Une fréquence unique conduit soit à payer trop pour certaines zones, "
                "soit à ne jamais traiter les autres.",
                "Le bon cahier des charges liste les zones, et pour chacune une fréquence. C'est "
                "plus long à écrire une fois, et cela supprime la quasi-totalité des désaccords "
                "ultérieurs.",
            ]),
            ("Les points sur lesquels un contrat doit être explicite", [
                "Le périmètre des bureaux. Un poste de travail encombré ne peut pas être "
                "dépoussiéré sans déplacer des documents, ce qu'aucun prestataire sérieux ne fera. "
                "La formule honnête est « poussière des surfaces dégagées », et il faut qu'elle "
                "soit écrite, sinon elle sera reprochée.",
                "Les consommables sanitaires. Papier, savon, sacs : inclus dans la prestation ou à "
                "votre charge ? Les deux se défendent ; l'absence de réponse écrite est ce qui crée "
                "le problème, en général un vendredi soir.",
                "Les horaires et les accès. Avant 8 h 30 ou après 18 h 30, avec quel moyen "
                "d'accès, et qui détient les clés ou les codes. Un contrat qui ne tranche pas cela "
                "produit des passages manqués dès le premier mois.",
                "Ce qui n'est pas compris. Vitrerie extérieure, moquettes en profondeur, remise en "
                "état après travaux, nettoyage des textiles de sièges : ce sont des prestations "
                "distinctes, à chiffrer à part. Les laisser dans un flou bienveillant garantit "
                "qu'elles ne seront jamais faites.",
            ]),
            ("Les deux zones qui décident de tout", [
                "Les sanitaires et la tisanerie. C'est sur elles que la qualité d'un prestataire "
                "est jugée, par les salariés comme par les visiteurs, et un plateau impeccable avec "
                "des sanitaires moyens sera perçu comme mal entretenu. Elles doivent être reprises "
                "à chaque passage, sans exception, et c'est le point sur lequel il faut être le "
                "plus ferme.",
                "L'inverse est vrai aussi : des sanitaires irréprochables rachètent beaucoup. Si "
                "votre budget impose de réduire quelque chose, réduisez ailleurs.",
            ]),
            ("Prévoir le contrôle, dès le départ", [
                "Un contrat d'entretien se dégrade lentement si personne ne regarde. Prévoyez un "
                "point à trois mois puis une fois par semestre, avec un interlocuteur désigné de "
                "chaque côté, et un cahier ou un fichier partagé où les remarques sont notées au "
                "fil de l'eau plutôt qu'accumulées jusqu'à la rupture.",
                "Prévoyez aussi les remises à niveau périodiques : moquettes et textiles de sièges "
                "une à deux fois par an, vitrages intérieurs au mois, parties hautes au trimestre. "
                "Ce sont elles qui empêchent un site de dériver, et elles ne se font jamais si "
                "elles ne sont pas inscrites au calendrier.",
            ]),
        ],
        "faq": [
            ("Faut-il fournir les produits et le matériel au prestataire ?",
             "Non, un prestataire vient avec son matériel et ses produits. Seuls les consommables "
             "sanitaires se discutent : inclus ou à votre charge, les deux formules existent et la "
             "seule erreur est de ne pas trancher par écrit."),
            ("Un prestataire doit-il dépoussiérer les bureaux encombrés ?",
             "Il ne le fera pas, et c'est normal : déplacer des documents sur un poste de travail "
             "n'est ni son rôle ni votre intérêt. Faites écrire « surfaces dégagées » dans le "
             "contrat, et prévoyez une journée de rangement avant une remise à niveau complète."),
            ("À quelle fréquence nettoyer les cloisons vitrées intérieures ?",
             "Une fois par mois suffit dans la plupart des cas, avec une reprise des portes vitrées "
             "et des zones de poignée plus souvent. Ce sont les surfaces que les occupants voient de "
             "près toute la journée, et elles pèsent plus que la façade sur l'impression générale."),
        ],
    },
    {
        "slug": "nettoyage-appartement-etat-des-lieux",
        "cat": "Appartement",
        "audience": "particulier",
        "service": "nettoyage-appartement-paris",
        "h1": "Nettoyage avant état des lieux : la liste de ce qui est réellement vérifié",
        "title": "Nettoyage avant état des lieux de sortie : la liste complète",
        "meta": "Four, réfrigérateur, joints, placards, gorges de fenêtres : les points où se "
                "décident les retenues sur dépôt de garantie, et ceux qui ne se rattrapent pas.",
        "lead": "Le motif de retenue le plus fréquent sur un dépôt de garantie est l'état de "
                "propreté. Voici ce qui est regardé, dans l'ordre, et ce qui relève de l'usure "
                "plutôt que du ménage.",
        "cle": "Le logement vide est le seul moment où tout est accessible.",
        "sections": [
            ("Ce qui est regardé en premier", [
                "Trois pièces concentrent l'essentiel de l'attention : la cuisine, la salle de "
                "bains et les sols. Dans la cuisine, le four et le réfrigérateur sont les deux "
                "points les plus systématiquement vérifiés, et les deux les plus souvent laissés en "
                "l'état par le locataire sortant. Le four, en particulier, demande du temps de pose "
                "et non de la force.",
                "Dans la salle de bains, ce sont les joints, la robinetterie entartrée et la paroi "
                "de douche. L'eau francilienne est calcaire : un dépôt s'installe en quelques mois "
                "et se dissout avec un détartrant adapté et de la patience, pas avec un abrasif qui "
                "rayera la paroi.",
                "Pour les sols, l'attention porte sur les plinthes et les angles, qui sont les "
                "endroits que personne ne fait et que tout le monde regarde.",
            ]),
            ("Ce que l'on ne pense pas à faire", [
                "Les intérieurs de placards et de rangements, vidés — c'est le seul moment où ils "
                "le sont. Les gorges et les rails de fenêtres, où la poussière de ville "
                "s'accumule. Les grilles de ventilation, souvent complètement obstruées. Les "
                "interrupteurs et les poignées, qui gardent la marque des mains. Le dessus des "
                "portes et des huisseries. L'intérieur de la hotte de cuisine, s'il y en a une.",
                "Et les surfaces que les meubles masquaient : derrière et sous le réfrigérateur, "
                "derrière la machine à laver, le long des murs sous les meubles. Un logement meublé "
                "ne permet pas de les atteindre ; un logement vide, oui, et c'est précisément pour "
                "cela que le nettoyage de sortie se fait après le déménagement et pas avant.",
            ]),
            ("La distinction qui compte : propreté et usure", [
                "Un bailleur peut retenir sur le dépôt de garantie pour un défaut de propreté. "
                "L'usure normale, elle, ne peut pas lui être imputée au locataire : un parquet "
                "patiné par dix ans d'usage, une peinture ternie, un joint définitivement coloré "
                "relèvent de la vétusté et non du ménage.",
                "Cette distinction se perd dans la discussion si rien ne la documente. C'est "
                "pourquoi nous vous remettons le détail de ce qui a été fait, et pourquoi nous "
                "vous disons avant de commencer ce qui ne se rattrapera pas. Il vaut mieux le savoir "
                "avant l'état des lieux que de le découvrir pendant.",
                "Ce qui ne se rattrape pas, le plus souvent : un joint de silicone noirci en "
                "profondeur, qui se remplace et ne se nettoie pas ; une paroi de douche attaquée "
                "par des années de calcaire ; un parquet gondolé par l'eau ; un revêtement brûlé "
                "ou entaillé.",
            ]),
            ("Quand le faire, et combien de temps prévoir", [
                "Après le déménagement complet, avant l'état des lieux, avec au moins un jour de "
                "marge. Un logement nettoyé la veille au soir et visité le matin est le bon "
                "enchaînement ; le même jour est risqué, parce que les sols doivent sécher et que "
                "le four demande du temps.",
                "Comptez deux à trois heures pour un studio ou un deux-pièces, une demi-journée "
                "pour un trois ou quatre-pièces vide. Le devis est ferme : s'il faut plus de temps "
                "que prévu, c'est notre affaire. En revanche nous vous disons à l'avance si la "
                "surface demande deux intervenants.",
            ]),
        ],
        "faq": [
            ("Un nettoyage professionnel évite-t-il la retenue sur le dépôt de garantie ?",
             "Il supprime le motif le plus fréquent, qui est la propreté. Il ne couvre pas l'usure "
             "ni les dégradations, qui relèvent d'une autre discussion avec le bailleur. Le détail "
             "écrit de ce qui a été fait est utile si l'état des lieux est contesté."),
            ("Faut-il être présent pendant l'intervention ?",
             "Non, dès lors que l'accès est réglé : clé confiée, boîte à clés ou code. Beaucoup de "
             "nos interventions de sortie se font en l'absence du locataire, qui a déjà déménagé. "
             "Nous vous envoyons les photos du logement terminé si vous le souhaitez."),
            ("Nettoyez-vous aussi les vitres à cette occasion ?",
             "Oui, intérieur et extérieur quand la menuiserie le permet, encadrements et gorges "
             "comprises. C'est un point régulièrement relevé dans un état des lieux, et c'est "
             "beaucoup plus simple à faire dans un logement vide."),
        ],
    },
]


# ---------------------------------------------------------------------------
# PÉRIMÈTRES ET LIMITES — écrits une fois, repris partout
# ---------------------------------------------------------------------------
# Ces blocs sont les mêmes sur toutes les pages hottes et vitrerie. Les
# dupliquer dans chaque entrée sectorielle ferait dériver les formulations
# page après page, et c'est exactement ce que l'audit avait relevé ailleurs.
HOTTE_PERIMETRE = (
    "Hotte : intérieur, extérieur, plénum et parties démontables",
    "Filtres : dégraissage par trempage, ou remplacement si nécessaire",
    "Conduits d'extraction : dégraissage par les trappes de visite",
    "Ramonage mécanique du conduit quand il y a de la suie (four à bois, charbon)",
    "Caisson et pales du moteur d'extraction, quand ils sont accessibles",
    "Protection de la cuisine avant ouverture, nettoyage de la zone après",
    "Remontage complet et essai d'extraction avant de partir",
    "Relevé daté et détaillé de l'intervention, zone par zone",
)

HOTTE_LIMITES = (
    "Nous délivrons une attestation de nettoyage et d'entretien de hotte, datée et détaillée : "
    "ce qui a été traité, sur quelle longueur de conduit, quelles trappes ont été ouvertes, "
    "l'état constaté avant et le résultat de l'essai d'extraction. Elle se range dans le livret "
    "d'entretien annexé à votre registre de sécurité, et c'est elle que votre assureur demande "
    "après un sinistre.",
    "Cette attestation dit ce que nous avons fait. Elle ne vaut ni attestation de conformité de "
    "votre installation, ni vérification annuelle au titre de l'article GC 22 : celle-ci relève "
    "d'un technicien compétent ou d'un organisme agréé, et c'est une prestation distincte de la "
    "nôtre. Méfiez-vous d'un prestataire de nettoyage qui vous promet les deux dans le même "
    "document.",
    "Nous n'intervenons pas sur le réseau : pose de trappe de visite, modification de tracé, "
    "remplacement de moteur relèvent d'un installateur. Nous constatons et nous vous orientons, "
    "sans rien vendre là-dessus.",
    "Sans trappe de visite accessible, un conduit ne peut pas être traité sur toute sa longueur. "
    "Nous le disons avant le devis plutôt que de facturer un dégraissage partiel présenté comme "
    "complet.",
)

HOTTE_REGLEMENT = (
    "Le texte applicable est l'arrêté du 25 juin 1980 portant règlement de sécurité contre "
    "l'incendie dans les établissements recevant du public. Sa section 7, « Entretien et "
    "vérifications », tient en deux articles.<br><br>"
    "<strong>Article GC 21 — l'entretien.</strong> Les filtres sont nettoyés ou remplacés au "
    "moins une fois par semaine. Les conduits d'évacuation sont ramonés au moins une fois par "
    "an, et leur vacuité vérifiée à cette occasion. Le circuit d'extraction est nettoyé aussi "
    "souvent que nécessaire. Les dates sont notées par l'exploitant dans un livret d'entretien "
    "annexé au registre de sécurité.<br><br>"
    "<strong>Article GC 22 — la vérification.</strong> Dans les établissements des quatre "
    "premières catégories, les installations de cuisson font l'objet d'une vérification "
    "annuelle par un technicien compétent ou un organisme agréé. Elle porte notamment sur "
    "l'état d'entretien des appareils et sur la ventilation des locaux : évacuation de l'air "
    "vicié, des buées et des graisses, et fonctionnement du dispositif d'extraction. Elle est "
    "consignée au registre de sécurité. Les établissements de 5<sup>e</sup> catégorie relèvent "
    "d'un autre régime, celui de l'arrêté du 22 juin 1990."
)

VITRES_PERIMETRE = (
    "Vitrage : les deux faces, quand la menuiserie permet d'accéder à l'extérieur",
    "Encadrements, montants et appuis repris dans le même passage",
    "Rails et gorges de coulissants, où se loge l'essentiel de la saleté",
    "Eau déminéralisée : séchage sans trace, sans essuyage donc sans marque de chiffon",
    "Dégraissage préalable des faces intérieures grasses (commerce de bouche)",
    "Perche télescopique jusqu'aux trois premiers niveaux depuis le sol",
    "Enseignes, bandeaux et vitrophanies, à la mouillette et sans racloir",
)

VITRES_LIMITES = (
    "Au-delà de trois niveaux depuis le sol, ou sans recul suffisant au pied de la façade, "
    "l'intervention demande une nacelle, un échafaudage ou un cordiste. Nous ne le faisons pas : "
    "ce sont d'autres compétences, d'autres équipements et d'autres assurances. Nous le disons "
    "avant le devis, jamais après l'intervention.",
    "Nous ne lavons pas de vitres depuis une échelle appuyée. C'est répandu et c'est une mauvaise "
    "idée : une main est occupée, ce qui est précisément ce qu'il ne faut pas en hauteur.",
    "Une baie fixe en étage dont la face extérieure n'est pas accessible depuis l'intérieur ne "
    "sera pas faite de ce côté, et c'est écrit sur le devis.",
)


# Suite de VILLES_PRO : les 22 communes qui étaient documentées ailleurs sur
# le site (VILLES, PREMIUM_VILLES) mais n'avaient pas encore d'angle hottes ni
# vitrerie. Les arrondissements parisiens sont les plus denses en restauration
# et ne pouvaient pas rester absents d'un catalogue qui met les hottes en avant.
VILLES_PRO += [
    {
        "slug": "paris-8", "nom": "Paris 8e", "cp": "75008", "dept": "75",
        "lat": 48.8721, "lon": 2.3120,
        "tissu":
            "Le 8e arrondissement réunit la restauration d'affaires des Champs-Élysées et du "
            "quartier de la Madeleine, les palaces et leurs cuisines, et un commerce de luxe qui "
            "tient sa vitrine comme une devanture de bijouterie. C'est l'arrondissement où "
            "l'exigence de discrétion est la plus forte.",
        "acces":
            "Stationnement quasi impossible, livraisons réglementées et horaires d'accès encadrés "
            "par la Ville comme par les établissements eux-mêmes. Nous intervenons sur créneau "
            "convenu à l'avance, en véhicule léger, avec notre eau et notre électricité.",
        "hotte":
            "Les cuisines du 8e sont souvent dimensionnées pour un service soutenu dans des "
            "immeubles haussmanniens qui n'avaient pas été conçus pour cela : conduits longs, "
            "tracés contraints par la structure, et des exigences de copropriété qui ferment la "
            "plupart des créneaux de journée. Le travail technique est classique ; c'est "
            "l'organisation qui demande du soin, et une intervention de nuit annoncée plusieurs "
            "semaines à l'avance.",
        "vitres":
            "La vitrine de luxe est le cas le plus exigeant qui existe : grandes surfaces sans "
            "menuiserie intermédiaire, éclairage rasant qui révèle le moindre défaut de séchage, "
            "et des laitons ou inox de devanture qui gardent la trace d'eau calcaire. L'eau "
            "déminéralisée et la reprise des encadrements ne sont pas des options ici.",
        "faq_hotte": ("Pouvez-vous intervenir de nuit dans un immeuble haussmannien ?",
                      "Oui, dans la plage autorisée par la copropriété, en protégeant les parties "
                      "communes traversées. La contrainte n'est pas technique, elle est "
                      "d'organisation : il faut la connaître avant, et c'est pour cela que nous "
                      "demandons le règlement de copropriété au premier rendez-vous."),
        "faq_vitres": ("Comment éviter les traces sur une grande devanture éclairée ?",
                       "En rinçant à l'eau déminéralisée et en ne l'essuyant pas. La trace vient "
                       "du calcaire de l'eau du réseau et de l'essuyage ; une eau privée de ses "
                       "minéraux sèche sans rien laisser, ce qui supprime les deux causes à la "
                       "fois. C'est exactement la configuration où cela se voit le plus."),
    },
    {
        "slug": "paris-11", "nom": "Paris 11e", "cp": "75011", "dept": "75",
        "lat": 48.8580, "lon": 2.3792,
        "tissu":
            "Le 11e est l'arrondissement qui compte le plus de restaurants et de bars de Paris : "
            "rue de Charonne, rue Oberkampf, Bastille, Sainte-Marthe. Des petites salles, des "
            "cuisines ouvertes, une rotation d'enseignes rapide, et presque toujours des logements "
            "au-dessus.",
        "acces":
            "Rues étroites, stationnement très contraint, livraisons tolérées le matin. Notre "
            "véhicule est léger et autonome en eau et en électricité : nous n'avons besoin ni "
            "d'une place devant la porte ni d'un point d'eau en cuisine.",
        "hotte":
            "C'est l'arrondissement où nous trouvons le plus de conduits jamais repris. La "
            "rotation des enseignes y est telle qu'un local change deux ou trois fois d'exploitant "
            "sans que le circuit d'extraction ne soit jamais ouvert : chacun hérite du dépôt du "
            "précédent et personne ne s'en sait responsable. Les logements au-dessus rendent par "
            "ailleurs les plaintes d'odeurs fréquentes, et elles signalent presque toujours un "
            "conduit chargé plutôt qu'un défaut de conception.",
        "vitres":
            "Devantures de bar et de restaurant, très sollicitées : traces de mains sur les portes "
            "vitrées, projections au bas du vitrage côté terrasse, et condensation intérieure aux "
            "heures de service. La zone basse et les poignées se reprennent chaque semaine, le "
            "vitrage complet toutes les deux semaines.",
        "faq_hotte": ("Je reprends un local, le conduit a-t-il été nettoyé ?",
                      "C'est la question à poser avant la reprise, et dans le 11e c'est presque "
                      "toujours non. Nous ouvrons les trappes et nous vous montrons l'état réel "
                      "avant de chiffrer : un conduit hérité est un coût à connaître avant la "
                      "signature, pas après."),
        "faq_vitres": ("Pouvez-vous passer avant l'ouverture dans une rue piétonne ?",
                       "Oui, entre 7 h et 9 h, dans la plage de livraison. C'est aussi le moment "
                       "où le verre est encore froid, ce qui donne un séchage régulier, et où "
                       "personne ne traverse le chantier."),
    },
    {
        "slug": "paris-12", "nom": "Paris 12e", "cp": "75012", "dept": "75",
        "lat": 48.8409, "lon": 2.3876,
        "tissu":
            "Le 12e mêle le marché d'Aligre et son commerce de bouche traditionnel, la "
            "restauration du quartier de Bercy, et les grandes brasseries des abords de la gare de "
            "Lyon, qui travaillent en service continu de très gros volumes.",
        "acces":
            "Les abords de la gare sont difficiles aux heures de pointe, le reste de "
            "l'arrondissement est praticable. Nous intervenons tôt le matin ou de nuit selon "
            "l'établissement.",
        "hotte":
            "Les brasseries de gare sont le profil le plus chargé que nous rencontrions dans "
            "Paris : service continu de 7 h à minuit, friture et grillade en permanence, et un "
            "conduit qui n'a pas de période creuse pour refroidir. Deux passages par an y sont un "
            "minimum, trois sont souvent plus réalistes. Autour d'Aligre, le profil est inverse : "
            "petits commerces de bouche, conduits courts mais anciens.",
        "vitres":
            "Grandes devantures de brasserie, hautes et exposées au trafic de l'avenue Daumesnil "
            "et du boulevard Diderot : le dépôt y est gras, fait de particules de freinage, et il "
            "demande un dégraissage avant lavage. Les commerces d'Aligre relèvent du travail de "
            "vitrine classique, hebdomadaire.",
        "faq_hotte": ("Une brasserie en service continu, à quel rythme ?",
                      "Deux passages par an au minimum sur la hotte et le conduit, trois à très "
                      "fort volume, et des filtres nettoyés ou remplacés au moins une fois par "
                      "semaine par votre équipe. Le service continu ne laisse aucune période de "
                      "refroidissement au conduit, et c'est ce qui accélère le dépôt."),
        "faq_vitres": ("Pourquoi ma devanture se salit-elle si vite sur le boulevard ?",
                       "Parce que ce qui s'y dépose n'est pas de la poussière mais un film gras : "
                       "particules de freinage et résidus d'hydrocarbures. L'eau claire l'étale au "
                       "lieu de l'enlever. Il faut un dégraissage, puis un rinçage à l'eau "
                       "déminéralisée."),
    },
    {
        "slug": "paris-15", "nom": "Paris 15e", "cp": "75015", "dept": "75",
        "lat": 48.8412, "lon": 2.3003,
        "tissu":
            "Le 15e est le plus peuplé des arrondissements parisiens, et sa restauration est celle "
            "d'un grand quartier résidentiel : commerces de bouche de proximité rue du Commerce et "
            "rue de la Convention, restaurants de quartier, et une restauration d'entreprise autour "
            "du front de Seine et de Balard.",
        "acces":
            "Stationnement contraint mais praticable tôt le matin, et les immeubles récents du "
            "front de Seine disposent de parkings accessibles. L'arrondissement est étendu : nous "
            "regroupons les interventions par secteur.",
        "hotte":
            "Deux profils bien distincts. Les boulangeries et les commerces de bouche de proximité, "
            "où la farine mêlée au gras forme une croûte dure qui ne part pas au dégraissant "
            "ménager, et qui demandent un créneau d'après-midi entre la fin de cuisson et la "
            "reprise du tour de nuit. Et les restaurants d'entreprise de Balard, plus volumineux, "
            "qui se traitent pendant les fermetures.",
        "vitres":
            "Vitrines de rue commerçante à rythme hebdomadaire, et de grandes façades vitrées "
            "d'immeubles tertiaires sur le front de Seine, dont seuls les premiers niveaux sont "
            "accessibles depuis le sol. Nous le disons avant le devis plutôt que de laisser un "
            "étage non fait.",
        "faq_hotte": ("À quelle heure intervenir dans une boulangerie du 15e ?",
                      "L'après-midi, entre la fin de la cuisson et la reprise du tour de nuit, ou "
                      "le jour de fermeture. C'est la seule fenêtre réelle, et elle est étroite : "
                      "nous la réservons à l'avance plutôt que de l'improviser."),
        "faq_vitres": ("Traitez-vous les tours du front de Seine ?",
                       "Pas en façade au-delà de trois niveaux : cela demande une nacelle ou un "
                       "cordiste, ce qui n'est pas notre métier. Nous traitons les commerces de "
                       "pied d'immeuble, les halls, les sas et toutes les surfaces intérieures."),
    },
    {
        "slug": "paris-16", "nom": "Paris 16e", "cp": "75016", "dept": "75",
        "lat": 48.8637, "lon": 2.2769,
        "tissu":
            "Le 16e est résidentiel et bourgeois : un commerce de bouche de qualité rue de Passy "
            "et rue de l'Annonciation, des restaurants de quartier plutôt que de flux, et une "
            "forte densité de cabinets libéraux et d'agences immobilières sur un marché de "
            "standing.",
        "acces":
            "Stationnement payant partout et parkings souterrains à hauteur limitée. Notre "
            "véhicule passe sous les 1,90 m de la plupart des sous-sols, et nous apportons eau et "
            "électricité.",
        "hotte":
            "Les cuisines du 16e sont installées dans des immeubles d'habitation de standing, où "
            "la contrainte dominante est la copropriété : horaires encadrés, parties communes à "
            "protéger, et des plaintes d'odeurs suivies de près par le syndic. Un dégraissage "
            "complet du circuit règle le plus souvent ce que des mois de courriers n'avaient pas "
            "réglé — et c'est l'hypothèse la moins coûteuse à tester avant d'envisager des travaux.",
        "vitres":
            "Beaucoup de fenêtres anciennes à petits bois et de hauteurs sous plafond de trois "
            "mètres, en cabinet comme en commerce. Ce sont les vitrages les plus longs à faire "
            "correctement : chaque carreau demande son passage, et nous comptons au vantail et non "
            "au mètre carré.",
        "faq_hotte": ("Le syndic me reproche des odeurs, que faire en premier ?",
                      "Faites dégraisser le circuit complet, conduits compris, et mesurez à "
                      "nouveau. Un conduit chargé perd de la section, l'extraction tire moins, et "
                      "les buées trouvent un autre chemin. C'est l'hypothèse la plus fréquente et "
                      "la moins chère ; des travaux sur le réseau ne se décident qu'après."),
        "faq_vitres": ("Comment comptez-vous une fenêtre à petits bois ?",
                       "Au vantail. Une fenêtre à six carreaux demande plusieurs fois le temps "
                       "d'une baie de même surface, et un prix au mètre carré serait trompeur dans "
                       "un sens comme dans l'autre. Nous comptons sur photos, devis ferme."),
    },
    {
        "slug": "paris-17", "nom": "Paris 17e", "cp": "75017", "dept": "75",
        "lat": 48.8872, "lon": 2.3220,
        "tissu":
            "Le 17e a deux visages : les Batignolles, devenus en dix ans l'un des quartiers de "
            "restauration les plus actifs de Paris, et la plaine Monceau, résidentielle et "
            "tertiaire. S'y ajoute le quartier d'affaires de Clichy-Batignolles, livré récemment.",
        "acces":
            "Les Batignolles sont difficiles d'accès aux heures de service ; les immeubles récents "
            "de Clichy-Batignolles disposent de parkings et de quais. Nous intervenons tôt le matin "
            "ou de nuit.",
        "hotte":
            "Les Batignolles concentrent beaucoup de petites cuisines ouvertes, installées dans des "
            "immeubles d'habitation, avec des conduits courts mais très sollicités. La cuisine "
            "ouverte ajoute une contrainte : la hotte est visible depuis la salle, donc son aspect "
            "compte, et les buées non captées se déposent sur le plafond et les luminaires. Un "
            "plafond jauni au-dessus du piano est un indice fiable d'extraction insuffisante.",
        "vitres":
            "Devantures de restaurant à reprendre chaque semaine aux Batignolles, et façades de "
            "bureaux récentes à Clichy-Batignolles, lisibles de loin et donc impitoyables au défaut "
            "de séchage. Les rez-de-chaussée et les halls sont de notre ressort, les étages non.",
        "faq_hotte": ("Ma cuisine est ouverte sur la salle, l'intervention salit-elle le "
                      "restaurant ?",
                      "Non : tout est bâché avant la première ouverture de trappe, et la zone est "
                      "nettoyée après. Le point de vigilance en cuisine ouverte est le plafond de "
                      "salle — s'il est jauni, l'extraction ne capte pas assez et le dégraissage "
                      "seul n'y suffira pas."),
        "faq_vitres": ("Intervenez-vous le week-end aux Batignolles ?",
                       "Oui, et c'est souvent le meilleur créneau pour un restaurant qui ne "
                       "déjeune pas le dimanche. Les horaires décalés ne sont pas facturés en "
                       "supplément."),
    },
    {
        "slug": "puteaux", "nom": "Puteaux", "cp": "92800", "dept": "92",
        "lat": 48.8846, "lon": 2.2386,
        "tissu":
            "Puteaux porte une grande partie de La Défense sur son territoire : une restauration de "
            "flux dimensionnée pour des milliers de salariés sur deux heures de déjeuner, et, en "
            "contrebas, un centre-ville ancien avec son commerce de proximité.",
        "acces":
            "Les dalles et parkings du quartier d'affaires imposent des accès réglementés, à "
            "organiser avec le gestionnaire du site. Le centre ancien est d'accès ordinaire.",
        "hotte":
            "La restauration de flux produit l'encrassement le plus massif et le plus concentré "
            "que nous rencontrions : friteuses et grillades à plein régime sur deux heures, cinq "
            "jours sur sept. C'est le profil qui demande le rythme le plus soutenu — deux passages "
            "par an au minimum, trois à très fort volume — et un suivi hebdomadaire des filtres par "
            "l'équipe, que la réglementation prévoit explicitement.",
        "vitres":
            "Verre partout et une limite nette : seuls les trois premiers niveaux sont accessibles "
            "à la perche depuis le sol. Nous nous concentrons sur les commerces de pied d'immeuble, "
            "les halls, les sas et l'intérieur, et nous l'annonçons avant le devis.",
        "faq_hotte": ("Combien de passages pour une cuisine qui ne sert qu'au déjeuner ?",
                      "Deux par an au minimum, et c'est contre-intuitif : ce qui charge un conduit "
                      "est la quantité de matière grasse vaporisée, pas le nombre d'heures "
                      "d'ouverture. Deux heures de friture intensive par jour chargent autant qu'un "
                      "service continu plus doux."),
        "faq_vitres": ("Intervenez-vous sur les tours de La Défense ?",
                       "Pas en façade au-delà de trois niveaux : il faut une nacelle ou un "
                       "cordiste, et ce n'est pas notre métier. Nous traitons les commerces de pied "
                       "d'immeuble, les halls et toutes les surfaces intérieures."),
    },
    {
        "slug": "rueil-malmaison", "nom": "Rueil-Malmaison", "cp": "92500", "dept": "92",
        "lat": 48.8768, "lon": 2.1801,
        "tissu":
            "Rueil-Malmaison réunit un centre-ville commerçant actif, plusieurs sièges sociaux "
            "installés dans des parcs d'activité, et un habitat résidentiel étendu. La restauration "
            "y est à la fois de quartier et d'entreprise.",
        "acces":
            "Stationnement praticable, parcs d'activité bien desservis. Rueil est à une trentaine "
            "de kilomètres de notre atelier : nous regroupons les interventions de l'ouest "
            "francilien sur une même tournée.",
        "hotte":
            "Les restaurants d'entreprise des parcs d'activité se planifient à l'année et "
            "s'entretiennent bien ; les restaurants du centre, installés dans du bâti plus ancien, "
            "demandent un constat avant de pouvoir être chiffrés sérieusement. Dans les deux cas, "
            "le ramonage annuel des conduits est le plancher réglementaire, et le rythme utile "
            "dépend du mode de cuisson dominant.",
        "vitres":
            "Vitrines de centre-ville à rythme hebdomadaire ou bimensuel, et façades de bureaux de "
            "parcs d'activité, grandes, régulières et accessibles depuis le sol : c'est la "
            "configuration la plus économique à entretenir, un passage trimestriel suffit "
            "généralement.",
        "faq_hotte": ("Peut-on signer un contrat annuel plutôt qu'appeler chaque fois ?",
                      "Oui, et c'est la formule la plus simple pour un restaurant d'entreprise : "
                      "un ou deux passages à date fixe, le relevé de chaque intervention qui vient "
                      "compléter votre livret d'entretien, et plus rien à suivre dans l'année."),
        "faq_vitres": ("Quel est le délai d'intervention à Rueil ?",
                       "Habituellement 48 à 72 h. Nous regroupons les interventions de l'ouest sur "
                       "une même tournée, ce qui limite les frais de déplacement ; ils sont "
                       "annoncés avant que vous validiez."),
    },
    {
        "slug": "saint-cloud", "nom": "Saint-Cloud", "cp": "92210", "dept": "92",
        "lat": 48.8456, "lon": 2.2189,
        "tissu":
            "Saint-Cloud est une commune résidentielle de standing, avec un commerce de bouche de "
            "qualité en centre-ville, quelques restaurants de quartier, et un tissu de bureaux "
            "limité mais présent.",
        "acces":
            "Rues en pente et stationnement contraint en centre, praticable ailleurs. Saint-Cloud "
            "est à une trentaine de kilomètres de notre atelier.",
        "hotte":
            "Peu de restauration de flux, beaucoup de petites cuisines dans des immeubles "
            "d'habitation. La contrainte est donc celle de la copropriété — horaires encadrés, "
            "parties communes à protéger — plutôt que celle du volume. Un passage annuel suffit "
            "souvent, deux si la cuisson dominante est la friture ou la grillade.",
        "vitres":
            "Vitrines de commerce de bouche et vitrages de cabinets. Les buées de cuisson déposent "
            "sur la face intérieure du verre un film gras qui éteint la couleur des produits "
            "exposés : c'est là que se joue l'aspect d'une vitrine de boulangerie, bien plus que "
            "sur la face extérieure.",
        "faq_hotte": ("Un seul passage par an suffit-il ?",
                      "C'est le plancher réglementaire pour le ramonage des conduits, et cela "
                      "suffit souvent sur une cuisson douce. En friture ou en grillade, deux "
                      "passages sont le bon rythme. Le premier passage permet de calibrer le "
                      "suivant, trappes ouvertes."),
        "faq_vitres": ("Pourquoi ma vitrine reste-t-elle voilée après nettoyage ?",
                       "Parce que le film gras déposé à l'intérieur du verre par les buées de "
                       "cuisson n'a pas été dégraissé avant d'être lavé. Un produit à vitres "
                       "l'étale sans le dissoudre : propre de près, voilé de loin."),
    },
    {
        "slug": "saint-germain-en-laye", "nom": "Saint-Germain-en-Laye", "cp": "78100",
        "dept": "78", "lat": 48.8987, "lon": 2.0940,
        "tissu":
            "Saint-Germain-en-Laye a un centre historique commerçant dense, piétonnier sur une "
            "bonne partie, avec un commerce de bouche de qualité et une restauration de terrasse "
            "active autour du château et du marché.",
        "acces":
            "Centre en grande partie piéton, avec des plages de livraison limitées au matin. Nous "
            "arrivons avant 7 h 30, qui est de toute façon le bon créneau pour un commerce de "
            "bouche.",
        "hotte":
            "Les cuisines du centre historique sont installées dans du bâti ancien, souvent "
            "protégé, avec des conduits contraints par la structure et parfois mitoyens. La "
            "question de savoir qui entretient quoi s'y pose plus souvent qu'ailleurs, et elle doit "
            "être tranchée avant l'intervention plutôt qu'après.",
        "vitres":
            "Vitrines de commerce de bouche et de boutiques, à reprendre chaque semaine en saison. "
            "Le centre piéton limite le film gras du trafic, mais les terrasses ajoutent des "
            "projections au bas des vitrages, qui se reprennent à chaque passage.",
        "faq_hotte": ("Mon conduit est mitoyen avec le commerce voisin, que faire ?",
                      "Il faut d'abord établir qui est responsable de quoi, ce qui se lit dans les "
                      "baux et le règlement de copropriété. En pratique, le plus efficace est une "
                      "intervention unique sur le circuit complet, refacturée au prorata : un "
                      "conduit partagé nettoyé par moitié ne sert à rien."),
        "faq_vitres": ("Intervenez-vous dans le centre piéton ?",
                       "Oui, avant 7 h 30, dans la plage de livraison autorisée. C'est aussi le "
                       "moment où le verre est encore froid, ce qui donne un séchage régulier."),
    },
    {
        "slug": "sceaux", "nom": "Sceaux", "cp": "92330", "dept": "92",
        "lat": 48.7789, "lon": 2.2900,
        "tissu":
            "Sceaux est une petite commune résidentielle au commerce de centre-ville soigné, avec "
            "un marché actif, des commerces de bouche de qualité et une restauration de quartier "
            "plutôt que de flux.",
        "acces":
            "Centre compact, stationnement praticable tôt le matin. Sceaux est à une trentaine de "
            "kilomètres de notre atelier : nous y intervenons dans le cadre d'une tournée du sud "
            "francilien.",
        "hotte":
            "Des cuisines de petite taille, dans des immeubles d'habitation, avec des conduits "
            "courts. Le volume est modeste mais les locaux sont anciens, et le circuit "
            "d'extraction est rarement documenté : dans la plupart des cas, personne ne sait quand "
            "il a été nettoyé pour la dernière fois. Nous commençons par ouvrir et constater.",
        "vitres":
            "Vitrines de commerce de proximité, bimensuelles, et vitrages de cabinets libéraux. Le "
            "trafic est modéré, donc le film gras extérieur l'est aussi : l'essentiel du travail se "
            "joue sur les faces intérieures et les encadrements.",
        "faq_hotte": ("Je ne sais pas quand mon conduit a été nettoyé la dernière fois.",
                      "C'est le cas le plus fréquent et ce n'est pas un problème : nous ouvrons "
                      "les trappes de visite et nous vous montrons l'état réel. Le devis se fait "
                      "sur ce constat, pas sur une estimation à l'aveugle."),
        "faq_vitres": ("Un passage par mois suffit-il pour ma vitrine ?",
                       "Dans une rue au trafic modéré comme le centre de Sceaux, oui, avec une "
                       "reprise des poignées et de la zone basse entre deux passages. En rue "
                       "passante, il faudrait un passage hebdomadaire."),
    },
]

# Fin de VILLES_PRO : la grande couronne et les communes de l'est, où le
# facteur dominant n'est plus l'accès mais la distance — donc le délai, et
# le regroupement des interventions sur une même tournée.
VILLES_PRO += [
    {
        "slug": "versailles", "nom": "Versailles", "cp": "78000", "dept": "78",
        "lat": 48.8014, "lon": 2.1301,
        "tissu":
            "Versailles a une restauration touristique concentrée autour du château et du quartier "
            "Notre-Dame, un marché couvert très actif, et un commerce de bouche de qualité. "
            "L'activité y est fortement saisonnière, ce qui change le calendrier d'entretien.",
        "acces":
            "Centre contraint, livraisons encadrées, forte affluence touristique en journée. Nous "
            "intervenons tôt le matin. Versailles est à une quarantaine de kilomètres de notre "
            "atelier : les interventions s'y planifient, elles ne s'improvisent pas.",
        "hotte":
            "La saisonnalité est le point à exploiter : une cuisine qui double son volume d'avril "
            "à septembre doit être dégraissée à la sortie de la haute saison, pas au hasard du "
            "calendrier. Beaucoup de cuisines sont par ailleurs installées dans du bâti ancien "
            "protégé, avec des conduits contraints par la structure et peu de trappes de visite.",
        "vitres":
            "Vitrines de commerce de bouche et de boutiques touristiques, à reprendre chaque "
            "semaine en saison, toutes les deux semaines hors saison. Les terrasses ajoutent des "
            "projections au bas des vitrages.",
        "faq_hotte": ("Quand faire dégraisser une cuisine saisonnière ?",
                      "À la sortie de la haute saison, pas au milieu. Le dépôt accumulé pendant "
                      "les mois pleins est celui qu'il faut retirer, et l'intervention se place "
                      "alors dans une période creuse où la cuisine peut être immobilisée sans "
                      "coût. C'est le meilleur arbitrage, et il est rarement fait."),
        "faq_vitres": ("Quel est le délai d'intervention à Versailles ?",
                       "Habituellement 48 à 72 h : nous sommes à une quarantaine de kilomètres et "
                       "nous regroupons les interventions de l'ouest sur une même tournée. Les "
                       "frais de déplacement sont annoncés avant que vous validiez."),
    },
    {
        "slug": "le-vesinet", "nom": "Le Vésinet", "cp": "78110", "dept": "78",
        "lat": 48.8925, "lon": 2.1330,
        "tissu":
            "Le Vésinet est une commune résidentielle de villas et de parcs, au commerce "
            "concentré autour du centre et de la gare : commerces de bouche, quelques restaurants "
            "de quartier, des cabinets libéraux.",
        "acces":
            "Stationnement aisé, voirie dégagée. Le Vésinet est à une quarantaine de kilomètres de "
            "notre atelier, dans la même tournée ouest que Saint-Germain-en-Laye et "
            "Rueil-Malmaison.",
        "hotte":
            "Peu d'établissements, mais presque tous en immeuble ou en rez-de-chaussée "
            "d'habitation : la contrainte est celle du voisinage et des horaires plutôt que celle "
            "du volume. Un passage annuel suffit dans la plupart des cas, deux en cuisson grasse. "
            "Le ramonage annuel des conduits reste le plancher réglementaire.",
        "vitres":
            "Vitrines de centre et vitrages de cabinets. Le trafic est faible, donc le film gras "
            "extérieur aussi : l'essentiel du travail se joue sur les encadrements, les appuis et "
            "les faces intérieures, qui sont ce qui salit à nouveau le verre.",
        "faq_hotte": ("Mon restaurant est en bas d'un immeuble, quelles précautions ?",
                      "Protection des parties communes traversées, intervention dans la plage "
                      "autorisée par la copropriété, et une attention particulière au circuit "
                      "d'extraction : c'est lui qui, encrassé, provoque les remontées d'odeurs "
                      "vers les logements et les plaintes qui suivent."),
        "faq_vitres": ("Les encadrements sont-ils compris dans le passage ?",
                       "Oui, toujours, ainsi que les appuis. C'est important : un appui chargé de "
                       "poussière fait couler une coulure sur la vitre à la première pluie, et le "
                       "nettoyage du verre seul ne tient alors que quelques jours."),
    },
    {
        "slug": "saint-maur-des-fosses", "nom": "Saint-Maur-des-Fossés", "cp": "94100",
        "dept": "94", "lat": 48.7994, "lon": 2.4934,
        "tissu":
            "Saint-Maur-des-Fossés est une grande commune résidentielle en boucle de Marne, avec "
            "plusieurs centres commerçants distincts — Le Parc, La Varenne, Champignol — et une "
            "restauration de quartier répartie entre eux plutôt que concentrée.",
        "acces":
            "Stationnement praticable, mais la commune est étendue et ses centres sont éloignés "
            "les uns des autres : nous groupons les interventions par quartier pour limiter les "
            "trajets.",
        "hotte":
            "Des restaurants de quartier, en petites salles, souvent en rez-de-chaussée "
            "d'immeuble, avec des conduits courts mais anciens. Les bords de Marne ajoutent des "
            "guinguettes et des établissements saisonniers, dont le rythme d'entretien doit suivre "
            "la saison plutôt que le calendrier.",
        "vitres":
            "Vitrines de commerce de proximité, bimensuelles, réparties sur plusieurs centres. "
            "C'est le cas où un contrat régulier couvrant plusieurs établissements d'un même "
            "quartier fait réellement baisser le coût au passage.",
        "faq_hotte": ("Faut-il dégraisser une cuisine saisonnière à la même fréquence ?",
                      "Non : il faut la caler sur la saison. Une guinguette ou une terrasse qui "
                      "travaille d'avril à septembre se dégraisse à la fermeture de saison, quand "
                      "le dépôt est à son maximum et que la cuisine peut être immobilisée sans "
                      "coût."),
        "faq_vitres": ("Nous avons plusieurs commerces dans la commune, est-ce plus avantageux ?",
                       "Oui, nettement : un passage unique couvrant plusieurs établissements d'un "
                       "même secteur répartit le déplacement, qui est la part fixe du coût. Nous "
                       "établissons alors un prix au passage et non à l'établissement."),
    },
    {
        "slug": "tremblay-en-france", "nom": "Tremblay-en-France", "cp": "93290",
        "dept": "93", "lat": 48.9486, "lon": 2.5697,
        "tissu":
            "Tremblay-en-France vit en grande partie de la proximité de Roissy : zones d'activité "
            "et de logistique, hôtellerie, et une restauration tournée vers les équipes "
            "aéroportuaires, qui travaillent en horaires décalés et en continu.",
        "acces":
            "Voirie dégagée, stationnement aisé, accès direct par l'A104 et la N2. Tremblay est à "
            "une quinzaine de minutes de notre atelier : c'est l'une des communes où nous pouvons "
            "nous engager sur un créneau serré.",
        "hotte":
            "La restauration d'hôtel et de zone aéroportuaire fonctionne sans période creuse : "
            "petits-déjeuners tôt, service continu, équipes de nuit. Il n'y a pas de fenêtre "
            "évidente, et c'est justement là que notre proximité compte — nous nous calons sur le "
            "créneau que vous pouvez libérer, même court, même à 3 h du matin, sans que le trajet "
            "n'oblige à élargir la plage.",
        "vitres":
            "Façades vitrées de locaux d'activité et d'hôtels : grandes, régulières, accessibles "
            "depuis le sol. C'est la configuration la plus économique à entretenir. Pour les "
            "hôtels, le sas d'entrée demande deux passages par semaine là où le reste tient au "
            "mois.",
        "faq_hotte": ("Pouvez-vous intervenir de nuit à Tremblay ?",
                      "Oui, et sans difficulté : nous sommes à quinze minutes. Une cuisine qui "
                      "n'a qu'une fenêtre de trois heures entre deux services est précisément le "
                      "cas où la proximité de l'atelier change ce que nous pouvons proposer."),
        "faq_vitres": ("Quel est le délai d'intervention à Tremblay ?",
                       "Habituellement 24 à 48 h, et souvent le jour même en cas d'urgence. Les "
                       "frais de déplacement y sont faibles : nous sommes à une quinzaine de "
                       "kilomètres."),
    },
    {
        "slug": "chelles", "nom": "Chelles", "cp": "77500", "dept": "77",
        "lat": 48.8797, "lon": 2.5928,
        "tissu":
            "Chelles est la plus grande commune de Seine-et-Marne par la population : un "
            "centre-ville commerçant actif autour de la gare et du marché, des zones d'activité, "
            "et un habitat largement pavillonnaire.",
        "acces":
            "Stationnement praticable, accès par l'A104 ou la N34. Chelles est à une vingtaine de "
            "kilomètres de notre atelier : nous y intervenons dans un délai de 48 à 72 h, en "
            "groupant les interventions de l'est francilien.",
        "hotte":
            "Un tissu de restauration de proximité et de commerces de bouche, en locaux souvent "
            "anciens, avec des conduits rarement documentés. La boulangerie y est particulièrement "
            "présente, et c'est le cas le plus technique : la farine mêlée au gras forme une croûte "
            "dure qui ne réagit pas comme une graisse de friture et demande un alcalin à temps de "
            "pose.",
        "vitres":
            "Vitrines de centre-ville, hebdomadaires ou bimensuelles selon la rue, et façades "
            "vitrées de locaux d'activité, accessibles depuis le sol et traitées au trimestre.",
        "faq_hotte": ("La farine change-t-elle quelque chose au nettoyage ?",
                      "Oui, et c'est ce que les prestataires généralistes sous-estiment. Mêlée au "
                      "gras, elle forme une croûte qui ne part pas au dégraissant ménager : il "
                      "faut un alcalin avec un vrai temps de pose, puis une action mécanique."),
        "faq_vitres": ("Quel est le délai d'intervention à Chelles ?",
                       "Habituellement 48 à 72 h. Nous groupons les interventions de l'est "
                       "francilien sur une même tournée, ce qui limite les frais de déplacement ; "
                       "ils sont annoncés avant que vous validiez."),
    },
    {
        "slug": "meaux", "nom": "Meaux", "cp": "77100", "dept": "77",
        "lat": 48.9601, "lon": 2.8785,
        "tissu":
            "Meaux a un centre historique commerçant autour de la cathédrale et du marché, une "
            "tradition de commerce de bouche marquée, et des zones d'activité en périphérie. "
            "C'est la commune la plus éloignée de notre atelier.",
        "acces":
            "Centre contraint, périphérie dégagée. Meaux est à une cinquantaine de kilomètres : "
            "les interventions s'y planifient à l'avance et se groupent, elles ne se font pas en "
            "urgence.",
        "hotte":
            "Commerces de bouche et restauration de centre-ville, en bâti ancien, avec des "
            "conduits contraints et peu de trappes de visite. C'est la configuration où le constat "
            "préalable compte le plus : sans accès intermédiaire, une ligne longue ne peut pas "
            "être traitée sur toute sa hauteur, et il vaut mieux le savoir avant le devis.",
        "vitres":
            "Vitrines de centre historique, bimensuelles, et façades de locaux d'activité en "
            "périphérie, trimestrielles. La distance rend un contrat régulier plus avantageux "
            "qu'une suite d'interventions ponctuelles.",
        "faq_hotte": ("Intervenez-vous jusqu'à Meaux ?",
                      "Oui, en planifiant. Nous sommes à une cinquantaine de kilomètres : "
                      "l'intervention se cale sur une date convenue à l'avance, de préférence "
                      "groupée avec d'autres établissements du secteur. Les frais de déplacement "
                      "sont annoncés avant que vous validiez."),
        "faq_vitres": ("Un contrat régulier est-il plus intéressant à cette distance ?",
                       "Oui, nettement. Le déplacement est la part fixe du coût : réparti sur des "
                       "passages programmés, et mieux encore sur plusieurs établissements d'un même "
                       "secteur, il pèse beaucoup moins qu'en intervention isolée."),
    },
    {
        "slug": "argenteuil", "nom": "Argenteuil", "cp": "95100", "dept": "95",
        "lat": 48.9474, "lon": 2.2467,
        "tissu":
            "Argenteuil est l'une des plus grandes communes du Val-d'Oise : un centre commerçant "
            "dense autour de la gare et du marché Héloïse, un commerce de bouche très présent, et "
            "des zones d'activité le long de la Seine.",
        "acces":
            "Centre chargé aux heures de marché, périphérie dégagée. Argenteuil est à une "
            "vingtaine de kilomètres de notre atelier, pour un délai habituel de 48 à 72 h.",
        "hotte":
            "Un tissu dense de restauration indépendante et de commerces de bouche, en locaux "
            "souvent anciens et fréquemment repris. Le conduit hérité d'une activité précédente "
            "est ici un cas courant : la peinture neuve ne change rien à ce qui est à l'intérieur, "
            "et nous ouvrons les trappes avant de chiffrer.",
        "vitres":
            "Vitrines de commerce de bouche et de proximité, hebdomadaires en rue passante. Le "
            "trafic du centre dépose un film gras — particules de freinage et hydrocarbures — qui "
            "demande un dégraissage et non un simple lavage.",
        "faq_hotte": ("Je reprends un local, faut-il faire nettoyer le conduit ?",
                      "Oui, et avant l'ouverture plutôt qu'après. Un conduit encrassé par "
                      "l'activité précédente reste encrassé après les travaux, et vous en héritez "
                      "avec la responsabilité qui va avec. Nous ouvrons les trappes et vous "
                      "montrons l'état avant de chiffrer."),
        "faq_vitres": ("Pourquoi ma vitrine se salit-elle si vite en centre-ville ?",
                       "Parce que ce qui s'y dépose est gras : particules de freinage et résidus "
                       "d'hydrocarbures. L'eau claire l'étale au lieu de l'enlever. Il faut un "
                       "dégraissage, puis un rinçage à l'eau déminéralisée."),
    },
    {
        "slug": "sarcelles", "nom": "Sarcelles", "cp": "95200", "dept": "95",
        "lat": 48.9959, "lon": 2.3785,
        "tissu":
            "Sarcelles a un commerce de proximité très dense, avec une restauration de cuisines du "
            "monde particulièrement présente et un centre commercial de centre-ville. Les "
            "commerces de bouche y travaillent sur des volumes importants.",
        "acces":
            "Stationnement praticable hors heures de pointe. Sarcelles est à une quinzaine de "
            "kilomètres de notre atelier, pour un délai habituel de 48 à 72 h.",
        "hotte":
            "Les cuisines du monde — wok, grillades, fritures — produisent les dépôts les plus "
            "difficiles. Le wok en particulier : la très haute température transforme l'huile en "
            "aérosol fin qui traverse les filtres et se dépose loin dans le conduit, bien au-delà "
            "de ce qu'un dégraissage de hotte seule atteint. Deux à trois passages par an sont ici "
            "le bon rythme.",
        "vitres":
            "Vitrines de commerce de proximité, hebdomadaires. Les commerces de bouche cumulent le "
            "film gras intérieur des buées de cuisson et le dépôt extérieur du trafic : les deux "
            "faces demandent un dégraissage, pas seulement un lavage.",
        "faq_hotte": ("La cuisson au wok demande-t-elle un traitement particulier ?",
                      "Oui. La très haute température vaporise l'huile en aérosol beaucoup plus "
                      "fin que la friture classique : il traverse les filtres et se dépose loin "
                      "dans le conduit. Un dégraissage limité à la hotte laisse l'essentiel en "
                      "place. Il faut traiter la ligne par les trappes de visite."),
        "faq_vitres": ("Les deux faces du vitrage sont-elles comprises ?",
                       "Oui, quand la menuiserie permet d'accéder à l'extérieur. Sur un commerce "
                       "de bouche, la face intérieure est même la plus importante : c'est le film "
                       "gras des buées qui éteint la couleur des produits en vitrine."),
    },
    {
        "slug": "cergy", "nom": "Cergy", "cp": "95000", "dept": "95",
        "lat": 49.0361, "lon": 2.0631,
        "tissu":
            "Cergy réunit une préfecture, une université, un quartier d'affaires et un centre "
            "commercial régional. La restauration y est largement collective ou de chaîne, calée "
            "sur le déjeuner des salariés et des étudiants.",
        "acces":
            "Dalles et parkings du quartier d'affaires d'accès réglementé, à organiser avec le "
            "gestionnaire du site. Cergy est à une quarantaine de kilomètres de notre atelier : "
            "les interventions s'y planifient.",
        "hotte":
            "La restauration collective universitaire et administrative fonctionne par calendrier : "
            "des périodes de production intense, puis des fermetures longues. C'est la "
            "configuration la plus confortable pour un dégraissage complet, à condition de réserver "
            "le créneau plusieurs mois à l'avance — tous les établissements visent les mêmes "
            "semaines de vacances scolaires.",
        "vitres":
            "Façades de bureaux et bâtiments universitaires : des surfaces grandes et régulières, "
            "pour partie accessibles depuis le sol. Les portes et les halls à forte fréquentation "
            "sont les seules surfaces qui demandent un passage rapproché ; le reste tient au "
            "trimestre.",
        "faq_hotte": ("Faut-il réserver longtemps à l'avance pour les vacances scolaires ?",
                      "Oui, deux à trois mois. Tous les établissements visent les mêmes semaines "
                      "et le nombre de créneaux de fermeture est limité. Une date fixée en début "
                      "d'année scolaire évite de se retrouver sans solution."),
        "faq_vitres": ("Quel est le délai d'intervention à Cergy ?",
                       "Habituellement 48 à 72 h pour une intervention ponctuelle. Nous sommes à "
                       "une quarantaine de kilomètres : un contrat régulier, avec des passages "
                       "programmés, est nettement plus avantageux à cette distance."),
    },
    {
        "slug": "massy", "nom": "Massy", "cp": "91300", "dept": "91",
        "lat": 48.7262, "lon": 2.2825,
        "tissu":
            "Massy réunit un pôle tertiaire autour de la gare TGV, des zones d'activité étendues "
            "et un centre commerçant. La restauration y est principalement d'entreprise et de "
            "chaîne, concentrée sur le déjeuner.",
        "acces":
            "Zones d'activité bien desservies et faciles d'accès, parkings disponibles. Massy est "
            "à une quarantaine de kilomètres de notre atelier, pour un délai de 48 à 72 h.",
        "hotte":
            "Restauration de flux et restauration d'entreprise : production concentrée sur deux "
            "heures, souvent en friture et en grillade, dans des cuisines bien dimensionnées. Le "
            "rythme utile y est de deux passages par an, et le suivi hebdomadaire des filtres par "
            "l'équipe fait ici une différence réelle sur l'intervalle entre deux dégraissages de "
            "conduit.",
        "vitres":
            "Façades de bureaux et de locaux d'activité, grandes et régulières, accessibles depuis "
            "le sol jusqu'à trois niveaux : la configuration la plus économique à entretenir. Les "
            "halls et les portes vitrées demandent en revanche un passage rapproché.",
        "faq_hotte": ("Les filtres changent-ils vraiment l'intervalle entre deux nettoyages ?",
                      "Oui, nettement. Un filtre propre arrête une part importante de la graisse "
                      "avant le conduit. Des filtres nettoyés ou remplacés chaque semaine — ce que "
                      "la réglementation prévoit — allongent réellement l'intervalle, et c'est le "
                      "geste le plus rentable de tout le dispositif."),
        "faq_vitres": ("Jusqu'à quelle hauteur intervenez-vous ?",
                       "Les trois premiers niveaux depuis le sol, à la perche et à l'eau "
                       "déminéralisée, à condition d'avoir du recul au pied de la façade. Au-delà, "
                       "il faut une nacelle ou un cordiste, et nous ne le faisons pas."),
    },
    {
        "slug": "evry-courcouronnes", "nom": "Évry-Courcouronnes", "cp": "91000",
        "dept": "91", "lat": 48.6238, "lon": 2.4297,
        "tissu":
            "Évry-Courcouronnes réunit une préfecture, une université, un centre hospitalier et un "
            "centre commercial régional. La restauration y est en grande partie collective, avec "
            "des cuisines de gros volume.",
        "acces":
            "Grands équipements dotés de quais de livraison et de parkings. Évry-Courcouronnes est "
            "à une cinquantaine de kilomètres de notre atelier : les interventions s'y planifient "
            "à l'avance.",
        "hotte":
            "Les cuisines de restauration collective sont ici parmi les plus volumineuses et les "
            "plus encadrées : plusieurs lignes de cuisson, un circuit d'extraction long, et une "
            "exigence de traçabilité portée par le service sécurité de l'établissement. "
            "L'intervention se fait sur fermeture programmée, trappe par trappe, avec un essai "
            "d'extraction après remontage et un relevé daté zone par zone.",
        "vitres":
            "Halls, circulations et portes vitrées à très forte fréquentation. Dans un équipement "
            "recevant du public, les portes se marquent en une demi-journée : c'est la surface à "
            "reprendre souvent, le reste tient au trimestre.",
        "faq_hotte": ("Comment prouver que l'entretien a été fait lors d'un contrôle ?",
                      "Par le livret d'entretien annexé à votre registre de sécurité : c'est lui "
                      "qui porte les dates, et c'est à l'exploitant de le tenir. Nous vous "
                      "remettons un relevé daté et détaillé, zone par zone, qui s'y range "
                      "directement."),
        "faq_vitres": ("Comment organiser le nettoyage dans un bâtiment ouvert au public ?",
                       "Zone par zone, aux heures de faible fréquentation, sans jamais fermer un "
                       "accès. Les halls et les portes se font tôt le matin ; les cloisons "
                       "intérieures peuvent se traiter en journée sans gêner personne."),
    },
]


# ---------------------------------------------------------------------------
# NETTOYAGE DE RESTAURANT — angle par commune
# ---------------------------------------------------------------------------
# Le nettoyage de restaurant n'est pas le ménage quotidien que l'équipe assure
# déjà : c'est le passage qui traite ce qu'un service ne permet jamais de
# faire — sols en profondeur, joints de carrelage gras, plinthes, dessous
# d'équipements, surfaces en hauteur, banquettes. Il se vend presque toujours
# avec le dégraissage de hotte, mais il se chiffre séparément.
#
# Écrit à part de VILLES_PRO puis fusionné : garder les quarante angles d'une
# même prestation dans un seul bloc permet de les relire ensemble et de voir
# tout de suite si deux communes disent la même chose.
ANGLES_RESTAURANT = {
    "paris-8": (
        "Les établissements du 8e ont un niveau d'exigence de salle que peu de quartiers "
        "connaissent, et une contrainte qui va avec : rien ne doit se voir. Les banquettes de "
        "velours, les moquettes de salle et les nappages fixes sont les surfaces qui trahissent "
        "l'usage, et elles relèvent de l'injection-extraction, pas du nettoyage courant. Les "
        "cuisines, elles, sont souvent en sous-sol, avec des sols et des joints de carrelage que "
        "le service quotidien ne traite jamais en profondeur.",
        ("Pouvez-vous intervenir sans que la salle soit vue en chantier ?",
         "Oui, c'est la règle ici : intervention de nuit ou le jour de fermeture, salle remise "
         "exactement en l'état, et aucun matériel laissé sur place. Les banquettes et les "
         "moquettes sont traitées par injection-extraction, qui sèche en quelques heures.")),
    "paris-11": (
        "Le 11e, c'est la petite salle : trente à cinquante couverts, cuisine ouverte, banquettes "
        "le long des murs et un sol qui prend tout. Le point qui décide du résultat est le joint "
        "de carrelage de cuisine — gras, noirci, impossible à reprendre pendant un service — et "
        "les dessous d'équipements mobiles, que personne ne déplace en semaine. C'est exactement "
        "ce qu'un passage dédié traite et que le nettoyage quotidien ne peut pas atteindre.",
        ("L'équipe nettoie déjà tous les soirs, qu'apportez-vous de plus ?",
         "Ce qu'un service ne permet pas de faire : les sols en profondeur, joints compris, les "
         "plinthes et les bas de murs, les dessous et arrières d'équipements, les surfaces en "
         "hauteur, et les banquettes en textile. C'est un passage complémentaire, pas un "
         "remplacement du vôtre.")),
    "paris-12": (
        "Les brasseries des abords de la gare de Lyon posent un problème de volume : grande salle, "
        "service continu, et aucune fenêtre de fermeture longue. Le travail se fait de nuit, par "
        "zones, en plusieurs passages plutôt qu'en une remise à niveau unique. Autour d'Aligre, le "
        "profil est inverse : petites salles, fermeture hebdomadaire, et une remise à niveau "
        "complète possible en une fois.",
        ("Comment faire quand le restaurant ne ferme jamais ?",
         "En découpant : une zone par passage, de nuit, plutôt qu'une remise à niveau complète "
         "qui demanderait une fermeture. La salle une nuit, la cuisine une autre, les sanitaires "
         "et les vitrages une troisième. Le résultat est le même, étalé sur trois semaines.")),
    "paris-15": (
        "Le 15e est un arrondissement de restaurants de quartier, fidélisés et installés depuis "
        "longtemps. C'est le profil où la remise à niveau périodique compte le plus : dans une "
        "salle qui tourne depuis dix ans, le gras s'est installé en haut — corniches, luminaires, "
        "grilles de ventilation — et sur les assises textiles, bien avant de se voir au sol.",
        ("À quelle fréquence prévoir une remise à niveau complète ?",
         "Deux à quatre fois par an selon le volume, en complément du nettoyage quotidien de "
         "l'équipe. Les banquettes et les chaises en textile, elles, une à deux fois par an : "
         "c'est ce qui rattrape le grisaillement que personne ne voit arriver.")),
    "paris-16": (
        "Les restaurants du 16e sont en rez-de-chaussée d'immeubles de standing, avec une salle "
        "soignée et une copropriété attentive. Deux conséquences : les horaires d'intervention "
        "sont encadrés, et les parties communes traversées doivent être protégées et rendues "
        "propres. Le travail technique est classique ; c'est la tenue de l'intervention qui est "
        "jugée.",
        ("La copropriété impose des horaires, est-ce compatible ?",
         "Oui. Nous travaillons dans la plage autorisée et nous protégeons les parties communes "
         "traversées. C'est une contrainte d'organisation, pas une contrainte technique : il faut "
         "simplement la connaître avant, pas la découvrir sur place.")),
    "paris-17": (
        "Aux Batignolles, les salles sont petites et les cuisines ouvertes sur la salle. Cela "
        "change la liste : le plafond et les luminaires de salle font partie du périmètre, parce "
        "que les buées non captées s'y déposent, et parce que le client les voit. C'est aussi "
        "l'indice à surveiller — un plafond jauni au-dessus du piano dit que l'extraction ne capte "
        "pas assez.",
        ("Le plafond au-dessus de la cuisine ouverte est jauni, est-ce rattrapable ?",
         "Le dépôt se nettoie, oui. Mais s'il revient en quelques mois, le problème n'est pas le "
         "nettoyage : c'est l'extraction qui ne capte pas assez. Nous vous le disons, et nous "
         "regardons d'abord l'état du conduit, qui est l'hypothèse la moins coûteuse.")),
    "saint-denis": (
        "La restauration dionysienne est diverse et travaille en volume : cuisines du monde autour "
        "du marché, restauration rapide près du stade, brasseries du centre. Les cuisines sont "
        "souvent petites pour le volume produit, et c'est le sol et les joints qui en souffrent "
        "d'abord — un carrelage de cuisine gras devient glissant, ce qui est un sujet de sécurité "
        "avant d'être un sujet de propreté.",
        ("Un sol de cuisine glissant, est-ce rattrapable ?",
         "Oui, dans la plupart des cas : ce qui rend un carrelage glissant est le film gras qui "
         "s'est polymérisé dans le relief antidérapant et l'a comblé. Un dégraissage alcalin avec "
         "temps de pose et une action mécanique le rouvrent. Si le relief est usé, en revanche, "
         "c'est le revêtement qu'il faut reprendre.")),
    "aubervilliers": (
        "Les établissements albertivillariens travaillent tôt et sans temps mort : restauration "
        "de quartier, cantines de grossistes, traiteurs. Les cuisines sont installées dans des "
        "locaux anciens où les plinthes, les bas de murs et les arrières d'équipements n'ont "
        "souvent jamais été repris. C'est là que se trouve l'essentiel du travail réel, pas sur "
        "les surfaces visibles.",
        ("Faut-il vider la cuisine avant votre passage ?",
         "Non. Nous déplaçons les équipements mobiles nous-mêmes et nous les remettons en place. "
         "Ce que nous vous demandons, c'est de dégager les denrées et le petit matériel : le reste "
         "fait partie de l'intervention.")),
    "montreuil": (
        "Montreuil a l'un des tissus de restauration indépendante les plus denses de la petite "
        "couronne, avec beaucoup de cuisines ouvertes et de grands volumes reconvertis. Les "
        "anciens ateliers transformés en salles posent une question propre : des hauteurs sous "
        "plafond importantes, donc des parties hautes — verrières, poutres, luminaires, grilles — "
        "que personne ne traite et qui portent pourtant le dépôt.",
        ("Traitez-vous les parties hautes d'une salle en ancien atelier ?",
         "Depuis le sol et à la perche, jusqu'à une hauteur raisonnable, oui : verrières, poutres "
         "basses, luminaires accessibles. Au-delà, il faut un moyen d'accès en hauteur que nous ne "
         "mettons pas en œuvre, et nous le disons au devis.")),
    "pantin": (
        "Pantin mêle une restauration nouvelle le long du canal, dans des locaux récents et bien "
        "conçus, et un commerce de bouche de centre ancien. Les premiers s'entretiennent avec un "
        "passage programmé deux à quatre fois par an ; les seconds demandent un vrai rattrapage "
        "initial avant de pouvoir être tenus à un rythme régulier.",
        ("Faut-il un premier passage plus lourd que les suivants ?",
         "Souvent, oui, et nous le chiffrons à part. Sur un local qui n'a jamais eu de remise à "
         "niveau, le premier passage est un rattrapage ; les suivants, qui entretiennent un état "
         "déjà atteint, sont plus courts et moins chers. Nous l'annonçons dès le devis.")),
    "bobigny": (
        "La restauration balbynienne est largement tournée vers le midi : brasseries, traiteurs, "
        "restauration rapide autour des administrations et de l'hôpital. Deux heures de service "
        "intense, puis plus rien — ce qui laisse une vraie fenêtre d'intervention l'après-midi, "
        "et c'est rare. Le point sensible reste la cuisine, dont le sol et les joints encaissent "
        "tout le service en une fois.",
        ("Pouvez-vous intervenir l'après-midi, entre deux services ?",
         "Oui, et à Bobigny c'est souvent le meilleur créneau : nous sommes à six kilomètres, "
         "donc une fenêtre de trois heures suffit sans marge de sécurité inutile.")),
    "aulnay-sous-bois": (
        "Aulnay a surtout des restaurants de quartier et des commerces de bouche, en salles "
        "moyennes, avec des équipes réduites. L'intérêt d'un passage dédié y est direct : il libère "
        "l'équipe de ce qu'elle ne peut pas faire correctement en fin de service — les sols en "
        "profondeur, les joints, les surfaces en hauteur — sans allonger ses horaires.",
        ("Est-ce rentable pour un petit établissement ?",
         "Souvent oui, parce que l'alternative est de faire faire ce travail par l'équipe en "
         "heures supplémentaires, moins bien et avec le matériel du bord. Nous sommes à cinq "
         "kilomètres, ce qui rend le déplacement négligeable et un passage court réellement "
         "viable.")),
    "le-blanc-mesnil": (
        "C'est notre commune, et cela change ce que nous pouvons proposer aux restaurants : un "
        "passage court mais fréquent, qui serait absurde ailleurs à cause du trajet, devient ici "
        "la meilleure formule. Un passage hebdomadaire d'une heure sur les sols de cuisine et les "
        "sanitaires tient un établissement mieux qu'une grosse remise à niveau trimestrielle.",
        ("Pouvez-vous passer chaque semaine, même pour une heure ?",
         "Oui, et c'est au Blanc-Mesnil que cela a le plus de sens : l'atelier est dans la "
         "commune, le trajet ne pèse rien. Un passage court et régulier tient un établissement "
         "mieux qu'une intervention lourde tous les trois mois.")),
    "drancy": (
        "Les restaurants drancéens sont en petites salles, avec des cuisines compactes où tout est "
        "serré. La difficulté n'est pas la surface mais l'accès : il faut déplacer pour atteindre, "
        "et c'est précisément ce qu'une équipe ne fait pas en fin de service. Les arrières et "
        "dessous d'équipements sont ici l'essentiel du travail.",
        ("Combien de temps dure une remise à niveau de cuisine ?",
         "Trois à six heures pour une cuisine de taille courante, selon l'état et le nombre "
         "d'équipements à déplacer. Nous travaillons de nuit ou le jour de fermeture, et la "
         "cuisine est opérationnelle au service suivant.")),
    "noisy-le-grand": (
        "La restauration noiséenne est largement tertiaire et de chaîne : des établissements "
        "standardisés, avec des procédures d'entretien internes et des attentes précises sur ce "
        "qui est fait et tracé. C'est le profil qui demande un relevé écrit de chaque passage, "
        "zone par zone, plus qu'un simple accord verbal.",
        ("Fournissez-vous un relevé de ce qui a été fait ?",
         "Oui, daté et détaillé zone par zone, à chaque passage. Pour une enseigne de chaîne, "
         "c'est ce qui permet au siège comme au gérant de suivre, et cela évite les discussions "
         "sur ce qui était compris ou non.")),
    "boulogne-billancourt": (
        "Les restaurants boulonnais sont pour la plupart en rez-de-chaussée d'immeubles "
        "d'habitation, ce qui ajoute une contrainte constante : le bruit et les odeurs vers les "
        "logements du dessus. L'intervention se fait donc dans une plage encadrée, et la question "
        "de l'extraction revient presque toujours dans la conversation — c'est elle qui cause les "
        "plaintes, pas le nettoyage de salle.",
        ("Les voisins se plaignent, le nettoyage peut-il aider ?",
         "Sur les odeurs, ce n'est pas le nettoyage de salle qui agit mais le dégraissage du "
         "circuit d'extraction : un conduit chargé tire moins, et les buées trouvent un autre "
         "chemin. C'est une prestation distincte, que nous assurons aussi, et c'est par là qu'il "
         "faut commencer.")),
    "levallois-perret": (
        "La restauration levalloisienne est calée sur le déjeuner des salariés : service court et "
        "dense, petites salles, cuisines insérées dans des immeubles tertiaires. La fenêtre "
        "d'intervention est large l'après-midi et le soir, ce qui est confortable ; la contrainte "
        "est l'accès au bâtiment en dehors des heures de bureau.",
        ("Comment accéder au local en dehors des heures de bureau ?",
         "Par un accès confié — clé, badge ou code — convenu une fois pour toutes, ou en présence "
         "d'un membre de votre équipe. C'est le point à régler au premier rendez-vous : sans lui, "
         "un planning du soir ne tient pas.")),
    "neuilly-sur-seine": (
        "Les établissements neuilléens ont une salle soignée et une clientèle attentive au détail. "
        "Les surfaces qui trahissent sont les assises en textile, les moquettes et les vitrages "
        "intérieurs — jamais les sols, que l'équipe tient bien. Un passage dédié y porte donc "
        "surtout sur le textile et sur les parties hautes.",
        ("Traitez-vous les banquettes et les chaises en tissu ?",
         "Oui, par injection-extraction : la solution est envoyée dans la fibre puis réaspirée "
         "aussitôt, sans eau stagnante donc sans auréole. Le séchage est de quatre à six heures, "
         "ce qui permet une intervention de nuit avant un service du midi.")),
    "courbevoie": (
        "La restauration de flux du quartier d'affaires produit un volume considérable en deux "
        "heures : sols de salle piétinés, sanitaires très sollicités, cuisine saturée. Le rythme "
        "utile n'est pas le même pour les trois — les sanitaires demandent une reprise "
        "quotidienne, la cuisine un passage profond mensuel, la salle quelque chose entre les "
        "deux.",
        ("Peut-on ne traiter que les sanitaires et la cuisine ?",
         "Oui, et c'est souvent le bon arbitrage quand le budget est contraint. Les sanitaires "
         "clients et la cuisine portent l'essentiel de ce qui se juge ; la salle peut rester au "
         "rythme de votre équipe avec une remise à niveau trimestrielle.")),
    "issy-les-moulineaux": (
        "La restauration isséenne est majoritairement d'entreprise, avec des cuisines dimensionnées "
        "et des services sécurité qui attendent de la traçabilité. L'intervention se cale sur les "
        "fermetures programmées, et le relevé écrit compte autant que le travail lui-même dans le "
        "dossier de l'établissement.",
        ("Pouvez-vous intervenir pendant une fermeture d'entreprise ?",
         "C'est le créneau que nous préférons : site vide, aucune contrainte de service, et le "
         "temps de faire les sols en profondeur et les parties hautes. Les semaines de fermeture "
         "d'août et de fin d'année se réservent plusieurs mois à l'avance.")),
}

ANGLES_RESTAURANT.update({
    "nanterre": (
        "La restauration nanterrienne est largement collective — universitaire, administrative, "
        "d'entreprise — avec de grandes salles et des sols qui encaissent un passage considérable "
        "sur des créneaux courts. Le travail utile y porte sur les sols en profondeur et les "
        "circulations, plus que sur le mobilier, et il se cale sur les périodes de fermeture.",
        ("Quand intervenir sur un restaurant universitaire ?",
         "Pendant les vacances scolaires ou les fermetures d'établissement, et il faut réserver "
         "deux à trois mois à l'avance : tous les établissements visent les mêmes semaines.")),
    "vincennes": (
        "Vincennes a une densité de commerces de bouche et de restaurants exceptionnelle pour sa "
        "taille, sur quelques centaines de mètres. Les salles sont petites, les cuisines aussi, et "
        "presque tout est en rez-de-chaussée d'immeuble ancien. La contrainte est l'horaire : la "
        "rue est commerçante et le voisinage proche.",
        ("Intervenez-vous tôt le matin à Vincennes ?",
         "Oui, avant 7 h 30, dans la plage de livraison autorisée. C'est le créneau qui gêne le "
         "moins le voisinage et qui laisse la salle prête pour le service du midi.")),
    "creteil": (
        "La restauration cristolienne est majoritairement collective ou de chaîne : centre "
        "hospitalier, université, centre commercial. Les volumes sont importants et les exigences "
        "de traçabilité réelles. L'intervention se fait par zones, sur fermeture programmée, avec "
        "un relevé daté que l'établissement range dans son dossier.",
        ("Travaillez-vous avec des établissements de santé ?",
         "Sur la restauration et les espaces communs, oui. En revanche, les protocoles de "
         "désinfection propres aux zones de soins et la filière des déchets d'activités de soins "
         "ne relèvent pas de nous : ce n'est pas notre métier et nous le disons d'emblée.")),
    "ivry-sur-seine": (
        "Les restaurants ivryens sont souvent installés dans d'anciens locaux d'activité "
        "reconvertis : grands volumes, hauteurs importantes, sols béton ou résine. Ces sols ne se "
        "lavent pas comme un carrelage — un produit trop alcalin ternit une résine de façon "
        "irréversible — et c'est le point que nous vérifions avant de commencer.",
        ("Comment nettoyez-vous un sol béton ciré ou en résine ?",
         "À pH neutre, jamais à l'alcalin fort, qui ternit la résine de façon irréversible. Nous "
         "identifions le revêtement avant de commencer et nous testons sur une zone cachée. Sur un "
         "sol déjà attaqué, le nettoyage le rendra propre mais pas neuf, et nous le disons "
         "avant.")),
    "puteaux": (
        "La restauration de flux de La Défense sert des milliers de couverts en deux heures, cinq "
        "jours sur sept. Les sanitaires clients et les sols de salle sont les deux surfaces qui "
        "décaissent tout, et elles demandent une reprise quotidienne ; la cuisine, elle, un "
        "passage profond mensuel.",
        ("Quel rythme pour un établissement à très fort volume ?",
         "Sanitaires et sols de salle repris chaque jour, cuisine en profondeur une fois par "
         "mois, et une remise à niveau complète deux à quatre fois par an. C'est la seule façon de "
         "tenir un site qui ne connaît pas de période creuse.")),
    "rueil-malmaison": (
        "Rueil mêle restaurants de centre-ville et restauration d'entreprise dans les parcs "
        "d'activité. Les seconds se planifient à l'année et s'entretiennent bien ; les premiers, "
        "en bâti plus ancien, demandent un rattrapage initial avant de pouvoir être tenus à un "
        "rythme régulier.",
        ("Le premier passage coûte-t-il plus cher que les suivants ?",
         "Sur un local qui n'a jamais eu de remise à niveau, oui, et nous le chiffrons à part. Les "
         "passages suivants entretiennent un état déjà atteint : ils sont plus courts et moins "
         "chers. C'est annoncé dès le devis.")),
    "saint-cloud": (
        "Saint-Cloud a peu d'établissements mais presque tous en rez-de-chaussée d'immeuble de "
        "standing, avec une salle soignée et une copropriété attentive. L'intervention se fait "
        "dans une plage encadrée, parties communes protégées, et c'est la tenue de l'intervention "
        "qui est jugée autant que le résultat.",
        ("Les parties communes de l'immeuble sont-elles protégées ?",
         "Oui, systématiquement : bâchage du parcours emprunté et nettoyage de la zone après notre "
         "passage. C'est ce que la copropriété regarde, et c'est ce qui décide si vous pourrez "
         "refaire intervenir quelqu'un l'année suivante.")),
    "saint-germain-en-laye": (
        "Le centre historique saint-germanois concentre des restaurants de terrasse et des "
        "commerces de bouche dans du bâti ancien, souvent protégé. Les salles ont du caractère — "
        "parquets, pierres, boiseries — et chaque matière a son produit et ses interdits : c'est "
        "un travail de diagnostic avant d'être un travail de nettoyage.",
        ("Avez-vous l'habitude des salles en bâti ancien ?",
         "Oui, et la règle y est la prudence : un parquet ancien non vitrifié ne supporte pas "
         "l'eau en quantité, une pierre calcaire se tache définitivement à l'acide. Nous "
         "identifions les matières avant de commencer et nous disons quand une surface relève d'un "
         "artisan plutôt que de nous.")),
    "versailles": (
        "La restauration versaillaise est saisonnière : le volume double d'avril à septembre. "
        "Cela devrait décider du calendrier d'entretien — une remise à niveau complète à la sortie "
        "de la haute saison, quand le dépôt est maximal et que la salle peut être immobilisée sans "
        "coût — et c'est un arbitrage que presque personne ne fait.",
        ("Quand faire la remise à niveau d'un restaurant saisonnier ?",
         "À la sortie de la haute saison, pas au milieu. C'est le moment où le dépôt accumulé est "
         "à son maximum et où l'établissement peut être immobilisé sans manque à gagner. "
         "L'intervention coûte le même prix et sert deux fois plus.")),
    "le-vesinet": (
        "Peu d'établissements au Vésinet, et presque tous de quartier, avec une clientèle "
        "d'habitués. Le résultat se joue sur la salle — assises textiles, vitrages, luminaires — "
        "plus que sur la cuisine, que des équipes stables tiennent généralement bien.",
        ("Traitez-vous les assises en tissu de la salle ?",
         "Oui, par injection-extraction, qui sèche en quatre à six heures : une intervention de "
         "nuit permet de rouvrir au service du midi. C'est ce qui rattrape le grisaillement "
         "progressif des assises, qu'un nettoyage courant ne traite pas.")),
    "sceaux": (
        "Les restaurants scéens sont petits, de quartier, avec des équipes réduites et des "
        "cuisines compactes. Un passage dédié y vaut surtout pour ce que l'équipe ne peut pas "
        "faire en fin de service : joints de carrelage, dessous d'équipements, surfaces en "
        "hauteur, grilles de ventilation.",
        ("Un petit établissement a-t-il intérêt à un passage dédié ?",
         "Oui, parce que l'alternative est de le faire faire par l'équipe en heures "
         "supplémentaires, moins bien et avec le matériel du bord. Un passage trimestriel de trois "
         "heures suffit souvent, et il se chiffre modestement.")),
    "saint-maur-des-fosses": (
        "Saint-Maur a des restaurants de quartier répartis entre plusieurs centres, plus des "
        "établissements de bord de Marne très saisonniers. Les seconds appellent une remise à "
        "niveau à la fermeture de saison ; les premiers, un rythme régulier. Grouper plusieurs "
        "établissements d'un même quartier fait réellement baisser le coût au passage.",
        ("Peut-on grouper plusieurs établissements ?",
         "Oui, et c'est avantageux : le déplacement est la part fixe du coût. Réparti sur "
         "plusieurs établissements d'un même secteur, il pèse beaucoup moins, et nous chiffrons "
         "alors au passage et non à l'établissement.")),
    "tremblay-en-france": (
        "La restauration tremblaysienne sert les équipes de la zone aéroportuaire : horaires "
        "décalés, service continu, pas de fenêtre évidente. Notre proximité est ici l'argument "
        "réel — nous nous calons sur le créneau que vous pouvez libérer, même court, même à 3 h du "
        "matin, sans que le trajet n'oblige à élargir la plage.",
        ("Pouvez-vous intervenir en pleine nuit ?",
         "Oui, nous sommes à quinze minutes. Un établissement qui n'a qu'une fenêtre de trois "
         "heures entre deux services est précisément le cas où la proximité de l'atelier change ce "
         "que nous pouvons proposer.")),
    "chelles": (
        "Chelles a une restauration de proximité et des commerces de bouche en locaux souvent "
        "anciens. Le premier passage y est presque toujours un rattrapage : plinthes, bas de murs, "
        "arrières d'équipements et joints de carrelage n'ont jamais été repris. Les suivants, qui "
        "entretiennent, sont nettement plus courts.",
        ("Quelle différence entre le premier passage et les suivants ?",
         "Le premier rattrape ce qui ne l'a jamais été, et il est plus long. Les suivants "
         "entretiennent un état déjà atteint : comptez la moitié du temps. Nous chiffrons les deux "
         "séparément dès le devis, pour que vous sachiez à quoi vous engager.")),
    "meaux": (
        "Meaux a une restauration de centre historique et une tradition de commerce de bouche "
        "marquée, dans du bâti ancien. La distance depuis notre atelier change l'économie de la "
        "prestation : un contrat régulier, avec des passages programmés et si possible groupés "
        "avec d'autres établissements du secteur, est nettement plus avantageux qu'une suite "
        "d'interventions isolées.",
        ("La distance renchérit-elle beaucoup la prestation ?",
         "Sur une intervention isolée, oui. Sur un contrat régulier, le déplacement est réparti "
         "sur des passages programmés, et il pèse peu. C'est encore mieux si plusieurs "
         "établissements du secteur sont traités le même jour.")),
    "argenteuil": (
        "Argenteuil a un tissu dense de restauration indépendante, en locaux fréquemment repris. "
        "Le cas courant est celui d'un établissement qui hérite de l'état laissé par le précédent "
        "exploitant : une remise à niveau complète au moment de la reprise coûte moins cher et "
        "sert plus longtemps qu'une suite de rattrapages partiels.",
        ("Je reprends un local, par quoi commencer ?",
         "Par une remise à niveau complète avant l'ouverture, pendant que le local est vide : "
         "c'est le seul moment où tout est accessible. Et par un constat du conduit d'extraction, "
         "qui est ce dont on hérite sans le voir.")),
    "sarcelles": (
        "La restauration sarcelloise est dense et variée, avec beaucoup de cuisines du monde "
        "travaillant au wok et à la friture. Ces cuissons déposent un film gras fin bien au-delà "
        "de la cuisine : murs, plafond, grilles de ventilation et jusqu'en salle. Le périmètre "
        "utile est donc plus large qu'une simple remise à niveau de sols.",
        ("Le gras se dépose-t-il vraiment jusqu'en salle ?",
         "En cuisson au wok ou en friture, oui, et c'est ce qui rend les surfaces collantes au "
         "toucher bien après le service. L'aérosol est très fin et il circule. Les parties hautes "
         "et les grilles de ventilation font donc partie du périmètre, pas seulement les sols.")),
    "cergy": (
        "La restauration cergyssoise est largement collective — universitaire, administrative — "
        "avec de grandes salles et des sols très sollicités sur des créneaux courts. "
        "L'intervention se cale sur les fermetures, qui sont longues et prévisibles : c'est la "
        "configuration la plus confortable, à condition de réserver tôt.",
        ("Faut-il réserver longtemps à l'avance ?",
         "Oui, deux à trois mois pour les vacances scolaires : tous les établissements visent les "
         "mêmes semaines. Une date fixée en début d'année scolaire évite de se retrouver sans "
         "solution.")),
    "massy": (
        "La restauration massicoise est d'entreprise et de chaîne, concentrée sur le déjeuner. Les "
        "cuisines sont bien dimensionnées et les procédures internes existent : ce qui manque "
        "généralement, c'est le passage profond que le quotidien ne couvre pas — joints, plinthes, "
        "dessous d'équipements, parties hautes.",
        ("Que couvre exactement le passage profond ?",
         "Les sols en profondeur avec les joints de carrelage, les plinthes et bas de murs, les "
         "dessous et arrières d'équipements mobiles, les surfaces en hauteur et les grilles de "
         "ventilation, la salle et les sanitaires clients. C'est ce qu'un service quotidien ne "
         "permet jamais de faire.")),
    "evry-courcouronnes": (
        "La restauration évryenne est en grande partie collective, avec de gros volumes et des "
        "exigences de traçabilité réelles. L'intervention se fait par zones, sur fermeture "
        "programmée, et le relevé daté remis à la fin compte autant que le travail dans le dossier "
        "de l'établissement.",
        ("Fournissez-vous un document à l'issue de l'intervention ?",
         "Oui : un relevé daté et détaillé, zone par zone, de ce qui a été traité. Pour un "
         "établissement collectif, c'est ce qui permet au service sécurité comme à la direction de "
         "suivre, et cela évite les discussions sur ce qui était compris.")),
})

# Fusion dans VILLES_PRO. Un angle manquant ferait une page sans contenu : on
# le refuse ici plutôt que de le découvrir en relisant le site.
for _v in VILLES_PRO:
    _a = ANGLES_RESTAURANT.get(_v["slug"])
    if _a is None:
        raise SystemExit("angle restaurant manquant pour %s" % _v["slug"])
    _v["restaurant"], _v["faq_restaurant"] = _a
del _v, _a


# ---------------------------------------------------------------------------
# NETTOYAGE DE RESTAURANT — périmètre et limites communs
# ---------------------------------------------------------------------------
RESTAURANT_PERIMETRE = (
    "Sols de cuisine en profondeur, joints de carrelage compris",
    "Plinthes, bas de murs, dessous et arrières d'équipements mobiles",
    "Inox : plans, dossenets, étagères, hottes en surface",
    "Surfaces en hauteur : étagères, luminaires, grilles de ventilation",
    "Salle : sols, banquettes et chaises en textile, vitrages intérieurs",
    "Sanitaires clients : détartrage complet, joints, robinetterie",
    "Vitrines et devanture, à l'eau déminéralisée",
    "Remise en place complète : la cuisine est opérationnelle au service suivant",
)

RESTAURANT_LIMITES = (
    "Ce passage ne remplace pas le nettoyage quotidien de votre équipe : il traite ce qu'un "
    "service ne permet jamais de faire. Les deux sont complémentaires, et un prestataire qui "
    "vous propose de remplacer l'un par l'autre vous vend soit trop, soit trop peu.",
    "Le dégraissage de la hotte, des filtres et des conduits d'extraction est une prestation "
    "distincte, que nous assurons également. Les deux se planifient souvent le même soir pour ne "
    "mobiliser la cuisine qu'une fois, mais elles se chiffrent séparément : ni le même matériel, "
    "ni le même temps.",
    "Nous ne faisons ni désinsectisation ni dératisation : elles relèvent d'agréments que nous ne "
    "détenons pas. Nous signalons ce que nous constatons, et nous nous arrêtons là.",
    "Nous n'intervenons pas sur les équipements eux-mêmes : nous nettoyons autour, dessous et "
    "derrière, mais le démontage d'un four ou d'une friteuse relève de votre mainteneur.",
)


# ---------------------------------------------------------------------------
# HAUTE PRESSION PAR SUPPORT
# ---------------------------------------------------------------------------
# C'est la prestation où le support décide de tout. Une même machine, mal
# réglée, nettoie un grès cérame et détruit une pierre de Bourgogne. Chaque
# entrée porte donc le réglage réel et le risque réel, pas une variation de
# vocabulaire — et quand nous ne traitons pas, c'est écrit.
#
# Rappel technique commun : la pression détache, le débit évacue. Monter la
# pression sans monter le débit abîme le support sans mieux nettoyer.
SURFACES_HP = [
    {
        "slug": "terrasse-pierre",
        "nom": "terrasse en pierre",
        "nom_long": "terrasse en pierre naturelle ou reconstituée",
        "le": "une terrasse en pierre",
        "pour": "particulier",
        "enjeu": "La pierre ne se répare pas",
        "probleme":
            "Une pierre naturelle est poreuse, et c'est dans cette porosité que s'installent les "
            "mousses et le noir. D'où la tentation de monter la pression pour aller les chercher — "
            "et c'est exactement ce qu'il ne faut pas faire. Une pierre calcaire tendre, une pierre "
            "de Bourgogne, un travertin se creusent sous une lance trop proche, et le relief ainsi "
            "créé retient davantage la saleté qu'avant.",
        "detail":
            "Le défaut typique est la zébrure : des bandes plus claires et légèrement creusées, "
            "laissées par une lance passée à main levée. Elles ne se rattrapent pas, et elles se "
            "voient pour toujours sous une lumière rasante. L'hydro-brosse rotative travaille à "
            "distance constante et supprime ce risque.",
        "reglage":
            "Pression modérée, hydro-brosse rotative, eau froide. Sur une pierre tendre ou "
            "ancienne, on descend encore et on compense par le temps de passage, jamais par la "
            "pression.",
        "contrainte":
            "Les joints de dallage sablés se déchaussent au lavage : le rejointoiement fait partie "
            "de l'intervention quand c'est le cas, sinon le sable part au premier orage et les "
            "dalles bougent.",
        "faq": ("Ma terrasse en pierre a des taches noires incrustées, partiront-elles ?",
                "Le noir de surface part. Celui qui a pénétré la porosité sur plusieurs années "
                "ressort partiellement, et insister à la pression creuserait la pierre sans "
                "l'enlever. Nous faisons un essai sur une zone cachée et nous vous montrons le "
                "résultat réellement atteignable avant de traiter l'ensemble."),
    },
    {
        "slug": "terrasse-bois",
        "nom": "terrasse en bois",
        "nom_long": "terrasse en bois ou en composite",
        "le": "une terrasse en bois",
        "pour": "particulier",
        "enjeu": "Le bois pardonne le moins",
        "probleme":
            "Le bois est le support sur lequel la haute pression fait le plus de dégâts, et le plus "
            "vite. Une lance trop forte ou trop proche arrache les fibres de surface : la lame "
            "devient pelucheuse, grise plus vite ensuite, et prend l'écharde. C'est irréversible "
            "sans ponçage.",
        "detail":
            "Deux règles qui changent tout : travailler dans le sens de la fibre, jamais en "
            "travers, et garder la buse à distance. Le composite n'est pas plus tolérant — il a "
            "une pression maximale indiquée par son fabricant, souvent basse, et un passage trop "
            "fort y laisse des marques satinées définitives.",
        "reglage":
            "Pression basse, buse large, distance constante, dans le sens des lames. Sur un bois "
            "très grisé, le dégrisage relève d'un produit et d'un ponçage, pas d'une montée en "
            "pression.",
        "contrainte":
            "Nous refusons de laver à haute pression un bois déjà fendu ou dont les lames jouent : "
            "l'eau s'infiltre sous la structure et accélère la dégradation. Nous le disons sur "
            "place plutôt que de prendre le chantier.",
        "faq": ("Peut-on rendre sa couleur d'origine à une terrasse grisée ?",
                "Pas à la haute pression. Le gris est une oxydation de surface du bois : elle se "
                "retire avec un produit dégriseur puis un rinçage, et la couleur se protège "
                "ensuite par une saturation. Monter la pression pour « aller chercher » le gris "
                "arrache les fibres et abîme la lame définitivement."),
    },
    {
        "slug": "terrasse-carrelage",
        "nom": "terrasse carrelée",
        "nom_long": "terrasse en carrelage ou en grès cérame",
        "le": "une terrasse carrelée",
        "pour": "particulier",
        "enjeu": "Le support solide, les joints fragiles",
        "probleme":
            "Le grès cérame et le carrelage extérieur sont les supports les plus tolérants : ils ne "
            "craignent presque rien. Le point faible n'est pas le carreau mais le joint — un joint "
            "de ciment fatigué part sous la pression, et un joint sablé se vide entièrement.",
        "detail":
            "L'autre sujet est l'antidérapant. Un carrelage extérieur a un relief destiné à "
            "éviter les glissades ; le film gras et les mousses le comblent peu à peu, et la "
            "terrasse devient glissante par temps humide. C'est un sujet de sécurité avant d'être "
            "un sujet d'aspect, et c'est le lavage qui le rouvre.",
        "reglage":
            "Pression moyenne à soutenue, hydro-brosse rotative, eau chaude si le dépôt est gras. "
            "Pression réduite au passage des joints.",
        "contrainte":
            "Sur un joint déjà fissuré, nous réduisons la pression et nous vous signalons les "
            "reprises nécessaires : le lavage révèle toujours l'état réel des joints, il ne le "
            "crée pas.",
        "faq": ("Ma terrasse carrelée est glissante, est-ce rattrapable ?",
                "Le plus souvent, oui. Ce qui rend un carrelage extérieur glissant, c'est le film "
                "organique et gras qui a comblé son relief antidérapant. Le lavage le rouvre et la "
                "terrasse redevient sûre. Si le relief lui-même est usé par le temps, en revanche, "
                "aucun nettoyage ne le reconstitue."),
    },
    {
        "slug": "allee-cour",
        "nom": "allée et cour",
        "nom_long": "allée, cour et descente de garage",
        "le": "une allée",
        "pour": "particulier",
        "enjeu": "Ce que l'on voit en arrivant",
        "probleme":
            "Une allée et une cour reçoivent tout : ruissellement de toiture, terre, feuilles, "
            "traces de pneus, gouttes d'huile au droit du véhicule. Les surfaces sont grandes, ce "
            "qui rend la régularité du passage plus importante que la puissance : une allée lavée "
            "à la lance garde des bandes visibles sur toute sa longueur.",
        "detail":
            "Les taches d'hydrocarbures au droit du stationnement sont le vrai sujet. L'eau froide "
            "les étale ; il faut de l'eau chaude et un dégraissant à temps de pose. Une tache "
            "ancienne, qui a pénétré un béton poreux, s'atténue sans disparaître complètement — "
            "nous le disons avant.",
        "reglage":
            "Hydro-brosse rotative sur les surfaces courantes, eau chaude sur les zones grasses, "
            "lance pour les bordures et les caniveaux.",
        "contrainte":
            "L'évacuation doit pouvoir absorber le volume d'eau. Sur une cour fermée sans "
            "écoulement suffisant, nous travaillons par portions pour éviter l'accumulation.",
        "faq": ("Une tache d'huile sur le béton part-elle complètement ?",
                "Rarement en totalité si elle est ancienne. Le béton est poreux : l'huile y "
                "descend, et ce qui est en profondeur ne remonte pas. À l'eau chaude avec un "
                "dégraissant, on retire ce qui est en surface et on atténue nettement le reste. "
                "Promettre la disparition complète serait vous mentir."),
    },
    {
        "slug": "facade-mur",
        "nom": "façade et mur",
        "nom_long": "façade accessible depuis le sol, mur et clôture",
        "le": "une façade",
        "pour": "mixte",
        "enjeu": "Nettoyer sans décaper",
        "probleme":
            "Sur une façade, la haute pression mal employée ne nettoie pas : elle décape. Un enduit "
            "fatigué part en plaques, une peinture se soulève, un joint de maçonnerie ancien se "
            "vide. Et une fois l'enduit entamé, l'eau entre dans le mur — le problème devient "
            "structurel, pas esthétique.",
        "detail":
            "Les surfaces nord et les pignons sans soleil se couvrent de vert : ce sont des algues "
            "et des mousses installées dans la porosité. Le lavage retire ce qui est visible ; "
            "elles reviennent, et sur un mur exposé au nord elles reviennent vite. Nous le disons "
            "d'emblée.",
        "reglage":
            "Pression basse à modérée, buse large, mouvement continu de bas en haut puis rinçage "
            "de haut en bas. Essai obligatoire sur une zone peu visible.",
        "contrainte":
            "Jusqu'à trois niveaux depuis le sol, et seulement avec du recul au pied de la façade. "
            "Au-delà, il faut une nacelle ou un cordiste : nous ne le faisons pas, et nous "
            "l'annonçons avant le devis.",
        "faq": ("Le lavage peut-il abîmer mon enduit de façade ?",
                "Oui, si la pression est mal réglée ou si l'enduit est déjà fatigué. C'est pour "
                "cela que nous commençons par un essai sur une zone peu visible : il montre en "
                "deux minutes si le support tient. S'il ne tient pas, nous refusons le chantier "
                "plutôt que de vous laisser avec une façade à refaire."),
    },
    {
        "slug": "parking-sous-sol",
        "nom": "parking et sous-sol",
        "nom_long": "parking, sous-sol et rampe d'accès",
        "le": "un parking",
        "pour": "pro",
        "enjeu": "Le gras, et où part l'eau",
        "probleme":
            "Un sol de parking accumule un film d'hydrocarbures, de poussières de freinage et de "
            "caoutchouc qui noircit uniformément et rend le sol glissant à l'entrée, là où les "
            "pneus arrivent mouillés. L'eau froide ne l'enlève pas : elle l'étale.",
        "detail":
            "La question à régler avant l'intervention n'est pas technique mais réglementaire : où "
            "partent les eaux de lavage. Chargées d'hydrocarbures, elles ne doivent pas rejoindre "
            "le réseau pluvial. Il faut un séparateur d'hydrocarbures en état de marche, ou une "
            "récupération. Nous vérifions ce point avant de chiffrer, et nous ne lançons pas une "
            "intervention tant qu'il n'est pas tranché.",
        "reglage":
            "Eau chaude, hydro-brosse rotative, dégraissant à temps de pose sur les zones de "
            "stationnement. Lance pour les caniveaux et les pieds de poteaux.",
        "contrainte":
            "Le parking doit être vidé zone par zone. Nous travaillons par tranches, la nuit ou le "
            "week-end, en coordination avec le gestionnaire : c'est l'organisation qui coûte du "
            "temps, pas le lavage.",
        "faq": ("Où partent les eaux de lavage d'un parking ?",
                "C'est la première question à régler, et elle est trop souvent oubliée. Des eaux "
                "chargées d'hydrocarbures ne doivent pas rejoindre le réseau pluvial : il faut un "
                "séparateur d'hydrocarbures en état, ou une récupération. Nous vérifions son "
                "existence et son entretien avant de chiffrer. Sans réponse claire, nous "
                "n'intervenons pas."),
    },
    {
        "slug": "quai-livraison",
        "nom": "quai de livraison",
        "nom_long": "quai de livraison et abords de benne",
        "le": "un quai de livraison",
        "pour": "pro",
        "enjeu": "Les odeurs viennent du sol",
        "probleme":
            "Un quai de livraison et les abords d'une benne concentrent des jus organiques qui "
            "pénètrent le béton et fermentent. L'odeur ne vient pas de la benne elle-même mais du "
            "sol autour, et aucun désodorisant n'y change quoi que ce soit tant que le sol n'est "
            "pas traité.",
        "detail":
            "C'est l'un des rares cas où l'eau chaude n'est pas un confort mais une nécessité : "
            "elle dissout les graisses animales et végétales qui ont figé dans la porosité. À "
            "froid, le lavage déplace l'odeur sans la retirer.",
        "reglage":
            "Eau chaude à température élevée, dégraissant alcalin à temps de pose, hydro-brosse "
            "puis rinçage abondant. Reprise des angles et du pied des murs à la lance.",
        "contrainte":
            "Intervention avant l'ouverture ou après la dernière livraison, et évacuation des eaux "
            "à vérifier comme pour un parking. Un passage mensuel tient un quai ; un passage "
            "annuel ne fait que rattraper.",
        "faq": ("Les odeurs autour de la benne vont-elles disparaître ?",
                "Si elles viennent du sol, oui, et c'est le cas le plus fréquent. Les jus "
                "organiques pénètrent le béton et fermentent : un lavage à l'eau chaude avec "
                "dégraissant les retire. Si l'odeur vient de la benne elle-même ou d'un local mal "
                "ventilé, le lavage du sol ne suffira pas, et nous vous le dirons."),
    },
    {
        "slug": "local-poubelles",
        "nom": "local poubelles",
        "nom_long": "local poubelles et local vide-ordures",
        "le": "un local poubelles",
        "pour": "pro",
        "enjeu": "Le premier motif de réclamation en copropriété",
        "probleme":
            "Le local poubelles est, avec la cage d'escalier, ce qui déclenche le plus de "
            "réclamations auprès d'un conseil syndical. Le sol y est le problème : béton brut, "
            "poreux, imprégné de jus, et des angles que la serpillière n'atteint jamais.",
        "detail":
            "Le lavage à haute pression en local fermé demande une précaution que beaucoup "
            "négligent : la projection. Tout ce qui est au mur et au plafond reçoit ce qui part du "
            "sol. On lave donc du haut vers le bas, puis on reprend le sol, et jamais l'inverse.",
        "reglage":
            "Eau chaude, pression modérée en milieu fermé, dégraissant alcalin, rinçage complet "
            "vers l'évacuation. Reprise des bacs à l'extérieur du local.",
        "contrainte":
            "Il faut une évacuation au sol dans le local, sinon l'eau stagne et le résultat est "
            "pire qu'avant. Quand il n'y en a pas, nous travaillons avec aspiration des eaux, et "
            "nous le chiffrons.",
        "faq": ("Que faire si le local n'a pas de siphon de sol ?",
                "Nous travaillons alors avec aspiration des eaux plutôt qu'au ruissellement : "
                "c'est plus long, donc plus cher, mais c'est la seule méthode propre. Laver à "
                "grande eau un local sans évacuation revient à y laisser une flaque chargée, et "
                "l'odeur revient en deux jours."),
    },
    {
        "slug": "cour-copropriete",
        "nom": "cour de copropriété",
        "nom_long": "cour, hall extérieur et parties communes d'immeuble",
        "le": "une cour de copropriété",
        "pour": "pro",
        "enjeu": "La valeur perçue des lots",
        "probleme":
            "Une cour d'immeuble, un porche et des abords d'entrée sont ce que voient les "
            "résidents, les visiteurs et les acquéreurs potentiels. Ils se dégradent lentement : "
            "pavés noircis, pied de murs vert, caniveaux chargés. Personne ne le remarque d'un "
            "jour à l'autre, tout le monde le constate sur une photo d'annonce.",
        "detail":
            "La difficulté est l'occupation permanente : il n'y a pas d'heure où une cour "
            "d'immeuble est vide. Nous travaillons par portions, en maintenant un cheminement "
            "praticable, et nous séchons les zones de passage avant de partir — une cour mouillée "
            "est un risque de chute dont la copropriété serait responsable.",
        "reglage":
            "Hydro-brosse rotative sur les pavés et le dallage, pression réduite au pied des murs "
            "et sur les joints, lance pour les caniveaux et les grilles.",
        "contrainte":
            "Intervention en semaine, en journée, avec information des résidents par affichage. "
            "Un passage annuel ou semestriel suffit sur une cour entretenue.",
        "faq": ("Faut-il prévenir les résidents ?",
                "Oui, par affichage dans le hall quelques jours avant : c'est ce qui évite les "
                "véhicules mal placés et les réclamations. Nous fournissons le texte au syndic si "
                "besoin. Nous maintenons un cheminement praticable pendant toute l'intervention."),
    },
    {
        "slug": "beton-enrobe",
        "nom": "béton et enrobé",
        "nom_long": "béton désactivé, béton lissé et enrobé",
        "le": "un sol en béton",
        "pour": "mixte",
        "enjeu": "Trois matériaux, trois limites",
        "probleme":
            "On range sous le même mot des supports qui n'ont rien en commun. Un béton désactivé "
            "a des granulats tenus par un liant que la pression peut déchausser. Un béton lissé "
            "est dense et tolérant, mais sa laitance de surface s'use. Un enrobé, lui, est tenu "
            "par un bitume que l'eau chaude ramollit et que la pression arrache.",
        "detail":
            "L'erreur classique est de traiter un enrobé comme un béton. Un enrobé lavé trop fort "
            "perd son liant : les gravillons se déchaussent, la surface devient rugueuse et le "
            "vieillissement s'accélère. Sur ce support, on travaille à pression basse et à l'eau "
            "froide, et on accepte un résultat moins spectaculaire.",
        "reglage":
            "Béton désactivé : pression modérée, hydro-brosse. Béton lissé : pression soutenue "
            "possible. Enrobé : pression basse, eau froide, jamais de dégraissant agressif.",
        "contrainte":
            "Sur un béton désactivé déjà déchaussé, le lavage accentuera le défaut. Nous le "
            "signalons avant : à ce stade, c'est une reprise de surface qu'il faut, pas un "
            "nettoyage.",
        "faq": ("Peut-on nettoyer un enrobé à la haute pression ?",
                "Avec précaution seulement, à pression basse et à l'eau froide. L'enrobé est tenu "
                "par un bitume : l'eau chaude le ramollit et la pression arrache les gravillons. "
                "Le résultat est moins net que sur du béton, et c'est normal — un enrobé propre "
                "reste un enrobé, il ne redevient pas noir."),
    },
]


# Périmètre et limites de la haute pression, écrits une fois. Les limites
# comptent plus ici que sur toute autre prestation : c'est celle où un
# prestataire pressé fait des dégâts irréversibles, et où dire non est le
# vrai service rendu.
HP_PERIMETRE = (
    "Identification du support et essai sur une zone cachée avant de traiter",
    "Hydro-brosse rotative sur les grandes surfaces : pas de zébrures",
    "Eau chaude sur les dépôts gras — parkings, quais, abords de bennes",
    "Pression réglée sur le matériau, et réduite au passage des joints",
    "Rinçage complet et évacuation des résidus",
    "Rejointoiement de sable des dallages quand le lavage l'a entamé",
    "Séchage des zones de passage avant de partir, en site occupé",
    "Eau et électricité fournies : aucun branchement demandé sur place",
)

HP_LIMITES = (
    "Pas de toiture, dans aucun cas. C'est du travail en hauteur, qui demande des compétences et "
    "des équipements que nous n'avons pas. Et les plaques en fibrociment posées avant 1997 "
    "peuvent contenir de l'amiante : le nettoyage haute pression y est à proscrire, parce qu'il "
    "libère des fibres.",
    "Pas de façade au-delà de trois niveaux depuis le sol, ni sans recul au pied du mur. Au-delà, "
    "il faut une nacelle ou un cordiste : ce sont d'autres métiers, d'autres assurances.",
    "Pas de produit de traitement destiné à retarder la repousse des mousses : cette catégorie "
    "relève d'une réglementation à part, et nous n'en appliquons pas. Le lavage retire ce qui est "
    "visible, il n'empêche pas la repousse, et nous le disons plutôt que de laisser croire le "
    "contraire.",
    "Pas de lavage d'un support déjà dégradé — enduit qui se décolle, bois fendu, béton désactivé "
    "déchaussé. La pression y accentuerait le défaut. Nous le constatons sur place et nous "
    "refusons le chantier plutôt que de vous laisser avec une surface à refaire.",
    "Pas de rejet d'eaux chargées d'hydrocarbures au réseau pluvial. Sur un parking ou un quai, "
    "nous vérifions l'existence et l'état du séparateur avant de chiffrer.",
)


# ---------------------------------------------------------------------------
# RISQUE INCENDIE ET OBLIGATIONS — bloc commun aux pages hottes
# ---------------------------------------------------------------------------
# Trois éléments et un seul manque rarement. C'est le mécanisme qu'il faut
# expliquer, pas la peur qu'il faut vendre : un exploitant qui comprend
# pourquoi son conduit brûle fait nettoyer, celui à qui on fait peur change
# de prestataire.
HOTTE_RISQUE = (
    ("Un combustible",
     "La graisse vaporisée par la cuisson condense sur les parois dès que l'air refroidit, et "
     "se polymérise à chaque reprise en chauffe. Elle devient dure, sèche et adhérente : ce "
     "n'est plus de la saleté, c'est un combustible."),
    ("Un comburant, en mouvement",
     "L'air circule en permanence dans le conduit, et en quantité. Un feu qui démarre là "
     "dispose d'exactement ce qu'il lui faut pour se développer, sans que rien ne le freine."),
    ("Une source d'allumage",
     "Une flamme de piano qui monte, un flambage, une friteuse en surchauffe, une étincelle. "
     "Des trois éléments, c'est le seul qui soit accidentel — les deux autres sont déjà là."),
)

HOTTE_PROPAGATION = (
    "Ce qui distingue un feu de conduit d'un feu de cuisine, c'est le chemin. Le conduit est un "
    "volume fermé, étroit et ventilé, qui traverse les planchers jusqu'en toiture. Le feu y "
    "progresse à l'abri des regards, chauffe les parois sur son passage, et peut ressortir à "
    "plusieurs étages de la cuisine. C'est pour cette raison que le texte réglementaire "
    "s'intéresse aux conduits et pas seulement aux hottes.",
    "Un feu de graisse ne s'éteint pas à l'eau : projetée dessus, elle se vaporise "
    "instantanément et disperse le combustible. C'est une donnée que toute équipe de cuisine "
    "devrait connaître avant d'en avoir besoin, et un extincteur de classe F doit être à portée.",
)

# Ce que l'exploitant doit pouvoir présenter. Formulé comme une liste de
# contrôle : c'est ainsi qu'il s'en servira, et c'est ce qui déclenche l'appel.
HOTTE_OBLIGATIONS = (
    "Des filtres nettoyés ou remplacés au moins une fois par semaine — c'est votre équipe, "
    "et c'est le geste le plus rentable de tout le dispositif",
    "Un ramonage des conduits d'évacuation au moins une fois par an, vacuité vérifiée",
    "Un circuit d'extraction nettoyé aussi souvent que nécessaire : une à trois fois par an "
    "selon votre mode de cuisson dominant",
    "Un livret d'entretien annexé au registre de sécurité, où les dates sont portées",
    "Une vérification annuelle des installations de cuisson (article GC 22), par un technicien "
    "compétent ou un organisme agréé, consignée au registre",
    "Une clause d'entretien dans votre contrat d'assurance multirisque : à lire avant le "
    "sinistre, pas après",
)
