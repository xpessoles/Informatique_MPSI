

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


# Génération de la trajectoire pour faire une pyramide
# coté a et hauteur h
def pyramide(a,h,e):
  # a : largeur en mm
  # b : hauteur en mm
  # e : epaisseur du fil en mm
  a=float(a);h=float(h);e=float(e);
  X=[-a/2]
  Y=[-a/2]
  Z=[e]
  nz=int(round(h/e))
  sensX=1
  sensY=1
  for iz in range(nz):
    ny=int(round(a*(1-iz/float(nz))/e))
    X.append(sensX*a/2*(1-iz/float(nz)))
    Y.append(Y[-1])
    Z.append(Z[-1])
    sensX=-sensX
    for iy in range(1,ny):
      X.append(X[-1])
      Y.append(Y[-1]+e*sensY)
      Z.append(Z[-1])
      X.append(sensX*a/2*(1-iz/float(nz)))
      Y.append(Y[-1])
      Z.append(Z[-1])
      sensX=-sensX
    X.append(X[-1]*(1-e*a/h/4))
    Y.append(Y[-1]*(1-e*a/h/4))
    Z.append(Z[-1]+e)
    sensY=-sensY
  return (X,Y,Z)

X,Y,Z=pyramide(5,5,0.5)
#X,Y,Z=pyramide(20,20,0.5)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X, Y, Z, label='parametric curve')
plt.show()


#Génération du fichier de points machine : 1 pt tous les 10 ms, à vitesse cste

#Création d'une liste de temps pour rester à vitesse constante
V=1. # mm/s
T=[0]
for i in range(1,len(X)):
  D=sqrt((X[i]-X[i-1])**2+(Y[i]-Y[i-1])**2+(Z[i]-Z[i-1])**2)
  T.append(T[-1]+D/V)

dt=0.01
t=arange(0,T[-1],dt)
x=0*t
y=0*t
z=0*t
k=1
for i in range(t.shape[0]):
  if (t[i]>T[k]):
    k=k+1
  x[i]=X[k-1]+(t[i]-T[k-1])*(X[k]-X[k-1])/(T[k]-T[k-1])
  y[i]=Y[k-1]+(t[i]-T[k-1])*(Y[k]-Y[k-1])/(T[k]-T[k-1])
  z[i]=Z[k-1]+(t[i]-T[k-1])*(Z[k]-Z[k-1])/(T[k]-T[k-1])

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()

#tracé de la vitesse
v=[]
for i in range(1,len(x)):
  v.append(sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2+(z[i]-z[i-1])**2)/dt)

plot(v)
