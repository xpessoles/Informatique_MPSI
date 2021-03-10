#!/usr/bin/python3

"""Calcule les solutions du DS
   Usage :

   python3 generateur.py p q

   écrit sur la sortie standard un csv (séparateur : ";") pour les
   valeurs du paramètre alpha dans range(p, q). L'entête comporte les
   numéros des questions, la valeur de alpha est en première colonne."""

import corrige_d02S as cor
from math import log
import numpy as np
import pdb

#alpha = 98

def corrige(alpha_sol):
    """Produit un tableau t contenant les valeurs attendues pour le DS,
        en fontion du paramètre alpha.
        t[0] contient la valeur de alpha et t[i] pour i=1, ..., 18
        contient la valeur attendue pour la question i."""
    sol = [alpha_sol]
    def calcule_u(n):
        u=alpha_sol+1
        for k in range(n):
            u+=log(u)
        return u



    def u_depasse(alpha_sol):
        u=alpha_sol+1
        n=0
        while u<=10+alpha_sol:
            u+=log(u)
            n+=1
        return n


    def calcule_su(n):
        u=alpha_sol+1
        S=0
        for k in range(n):
            u+=log(u)
            S+=u
        return S
    #Qu 1
    Q1=calcule_u(alpha_sol+100)
    sol.append(Q1)

    Q2=calcule_u(alpha_sol+50)
    sol.append(Q2%3)

    Q3=u_depasse(alpha_sol)
    sol.append(Q3)

    Q4=calcule_su(10000+alpha_sol)
    sol.append(Q4)
    alt=cor.generer_altitude(alpha_sol)
    sol.append(len(alt))
    Q6=cor.altmax(alt)
    sol.append(Q6)

    Q78=cor.denivmax(alt)
    sol.append(Q78[0])
    sol.append(Q78[1])

    Q9=cor.denivtotal(alt)
    sol.append(Q9)
    Q10=len(cor.sommets(alt))
    sol.append(Q10)
    return sol

def convv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 3 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.3f}".format(v)
    return str(v)

def conv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 5 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.5f}".format(v)
    return str(v)

def print_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    print(';'.join(conv(v) for v in l))

def renvoie_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    return(';'.join(conv(v) for v in l))



from sys import argv

def main():
  #alphas=range(int(argv[1]),int(argv[2]))
  alphas=range(1,99)
  t = list(range(11))
  t[0] = 'alpha'
  print_line(t)
  tableau_tex='\\begin{longtable}{|'+len(t)*'c|'+'} \n '
  with open('reponses.csv','w') as f0:
    line=renvoie_line(t)
    tableau_tex+='\\textbf{'+line.replace(';','}&\\textbf{')+'}\\endhead \n\\hline \n'
    f0.write(line+'\n')
    for a in alphas:
        line=corrige(a)

        print_line(line)
        f0.write(renvoie_line(corrige(a)))
        tableau_tex+=renvoie_line(corrige(a)).replace(';','&')+'\\\\ \n\\hline \n'
        f0.write('\n')
    tableau_tex+='\\end{longtable}\n'
    #print(tableau_tex)
    with open('reponses.tex','w',encoding='utf8') as f1:
        f1.write(tableau_tex)
  # for a in alphas:
  #   print_line(corrige(a))

# if __name__ == "__main__":
#    main()


def generer_note(fichier_resultats,erreur1,erreur2):
    #fichier_resultats='DS6_reponses0.csv'
    with open(fichier_resultats,'r',encoding='utf8') as f:
        data=f.readlines()
    notes=[]
    notes_valeurs=[]
    titre_questions=data[0].strip().split(';')[4:]
    for ligne in data[1:]:
        ligne=ligne.strip().split(';')
        #print(ligne)
        alpha=int(ligne[1][1:-1])
        nom=ligne[2][1:-1]
        classe=ligne[4][1:-1]
        if '1' in classe:
            erreur=erreur1
        else:
            erreur=erreur2
        note=[nom,classe]
        note_valeurs=note.copy()
        bonnes_reponses=corrige(alpha)[1:]
        # bonnes_reponses=corrige(alpha)[1:5]
        # bonnes_reponses+=[corrige(alpha)[5][0]]
        # bonnes_reponses+=[corrige(alpha)[5][1]]
        # bonnes_reponses+=[corrige(alpha)[5][2]]
        # bonnes_reponses+=corrige(alpha)[6:]
        for x in bonnes_reponses:
            note_valeurs.append(conv(x))
        for i,x in enumerate(bonnes_reponses):
            #print(type(x),x,i)
            for j,reponse in enumerate(ligne[5:]):
                car1=''
                for car in reponse:
                    #print(car,car.isnumeric())
                    if car.isnumeric() or car=='.' or car=='[' or car==']' or car==',':
                        car1+=car
                #print(ligne,car1)
                ligne[5+j]=car1
            #pdb.set_trace()
            if ligne[5+i]=="" or ('[' in ligne[5+i] and (type(x)!=np.ndarray or type(x)!=list)):
                note.append(0)
                #res='0'
            elif type(x)==np.ndarray or type(x)==list:
                # if 'ADAMCZAK' in nom.upper():
                #     pdb.set_trace()
                res=ligne[5+i]
                note.append(int(str(x.tolist()).replace(' ','') in res or str(x.tolist()).replace(' ','') in res.replace(' ','') or str(x) in res or str(x).replace(' ',',') in res))
            elif type(x)==int:
                res=float(ligne[5+i])
                note.append(int(x==res))
            elif type(x)==float or type(x)==np.float64:
                res=ligne[5+i]
                if ',' in res:
                    res=float(res.replace(',','.'))
                # elif '^' in res:
                #     res=float(res.replace('^','**'))
                else:
                    try:
                        float(res)
                    except:
                        res=x+1
                    res=float(res)
                note.append(int(abs(x-res)<=erreur))
            else:
                res=float(ligne[4+i][1:-1])
                note.append(int(abs(x-res)<=erreur))
            note_valeurs.append(res)
        coeffs=(len(note)-2)*[1]
        note_globale=np.dot(np.array(note[2:]),np.array(coeffs))*20/sum(coeffs)
        note.append(note_globale)
        notes.append(note)
        notes_valeurs.append(note_valeurs)
    return notes,coeffs,titre_questions,notes_valeurs




# def exporter_notes(notes,file,delimiter):
#

def remplacer_dans_fichier(fichier0,fichier,carac0,carac1):
  with open(fichier0,'r',encoding='utf-8') as f:
    texte0=f.read()
    texte=texte0.replace(carac0,carac1)
  with open(fichier,'w',encoding='utf-8') as f:
    f.write(texte)

fichier_resultats0='DS2_machine_ipt_2020_2021.csv'
remplacer_dans_fichier(fichier_resultats0,fichier_resultats0.split('.csv')[0]+'2.csv','","','";"')
#
fichier_resultats=fichier_resultats0.split('.csv')[0]+'2.csv'

erreur=1e-4
erreur1=1e-5
erreur2=1e-5
notes,coeffs,titre_questions,notes_valeurs=generer_note(fichier_resultats,erreur1,erreur2)


file='Notes_DS2_machine_ipt_2020_2021.csv'
file_valeurs=file.split('.csv')[0]+'_valeurs.csv'

with open(file,'w',encoding='utf-8') as f:
    f.write(renvoie_line(titre_questions)+'\n')
    f.write(renvoie_line(coeffs)+'\n')
    for note in notes:
        f.write(renvoie_line(note)+'\n')


with open(file_valeurs,'w',encoding='utf-8') as f:
    for note in notes_valeurs:
        f.write(renvoie_line(note)+'\n')
        #for i,x in enumerate(note):

            # if i==len(note)-1:
            #     ligne+=str(x)+'\n'
            # else:
            #     ligne+=str(x)+';'
        #print(ligne)
    #f.write(ligne)
