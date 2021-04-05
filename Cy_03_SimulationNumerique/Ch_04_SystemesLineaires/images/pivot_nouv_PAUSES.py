import numpy as np
from numpy import array, zeros
from random import uniform

def cherche_pivot(A, i):
    """Cherche et renvoie un j tel que abs(A[j][i]) est maximal, avec j>=i"""
    n = len(A)
    best = i
    for j in range(i+1, n):
        # Inv : pour tout k <= j, abs(A[best][i]) >= abs(A[k][i])
        if abs(A[j,i]) > abs(A[best,i]):
            best = j
    return best
  
def echange_lignes(A, i, j):
    """Échange les lignes i et j de la matrice A"""
    A[i,:],A[j,:] = A[j,:].copy(), A[i,:].copy()
    return None

def descente(A,b):
    """Phase de descente de la méthode du pivot pour résoudre Ax = b.
    Préconditions : A et b sont de type array,
                    A est inversible,
                    b a même nombre de lignes que A.
    Attention: cette fonction modifie A et b."""
    n = len(A)
    for i in range(n-1):
        ip = cherche_pivot(A, i)
        # on met en place la ligne du pivot :
        echange_lignes(A, i, ip)
        echange_lignes(b, i, ip)
        p = A[i, i] # le pivot
        for j in range(i+1, n):
            alpha = - A[j,i] / p # Coefficient multiplicateur
            b[j,:] = b[j,:] + alpha * b[i,:]
            A[j,:] = A[j,:] + alpha * A[i,:]
    return None

def remontee(U,B):
    """Résout le système UX = b.
    Préconditions: U triangulaire supérieure
                   b a autant de lignes que U."""
    n, m = B.shape
    X = zeros((n, m))
    for i in range(n):
        # Invariant X[n-i:] est correct
        s = U[n-1-i, n-i:].dot(X[n-i:])
        X[n-1-i] = (B[n-1-i] - s) / U[n-1-i, n-1-i]
    return X

def resout(A,b):
    """Applique la méthode du pivot pour résoudre Ax = b.
    Renvoie la solution x trouvée.
    Préconditions : A et b sont de type array,
                    A est inversible,
                    b a même nombre de lignes que A."""
    n = len(A)
    q = len(b)
    # On copie A et b
    A_, b_ = A.copy(), b.copy()
    descente(A_,b_)
    return remontee(A_,b_)
  

A1 = array([[10., 7., 2.], [0., 2., 3.], [0., 0., 5.]])
b1 = array([[1., 0.], [0., 0.], [0., 1.]])

A2 = array([[0., 3.], [2., 0.]])
b2 = array([[7.], [5.]])
 


def presentation_pb():
    print("On veut résoudre A*X=b")
    A = array([[2., 5., -3.,-2.], [-2., -3., 2., -5.], [1., 3., -2., 2.], [-1., 6., 4., 2.]])
    b = array([[1], [1], [1.], [1.]])
    ch=""
    i=0
    ch = str(A[i,0])+'.w  +  '
    ch = ch + str(A[i,1])+'.x  '
    ch = ch + str(A[i,2])+'.y + '
    ch = ch + str(A[i,3])+'.z = '
    ch = ch + str(b[i][0])
    print(ch)
    
    ch=""
    i=1
    ch = str(A[i,0])+'.w + '
    ch = ch + str(A[i,1])+'.x  '
    ch = ch + str(A[i,2])+'.y  + '
    ch = ch + str(A[i,3])+'.z = '
    ch = ch + str(b[i][0])
    print(ch)
    
    ch=""
    i=2
    ch = str(A[i,0])+'.w  +  '
    ch = ch + str(A[i,1])+'.x  '
    ch = ch + str(A[i,2])+'.y + '
    ch = ch + str(A[i,3])+'.z  = '
    ch = ch + str(b[i][0])
    print(ch)
    
    ch=""
    i=3
    ch = str(A[i,0])+'.w +  '
    ch = ch + str(A[i,1])+'.x  '
    ch = ch + str(A[i,2])+'.y  + '
    ch = ch + str(A[i,3])+'.z  = '
    ch = ch + str(b[i][0])
    print(ch)
    
    AA= A.copy()
    bb = b.copy()
    print("")
    a=input ("Recherche du pivot dans la colonne 0.")
    i=0
    ip = cherche_pivot(AA,0)
    p = AA[0][0]
    print("index ligne pivot = "+str(ip))
    print("On ne change rien, à la ligne 0.")
    print("On fait les transvections pour faire apparaitre les 0 sur la colonne 0.")
    
    for j in range(1, 4):
        alpha = - AA[j,i] / p # Coefficient multiplicateur
        bb[j,:] = bb[j,:] + alpha * bb[i,:]
        AA[j,:] = AA[j,:] + alpha * AA[i,:]
        
    a=input("- PAUSE -")
    
    print(AA)
    
    a=input(" - PAUSE - ")
    print(" >>> Recherche du pivot dans la premiere colonne, de la ligne 1 à 3.")
    i=1
    ip = cherche_pivot(AA,i)
    p = AA[ip,i]
    print("index ligne pivot = "+str(ip))
    print("pivot = "+str(p))
    print("Echange des lignes 1 et "+str(ip))
    echange_lignes(AA, i, ip)
    echange_lignes(bb, i, ip)
    print(AA)
    a=input(" - PAUSE - ")
    print("On fait les transvections pour faire apparaitre les 0 sur la colonne 1.")
    
    for j in range(i+1, 4):
        alpha = - AA[j,i] / p # Coefficient multiplicateur
        print(alpha,p)
        bb[j,:] = bb[j,:] + alpha * bb[i,:]
        AA[j,:] = AA[j,:] + alpha * AA[i,:]
    
    print(AA)
    a=input("-PAUSE-")
    print(" >>> Recherche du pivot dans la premiere colonne, de la ligne 2 à 3.")
    i=2
    ip = cherche_pivot(AA,i)
    p = AA[ip,i]
    print("index ligne pivot = "+str(ip))
    print("pivot = "+str(p))
    print("Echange des lignes 1 et "+str(ip))
    echange_lignes(AA, i, ip)
    echange_lignes(bb, i, ip)
    print(AA)
    a=input(" - PAUSE - ")
    print("On fait les transvections pour faire apparaitre les 0 sur la colonne 1.")
    
    for j in range(i+1, 4):
        alpha = - AA[j,i] / p # Coefficient multiplicateur
        print(alpha,p)
        bb[j,:] = bb[j,:] + alpha * bb[i,:]
        AA[j,:] = AA[j,:] + alpha * AA[i,:]
    
    print(AA)
    
    return None
presentation_pb()