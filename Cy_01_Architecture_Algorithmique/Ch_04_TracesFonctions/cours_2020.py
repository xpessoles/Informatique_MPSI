import matplotlib.pyplot as plt
x = [1, 3, 4, 2]
y = [2, 1, 4, 2]
plt.clf()
plt.plot(x,y,label='$\\int \\alpha$')
plt.xlabel('axe des abscisses')
plt.ylabel('axe des ordonnées')
plt.legend()
#plt.show()
plt.savefig("ex_base_01.png")

from numpy import linspace
from math import cos,pi
x = linspace(0,2*pi,400)
y = [cos(t) for t in x]
plt.clf()
plt.plot(x,y)
plt.xlabel('$t$')
plt.ylabel('$\\cos(t)$')
plt.savefig('ex_numpy_01.png')
