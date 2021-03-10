
from mpl_toolkits.mplot3d import axes3d


# Fonction de génération de la trajectoire pour faire une pyramide
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


# Génération de la trajectoire brute
X,Y,Z=pyramide(5,5,0.5)

# Tracé de la trajectoire brute
fig = figure()
ax = fig.gca(projection='3d')
ax.plot(X, Y, Z)
plt.show()
