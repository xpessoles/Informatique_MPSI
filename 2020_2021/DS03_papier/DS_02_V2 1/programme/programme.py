site = 'https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19/#_'
"https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675"

regions = [[11,'Ile de France'],[32,'Hauts de France'],[28,'Normandie'],[44,'Grand Est'],[53,'Bretagne'],[24,'Centre Val de Loire'],[27,'Bourgogne et Franche Comté'],[52,'Pays de Loire'],[75,'Nouvelle Aquitaine'],[84,'Auvergne et Rhône-Alpes'],[76,'Occitanie'],[93,'Provence-Alpes-Côte dAzur'],[94,'Corse'],[3,'Guyane'],[1,'Guadeloupe'],[2,'Martinique'],[4,'Réunion'],[6,'Mayotte'],[978,'Saint-Martin'],[977,'Saint-Barthelemy'],[975,'Saint-Pierre et Miquelon']]
regions = sorted(regions, key=lambda a_entry: a_entry[0])

file = "sp-pos-quot-reg-2020-11-08-19h15.csv"
import numpy as np
import matplotlib.pyplot as plt

fid = open(file,'r')
data = fid.readlines()
fid.close()
data = data[1:]
codes_regions=[]
liste_jours = []
nb_prelev_h = []
nb_cas_pos_h = []
nb_prelev_f = []
nb_cas_pos_f = []
cl_age = []
for ligne in data :
    ligne = ligne.strip()
    ligne = ligne.split(";")
    
    codes_regions.append(int(ligne[0]))
    liste_jours.append(ligne[1])
    nb_cas_pos_f.append(int(ligne[2]))
    nb_cas_pos_h.append(int(ligne[3]))
    nb_prelev_f.append(int(ligne[5]))
    nb_prelev_h.append(int(ligne[6]))
    cl_age.append(int(ligne[8]))
    

# Ecrire une fonction permettant de savoir si des tests ont été réalisés un jour donné.

def is_test(jours:list,jour:str) -> bool :
    for d in jours :
        if d == jour :
            return True
    return False

def is_test_while(jours:list,jour:str) -> bool :
    i = 0
    while i<len(jours): 
        if jours[i] == jour :
            return True
        i=i+1
    return False

print(is_test(liste_jours,"2020-05-13"))
print(is_test_while(liste_jours,"2020-05-13"))

# Ecrire une fonction permettant de retourner la liste des indices d'un jour donné 
def indices_jour(jours:list, jour:str) -> list :
    liste_indices = []
    for i in range(len(jours)):
        if jours[i] == jour :
            liste_indices.append(i)
    return liste_indices

# En utilisant la fonction définie précédemment, déterminer le nombres de personnes d'un sexe donné, testées un jour donné. 

def compte_test_jour(jours,jour,tests):
    liste_indices = indices_jour(jours, jour)
    nb_tests = 0
    for i in liste_indices : 
        nb_tests = nb_tests + tests[i]
    return nb_tests
     
# Donner l'instruction permettant de savoir combien d'hommes ont été testés le '2020-11-05'
compte_test_jour(liste_jours,'2020-11-05',nb_prelev_f)
compte_test_jour(liste_jours,'2020-11-05',nb_cas_pos_h)

# Réaliser une fonction permettant de faire la liste des jours
def  creer_liste_jours(jours):
    liste_jours = []
    for d in jours :
        if not(d in liste_jours) :
             liste_jours.append(d)
    return liste_jours

liste_j = creer_liste_jours(liste_jours)
    
# Realiser une fonction permettant de donner le nombre de tests par jours pour un sexe donné
def creer_liste_test(dates:list, tests:list) -> list :
    liste_j = creer_liste_jours(dates)
    res = []
    for jour in liste_j :
        res.append(compte_test_jour(dates,jour,tests))
    return res

liste_j = creer_liste_jours(liste_jours)
l_test_f = creer_liste_test(liste_jours,nb_prelev_f)
l_pos_f = creer_liste_test(liste_jours,nb_cas_pos_f)
 
#plt.plot(l_test_f)
#plt.plot(l_pos_f)
#plt.show()

# Realiser une fonction permettant de donner le nombre de tests par jour, tout sexe confondu

def nb_tests_jour(dates:list, tests1:list, tests2:list) -> list :
    nb_tests_h = creer_liste_test(dates,tests1)
    nb_tests_f = creer_liste_test(dates,tests2)
    
    nb_tests = [nb_tests_h[i]+nb_tests_f[i] for i in range(len(nb_tests_h))]
    return nb_tests
    
nb_test = nb_tests_jour(liste_jours,nb_prelev_h,nb_prelev_h)
nb_pos = nb_tests_jour(liste_jours,nb_cas_pos_h,nb_cas_pos_f)
"""
plt.plot(nb_test,label="Nombre de tests")
plt.plot(nb_pos,label="Nombre de cas positifs")
plt.xlabel('Jour')
plt.legend()
plt.show()
"""
# positivite tests
def positivite(tests,pos):
    res = [pos[i]/tests[i]*100 for i in range(len(tests))]
    return res

def moyenne_glissante(tests,nb):
    res = []
    for i in range(len(tests)-nb):
        s = 0
        for j in range(i,i+nb):
            s = s+tests[j]
        res.append(s/nb)
    return res
    
taux_pos = positivite(nb_test,nb_pos)
taux_pos_gl = moyenne_glissante(taux_pos,3)

plt.plot(taux_pos)
plt.plot(taux_pos_gl)
#plt.show()