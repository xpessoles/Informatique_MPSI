NOM = "MEISSIREL"
Prenom = "ELISE"
Classe = "MPSI2"
alpha="54"

## Question 1
Q1_req = "SELECT TIT_CODE, CLI_NOM, CLI_PRENOM from T_CLIENT"

## Question 2
Q2_req = "select count(*) from T_CLIENT"
Q2_res = "90"

## Question 3
Q3_req = "select CLI_NOM, CLI_PRENOM from T_CLIENT where TIT_CODE='Mme.'"

## Question 4
Q4_req = "select count(*) from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.'"


## Question 5
Q5_req = "select count(*) from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.'"
Q5_res = "15"

## Question 6
Q6_req = "select CLI_NOM as Nom, CLI_PRENOM as Prénom from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.' order by CLI_NOM;"


## Question 7
Q7_req = "select CLI_NOM, TEL_NUMERO from T_CLIENT join T_TELEPHONE on T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID"

## Question 8
Q8_req = "select CLI_NOM, CLI_PRENOM from T_CLIENT where CLI_NOM in (select CLI_NOM from T_CLIENT group by CLI_NOM HAVING count(*)>1)"

## Question 9
Q9_req = "select CLI_NOM, count(*) from T_CLIENT group by CLI_NOM having count(*)>1"
Q9_res = "BENATTAR : 2, MARTIN : 2"

## Question 10
Q10_req = "select avg(LIF_REMISE_POURCENT) AS 'moyenne pourcentage', avg (LIF_REMISE_MONTANT)AS 'moyenne montant' from T_LIGNE_FACTURE"
Q10_res = "69,103"

## Question 11
Q11_req = "select max(LIF_REMISE_POURCENT) AS 'maximum pourcentage', max(LIF_REMISE_MONTANT)AS 'maximum montant' from T_LIGNE_FACTURE"
Q11_res = "69,103"

## Question 12
Q12_req = "select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT is NOT NULL or LIF_REMISE_POURCENT is NOT NULL"


## Question 13
Q13_req = "SELECT DISTINCT CLI_ID from T_FACTURE where FAC_ID in (select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT is NOT NULL or LIF_REMISE_POURCENT is NOT NULL)"

## Question 14
Q14_req = "SELECT DISTINCT CLI_ID from T_FACTURE where FAC_ID not in (select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT is NOT NULL or LIF_REMISE_POURCENT is NOT NULL)"


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
