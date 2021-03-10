NOM = "HAMADI"
Prenom = "Halima"
Classe = "MPSI2"
alpha="73"

## Question 1
Q1_req = "select CLI_NOM,CLI_PRENOM, TIT_CODE from T_CLIENT;"

## Question 2
Q2_req = "select count (CLI_ID) from T_CLIENT;"
Q2_res = "89"

## Question 3
Q3_req = "select CLI_NOM,CLI_PRENOM from T_CLIENT where TIT_CODE='Mme.';"

## Question 4
Q4_req = "select CLI_NOM,CLI_PRENOM,TIT_CODE from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.';"


## Question 5
Q5_req = "select count(*) from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.';"
Q5_res = "15"

## Question 6
Q6_req = "select DISTINCT CLI_NOM as Noms , CLI_PRENOM as Prénoms from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.' order by Noms ASC, Prénoms ASC;"


## Question 7
Q7_req = "select T_CLIENT.CLI_NOM, T_TELEPHONE.TEL_NUMERO from T_CLIENT, T_TELEPHONE;"

## Question 8
Q8_req = "select T_CLIENT.CLI_NOM, T_CLIENT.CLI_PRENOM from T_CLIENT where t_client.CLI_NOM=(select T_CLIENT.CLI_NOM from T_CLIENT GROUP by T_CLIENT.CLI_NOM HAVING count(CLI_NOM)>1);"

## Question 9
Q9_req = "select CLI_NOM, cn from ( select CLI_NOM, count(CLI_NOM) as cn from T_CLIENT GROUP by CLI_NOM );"
Q9_res = "MARTIN =3, les autres=1"

## Question 10
Q10_req = "select avg( LIF_REMISE_POURCENT), avg( LIF_REMISE_MONTANT) from T_LIGNE_FACTURE;"
Q10_res = "88.0 et 122.0"

## Question 11
Q11_req = "select max( LIF_REMISE_POURCENT), max( LIF_REMISE_MONTANT) from T_LIGNE_FACTURE;"
Q11_res = "88 et 122"

## Question 12
Q12_req = "select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT !=0 or LIF_REMISE_POURCENT!=0;"


## Question 13
Q13_req = "select CLI_ID from T_FACTURE join T_LIGNE_FACTURE on T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID where LIF_REMISE_MONTANT !=0 or LIF_REMISE_POURCENT!=0;"

## Question 14
Q14_req = "select CLI_ID from T_FACTURE join T_LIGNE_FACTURE on T_FACTURE.FAC_ID=T_LIGNE_FACTURE.FAC_ID where LIF_REMISE_MONTANT < 122 and LIF_REMISE_POURCENT <88;"


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
