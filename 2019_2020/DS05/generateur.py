#!/usr/bin/python3

"""Calcule les solutions du DS (version du 28 mars 2015).
   Usage :

   python3 generateur.py p q

   écrit sur la sortie standard un csv (séparateur : ";") pour les
   valeurs du paramètre alpha dans range(p, q). L'entête comporte les
   numéros des questions, la valeur de alpha est en première colonne."""

from ds5_corrige import *
import pdb




def conv(x, n):
    return int((x*n) // m) # on reconvertit en "petit" entier si possible


#alpha = 1

def corrige(alpha):
    """Produit un tableau t contenant les valeurs attendues pour le DS,
        en fontion du paramètre alpha.
        t[0] contient la valeur de alpha et t[i] pour i=1, ..., 18
        contient la valeur attendue pour la question i."""
    sol = [alpha]
    #sol_precise=trapeze(f,0,alpha,int(alpha**2*np.sqrt(1000))*10)
    # Qu. 1 :
    sol.append(rect_gauche(f,0,alpha,1000))
    # Qu. 2 :
    sol.append(rect_droit(f,0,alpha,1000))
    # Qu. 3 :
    sol.append(trapeze(f,0,alpha,1000))
    # Qu. 4 :
    u0=alpha
    v0=alpha+10
    a=alpha*1e-2
    b=alpha*1e-3
    c = alpha*1e-2
    d = 0.2*alpha*1e-3
    t0,t1,h = 0,20,.01
    def proie_seule(u,t):
        return a*u
    def proie_predateur(X,t):
        u,v = X
        return np.array([u*(a-b*v),-v*(c-d*u)])
    t_list,A_list = euler(proie_seule,t0,t1,u0,h)
    sol.append(float(A_list[-1]))
    X0 = np.array([u0,v0])
    t_list, X_list = euler(proie_predateur,0,300,X0,h)
    # Qu. 5 :
    sol.append(float(X_list[-1][0]))
    # Qu. 6 :
    sol.append(float(X_list[-1][1]))
    return sol


def convv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 5 chiffres après la virgule."""
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
  t = list(range(7))
  t[0] = 'alpha'
  #pdb.set_trace()
  print_line(t)
  with open('reponses.csv','w') as f:
    f.write(renvoie_line(t)+'\n')
    for a in alphas:
      print_line(corrige(a))
      f.write(renvoie_line(corrige(a)))
      f.write('\n')

if __name__ == "__main__":
   main()
