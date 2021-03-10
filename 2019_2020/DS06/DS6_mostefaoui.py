#DS5

from math import sqrt
import numpy as np
from scipy.integrate import odeint

#Exo 1

def Rg(f,a,b,N):
	S = 0
	h = (b-a)/N
	for k in range(N):
		S += f(a + k*h)
	return S*h

def rect_gauche(f,a,b,n):
    h=(b-a)/n
    S=0
    for k in range(n):
        S+=f(a+k*h)
    return S*h

def Rd(f,a,b,N):
	S = 0
	h = (b-a)/N
	for k in range(1,N+1):
		S += f(a + k*h)
	return S*h

def Tr(f,a,b,N):
	S = 0.5*(f(a)+f(b))
	h = (b-a)/N
	for k in range(1,N):
		S += f(a + k*h)
	return S*h

def euler(F,a,b,y0,h):
	y = y0
	t = a
	y_list = [y0]
	t_list = [a]

	while t+h <= b:
		y = y + h*F(y,t)
		y_list.append(y)
		t = t + h
		t_list.append(t)

	return t_list,y_list

alpha = 67
epsilon = 1e-3
m = 1 + 0.01*alpha
g = 9.81
L = alpha
theta0 = np.pi / (4*alpha)
a = 2*g/L

T0 = 2*np.pi*np.sqrt(L/g)
print("Q1:",T0)

f = lambda x: 1 / (np.sqrt(a*(np.cos(x)-np.cos(theta0))))

Tg_int = Rg(f,0,theta0*(1-epsilon),100)
Td_int = Rd(f,0,theta0*(1-epsilon),100)
Tt_int = Tr(f,0,theta0*(1-epsilon),100)

print("Q2:",4*Tg_int)
print("Q2:",4*rect_gauche(f,0,theta0,100))
print("Q3:",4*Td_int)
print("Q4:",4*Tt_int)

epsg = abs(4*Tg_int - T0)
epsd = abs(4*Td_int - T0)
epst = abs(4*Tt_int - T0)

print("Q5: \n epsg = {} \n epsd = {} \n epst = {}".format(epsg,epsd,epst))

#Exo 2

Vm = 1.5 + alpha/100
Vc = 8

X0 = 100 + alpha
Y0 = 300 + alpha

#question 6
condinit = np.array([X0,Y0])
print("Q6:", condinit)

def F(X,t):
	x,y = X
	norm = np.sqrt((Vm*t - x)**2 + (-y)**2)
	dx = Vc * (Vm*t - x) / norm
	dy = Vc * (-y) / norm
	return np.array([dx,dy])

x,y = euler(F,0,38,condinit,38/100)

print("Q7:", y[-1][0])
print("Q8:", y[-1][1])



# def F1(y,t):
# 	a = alpha*(10**(-2))
# 	dy = a*y
# 	return dy

# t_list,y_list = euler(F1,0,20,alpha,1/100)

# print(y_list[-1])

# def F2(X,t):
# 	a = alpha*(10**(-2))
# 	b = alpha*(10**(-3))
# 	c = alpha*(10**(-2))
# 	d = (alpha/5)*(10**(-3))
# 	u,v = X
# 	return np.array([u*(a-b*v),-v*(c-d*u)])

# x,y = euler(F2,0,300,[alpha,alpha+10],1000)
# print(y[-1])