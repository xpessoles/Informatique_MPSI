import math as m
import numpy as np
import matplotlib.pyplot as plt

alpha = 72

L = alpha
masse = 1+0.01*alpha
g = 9.81
theta_0 = m.pi/(4*alpha)
epsilon = 1e-3
theta_0b = theta_0*(1-epsilon)
n=100

# Question 1
T_0 = m.sqrt(L/g)*2*m.pi
print("Q1",T_0)
# Question 2
def rg (f,a,b,n):
    s = f(a)
    pas = (b-a)/n
    for i in range(1,n):
        s = s+f(a+pas*i)
    return s*pas

def rd (f,a,b,n):
    s = f(b)
    pas = (b-a)/n
    for i in range(1,n):
        s = s+f(a+pas*i)
    return s*pas

def tr (f,a,b,n):
    s = (f(a)+f(b))/2
    pas = (b-a)/n
    for i in range(1,n):
        s = s+f(a+pas*i)
    return s*pas

def periode(theta):
    return 4/(m.sqrt((2*g/L)*(m.cos(theta)-m.cos(theta_0))))

a=0

Tg = rg(periode,a,theta_0,n)
Td = rd(periode,a,theta_0b,n)
Tt = tr(periode,a,theta_0b,n)
print("Q2",Tg)
print("Q3",Td)
print("Q4",Tt)

print("Q5 - epsG",abs(Tg-T_0))
print("Q5 - epsD",abs(Td-T_0))
print("Q5 - epst",abs(Tt-T_0))



def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0]
    t_list = [a]
    while t+h <= b:

        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list

def F(X,t):
    vc = 8
    vm = 1.5 + alpha/100
    x,y=X
    xp  = vc *(vm*t-x)/m.sqrt((vm*t-x)**2+y*y)
    yp  = vc *(-y)/m.sqrt((vm*t-x)**2+y*y)
    return np.array([xp,yp])

X0 = np.array([100+alpha,300+alpha])
t, X = euler(F,0,38,X0,38/100)

les_x=[x[0] for x in X]
les_y=[x[1] for x in X]
plt.plot(les_x,les_y)
#plt.show()
print("Q6",X0)
print("Q7",les_x[-1])
print("Q8",les_y[-1])