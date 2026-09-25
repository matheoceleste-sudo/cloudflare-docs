// Prestations Clairvent — chaque entrée génère une page /prestations/<slug>.html
export const services = [
  {
    slug: "nettoyage-hotte-professionnelle",
    nav: "Nettoyage de hotte professionnelle",
    title: "Nettoyage de hotte professionnelle",
    metaTitle: "Nettoyage de hotte professionnelle en Île-de-France | Clairvent",
    desc: "Dégraissage complet de hotte de cuisine professionnelle : hotte, filtres, plénum, conduit et tourelle. Techniciens diplômés, certificat remis, devis gratuit.",
    icon: "hood",
    group: "hotte",
    pillar: true,
    lead: "Le dégraissage complet de votre système d'extraction, de la hotte jusqu'à la tourelle en toiture, réalisé par des techniciens diplômés et formés au risque incendie. Certificat de nettoyage remis le jour même.",
    intro: [
      "Chaque service dépose dans votre hotte une fine pellicule de graisse. Invisible au début, elle s'accumule dans les filtres, colle aux parois du plénum puis tapisse l'intérieur du conduit. Au-delà de quelques millimètres, ce dépôt devient un combustible idéal : une flamme de sauteuse ou un retour de friteuse suffit à l'embraser, et le feu se propage à toute la gaine en quelques secondes.",
      "Notre prestation de nettoyage de hotte professionnelle traite l'ensemble du circuit, pas seulement la partie visible. C'est ce que demande le règlement de sécurité incendie des établissements recevant du public, et c'est ce que vérifient les assureurs après un sinistre."
    ],
    includes: [
      "Protection de la cuisine : bâchage des pianos, plans de travail et sols",
      "Dépose, trempage et dégraissage des filtres à chicanes",
      "Dégraissage intérieur et extérieur de la hotte (caisson, gouttières, rampes)",
      "Nettoyage du plénum et des zones situées derrière les filtres",
      "Dégraissage du conduit d'extraction sur toute sa longueur accessible",
      "Nettoyage du caisson ou de la tourelle d'extraction et de la turbine",
      "Contrôle visuel de la courroie, du moteur et des trappes de visite",
      "Rinçage, séchage, remise en place et essai de fonctionnement",
      "Photos avant / après et certificat de nettoyage daté et signé"
    ],
    steps: [
      ["Visite technique ou étude sur photos", "Nous relevons la longueur de hotte, le tracé du conduit, les accès et le type de cuisson pour chiffrer au plus juste."],
      ["Intervention hors service", "Nous intervenons tôt le matin, entre deux services, la nuit ou le jour de fermeture : votre activité n'est jamais interrompue."],
      ["Dégraissage du circuit complet", "Hotte, filtres, plénum, conduit, extracteur : chaque élément est traité avec la méthode adaptée (mousse active, grattage, brossage, vapeur)."],
      ["Contrôle et rapport", "Photos avant / après, points de vigilance relevés, certificat remis au responsable de l'établissement."]
    ],
    body: `
<h2>Pourquoi le nettoyage de la seule hotte ne suffit pas</h2>
<p>Beaucoup d'établissements font laver leurs filtres et essuient la façade de la hotte en pensant être à jour. C'est une erreur fréquente : l'essentiel de la graisse se trouve derrière les filtres, dans le plénum et le conduit, là où l'air chargé de vapeurs grasses refroidit et se condense. Un incendie de cuisine qui atteint une gaine encrassée devient très difficile à maîtriser.</p>
<p>Le règlement de sécurité contre l'incendie dans les ERP (arrêté du 25 juin 1980, article GC 21) impose un nettoyage de l'ensemble du circuit d'extraction <strong>au minimum une fois par an</strong>. Pour une cuisine très sollicitée, ce rythme doit être renforcé.</p>
<h2>Une méthode adaptée à chaque type de graisse</h2>
<p>Une graisse de friteuse, un dépôt carbonisé de grill ou une laque collante de wok ne se traitent pas de la même manière. Nos techniciens choisissent le procédé et le produit en fonction du support (inox, acier galvanisé, aluminium) et du niveau d'encrassement : dégraissant alcalin en mousse, grattage manuel à la raclette, brossage rotatif du conduit, vapeur sèche ou haute pression selon l'accès.</p>
<h2>Ce que vous recevez à la fin</h2>
<p>À la fin de chaque intervention, vous recevez un certificat de nettoyage mentionnant les éléments traités, la date, le technicien et les éventuelles réserves (zones inaccessibles, trappe de visite manquante, courroie usée). Ce document est celui que demandent la commission de sécurité et votre assureur.</p>`,
    faq: [
      ["Combien de temps dure un nettoyage de hotte professionnelle ?", "Pour une cuisine de restaurant classique (une hotte de 2 à 4 mètres, un conduit droit et une tourelle en toiture), comptez 3 à 5 heures. Une cuisine collective ou un conduit très long peut demander une nuit complète."],
      ["Faut-il fermer le restaurant pendant l'intervention ?", "Non. Nous intervenons en dehors de vos services : tôt le matin, l'après-midi, la nuit ou le jour de fermeture. La cuisine est rendue propre, sèche et prête à l'emploi."],
      ["Quel est le prix d'un nettoyage de hotte ?", "Chaque installation est différente : longueur de hotte, longueur et accessibilité du conduit, niveau d'encrassement, type d'extracteur. C'est pourquoi nos prix sont établis sur devis, gratuit et sans engagement, après une visite ou l'étude de vos photos."],
      ["Remettez-vous un certificat pour l'assurance ?", "Oui, systématiquement. Il est daté, signé, détaille les éléments nettoyés et s'accompagne de photos avant / après."]
    ],
    related: ["reglementation-nettoyage-hotte-erp", "frequence-degraissage-hotte", "incendie-conduit-extraction-comment-l-eviter"]
  },
  {
    slug: "degraissage-conduit-extraction",
    nav: "Dégraissage de conduit d'extraction",
    title: "Dégraissage de conduit d'extraction",
    metaTitle: "Dégraissage de conduit d'extraction de cuisine | Clairvent",
    desc: "Dégraissage intérieur des gaines et conduits d'extraction de cuisine professionnelle : brossage, grattage, mousse active. Certificat conforme au règlement ERP.",
    icon: "duct",
    group: "hotte",
    lead: "Le conduit est la partie la plus dangereuse et la plus négligée de votre extraction. Nous le dégraissons sur toute sa longueur accessible, par les trappes de visite, avec un rapport photo à l'appui.",
    intro: [
      "Entre la hotte et la toiture, l'air chaud se refroidit et la graisse se dépose sur les parois du conduit. Horizontal, vertical, coudé, rectangulaire ou circulaire : chaque tronçon accumule un dépôt qui peut atteindre plusieurs millimètres en quelques mois dans une cuisine intensive.",
      "Nos techniciens accèdent à l'intérieur de la gaine par les trappes existantes, utilisent des brosses rotatives adaptées aux sections circulaires et rectangulaires, et grattent manuellement les dépôts épais avant l'application d'un dégraissant."
    ],
    includes: [
      "Repérage du tracé et des trappes de visite existantes",
      "Protection des zones de passage (faux plafonds, couloirs, locaux traversés)",
      "Grattage des dépôts épais et carbonisés",
      "Brossage rotatif mécanique des sections accessibles",
      "Application de dégraissant alcalin et rinçage maîtrisé",
      "Nettoyage des coudes, des piquages et des registres",
      "Photos intérieures avant / après à chaque trappe",
      "Signalement des zones inaccessibles et conseil de pose de trappes"
    ],
    steps: [
      ["Relevé du réseau", "Longueur, sections, coudes, traversées de plancher : nous cartographions votre conduit pour choisir les outils adaptés."],
      ["Ouverture et protection", "Ouverture des trappes, confinement des zones sensibles, protection des faux plafonds."],
      ["Dégraissage mécanique puis chimique", "Grattage, brossage rotatif, application de mousse dégraissante et récupération des résidus."],
      ["Contrôle photo tronçon par tronçon", "Chaque trappe fait l'objet d'une photo avant / après, jointe à votre certificat."]
    ],
    body: `
<h2>Le conduit, un vecteur de propagation du feu</h2>
<p>Dans la grande majorité des incendies de cuisine professionnelle, le départ de feu est modeste : une poêle qui s'enflamme, un bac de friture qui déborde. C'est la graisse accumulée dans le conduit qui transforme cet incident en sinistre : les flammes sont aspirées, le dépôt s'embrase et le feu peut gagner les étages, la toiture ou les locaux traversés.</p>
<h2>Et si le conduit n'a pas de trappes de visite ?</h2>
<p>C'est fréquent dans les installations anciennes. Nous nettoyons alors tout ce qui est accessible depuis la hotte et depuis l'extracteur, puis nous l'indiquons clairement sur le certificat. Nous vous conseillons sur l'emplacement de trappes à faire poser par votre installateur afin que le conduit puisse être entièrement traité lors du prochain passage.</p>
<div class="callout"><svg class="ico"><use href="#i-info"/></svg><p>Un certificat honnête mentionne les zones non traitées. Méfiez-vous d'une attestation qui certifie « 100 % du réseau » sans aucune trappe de visite : en cas de sinistre, l'expert de l'assurance le verra.</p></div>`,
    faq: [
      ["Comment nettoyez-vous un conduit vertical qui monte sur plusieurs étages ?", "Par le haut depuis l'extracteur en toiture et par le bas depuis la hotte, avec des brosses rotatives montées sur flexibles. Les trappes intermédiaires, quand elles existent, permettent de traiter chaque tronçon."],
      ["Le dégraissage abîme-t-il les conduits en acier galvanisé ?", "Non, à condition d'utiliser le bon produit. Nous adaptons la concentration du dégraissant au matériau et nous rinçons pour ne laisser aucun résidu corrosif."],
      ["Que faire si le conduit passe dans un logement ou un local voisin ?", "Nous protégeons les zones traversées et nous intervenons par les trappes disponibles. Si l'accès est impossible, nous le mentionnons sur le certificat et nous vous conseillons pour la suite."]
    ],
    related: ["trappes-de-visite-conduit-extraction", "incendie-conduit-extraction-comment-l-eviter", "anatomie-systeme-extraction-cuisine"]
  },
  {
    slug: "nettoyage-tourelle-caisson-extraction",
    nav: "Nettoyage de tourelle et caisson d'extraction",
    title: "Nettoyage de tourelle et de caisson d'extraction",
    metaTitle: "Nettoyage de tourelle et caisson d'extraction | Clairvent",
    desc: "Nettoyage de tourelle d'extraction en toiture, caisson de ventilation et turbine : dégraissage, contrôle de la courroie et du moteur. Devis gratuit en Île-de-France.",
    icon: "fan",
    group: "hotte",
    lead: "L'extracteur est le cœur de votre ventilation. Encrassé, il perd en débit, vibre, consomme davantage et finit par tomber en panne. Nous le dégraissons et vérifions ses organes visibles.",
    intro: [
      "Qu'il s'agisse d'une tourelle posée en toiture ou d'un caisson de ventilation installé en combles ou en local technique, l'extracteur reçoit en permanence un air chargé de graisse. Les pales de la turbine s'alourdissent, se déséquilibrent, et le dépôt coule parfois sur la toiture.",
      "Nos techniciens, habilités au travail en hauteur, interviennent en toiture avec les protections collectives ou individuelles adaptées, consignent l'appareil et le dégraissent entièrement."
    ],
    includes: [
      "Consignation électrique de l'extracteur avant intervention",
      "Démontage des capots et accès à la turbine",
      "Dégraissage des pales, de la volute et du caisson",
      "Nettoyage du bac de récupération et des abords en toiture",
      "Contrôle visuel de la courroie, des poulies et de la fixation moteur",
      "Remontage, essai de fonctionnement et vérification du sens de rotation",
      "Signalement des anomalies (bruit, vibration, courroie usée)"
    ],
    steps: [
      ["Accès sécurisé", "Vérification des accès en toiture, mise en place des protections et balisage."],
      ["Consignation", "L'extracteur est mis hors tension et condamné pendant toute l'intervention."],
      ["Dégraissage de la turbine", "Grattage et dégraissage des pales et du caisson, rinçage contrôlé, récupération des eaux grasses."],
      ["Remise en service", "Remontage, essai, contrôle du débit apparent et compte rendu."]
    ],
    body: `
<h2>Les signes d'un extracteur encrassé</h2>
<ul>
<li>La fumée et les odeurs restent dans la cuisine malgré la hotte en marche.</li>
<li>L'extracteur fait plus de bruit qu'avant, ou vibre au démarrage.</li>
<li>De la graisse coule sur la toiture ou autour de la tourelle.</li>
<li>La courroie casse ou patine régulièrement.</li>
</ul>
<p>Ces symptômes indiquent souvent une turbine alourdie par la graisse. Un nettoyage rétablit le débit d'extraction et prolonge la durée de vie du moteur.</p>
<h2>Sécurité en toiture</h2>
<p>Intervenir sur un toit n'est jamais anodin. Nos équipes sont formées au travail en hauteur et n'interviennent qu'avec des accès sécurisés. Si votre toiture n'offre pas d'accès conforme, nous vous le signalons lors de la visite technique et nous proposons une solution adaptée (nacelle, accès par l'intérieur, intervention sur le caisson depuis le local technique).</p>`,
    faq: [
      ["Vous occupez-vous de la maintenance mécanique du moteur ?", "Nous réalisons un contrôle visuel (courroie, poulies, fixations, bruit) et nous signalons toute anomalie. Le remplacement de pièces mécaniques ou électriques relève de votre ventiliste ou de votre installateur, que nous pouvons conseiller."],
      ["À quelle fréquence nettoyer la tourelle ?", "En même temps que le conduit, c'est-à-dire au minimum une fois par an, et plus souvent pour une cuisine intensive. Traiter la hotte sans l'extracteur n'a pas de sens : la graisse de la turbine finit par retomber dans le conduit."]
    ],
    related: ["tourelle-extraction-entretien", "anatomie-systeme-extraction-cuisine", "odeurs-cuisine-restaurant-voisinage"]
  },
  {
    slug: "nettoyage-filtres-hotte",
    nav: "Nettoyage et échange de filtres",
    title: "Nettoyage et échange de filtres de hotte",
    metaTitle: "Nettoyage de filtres de hotte professionnelle | Clairvent",
    desc: "Nettoyage par trempage de vos filtres à chicanes ou échange standard de filtres propres. Service ponctuel ou périodique pour restaurants en Île-de-France.",
    icon: "filter",
    group: "hotte",
    lead: "Des filtres propres, c'est une extraction efficace et un conduit protégé. Nous nettoyons vos filtres par trempage dégraissant, ou nous les échangeons contre un jeu propre lors d'un passage périodique.",
    intro: [
      "Les filtres à chicanes sont la première barrière contre la graisse. Leur rôle est de condenser un maximum de gouttelettes avant qu'elles n'entrent dans le conduit. Saturés, ils laissent passer la graisse et freinent l'aspiration.",
      "Entre deux dégraissages complets, un nettoyage régulier des filtres est la mesure la plus simple et la plus efficace pour garder votre installation saine."
    ],
    includes: [
      "Dépose de l'ensemble des filtres",
      "Trempage dans un bain dégraissant chaud adapté à l'inox ou à l'aluminium",
      "Brossage et rinçage de chaque chicane",
      "Contrôle de l'état (déformation, corrosion, filtres manquants)",
      "Nettoyage des glissières et de la gouttière de récupération",
      "Remise en place et vérification de l'étanchéité du montage",
      "Option : échange standard par un jeu de filtres déjà propres"
    ],
    steps: [
      ["Inventaire", "Nombre, dimensions et matériau de vos filtres."],
      ["Dépose et trempage", "Bain dégraissant chaud, temps de pose adapté au niveau d'encrassement."],
      ["Rinçage et contrôle", "Chaque filtre est rincé, contrôlé et séché."],
      ["Remontage", "Filtres remis en place, glissières et gouttières nettoyées."]
    ],
    body: `
<h2>Filtres à chicanes ou filtres à mailles ?</h2>
<p>Les filtres à mailles (grillage métallique) retiennent la graisse mais s'encrassent très vite et sont difficiles à nettoyer à cœur. Les filtres à chicanes, en inox, forcent l'air à changer de direction : la graisse se condense et s'écoule vers la gouttière. Ils sont recommandés en cuisine professionnelle, plus sûrs face à la flamme et beaucoup plus faciles à entretenir.</p>
<h2>Le lave-vaisselle, une fausse bonne idée ?</h2>
<p>Passer ses filtres au lave-vaisselle professionnel dépanne entre deux interventions, mais cela ne remplace pas un trempage : la graisse cuite reste au fond des chicanes, et elle se redépose dans la machine. Nous expliquons dans notre guide <a href="../conseils/nettoyer-filtres-hotte-professionnelle.html">comment nettoyer les filtres de hotte professionnelle</a> la bonne routine entre deux passages.</p>`,
    faq: [
      ["À quelle fréquence faut-il nettoyer les filtres ?", "En cuisine professionnelle, un nettoyage hebdomadaire par votre équipe est un bon rythme, complété par un trempage professionnel lors de chaque dégraissage. En friture ou grillade intensive, un nettoyage tous les deux ou trois jours peut être nécessaire."],
      ["Proposez-vous des filtres neufs ?", "Nous pouvons vous indiquer les dimensions et le type de filtres adaptés à votre hotte et vous signaler les filtres déformés à remplacer."]
    ],
    related: ["nettoyer-filtres-hotte-professionnelle", "filtres-chicanes-ou-mailles", "entretien-quotidien-hotte-restaurant"]
  },
  {
    slug: "nettoyage-plenum-hotte",
    nav: "Nettoyage du plénum",
    title: "Nettoyage du plénum de hotte",
    metaTitle: "Nettoyage du plénum de hotte de cuisine | Clairvent",
    desc: "Nettoyage du plénum, la zone cachée derrière les filtres de hotte où la graisse s'accumule. Dégraissage complet par des techniciens formés.",
    icon: "layers",
    group: "hotte",
    lead: "Derrière vos filtres se cache le plénum : une chambre qui collecte l'air avant le conduit. C'est souvent la zone la plus grasse de toute la hotte, et la moins nettoyée.",
    intro: [
      "Le plénum est invisible en service : on le découvre en retirant les filtres. Ses parois, son plafond et le départ du conduit se couvrent d'une couche de graisse brunâtre qui peut goutter sur les plats ou s'enflammer au contact d'une flambée.",
      "Nous le traitons systématiquement dans le cadre d'un dégraissage complet, ou lors d'une intervention dédiée si votre conduit a été nettoyé récemment."
    ],
    includes: [
      "Dépose des filtres et protection des équipements de cuisson",
      "Grattage des dépôts sur les parois et le plafond du plénum",
      "Application de dégraissant en mousse et temps de pose",
      "Nettoyage du départ de conduit et du piquage",
      "Nettoyage des gouttières, des bacs et des robinets de vidange",
      "Rinçage et essuyage, remise en place des filtres"
    ],
    steps: [
      ["Dépose des filtres", "Accès complet à la chambre située derrière les filtres."],
      ["Grattage", "Retrait des dépôts épais à la raclette inox."],
      ["Dégraissage", "Mousse active, brossage, rinçage maîtrisé."],
      ["Contrôle", "Photos du plénum avant / après pour votre dossier."]
    ],
    body: `
<h2>Pourquoi le plénum est un point critique</h2>
<p>Placé juste au-dessus des feux, le plénum reçoit l'air le plus chaud et le plus gras de la cuisine. En cas de flambée, c'est la première surface atteinte par les flammes après les filtres. Un plénum encrassé transforme une flamme de quelques secondes en départ de feu.</p>
<p>C'est aussi un enjeu d'hygiène : la graisse qui s'y accumule peut s'oxyder, dégager des odeurs rances et goutter sur les postes de travail, ce qu'un contrôle sanitaire relève immédiatement.</p>`,
    faq: [
      ["Mon équipe peut-elle nettoyer le plénum elle-même ?", "Elle peut essuyer ce qui est accessible, mais le plénum demande un grattage et des produits professionnels difficiles à manipuler en cuisine. Nous recommandons un nettoyage professionnel à chaque dégraissage du circuit."]
    ],
    related: ["anatomie-systeme-extraction-cuisine", "hygiene-hotte-controle-sanitaire", "entretien-quotidien-hotte-restaurant"]
  },
  {
    slug: "certificat-degraissage-hotte",
    nav: "Certificat de dégraissage",
    title: "Certificat de dégraissage de hotte",
    metaTitle: "Certificat de nettoyage de hotte pour l'assurance | Clairvent",
    desc: "Obtenez un certificat de dégraissage de hotte et de conduit, daté et signé, avec photos avant / après. Le document demandé par votre assureur et la commission de sécurité.",
    icon: "doc",
    group: "hotte",
    lead: "Le certificat de nettoyage est la preuve que votre établissement respecte ses obligations. Nous le remettons à l'issue de chaque intervention, avec un dossier photo et la liste précise des éléments traités.",
    intro: [
      "La commission de sécurité le demande lors de ses visites, votre assureur le réclame après un sinistre, et votre bailleur peut l'exiger dans le bail commercial. Le certificat de dégraissage n'est pas une formalité : c'est lui qui prouve, noir sur blanc, que votre installation a été entretenue.",
      "Nous ne délivrons un certificat qu'après intervention réelle de nos techniciens, avec des photos horodatées et une description honnête de ce qui a été traité et de ce qui ne l'a pas été."
    ],
    includes: [
      "Identification de l'établissement et de l'installation",
      "Liste des éléments nettoyés : hotte, filtres, plénum, conduit, extracteur",
      "Longueur de conduit traitée et zones inaccessibles éventuelles",
      "Méthodes et produits utilisés",
      "Observations et recommandations (trappes, courroie, filtres)",
      "Nom du technicien, date et signature",
      "Dossier photo avant / après en annexe",
      "Date conseillée pour le prochain passage"
    ],
    steps: [
      ["Intervention", "Le certificat découle d'un nettoyage réellement effectué par notre équipe."],
      ["Documentation", "Photos avant / après et relevé des points de vigilance pendant l'intervention."],
      ["Remise", "Certificat remis en main propre et envoyé par e-mail au format PDF."],
      ["Suivi", "Nous vous rappelons avant l'échéance du prochain nettoyage."]
    ],
    body: `
<h2>À quoi ressemble notre certificat ?</h2>
<p>Vous pouvez consulter un <a href="../certificat-de-degraissage.html">exemple de certificat de dégraissage</a> pour voir les informations qu'il contient. Il est conçu pour répondre aux questions que pose un préventionniste ou un expert d'assurance : quoi, quand, comment, par qui, et avec quelles réserves.</p>
<h2>Le rôle du certificat en cas de sinistre</h2>
<p>Après un incendie, l'expert mandaté par l'assureur cherche à établir si l'installation était entretenue conformément à la réglementation et au contrat. L'absence de justificatif peut conduire à une réduction d'indemnité ou à un refus de garantie, selon les clauses de votre contrat. Conservez vos certificats au moins cinq ans et joignez-les à votre registre de sécurité.</p>
<div class="callout callout-warn"><svg class="ico"><use href="#i-alert"/></svg><p>Nous ne délivrons jamais de certificat sans intervention. Un certificat de complaisance ne vous protège pas : il vous expose.</p></div>`,
    faq: [
      ["Pouvez-vous établir un certificat pour un nettoyage fait par une autre entreprise ?", "Non. Nous certifions uniquement les travaux réalisés par nos techniciens. Nous pouvons en revanche réaliser un diagnostic de l'état de votre installation."],
      ["Le certificat est-il valable pour la commission de sécurité ?", "Il atteste de l'entretien réalisé et se range dans votre registre de sécurité, que la commission consulte lors de ses visites."],
      ["Combien de temps conserver les certificats ?", "Nous conseillons de conserver l'historique complet dans le registre de sécurité, au minimum cinq ans."]
    ],
    related: ["certificat-nettoyage-hotte-assurance", "registre-securite-cuisine-erp", "commission-securite-cuisine-preparer"]
  },
  {
    slug: "contrat-entretien-hotte",
    nav: "Contrat d'entretien périodique",
    title: "Contrat d'entretien de hotte professionnelle",
    metaTitle: "Contrat d'entretien de hotte et d'extraction | Clairvent",
    desc: "Contrat d'entretien périodique de hotte et de conduit d'extraction : passages planifiés, rappels, certificats. Fréquence adaptée à votre activité, tarif sur devis.",
    icon: "calendar",
    group: "hotte",
    lead: "Ne vous souciez plus des échéances. Nous planifions vos dégraissages selon la fréquence adaptée à votre cuisine, nous vous rappelons avant chaque passage et nous tenons votre historique à jour.",
    intro: [
      "Un restaurant très actif doit faire dégraisser son extraction deux, trois voire quatre fois par an. Entre les services, les fournisseurs et le personnel, il est facile de laisser passer une échéance. Le contrat d'entretien règle ce problème.",
      "Vous choisissez la fréquence avec nous, sur la base de votre type de cuisson et de votre volume. Nous nous chargeons du reste."
    ],
    includes: [
      "Visite initiale et état des lieux complet de l'installation",
      "Calendrier de passages établi à l'avance, sur vos créneaux",
      "Rappel quelques jours avant chaque intervention",
      "Dégraissage du circuit complet à chaque passage",
      "Option : nettoyage intermédiaire des filtres",
      "Certificat et dossier photo à chaque passage",
      "Historique centralisé pour le registre de sécurité",
      "Interlocuteur unique et prioritaire en cas d'urgence"
    ],
    steps: [
      ["État des lieux", "Visite complète, relevé de l'installation et du niveau d'encrassement."],
      ["Fréquence sur mesure", "Nous proposons un rythme justifié par votre activité, jamais surdimensionné."],
      ["Planification", "Les dates sont fixées à l'avance sur vos jours et heures de fermeture."],
      ["Suivi", "Certificats, photos et recommandations archivés et envoyés à chaque passage."]
    ],
    body: `
<h2>Quelle fréquence pour votre contrat ?</h2>
<table>
<thead><tr><th>Type d'activité</th><th>Fréquence indicative</th></tr></thead>
<tbody>
<tr><td>Grill, rôtisserie, friture intensive, wok, kebab</td><td>Tous les 3 mois</td></tr>
<tr><td>Restaurant traditionnel à forte fréquentation, brasserie</td><td>Tous les 4 à 6 mois</td></tr>
<tr><td>Restaurant à activité modérée, restauration collective</td><td>Tous les 6 mois</td></tr>
<tr><td>Faible activité, cuisson vapeur, salon de thé</td><td>Une fois par an (minimum réglementaire)</td></tr>
</tbody>
</table>
<p>Ces valeurs sont indicatives. Utilisez notre <a href="../diagnostic.html">outil de diagnostic</a> pour obtenir une recommandation adaptée à votre cuisine.</p>
<h2>Les avantages d'un contrat</h2>
<ul>
<li><strong>Tranquillité</strong> : plus aucune échéance oubliée, un registre toujours à jour.</li>
<li><strong>Économie</strong> : un circuit entretenu régulièrement se nettoie plus vite qu'un circuit saturé.</li>
<li><strong>Priorité</strong> : en cas de problème (odeur, fumée, extracteur bruyant), vous êtes rappelé en priorité.</li>
</ul>`,
    faq: [
      ["Le contrat m'engage-t-il sur plusieurs années ?", "Nous proposons des contrats annuels, sans reconduction cachée. Le rythme peut être ajusté si votre activité évolue."],
      ["Le tarif du contrat est-il fixé à l'avance ?", "Oui, le devis du contrat précise le prix de chaque passage. Vous savez exactement ce que vous payez sur l'année."]
    ],
    related: ["frequence-degraissage-hotte", "budget-entretien-hotte-restaurant", "choisir-entreprise-nettoyage-hotte"]
  },
  {
    slug: "diagnostic-inspection-extraction",
    nav: "Diagnostic et inspection de l'extraction",
    title: "Diagnostic et inspection de votre extraction",
    metaTitle: "Diagnostic de hotte et inspection de conduit d'extraction | Clairvent",
    desc: "Diagnostic de l'état de votre hotte et de votre conduit d'extraction : niveau d'encrassement, accès, trappes, extracteur. Rapport photo et recommandations.",
    icon: "search",
    group: "hotte",
    lead: "Vous reprenez un fonds de commerce, vous préparez une commission de sécurité ou vous ne savez pas quand votre extraction a été nettoyée pour la dernière fois ? Nous faisons le point avant d'intervenir.",
    intro: [
      "Le diagnostic permet de savoir exactement où vous en êtes : épaisseur du dépôt dans le conduit, état des filtres, présence et position des trappes de visite, accessibilité de l'extracteur, conformité apparente de l'installation.",
      "Il débouche sur un rapport clair et, si nécessaire, sur un devis de nettoyage précis. Aucune mauvaise surprise le jour de l'intervention."
    ],
    includes: [
      "Inspection de la hotte, des filtres et du plénum",
      "Ouverture des trappes et contrôle visuel du conduit",
      "Estimation de l'épaisseur des dépôts gras",
      "Inspection de l'extracteur (accès, état apparent, courroie)",
      "Relevé des trappes manquantes et zones inaccessibles",
      "Rapport photo et recommandations priorisées"
    ],
    steps: [
      ["Rendez-vous", "Une visite d'environ une heure, sur un créneau calme."],
      ["Inspection", "Hotte, conduit, extracteur : nous ouvrons, mesurons, photographions."],
      ["Rapport", "Un document clair, avec les points urgents et les points à surveiller."],
      ["Devis", "Si un nettoyage est nécessaire, vous recevez un devis détaillé."]
    ],
    body: `
<h2>Quand demander un diagnostic ?</h2>
<ul>
<li>À la reprise ou à l'achat d'un restaurant, avant de signer.</li>
<li>Avant la visite périodique de la commission de sécurité.</li>
<li>Lorsque l'historique d'entretien est perdu ou incomplet.</li>
<li>En cas de fumée, d'odeurs persistantes ou de graisse qui coule.</li>
<li>Après un petit départ de feu, même maîtrisé.</li>
</ul>
<p>Pour un repreneur, le diagnostic est aussi un argument de négociation : un conduit jamais nettoyé représente un coût à prévoir dès l'ouverture.</p>`,
    faq: [
      ["Le diagnostic est-il payant ?", "La visite technique préalable à un devis de nettoyage est gratuite. Un diagnostic complet avec rapport écrit, sans nettoyage derrière, fait l'objet d'un devis."]
    ],
    related: ["reprise-restaurant-etat-extraction", "commission-securite-cuisine-preparer", "trappes-de-visite-conduit-extraction"]
  },
  {
    slug: "nettoyage-hotte-particulier",
    nav: "Nettoyage de hotte pour particuliers",
    title: "Nettoyage de hotte pour particuliers",
    metaTitle: "Nettoyage de hotte de cuisine chez les particuliers | Clairvent",
    desc: "Nettoyage en profondeur de votre hotte domestique : filtres, moteur, caisson, façade inox ou verre. Intervention à domicile en Île-de-France, devis gratuit.",
    icon: "home",
    group: "cuisine",
    lead: "Votre hotte aspire moins bien, sent le rance ou colle au toucher ? Nous la démontons, la dégraissons en profondeur et vous la rendons comme neuve, sans rayer ni abîmer les finitions.",
    intro: [
      "Une hotte domestique n'est pas conçue pour être démontée facilement, et les produits vendus en grande surface ne suffisent pas contre une graisse cuite depuis des années. Résultat : on nettoie la façade et les filtres, mais le caisson et le ventilateur restent gras.",
      "Nos techniciens connaissent les principaux modèles (îlot, murale, casquette, plan de travail, intégrée) et savent jusqu'où démonter sans risque."
    ],
    includes: [
      "Protection de la plaque de cuisson et du plan de travail",
      "Dépose et trempage des filtres métalliques",
      "Nettoyage intérieur du caisson et de la grille du ventilateur",
      "Dégraissage de la façade (inox brossé, verre, laqué) sans rayure",
      "Nettoyage de l'éclairage et des commandes",
      "Remplacement du filtre à charbon si vous l'avez fourni",
      "Conseils d'entretien adaptés à votre modèle"
    ],
    steps: [
      ["Prise de rendez-vous", "Vous choisissez un créneau en ligne ou par téléphone."],
      ["Démontage raisonné", "Nous démontons ce qui peut l'être sans risque pour votre appareil."],
      ["Dégraissage", "Produits professionnels adaptés aux finitions, sans solvant agressif."],
      ["Remontage et test", "La hotte est remontée, testée à toutes les vitesses."]
    ],
    body: `
<h2>Combien de fois par an nettoyer une hotte domestique ?</h2>
<p>Les filtres métalliques se lavent idéalement une fois par mois. Un nettoyage complet du caisson et de la façade une à deux fois par an suffit pour une utilisation familiale. Le filtre à charbon d'une hotte en recyclage se remplace, selon les fabricants, tous les trois à six mois.</p>
<p>Pour aller plus loin, consultez notre guide <a href="../conseils/nettoyer-hotte-cuisine-maison.html">comment nettoyer sa hotte de cuisine à la maison</a>.</p>
<h2>Nettoyage de hotte et nettoyage de cuisine</h2>
<p>Beaucoup de nos clients particuliers profitent de l'intervention pour faire nettoyer toute la cuisine : crédence, plaque, four, façades de meubles. Découvrez notre prestation de <a href="nettoyage-cuisine-particulier.html">nettoyage de cuisine pour particuliers</a>.</p>`,
    faq: [
      ["Intervenez-vous pour une seule hotte chez un particulier ?", "Oui. Nous intervenons pour une hotte seule, ou pour la hotte et la cuisine complète, à domicile dans toute l'Île-de-France."],
      ["Utilisez-vous des produits dangereux chez moi ?", "Nous utilisons des dégraissants professionnels dosés pour un usage domestique, et nous rinçons soigneusement. La cuisine peut être utilisée dès notre départ."]
    ],
    related: ["nettoyer-hotte-cuisine-maison", "hotte-domestique-mauvaise-aspiration", "filtre-charbon-hotte-quand-changer"]
  },
  {
    slug: "nettoyage-cuisine-professionnelle",
    nav: "Nettoyage de cuisine professionnelle",
    title: "Nettoyage de cuisine professionnelle",
    metaTitle: "Nettoyage complet de cuisine professionnelle | Clairvent",
    desc: "Nettoyage en profondeur de cuisine de restaurant : sols, murs, plafonds, équipements de cuisson, inox, siphons. Protocole HACCP, techniciens diplômés, devis gratuit.",
    icon: "kitchen",
    group: "cuisine",
    pillar: true,
    lead: "Un grand nettoyage de toute votre cuisine, du plafond aux siphons, réalisé par une équipe formée aux règles d'hygiène alimentaire. Idéal en complément du dégraissage de hotte, ou à chaque période de fermeture.",
    intro: [
      "Le nettoyage quotidien fait par vos équipes maintient la cuisine propre en surface. Mais il y a les zones qu'on n'atteint jamais en service : derrière les pianos, sous les friteuses, les plinthes, les plafonds, les grilles de ventilation, les pieds de tables inox.",
      "Nos techniciens réalisent un nettoyage de fond selon un protocole structuré, du haut vers le bas et du plus propre vers le plus sale, avec des produits compatibles avec le contact alimentaire."
    ],
    includes: [
      "Déplacement des équipements mobiles et nettoyage derrière et dessous",
      "Dégraissage des plafonds, luminaires et grilles de ventilation",
      "Lessivage des murs, carrelages et joints",
      "Dégraissage des pianos, fours, friteuses, grills et salamandres",
      "Nettoyage et désinfection des plans de travail et des inox",
      "Nettoyage des chambres froides et des réfrigérateurs (sur demande)",
      "Récurage des sols, siphons et caniveaux",
      "Désinfection finale des surfaces en contact alimentaire"
    ],
    steps: [
      ["Préparation", "Produits alimentaires rangés et protégés avec vous, équipements débranchés."],
      ["Du haut vers le bas", "Plafonds, murs, équipements, plans de travail, puis sols."],
      ["Désinfection", "Produits conformes au contact alimentaire, rinçage des surfaces concernées."],
      ["Réception", "Tour de la cuisine avec vous, photos et remise des lieux prêts pour le service."]
    ],
    body: `
<h2>Un nettoyage de fond, à quelle fréquence ?</h2>
<p>La plupart des restaurants programment un grand nettoyage de cuisine une à quatre fois par an, souvent pendant les fermetures annuelles, avant une réouverture, ou avant une visite des services vétérinaires. Coupler ce nettoyage au dégraissage de l'extraction est la solution la plus efficace : la graisse qui tombe de la hotte pendant le dégraissage est éliminée dans la foulée.</p>
<h2>Hygiène et plan de maîtrise sanitaire</h2>
<p>Le règlement européen (CE) n° 852/2004, dit « paquet hygiène », impose aux exploitants de maintenir les locaux et équipements propres et en bon état. Notre intervention s'intègre à votre plan de nettoyage et de désinfection : nous vous remettons un compte rendu détaillé à joindre à votre plan de maîtrise sanitaire.</p>
<h2>Et si le résultat ne vous convient pas ?</h2>
<p>Nous faisons le tour de la cuisine avec vous à la fin de l'intervention. Si un point ne vous satisfait pas, nous le reprenons immédiatement. Et si une zone s'avère insuffisamment traitée après notre départ, nous revenons la <a href="remise-en-etat-cuisine.html">nettoyer à nouveau</a>.</p>`,
    faq: [
      ["Combien de temps faut-il pour nettoyer une cuisine de restaurant ?", "Pour une cuisine de 20 à 40 m², comptez une demi-journée à une journée avec une équipe de deux ou trois techniciens. Nous travaillons de nuit ou le jour de fermeture."],
      ["Vos produits sont-ils compatibles avec le contact alimentaire ?", "Oui. Nous utilisons des dégraissants et désinfectants professionnels adaptés aux surfaces en contact avec les denrées, et nous rinçons ces surfaces après application."],
      ["Pouvez-vous intervenir en même temps que le nettoyage de hotte ?", "C'est même recommandé : une seule intervention, une seule fermeture, et un résultat homogène de la toiture jusqu'au sol."]
    ],
    related: ["grand-nettoyage-cuisine-restaurant-checklist", "plan-nettoyage-desinfection-cuisine", "hygiene-hotte-controle-sanitaire"]
  },
  {
    slug: "remise-en-etat-cuisine",
    nav: "Remise en état / nouveau nettoyage de cuisine",
    title: "Remise en état et nouveau nettoyage de cuisine",
    metaTitle: "Remise en état de cuisine et reprise de nettoyage | Clairvent",
    desc: "Cuisine mal nettoyée, reprise d'un nettoyage raté, local laissé en mauvais état : nous refaisons un nettoyage complet de votre cuisine. Devis gratuit sous 24 h.",
    icon: "refresh",
    group: "cuisine",
    lead: "Un premier nettoyage vous a déçu ? Un local vous a été rendu en mauvais état ? Nous reprenons tout depuis le début et nous remettons votre cuisine au niveau d'exigence d'une cuisine professionnelle.",
    intro: [
      "Il arrive qu'un nettoyage ne tienne pas ses promesses : graisse restée derrière les équipements, traces sur l'inox, joints noirs, odeurs persistantes. Il arrive aussi qu'on reprenne une cuisine laissée à l'abandon pendant des mois. Dans les deux cas, il faut refaire un nettoyage, et le refaire bien.",
      "Notre prestation de remise en état commence par un constat précis de ce qui n'a pas été fait, puis applique un protocole complet, avec les outils et les temps d'action nécessaires."
    ],
    includes: [
      "Constat initial avec photos des zones insatisfaisantes",
      "Décapage des graisses anciennes et carbonisées",
      "Détartrage des surfaces et des robinetteries",
      "Rénovation de l'aspect des inox (dégraissage, lustrage dans le sens du grain)",
      "Nettoyage en profondeur des joints de carrelage",
      "Traitement des odeurs (siphons, caniveaux, bacs à graisse accessibles)",
      "Désinfection finale et compte rendu avant / après",
      "Engagement de reprise si un point n'est pas conforme au constat"
    ],
    steps: [
      ["Constat", "Nous listons avec vous chaque point à reprendre, photos à l'appui."],
      ["Décapage", "Les dépôts anciens sont traités avec les produits et temps de pose adaptés."],
      ["Finition", "Inox, carrelages, joints et sols sont remis à niveau."],
      ["Validation", "Réception contradictoire : nous comparons avec le constat initial."]
    ],
    body: `
<h2>Les situations où l'on nous appelle</h2>
<ul>
<li><strong>Un nettoyage précédent décevant</strong>, réalisé par un autre prestataire ou en interne.</li>
<li><strong>La reprise d'un fonds de commerce</strong> dont la cuisine est restée fermée plusieurs mois.</li>
<li><strong>La fin d'un bail</strong> : le local doit être rendu propre au bailleur.</li>
<li><strong>Avant une réouverture</strong> après travaux, sinistre ou fermeture administrative.</li>
<li><strong>Après une mise en demeure</strong> suite à un contrôle sanitaire.</li>
</ul>
<h2>Notre garantie de reprise</h2>
<p>Parce que nous savons ce qu'est une prestation décevante, nous nous engageons : si, lors de la réception, un point listé au constat n'est pas traité correctement, nous le reprenons sans supplément. C'est le principe de toutes nos interventions de nettoyage de cuisine.</p>`,
    faq: [
      ["Pouvez-vous refaire le nettoyage de ma cuisine rapidement ?", "Nous répondons sous 24 heures ouvrées et nous proposons en général une intervention dans la semaine, y compris la nuit ou le dimanche."],
      ["Refaites-vous gratuitement vos propres nettoyages en cas de problème ?", "Oui. Si un point de notre propre prestation n'est pas conforme à ce qui était prévu, nous revenons le reprendre sans frais."]
    ],
    related: ["refaire-nettoyage-cuisine-rate", "reprise-restaurant-etat-extraction", "grand-nettoyage-cuisine-restaurant-checklist"]
  },
  {
    slug: "nettoyage-cuisine-particulier",
    nav: "Nettoyage de cuisine pour particuliers",
    title: "Nettoyage de cuisine pour particuliers",
    metaTitle: "Nettoyage complet de cuisine à domicile | Clairvent",
    desc: "Grand nettoyage de cuisine à domicile : hotte, crédence, plaques, four, façades et intérieurs de meubles, électroménager. Idéal avant un emménagement ou une vente.",
    icon: "sparkle",
    group: "cuisine",
    lead: "Une cuisine qui retrouve son éclat, de la hotte au sol : dégraissage, détartrage, intérieurs de meubles, four et électroménager. Parfait avant un emménagement, une vente ou simplement pour repartir sur de bonnes bases.",
    intro: [
      "Dans une cuisine familiale, la graisse se dépose partout : sur le dessus des meubles hauts, sur la crédence, dans le four, sur les poignées. Le détartrage et le dégraissage de fond prennent des heures et demandent les bons produits.",
      "Nos techniciens appliquent à votre cuisine les méthodes des cuisines professionnelles, avec des produits adaptés à un usage domestique."
    ],
    includes: [
      "Nettoyage complet de la hotte (filtres, caisson, façade)",
      "Dégraissage de la crédence, des joints et des prises",
      "Nettoyage de la plaque (vitrocéramique, induction, gaz)",
      "Nettoyage intérieur du four et du micro-ondes",
      "Façades, poignées et dessus des meubles hauts",
      "Intérieur des placards (option, meubles vidés)",
      "Réfrigérateur intérieur et joints (option)",
      "Évier, robinetterie, détartrage et sol"
    ],
    steps: [
      ["Rendez-vous", "En ligne ou par téléphone, 7 jours sur 7."],
      ["Protection", "Nous protégeons les sols et les surfaces fragiles."],
      ["Nettoyage complet", "Du haut vers le bas, selon la liste validée avec vous."],
      ["Contrôle avec vous", "Tour de la cuisine avant notre départ."]
    ],
    body: `
<h2>Pour quelles occasions ?</h2>
<ul>
<li>Avant d'emménager, pour partir d'une cuisine vraiment propre.</li>
<li>Avant un état des lieux de sortie, pour récupérer votre dépôt de garantie.</li>
<li>Avant la vente ou la mise en location d'un bien.</li>
<li>Après des travaux, pour éliminer poussière et résidus.</li>
<li>Une ou deux fois par an, pour entretenir durablement.</li>
</ul>`,
    faq: [
      ["Dois-je vider mes placards ?", "Seulement si vous souhaitez l'option de nettoyage intérieur des meubles. Pour un nettoyage extérieur, il suffit de dégager les plans de travail."],
      ["Combien de temps dure le nettoyage d'une cuisine à domicile ?", "De 3 à 6 heures selon la taille de la cuisine, son état et les options choisies."]
    ],
    related: ["nettoyer-hotte-cuisine-maison", "degraisser-cuisine-maison-methode-pro", "nettoyage-cuisine-etat-des-lieux"]
  },
  {
    slug: "nettoyage-cuisine-apres-sinistre",
    nav: "Nettoyage après incendie ou sinistre",
    title: "Nettoyage de cuisine après incendie ou sinistre",
    metaTitle: "Nettoyage de cuisine après incendie, fumée ou dégât | Clairvent",
    desc: "Nettoyage de cuisine après un départ de feu, des fumées ou un dégât des eaux : suies, graisses brûlées, odeurs. Intervention rapide et rapport pour votre assureur.",
    icon: "fire",
    group: "cuisine",
    lead: "Après un départ de feu, même maîtrisé, les suies et les graisses brûlées se déposent partout. Nous intervenons rapidement pour nettoyer, désodoriser et vous permettre de rouvrir dans les meilleures conditions.",
    intro: [
      "Un feu de friteuse ou de hotte laisse derrière lui des suies grasses, acides et corrosives, qui s'incrustent sur l'inox, les murs et les équipements. Plus on attend, plus elles sont difficiles à retirer.",
      "Nous intervenons après le passage de l'expert de votre assurance, ou en coordination avec lui, et nous documentons chaque étape."
    ],
    includes: [
      "Constat photo détaillé pour votre dossier d'assurance",
      "Retrait des suies sèches par aspiration et éponges spécifiques",
      "Dégraissage des suies grasses sur toutes les surfaces",
      "Dégraissage complet du circuit d'extraction touché",
      "Nettoyage des équipements récupérables",
      "Traitement des odeurs de fumée",
      "Compte rendu et certificat de nettoyage de l'extraction"
    ],
    steps: [
      ["Mise en sécurité", "Nous intervenons une fois l'installation électrique et gaz vérifiée."],
      ["Constat", "Photos et relevé des surfaces et équipements touchés."],
      ["Nettoyage", "Suies sèches, suies grasses, extraction, équipements, sols."],
      ["Rapport", "Document remis pour votre assureur et votre réouverture."]
    ],
    body: `
<h2>Ne rallumez pas l'extraction après un feu de hotte</h2>
<p>Après un feu, le conduit peut contenir des résidus incandescents ou des dépôts fragilisés. Avant toute remise en service, faites contrôler et nettoyer l'ensemble du circuit. Notre guide <a href="../conseils/que-faire-apres-feu-de-hotte.html">que faire après un feu de hotte</a> détaille les étapes à suivre.</p>`,
    faq: [
      ["Travaillez-vous avec les assurances ?", "Nous établissons des devis et des rapports détaillés que vous pouvez transmettre à votre assureur ou à l'expert. Le règlement est convenu avec vous au moment du devis."]
    ],
    related: ["que-faire-apres-feu-de-hotte", "feu-de-friteuse-bons-reflexes", "incendie-conduit-extraction-comment-l-eviter"]
  },
  {
    slug: "nettoyage-equipements-cuisson",
    nav: "Nettoyage pianos, fours, friteuses",
    title: "Nettoyage des pianos, fours et friteuses",
    metaTitle: "Nettoyage de piano, four, friteuse et grill professionnels | Clairvent",
    desc: "Dégraissage en profondeur des équipements de cuisson professionnels : pianos, fours mixtes, friteuses, grills, planchas, salamandres. Techniciens formés.",
    icon: "flame",
    group: "cuisine",
    lead: "Vos équipements de cuisson sont vos outils de production. Nous les dégraissons en profondeur, jusque dans les zones que vos équipes ne peuvent pas atteindre en service.",
    intro: [
      "Sous les brûleurs, derrière les panneaux latéraux, dans les bacs de récupération : la graisse cuite s'accumule et finit par gêner le fonctionnement, dégager de la fumée et des odeurs, voire provoquer des départs de feu.",
      "Nous traitons chaque équipement selon ses spécificités et les recommandations du fabricant."
    ],
    includes: [
      "Pianos : grilles, brûleurs, chapeaux, bacs et habillages",
      "Fours mixtes et fours à convection : enceinte, joints, grilles (hors détartrage générateur)",
      "Friteuses : vidange, dégraissage de la cuve et de l'habillage",
      "Grills, planchas, salamandres, rôtissoires, broches",
      "Déplacement et nettoyage derrière et sous les équipements",
      "Remontage et vérification visuelle du bon état"
    ],
    steps: [
      ["Mise hors service", "Équipements froids, gaz et électricité coupés."],
      ["Démontage", "Pièces amovibles déposées et mises à tremper."],
      ["Dégraissage", "Graisses cuites et carbonisées traitées au bon produit."],
      ["Remontage", "Pièces remises en place, équipements prêts à l'emploi."]
    ],
    body: `
<h2>Un complément naturel du dégraissage de hotte</h2>
<p>Les équipements de cuisson sont la source de la graisse qui encrasse votre hotte. Une friteuse dont l'habillage est gras, un grill dont les bacs débordent augmentent aussi le risque d'inflammation sous la hotte. Traiter les deux ensemble, c'est agir à la source et sur la conséquence.</p>`,
    faq: [
      ["Détartrez-vous les générateurs de vapeur des fours mixtes ?", "Le détartrage du générateur relève de la maintenance technique préconisée par le fabricant. Nous nettoyons l'enceinte, les grilles et les joints, et nous vous signalons tout besoin de maintenance."]
    ],
    related: ["feu-de-friteuse-bons-reflexes", "grand-nettoyage-cuisine-restaurant-checklist", "entretien-quotidien-hotte-restaurant"]
  },
  {
    slug: "nettoyage-chambre-froide",
    nav: "Nettoyage de chambres froides",
    title: "Nettoyage et désinfection de chambres froides",
    metaTitle: "Nettoyage et désinfection de chambre froide | Clairvent",
    desc: "Nettoyage et désinfection de chambres froides positives et négatives, armoires réfrigérées et vitrines. Protocole hygiène, intervention hors service.",
    icon: "snow",
    group: "cuisine",
    lead: "Parois, rayonnages, joints, évaporateur accessible, sol : nous nettoyons et désinfectons vos chambres froides et armoires réfrigérées dans le respect de la chaîne du froid.",
    intro: [
      "Une chambre froide sale, c'est un risque de contamination croisée, de moisissures sur les joints et d'odeurs qui imprègnent les denrées. C'est aussi un point systématiquement contrôlé par les services sanitaires.",
      "Nous organisons l'intervention avec vous pour limiter au maximum la durée pendant laquelle vos produits sont déplacés."
    ],
    includes: [
      "Organisation du déstockage temporaire avec votre équipe",
      "Nettoyage des parois, du plafond et de la porte",
      "Démontage et nettoyage des rayonnages",
      "Nettoyage des joints de porte et des rideaux à lanières",
      "Nettoyage des surfaces accessibles de l'évaporateur et du bac de condensats",
      "Désinfection finale et séchage avant remise en froid"
    ],
    steps: [
      ["Planification", "Créneau choisi pour limiter la durée de déstockage."],
      ["Nettoyage", "Du plafond au sol, rayonnages démontés."],
      ["Désinfection", "Produit adapté au contact alimentaire, temps d'action respecté."],
      ["Remise en service", "Séchage, remise en froid, restockage avec vous."]
    ],
    body: `
<h2>À quelle fréquence nettoyer une chambre froide ?</h2>
<p>Un nettoyage des sols et des surfaces de contact fait partie du nettoyage courant. Un nettoyage complet avec démontage des rayonnages est recommandé au moins une fois par mois en restauration, et dès qu'un incident (fuite, casse, produit renversé) le nécessite. Le plan de nettoyage de votre établissement doit préciser ce rythme.</p>`,
    faq: [
      ["Intervenez-vous sur la partie frigorifique ?", "Non, la maintenance du groupe froid relève d'un frigoriste. Nous nettoyons les surfaces accessibles sans démonter les organes techniques."]
    ],
    related: ["plan-nettoyage-desinfection-cuisine", "hygiene-hotte-controle-sanitaire", "grand-nettoyage-cuisine-restaurant-checklist"]
  },
  {
    slug: "nettoyage-avant-ouverture-controle",
    nav: "Nettoyage avant ouverture ou contrôle",
    title: "Nettoyage avant ouverture ou contrôle sanitaire",
    metaTitle: "Nettoyage de cuisine avant ouverture ou contrôle sanitaire | Clairvent",
    desc: "Préparez l'ouverture de votre restaurant, une réouverture ou un contrôle sanitaire : dégraissage de hotte, nettoyage complet de cuisine, certificat et compte rendu.",
    icon: "shield",
    group: "cuisine",
    lead: "Ouverture d'un nouveau restaurant, réouverture après travaux ou visite annoncée des services sanitaires : nous préparons votre cuisine et votre extraction pour que tout soit irréprochable le jour J.",
    intro: [
      "Une ouverture ou un contrôle se préparent. Poussières de chantier, graisses de l'exploitant précédent, extraction jamais nettoyée : autant de points qui peuvent retarder une ouverture ou conduire à une mise en demeure.",
      "Nous réalisons en une seule intervention le dégraissage de l'extraction, le nettoyage complet de la cuisine et la remise des documents qui vont avec."
    ],
    includes: [
      "Dégraissage du circuit d'extraction complet et certificat",
      "Nettoyage après travaux : poussières, résidus de colle et de ciment",
      "Nettoyage complet des équipements et des surfaces",
      "Nettoyage des chambres froides et réserves",
      "Désinfection des surfaces en contact alimentaire",
      "Compte rendu à joindre au plan de maîtrise sanitaire"
    ],
    steps: [
      ["Point sur le calendrier", "Nous calons l'intervention au plus près de votre date d'ouverture ou de contrôle."],
      ["Extraction", "Dégraissage complet et certificat."],
      ["Cuisine", "Nettoyage de fond de toutes les zones."],
      ["Documents", "Certificat, photos et compte rendu remis."]
    ],
    body: `
<h2>Les points que regardent les contrôleurs</h2>
<p>Lors d'une inspection, les agents des services vétérinaires (DDPP) observent l'état général des locaux, la propreté des équipements, la présence de graisse sur les hottes et les plafonds, l'état des chambres froides, et consultent votre plan de nettoyage. Notre guide <a href="../conseils/hygiene-hotte-controle-sanitaire.html">hygiène de la hotte et contrôle sanitaire</a> détaille ces points.</p>`,
    faq: [
      ["Pouvez-vous intervenir dans l'urgence avant un contrôle ?", "Nous faisons notre maximum pour intervenir sous quelques jours, y compris la nuit et le week-end. Appelez-nous directement pour les situations urgentes."]
    ],
    related: ["hygiene-hotte-controle-sanitaire", "ouvrir-restaurant-checklist-extraction", "commission-securite-cuisine-preparer"]
  }
];
