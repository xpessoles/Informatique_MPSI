NOM = "FAURE"
Prenom = "Benoit"
Classe = "MPSI2"
alpha="69"

## Question 1
Q1_req = "SELECT TIT_CODE, CLI_NOM, CLI_PRENOM FROM T_CLIENT"

## Question 2
Q2_req = "SELECT count(CLI_ID) FROM T_CLIENT"
Q2_res = "90"

## Question 3
Q3_req = "SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT WHERE TIT_CODE = "Mme.""

## Question 4
Q4_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE = "Mme." OR TIT_CODE = "Melle.""


## Question 5
Q5_req = "SELECT count(CLI_ID) FROM T_CLIENT WHERE TIT_CODE = "Mme." OR TIT_CODE = "Melle.""
Q5_res = "15"

## Question 6
Q6_req = "SELECT CLI_NOM as Noms, CLI_PRENOM as Prénoms FROM T_CLIENT WHERE TIT_CODE = "Mme." OR TIT_CODE = "Melle." ORDER BY CLI_NOM ASC, CLI_PRENOM ASC"


## Question 7
Q7_req = "SELECT CLI_NOM, TEL_NUMERO FROM T_CLIENT, T_TELEPHONE WHERE T_CLIENT.CLI_ID = T_TELEPHONE.CLI_ID"

## Question 8
Q8_req = "SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT WHERE CLI_NOM = (SELECT CLI_NOM FROM T_CLIENT GROUP BY CLI_NOM HAVING count(CLI_NOM)>1)"

## Question 9
Q9_req = "SELECT CLI_NOM, count(CLI_PRENOM) FROM T_CLIENT WHERE CLI_NOM = (SELECT CLI_NOM FROM T_CLIENT GROUP BY CLI_NOM HAVING count(CLI_NOM)>1)"
Q9_res = "2"

## Question 10
Q10_req = "SELECT AVG(LIF_REMISE_POURCENT), AVG(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE"
Q10_res = "84.0, 118.0"

## Question 11
Q11_req = "SELECT MAX(LIF_REMISE_POURCENT), MAX(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE"
Q11_res = "84, 118"

## Question 12
Q12_req = "SELECT FAC_ID as fac_id1 FROM T_LIGNE_FACTURE WHERE LIF_REMISE_MONTANT IS NOT NULL or LIF_REMISE_POURCENT IS NOT NULL"

## Question 13
Q13_req = "SELECT CLI_ID FROM T_FACTURE WHERE FAC_ID = (SELECT FAC_ID FROM T_LIGNE_FACTURE WHERE LIF_REMISE_MONTANT IS NOT NULL or LIF_REMISE_POURCENT IS NOT NULL) GROUP BY CLI_ID"

## Question 14
Q14_req = "SELECT CLI_ID FROM T_FACTURE WHERE FAC_ID = (SELECT FAC_ID FROM T_LIGNE_FACTURE WHERE LIF_REMISE_MONTANT IS NULL or LIF_REMISE_POURCENT IS NULL) GROUP BY CLI_ID"


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
