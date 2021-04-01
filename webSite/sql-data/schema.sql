CREATE TABLE animaux
(
  id            INT PRIMARY KEY     NOT NULL,
  famille_id    INT                 NOT NULL,
  sexe          TEXT                NOT NULL,
  presence      BOOLEAN             NOT NULL,
  apprivoise    BOOLEAN             NOT NULL,
  mort_ne       BOOLEAN             NOT NULL,
  decede        BOOLEAN             NOT NULL,
  FOREIGN KEY (famille_id) REFERENCES familles (id)
);

CREATE TABLE familles
(
  id            INT PRIMARY KEY     NOT NULL,
  nom           TEXT                NOT NULL
);

CREATE TABLE types
(
  id            INT PRIMARY KEY     NOT NULL,
  type          TEXT                NOT NULL
);

CREATE TABLE animaux_types
(
  animal_id     INT                 NOT NULL,
  type_id       INT                 NOT NULL,
  pourcentage   REAL                NOT NULL,
  PRIMARY KEY (animal_id,type_id),
  FOREIGN KEY (animal_id) REFERENCES animaux (id),
  FOREIGN KEY (type_id) REFERENCES types (id)
);

CREATE TABLE velages
(
  id            INT PRIMARY KEY     NOT NULL,
  mere_id       INT                 NOT NULL,
  pere_id       INT                 NOT NULL,
  date          DATE                NOT NULL,
  FOREIGN KEY (pere_id) REFERENCES animaux (id),
  FOREIGN KEY (mere_id) REFERENCES animaux (id)
);

CREATE TABLE animaux_velages
(
  animal_id     INT                 NOT NULL,
  velage_id     INT                 NOT NULL,
  PRIMARY KEY (animal_id,velage_id),
  FOREIGN KEY (animal_id) REFERENCES animaux (id),
  FOREIGN KEY (velage_id) REFERENCES velages (id)
);

CREATE TABLE complications
(
  id            INT PRIMARY KEY     NOT NULL,
  complication  TEXT                NOT NULL
);

CREATE TABLE velages_complications
(
  velage_id       INT               NOT NULL,
  complication_id INT               NOT NULL,
  PRIMARY KEY (velage_id,complication_id),
  FOREIGN KEY (velage_id) REFERENCES velages (id),
  FOREIGN KEY (complication_id) REFERENCES complications (id)
);