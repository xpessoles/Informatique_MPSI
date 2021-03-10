import pytest
import sqlite3


from DS08_corrige import *
#from SQL_005_eleve import *
#from SQL_005_eleve_durif import *
#from DS_08_abid import *


def generate_test(nb):
    for n in range(1,nb+1):
        if n in [2,5,10,11,15]:
            print("def test_Q"+str(n)+"_res ():")
            print("    assert sol_Q"+str(n)+"_res.upper() ==  Q"+str(n)+"_res.upper()")
            print()
        print("def test_Q"+str(n)+"_req ():")
        print("    assert requete(sol_Q"+str(n)+"_req) == requete(Q"+str(n)+"_req)")
        print()


generate_test(15)



def generate_go(nb):
    for n in range(1,nb+1):
        print("test_Q"+str(n)+"_res ()")
        print("test_Q"+str(n)+"_req ()")


def requete (req):
    conn = sqlite3.connect('veekun-pokedex.sqlite')
    c=conn.cursor()
    c.execute(req)
    rep = c.fetchall()
    conn.close()
    return rep




def go():
    test_Q1_req ()
    test_Q2_res ()
    test_Q2_req ()
    test_Q3_req ()
    #test_Q4_res ()
    test_Q4_req ()
    test_Q5_res ()
    test_Q5_req ()
    #test_Q6_res ()
    test_Q6_req ()
    #test_Q7_res ()
    test_Q7_req ()
    #test_Q8_res ()
    test_Q8_req ()
    #test_Q9_res ()
    test_Q9_req ()
    test_Q10_res ()
    test_Q10_req ()
    #test_Q11_res ()
    test_Q11_req ()
    #test_Q12_res ()
    test_Q12_req ()
    #test_Q13_res ()
    test_Q13_req ()
    #test_Q14_res ()
    test_Q14_req ()
    test_Q15_res ()
    test_Q15_req ()
