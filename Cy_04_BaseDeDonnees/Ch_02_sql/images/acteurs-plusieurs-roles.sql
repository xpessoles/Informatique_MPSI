SELECT nom, prenom, COUNT(*) AS nbroles
FROM personne, joue
WHERE personne.id=idacteur
GROUP BY personne.id
HAVING nbroles >= 2;
