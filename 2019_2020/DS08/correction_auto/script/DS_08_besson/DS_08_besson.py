NOM = "BESSON"
Prenom = "Mathis"
Classe = "MPSI2"
alpha="36"

## Question 1
Q1_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT"

## Question 2
Q2_req = "SELECT COUNT(*) FROM T_CLIENT"
Q2_res = "91"

## Question 3
Q3_req = "SELECT CLI_NOM, CLI_PRENOM FROM T_CLIENT WHERE TIT_CODE='Mme.'"

## Question 4
Q4_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.'"


## Question 5
Q5_req = "SELECT count(*) FROM T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.'"
Q5_res = "15"

## Question 6
Q6_req = "SELECT CLI_NOM as Noms, CLI_PRENOM as Prénoms FROM T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.' ORDER BY Noms"


## Question 7
Q7_req = "SELECT T_CLIENT.CLI_NOM as Noms, T_TELEPHONE.TEL_NUMERO from T_CLIENT join T_TELEPHONE on T_TELEPHONE.CLI_ID=T_CLIENT.CLI_ID WHERE T_TELEPHONE.TYP_CODE='TEL'"

## Question 8
Q8_req = "SELECT CLI_NOM from T_CLIENT group by having count(CLI_NOM)>1"

## Question 9
Q9_req = "SELECT CLI_NOM,count(CLI_NOM) from T_CLIENT group by having count(CLI_NOM)>1"
Q9_res = "BENATTAR:2 et MARTIN:2"

## Question 10
Q10_req = "SELECT avg(LIF_remise_pourcent) as pourcent_moy, avg(LIF_remise_montant) as remise_moy from T_LIGNE_FACTURE"
Q10_res = "moyenne pourcent: 51.0 et moyenne remise: 85.0"

## Question 11
Q11_req = "SELECT max(LIF_remise_pourcent),max(LIF_remise_montant) FROM T_LIGNE_FACTURE"
Q11_res = "max pourecntage: 51 et max remise: 85"

## Question 12
Q12_req = "SELECT FAC_ID as fact_id1 from T_LIGNE_FACTURE WHERE LIF_REMISE_MONTANT>0 or LIF_REMISE_POURCENT>0"


## Question 13
Q13_req = "SELECT T_facture.CLI_ID from T_FACTURE join T_LIGNE_FACTURE on T_LIGNE_FACTURE;FAC_ID=T_FACTURE.FAC_ID WHERE LIF_REMISE_MONTANT>0 or LIF_REMISE_POURCENT>0"

## Question 14
Q14_req = "SELECT T_FACTURE.CLI_ID FROM T_FACTURE EXCEPT(SELECT T_facture.CLI_ID from T_FACTURE join T_LIGNE_FACTURE on T_LIGNE_FACTURE;FAC_ID=T_FACTURE.FAC_ID WHERE LIF_REMISE_MONTANT>0 or LIF_REMISE_POURCENT>0) "


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
