NOM = "MARJOLLET"
Prenom = "Iris"
Classe = "MPSI2"
alpha="51"

## Question 1
Q1_req = "SELECT TIT_CODE,CLI_NOM,CLI_PRENOM FROM T_client ;;"

## Question 2
Q2_req = "SELECT COUNT(*) FROM T_client;;"
Q2_res = "91"

## Question 3
Q3_req = "SELECT CLI_NOM,CLI_PRENOM FROM T_client WHERE TIT_CODE='Mme.';;"

## Question 4
Q4_req = "SELECT TIT_CODE,CLI_NOM,CLI_PRENOM FROM T_client WHERE TIT_CODE != 'M.';;"


## Question 5
Q5_req = "SELECT COUNT (*) FROM T_client WHERE TIT_CODE != 'M.';;"
Q5_res = "16"

## Question 6
Q6_req = "SELECT CLI_NOM AS Noms ,CLI_PRENOM AS Prénoms FROM T_CLIENT WHERE TIT_CODE != 'M.' ORDER BY Noms ASC ;;"


## Question 7
Q7_req = "SELECT CLI_NOM , TEL_NUMERO FROM T_CLIENT, T_TELEPHONE WHERE T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID;;"

## Question 8
Q8_req = "SELECT CLI_NOM,CLI_PRENOM FROM T_CLIENT WHERE CLI_NOM=(SELECT CLI_NOM FROM(SELECT CLI_NOM,COUNT(*) AS Nb FROM T_CLIENT GROUP BY CLI_NOM) WHERE Nb>1);;"

## Question 9
Q9_req = "SELECT CLI_NOM,Nb FROM (SELECT CLI_NOM,COUNT(*) AS Nb FROM T_CLIENT GROUP BY CLI_NOM) WHERE Nb>1;;"
Q9_res = "MARTIN : 2"

## Question 10
Q10_req = "SELECT CAST(SUM(LIF_REMISE_MONTANT) AS FLOAT)/CAST(SUM(LIF_QTE) AS FLOAT), CAST(SUM(LIF_REMISE_POURCENT) as FLOAT)/CAST(SUM(LIF_QTE) AS FLOAT) FROM T_LIGNE_FACTURE;;"
Q10_res = "en pourcentage : 1.79 , en montant : 2.29"

## Question 11
Q11_req = "SELECT MAX(LIF_REMISE_POURCENT), MAX(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE;;"
Q11_res = "en pourcentage : 66, en montant : 100"

## Question 12
Q12_req = "SELECT FAC_ID AS fac_id1 FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT OR LIF_REMISE_MONTANT;;"


## Question 13
Q13_req = ""

## Question 14
Q14_req = ""


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
