from prog import *
import sqlite3
#from DS08_corrige import *

def convert(i):
    if int(i)<10:
        return '0'+i
    else:
        return i

def renvoie_res_requete(req):
    resultat=requete (req)
    if len(resultat)>1:
        return resultat
    else:
        resultat=resultat[0]
        if len(resultat)==1:
            return resultat[0]
        else:
            return resultat

def requete (req):
    conn = sqlite3.connect('../../bdd/hotel_'+convert(alpha)+'.db')
    c=conn.cursor()
    c.execute(req)
    rep = c.fetchall()
    conn.close()
    return rep


## Question 1
sol_Q1_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT"

## Question 2
sol_Q2_req = "SELECT COUNT(*) FROM T_CLIENT ;"
sol_Q2_res = str(renvoie_res_requete(sol_Q2_req))

## Question 3
sol_Q3_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE='Mme.'"

## Question 4
sol_Q4_req = "SELECT CLI_NOM, CLI_PRENOM, TIT_CODE FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.'"


## Question 5
sol_Q5_req = "SELECT count(*) FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.'"
#sol_Q5_res = "17"
sol_Q5_res = str(renvoie_res_requete(sol_Q5_req))

## Question 6
sol_Q6_req = "SELECT CLI_NOM as noms, CLI_PRENOM as prenoms FROM T_CLIENT WHERE TIT_CODE='Mme.' OR TIT_CODE='Melle.' ORDER BY noms, prenoms"


## Question 7
sol_Q7_req = "SELECT T_CLIENT.CLI_NOM, T_TELEPHONE.TEL_NUMERO FROM T_CLIENT JOIN T_TELEPHONE ON T_CLIENT.CLI_ID=T_TELEPHONE.CLI_ID"

## Question 8
sol_Q8_req = "SELECT NOM FROM (SELECT CLI_NOM as Nom, CLI_PRENOM as prenom, COUNT(*) as nb_nom FROM T_CLIENT GROUP BY Nom) WHERE nb_nom>1"

## Question 9
sol_Q9_req = "SELECT * FROM(SELECT CLI_NOM,COUNT(CLI_NOM) AS ct FROM T_CLIENT GROUP BY CLI_NOM ORDER BY CLI_NOM) WHERE ct>1"
#sol_Q9_res = "BENATTAR : 2, MARTIN : 3"
sol_Q9_res = str(renvoie_res_requete(sol_Q9_req))

## Question 10
sol_Q10_req = " SELECT AVG(LIF_REMISE_MONTANT),  AVG(LIF_REMISE_POURCENT) FROM T_LIGNE_FACTURE"
#sol_Q10_res = "Montant : 50, pourcent : 15"
sol_Q10_res = str(renvoie_res_requete(sol_Q10_req))

## Question 11
sol_Q11_req = " SELECT MAX(LIF_REMISE_MONTANT),  AVG(LIF_REMISE_POURCENT) FROM T_LIGNE_FACTURE"
#sol_Q11_res = "Montant : 50, pourcent : 15"
sol_Q11_res = str(renvoie_res_requete(sol_Q11_req))

## Question 12
sol_Q12_req = "SELECT FAC_ID FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0"


## Question 13
sol_Q13_req = "SELECT DISTINCT CLI_ID FROM T_FACTURE JOIN (SELECT T_LIGNE_FACTURE.FAC_ID as facid1  FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0) ON facid1=T_FACTURE.FAC_ID"

## Question 14
sol_Q14_req = "SELECT CLI_ID FROM T_CLIENT EXCEPT SELECT DISTINCT CLI_ID FROM T_FACTURE JOIN (SELECT T_LIGNE_FACTURE.FAC_ID as facid1  FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0) ON facid1=T_FACTURE.FAC_ID"


## Question 15
sol_Q15_req = "SELECT T_CLIENT.CLI_NOM, T_CLIENT.CLI_PRENOM, max(montant_total) FROM T_CLIENT JOIN (SELECT CLI_ID as id_client, sum(montant) as montant_total FROM T_FACTURE JOIN (SELECT T_LIGNE_FACTURE.FAC_ID as facid1,  T_LIGNE_FACTURE.LIF_REMISE_MONTANT as montant FROM T_LIGNE_FACTURE WHERE LIF_REMISE_POURCENT>0 OR LIF_REMISE_MONTANT>0)ON facid1=T_FACTURE.FAC_ID GROUP BY CLI_ID) ON T_CLIENT.CLI_ID=id_client;"
#sol_Q15_res ="Medard,Jacques,600"
sol_Q15_res = str(renvoie_res_requete(sol_Q15_req))

def test_Q1_req ():
    assert requete(sol_Q1_req) == requete(Q1_req)

def test_Q2_res ():
    assert sol_Q2_res.upper() ==  Q2_res.upper()

def test_Q2_req ():
    assert requete(sol_Q2_req) == requete(Q2_req)

def test_Q3_req ():
    assert requete(sol_Q3_req) == requete(Q3_req)

def test_Q4_req ():
    assert requete(sol_Q4_req) == requete(Q4_req)

def test_Q5_res ():
    assert sol_Q5_res.upper() ==  Q5_res.upper()

def test_Q5_req ():
    assert requete(sol_Q5_req) == requete(Q5_req)

def test_Q6_req ():
    assert requete(sol_Q6_req) == requete(Q6_req)

def test_Q7_req ():
    assert requete(sol_Q7_req) == requete(Q7_req)

def test_Q8_req ():
    assert requete(sol_Q8_req) == requete(Q8_req)

def test_Q9_req ():
    assert requete(sol_Q9_req) == requete(Q9_req)

def test_Q10_res ():
    assert sol_Q10_res.upper() ==  Q10_res.upper()

def test_Q10_req ():
    assert requete(sol_Q10_req) == requete(Q10_req)

def test_Q11_res ():
    assert sol_Q11_res.upper() ==  Q11_res.upper()

def test_Q11_req ():
    assert requete(sol_Q11_req) == requete(Q11_req)

def test_Q12_req ():
    assert requete(sol_Q12_req) == requete(Q12_req)

def test_Q13_req ():
    assert requete(sol_Q13_req) == requete(Q13_req)

def test_Q14_req ():
    assert requete(sol_Q14_req) == requete(Q14_req)

def test_Q15_res ():
    assert sol_Q15_res.upper() ==  Q15_res.upper()

def test_Q15_req ():
    assert requete(sol_Q15_req) == requete(Q15_req)