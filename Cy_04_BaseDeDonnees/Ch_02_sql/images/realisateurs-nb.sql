SELECT nom, prenom, COUNT(*) as nbfilms
FROM PERSONNE, FILM
WHERE idrealisateur = PERSONNE.id
GROUP BY PERSONNE.id;