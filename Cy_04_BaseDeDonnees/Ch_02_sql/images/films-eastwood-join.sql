SELECT titre, date 
FROM FILM
JOIN PERSONNE ON idrealisateur = PERSONNE.id
WHERE nom = 'Eastwood' ;
