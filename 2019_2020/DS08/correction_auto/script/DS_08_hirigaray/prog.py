NOM = "HIRIGARAY"
Prenom = "Mathieu"
Classe = "MPSI2"
alpha="43"

## Question 1
Q1_req = "select TIT_CODE, CLI_NOM, CLI_PRENOM from T_CLIENT;"

## Question 2
Q2_req = "select count(*) from T_CLIENT;"
Q2_res = "92"

## Question 3
Q3_req = "select CLI_NOM, CLI_PRENOM from T_CLIENT where TIT_CODE='Mme.';"

## Question 4
Q4_req = "select CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.';"


## Question 5
Q5_req = "select CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.';"
Q5_res = "15"

## Question 6
Q6_req = "select CLI_NOM as Noms, CLI_PRENOM as Prénoms from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.' order by Noms, Prénoms asc;"


## Question 7
Q7_req = "select CLI_NOM as Noms, TEL_NUMERO from  T_CLIENT join T_TELEPHONE on T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID;"

## Question 8
Q8_req = "select CLI_NOM from T_CLIENT except select distinct CLI_NOM from T_CLIENT;"

## Question 9
Q9_req = ""
Q9_res = "2"

## Question 10
Q10_req = "SELECT AVG(LIF_REMISE_POURCENT), AVG(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE;"
Q10_res = "58.0, 92.0"

## Question 11
Q11_req = "SELECT max(LIF_REMISE_POURCENT), max(LIF_REMISE_MONTANT) FROM T_LIGNE_FACTURE;"
Q11_res = "58, 92"

## Question 12
Q12_req = "select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_POURCENT!='NULL' or LIF_REMISE_MONTANT!='NULL';"


## Question 13
Q13_req = "select distinct CLI_ID from T_FACTURE join (select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_POURCENT!='NULL' or LIF_REMISE_MONTANT!='NULL') on FAC_ID=fac_id1;"

## Question 14
Q14_req = "select distinct CLI_ID from T_FACTURE join (select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_POURCENT='NULL' and LIF_REMISE_MONTANT='NULL') on FAC_ID=fac_id1;"


## Question 15
Q15_req = "select CLI_NOM, CLI_PRENOM, CLI_ID from T_CLIENT where (select LIF_MONTANT from T_LIGNE_FACTURE join T_FACTURE on T_LIGNE_FACTURE.FAC_ID= T_FACTURE.FAC_ID)=(select max(tt) as aa from (select LIF_MONTANT as tt from T_LIGNE_FACTURE));"
Q15_res ="nom,prenom,480"
