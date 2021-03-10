from numpy import array
import matplotlib.pyplot as plt

def euler(f, a, b, y0, h):
    t, y = a, y0
    t_list, y_list = [a], [y0]
    while t + h <= b:
        y = y + h*f(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list

alpha = 32
a = alpha * 10**(-2)
b = alpha * 10**(-3)
c = alpha*1e-2
# c = a
d = (alpha/5) * 10**(-3)

def f(x, t):
    u, v = x[0], x[1]
    return array([u*(a - b*v), (-v)*(c - d*u)])

# t_list, y_list = euler(f, 0, 300, array([alpha, alpha+300]), 0.01)
t_list_abid, y_list_abid = euler(f, 0, 300, array([alpha, alpha+10]), 0.01)

u_abid=[y[0] for y in y_list_abid]
v_abid=[y[1] for y in y_list_abid]

plt.clf()
plt.plot(t_list_abid,u_abid,label='Proie Abid')
plt.plot(t_list,u_list,label='Proie')
#plt.plot(t_list,v_list,label='Prédateur')
plt.show()

print(y_list[-1])