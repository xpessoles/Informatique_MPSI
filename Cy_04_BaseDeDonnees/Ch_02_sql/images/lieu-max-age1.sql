SELECT *
FROM PERSONNE
WHERE datenaissance = (SELECT min(datenaissance)
                       FROM PERSONNE
                       )
;
