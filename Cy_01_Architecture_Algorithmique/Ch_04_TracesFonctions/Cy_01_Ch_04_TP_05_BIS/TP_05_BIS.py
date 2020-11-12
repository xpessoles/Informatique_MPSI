import numpy as np
import matplotlib.pyplot as plt

def suite(x,mu):
    return mu*x*(1-x)

def logistique1(mu,x0,n):
    Xn = [x0]
    for i in range(n):
        Xn.append(suite(Xn[-1],mu))
    plt.figure()
    titre = "$\mu$ = "+str(mu)+", x0 = "+str(x0)+", n="+str(n)
    plt.plot(Xn,".-")
    plt.title(titre)
    plt.grid()
    plt.show()
    
#logistique1(2.8,0.9,20)

def logistique2(mu,x0,n):
    Xn = [x0]
    Yn = [suite(x0,mu)]
    for i in range(n):
        x=Xn[-1]
        y=Yn[-1]
        Xn.append(y)
        Yn.append(y)
        Xn.append(y)
        Yn.append(suite(y,mu))
    plt.figure()
    titre = "$\mu$ = "+str(mu)+", x0 = "+str(x0)+", n="+str(n)
    plt.plot(Xn,Yn,".-")
    
    # Tracé de la bissectrice
    plt.plot([0,1],[0,1])
    
    # Tracé de la fonction
    les_x = [x/100 for x in range(101)]
    les_y = [suite(x,mu) for x in les_x]
    plt.plot(les_x,les_y)
    
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.axis("equal")
    plt.title(titre)
    plt.grid()
    plt.show()

#logistique2(2.8,0.9,10)
#Quesiton 4
def question_4():
    mu = 2
    les_X = []
    les_mu = []
    while mu<=4:
        Xn=[0.9]
        for i in range(201):
            y = suite(Xn[-1],mu)
            y = round(y,3)
            Xn.append(y)
        les_X.append(Xn[101:])
        mu = mu+0.002
        les_mu.append(mu)
    
    LES_X = []
    LES_Y = []
    
    for i in range(len(les_mu)):
        for x in les_X[i]:
            LES_X.append(les_mu[i])
            LES_Y.append(x)
    plt.plot(LES_X,LES_Y,',')
    plt.grid()
    plt.axis("equal")
    plt.show()

question_4()