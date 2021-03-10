#!/usr/bin/python3

"""Calcule les solutions du DS (

   python3 generateur.py p q

   écrit sur la sortie standard un csv (séparateur : ";") pour les
   valeurs du paramètre alpha dans range(p, q). L'entête comporte les
   numéros des questions, la valeur de alpha est en première colonne."""

from ds6_corrige import *
import pdb
from numpy import array



def conv(x, n):
    return int((x*n) // m) # on reconvertit en "petit" entier si possible

#
# alpha = 16

def corrige(alpha):
    """Produit un tableau t contenant les valeurs attendues pour le DS,
        en fontion du paramètre alpha.
        t[0] contient la valeur de alpha et t[i] pour i=1, ..., 18
        contient la valeur attendue pour la question i."""
    L=alpha
    m=1+0.01*alpha
    theta0=np.pi/(4*alpha)
    g=9.81
    sol = [alpha]
    #Q1
    T0=np.sqrt(L/g)*2*np.pi
    sol.append(T0)
    # Qu. 2 :
    #pdb.set_trace()
    def f(x):
        return 4/np.sqrt(2*g/L*(np.cos(x)-np.cos(theta0)))
    Tg=rect_gauche(f,0,theta0,100)
    Td=rect_droit(f,0,theta0-theta0/1000,100)
    Tt=trapeze(f,0,theta0-theta0/1000,100)
    sol.append(Tg)
    # Qu. 3 :
    sol.append(Td)
    # Qu. 4 :
    sol.append(Tt)
    # Qu. 5 :
    # sol.append(abs(rect_gauche(f,0,theta0,100)-T0))
    # sol.append(abs(rect_droit(f,0,theta0-theta0/1000,100)-T0))
    # sol.append(abs(trapeze(f,0,theta0-theta0/1000,100)-T0))
    sol.append((float(convv(abs(Tg-T0))),float(convv(abs(Td-T0))),float(convv(abs(Tt-T0)))))
    X0=np.array([100+alpha,300+alpha])
    t=np.linspace(0,38,100)
    def F(X,t):
        vc = 8
        vm = 1.5 + alpha/100
        x,y=X
        xp  = vc *(vm*t-x)/np.sqrt((vm*t-x)**2+y*y)
        yp  = vc *(-y)/np.sqrt((vm*t-x)**2+y*y)
        return np.array([xp,yp])
    t_list, X_list=euler(F,0,38,X0,38/100)
    X=[x[0] for x in X_list]
    Y=[x[1] for x in X_list]
    # Qu. 6 :
    sol.append(X0)
    # Qu. 7 :
    sol.append(X[-1])
    # Qu. 8 :
    sol.append(Y[-1])
    return sol


def conv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 5 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.5f}".format(v)
    return str(v)

def convv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 3 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.3f}".format(v)
    return str(v)

def print_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    print(';'.join(convv(v) for v in l))

def renvoie_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    return(';'.join(convv(v) for v in l))



from sys import argv

def main():
  alphas=list(range(1,100))
  t = list(range(8))
  t[0] = 'alpha'
  #pdb.set_trace()
  print_line(t)
  with open('reponses.csv','w') as f0:
    f0.write(renvoie_line(t)+'\n')
    for a in alphas:
      print_line(corrige(a))
      f0.write(renvoie_line(corrige(a)))
      f0.write('\n')

# if __name__ == "__main__":
#    main()

def generer_note(fichier_resultats,erreur):
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
        classe=ligne[3][1:-1]
        note=[nom,classe]
        note_valeurs=note.copy()
        bonnes_reponses=corrige(alpha)[1:5]
        bonnes_reponses+=[corrige(alpha)[5][0]]
        bonnes_reponses+=[corrige(alpha)[5][1]]
        bonnes_reponses+=[corrige(alpha)[5][2]]
        bonnes_reponses+=corrige(alpha)[6:]
        for x in bonnes_reponses:
            note_valeurs.append(convv(x))
        for i,x in enumerate(bonnes_reponses):
            #print(type(x),x,i)
            if ligne[4+i][1:-1]=="":
                note.append(0)
            elif type(x)==np.ndarray or type(x)==list:
                # if 'ADAMCZAK' in nom.upper():
                #     pdb.set_trace()
                res=ligne[4+i][1:-1]
                note.append(int(str(x.tolist()).replace(' ','') in res or str(x.tolist()).replace(' ','') in res.replace(' ','') or str(x) in res or str(x).replace(' ',',')[1:-1] in res))
            elif type(x)==int:
                res=float(ligne[4+i][1:-1])
                note.append(int(x==res))
            elif type(x)==float or type(x)==np.float64:
                res=ligne[4+i][1:-1]
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

fichier_resultats='DS6_reponses0.csv'
erreur=1e-3
notes,coeffs,titre_questions,notes_valeurs=generer_note(fichier_resultats,erreur)


file='Notes_DS06_ipt_mpsi12_2019_2020.csv'
file_valeurs=file.split('.csv')[0]+'_valeurs.csv'

with open(file,'w',encoding='utf8') as f:
    f.write(renvoie_line(titre_questions)+'\n')
    f.write(renvoie_line(coeffs)+'\n')
    for note in notes:
        f.write(renvoie_line(note)+'\n')


with open(file_valeurs,'w',encoding='utf8') as f:
    for note in notes_valeurs:
        f.write(renvoie_line(note)+'\n')
        #for i,x in enumerate(note):

            # if i==len(note)-1:
            #     ligne+=str(x)+'\n'
            # else:
            #     ligne+=str(x)+';'
        #print(ligne)
    #f.write(ligne)
