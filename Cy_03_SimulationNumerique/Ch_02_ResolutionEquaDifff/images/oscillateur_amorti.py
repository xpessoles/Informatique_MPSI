from numpy import linspace, array
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

y0 = 1 # m
yp0 = 0 # m * s**-1
t0, t1, h = 0, 20, .01 # s
m = 250 # kg
c = 100 # kg * s**-1
k = 1000 # kg * s**-2

def F(X,t) :
    y,yp = X
    ypp = -(k*y + c*yp)/m
    return array([yp,ypp])

X0 = array([y0,yp0])

t_list, X_list = euler(F,t0,t1,X0,h)

y_list = [X[0] for X in X_list]
yp_list = [X[1] for X in X_list]

plt.clf()
plt.plot(t_list,y_list)
plt.xlabel('Temps ($s$)')
plt.ylabel('Position ($m$)')
plt.grid()
plt.savefig('oscillateur_amorti_trajectoire.png')

plt.clf()
plt.plot(y_list,yp_list)
plt.xlabel('Position ($m$)')
plt.ylabel('Vitesse ($m.s^{-1}$)')
plt.grid()
plt.savefig('oscillateur_amorti_phase.png')

from scipy.integrate import odeint
from numpy import linspace

y0 = 1 # m
yp0 = 0 # m * s**-1
t0, t1 = 0, 20 # s
n = 1000
m = 250 # kg
c = 100 # kg * s**-1
k = 1000 # kg * s**-2

X0 = array([y0,yp0])

def F(X,t) :
    y,yp = X
    ypp = -(k*y + c*yp)/m
    return array([yp,ypp])

t_list = linspace(t0,t1,n)
X_list = odeint(F,X0,t_list)
y_list = [X[0] for X in X_list]

plt.clf()
plt.plot(t_list,y_list)
plt.xlabel('Temps ($s$)')
plt.ylabel('Position ($m$)')
plt.grid()
plt.savefig('oscillateur_amorti_odeint.png')

plt.clf()
h = .15
t_list, X_list = euler(F,t0,t1,X0,h)
y_list = [X[0] for X in X_list]
plt.plot(t_list,y_list,linestyle='-.',label='h = {}'.format(h))
h = .1
t_list, X_list = euler(F,t0,t1,X0,h)
y_list = [X[0] for X in X_list]
plt.plot(t_list,y_list,linestyle=':',label='h = {}'.format(h))
h = .01
t_list, X_list = euler(F,t0,t1,X0,h)
y_list = [X[0] for X in X_list]
plt.plot(t_list,y_list,linestyle='-',label='h = {}'.format(h))
plt.xlabel('Position ($m$)')
plt.ylabel('Vitesse ($m.s^{-1}$)')
plt.legend()
plt.savefig('oscillateur_amorti_pas.png')

