import numpy as np
from math import exp, log
import matplotlib.pyplot as plt

T = [0, 7, 18, 27, 37, 56, 102]
C = [34.83, 32.14, 28.47, 25.74, 23.14, 18.54, 11.04]

def trace_fonction(xmin,xmax,f,nom_de_fichier,lab=""):
    """Trace la courbe de f sur [xmin,xmax]
    Enregistre dans nom_de_fichier"""
    plt.clf()
    les_x = np.linspace(xmin,xmax,1000)
    les_y = [f(t) for t in les_x]
    plt.plot(les_x,les_y,".",label=lab)
    if lab != '' :
        plt.legend()
    plt.show()
    
    #plt.clf()
    
xmin = 0
xmax = 20
def f(x) :
    return 0.02*x*(x-5)
    
#trace_fonction(xmin,xmax,f,'fig_ex_fonction.png')

def trace_ajustement(X,Y,f,nom_de_fichier,lab='Courbe d ajustement'):
    """Trace la courbe de f et les points (X,Y)
    Enregistre dans nom_de_fichier"""
    plt.clf()
    plt.plot(X,Y, 'rx',label='Mesures expérimentales')
    les_x = np.linspace(min(X),max(X),1000)
    les_y = [f(t) for t in les_x]
    plt.plot(les_x,les_y,label=lab)
    plt.xlabel('Temps (s)')
    plt.ylabel('Concentration (mol / L)')
    plt.title('Évolution de la concentration en fonction du temps')
    plt.legend()
    plt.show()
    #pl.savefig(nom_de_fichier)
    plt.clf()
    
def g(x) :
    return 34 - 0.2*x
#trace_ajustement(T,C,g,'fig_ex_ajustement.png')

def L1(k):
    """L1(k)"""
    S = 0
    for i in range(len(T)):
        S = S + (C[i]-C[0]*exp(-k*T[i]))**2
    return S/7
    
def dL1(k):
    """L1'(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i] * (C[i]-C[0]*exp(-k*T[i])) * exp(-k*T[i])
    return 2*C[0]*S / 7
    
def ddL1(k):
    """L1''(k)"""
    S = 0
    for i in range(len(T)) :
        S = S + T[i]**2 * (2*C[0]*exp(-k*T[i]) - C[i]) * exp(-k*T[i])
    return 2*C[0]*S / 7
    
def newton(f,fp,x0,eps):
    """Zéro de f par la méthode de Newton, critère d'arret eps
    fp : dérivée de f
    x0 : point initial"""
    u = x0
    v = u - f(u)/fp(u)
    while abs(v-u) > eps:
        u, v = v, v - f(v)/fp(v)
    return u
    
def val_k1() :
    """Valeur de k1"""
    return newton(dL1, ddL1, 0.01, 10**-10)

k1 = val_k1()