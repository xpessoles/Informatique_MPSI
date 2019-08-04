from numpy import array, transpose
from numpy.linalg import solve
import matplotlib.pyplot as plt
A = array([[1. ,  -40.],
           [1. ,  -35.5],
           [1. ,   -30.5],
           [1. ,   -25.5],
           [1. ,  -20.5],
           [1. ,   -15.5],
           [1. ,   -10.5],
           [1. ,  -5.5],
           [1. ,   -0.5],
           [1. ,   4.5],
           [1. ,  19.5],
           [1. ,   34.5],
           [1. ,   44.5],
           [1. ,   49.5]])
b = array([[-39.67],
           [-32.68],
           [-23.81],
           [-13.61],
           [-3.76],
           [5.38],
           [12.50],
           [24.28],
           [32.57],
           [38.78],
           [66.65],
           [93.18],
           [111.88],
           [121.52]])
At = transpose(A)
X = solve(At.dot(A),At.dot(b))
alpha = X[0,0]
beta = X[1,0]
x = [-40.,
     -35.5,
     -30.5,
     -25.5,
     -20.5,
     -15.5,
     -10.5,
      -5.5,
      -0.5,
       4.5,
      19.5,
      34.5,
      44.5,
      49.5]

y = [-39.67,
     -32.68,
      -23.81,
      -13.61,
      -3.76,
      5.38,
      12.50,
      24.28,
     32.57,
      38.78,
      66.65,
      93.18,
      111.88,
      121.52]

def f(t) :
    return alpha + beta*t

plt.clf()
plt.plot([-42,51], [f(-42),f(51)],label="$y = "+str(alpha)+" + "+str(beta)+"\\cdot x$",linewidth = 2)
plt.plot(x,y,'xr',label="Mesures expérimentales",markersize=10,markeredgewidth=3)
plt.axis([-42,51]+[f(-42),f(51)])
plt.xlabel("Température (°C)")
plt.ylabel("Température (°F)")
plt.legend(loc=0)
plt.savefig("regression_temperature.png")
