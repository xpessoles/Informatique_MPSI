NOM = "KHATIB"
Prenom = "Rabab"
Classe = "MPSI2"
alpha="7"

## Question 1
Q1_req = "SELECT TIT_CODE, CLI_NOM, CLI_PRENOM FROM T_CLIENT;"

## Question 2
Q2_req = "SELECT COUNT (*) FROM T_CLIENT;"
Q2_res = "98"

## Question 3
Q3_req = "SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT WHERE TIT_CODE='Mme.';"

## Question 4
Q4_req = "SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT WHERE (TIT_CODE='Mme.' OR TIT_CODE='Melle.');"

## Question 5
Q5_req = "SELECT COUNT (*) FROM T_CLIENT WHERE (TIT_CODE='Mme.' OR TIT_CODE='Melle.' );"
Q5_res = "17"

## Question 6
Q6_req = "SELECT CLI_NOM AS 'Noms', CLI_PRENOM AS 'Prénoms'  FROM (SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT WHERE (TIT_CODE='Mme.' OR TIT_CODE='Melle.' ) ORDER BY CLI_NOM) ORDER BY CLI_PRENOM;"

## Question 7
Q7_req = ""

## Question 8
Q8_req = ""

## Question 9
Q9_req = ""
Q9_res = ""

## Question 10
Q10_req = ""
Q10_res = ""

## Question 11
Q11_req = ""
Q11_res = ""

## Question 12
Q12_req = "SELECT FAC_ID AS 'fac_id1' FROM T_LIGNE_FACTURE WHERE LIF_REMISE_MONTANT<>'NULL';"


## Question 13
Q13_req = "SELECT CLI_ID FROM T_FACTURE JOIN T_LIGNE_FACTURE ON T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID WHERE LIF_REMISE_MONTANT<>'NULL';"

## Question 14
Q14_req = ""


## Question 15
Q15_req = "SELECT MAX(cout) FROM (SELECT FAC_ID, SUM(LIF_REMISE_MONTANT) AS 'cout' FROM T_LIGNE_FACTURE GROUP BY FAC_ID);"
Q15_res ="MEDARD,Jacques,504"
