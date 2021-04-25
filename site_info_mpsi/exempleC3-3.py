#from scipy.optimize import newton
import numpy as np

def f(x):
    return 16*x**4-20*x**2+5

def fp(x):
    return 4*16*x**3-2*20*x



def secante(f,u0,u1,eps):
    """Zéro de f par la méthode de la sécante
    u0,u1 : deux premiers points
    eps : critère d'arrêt"""
    u,v = u0,u1
    while abs(u-v) > eps :
        p = (f(u)-f(v)) / (u-v)
        u,v = v,u - f(u)/p
    return u

def newton(f, fp, x0, epsilon):
    """Zéro de f par la méthode de Newton départ : x0, f' = fp, critère d'arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    while abs(v-u) > epsilon:
        u, v = v, v - f(v)/fp(v)
    return u

a=newton(f,fp,1,1e-10)

#Nombre d'or

b=newton(lambda x:x**2-x-1,lambda x:2*x-1,1,1e-10)
