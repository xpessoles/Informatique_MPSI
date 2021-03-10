NOM = "bonnefoy"
Prenom = "léo"
Classe = "mpsi2"
alpha="12"

## Question 1
Q1_req = "select TIT_CODE,CLI_NOM,CLI_PRENOM from T_CLIENT"

## Question 2
Q2_req = "select count(*) from T_CLIENT"
Q2_res = "97"

## Question 3
Q3_req = "select CLI_NOM,CLI_PRENOM from T_CLIENT where TIT_CODE='Mme.'"

## Question 4
Q4_req = "select TIT_CODE,CLI_NOM,CLI_PRENOM from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.'"


## Question 5
Q5_req = "select count(*) from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.'"
Q5_res = "17"

## Question 6
Q6_req = "select CLI_NOM as Noms,CLI_PRENOM  as Prenoms from T_CLIENT where TIT_CODE='Mme.' or TIT_CODE='Melle.' group by Noms"


## Question 7
Q7_req = "select CLI_NOM as Noms,TEL_NUMERO as nb_telephone from T_CLIENT,T_TELEPHONE where T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID"

## Question 8
Q8_req = "select CLI_NOM as Noms from T_CLIENT group by CLI_NOM having count(Noms)>1"

## Question 9
Q9_req = "select count(*) from ( select CLI_NOM as Noms from T_CLIENT group by CLI_NOM having count(Noms)>1)"
Q9_res = "2select avg(LIF_REMISE_POURCENT) as val_moyenne_remise , avg(LIF_REMISE_MONTANT) as val_moyenne_montant from T_LIGNE_FACTURE"

## Question 10
Q10_req = "select avg(LIF_REMISE_POURCENT) as val_moyenne_remise , avg(LIF_REMISE_MONTANT) as val_moyenne_montant from T_LIGNE_FACTURE"
Q10_res = "27 et 61"

## Question 11
Q11_req = "select max(LIF_REMISE_POURCENT) as val_max_remise , max(LIF_REMISE_MONTANT) as val_max_montant from T_LIGNE_FACTURE"
Q11_res = "27 et 61"

## Question 12
Q12_req = "select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_POURCENT<>'NULL' or LIF_REMISE_MONTANT <> 'NULL'"


## Question 13
Q13_req = "select  CLI_ID from T_FACTURE,(select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_POURCENT<>'NULL' or LIF_REMISE_MONTANT <> 'NULL')where fac_id1=FAC_ID "

## Question 14
Q14_req = "select  CLI_ID from T_FACTURE,(select FAC_ID as fac_id2 from T_LIGNE_FACTURE EXCEPT select FAC_ID as fac_id1 from T_LIGNE_FACTURE where LIF_REMISE_POURCENT<>'NULL' or LIF_REMISE_MONTANT <> 'NULL') where fac_id2=FAC_ID"


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
