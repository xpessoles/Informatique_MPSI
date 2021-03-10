NOM = ""
Prenom = ""
Classe = ""
alpha=""

## Question 1
sol_Q1_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT"

## Question 2
sol_Q2_req = "SELECT COUNT(*) FROM T_CLIENT ;"
sol_Q2_res = "100"

## Question 3
sol_Q3_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE='Mme.'"

## Question 4
sol_Q4_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.'"


## Question 5
sol_Q5_req = "SELECT count(*) FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.'"
sol_Q5_res = "17"

## Question 6
sol_Q6_req = "SELECT CLI_NOM as noms, CLI_PRENOM as prenoms FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.' ORDER BY noms, prenoms"


## Question 7
sol_Q7_req = "SELECT T_CLIENT.CLI_NOM, T_TELEPHONE.TEL_NUMERO FROM T_CLIENT JOIN T_TELEPHONE ON T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID WHERE T_TELEPHONE.TYP_CODE="TEL""

## Question 8
sol_Q8_req = "SELECT NOM FROM (SELECT CLI_NOM as Nom, CLI_PRENOM as prenom, COUNT(*) as nb_nom FROM T_CLIENT GROUP BY Nom) WHERE nb_nom>1"

## Question 9
sol_Q9_req = "SELECT * FROM(SELECT CLI_NOM,COUNT(CLI_NOM) AS ct FROM T_CLIENT GROUP BY CLI_NOM ORDER BY CLI_NOM) WHERE ct>1"
sol_Q9_res = "BENATTAR : 2, MARTIN : 3"

## Question 10
sol_Q10_req = " SELECT AVG(LIF_REMISE_MONTANT),  AVG(LIF_REMISE_POURCENT) FROM T_LIGNE_FACTURE"
sol_Q10_res = "Montant : 50, pourcent : 15"

## Question 11
sol_Q11_req = " SELECT MAX(LIF_REMISE_MONTANT),  AVG(LIF_REMISE_POURCENT) FROM T_LIGNE_FACTURE"
sol_Q11_res = "Montant : 50, pourcent : 15"

## Question 12
sol_Q12_req = "SELECT FAC_ID FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0"


## Question 13
sol_Q13_req = "SELECT DISTINCT CLI_ID FROM T_FACTURE JOIN (SELECT T_LIGNE_FACTURE.FAC_ID as facid1  FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0) ON facid1=T_FACTURE.FAC_ID"

## Question 14
sol_Q14_req = "SELECT CLI_ID FROM T_CLIENT EXCEPT SELECT DISTINCT CLI_ID FROM T_FACTURE JOIN (SELECT T_LIGNE_FACTURE.FAC_ID as facid1  FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0) ON facid1=T_FACTURE.FAC_ID"


## Question 15
sol_Q15_req = "SELECT T_CLIENT.CLI_NOM, T_CLIENT.CLI_PRENOM, max(montant_total) FROM T_CLIENT JOIN (SELECT CLI_ID as id_client, sum(montant) as montant_total FROM T_FACTURE JOIN (SELECT T_LIGNE_FACTURE.FAC_ID as facid1,  T_LIGNE_FACTURE.LIF_REMISE_MONTANT as montant FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0)ON facid1=T_FACTURE.FAC_ID GROUP BY CLI_ID) ON T_CLIENT.CLI_ID=id_client;"
sol_Q15_res ="Medard,Jacques,600"
