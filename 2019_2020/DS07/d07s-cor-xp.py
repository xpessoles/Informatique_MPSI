import math as m
import numpy as np

alpha = 64

# Question 1
def trapeze(f,a,b,n):
    s = (f(a)+f(b))/2
    pas = (b-a)/n
    for i in range(1,n):
        s = s+f(a+pas*i)
    return s*pas

def f(t):
    return m.cos(m.sqrt(t))
res = trapeze(f,alpha,alpha+1,1000)
print ("Question 1 :"+str(res))

# Question 2
def dichotomie(f, a, b, epsilon):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
       Préconditions : f(a) * f(b) <= 0
                       f continue sur [a,b]
                       epsilon > 0"""
    fa, fb= f(a), f(b)
    while b-a > 2*epsilon:
        m = (a + b)/2
        fm = f(m)
        if fa*fm <= 0:
            b,fb = m,fm
        else:
            a,fa = m,fm
    return (a + b)/2

A = [[0,1,32,243],[1,32,243,1024],[32,243,1024,3125],[243,1024,3125,7776]]
mA = np.array(A)
V=np.array([[1],[2],[3],[alpha]])
invmA = np.linalg.inv(mA)
X = np.dot(invmA,V)
print("Question 9 : " + str(X[0]))

B= np.dot(A,A)
B= np.dot(B,A)

print("Question 10 : " + str(B[0,0]%(10000+alpha)))

