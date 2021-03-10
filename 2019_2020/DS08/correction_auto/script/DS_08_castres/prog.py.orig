NOM = "Castres"
Prenom = "Yann"
Classe = "MPSI 2"
alpha="9"

## Question 1
Q1_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT;"

## Question 2
Q2_req = "select count(*) as nbcli from T_CLIENT;"
Q2_res = "98"

## Question 3
Q3_req = "SELECT CLI_NOM, CLI_PRENOM from T_CLIENT where TIT_CODE="Mme.";"

## Question 4
Q4_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT where TIT_CODE="Mme." or TIT_CODE="Melle.";"


## Question 5
Q5_req = "SELECT count(*) as nbclie from (SELECT CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT where TIT_CODE="Mme." or TIT_CODE="Melle.");"
Q5_res = "17"

## Question 6
Q6_req = "SELECT CLI_NOM as Noms, CLI_PRENOM as Prénoms from
(SELECT CLI_NOM, CLI_PRENOM, TIT_CODE from T_CLIENT where TIT_CODE="Mme." or TIT_CODE="Melle.")
order by CLI_NOM ASC;"


## Question 7
Q7_req = "SELECT CLI_NOM, TEL_NUMERO from T_CLIENT
Join T_TELEPHONE on T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID; "

## Question 8
Q8_req = "SELECT CLI_NOM, CLI_PRENOM, count(*) from T_CLIENT group by CLI_NOM having count(CLI_NOM)>1;"

## Question 9
Q9_req = "SELECT CLI_NOM, count(*) from T_CLIENT group by CLI_NOM having count(CLI_NOM)>1;"
Q9_res = "2 benattar,3 martin"

## Question 10
Q10_req = "SELECT avg(LIF_REMISE_POURCENT), avg(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE;"
Q10_res = "Pourcent : 24, Montant : 58"

## Question 11
Q11_req = "SELECT max(LIF_REMISE_POURCENT), max(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE;"
Q11_res = "Pourcent : 24, Montant : 58""

## Question 12
Q12_req = "Select FAC_ID from T_LIGNE_FACTURE where LIF_REMISE_POURCENT>0 or LIF_REMISE_MONTANT>0;"


## Question 13
Q13_req = "SELECT DISTINCT CLI_ID from T_FACTURE
JOIN T_LIGNE_FACTURE on T_LIGNE_FACTURE.FAC_ID=T_FACTURE.FAC_ID
where LIF_REMISE_POURCENT>0 or LIF_REMISE_MONTANT>0;

;"

## Question 14
Q14_req = "SELECT CLI_ID from T_FACTURE
except
SELECT DISTINCT CLI_ID from T_FACTURE
JOIN T_LIGNE_FACTURE on T_LIGNE_FACTURE.FAC_ID=T_FACTURE.FAC_ID
where LIF_REMISE_POURCENT>0 or LIF_REMISE_MONTANT>0;"


## Question 15
Q15_req = "select T_CLIENT.CLI_NOM, T_CLIENT.CLI_PRENOM, max(nbred) from (select T_FACTURE.CLI_ID, count(T_FACTURE.CLI_ID) as nbred from T_FACTURE join T_LIGNE_FACTURE on T_LIGNE_FACTURE.FAC_ID=T_FACTURE.FAC_ID
where LIF_REMISE_POURCENT>0 or LIF_REMISE_MONTANT>0 group by CLI_ID) as tout join T_CLIENT on T_client.CLI_ID=tout.CLI_ID;"
Q15_res ="nom: THOMASSE,prenom:Jean-Claude,montant : 20"
