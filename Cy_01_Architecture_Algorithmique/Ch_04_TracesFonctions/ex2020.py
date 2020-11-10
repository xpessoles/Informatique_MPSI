import matplotlib.pyplot as plt
from numpy import linspace

def f1(x):
    return x

def f2(x):
    return x**2

def f3(x):
    return x**0.5


x=linspace(1,1e5,100)
plt.clf()
plt.loglog(x,f1(x),label='$x\\to x$')
plt.loglog(x,f2(x),label='$x\\to x^2$')
plt.loglog(x,f3(x),label='$x\\to \\sqrt{x}$')
plt.grid()
plt.legend()
plt.show()

# plt.clf()
# plt.semilogx(x,f1(x),label='$x\\to x$')
# plt.semilogx(x,f2(x),label='$x\\to x^2$')
# plt.semilogx(x,f3(x),label='$x\\to \\sqrt{x}$')
#
# plt.legend()
# plt.show()