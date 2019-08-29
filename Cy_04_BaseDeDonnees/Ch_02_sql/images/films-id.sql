CREATE TABLE "PERSONNAGE" (
  "id" INTEGER,
  "nom" VARCHAR(50),
  PRIMARY KEY("id")
);

CREATE TABLE "JOUE" (
  "id.1",
  "id.2",
  "id.3",
  PRIMARY KEY("id.1", "id.2", "id.3")
);

CREATE TABLE "PERSONNE" (
  "id" INTEGER,
  "nom" VARCHAR(50),
  "prenom" VARCHAR(50),
  "date_naissance" DATE,
  PRIMARY KEY("id")
);

CREATE TABLE "FILM" (
  "id.1",
  "titre",
  "date",
  "id.2",
  PRIMARY KEY("id.1")
);

ALTER TABLE "JOUE" ADD FOREIGN KEY ("id") REFERENCES "PERSONNE" ("id");

ALTER TABLE "JOUE" ADD FOREIGN KEY ("id") REFERENCES "FILM" ("id");

ALTER TABLE "JOUE" ADD FOREIGN KEY ("id") REFERENCES "PERSONNAGE" ("id");

ALTER TABLE "FILM" ADD FOREIGN KEY ("id") REFERENCES "PERSONNE" ("id");

INSERT INTO PERSONNE (nom, prenom, date_naissance) VALUES('Kubrick', 'Stanley', date('1928-07-26'));


DELETE FROM ... WHERE ...
