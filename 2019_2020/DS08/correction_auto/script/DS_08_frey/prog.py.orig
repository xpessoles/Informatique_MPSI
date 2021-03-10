NOM = "FREY"
Prenom = "Elsa"
Classe = "MPSI2"
alpha="04"

## Question 1
Q1_req = "Select Distinct CLI_NOM, CLI_PRENOM,TIT_CODE
from T_CLIENT;"

## Question 2
Q2_req = "Select Count(*)
from T_CLIENT;"
Q2_res = "97"

## Question 3
Q3_req = "Select CLI_NOM, CLI_PRENOM
from T_CLIENT
Where TIT_CODE='Mme.';"

## Question 4
Q4_req = "Select CLI_NOM, CLI_PRENOM, TIT_CODE
from T_CLIENT
Where TIT_CODE='Melle.' or TIT_CODE='Mme.';"


## Question 5
Q5_req = "Select Count(*)
from T_CLIENT
Where TIT_CODE='Melle.' or TIT_CODE='Mme.';"
Q5_res = "17"

## Question 6
Q6_req = "
Select CLI_NOM AS Noms , CLI_PRENOM as Prénoms
from T_CLIENT
Where TIT_CODE='Melle.' or TIT_CODE='Mme.'
Order by Noms ASC, Prénoms asc;"


## Question 7
Q7_req = "Select T_CLIENT.CLI_NOM as Noms, T_TELEPHONE.TEL_NUMERO as num_tel
from T_CLIENT, T_TELEPHONE
Where T_CLIENT.CLI_ID=T_TELEPHONE.TEL_ID;"

## Question 8
Q8_req = "SELECT   CLI_NOM, CLI_PRENOM
FROM     T_CLIENT
Where CLI_NOM='BENATTAR' or CLI_NOM='MARTIN';"

## Question 9
Q9_req = "SELECT   COUNT(*) AS nbr_doublon, CLI_NOM
FROM     T_CLIENT
GROUP BY CLI_NOM
HAVING   COUNT(*) > 1;"
Q9_res = "Benattar:2
Martin:3"

## Question 10
Q10_req = "Select AVG(LIF_REMISE_POURCENT),AVG(LIF_REMISE_MONTANT)
from T_LIGNE_FACTURE;
"
Q10_res = "19.0 ; 53.0"

## Question 11
Q11_req = "
Select MAX(LIF_REMISE_POURCENT),MAX(LIF_REMISE_MONTANT)
from T_LIGNE_FACTURE;"
Q11_res = "19 ; 53"

## Question 12
Q12_req = "Select distinct FAC_ID as fac_id1
from T_LIGNE_FACTURE
Where LIF_REMISE_MONTANT not null or LIF_REMISE_POURCENT not null;"


## Question 13
Q13_req = "Select distinct CLI_ID
from T_FACTURE
Union
Select distinct FAC_ID as fac_id1
from T_LIGNE_FACTURE
Where LIF_REMISE_MONTANT not null or LIF_REMISE_POURCENT not null;"

## Question 14
Q14_req = "Select distinct CLI_ID
from T_FACTURE
Except
Select distinct FAC_ID as fac_id1
from T_LIGNE_FACTURE
Where LIF_REMISE_MONTANT not null or LIF_REMISE_POURCENT not null;"


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
