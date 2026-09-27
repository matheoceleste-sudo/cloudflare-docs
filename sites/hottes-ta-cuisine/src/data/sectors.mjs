// Secteurs d'activité — une page /secteurs/<slug>.html chacun
export const sectors = [
  {
    slug: "restaurants", name: "Restaurants traditionnels", icon: "plate",
    desc: "Nettoyage de hotte et de cuisine pour restaurants traditionnels et gastronomiques en Île-de-France : intervention hors service, certificat, devis gratuit.",
    lead: "Du bistrot de quartier à la table gastronomique, nous dégraissons votre extraction et nettoyons votre cuisine sans jamais toucher à vos services.",
    context: "Un restaurant traditionnel combine souvent plusieurs modes de cuisson : piano, four, plancha, friteuse, salamandre. L'encrassement est régulier et modéré à fort selon le volume de couverts. Le plus grand enjeu : trouver le bon créneau, car la cuisine tourne midi et soir.",
    risks: ["Graisse mixte (sauteuses, friture, grillade) qui se dépose dans le plénum", "Conduits souvent longs en immeuble parisien", "Peu de temps disponible entre deux services"],
    freq: "2 à 3 dégraissages par an selon le volume",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-cuisine-professionnelle", "contrat-entretien-hotte", "nettoyage-equipements-cuisson"]
  },
  {
    slug: "restauration-rapide", name: "Restauration rapide et snacking", icon: "burger",
    desc: "Dégraissage de hotte pour fast-food, burgers, friteries et snacks : fréquence renforcée, intervention de nuit, certificat pour votre assurance.",
    lead: "Friteuses et grills tournent en continu : votre extraction s'encrasse vite. Nous vous proposons un rythme adapté et des interventions de nuit.",
    context: "La restauration rapide concentre les procédés les plus générateurs de graisse : friture en continu, grill à burgers, plancha. Les amplitudes horaires sont larges, parfois jusque tard dans la nuit. Les filtres saturent en quelques jours.",
    risks: ["Friture intensive et continue", "Filtres saturés très rapidement", "Amplitudes horaires qui réduisent les créneaux"],
    freq: "Tous les 3 à 4 mois",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-filtres-hotte", "contrat-entretien-hotte", "nettoyage-equipements-cuisson"]
  },
  {
    slug: "pizzerias", name: "Pizzerias", icon: "pizza",
    desc: "Nettoyage de hotte et d'extraction pour pizzerias : dégraissage, nettoyage des postes de cuisson et de la cuisine, en complément du ramonage du four.",
    lead: "Four à bois ou à gaz, plancha, friteuse : nous dégraissons votre extraction et nettoyons votre cuisine, en complément du ramonage de votre four.",
    context: "Dans une pizzeria, le four dispose généralement de son propre conduit, qui se ramone. La hotte au-dessus des autres postes (plancha, friteuse, pâtes) doit, elle, être dégraissée. La farine en suspension se mêle à la graisse et forme des dépôts compacts.",
    risks: ["Mélange farine et graisse dans les filtres", "Chaleur intense à proximité du four", "Confusion fréquente entre ramonage et dégraissage"],
    freq: "2 à 3 dégraissages par an",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-equipements-cuisson", "nettoyage-cuisine-professionnelle"]
  },
  {
    slug: "grills-rotisseries-kebabs", name: "Grills, rôtisseries et kebabs", icon: "flame",
    desc: "Dégraissage de hotte pour grills, rôtisseries, kebabs et restaurants de viande : fréquence trimestrielle, graisses lourdes, certificat conforme.",
    lead: "Broches, braises, grills au charbon : ce sont les cuisines les plus exigeantes pour une extraction. Nous les connaissons bien.",
    context: "Les grillades et rôtisseries produisent une graisse animale lourde, chargée de particules carbonisées. Le dépôt dans le conduit est rapide et très combustible. Ce type de cuisine justifie généralement un dégraissage trimestriel.",
    risks: ["Graisse animale lourde et particules carbonisées", "Températures élevées sous la hotte", "Encrassement rapide de la turbine"],
    freq: "Tous les 3 mois",
    services: ["nettoyage-hotte-professionnelle", "degraissage-conduit-extraction", "nettoyage-tourelle-caisson-extraction", "contrat-entretien-hotte"]
  },
  {
    slug: "cuisines-asiatiques", name: "Cuisines asiatiques et woks", icon: "wok",
    desc: "Nettoyage de hotte pour restaurants asiatiques, woks et teppanyaki : graisses fines, flammes hautes, dégraissage renforcé du plénum et du conduit.",
    lead: "La cuisson au wok envoie des graisses fines très loin dans le conduit. Nous adaptons nos produits et notre fréquence à cette cuisine exigeante.",
    context: "Le wok et la cuisson à très haute température produisent des aérosols fins qui franchissent plus facilement les filtres et laissent une laque collante dans le plénum et le conduit.",
    risks: ["Graisse fine et collante difficile à dissoudre", "Flammes qui atteignent les filtres", "Volumes élevés en service rapide"],
    freq: "Tous les 3 mois",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-plenum-hotte", "degraissage-conduit-extraction", "contrat-entretien-hotte"]
  },
  {
    slug: "boulangeries-patisseries", name: "Boulangeries, pâtisseries, traiteurs-snacking", icon: "bread",
    desc: "Nettoyage de hotte et de laboratoire pour boulangeries et pâtisseries avec offre snacking : extraction, fours, plans de travail, chambres froides.",
    lead: "Snacking, viennoiseries, quiches et sandwichs chauds : votre laboratoire a aussi besoin d'une extraction et d'une cuisine impeccables.",
    context: "Les boulangeries qui proposent une offre salée ou traiteur disposent souvent d'une hotte au-dessus des fours ou des postes de cuisson. La farine et la graisse s'y mêlent. Le laboratoire doit par ailleurs répondre aux exigences d'hygiène alimentaire.",
    risks: ["Farine en suspension qui colmate les filtres", "Horaires de nuit qui compliquent les créneaux", "Laboratoire soumis aux contrôles sanitaires"],
    freq: "1 à 2 dégraissages par an",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-cuisine-professionnelle", "nettoyage-chambre-froide"]
  },
  {
    slug: "hotels", name: "Hôtels et résidences", icon: "building",
    desc: "Nettoyage de hotte et de cuisine pour hôtels, restaurants d'hôtel et résidences de tourisme : interventions planifiées, discrètes, certificat pour votre registre.",
    lead: "Petit-déjeuner, room service, restaurant, banquets : nous planifions nos interventions pour qu'elles restent invisibles pour vos clients.",
    context: "Les cuisines d'hôtel fonctionnent souvent de 6 h à minuit, avec plusieurs hottes et des conduits longs qui traversent le bâtiment. Le moindre incident impacte directement la clientèle hébergée.",
    risks: ["Conduits longs traversant plusieurs niveaux", "Plusieurs hottes et zones de cuisson", "Exigence de discrétion vis-à-vis des clients"],
    freq: "2 à 4 dégraissages par an selon l'activité",
    services: ["nettoyage-hotte-professionnelle", "degraissage-conduit-extraction", "contrat-entretien-hotte", "nettoyage-cuisine-professionnelle"]
  },
  {
    slug: "restauration-collective", name: "Restauration collective et cantines", icon: "users",
    desc: "Nettoyage de hotte et de cuisine pour cantines scolaires, restaurants d'entreprise et cuisines centrales : interventions pendant les vacances, certificats, contrats.",
    lead: "Cantines scolaires, restaurants d'entreprise, cuisines centrales : nous intervenons pendant les vacances ou les week-ends, avec des contrats pluriannuels clairs.",
    context: "Les cuisines collectives disposent de grandes hottes et de volumes de production importants, mais souvent de modes de cuisson moins gras qu'en restauration commerciale. Les calendriers sont prévisibles, ce qui facilite la planification.",
    risks: ["Grandes surfaces de hotte et nombreux filtres", "Exigences documentaires des collectivités", "Fenêtres d'intervention concentrées sur les vacances"],
    freq: "1 à 2 dégraissages par an",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-cuisine-professionnelle", "contrat-entretien-hotte", "nettoyage-chambre-froide"]
  },
  {
    slug: "ehpad-etablissements-sante", name: "EHPAD et établissements de santé", icon: "heart",
    desc: "Nettoyage de hotte et de cuisine pour EHPAD, cliniques et établissements de santé : protocoles d'hygiène renforcés, interventions planifiées, traçabilité.",
    lead: "Vos résidents et patients sont fragiles. Nos protocoles d'hygiène et notre traçabilité sont à la hauteur de cette responsabilité.",
    context: "En établissement de santé ou médico-social, la cuisine doit concilier production continue, publics sensibles et exigences de traçabilité élevées. Les interventions doivent être planifiées avec la direction et le responsable de cuisine.",
    risks: ["Public fragile et exigences sanitaires fortes", "Production 7 jours sur 7", "Traçabilité exigée par les autorités de tutelle"],
    freq: "1 à 2 dégraissages par an",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-cuisine-professionnelle", "nettoyage-chambre-froide", "certificat-degraissage-hotte"]
  },
  {
    slug: "dark-kitchens", name: "Dark kitchens et cuisines de livraison", icon: "box",
    desc: "Nettoyage de hotte pour dark kitchens, ghost kitchens et cuisines partagées : fréquence adaptée à l'activité intensive, interventions de nuit.",
    lead: "Plusieurs marques, beaucoup de friture, des amplitudes horaires énormes : votre extraction travaille plus qu'ailleurs. Votre entretien doit suivre.",
    context: "Les cuisines dédiées à la livraison fonctionnent souvent 12 heures par jour ou plus, avec une forte proportion de friture et de grill. Les cuisines partagées imposent un calendrier commun et un interlocuteur unique.",
    risks: ["Activité très intensive et continue", "Plusieurs exploitants sur un même circuit", "Obligations du gestionnaire de site"],
    freq: "Tous les 3 à 4 mois",
    services: ["nettoyage-hotte-professionnelle", "contrat-entretien-hotte", "nettoyage-filtres-hotte", "nettoyage-cuisine-professionnelle"]
  },
  {
    slug: "traiteurs-laboratoires", name: "Traiteurs et laboratoires culinaires", icon: "chef",
    desc: "Nettoyage de hotte, de cuisine et de chambres froides pour traiteurs, laboratoires et cuisines de production : hygiène, traçabilité, interventions planifiées.",
    lead: "Production pour événements, plats cuisinés, préparations : vos laboratoires sont contrôlés de près. Nous vous aidons à rester irréprochables.",
    context: "Les traiteurs et laboratoires produisent par pics, parfois en volumes très importants avant un événement. Les exigences d'hygiène sont élevées et les services sanitaires contrôlent régulièrement ces établissements.",
    risks: ["Pics de production intenses", "Nombreuses chambres froides", "Contrôles sanitaires fréquents"],
    freq: "2 dégraissages par an en moyenne",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-chambre-froide", "nettoyage-cuisine-professionnelle", "nettoyage-avant-ouverture-controle"]
  },
  {
    slug: "food-trucks", name: "Food trucks et cuisines mobiles", icon: "truck",
    desc: "Nettoyage de hotte et de cuisine pour food trucks et remorques de restauration : dégraissage de l'extraction, des équipements et de l'habitacle.",
    lead: "Peu d'espace, beaucoup de cuisson : l'extraction d'un food truck s'encrasse vite. Nous la nettoyons là où votre camion est stationné.",
    context: "Dans un food truck, la hotte est proche des postes de cuisson et du plafond, et le conduit est court. La graisse se dépose vite sur toutes les surfaces du véhicule, et l'espace confiné augmente le risque en cas de départ de feu.",
    risks: ["Espace confiné et proximité des flammes", "Graisse sur toutes les surfaces", "Contrôles lors des événements et marchés"],
    freq: "Tous les 3 à 4 mois selon l'activité",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-filtres-hotte", "nettoyage-equipements-cuisson"]
  }
];
