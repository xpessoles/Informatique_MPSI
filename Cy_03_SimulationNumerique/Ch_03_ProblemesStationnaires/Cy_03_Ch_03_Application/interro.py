import matplotlib.pyplot as plt
def euler(F,a,b,y0,h):
    y=y0
    t = a
    y_list = [y0]
    t_list = [a]
    while t+h <= b:
        y = y+h*F(y,t)
        y_list.append(y)
        t = t+h
        t_list.append(t)
    return t_list,y_list

def F4(y,t):
    alpha = 2
    return -alpha*y

y0 = 1
les_t,les_y = euler(F4,0,5,y0,0.01)
plt.plot(les_t,les_y)
#plt.show()


def F5(y,t):
    alpha = 1
    beta=.1
    return -alpha*y/beta

y0 = 1
les_t,les_y = euler(F5,0,5,y0,0.01)
plt.plot(les_t,les_y)
plt.show()

def F6(X,t):
    y,yp = X
    
    ypp = (1-y-byp)/a
