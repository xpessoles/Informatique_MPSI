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

alpha = 16

def corrige(alpha):
  """Produit un tableau t contenant les valeurs attendues pour le DS,
     en fontion du paramètre alpha.
     t[0] contient la valeur de alpha et t[i] pour i=1, ..., 18
     contient la valeur attendue pour la question i."""
  sol = [alpha]
  t = sujet.cree_tableau(alpha)
  # Qu. 1 :
  N = len(t)
  sol.append(N)
  # Qu. 2 :
  sol.append(len([x for x in t if x >= 3000]))
  # Qu. 3 :
  sol.append(len([x for x in t if x%3 == 0]))
  # Qu. 4 :
  sol.append(len([0 for i in range(N-1) for j in range(i+1, N) if t[i] < t[j]]))

  u = 10 + alpha
  U = []
  for i in range(10000) :
      # invariant: u vaut u_k et U contient u_k pour k in range(i)
      # 
      U.append(u)
      u = (15091*u) % 64007
  # Qu. 5
  sol.append(U[42])
  # Qu. 6
  sol.append(U[-1])
  # Qu. 7
  sol.append(len([x for x in U if x%17 == 0]))
  # Qu. 8
  sol.append(len([i for i in range(len(U)-1) if abs(U[i]-U[i+1]) <= 1000]))
  # Qu. 9
  sol.append(sum(U))

  toto = open('zeta5.txt','r')
  toto.readline()
  toto.readline() # on élimine les deux premières lignes
  lignes = toto.readlines()
  toto.close()

  blocs10 = [b for l in lignes for b in l.split()[:5]]
  # Qu. 10
  s = str(2000 + alpha)

  def nbinbloc(s, b):
    return len([i for i in range(len(b)-len(s)+1) if b[i:i+len(s)] == s])

  def nbinblocs(s, blocs):
    return sum(nbinbloc(s, b) for b in blocs)

  sol.append(nbinblocs(s, blocs10))
  # Qu. 11
  blocs50 = [ ''.join(blocs10[i:i+5]) for i in range(0, len(blocs10), 5) ]
  sol.append(nbinblocs(s, blocs50))
  # Qu. 12
  blocs500 = [ ''.join(blocs50[i:i+10]) for i in range(0, len(blocs50), 10) ]
  sol.append(nbinblocs(s, blocs500))
  # Qu. 13
  sol.append(nbinbloc(s, ''.join(blocs500)))
  # Qu. 14
  sol.append(so.brentq(lambda x : x**2 + sqrt(x) -10 -alpha,3,11))
  # Qu. 15
  def F (x,t) :
    return 3*cos(x) + t

  sol.append(si.odeint(F, alpha, [0,1])[-1, 0])

  # Qu. 16
  def G (X,t) :
    a,b = X[0],X[1]
    return array([b,1+sin(t+a)])
  sol.append(si.odeint(G,array([0,0]),[0,1 + alpha/10])[-1,0])

  # Qu. 17
  sol.append(si.odeint(G,array([0,1]),[0, 1 + alpha/10])[-1,0])

  # Qu. 18
  def H (X,t) :
    a,b = X[0],X[1]
    return array([b,1+atan(t+a)])
  f = lambda beta : si.odeint(H,array([0,beta]),[0, 1 + alpha/10])[-1,0]-1-(2/3)*alpha

  sol.append(so.brentq(f,-10,10))

  return sol

def conv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 5 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.5f}".format(v)
    return str(v)
    
def print_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    print(';'.join(conv(v) for v in l))

from sys import argv

def main():
  alphas=range(int(argv[1]),int(argv[2]))
  t = list(range(19))
  t[0] = 'alpha'
  print_line(t)
  for a in alphas:
    print_line(corrige(a))

if __name__ == "__main__":
   main()
