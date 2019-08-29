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

def rmatrix(n,p, m):
    '''Renvoie une matrice de dimensions (n,p) avec des coefficients uniformes entre 0 et m'''
    return array([[uniform(0,m) for j in range(p)] for i in range(n)])

A = rmatrix(5,5,100)
b = rmatrix(5,2,100)

# hilbert
n = 5
M = array([[ 1/(i+j+1.) for j in range(n)]
               for i in range(n)])
u0 = array([[-0.76785474],
       [-0.44579106],
       [-0.32157829],
       [-0.25343894],
       [-0.20982264]])
s0 = resout(M, u0)
u1 = array([[-0.76784856],
       [-0.44590775],
       [-0.32107213],
       [-0.25420613],
       [-0.20944639]])
s1 = resout(M, u1)
# finhilbert


