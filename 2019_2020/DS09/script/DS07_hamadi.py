from math import cos

#Q1
def f(x):
    f=cos(t**0.5)

a=74
b=73
N=1000

def T(f,a,b,N):
    S=0.5*(f(a)+f(b))
    h=(b-a)/N
    for k in range(1,N):
        S=S+f(a+k*h)
    return S*h


#Q2
def f(x):
    f=x**2+x**0.5-83

epsilon=1/100000
a=0
b=100000

def dichotomie(f,a,b,epsilon):
    c, d =a, b
    fc ,fd= f(c), f(d)
    while d-c>2*epsilon:
        m=(c+d)/2
        fm=f(m)
        if fc*fm<=0:
            d, fd=m, fm
        else:
            c,fc=m, fm
    return (c+d)/2

#Q3

def f(x):
    f=x**2+x**0.5-83

x0=73
fp=2*x+1/(2*x**0.5)

def newton(f,fp,x0, epsilon):
    u=x0
    v=u-f(u)/fp(u)
    while abs(v-u)>epsilon:
        u,v=v, v-f(v)/fp(v)
    return u

#Q4

def f(x):
    f=x**2+x**0.5-83

a=85
b=0
epsilon= 1/100000

def dichotomie(f,a,b,epsilon):
    c, d =a, b
    fc ,fd= f(c), f(d)
    while d-c>2*epsilon:
        m=(c+d)/2
        fm=f(m)
        if fc*fm<=0:
            d, fd=m, fm
        else:
            c,fc=m, fm
    return (c+d)/2

#Q5

from math import cos

def f(x):
    2+x**0.5+cos(x)

def a(x):
    x+73

b=73
N=1000

def T(f,a,b,N):
    S=0.5*(f(a)+f(b))
    h=(b-a)/N
    for k in range(1,N):
        S=S+f(a+k*h)
    return S*h

g= T(f,a,b,N)-10

epsilon= 1/100000

def dichotomie(g,a,b,epsilon):
    c, d =a, b
    gc ,gd= g(c), g(d)
    while d-c>2*epsilon:
        m=(c+d)/2
        gm=g(m)
        if gc*gm<=0:
            d, gd=m, gm
        else:
            c,gc=m, gm
    return (c+d)/2

#Q6
#Q9
A= array([[0,1,32,243],[1,32,243,1024],[32,243,1024,3125],[243,1024,3125,7776]])
b= array([[1,2,3,73]])

# def cherche_pivot(A,j):
#
# def echanges_lignes(A,i,j):
#

def descente(A,b):
    n=len(A)
    for j in range(n-1):
        ip=cherche_pivot(A,j)
        echange_ligne(A,j,ip)
        echange_ligne(b,j,ip)
        p=A[j,j
        for i in range(j+1, n)]
        alpha=-A[i,j]/p
        b[i,:]=b[i,:]+alpha*b[j,:]
        A[i,:]=A[i,:]+alpha*A[j,:]
    return None

def remontee(U,B):
    n,m=B.shape
    X=zeros((n,m))
    for k in range((n):
        i=n-1-k
        s=U[i,i+1:].dot(X[i+1:])
        X[i]=(B[i]-s)/U[i,i]
    return X



def resout(A,b):
    n=len(A)
    A_, b-=A.copy(), b.copy()
    descente(A_,b_)
    return remontee(A_,b_)

X=resout(A,b)

x1= X[[0],:]

#Q10




















