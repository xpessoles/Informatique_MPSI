SELECT COUNT(*) AS nbacteurs
FROM (SELECT DISTINCT idacteur
      FROM JOUE
      )
;
