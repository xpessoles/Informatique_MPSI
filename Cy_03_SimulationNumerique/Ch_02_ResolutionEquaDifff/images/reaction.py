import matplotlib.pyplot as plt

def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a] # la liste des temps
    while t+h <= b:
        # Variant : floor((b-t)/h)
        # Invariant : au tour k, y_list = [y_0,...,y_k], t_list = [t_0,...,t_k]
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list

A0 = 1 # mol
alpha = 1 # s**-1
t0,t1,h = 0,6,.1

def F(y,t) :
    return -alpha*y

t_list,A_list = euler(F,t0,t1,A0,h)
plt.plot(t_list,A_list)
plt.xlabel('Temps ($s$)')
plt.ylabel('Concentration ($mol$)')
plt.grid()
plt.savefig('reaction_ordre1.png')
