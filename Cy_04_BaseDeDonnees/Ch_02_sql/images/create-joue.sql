CREATE TABLE JOUE (
  idacteur INTEGER,
  idfilm INTEGER,
  idpersonnage INTEGER,
  PRIMARY KEY(idacteur, idfilm, idpersonnage),
  FOREIGN KEY(idacteur) REFERENCES PERSONNE,
  FOREIGN KEY(idfilm) REFERENCES FILM,
  FOREIGN KEY(idpersonnage) REFERENCES PERSONNAGE
);
