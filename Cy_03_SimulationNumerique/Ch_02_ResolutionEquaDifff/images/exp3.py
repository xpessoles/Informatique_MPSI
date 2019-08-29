from math import exp
from numpy import linspace
import matplotlib.pyplot as plt

def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a] # la liste des temps
    while t+h <= b:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list

def F(y,t) :
    return y

plt.clf()
t_list = linspace(0,3,1000)
y_list = [exp(t) for t in t_list]
plt.plot(t_list,y_list,linewidth=3,label="Exponentielle")
h = 1
t_list,y_list = euler(F,0,3,1,h)
plt.plot(t_list,y_list,linestyle='--',label="$h=1$")
plt.legend()
h = .1
t_list,y_list = euler(F,0,3,1,h)
plt.plot(t_list,y_list,linestyle='-.',label="$h=1/10$")
plt.legend()
h = .03
t_list,y_list = euler(F,0,3,1,h)
plt.plot(t_list,y_list,linestyle=':',label="$h=3/100$")
plt.legend()
plt.savefig('exp3.png')
