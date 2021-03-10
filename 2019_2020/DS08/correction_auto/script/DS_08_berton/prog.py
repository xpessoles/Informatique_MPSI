NOM = "BERTON"
Prenom = "Margot"
Classe = "MPSI 2"
alpha="65"

## Question 1
Q1_req = """SELECT CLI_NOM,CLI_PRENOM,TIT_CODE
            FROM T_CLIENT;"""

## Question 2
Q2_req = """SELECT COUNT(CLI_ID)
            FROM T_CLIENT;"""
Q2_res = "90"

## Question 3
Q3_req = """SELECT CLI_NOM,CLI_PRENOM
            FROM T_CLIENT
            WHERE TIT_CODE = "Mme.";"""

## Question 4
Q4_req = """SELECT CLI_NOM,CLI_PRENOM,TIT_CODE
            FROM T_CLIENT
            WHERE TIT_CODE = "Mme."

            UNION

            SELECT CLI_NOM,CLI_PRENOM,TIT_CODE
            FROM T_CLIENT
            WHERE TIT_CODE = "Melle.";"""


## Question 5
Q5_req = """SELECT COUNT(CLI_ID)
            FROM T_CLIENT
            WHERE TIT_CODE = "Mme." OR TIT_CODE = "Melle.";"""
Q5_res = "13"

## Question 6
Q6_req = """SELECT CLI_NOM AS Noms,CLI_PRENOM AS Prénoms
            FROM T_CLIENT
            WHERE TIT_CODE = "Mme." or TIT_CODE = "Melle."
            ORDER BY Noms ASC;"""


## Question 7
Q7_req = """SELECT CLI_NOM,TEL_NUMERO
            FROM T_CLIENT,T_TELEPHONE;"""

## Question 8
Q8_req = ""

## Question 9
Q9_req = """SELECT COUNT(*) AS "Nombre d'occurences",CLI_NOM
            FROM T_CLIENT
            GROUP BY CLI_NOM;"""
Q9_res = "1 pour tous, sauf pour Martin et Benattar : 2"

## Question 10
Q10_req = """SELECT AVG(LIF_REMISE_POURCENT),AVG(LIF_REMISE_MONTANT)
             FROM T_LIGNE_FACTURE;"""
Q10_res = "Moyenne remise pourcentage : 80.0, remise montant : 114.0"

## Question 11
Q11_req = """SELECT MAX(LIF_REMISE_POURCENT),MAX(LIF_REMISE_MONTANT)
             FROM T_LIGNE_FACTURE;"""
Q11_res = "Max remise pourcentage : 80, remise montant : 114"

## Question 12
Q12_req = """SELECT FAC_ID AS fac_id1
             FROM T_LIGNE_FACTURE
             WHERE LIF_REMISE_MONTANT IS NOT NULL
                   OR LIF_REMISE_POURCENT IS NOT NULL;"""


## Question 13
Q13_req = """SELECT CLI_ID
             FROM T_FACTURE
             WHERE T_FACTURE.FAC_ID = (SELECT FAC_ID AS fac_id1
						               FROM T_LIGNE_FACTURE
						               WHERE LIF_REMISE_MONTANT IS NOT NULL
								       OR LIF_REMISE_POURCENT IS NOT NULL)
;"""

## Question 14
Q14_req = """SELECT CLI_ID
             FROM T_FACTURE
             WHERE T_FACTURE.FAC_ID = (SELECT FAC_ID AS fac_id1
						               FROM T_LIGNE_FACTURE
						               WHERE LIF_REMISE_MONTANT IS NULL
								       AND LIF_REMISE_POURCENT IS NULL)"""


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
