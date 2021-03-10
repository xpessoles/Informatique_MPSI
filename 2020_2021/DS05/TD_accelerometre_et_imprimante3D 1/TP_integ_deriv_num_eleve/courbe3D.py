 
from mpl_toolkits.mplot3d import axes3d

# Construction d'une courbe en hélice conique
th=arange(0,15*pi,0.1)
X=(10-th/5)*cos(th)
Y=(10-th/5)*sin(th)
Z=th/10

# Tracé de l'hélice
fig = figure()
ax = fig.gca(projection='3d')
ax.plot(X, Y, Z)
plt.show()
