import numpy as np

# donnees
R1,R2,R3,R4,R=10**4,10**3,10**4,10**3,10**3
E=10

A=np.array([[1,-1,0,0,-1],[0,0,1,-1,-1],[R1,R2,0,0,0],[0,0,R3,R4,0],[R1,0,0,-R4,R]])
B=np.array([[0],[0],[E],[E],[0]])
X=np.linalg.solve(A,B)
print(X[4,0])
