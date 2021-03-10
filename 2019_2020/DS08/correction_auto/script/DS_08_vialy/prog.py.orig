NOM = "VIALY"
Prenom = "Carla"
Classe = "MPSI2"
alpha="60"

## Question 1
Q1_req = "select CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT"

## Question 2
Q2_req = "select count(*) from T_CLIENT"
Q2_res = "89"

## Question 3
Q3_req = "select CLI_NOM, CLI_PRENOM from T_CLIENT where TIT_CODE='Mme.'"

## Question 4
Q4_req = "select CLI_NOM, CLI_PRENOM from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.'
"


## Question 5
Q5_req = "select count(*) from T_CLIENT where TIT_CODE!='M.'"
Q5_res = "16"

## Question 6
Q6_req = "select CLI_NOM as 'Noms',CLI_PRENOM as 'Prénoms' from T_CLIENT where TIT_CODE!='M.' order by CLI_NOM"


## Question 7
Q7_req = ""

## Question 8
Q8_req = "select CLI_NOM from T_CLIENT group by CLI_NOM having count(CLI_NOM)>1"

## Question 9
Q9_req = "select CLI_NOM, count(CLI_NOM) from T_CLIENT group by CLI_NOM having count(CLI_NOM)>1"
Q9_res = "BENATTAR 2, MARTIN 3"

## Question 10
Q10_req = "select avg(LIF_REMISE_POURCENT), avg(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE"
Q10_res = "75.0, 109.0"

## Question 11
Q11_req = "select max(LIF_REMISE_POURCENT), max(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE"
Q11_res = "75, 109"

## Question 12
Q12_req = "select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT=109 or LIF_REMISE_POURCENT=75"


## Question 13
Q13_req = "select distinct CLI_ID from T_FACTURE JOIN (select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT=109 or LIF_REMISE_POURCENT=75) on T_FACTURE.FAC_ID=fac_id1"

## Question 14
Q14_req = "select CLI_ID from T_CLIENT except select distinct CLI_ID from T_FACTURE JOIN (select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT=109 or LIF_REMISE_POURCENT=75) on T_FACTURE.FAC_ID=fac_id1"


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
