# Mise en service de l'automatisation

Ce document décrit comment activer le système qui reçoit les réservations,
envoie les devis et relance les clients. Comptez une heure la première fois,
l'essentiel étant l'attente de la propagation DNS.

**Tant que l'étape 3 n'est pas faite, aucun courriel ne part.** Les demandes
sont bien enregistrées et visibles dans la console, mais le client ne reçoit
rien. La console affiche un bandeau rouge dans cet état. Faites les étapes
dans l'ordre.

---

## Ce que fait le système

Un client réserve sur le site. Selon la prestation :

**Prestations à prix fixe** — nettoyage automobile, nettoyage textile.
Le devis est calculé par le serveur, envoyé au client dans la minute, et
consultable sur une adresse privée où il peut l'accepter d'un bouton.

**Prestations sur devis** — hottes, entreprise, appartement, haute pression,
vitres, restaurant. Le client reçoit un accusé de réception qui annonce un
rappel sous 24 h. Vous recevez la demande, vous tapez les postes dans la
console, et le devis part automatiquement. Si vous ne l'avez pas chiffrée au
bout de deux jours, le système vous le rappelle.

Ensuite, sans rien faire :

| Quand | Ce qui part | À qui |
|---|---|---|
| Immédiatement | Devis ou accusé de réception | Client |
| Immédiatement | Notification de la demande | Vous |
| J+3 sans réponse | Première relance | Client |
| J+8 sans réponse | Deuxième relance | Client |
| J+15 sans réponse | Dernière relance | Client |
| J+22 | Dossier classé, en silence | — |
| À l'acceptation | Confirmation / alerte | Client et vous |
| La veille de l'intervention | Rappel du rendez-vous | Client |
| 3 jours après l'intervention | Demande d'avis Google | Client |

Le rappel de la veille et la demande d'avis supposent que **la date
d'intervention soit saisie dans la console**. Sans elle, ils ne partent pas.

---

## Étape 1 — Créer la base de données

Dans un terminal, depuis le dossier `mathclean-wp` :

```bash
npx wrangler d1 create mathclean
```

La commande affiche un identifiant, du genre
`database_id = "a1b2c3d4-...". `Recopiez-le dans `wrangler.jsonc`, à la place
de `À REMPLACER — voir AUTOMATISATION.md`.

Puis créez les tables :

```bash
npx wrangler d1 execute mathclean --remote --file=worker/schema.sql
```

---

## Étape 2 — Choisir un expéditeur

Il faut un service qui envoie les courriels. Deux conviennent, le gratuit
suffit largement pour votre volume.

| | Resend | Brevo |
|---|---|---|
| Gratuit | 3 000 par mois, 100 par jour | 300 par jour |
| Société | américaine | française |
| Mise en route | plus simple | un peu plus longue |

Prenez **Resend** si vous n'avez pas de préférence : `resend.com`, créez un
compte, section **Domains**, ajoutez `mathclean.fr`.

Resend affiche alors trois enregistrements DNS à créer. Comme votre domaine
est déjà chez Cloudflare, allez dans le tableau de bord Cloudflare →
`mathclean.fr` → **DNS** → **Add record**, et recopiez-les à l'identique.

**Ne sautez pas cette partie.** Ces enregistrements (SPF et DKIM) prouvent que
c'est bien vous qui envoyez. Sans eux, vos devis arrivent en indésirables, ou
n'arrivent pas du tout. La vérification prend de quelques minutes à quelques
heures.

Une fois le domaine vérifié, section **API Keys**, créez une clé et copiez-la.

---

## Étape 3 — Poser les secrets

Trois commandes. Chacune demande la valeur, qui ne s'affiche pas à l'écran.

```bash
npx wrangler secret put RESEND_API_KEY
# collez la clé Resend

npx wrangler secret put ADMIN_CLE
# choisissez un mot de passe long pour la console — gardez-le dans votre
# gestionnaire de mots de passe, il n'est récupérable nulle part

npx wrangler secret put SEL_IP
# n'importe quelle suite de caractères aléatoires : elle sert à compter les
# demandes par visiteur sans conserver les adresses IP
```

Si vous avez choisi Brevo, remplacez la première par `BREVO_API_KEY`.

---

## Étape 4 — Déployer

```bash
npx wrangler deploy
```

---

## Étape 5 — Vérifier

1. Allez sur `mathclean.fr/reservation` et réservez un nettoyage automobile
   avec votre propre adresse électronique.
2. Vous devez recevoir **deux** courriels : le devis, et la notification.
3. Ouvrez le lien du devis, cliquez **Accepter**. Deux courriels de plus.
4. Ouvrez `mathclean.fr/admin`, entrez votre clé : la demande est là.
5. Supprimez-la ensuite si vous voulez repartir propre :
   ```bash
   npx wrangler d1 execute mathclean --remote --command "DELETE FROM demandes WHERE email='votre@adresse'"
   ```

Pour déclencher les relances à la main sans attendre la nuit, la console a un
bouton, ou en ligne de commande :

```bash
npx wrangler dev --test-scheduled
curl "http://localhost:8787/cdn-cgi/handler/scheduled"
```

---

## La console

`mathclean.fr/admin`, votre clé. Elle tient dans un téléphone.

- **En cours** : tout ce qui n'est ni classé ni terminé.
- **À chiffrer** : les sur-devis qui attendent votre prix. C'est l'onglet à
  regarder chaque matin.
- Sur une demande : le détail, le téléphone cliquable, le devis tel que le
  client le voit, et deux champs — les postes du devis, et la date
  d'intervention.
- Le journal des courriels, en bas, dit ce qui est parti et ce qui a échoué,
  avec le motif.

**Chiffrer un sur-devis** : une ligne par poste, un trait vertical avant le
montant.

```
Dégraissage hotte, caisson et filtres | 380
Conduit d'extraction jusqu'au ventilateur | 240
Déplacement | 15
```

Le total se calcule tout seul, le devis part au client, et le cycle de
relances démarre.

---

## Ce qu'il faut savoir

**Les prix ne peuvent pas être trafiqués.** Le navigateur envoie ce que le
client a *choisi* — un numéro de formule, des options, des quantités — jamais
un montant. Le serveur applique sa propre grille, produite à partir de
`content.py` par `build.py`. Un visiteur qui modifie le total affiché dans sa
page n'obtient rien : c'est vérifié par `worker/chiffrage.test.mjs`, qui
rejoue notamment une tentative de passer un forfait à 1 €.

**Les frais de déplacement non plus.** Le code postal déclaré donne une
distance plancher. Annoncer 1 km depuis Versailles ne passe pas.

**Rien ne part deux fois.** Chaque type de courriel est unique par demande,
garanti par la base. Une passe de relances rejouée n'envoie rien de plus.

**Rien ne se perd.** Un envoi raté est réessayé chaque nuit, cinq fois. Si
vous configurez la clé d'envoi après avoir reçu des demandes, tout ce qui
avait échoué repart à la passe suivante.

**Changer un prix** se fait dans `content.py`, puis `python3 build.py`, puis
`npx wrangler deploy`. Le site et le serveur de devis sont alors d'accord,
parce qu'ils lisent la même source.

---

## Ce qui reste à votre main

Le système ne décide jamais d'un prix sur une prestation qui demande de voir.
C'est délibéré : un devis ferme envoyé automatiquement sur un dégraissage de
hotte vous engagerait sur un montant calculé à partir de ce que le client a
déclaré. Vous gardez la main sur les six prestations concernées, et
l'automatisme s'occupe du reste — l'accusé, la mise en forme, l'envoi, les
relances, le rappel et la demande d'avis.

La date d'intervention est l'autre chose qu'il faut saisir. Deux courriels en
dépendent, dont la demande d'avis Google — celle qui compte le plus pour vous
en ce moment.
