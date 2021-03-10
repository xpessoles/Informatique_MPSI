NOM = "HATOUM"
Prenom = "RALPH"
Classe = "MPSI2"
alpha="10"

## Question 1
Q1_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_LIBELLE from T_CLIENT, T_titre where t_client.TIT_CODE = t_titre.TIT_CODE "

## Question 2
Q2_req = "SELECT count (*) from t_client"
Q2_res = "96"

## Question 3
Q3_req = "SELECT CLI_NOM, CLI_PRENOM from T_CLIENT, T_titre where t_client.TIT_CODE = t_titre.TIT_CODE and t_titre.TIT_LIBELLE='Madame'"

## Question 4
Q4_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_LIBELLE  from T_CLIENT, T_titre where t_client.TIT_CODE = t_titre.TIT_CODE and ( t_titre.TIT_LIBELLE='Madame' or t_titre.TIT_LIBELLE='Mademoiselle')"


## Question 5
Q5_req = "SELECT count(*) from ( SELECT CLI_NOM, CLI_PRENOM, TIT_LIBELLE  from T_CLIENT, T_titre where t_client.TIT_CODE = t_titre.TIT_CODE and ( t_titre.TIT_LIBELLE='Madame' or t_titre.TIT_LIBELLE='Mademoiselle') )"
Q5_res = "17"

## Question 6
Q6_req = "SELECT CLI_NOM as 'Noms', CLI_PRENOM as 'Prénoms' from T_CLIENT, T_titre where t_client.TIT_CODE = t_titre.TIT_CODE and ( t_titre.TIT_LIBELLE='Madame' or t_titre.TIT_LIBELLE='Mademoiselle') order by CLI_NOM asc "


## Question 7
Q7_req = "SELECT CLI_NOM, TEL_NUMERO from T_CLIENT, T_TELEPHONE where T_TELEPHONE.CLI_ID = T_CLIENT.CLI_ID"

## Question 8
Q8_req = "SELECT CLI_NOM, CLI_PRENOM  from (SELECT CLI_NOM, CLI_PRENOM, count(*) as nb from T_CLIENT group by CLI_NOM) where nb > 1 ;"

## Question 9
Q9_req = "SELECT CLI_NOM, nb  from (SELECT CLI_NOM, CLI_PRENOM, count(*) as nb from T_CLIENT group by CLI_NOM) where nb > 1 ;"
Q9_res = "BENATTAR 2, MARTIN 3"

## Question 10
Q10_req = "SELECT sum(LIF_remise_pourcent)/count(lif_remise_pourcent), sum(lif_remise_montant)/count(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE "
Q10_res = "25 59"

## Question 11
Q11_req = "SELECT max(LIF_REMISE_POURCENT), max(LIF_REMISE_MONTANT) from T_LIGNE_FACTURE "
Q11_res = "25 59"

## Question 12
Q12_req = "select DISTINCT FAC_ID as fac_id1 from T_LIGNE_FACTURE where (LIF_REMISE_MONTANT is not NULL or LIF_REMISE_MONTANT is not NULL)"


## Question 13
Q13_req = "select distinct CLI_ID from T_FACTURE join (select DISTINCT FAC_ID as fac_id1 from T_LIGNE_FACTURE where (LIF_REMISE_MONTANT is not NULL or LIF_REMISE_MONTANT is not NULL)) on T_FACTURE.FAC_ID = fac_id1"

## Question 14
Q14_req = ""


## Question 15
Q15_req = ""
Q15_res ="nom,prenom,montant"
