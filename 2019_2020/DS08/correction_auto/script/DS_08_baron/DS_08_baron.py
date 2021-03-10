NOM = "Baron"
Prenom = "Tanya"
Classe = "MPSI 2"
alpha="57"

## Question 1
Q1_req = "select TIT_CODE, CLI_NOM, CLI_PRENOM from T_CLIENT;"

## Question 2
Q2_req = "select count(CLI_NOM) from T_CLIENT;"
Q2_res = "92"

## Question 3
Q3_req = "select CLI_NOM, CLI_PRENOM from T_CLIENT where TIT_CODE = 'Mme.';"

## Question 4
Q4_req = "select TIT_CODE, CLI_NOM, CLI_PRENOM from T_CLIENT where TIT_CODE = 'Mme.' or  TIT_CODE= 'Melle.';"


## Question 5
Q5_req = "select count(CLI_NOM) from T_CLIENT where TIT_CODE = 'Mme.' or  TIT_CODE= 'Melle.';"
Q5_res = "17"

## Question 6
Q6_req = "select CLI_NOM as NOM, CLI_PRENOM as PRENOM from T_CLIENT where TIT_CODE = 'Mme.' or  TIT_CODE= 'Melle.' order by CLI_NOM asc;"


## Question 7
Q7_req = "select CLI_NOM, TEL_NUMERO from T_CLIENT join T_TELEPHONE on T_TELEPHONE.CLI_ID = T_CLIENT.CLI_ID;"

## Question 8
Q8_req = "select CLI_NOM, CLI_PRENOM from T_CLIENT group by CLI_NOM having count(CLI_NOM)>1 ; "

## Question 9
Q9_req = "select length(CLI_NOM) from T_CLIENT group by CLI_NOM having count(CLI_NOM)>1 ;"
Q9_res = "8 , 6"

## Question 10
Q10_req = "select avg(LIF_REMISE_POURCENT), avg(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE;"
Q10_res = "72.0  , 106.0"

## Question 11
Q11_req = "select max(LIF_REMISE_POURCENT), max(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE;"
Q11_res = "72,  106"

## Question 12
Q12_req = "select distinct FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT = '106' or LIF_REMISE_POURCENT= '72';"


## Question 13
Q13_req = ""

## Question 14
Q14_req = ""


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"


