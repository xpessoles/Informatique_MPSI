SELECT DISTINCT nom, prenom 
FROM PERSONNE, JOUE
WHERE id = idacteur
ORDER BY nom ASC, prenom ASC;
