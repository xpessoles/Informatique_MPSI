import matplotlib.pyplot as plt
import numpy as np


def proie_seule(u,t):
    return a*u

def proie_predateur(X,t):
    u,v = X
    return np.array([u*(a-b*v),-v*(c-d*u)])

def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0] 
    t_list = [a]
    while t+h <= b:
      
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list
    


a=0.13
b=0.005
u0 = 15
c = 0.03
d = 0.001
v0 = 20
t0,t1,h = 0,20,.01

# Question 1 : Donner la population de la proie au bout de 20 unités de temps.

# t_list,A_list = euler(proie_seule,t0,t1,u0,h)
# plt.plot(t_list,A_list)
# plt.xlabel('Temps ($s$)')
# plt.ylabel('Concentration ($mol$)')
# plt.grid()
# plt.show()

# Question 2 Donner la population de proies et prédateurs au bout de 300 unités de temps.


X0 = np.array([u0,v0])
t_list, X_list = euler(proie_predateur,0,300,X0,h)

u_list = [X[0] for X in X_list]
v_list = [X[1] for X in X_list]
plt.clf()

plt.plot(t_list,u_list)
plt.plot(t_list,v_list)

plt.xlabel('Temps ($s$)')
plt.ylabel('Position ($m$)')
plt.grid()
plt.show()

