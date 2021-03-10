NOM = "Azahriou"
Prenom = "Mohamed"
Classe = "mpsi2"
alpha="88"

## Question 1
Q1_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT ;"

## Question 2
Q2_req = "select count(*) as nb_client from T_CLIENT"
Q2_res = "86"

## Question 3
Q3_req = "SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT where TIT_CODE='Mme.';"

## Question 4
Q4_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.';"


## Question 5
Q5_req = "SELECT count(*) FROM T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.';"
Q5_res = "13"

## Question 6
Q6_req = "SELECT CLI_NOM as Noms, CLI_PRENOM as Prénoms FROM T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.' order by Noms;"


## Question 7
Q7_req = "select T_CLIENT.CLI_NOM as Noms, T_TELEPHONE.TEL_NUMERO from T_CLIENT join T_TELEPHONE on T_TELEPHONE.CLI_ID=T_CLIENT.CLI_ID where T_TELEPHONE.TYP_CODE='TEL';"

## Question 8
Q8_req = "SELECT CLI_NOM from T_CLIENT group by CLI_NOM having count(CLI_NOM)>1;"

## Question 9
Q9_req = "SELECT CLI_NOM, count(cli_nom) from T_CLIENT group by CLI_NOM having count(CLI_NOM)>1"
Q9_res = "BENATTAR2,MARTIN2"

## Question 10
Q10_req = "select avg(LIF_remise_pourcent) as moyenne_pourcent, avg(LIF_remise_montant) from T_LIGNE_FACTURE;"
Q10_res = "103.0,137.0"

## Question 11
Q11_req = "select max(LIF_remise_pourcent) as max_pourcent, max(LIF_remise_montant) as max_montant from T_LIGNE_FACTURE;"
Q11_res = "103,137"

## Question 12
Q12_req = "select FAC_ID as fact_id1 from T_LIGNE_FACTURE where LIF_REMISE_MONTANT>0 or LIF_REMISE_POURCENT>0;"


## Question 13
Q13_req = "select T_facture.CLI_ID from T_FACTURE join T_LIGNE_FACTURE on T_LIGNE_FACTURE.FAC_ID=T_FACTURE.FAC_ID where LIF_REMISE_MONTANT>0 or LIF_REMISE_POURCENT>0;"

## Question 14
Q14_req = ""


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
