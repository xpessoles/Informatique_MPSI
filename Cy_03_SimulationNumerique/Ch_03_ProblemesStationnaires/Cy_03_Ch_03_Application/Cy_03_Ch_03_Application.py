import numpy as np
import matplotlib.pyplot as plt
import math as m
def dichotomie(f, a, b, epsilon):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
    Préconditions : f(a) * f(b) <= 0
    f continue sur [a,b]
    epsilon > 0"""
    fa, fb = f(a), f(b)
    n=0
    while b - a > 2 * epsilon:
        n=n+1
        m = (a + b) / 2.
        fm = f(m)
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2.,n
    
def dichotomie2(f,n, a, b, epsilon):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
    Préconditions : f(a) * f(b) <= 0
    f continue sur [a,b]
    epsilon > 0"""
    fa, fb = f(a,n), f(b,n)
    n=0
    while b - a > 2 * epsilon:
        n=n+1
        m = (a + b) / 2.
        fm = f(m,n)
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2.,n
    

def secante(f,u0,u1,eps):
    """Zéro de f par la méthode de la sécante
    u0,u1 : deux premiers points
    eps : critère d'arrêt"""
    u,v = u0,u1
    n=0
    while abs(u-v) > eps :
        n+=1
        p = (f(u)-f(v)) / (u-v)
        u,v = v,u - f(u)/p
    return u,n

def newton(f, fp, x0, epsilon):
    """Zéro de f par la méthode de Newton
    départ : x0, f' = fp, critère d'arrêt epsilon"""
    n=0
    u = x0
    v = u - f(u)/fp(u)
    while abs(v-u) > epsilon:
        n=n+1
        u, v = v, v - f(v)/fp(v)
    return u,n

def fE(x):
    return x*m.log(x)-1

def fEp(x):
    return m.log(x)+1

def solve_fE():
    a,b,epsilon = 1,m.e,10e-6/2
    sol = dichotomie(fE,a,b,epsilon)
    print("Dichotomie :",sol)
    sol = secante(fE,a,b,epsilon)
    print("Secante :",sol)
    sol = newton(fE,fEp,a,epsilon)
    print("Newton :",sol)


def fn(x,n):
    return x**n+x**(n-1)+x-1

def solve_fn():
    a,b,epsilon = 0,1,10e-3
    for i in range(1,101):
        sol = dichotomie2(fn,i,a,b,epsilon)
        print("Dichotomie :",i,sol)
        
def plot_fn():
    for i in range(1000,1010):
        les_x =np.linspace(0.8,1,1000)
        les_y = [fn(x,i) for x in les_x]
        plt.plot(les_x,les_y)
    plt.grid()
    plt.show()

plot_fn()
        
#solve_fn()
#solve_fE()