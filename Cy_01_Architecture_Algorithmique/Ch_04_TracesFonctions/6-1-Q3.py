from numpy import linspace
import matplotlib.pyplot as plt

x=linspace(1,1e5,100)
y=[t**2 for t in x]
y1=[t**(0.5) for t in x]

plt.clf()
plt.loglog(x,y,label='$x^2$')
plt.loglog(x,y1,label='$\\sqrt{x}$')
# plt.xscale('log')
# plt.yscale('log')
plt.legend()
plt.grid()
plt.show()