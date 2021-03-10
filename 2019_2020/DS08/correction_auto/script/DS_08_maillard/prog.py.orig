NOM = "MAILLARD"
Prenom = "Chloé"
Classe = "MPSI2"
alpha="46"

## Question 1
Q1_req = "select CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT;"

## Question 2
Q2_req = "select count(*) from T_CLIENT;"
Q2_res = "92"

## Question 3
Q3_req = "select CLI_NOM, CLI_PRENOM from T_CLIENT where TIT_CODE='Mme.';"

## Question 4
Q4_req = "select CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.';"


## Question 5
Q5_req = "select count(*) from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.';"
Q5_res = "16"

## Question 6
Q6_req = "select CLI_NOM as Noms, CLI_PRENOM as 'Prénoms' from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.' order by CLI_NOM ASC;"


## Question 7
Q7_req = "select CLI_NOM, TEL_NUMERO from T_CLIENT join T_TELEPHONE on T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID;"

## Question 8
Q8_req = "select CLI_NOM, count(*) as nb from T_CLIENT group by CLI_NOM having nb>=2;"

## Question 9
Q9_req = "select count(*) as nb from T_CLIENT group by CLI_NOM having nb>=2;"
Q9_res = "2,2"

## Question 10
Q10_req = "select avg(LIF_REMISE_POURCENT), avg(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE;"
Q10_res = "61,95"

## Question 11
Q11_req = "select max(LIF_REMISE_POURCENT), max(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE;"
Q11_res = "61,95"

## Question 12
Q12_req = "select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT!='NULL' or LIF_REMISE_POURCENT!='NULL';"


## Question 13
Q13_req = "select T_CLIENT.CLI_ID from T_CLIENT join T_FACTURE on T_CLIENT.CLI_ID=T_FACTURE.CLI_ID join T_LIGNE_FACTURE on T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID where LIF_REMISE_MONTANT!='NULL' or LIF_REMISE_POURCENT!='NULL';"

## Question 14
Q14_req = "select T_CLIENT.CLI_ID from T_CLIENT join T_FACTURE on T_CLIENT.CLI_ID=T_FACTURE.CLI_ID join T_LIGNE_FACTURE on T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID where LIF_REMISE_MONTANT='NULL' and LIF_REMISE_POURCENT='NULL';"


## Question 15
Q15_req = "select T_CLIENT.CLI_NOM, T_CLIENT.CLI_PRENOM, sum(LIF_REMISE_MONTANT), sum(LIF_REMISE_POURCENT) from T_CLIENT join T_FACTURE on T_CLIENT.CLI_ID=T_FACTURE.CLI_ID join T_LIGNE_FACTURE on T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID group by T_CLIENT.CLI_NOM ;"
Q15_res ="Benattar,Pierre,1615"
