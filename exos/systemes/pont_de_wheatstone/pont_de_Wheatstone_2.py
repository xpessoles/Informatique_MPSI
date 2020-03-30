# -*- coding: utf-8 -*-
"""
Created on Sat May 24 06:38:15 2014

@author: ericguichet
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# donnees
R1,R4,R=10**3,2*10**3,10**3
R2=(random.randrange(11)+5)*500
E=10

t=np.linspace(10**3,2*10**4,100) # valeurs de R3
i=[]
for R3 in t:
    A=np.array([[1,-1,0,0,-1],[0,0,1,-1,-1],[R1,R2,0,0,0],[0,0,R3,R4,0],[R1,0,0,-R4,R]])
    B=np.array([[0],[0],[E],[E],[0]])
    X=np.linalg.solve(A,B)
    i=i+[X[4,0]*1000] # *1000 pour recuperer une intensite en mA
plt.plot(t,i)
plt.axhline()
plt.show()
