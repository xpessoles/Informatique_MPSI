NOM = "PETIT"
Prenom = "Theo"
Classe = "MPSI2"
alpha="70"

## Question 1
Q1_req = "SELECT CLI_NOM,CLI_PRENOM,TIT_CODE from T_CLIENT"

## Question 2
Q2_req = "SELECT COUNT (*) from (SELECT DISTINCT CLI_ID from T_CLIENT)"
Q2_res = ""

## Question 3
Q3_req = "SELECT CLI_NOM,CLI_PRENOM from T_CLIENT WHERE TIT_CODE = 'Mme.'"

## Question 4
Q4_req = "SELECT CLI_NOM,CLI_PRENOM,TIT_CODE from T_CLIENT WHERE TIT_CODE = 'Mme.' OR TIT_CODE='Melle.'"


## Question 5
Q5_req = "SELECT COUNT (*) from T_CLIENT WHERE TIT_CODE = 'Mme.' OR TIT_CODE='Melle.'"
Q5_res = ""

## Question 6
Q6_req = "SELECT CLI_NOM as 'Noms' , CLI_PRENOM as 'Prénoms' From T_CLIENT WHERE TIT_CODE = 'Mme.' OR TIT_CODE='Melle.' ORDER BY CLI_NOM ASC, CLI_PRENOM ASC"


## Question 7
Q7_req = "SELECT T_CLIENT.CLI_NOM,T_TELEPHONE.TEL_NUMERO from T_CLIENT join T_TELEPHONE on T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID"

## Question 8
Q8_req = "SELECT CLI_NOM FROM (SELECT CLI_NOM,count(CLI_NOM) as a FROM T_CLIENT GROUP BY CLI_NOM) where a > 1"

## Question 9
Q9_req = ""
Q9_res = ""

## Question 10
Q10_req = "SELECT avg(LIF_REMISE_POURCENT), avg(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE"
Q10_res = ""

## Question 11
Q11_req = "SELECT max(LIF_REMISE_POURCENT), max(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE"
Q11_res = ""

## Question 12
Q12_req = ""


## Question 13
Q13_req = ""

## Question 14
Q14_req = ""


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
