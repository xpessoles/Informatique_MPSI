#!/usr/bin/python3

"""Calcule les solutions du DS
   Usage :

   python3 generateur.py p q

   écrit sur la sortie standard un csv (séparateur : ";") pour les
   valeurs du paramètre alpha dans range(p, q). L'entête comporte les
   numéros des questions, la valeur de alpha est en première colonne."""

import ds5_accelero as cor
from math import log
import numpy as np
import pdb
import matplotlib.pyplot as plt

#alpha = 98


def lire_accelero(fichier):
    with open(fichier,'r',encoding='utf8') as f:
        data=f.readlines()
        dT,X,Y,Z=[],[],[],[]
        for ligne in data:
            dt,x,y,z=ligne.split(',')
            dT.append(int(dt))
            X.append(int(x))
            Y.append(int(y))
            Z.append(int(z))
    return dT,X,Y,Z

def corrige(alpha_sol):
    """Produit un tableau t contenant les valeurs attendues pour le DS,
        en fontion du paramètre alpha.
        t[0] contient la valeur de alpha et t[i] pour i=1, ..., 18
        contient la valeur attendue pour la question i."""
    sol = [alpha_sol]





    #Qu 1
    dT,X,Y,Z=lire_accelero('mesure_accelero_'+str(alpha_sol)+'.txt')
    Q1=len(dT)
    sol.append(Q1)

    #Q2
    def calculer_temps(dT):
        T=[0]
        for dt in dT[1:]:
            T.append(T[-1]+dt*1e-6)
        return T
    T=  calculer_temps(dT)
    sol.append(T[-1])

    plt.clf()
    plt.plot(T)
    plt.savefig('courbes_corrigees/q02_'+str(alpha_sol)+'.png')

    #Q3
    def calculer_acceleration(X,Y,Z):
        AX,AY,AZ=[],[],[]
        for i in range(len(X)):
            AX.append(X[i]*10/255)
            AY.append(Y[i]*10/255)
            AZ.append(Z[i]*10/255)
        return AX,AY,AZ

    AX,AY,AZ=calculer_acceleration(X,Y,Z)


    sol.append(max(AX))
    sol.append(max(AY))
    sol.append(max(AZ))

    #Q04
    plt.clf()
    plt.plot(T,AX,'r',label='$a_x$')
    plt.plot(T,AY,'g',label='$a_y$')
    plt.plot(T,AZ,'b',label='$a_z$')
    plt.legend()
    plt.xlabel('temps en $\\mu s$')
    plt.ylabel('accélération en $m/s^2$')
    plt.savefig('courbes_corrigees/q04_'+str(alpha_sol)+'.png')

    #Q05
    def trapeze(A):
        V=[0]
        for i in range(1,len(A)):
            V.append(V[-1]+0.5*(A[i-1]+A[i]))
        return V

    VX=trapeze(AX)
    VY=trapeze(AY)
    VZ=trapeze(AZ)


    plt.clf()
    plt.plot(T,VX,'r',label='$v_x$')
    plt.plot(T,VY,'g',label='$v_y$')
    plt.plot(T,VZ,'b',label='$v_z$')
    plt.legend()
    plt.xlabel('temps en $\\mu s$')
    plt.ylabel('vitesse en $m/s$')
    plt.savefig('courbes_corrigees/q05_'+str(alpha_sol)+'.png')


    #Q06
    sol.append(max(VX))
    sol.append(max(VY))
    sol.append(max(VZ))

    #Q07
    def moyenne(A,T,tmax):
        i=0
        t=T[0]
        m=A[0]
        while t<tmax:
            i+=1
            m+=A[i]
            t=T[i]
        return m/(i+1)

    mX1=moyenne(AX,T,2)
    mY1=moyenne(AY,T,2)
    mZ1=moyenne(AZ,T,2)

    sol.append(mX1)
    sol.append(mY1)
    sol.append(mZ1)

    #Q08
    AX1=[ax-mX1 for ax in AX]
    AY1=[ay-mY1 for ay in AY]
    AZ1=[az-mZ1 for az in AZ]

    sol.append(max(AX1))
    sol.append(max(AY1))
    sol.append(max(AZ1))

    #Q09
    VX1=trapeze(AX1)
    VY1=trapeze(AY1)
    VZ1=trapeze(AZ1)
    sol.append(max(VX1))
    sol.append(max(VY1))
    sol.append(max(VZ1))

    #Q10
    plt.clf()
    plt.plot(T,VX1,'r',label='$v_x$')
    plt.plot(T,VY1,'g',label='$v_y$')
    plt.plot(T,VZ1,'b',label='$v_z$')
    plt.legend()
    plt.xlabel('temps en $\\mu s$')
    plt.ylabel('vitesse en $m/s$')
    plt.savefig('courbes_corrigees/q10_'+str(alpha_sol)+'.png')

    #Q11
    X1=trapeze(VX1)
    Y1=trapeze(VY1)
    Z1=trapeze(VZ1)

    sol.append(max(X1))
    sol.append(max(Y1))
    sol.append(max(Z1))

    #Q12
    plt.clf()
    plt.plot(X1,Y1)
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.savefig('courbes_corrigees/q12_'+str(alpha_sol)+'.png')

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
    print(';'.join(convv(v) for v in l))

def renvoie_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    return(';'.join(convv(v) for v in l))



from sys import argv

def main():
  #alphas=range(int(argv[1]),int(argv[2]))
  alphas=range(1,99)
  t = ['0','Q1','Q2','$Q3 : a^{max}_x$','$Q3 : a^{max}_y$','$Q3 : a^{max}_z$','$Q6 : v^{max}_x$','$Q6 : v^{max}_y$','$Q6 : v^{max}_z$','$Q7 : v^{moy}_x$','$Q7 : v^{moy}_y$','$Q7 : v^{moy}_z$','$Q8 : a^{max}_x$','$Q8 : a^{max}_y$','$Q8 : a^{max}_z$','$Q9 : v^{max}_x$','$Q9 : v^{max}_y$','$Q9 : v^{max}_z$','$Q11 : x^{max}$','$Q11 : y^{max}$','$Q11 : z^{max}$']
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
    #fichier_resultats='DS5_machine_ipt_2020_2021.csv'
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

fichier_resultats0='DS5_machine_ipt_2020_2021.csv'
remplacer_dans_fichier(fichier_resultats0,fichier_resultats0.split('.csv')[0]+'2.csv','","','";"')
#
fichier_resultats=fichier_resultats0.split('.csv')[0]+'2.csv'

erreur=1e-2
erreur1=1e-2
erreur2=1e-2
#pdb.set_trace()
notes,coeffs,titre_questions,notes_valeurs=generer_note(fichier_resultats,erreur1,erreur2)


file='Notes_DS5_machine_ipt_2020_2021.csv'
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
