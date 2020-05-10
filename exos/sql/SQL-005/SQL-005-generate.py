import sqlite3
#c = conn.cursor()

from SQL_005_corr import *
from SQL_005_eleve import *

def test_egalite(sol,el):
    if sol == el :
        return 1
    else :
        return 0
        

def test_requete (sol,el):
    conn = sqlite3.connect('veekun-pokedex.sqlite')
    c=conn.cursor()
    c.execute(sol)
    sol_sql = c.fetchall()
    c.execute(el)
    el_sql = c.fetchall()
    conn.close()
    if sol_sql == el_sql :
        return 1
    else : 
        return 0
    
def go():
    res_tp = [NOM]
    res_tp.append(test_egalite(sol_Q1_res,Q1_res))
    
    res_tp.append(test_requete(sol_Q4_req,Q4_req))
    res_tp.append(test_egalite(sol_Q4_res,Q4_res))
    return res_tp

res = go()
print(res)