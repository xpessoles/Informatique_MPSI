NOM = "Benmaamar"
Prenom = "Bayane"
Classe = "MPSI2"
alpha="80"

## Question 1
Q1_req = "SELECT CLI_NOM,CLI_PRENOM,TIT_CODE FROM T_CLIENT"

## Question 2
Q2_req = "SELECT COUNT (*) from (SELECT DISTINCT CLI_ID FROM T_CLIENT)"
Q2_res = "87"

## Question 3
Q3_req = "SELECT CLI_NOM,CLI_PRENOM FROM T_CLIENT WHERE TIT_CODE = 'Mme.'"

## Question 4
Q4_req = "SELECT CLI_NOM,CLI_PRENOM FROM T_CLIENT WHERE TIT_CODE='Mme.'"


## Question 5
Q5_req = "SELECT COUNT (*) FROM T_CLIENT WHERE TIT_CODE= 'Mme.' OR TIT_CODE='Melle.'"
Q5_res = "15"

## Question 6
Q6_req = "SELECT CLI_NOM AS 'Noms' ,CLI_PRENOM AS 'Prenoms' FROM T_CLIENT WHERE TIT_CODE= 'Mme.' OR TIT_CODE= 'Melle.' ORDER BY CLI_NOM ASC, CLI_PRENOM ASC"


## Question 7
Q7_req = "SELECT T_CLIENT.CLI_NOM,T_TELEPHONE.TEL_NUMERO FROM T_CLIENT JOIN T_TELEPHONE ON T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID"

## Question 8
Q8_req = "SELECT CLI_NOM,CLI_PRENOM from T_CLIENT JOIN (SELECT CLI_NOM as nom, COUNT(CLI_NOM) as nb FROM T_CLIENT GROUP BY CLI_NOM) ON T_CLIENT.CLI_NOM=nom WHERE nb>1"

## Question 9
Q9_req = "SELECT CLI_NOM,nb from (SELECT CLI_NOM,COUNT(CLI_NOM) as nb FROM T_CLIENT GROUP BY CLI_NOM) WHERE nb>1"
Q9_res = " 'BENATTAR 2 ', 'MARTIN 3'"

## Question 10
Q10_req = "SELECT avg(LIF_REMISE_POURCENT),avg(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE"
Q10_res = " '95','129'"

## Question 11
Q11_req = "SELECT max(LIF_REMISE_POURCENT),max(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE"
Q11_res = "'95','129'"

## Question 12
Q12_req = ""


## Question 13
Q13_req = ""

## Question 14
Q14_req = ""


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
