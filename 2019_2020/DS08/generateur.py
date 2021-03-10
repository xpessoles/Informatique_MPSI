#!/usr/bin/python3

"""Calcule les solutions du DS (version du 28 mars 2015).
   Usage :

   python3 generateur.py p q

   écrit sur la sortie standard un csv (séparateur : ";") pour les
   valeurs du paramètre alpha dans range(p, q). L'entête comporte les
   numéros des questions, la valeur de alpha est en première colonne."""

import sujet

import scipy.optimize as so
import scipy.integrate as si
from math import sqrt, sin, cos, atan
from numpy import array
import numpy as np

def trapeze(f,a,b,n):
    h=(b-a)/n
    S=0.5*(f(a)+f(b))
    for k in range(1,n):
        S+=f(a+k*h)
    return S*h

def dichotomie(f, a, b, epsilon):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
       Préconditions : f(a) * f(b) <= 0
                       f continue sur [a,b]
                       epsilon > 0"""
    c, d = a, b
    fc, fd = f(c), f(d)
    k=0
    while d - c > 2 * epsilon:
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
        k+=1
    return (c + d) / 2.,k

def newton(f, fp, x0, epsilon):
    """Zéro de f par la méthode de Newton
       départ : x0, f' = fp, critère d'arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    k=0
    while abs(v-u) > epsilon:
        u, v = v, v - f(v)/fp(v)
        k+=1
    return u,k



#alpha = 16

def corrige(alpha):
  """Produit un tableau t contenant les valeurs attendues pour le DS,
     en fontion du paramètre alpha.
     t[0] contient la valeur de alpha et t[i] pour i=1, ..., 18
     contient la valeur attendue pour la question i."""
  sol = [alpha]
  #Qu 1
  sol.append(trapeze(lambda x : cos(sqrt(x)),alpha,alpha+1,1000))

  #Qu 2
  def f2(t):
      return t**2+t**0.5-10-alpha

  def f2p(t):
      return 2*t+0.5*t**(-0.5)


  sol.append(newton(f2,f2p,1,1e-5)[0])

  #Qu 3
  sol.append(newton(f2,f2p,alpha,1e-5)[1])


  #Qu 4
  sol.append(dichotomie(f2, 0, 12+alpha, 1e-5)[1])

# Qu. 5 :
  sol.append(dichotomie(lambda t : trapeze(lambda x : 2+sqrt(x)+cos(x),alpha,alpha+t,1000)-10,0,50,1e-5)[0])

  #Qu 6
  def F (x,t) :
    return 3*cos(x) + t

  sol.append(si.odeint(F, alpha, [0,1])[-1, 0])

  # # Qu. 5
  # def G (X,t) :
  #   a,b = X[0],X[1]
  #   return array([b,1+sin(t+a)])
  # sol.append(si.odeint(G,array([0,0]),[0,1 + alpha/10])[-1,0])
  #
  # # Qu. 6
  # sol.append(si.odeint(G,array([0,1]),[0, 1 + alpha/10])[-1,0])

  # Qu. 7
  def G (X,t) :
      a,b = X[0],X[1]
      return array([b,1+sin(t+a)])

  les_t = [i*(1+alpha/10)/10000 for i in range(10001)]

  sol.append(si.odeint(G,array([0,0]),les_t)[-1,0])

  # Qu. 8
  def H (X,t) :
    a,b = X[0],X[1]
    return array([b,1+atan(t+a)])
  f = lambda beta : si.odeint(H,array([0,beta]),[0, 1 + alpha/10])[-1,0]-1-(2/3)*alpha

  sol.append(so.brentq(f,-10,10))

  # Qu. 9
  A=array([[0,1,32,243],[1,32,243,1024],[32,243,1024,3125],[243,1024,3125,7776]])
  B=array([[1],[2],[3],[alpha]])

  X=np.linalg.solve(A,B)
  sol.append(X[0][0])

  # Qu. 10
  B=np.dot(A,np.dot(A,A))
  sol.append(B[0][0]%(10000+alpha))


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
  with open('reponses.csv','w') as f0:
    f0.write(renvoie_line(t)+'\n')
    for a in alphas:
      print_line(corrige(a))
      f0.write(renvoie_line(corrige(a)))
      f0.write('\n')
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
        classe=ligne[3][1:-1]
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

def remplacer_dans_fichier(fichier0,fichier,carac0,carac1):
  with open(fichier0,'r',encoding='utf8') as f:
    texte0=f.read()
    texte=texte0.replace(carac0,carac1)
  with open(fichier,'w',encoding='utf8') as f:
    f.write(texte)

fichier_resultats0='DS7_ipt_2019_2020.csv'
remplacer_dans_fichier(fichier_resultats0,fichier_resultats0.split('.csv')[0]+'2.csv',",",";")

fichier_resultats=fichier_resultats0.split('.csv')[0]+'2.csv'

erreur=1e-4
erreur1=1e-3
erreur2=1e-4
notes,coeffs,titre_questions,notes_valeurs=generer_note(fichier_resultats,erreur1,erreur2)


file='Notes_DS07_ipt_mpsi12_2019_2020.csv'
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
