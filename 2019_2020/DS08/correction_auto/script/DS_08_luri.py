NOM = "Luri Vañó"
Prenom = "Jorge"
Classe = "MPSI 2"
alpha="2"

## Question 1
Q1_req = "SELECT TIT_CODE, CLI_PRENOM, CLI_NOM
FROM T_CLIENT
;;"

## Question 2
Q2_req = "SELECT COUNT()
FROM T_CLIENT
;;"
Q2_res = "97"

## Question 3
Q3_req = "SELECT CLI_PRENOM, CLI_NOM
FROM T_CLIENT
WHERE TIT_CODE="Mme."
;;"

## Question 4
Q4_req = "SELECT TIT_CODE, CLI_PRENOM, CLI_NOM
FROM T_CLIENT
WHERE TIT_CODE="Mme."

UNION

SELECT TIT_CODE, CLI_PRENOM, CLI_NOM
FROM T_CLIENT
WHERE TIT_CODE="Melle."
;;"


## Question 5
Q5_req = "SELECT COUNT()
FROM T_CLIENT
WHERE TIT_CODE="Mme." OR TIT_CODE="Melle."
;;"
Q5_res = "17"

## Question 6
Q6_req = "SELECT CLI_NOM AS "Nom", CLI_PRENOM AS "Prenom"
FROM T_CLIENT
WHERE TIT_CODE="Melle." OR TIT_CODE="Mme."
ORDER BY CLI_NOM"


## Question 7
Q7_req = "SELECT CLI_NOM AS "Nom", TEL_NUMERO AS "Numéro de téléphone"
FROM T_CLIENT, T_TELEPHONE
WHERE T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID
ORDER BY CLI_NOM"

## Question 8
Q8_req = "SELECT TIT_CODE, T_CLIENT.CLI_PRENOM, T_CLIENT.CLI_NOM
FROM T_CLIENT
WHERE T_CLIENT.CLI_NOM= (SELECT T_CLIENT.CLI_NOM FROM T_CLIENT GROUP by	T_CLIENT.CLI_NOM HAVING  COUNT(CLI_NOM)=3) OR T_CLIENT.CLI_NOM= (SELECT T_CLIENT.CLI_NOM FROM T_CLIENT GROUP by	T_CLIENT.CLI_NOM HAVING  COUNT(CLI_NOM)=2)

"

## Question 9
Q9_req = "SELECT CLI_NOM,  COUNT(*) AS Nombre
FROM T_CLIENT
GROUP BY CLI_NOM
HAVING Nombre>=2"
Q9_res = "Benattar=2;Martin=3"

## Question 10
Q10_req = "SELECT AVG(LIF_REMISE_POURCENT) AS "Valeur moyenne des remises en pourcentage", AVG(LIF_REMISE_MONTANT) AS "Valeur moyenne des remises en montant"
FROM T_LIGNE_FACTURE"
Q10_res = "17;51"

## Question 11
Q11_req = "SELECT max(LIF_REMISE_POURCENT) AS "Valeur maximale des remises en pourcentage", max(LIF_REMISE_MONTANT) AS "Valeur maximale des remises en montant"
FROM T_LIGNE_FACTURE"
Q11_res = "17;51"

## Question 12
Q12_req = "SELECT FAC_ID AS "fac_id1"
FROM T_LIGNE_FACTURE
WHERE LIF_REMISE_MONTANT>0 OR LIF_REMISE_POURCENT>0"


## Question 13
Q13_req = "SELECT T_FACTURE.CLI_ID
FROM T_FACTURE, T_LIGNE_FACTURE
WHERE (LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0) AND T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID"

## Question 14
Q14_req = "SELECT T_FACTURE.CLI_ID
FROM T_FACTURE

EXCEPT

SELECT T_FACTURE.CLI_ID
FROM T_FACTURE, T_LIGNE_FACTURE
WHERE (LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0) AND T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID"


## Question 15
Q15_req = "SELECT CLI_NOM, CLI_PRENOM, max(LIF_MONTANT)*0.17
FROM T_CLIENT, T_LIGNE_FACTURE, T_FACTURE
WHERE T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID AND T_FACTURE.CLI_ID=T_CLIENT.CLI_ID AND LIF_REMISE_POURCENT>0"
Q15_res ="THIRIOT,Jacky,81.6"
