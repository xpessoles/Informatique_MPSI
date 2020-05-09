import sqlite3
conn = sqlite3.connect('veekun-pokedex.sqlite')
#c = conn.cursor()

"""
for i in range(1,25):
    print("## Question "+str(i))
    print("sol_Q"+str(i)+'_req = ""')
    print("sol_Q"+str(i)+'_res = ""')
    print("")
"""
    
## Question 1
sol_Q1_res = 172

## Question 2
sol_Q2_res = 'pokemon(id : integer, identifier : string, species_id : integer, height : integer, weight : integer, base_experience : integer, order : integer, is_default : boolean)'

## Question 3
sol_Q3_res = "La clé primaire d'une table est une contrainte d'unicité, composée d'une ou plusieurs colonnes et qui permet d'identifier de manière unique chaque ligne de la table."

## Question 4
sol_Q4_req = "SELECT height FROM pokemon WHERE identifier = 'pikachu';"
sol_Q4_res = "4"

## Question 5
sol_Q5_req = "SELECT weight FROM pokemon WHERE identifier = 'pikachu';"
sol_Q5_res = "60"

## Question 6
sol_Q6_req = "SELECT identifier FROM pokemon WHERE height> 4;"

## Question 7
sol_Q7_req = "SELECT identifier FROM pokemon WHERE height > (SELECT height FROM pokemon WHERE identifier = 'pikachu');"

## Question 8
sol_Q8_req = "SELECT count(*) FROM pokemon WHERE height > (SELECT height FROM pokemon WHERE identifier = 'pikachu');"
sol_Q8_res = "678"

## Question 9
sol_Q9_req = "SELECT count(*) FROM pokemon WHERE height = (SELECT height FROM pokemon WHERE identifier = 'pikachu');"
sol_Q9_res = "63"

## Question 10
sol_Q10_req = "SELECT identifier,max(weight) FROM pokemon WHERE height = (SELECT height FROM pokemon WHERE identifier = 'pikachu');"
sol_Q10_res = "nom,poids"

## Question 11
sol_Q11_req = ""
sol_Q11_res = ""

## Question 12
sol_Q12_req = ""
sol_Q12_res = ""

## Question 13
sol_Q13_req = ""
sol_Q13_res = ""
## Question 14
sol_Q14_req = ""
sol_Q14_res = ""
## Question 15
sol_Q15_req = ""
sol_Q15_res = ""
## Question 16
sol_Q16_req = ""
sol_Q16_res = ""
## Question 17
sol_Q17_req = ""
sol_Q17_res = ""
## Question 18
sol_Q18_req = ""
sol_Q18_res = ""
## Question 19
sol_Q19_req = ""
sol_Q19_res = ""
## Question 20
sol_Q20_req = ""
sol_Q20_res = ""
## Question 21
sol_Q21_req = ""
sol_Q21_res = ""
## Question 22
sol_Q22_req = ""
sol_Q22_res = ""
## Question 23
sol_Q23_req = ""
sol_Q23_res = ""
## Question 24
sol_Q24_req = ""
sol_Q24_res = ""