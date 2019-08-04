SELECT FILM.titre, FILM.date 
FROM FILM, PERSONNE
WHERE idrealisateur = PERSONNE.id
      AND 
      nom = 'Eastwood' ;
