NOM = "FORTIN"
Prenom = "Côme"
Classe = "MPSI2"
alpha="84"

## Question 1
Q1_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT;"

## Question 2
Q2_req = "SELECT count(*) from T_CLIENT;"
Q2_res = "86"

## Question 3
Q3_req = "SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT WHERE TIT_CODE = 'Mme.';"

## Question 4
Q4_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE = 'Mme.' UNION SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE = 'Melle.';"


## Question 5
Q5_req = "SELECT count(*) as nbr_clientes FROM (SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE = 'Mme.' UNION SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE = 'Melle.');"
Q5_res = "15"

## Question 6
Q6_req = "SELECT CLI_NOM as Noms, CLI_PRENOM as Prénoms FROM (SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE = 'Mme.' UNION SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE = 'Melle.') ORDER by CLI_NOM ASC, CLI_PRENOM ASC;"


## Question 7
Q7_req = "SELECT CLI_NOM, TEL_NUMERO FROM T_CLIENT JOIN T_TELEPHONE on T_CLIENT.CLI_ID = T_TELEPHONE.CLI_ID;"

## Question 8
Q8_req = "SELECT T_CLIENT.CLI_NOM, T_CLIENT.CLI_PRENOM FROM T_CLIENT WHERE T_CLIENT.CLI_NOM = (SELECT T_CLIENT.CLI_NOM FROM T_CLIENT GROUP by T_CLIENT.CLI_NOM HAVING count(CLI_NOM) >=2);"

## Question 9
Q9_req = "SELECT CLI_NOM, count(*) as même_nom FROM T_CLIENT GROUP by CLI_NOM HAVING même_nom >=2;"
Q9_res = "Martin = 3"

## Question 10
Q10_req = "SELECT avg(LIF_REMISE_POURCENT) as moyenne_pourcent, avg(LIF_REMISE_MONTANT) as moyenne_montant FROM T_LIGNE_FACTURE;"
Q10_res = "Remises en pourcentage = 99.0, Remises en montant = 133.0"

## Question 11
Q11_req = "SELECT max(LIF_REMISE_POURCENT) as max_pourcent, max(LIF_REMISE_MONTANT) as max_montant FROM T_LIGNE_FACTURE;"
Q11_res = "Remises en pourcentage = 99.0, Remises en montant = 133.0"

## Question 12
Q12_req = "SELECT FAC_ID as fac_id1 FROM T_LIGNE_FACTURE WHERE LIF_REMISE_MONTANT > 0 UNION SELECT FAC_ID, LIF_REMISE_MONTANT, LIF_REMISE_POURCENT as fac_id1 FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT > 0;"


## Question 13
Q13_req = ""

## Question 14
Q14_req = ""


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
