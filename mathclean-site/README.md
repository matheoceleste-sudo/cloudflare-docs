# Site MathClean

Site vitrine statique pour MathClean, entreprise de nettoyage à Paris.
Aucune dépendance, aucun build : trois fichiers HTML/CSS/JS qui se déploient
tels quels sur Cloudflare Pages, Netlify, Vercel ou un hébergement classique.

```
mathclean-site/
├── index.html            page principale
├── mentions-legales.html mentions légales / RGPD
└── assets/
    ├── styles.css        design system complet
    └── app.js            menu, formulaire 2 étapes, estimation live
```

## À remplacer avant la mise en ligne

Le site est livré avec des coordonnées **fictives**. Il faut impérativement
les remplacer par les vraies avant de publier.

| Élément | Valeur actuelle | Où |
|---|---|---|
| Téléphone | `01 23 45 67 89` et `tel:+33123456789` | `index.html`, `mentions-legales.html` |
| E-mail | `contact@mathclean.fr` | `index.html`, `mentions-legales.html`, `assets/app.js` |
| Domaine | `https://mathclean.fr/` | balises `canonical`, `og:*` et JSON-LD dans `index.html` |
| SIREN, adresse, forme juridique | `[…]` entre crochets | `mentions-legales.html` |
| Tarifs affichés | 29 € / 25 € / sur devis | section `#tarifs` de `index.html` |
| Avis clients | trois témoignages d'exemple | section `#avis` de `index.html` |
| Note et nombre d'avis | 4,9 / 127 | bloc JSON-LD en bas d'`index.html` |

Remplacer le numéro partout d'un coup :

```bash
cd mathclean-site
grep -rl "01 23 45 67 89" . | xargs sed -i 's/01 23 45 67 89/VOTRE NUMÉRO/g'
grep -rl "+33123456789"   . | xargs sed -i 's/+33123456789/+33VOTRENUMERO/g'
```

## Réception des demandes de devis

Tout se règle dans le bloc `CONFIG` en haut d'`assets/app.js`.

- **Par défaut** (`endpoint: null`) : le formulaire ouvre le client mail du
  visiteur avec la demande pré-remplie vers `CONFIG.email`. Ça fonctionne sans
  serveur, mais le visiteur doit valider l'envoi depuis sa messagerie.
- **Recommandé en production** : renseigner `endpoint` avec l'URL d'un service
  de formulaire (Formspree, Web3Forms) ou d'un Worker Cloudflare. Le formulaire
  poste alors le JSON en arrière-plan et affiche directement la confirmation.

Les tarifs horaires qui alimentent l'estimation affichée en direct sous le
formulaire se règlent dans le même bloc (`tarifHoraire`, `dureeParSurface`).
C'est une fourchette indicative : le texte sous l'estimation précise bien que
le prix ferme est confirmé après échange.

## Déploiement sur Cloudflare Pages

```bash
npx wrangler pages deploy mathclean-site --project-name mathclean
```

Ou depuis le tableau de bord : nouveau projet Pages connecté au dépôt, aucune
commande de build, répertoire de sortie `mathclean-site`.

## Aperçu en local

```bash
cd mathclean-site && python3 -m http.server 4173
# puis http://localhost:4173
```

## Choix de conception

Reprise de la structure du modèle demandé — bandeau vert forêt, titres serif,
fond crème, devis en deux étapes — avec quelques écarts assumés :

- **Ajouté** : estimation tarifaire calculée en direct dans le formulaire, FAQ
  dépliable, section avis clients, barre d'action fixe en bas sur mobile,
  bandeau de garanties, données structurées `LocalBusiness` pour le SEO local.
- **Retiré** : la question « quel matériel est prévu » du formulaire d'origine,
  remplacée par surface et fréquence, qui servent au calcul de l'estimation.
