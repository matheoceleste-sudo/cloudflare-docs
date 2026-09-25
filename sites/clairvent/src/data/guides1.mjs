// Conseils (1/2) — réglementation, sécurité incendie, hygiène
export const guides1 = [
  {
    slug: "reglementation-nettoyage-hotte-erp",
    cat: "reg",
    title: "Nettoyage de hotte : ce que dit la réglementation en ERP",
    desc: "Article GC 21, fréquence minimale, certificat, responsabilités : tout ce que la réglementation impose aux cuisines professionnelles recevant du public.",
    services: ["nettoyage-hotte-professionnelle", "certificat-degraissage-hotte"],
    body: `
<p>Restaurants, brasseries, hôtels, cantines, établissements de santé : dès lors qu'une cuisine se trouve dans un établissement recevant du public (ERP), son système d'extraction est soumis à des règles précises. Voici l'essentiel à connaître, sans jargon.</p>
<h2>Le texte de référence : le règlement de sécurité incendie</h2>
<p>Le règlement de sécurité contre les risques d'incendie et de panique dans les ERP est fixé par l'arrêté du 25 juin 1980. Sa section consacrée aux « grandes cuisines » (articles GC) encadre la conception et l'entretien des installations de cuisson et d'extraction. L'article GC 21 prévoit notamment que les installations d'extraction soient entretenues et que les conduits, filtres et extracteurs fassent l'objet d'un nettoyage <strong>au minimum une fois par an</strong>.</p>
<p>Ce minimum annuel concerne l'ensemble du circuit : hotte, filtres, plénum, conduit et extracteur. Nettoyer seulement les filtres ne permet pas de respecter cette obligation.</p>
<h2>Une fréquence minimale, pas une fréquence idéale</h2>
<p>Une fois par an, c'est le plancher réglementaire. Une cuisine qui fait de la friture, du grill ou du wok plusieurs heures par jour encrasse son conduit bien plus vite. Les professionnels du secteur recommandent couramment un rythme de deux à quatre dégraissages par an pour les cuisines intensives. Consultez notre guide <a href="frequence-degraissage-hotte.html">à quelle fréquence dégraisser sa hotte</a> pour déterminer le bon rythme.</p>
<h2>Qui est responsable ?</h2>
<p>L'exploitant de l'établissement est responsable de l'entretien de ses installations techniques. Dans le cadre d'un bail commercial, la répartition entre locataire et propriétaire dépend des clauses du bail : l'entretien courant (dont le dégraissage) incombe le plus souvent à l'exploitant. Nous détaillons ce point dans <a href="responsabilite-locataire-proprietaire-hotte.html">qui doit payer le nettoyage de la hotte</a>.</p>
<h2>La preuve : certificat et registre de sécurité</h2>
<p>Chaque intervention doit être justifiée. Le certificat de nettoyage remis par l'entreprise est à conserver dans le registre de sécurité de l'établissement, que la commission de sécurité consulte lors de ses visites périodiques. En cas de sinistre, c'est également ce document que demandera l'expert de votre assureur.</p>
<h2>Les autres textes à connaître</h2>
<ul>
<li><strong>Le Code du travail</strong> impose que les installations d'aération et d'assainissement des locaux de travail soient maintenues en bon état de fonctionnement.</li>
<li><strong>Le règlement (CE) n° 852/2004</strong> relatif à l'hygiène des denrées alimentaires impose des locaux et équipements propres et entretenus.</li>
<li><strong>Le règlement sanitaire départemental</strong> peut contenir des dispositions sur l'évacuation des fumées et des odeurs.</li>
<li><strong>La norme NF EN 16282</strong> fournit des références techniques pour la ventilation des cuisines professionnelles.</li>
<li><strong>Votre contrat d'assurance</strong> peut fixer ses propres exigences de fréquence : relisez-le.</li>
</ul>
<div class="callout"><svg class="ico"><use href="#i-info"/></svg><p>Cet article est un guide pratique et ne remplace pas la lecture des textes officiels ni l'avis de votre préventionniste ou de votre assureur.</p></div>`
  },
  {
    slug: "frequence-degraissage-hotte",
    cat: "reg",
    title: "À quelle fréquence faut-il dégraisser sa hotte professionnelle ?",
    desc: "Minimum réglementaire, type de cuisson, volume de couverts : comment déterminer la bonne fréquence de nettoyage de votre hotte et de votre conduit.",
    services: ["contrat-entretien-hotte", "nettoyage-hotte-professionnelle"],
    body: `
<p>« Une fois par an, c'est suffisant ? » C'est la question que l'on nous pose le plus. La réponse honnête : cela dépend de ce que vous cuisinez, de combien vous cuisinez et de la qualité de vos filtres.</p>
<h2>Le minimum : une fois par an</h2>
<p>Pour un ERP, le règlement de sécurité incendie impose au minimum un nettoyage annuel de l'ensemble du circuit d'extraction. C'est une obligation, pas une recommandation. Mais c'est un minimum pensé pour les cuisines à activité modérée.</p>
<h2>Les quatre facteurs qui accélèrent l'encrassement</h2>
<ol>
<li><strong>Le type de cuisson.</strong> Friture, grillade, plancha, wok et rôtisserie projettent beaucoup plus de graisse que la cuisson vapeur ou le four.</li>
<li><strong>Le volume.</strong> Un restaurant qui sert 300 couverts par jour encrasse sa hotte trois fois plus vite qu'un restaurant à 100 couverts.</li>
<li><strong>Les heures de cuisson.</strong> Une cuisine qui tourne de 11 h à 23 h sans coupure n'a rien à voir avec un service unique le midi.</li>
<li><strong>L'état des filtres.</strong> Des filtres à chicanes propres retiennent une grande partie de la graisse. Des filtres saturés ou à mailles la laissent passer dans le conduit.</li>
</ol>
<h2>Les fréquences couramment recommandées</h2>
<table>
<thead><tr><th>Profil</th><th>Exemples</th><th>Fréquence</th></tr></thead>
<tbody>
<tr><td>Très forte production de graisse</td><td>Kebab, grill au charbon, friterie, wok, rôtisserie</td><td>Tous les 3 mois</td></tr>
<tr><td>Forte</td><td>Brasserie, restauration rapide, pizzeria à fort volume</td><td>Tous les 4 mois</td></tr>
<tr><td>Modérée</td><td>Restaurant traditionnel, restauration collective</td><td>Tous les 6 mois</td></tr>
<tr><td>Faible</td><td>Salon de thé, cuisson vapeur, faible volume</td><td>Une fois par an</td></tr>
</tbody>
</table>
<p>Ces rythmes s'inspirent des pratiques professionnelles courantes et des référentiels internationaux. Ils doivent être ajustés à l'état réel constaté lors de chaque passage : c'est l'intérêt d'un prestataire qui photographie l'intérieur du conduit.</p>
<h2>Testez votre installation</h2>
<p>Notre <a href="../diagnostic.html">outil de diagnostic en ligne</a> vous donne en trente secondes une recommandation adaptée à votre cuisine. Pour une évaluation précise, demandez une visite technique gratuite.</p>`
  },
  {
    slug: "incendie-conduit-extraction-comment-l-eviter",
    cat: "feu",
    title: "Incendie de conduit d'extraction : comment il se produit et comment l'éviter",
    desc: "Comprendre le mécanisme d'un feu de gaine en cuisine professionnelle et les mesures concrètes pour réduire ce risque au quotidien.",
    services: ["degraissage-conduit-extraction", "nettoyage-hotte-professionnelle"],
    body: `
<p>Le feu de conduit est l'un des sinistres les plus redoutés en restauration. Rapide, difficile à atteindre, il peut se propager bien au-delà de la cuisine. Bonne nouvelle : il est en grande partie évitable.</p>
<h2>Le mécanisme en trois temps</h2>
<ol>
<li><strong>L'accumulation.</strong> Les vapeurs grasses aspirées par la hotte refroidissent dans le conduit et se déposent sur les parois. Service après service, la couche s'épaissit et durcit.</li>
<li><strong>L'allumage.</strong> Une flambée, un feu de friteuse, une étincelle de grill ou une simple montée en température suffisent à enflammer ce dépôt, surtout s'il se trouve près de la hotte.</li>
<li><strong>La propagation.</strong> Le tirage de l'extracteur alimente le feu en oxygène et l'entraîne vers le haut. Le conduit peut atteindre des températures très élevées et communiquer le feu aux matériaux voisins : faux plafonds, charpente, locaux traversés.</li>
</ol>
<h2>Les mesures qui font vraiment la différence</h2>
<ul class="check">
<li>Faire dégraisser l'ensemble du circuit à une fréquence adaptée à votre activité, au minimum une fois par an.</li>
<li>Utiliser des filtres à chicanes et les nettoyer très régulièrement.</li>
<li>Ne jamais faire fonctionner la cuisson sans les filtres en place.</li>
<li>Éviter les flambées directement sous des filtres saturés.</li>
<li>Faire poser des trappes de visite pour que tout le conduit soit accessible.</li>
<li>Disposer d'un extincteur adapté aux feux d'huiles (classe F) et former l'équipe à son usage.</li>
<li>Faire vérifier votre système d'extinction automatique s'il en existe un.</li>
</ul>
<h2>Les signaux d'alerte</h2>
<p>Graisse qui goutte des filtres, odeur de graisse chaude persistante, dépôt visible dans le plénum, extraction moins efficace : ce sont des signes qu'un dégraissage s'impose. Consultez notre liste des <a href="signes-hotte-a-nettoyer.html">signes qu'une hotte doit être nettoyée</a>.</p>
<div class="callout callout-warn"><svg class="ico"><use href="#i-alert"/></svg><p>En cas de feu de hotte : coupez les feux et l'extraction si vous pouvez le faire sans danger, utilisez l'extincteur adapté, n'utilisez jamais d'eau sur un feu d'huile, évacuez et appelez le 18 ou le 112.</p></div>`
  },
  {
    slug: "certificat-nettoyage-hotte-assurance",
    cat: "reg",
    title: "Certificat de nettoyage de hotte : pourquoi votre assureur le réclame",
    desc: "Que doit contenir un certificat de dégraissage, combien de temps le garder et quel est son rôle en cas de sinistre dans votre restaurant.",
    services: ["certificat-degraissage-hotte"],
    body: `
<p>Vous l'avez peut-être découvert en renouvelant votre contrat ou lors d'une visite de la commission de sécurité : le certificat de nettoyage de hotte est devenu une pièce incontournable du dossier d'un restaurant.</p>
<h2>Ce que votre contrat peut prévoir</h2>
<p>De nombreux contrats multirisques professionnels prévoient une obligation d'entretien des installations d'extraction, parfois avec une fréquence précise. En cas de sinistre, l'expert vérifie que ces obligations ont été respectées. À défaut de justificatif, l'assureur peut, selon les clauses du contrat, appliquer une réduction d'indemnité ou une déchéance de garantie. Relisez vos conditions particulières et générales : c'est souvent là que la fréquence est écrite.</p>
<h2>Un bon certificat contient au minimum</h2>
<ul class="check">
<li>L'identification de l'établissement et de l'entreprise intervenante.</li>
<li>La date de l'intervention et le nom du technicien.</li>
<li>La liste des éléments nettoyés : hotte, filtres, plénum, conduit, extracteur.</li>
<li>La longueur de conduit traitée et les zones inaccessibles.</li>
<li>Les observations : trappes manquantes, courroie usée, anomalies.</li>
<li>Des photos avant / après, idéalement à l'intérieur du conduit.</li>
<li>Une signature et, si possible, une recommandation pour le prochain passage.</li>
</ul>
<h2>Méfiez-vous des certificats trop parfaits</h2>
<p>Un certificat qui atteste « nettoyage complet » d'un conduit de 15 mètres sans aucune trappe de visite ne tiendra pas face à un expert. Il vaut mieux un certificat honnête, avec réserves, qu'un document de complaisance.</p>
<h2>Combien de temps le conserver ?</h2>
<p>Conservez l'historique complet dans votre registre de sécurité. Un minimum de cinq ans est une bonne pratique, et gardez toujours au moins les derniers certificats consultables sur place. Voir un <a href="../certificat-de-degraissage.html">exemple de certificat Clairvent</a>.</p>`
  },
  {
    slug: "registre-securite-cuisine-erp",
    cat: "reg",
    title: "Le registre de sécurité d'une cuisine d'ERP : mode d'emploi",
    desc: "Qu'est-ce que le registre de sécurité, que doit-il contenir pour la cuisine et l'extraction, et comment le tenir à jour sans effort.",
    services: ["certificat-degraissage-hotte", "contrat-entretien-hotte"],
    body: `
<p>Tout ERP doit tenir un registre de sécurité. C'est le carnet de santé de votre établissement face au risque incendie, et la commission de sécurité le consulte à chaque visite.</p>
<h2>Ce qu'on y trouve</h2>
<ul>
<li>Les renseignements indispensables à la bonne marche du service de sécurité.</li>
<li>Les dates des vérifications techniques et des contrôles (électricité, gaz, extincteurs, désenfumage…).</li>
<li>Les dates et la nature des travaux d'aménagement et de transformation.</li>
<li>Les formations et exercices réalisés par le personnel.</li>
<li>Pour la cuisine : les certificats de nettoyage de l'extraction et les vérifications des appareils de cuisson.</li>
</ul>
<h2>Nos conseils pour un registre toujours prêt</h2>
<ol>
<li>Rangez les documents par thème et par ordre chronologique.</li>
<li>Glissez chaque certificat de dégraissage dès sa réception, avec ses photos.</li>
<li>Notez sur une page de synthèse les dates des prochaines échéances.</li>
<li>Gardez une copie numérique : nos certificats sont envoyés en PDF.</li>
</ol>
<p>Avec un <a href="../prestations/contrat-entretien-hotte.html">contrat d'entretien</a>, nous vous envoyons l'historique complet de vos interventions à chaque passage.</p>`
  },
  {
    slug: "commission-securite-cuisine-preparer",
    cat: "reg",
    title: "Préparer la visite de la commission de sécurité côté cuisine",
    desc: "Extraction, certificats, appareils de cuisson, extincteurs : la check-list pour aborder sereinement la visite de la commission de sécurité.",
    services: ["diagnostic-inspection-extraction", "nettoyage-avant-ouverture-controle"],
    body: `
<p>La commission de sécurité visite périodiquement les ERP, selon leur type et leur catégorie. La cuisine fait partie des zones à risque qu'elle observe avec attention. Voici comment vous y préparer.</p>
<h2>Check-list cuisine et extraction</h2>
<ul class="check">
<li>Le dernier certificat de dégraissage de l'extraction date de moins d'un an (ou selon votre fréquence).</li>
<li>Le certificat couvre l'ensemble du circuit : hotte, filtres, conduit, extracteur.</li>
<li>Les filtres sont en place, propres et non déformés.</li>
<li>Aucune graisse ne coule de la hotte ou des gouttières.</li>
<li>Les dispositifs de coupure (gaz, électricité, extraction) sont accessibles et signalés.</li>
<li>Les extincteurs sont présents, adaptés et vérifiés.</li>
<li>Les vérifications gaz et électricité sont à jour et consignées.</li>
<li>Le registre de sécurité est complet et disponible.</li>
</ul>
<h2>Anticiper plutôt que subir</h2>
<p>Programmez le dégraissage de votre extraction quelques semaines avant la visite prévue : vous aurez un certificat récent et une hotte impeccable. Si vous doutez de l'état de votre installation, un <a href="../prestations/diagnostic-inspection-extraction.html">diagnostic</a> permet de faire le point.</p>`
  },
  {
    slug: "que-faire-apres-feu-de-hotte",
    cat: "feu",
    title: "Que faire après un feu de hotte dans votre cuisine ?",
    desc: "Mise en sécurité, déclaration à l'assurance, contrôle du conduit, nettoyage des suies : les étapes à suivre après un départ de feu sous la hotte.",
    services: ["nettoyage-cuisine-apres-sinistre", "degraissage-conduit-extraction"],
    body: `
<p>Même maîtrisé en quelques secondes, un feu sous la hotte ne doit jamais être pris à la légère. Voici les étapes à suivre, dans l'ordre.</p>
<h2>1. Mettre en sécurité</h2>
<p>Assurez-vous que le feu est totalement éteint, y compris dans le conduit. En cas de doute (chaleur anormale sur la gaine, fumée qui persiste, odeur de brûlé en toiture), appelez les pompiers : un feu de conduit peut couver. Coupez le gaz et l'alimentation des appareils concernés.</p>
<h2>2. Ne pas remettre l'extraction en route</h2>
<p>Un conduit qui a pris feu peut contenir des dépôts fragilisés ou des braises. Une remise en service peut relancer la combustion. Faites d'abord inspecter l'installation.</p>
<h2>3. Documenter</h2>
<p>Prenez des photos de la hotte, des filtres, des surfaces noircies et de tout dommage visible. Notez l'heure et les circonstances. Ces éléments seront utiles pour votre déclaration.</p>
<h2>4. Prévenir votre assureur</h2>
<p>Déclarez le sinistre dans les délais prévus par votre contrat. L'assureur peut mandater un expert : ne faites pas nettoyer avant son passage sans son accord, sauf urgence sanitaire.</p>
<h2>5. Faire nettoyer et contrôler</h2>
<p>Le nettoyage après feu comprend le retrait des suies, le dégraissage complet du circuit et une vérification de l'état des éléments (filtres déformés, joints, extracteur). Selon les dégâts, l'intervention d'un installateur peut être nécessaire avant la remise en service.</p>
<h2>6. Comprendre la cause</h2>
<p>Dans la plupart des cas, un feu de hotte s'explique par des filtres saturés, un plénum gras ou une flambée mal maîtrisée. C'est le moment de revoir votre fréquence de dégraissage et vos routines d'entretien.</p>`
  },
  {
    slug: "feu-de-friteuse-bons-reflexes",
    cat: "feu",
    title: "Feu de friteuse : les bons réflexes à enseigner à votre équipe",
    desc: "Pourquoi il ne faut jamais d'eau, quel extincteur utiliser, comment prévenir : le guide pour former votre brigade au risque de feu d'huile.",
    services: ["nettoyage-equipements-cuisson", "nettoyage-hotte-professionnelle"],
    body: `
<p>Le feu de friteuse est un classique des cuisines professionnelles. Il se transmet très vite à une hotte encrassée. Former votre équipe aux bons gestes prend dix minutes et peut sauver votre établissement.</p>
<h2>La règle d'or : jamais d'eau</h2>
<p>Jetée sur de l'huile en feu, l'eau se vaporise instantanément et projette l'huile enflammée en une boule de feu. C'est l'erreur la plus dangereuse, et la plus instinctive.</p>
<h2>Les bons gestes</h2>
<ol>
<li>Couper l'alimentation de la friteuse (gaz ou électricité) si c'est possible sans danger.</li>
<li>Étouffer le feu : couvercle métallique, couverture anti-feu.</li>
<li>Utiliser un extincteur adapté aux feux d'huiles et graisses de cuisson (classe F).</li>
<li>Ne pas déplacer la friteuse.</li>
<li>Évacuer et appeler le 18 ou le 112 si le feu n'est pas maîtrisé immédiatement.</li>
</ol>
<h2>La prévention</h2>
<ul class="check">
<li>Respecter la température de consigne et le niveau d'huile.</li>
<li>Changer l'huile régulièrement : une huile dégradée s'enflamme plus facilement.</li>
<li>Garder l'habillage et les abords de la friteuse propres.</li>
<li>Maintenir des filtres de hotte propres au-dessus du poste de friture.</li>
<li>Faire dégraisser l'extraction à la bonne fréquence.</li>
</ul>`
  },
  {
    slug: "extincteur-cuisine-professionnelle-classe-f",
    cat: "feu",
    title: "Quel extincteur pour une cuisine professionnelle ? Le point sur la classe F",
    desc: "Classes de feu, extincteur pour feux d'huiles, couverture anti-feu, emplacement : bien équiper sa cuisine professionnelle contre l'incendie.",
    services: ["nettoyage-hotte-professionnelle"],
    body: `
<p>Tous les extincteurs ne se valent pas face à un feu de cuisine. Les huiles et graisses de cuisson brûlent à très haute température et nécessitent un agent spécifique.</p>
<h2>Les classes de feu en bref</h2>
<table>
<thead><tr><th>Classe</th><th>Type de feu</th></tr></thead>
<tbody>
<tr><td>A</td><td>Solides (bois, papier, tissus)</td></tr>
<tr><td>B</td><td>Liquides et solides liquéfiables</td></tr>
<tr><td>C</td><td>Gaz</td></tr>
<tr><td>D</td><td>Métaux</td></tr>
<tr><td>F</td><td>Huiles et graisses de cuisson</td></tr>
</tbody>
</table>
<h2>L'extincteur adapté</h2>
<p>Pour les postes de friture et de cuisson grasse, on recommande un extincteur homologué pour les feux de classe F, souvent à base d'agent saponifiant : il forme une couche qui refroidit l'huile et l'isole de l'oxygène. Un extincteur à CO₂ reste utile pour les feux d'origine électrique. Votre vérificateur ou votre préventionniste vous indiquera l'équipement exact adapté à votre cuisine.</p>
<h2>Où les placer ?</h2>
<p>Près des sorties de la cuisine et à portée des postes de cuisson, jamais derrière la source du feu. Signalisation visible, vérification annuelle par un organisme compétent, et formation du personnel à la manipulation.</p>
<p>Le meilleur extincteur reste un circuit d'extraction propre : sans graisse accumulée, un départ de feu ne trouve pas de combustible pour se propager.</p>`
  },
  {
    slug: "hygiene-hotte-controle-sanitaire",
    cat: "hyg",
    title: "Hygiène de la hotte et contrôle sanitaire : ce que regardent les inspecteurs",
    desc: "Graisse qui goutte, plafonds encrassés, plan de nettoyage : comment la hotte pèse dans un contrôle sanitaire et comment être irréprochable.",
    services: ["nettoyage-avant-ouverture-controle", "nettoyage-plenum-hotte"],
    body: `
<p>On associe souvent la hotte au risque incendie. Mais c'est aussi un point d'hygiène majeur, que les agents de la DDPP (services vétérinaires) observent lors de leurs inspections.</p>
<h2>Pourquoi la hotte est un sujet d'hygiène</h2>
<p>Placée au-dessus des postes de cuisson, la hotte peut laisser goutter de la graisse oxydée ou des condensats sur les préparations. Une hotte grasse attire les nuisibles et dégage des odeurs rances. Le « paquet hygiène » (règlement CE n° 852/2004) impose que les locaux et équipements en contact direct ou indirect avec les denrées soient propres et bien entretenus.</p>
<h2>Les points observés</h2>
<ul class="check">
<li>Propreté extérieure de la hotte et des filtres.</li>
<li>Absence de coulures ou de gouttes au-dessus des plans de travail.</li>
<li>État des plafonds, des luminaires et des grilles de ventilation.</li>
<li>Existence d'un plan de nettoyage et de désinfection, et preuves de son application.</li>
<li>État général des équipements de cuisson et des sols.</li>
</ul>
<h2>Intégrer la hotte à votre plan de nettoyage</h2>
<p>Votre plan de nettoyage doit préciser qui nettoie quoi, quand et avec quel produit. Pour la hotte : essuyage quotidien de la façade, nettoyage hebdomadaire des filtres par l'équipe, et dégraissage complet par un prestataire à la fréquence adaptée. Voir notre guide <a href="plan-nettoyage-desinfection-cuisine.html">construire son plan de nettoyage et de désinfection</a>.</p>`
  },
  {
    slug: "plan-nettoyage-desinfection-cuisine",
    cat: "hyg",
    title: "Construire le plan de nettoyage et de désinfection de sa cuisine",
    desc: "Méthode simple pour rédiger un plan de nettoyage et de désinfection conforme à l'esprit HACCP, avec un modèle pour la hotte et l'extraction.",
    services: ["nettoyage-cuisine-professionnelle", "nettoyage-chambre-froide"],
    body: `
<p>Le plan de nettoyage et de désinfection (PND) fait partie des bonnes pratiques d'hygiène qui composent votre plan de maîtrise sanitaire. Il répond à cinq questions : quoi, qui, quand, comment, avec quoi.</p>
<h2>Les cinq colonnes d'un bon plan</h2>
<table>
<thead><tr><th>Quoi</th><th>Qui</th><th>Quand</th><th>Comment</th><th>Produit</th></tr></thead>
<tbody>
<tr><td>Façade de la hotte</td><td>Commis de fermeture</td><td>Chaque soir</td><td>Essuyage dégraissant, rinçage</td><td>Dégraissant alimentaire</td></tr>
<tr><td>Filtres de hotte</td><td>Plonge</td><td>Chaque semaine</td><td>Trempage, brossage, rinçage</td><td>Dégraissant filtres</td></tr>
<tr><td>Plénum, conduit, extracteur</td><td>Prestataire</td><td>Selon fréquence définie</td><td>Dégraissage complet</td><td>Selon prestataire</td></tr>
<tr><td>Plans de travail</td><td>Chaque poste</td><td>Après chaque usage</td><td>Nettoyage puis désinfection</td><td>Détergent-désinfectant</td></tr>
<tr><td>Chambres froides</td><td>Chef de partie</td><td>Chaque mois</td><td>Vidage, nettoyage, désinfection</td><td>Détergent-désinfectant</td></tr>
</tbody>
</table>
<h2>Nettoyer puis désinfecter</h2>
<p>La désinfection n'est efficace que sur une surface propre. On dégraisse et on nettoie d'abord, on rince, puis on désinfecte en respectant le temps de contact indiqué sur le produit, et on rince à nouveau si la notice l'exige pour les surfaces en contact alimentaire.</p>
<h2>Tracer ce qui est fait</h2>
<p>Une feuille d'émargement par zone, cochée à chaque nettoyage, suffit à prouver que le plan est appliqué. Les certificats de vos prestataires complètent ces preuves pour les opérations techniques.</p>`
  },
  {
    slug: "odeurs-cuisine-restaurant-voisinage",
    cat: "hyg",
    title: "Odeurs de cuisine et plaintes du voisinage : le rôle de l'extraction",
    desc: "Pourquoi une extraction encrassée aggrave les odeurs, ce que peut exiger le voisinage et comment réduire les nuisances olfactives de votre restaurant.",
    services: ["nettoyage-tourelle-caisson-extraction", "degraissage-conduit-extraction"],
    body: `
<p>Les odeurs de cuisine sont une source fréquente de conflits entre restaurants et riverains, notamment en copropriété. Une extraction mal entretenue en est souvent la première cause.</p>
<h2>Pourquoi une extraction sale sent plus fort</h2>
<p>La graisse accumulée dans le conduit et sur la turbine s'oxyde et rancit. Elle dégage des odeurs même en dehors des heures de cuisson. De plus, une turbine encrassée aspire moins : les fumées stagnent, s'échappent par les ouvrants et se diffusent dans la cour ou chez les voisins.</p>
<h2>Les leviers d'action</h2>
<ol>
<li><strong>Nettoyer l'ensemble du circuit</strong>, y compris l'extracteur, pour retrouver le débit d'origine et supprimer les dépôts odorants.</li>
<li><strong>Vérifier le rejet</strong> : sa hauteur et son orientation par rapport aux fenêtres voisines, conformément au règlement sanitaire départemental et au règlement de copropriété.</li>
<li><strong>Étudier un traitement des odeurs</strong> (filtration, dispositifs spécifiques) avec un ventiliste si le problème persiste.</li>
</ol>
<h2>Dialoguer avec le voisinage</h2>
<p>Présenter un certificat de nettoyage récent au syndic ou aux voisins est souvent un premier pas apaisant : il montre que vous prenez le sujet au sérieux.</p>`
  },
  {
    slug: "responsabilite-locataire-proprietaire-hotte",
    cat: "ges",
    title: "Bail commercial : qui doit payer le nettoyage de la hotte ?",
    desc: "Locataire ou propriétaire : comment se répartissent l'entretien, le dégraissage et le remplacement de l'extraction dans un bail commercial.",
    services: ["contrat-entretien-hotte", "certificat-degraissage-hotte"],
    body: `
<p>Question classique à la signature d'un bail ou à la reprise d'un fonds : qui prend en charge l'entretien de l'extraction de cuisine ?</p>
<h2>Le principe : l'entretien courant revient à l'exploitant</h2>
<p>Dans la plupart des baux commerciaux, l'entretien courant et le nettoyage des équipements liés à l'activité (dont la hotte et son conduit) sont à la charge du locataire exploitant. C'est lui qui utilise l'installation et qui l'encrasse.</p>
<h2>Les grosses réparations : cela dépend</h2>
<p>Le remplacement d'un extracteur, la réfection d'un conduit ou la mise en conformité peuvent relever du bailleur ou du locataire selon les clauses du bail et la nature des travaux. Depuis la loi Pinel, certaines charges ne peuvent plus être imputées au locataire. Faites relire votre bail par un professionnel en cas de doute.</p>
<h2>Ce que nous conseillons</h2>
<ul class="check">
<li>Vérifier la clause « entretien des installations techniques » avant de signer.</li>
<li>Faire constater l'état de l'extraction à l'entrée dans les lieux (un <a href="../prestations/diagnostic-inspection-extraction.html">diagnostic</a> est idéal).</li>
<li>Conserver tous les certificats de nettoyage pendant la durée du bail.</li>
<li>Faire dégraisser l'extraction avant de rendre les lieux.</li>
</ul>`
  },
  {
    slug: "norme-nf-en-16282-ventilation-cuisine",
    cat: "reg",
    title: "Norme NF EN 16282 : ce qu'il faut savoir sur la ventilation des cuisines",
    desc: "La norme européenne sur les équipements de ventilation des cuisines professionnelles expliquée simplement : périmètre, apports, liens avec l'entretien.",
    services: ["diagnostic-inspection-extraction", "nettoyage-hotte-professionnelle"],
    body: `
<p>La série de normes NF EN 16282 porte sur les équipements pour cuisines commerciales et plus particulièrement sur les éléments de ventilation : hottes, plafonds filtrants, dispositifs de séparation des aérosols, conduits, etc.</p>
<h2>Ce que couvre la norme</h2>
<p>Découpée en plusieurs parties, elle traite des principes généraux, des exigences de conception et de performance des hottes, des filtres et séparateurs d'aérosols, des éléments d'entrée et de sortie d'air, et de l'installation. Elle aborde aussi l'accessibilité pour le nettoyage et l'entretien.</p>
<h2>Une norme, pas une loi</h2>
<p>Une norme est d'application volontaire, sauf lorsqu'un texte réglementaire la rend obligatoire. Elle constitue néanmoins une référence de l'état de l'art : un installateur, un bureau de contrôle ou un expert peuvent s'y référer pour juger de la qualité d'une installation.</p>
<h2>Ce qui compte pour l'entretien</h2>
<ul>
<li>Des filtres qui séparent efficacement les aérosols gras et qui se démontent facilement.</li>
<li>Des conduits accessibles, avec des ouvertures d'inspection et de nettoyage.</li>
<li>Des pentes et des points de récupération des graisses.</li>
</ul>
<p>Une installation pensée pour être nettoyée se nettoie mieux, plus vite et moins cher. C'est un point à aborder avec votre installateur lors de tout projet de rénovation.</p>`
  },
  {
    slug: "dark-kitchen-extraction-obligations",
    cat: "reg",
    title: "Dark kitchen et laboratoire : quelles obligations pour l'extraction ?",
    desc: "Cuisines de livraison, laboratoires, cuisines partagées : les règles d'entretien de l'extraction quand la cuisine ne reçoit pas de public.",
    services: ["nettoyage-hotte-professionnelle", "contrat-entretien-hotte"],
    body: `
<p>Une dark kitchen ne reçoit pas de clients. Est-elle pour autant dispensée d'entretenir son extraction ? Non, et voici pourquoi.</p>
<h2>Pas d'ERP, mais un lieu de travail</h2>
<p>Si le local n'accueille pas de public, il ne relève pas forcément du règlement de sécurité des ERP. En revanche, il reste un lieu de travail soumis au Code du travail, qui impose le maintien en bon état des installations d'aération et la prévention du risque incendie pour les salariés.</p>
<h2>Les assureurs et les bailleurs</h2>
<p>Votre assureur et votre bailleur ont souvent les mêmes exigences qu'en restauration classique : dégraissage régulier et justificatifs. Dans les cuisines partagées, le gestionnaire du site impose généralement un calendrier commun.</p>
<h2>Une activité souvent très intensive</h2>
<p>Les dark kitchens tournent parfois douze heures par jour, avec plusieurs marques et beaucoup de friture. Le rythme de dégraissage doit en tenir compte : tous les trois à quatre mois est courant. Découvrez notre offre dédiée aux <a href="../secteurs/dark-kitchens.html">dark kitchens</a>.</p>`
  },
  {
    slug: "hotte-restaurant-copropriete",
    cat: "reg",
    title: "Restaurant en copropriété : l'extraction sous surveillance",
    desc: "Conduit dans les parties communes, règlement de copropriété, syndic : ce que doit savoir un restaurateur installé en immeuble d'habitation.",
    services: ["degraissage-conduit-extraction", "certificat-degraissage-hotte"],
    body: `
<p>À Paris et en petite couronne, une grande partie des restaurants sont installés en pied d'immeuble. Leur conduit d'extraction traverse souvent les étages jusqu'au toit.</p>
<h2>Un risque partagé</h2>
<p>Un feu de conduit dans un immeuble d'habitation met en danger les occupants. C'est pourquoi le syndic et les copropriétaires sont particulièrement attentifs à l'entretien de l'extraction. Le règlement de copropriété peut prévoir des obligations spécifiques et le syndic peut demander la communication des certificats.</p>
<h2>Les bonnes pratiques</h2>
<ul class="check">
<li>Communiquer spontanément vos certificats de dégraissage au syndic.</li>
<li>Prévenir le gardien ou le syndic avant une intervention en toiture.</li>
<li>Faire poser des trappes de visite accessibles depuis vos locaux lorsque c'est possible.</li>
<li>Traiter rapidement toute plainte d'odeur ou de bruit.</li>
</ul>
<p>Nos techniciens ont l'habitude d'intervenir en immeuble parisien : accès par les parties communes, protection des cages d'escalier, intervention en toiture coordonnée avec le syndic.</p>`
  },
  {
    slug: "epaisseur-graisse-conduit-seuil",
    cat: "feu",
    title: "Quelle épaisseur de graisse dans un conduit devient dangereuse ?",
    desc: "Comment mesurer le dépôt de graisse dans un conduit d'extraction, quels seuils sont utilisés par les professionnels et que faire selon le résultat.",
    services: ["diagnostic-inspection-extraction", "degraissage-conduit-extraction"],
    body: `
<p>Tant qu'on n'ouvre pas le conduit, on ne sait pas. C'est pourquoi l'inspection régulière est aussi importante que le nettoyage lui-même.</p>
<h2>Comment mesure-t-on ?</h2>
<p>Les professionnels utilisent une jauge à peigne, que l'on applique sur la paroi pour lire directement l'épaisseur du dépôt, ou réalisent un relevé visuel et photographique à chaque trappe de visite.</p>
<h2>Les repères utilisés</h2>
<p>Plusieurs référentiels internationaux considèrent qu'un dépôt de l'ordre de quelques dixièmes de millimètre à un millimètre justifie une intervention de nettoyage, et qu'au-delà de deux millimètres le nettoyage devient urgent. Ces repères ne sont pas des seuils réglementaires français, mais ils donnent une bonne idée du niveau à partir duquel la graisse devient un combustible significatif.</p>
<table>
<thead><tr><th>Dépôt constaté</th><th>Lecture</th></tr></thead>
<tbody>
<tr><td>Film léger, paroi visible</td><td>Situation maîtrisée, fréquence adaptée</td></tr>
<tr><td>Dépôt uniforme, paroi masquée</td><td>Nettoyage à programmer</td></tr>
<tr><td>Dépôt épais, collant ou croûteux</td><td>Nettoyage urgent, fréquence à revoir</td></tr>
</tbody>
</table>
<p>Nos certificats indiquent l'état constaté à l'ouverture : c'est ce qui permet d'ajuster intelligemment votre fréquence d'intervention.</p>`
  },
  {
    slug: "trappes-de-visite-conduit-extraction",
    cat: "equ",
    title: "Trappes de visite : pourquoi votre conduit en a besoin",
    desc: "Rôle des trappes de visite sur un conduit d'extraction de cuisine, où les placer et comment elles conditionnent la qualité du nettoyage.",
    services: ["degraissage-conduit-extraction", "diagnostic-inspection-extraction"],
    body: `
<p>Une trappe de visite est une ouverture étanche aménagée sur le conduit, qui permet d'y accéder pour l'inspecter et le nettoyer. Sans elle, une partie du conduit reste hors d'atteinte.</p>
<h2>Où les placer ?</h2>
<ul>
<li>À proximité de chaque changement de direction (coudes).</li>
<li>Régulièrement sur les tronçons horizontaux longs.</li>
<li>En pied et en tête des tronçons verticaux.</li>
<li>Près des registres, clapets et équipements intermédiaires.</li>
</ul>
<p>L'emplacement exact dépend du tracé, des outils de nettoyage et des contraintes du bâtiment. C'est à votre installateur ou ventiliste de les poser, en respectant les exigences d'étanchéité et de résistance au feu du conduit.</p>
<h2>Sans trappes, que peut-on faire ?</h2>
<p>Nous nettoyons tout ce qui est atteignable depuis la hotte et l'extracteur, avec des brosses rotatives sur flexibles. Au-delà, nous le mentionnons sur le certificat. Un certificat qui signale les zones non accessibles vous protège : il prouve votre bonne foi et oriente les travaux à prévoir.</p>`
  },
  {
    slug: "anatomie-systeme-extraction-cuisine",
    cat: "equ",
    title: "Hotte, plénum, conduit, tourelle : comprendre votre système d'extraction",
    desc: "Le parcours de l'air gras depuis la cuisson jusqu'à la toiture, élément par élément, et ce que chacun demande comme entretien.",
    services: ["nettoyage-hotte-professionnelle", "nettoyage-plenum-hotte"],
    body: `
<p>Pour bien entretenir une installation, il faut la comprendre. Suivons le chemin d'une bouffée de vapeur grasse depuis la sauteuse jusqu'au ciel. Vous pouvez aussi explorer notre <a href="../methode.html">schéma interactif</a>.</p>
<h2>1. La hotte</h2>
<p>Le caisson inox au-dessus des postes de cuisson capte les fumées. Elle comporte souvent une gouttière périphérique et des robinets de vidange qui récupèrent la graisse condensée.</p>
<h2>2. Les filtres</h2>
<p>Placés en biais dans la hotte, les filtres à chicanes forcent l'air à changer de direction. Les gouttelettes de graisse s'y condensent et ruissellent vers la gouttière. C'est la première et la plus importante barrière.</p>
<h2>3. Le plénum</h2>
<p>C'est la chambre située derrière les filtres, qui collecte l'air filtré avant son départ dans le conduit. Invisible en service, elle est souvent très grasse.</p>
<h2>4. Le conduit (ou gaine)</h2>
<p>Il transporte l'air jusqu'à l'extérieur, parfois sur plusieurs dizaines de mètres, avec des tronçons horizontaux, verticaux et des coudes. La graisse s'y dépose en refroidissant. C'est la zone la plus à risque en cas de feu.</p>
<h2>5. L'extracteur</h2>
<p>Tourelle en toiture ou caisson de ventilation, c'est lui qui crée l'aspiration. Sa turbine s'encrasse et se déséquilibre avec le temps.</p>
<h2>6. Le rejet et la compensation</h2>
<p>L'air est rejeté à l'extérieur, et un apport d'air neuf (compensation) doit remplacer l'air extrait pour que la hotte fonctionne correctement.</p>`
  },
  {
    slug: "filtres-chicanes-ou-mailles",
    cat: "equ",
    title: "Filtres à chicanes ou filtres à mailles : lequel choisir ?",
    desc: "Comparatif des deux grandes familles de filtres de hotte : efficacité, sécurité incendie, entretien et coût sur la durée.",
    services: ["nettoyage-filtres-hotte"],
    body: `
<p>Le choix des filtres a un impact direct sur la quantité de graisse qui entre dans votre conduit et sur la fréquence de nettoyage nécessaire.</p>
<h2>Le comparatif</h2>
<table>
<thead><tr><th></th><th>Filtres à chicanes</th><th>Filtres à mailles</th></tr></thead>
<tbody>
<tr><td>Principe</td><td>Condensation par changements de direction</td><td>Rétention dans un grillage</td></tr>
<tr><td>Matériau courant</td><td>Inox</td><td>Aluminium ou inox</td></tr>
<tr><td>Comportement face à la flamme</td><td>Bonne barrière</td><td>Le grillage gras peut s'enflammer</td></tr>
<tr><td>Encrassement</td><td>Progressif, la graisse s'écoule</td><td>Rapide, colmatage</td></tr>
<tr><td>Nettoyage</td><td>Facile, trempage ou machine</td><td>Difficile à cœur</td></tr>
<tr><td>Usage recommandé</td><td>Cuisine professionnelle</td><td>Usage domestique</td></tr>
</tbody>
</table>
<h2>Notre avis</h2>
<p>En cuisine professionnelle, les filtres à chicanes en inox sont la référence. Si votre hotte est encore équipée de filtres à mailles, parlez-en à votre installateur : le remplacement est souvent simple et rapidement rentabilisé par la réduction de l'encrassement du conduit.</p>`
  },
  {
    slug: "nettoyer-filtres-hotte-professionnelle",
    cat: "ent",
    title: "Comment nettoyer les filtres de hotte professionnelle entre deux passages",
    desc: "La routine hebdomadaire de nettoyage des filtres à chicanes : matériel, produit, trempage, rinçage et erreurs à éviter.",
    services: ["nettoyage-filtres-hotte"],
    body: `
<p>Entre deux dégraissages professionnels, le nettoyage régulier des filtres par votre équipe est la meilleure protection de votre conduit. Voici la méthode.</p>
<h2>Le matériel</h2>
<ul>
<li>Un bac de trempage assez grand pour immerger un filtre à plat.</li>
<li>Un dégraissant alcalin adapté (vérifiez la compatibilité avec l'aluminium si vos filtres en contiennent).</li>
<li>De l'eau chaude, une brosse à poils durs non métallique, des gants et des lunettes.</li>
</ul>
<h2>La méthode en 6 étapes</h2>
<ol>
<li>Arrêter la cuisson et laisser refroidir la hotte.</li>
<li>Déposer les filtres en les tenant bien droits pour ne pas renverser la graisse.</li>
<li>Les immerger dans l'eau chaude additionnée de dégraissant, selon le dosage du fabricant.</li>
<li>Laisser agir le temps indiqué, puis brosser dans le sens des chicanes.</li>
<li>Rincer abondamment à l'eau chaude.</li>
<li>Laisser égoutter et sécher avant de remonter, bords ouverts vers le bas.</li>
</ol>
<h2>Les erreurs à éviter</h2>
<ul class="check cross">
<li>Cuisiner sans filtres pendant qu'ils sèchent.</li>
<li>Utiliser une paille de fer qui raye l'inox et favorise l'accroche de la graisse.</li>
<li>Remonter un filtre déformé qui laisse passer l'air gras sur les côtés.</li>
<li>Oublier la gouttière et les glissières.</li>
</ul>
<p>Astuce : un deuxième jeu de filtres permet de nettoyer sans jamais laisser la hotte nue.</p>`
  },
  {
    slug: "entretien-quotidien-hotte-restaurant",
    cat: "ent",
    title: "Entretien quotidien de la hotte : la routine en 10 minutes",
    desc: "Les gestes simples à intégrer à la fermeture de votre cuisine pour garder une hotte propre et espacer les gros dégraissages.",
    services: ["nettoyage-filtres-hotte", "contrat-entretien-hotte"],
    body: `
<p>Dix minutes à la fermeture suffisent à garder une hotte saine entre deux interventions professionnelles.</p>
<h2>Chaque jour</h2>
<ul class="check">
<li>Essuyer la façade et les bords de la hotte avec un dégraissant adapté.</li>
<li>Vider et nettoyer la gouttière ou les godets de récupération.</li>
<li>Vérifier que tous les filtres sont en place et bien emboîtés.</li>
<li>Nettoyer les luminaires sous hotte s'ils sont gras.</li>
</ul>
<h2>Chaque semaine</h2>
<ul class="check">
<li>Nettoyer les filtres par trempage (plus souvent en friture intensive).</li>
<li>Nettoyer les glissières des filtres.</li>
<li>Contrôler visuellement l'intérieur de la hotte derrière les filtres.</li>
</ul>
<h2>Chaque mois</h2>
<ul class="check">
<li>Noter l'état du plénum et la présence éventuelle de coulures.</li>
<li>Écouter l'extracteur : bruit inhabituel, vibration ?</li>
<li>Vérifier la date du prochain dégraissage professionnel.</li>
</ul>
<p>Une hotte bien entretenue au quotidien se dégraisse plus vite et plus complètement lors de nos passages.</p>`
  },
  {
    slug: "tourelle-extraction-entretien",
    cat: "equ",
    title: "Tourelle d'extraction : entretien, pannes fréquentes et durée de vie",
    desc: "Comment fonctionne une tourelle d'extraction de cuisine, pourquoi elle s'encrasse, et comment prolonger sa durée de vie.",
    services: ["nettoyage-tourelle-caisson-extraction"],
    body: `
<p>Posée sur le toit, on l'oublie facilement. Pourtant la tourelle d'extraction est le moteur de toute votre ventilation.</p>
<h2>Pourquoi elle s'encrasse</h2>
<p>Même avec de bons filtres, une partie des aérosols gras atteint la turbine. La graisse se dépose sur les pales, les alourdit et les déséquilibre. Elle peut aussi s'écouler par les joints et tacher la toiture.</p>
<h2>Les pannes les plus courantes</h2>
<ul>
<li><strong>Courroie usée ou cassée</strong> sur les modèles à transmission.</li>
<li><strong>Roulements bruyants</strong>, souvent aggravés par le balourd d'une turbine grasse.</li>
<li><strong>Moteur qui chauffe</strong> parce qu'il force pour un débit insuffisant.</li>
<li><strong>Infiltrations</strong> d'eau de pluie par des capots mal refermés.</li>
</ul>
<h2>Prolonger sa durée de vie</h2>
<p>Un nettoyage régulier de la turbine, en même temps que le conduit, est la première mesure. Il doit être complété par la maintenance mécanique prévue par le fabricant (courroie, roulements, contrôle électrique), assurée par votre ventiliste. Nos techniciens vous signalent toute anomalie observée.</p>`
  },
  {
    slug: "signes-hotte-a-nettoyer",
    cat: "ent",
    title: "10 signes que votre hotte doit être nettoyée sans attendre",
    desc: "Graisse qui goutte, fumée qui stagne, bruit de l'extracteur : les indices qui montrent que votre extraction a besoin d'un dégraissage.",
    services: ["nettoyage-hotte-professionnelle", "diagnostic-inspection-extraction"],
    body: `
<p>Votre hotte vous parle. Voici les dix signaux qui doivent vous faire décrocher le téléphone.</p>
<ol>
<li><strong>De la graisse goutte des filtres</strong> ou coule le long des parois de la hotte.</li>
<li><strong>La fumée stagne</strong> dans la cuisine alors que l'extraction fonctionne.</li>
<li><strong>Les filtres sont collants</strong> quelques jours seulement après leur nettoyage.</li>
<li><strong>Une odeur de graisse rance</strong> persiste même cuisine fermée.</li>
<li><strong>L'extracteur est plus bruyant</strong> qu'avant ou vibre.</li>
<li><strong>La graisse coule en toiture</strong> autour de la tourelle.</li>
<li><strong>Le plénum est brun et brillant</strong> quand on retire les filtres.</li>
<li><strong>Il fait plus chaud en cuisine</strong> : l'air chaud n'est plus évacué correctement.</li>
<li><strong>Le dernier certificat date de plus d'un an</strong>, ou vous n'en trouvez pas.</li>
<li><strong>Vous avez eu une flambée</strong> qui a « léché » les filtres.</li>
</ol>
<p>Un seul de ces signes justifie une inspection. Plusieurs signes à la fois : un dégraissage s'impose rapidement. <a href="../reservation.html">Réservez une intervention</a> ou demandez une visite gratuite.</p>`
  }
];
