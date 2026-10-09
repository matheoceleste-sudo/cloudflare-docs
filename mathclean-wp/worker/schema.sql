-- Base MathClean — demandes, devis et journal d'envoi.
--
-- À appliquer une seule fois :
--   npx wrangler d1 execute mathclean --remote --file=worker/schema.sql
--
-- Toutes les dates sont stockées en ISO 8601 UTC. L'affichage repasse en
-- heure de Paris au moment du rendu, pas au moment du stockage : une base qui
-- mélange les fuseaux ne se rattrape plus.

CREATE TABLE IF NOT EXISTS demandes (
  id              INTEGER PRIMARY KEY AUTOINCREMENT,
  reference       TEXT    NOT NULL UNIQUE,   -- MC-2026-0001, visible du client
  jeton           TEXT    NOT NULL UNIQUE,   -- adresse secrète du devis
  cree_le         TEXT    NOT NULL,

  -- Le client
  nom             TEXT    NOT NULL,
  email           TEXT    NOT NULL,
  telephone       TEXT    NOT NULL,
  adresse         TEXT,
  code_postal     TEXT,
  ville           TEXT,
  acces           TEXT,
  type_client     TEXT,                      -- particulier | professionnel

  -- Ce qui est demandé
  prestation      TEXT    NOT NULL,          -- slug de la prestation
  prestation_nom  TEXT    NOT NULL,
  regime          TEXT    NOT NULL,          -- ferme | surdevis
  date_souhaitee  TEXT,
  creneau         TEXT,
  message         TEXT,

  -- Le chiffrage, recalculé côté serveur et jamais repris du formulaire
  lignes          TEXT    NOT NULL,          -- JSON : [{libelle, qte, pu, total}]
  deplacement_eur INTEGER NOT NULL DEFAULT 0,
  deplacement_km  REAL,
  total_eur       INTEGER,                   -- NULL tant qu'un sur-devis n'est pas chiffré

  -- Le cycle de vie
  statut          TEXT    NOT NULL,          -- nouveau | devis_envoye | vu | accepte
                                             -- | refuse | planifie | realise | clos
  vu_le           TEXT,
  accepte_le      TEXT,
  refuse_le       TEXT,
  clos_le         TEXT,
  date_intervention TEXT,

  -- Les relances
  relances        INTEGER NOT NULL DEFAULT 0,
  derniere_relance TEXT,

  -- Technique
  ip_hash         TEXT,
  agent           TEXT
);

CREATE INDEX IF NOT EXISTS idx_demandes_statut ON demandes(statut);
CREATE INDEX IF NOT EXISTS idx_demandes_cree   ON demandes(cree_le);
CREATE INDEX IF NOT EXISTS idx_demandes_ip     ON demandes(ip_hash, cree_le);

-- Journal d'envoi. L'index unique est la pièce maîtresse du système : il rend
-- physiquement impossible d'envoyer deux fois le même courriel à la même
-- demande. Un cron qui repasse, une erreur réseau rejouée, un double clic —
-- tout cela se heurte à une contrainte de base, pas à une intention.
--
-- `tentatives` est l'autre moitié du mécanisme. Un envoi en échec garde sa
-- ligne, donc sa place ; la passe suivante peut le reprendre tant que le
-- compteur n'a pas atteint sa limite. Le jour où une clé d'envoi est enfin
-- configurée, tout ce qui avait échoué repart de lui-même.
CREATE TABLE IF NOT EXISTS courriels (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  demande_id  INTEGER NOT NULL REFERENCES demandes(id) ON DELETE CASCADE,
  type        TEXT    NOT NULL,   -- devis | accuse | notif | relance1 | relance2
                                  -- | relance3 | veille | avis | accepte_notif
  envoye_le   TEXT    NOT NULL,
  destinataire TEXT   NOT NULL,
  statut      TEXT    NOT NULL,   -- en_cours | ok | erreur
  tentatives  INTEGER NOT NULL DEFAULT 1,
  detail      TEXT
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_courriels_unicite
  ON courriels(demande_id, type);
