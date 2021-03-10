from math import log
import matplotlib.pyplot as plt

alpha=44

def calcule_u(n):
    u=alpha+1
    for k in range(n):
        u+=log(u)
    return u

Q1=calcule_u(alpha+100)
print('Q1 : '+str(Q1))

Q2=calcule_u(alpha+50)
print('Q2 : '+str(Q2%3))

def u_depasse(alpha):
    u=alpha+1
    n=0
    while u<=10+alpha:
        u+=log(u)
        n+=1
    return n

print('Q3 : '+str(u_depasse(alpha)))

def calcule_su(n):
    u=alpha+1
    S=0
    for k in range(n):
        u+=log(u)
        S+=u
    return S

print('Q4 : '+str(calcule_su(10000+alpha)))

#generation altitude

def generer_altitude(alpha):
    alt0= [300, 500, 600, 1000, 800, 900, 500, 600, 200, 0]
    alt0=(alpha%4+1)*alt0
    alt0=alt0[alpha%3:-1-alpha%2]
    alt=[]
    for i,x in enumerate(alt0):
        delta=(-1)**i*((alpha+i%3)*739)%79
        alt.append(x+delta)
    return alt

alt=generer_altitude(alpha)

# plt.clf()
# for k in range(101):
#     alt=generer_altitude(k)
#     plt.plot(alt)
#     print(len(alt))
#
# plt.show()

print('Q5 : '+str(len(alt)))

def altmax(alt):
    m = 0
    for x in alt:
        if x > m:
            m = x
    return m

print('Q6 : '+str(altmax(alt)))


def denivmax(alt):
    x, m ,t= 0, 0,0
    for i,y in enumerate(alt):
        if y - x > m:
            m = y - x
            t=i+1
        x = y
    return m,t

print('Q7 : '+str(denivmax(alt)[0]))

print('Q8 : '+str(denivmax(alt)[1]))

def denivtotal(alt):
    x, d = 0, 0
    for y in alt:
        if y - x > 0:
            d += y - x
        x = y
    return d

print('Q9 : '+str(denivtotal(alt)))

def sommets(alt):
    s = []
    x, y = 0, alt[0]
    for z in alt[1:]:
        if x < y and z < y:
            s.append(y)
        x, y = y, z
    return s

print('Q10 : '+str(len(sommets(alt))))




