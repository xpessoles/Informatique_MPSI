import numpy as np
import matplotlib.pyplot as plt


def lire_accelero(fichier):
    with open(fichier,'r',encoding='utf8') as f:
        data=f.readlines()
        dT,X,Y,Z=[],[],[],[]
        for ligne in data:
            dt,x,y,z=ligne.split(',')
            dT.append(int(dt))
            X.append(int(x))
            Y.append(int(y))
            Z.append(int(z))
    return dT,X,Y,Z



def generer_acceleration(dT0,X0,Y0,Z0,alpha):
    dT,X,Y,Z=[],[],[],[]
    for i in range(0,len(dT0),alpha%5+1):
        dT.append(dT0[i]+alpha%9)
        if alpha%15<5:
            X.append(int(X0[i])+(-1)**alpha*alpha%7)
            Y.append(int(Y0[i])+(-1)**alpha*alpha%7)
            Z.append(int(Z0[i])+(-1)**alpha*alpha%7)
        elif alpha%15<10:
            X.append(int(Y0[i])+(-1)**alpha*alpha%7)
            Y.append(int(Z0[i])+(-1)**alpha*alpha%7)
            Z.append(int(X0[i])+(-1)**alpha*alpha%7)
        else:
            X.append(int(Z0[i])+(-1)**alpha*alpha%7)
            Y.append(int(X0[i])+(-1)**alpha*alpha%7)
            Z.append(int(Y0[i])+(-1)**alpha*alpha%7)
        dT[0]=0
    return dT,X,Y,Z

def export_acceleration(dT0,X0,Y0,Z0,alpha):
    dT,X,Y,Z=generer_acceleration(dT0,X0,Y0,Z0,alpha)
    with open('mesure_accelero'+'_'+str(alpha)+'.txt','w') as f:
        for i in range(len(dT)):
            f.write(str(dT[i])+','+str(X[i])+','+str(Y[i])+','+str(Z[i])+'\n')



dT0,X0,Y0,Z0=lire_accelero('mesure_accelero.txt')
alpha=10
dT,X,Y,Z=generer_acceleration(dT0,X0,Y0,Z0,alpha)

for a in range(1,99):
    export_acceleration(dT0,X0,Y0,Z0,a)


plt.clf()
plt.plot(dT)

#Q1

dT,X,Y,Z=lire_accelero('mesure_accelero_10.txt')
print('Q1 : '+str(len(dT)))


#Q2
def calculer_temps(dT):
    T=[0]
    for dt in dT[1:]:
        T.append(T[-1]+dt)
    return T
T=  calculer_temps(dT)
print('Q2 : '+str(T[-1]))

plt.clf()
plt.plot(T)
plt.savefig('q02_durif_emilien.png')


#Q3
def calculer_acceleration(X,Y,Z):
    AX,AY,AZ=[],[],[]
    for i in range(len(X)):
        AX.append(X[i]*10/255)
        AY.append(Y[i]*10/255)
        AZ.append(Z[i]*10/255)
    return AX,AY,AZ

T=calculer_temps(dT)
AX,AY,AZ=calculer_acceleration(X,Y,Z)

print('Q3 max(ax): '+str(max(AX)))
print('Q3 max(ay): '+str(max(AY)))
print('Q3 max(az): '+str(max(AZ)))

#Q04
plt.clf()
plt.plot(T,AX,'r',label='$a_x$')
plt.plot(T,AY,'g',label='$a_y$')
plt.plot(T,AZ,'b',label='$a_z$')
plt.legend()
plt.xlabel('temps en $\\mu s$')
plt.ylabel('accélération en $m/s^2$')
plt.savefig('q04_durif_emilien.png')

#Q05
def trapeze(A):
    V=[0]
    for i in range(1,len(A)):
        V.append(V[-1]+0.5*(A[i-1]+A[i]))
    return V

VX=trapeze(AX)
VY=trapeze(AY)
VZ=trapeze(AZ)


plt.clf()
plt.plot(T,VX,'r',label='$v_x$')
plt.plot(T,VY,'g',label='$v_y$')
plt.plot(T,VZ,'b',label='$v_z$')
plt.legend()
plt.xlabel('temps en $\\mu s$')
plt.ylabel('vitesse en $m/s$')
plt.savefig('q05_durif_emilien.png')


#Q06
print('Q6 max(vx): '+str(max(VX)))
print('Q6 max(vy): '+str(max(VY)))
print('Q6 max(vz): '+str(max(VZ)))


#Q07
def moyenne(A,T,tmax):
    i=0
    t=T[0]
    m=A[0]
    while t<tmax:
        i+=1
        m+=A[i]
        t=T[i]
    return m/(i+1)

mX1=moyenne(AX,T,2*1e6)
mY1=moyenne(AY,T,2*1e6)
mZ1=moyenne(AZ,T,2*1e6)

print('Q7 moy(ax): '+str(mX1))
print('Q7 moy(ay): '+str(mY1))
print('Q7 moy(az): '+str(mZ1))


#Q08
AX1=[ax-mX1 for ax in AX]
AY1=[ay-mY1 for ay in AY]
AZ1=[az-mZ1 for az in AZ]

print('Q8 max(ax): '+str(max(AX1)))
print('Q8 max(ay): '+str(max(AY1)))
print('Q8 max(az): '+str(max(AZ1)))

# plt.clf()
# plt.plot(T,AX1,'r',label='$a_x$')
# plt.plot(T,AY1,'g',label='$a_y$')
# plt.plot(T,AZ1,'b',label='$a_z$')
# plt.legend()
# plt.savefig('accelerations1.png')
#


#Q09
VX1=trapeze(AX1)
VY1=trapeze(AY1)
VZ1=trapeze(AZ1)
print('Q9 max(vx): '+str(max(VX1)))
print('Q9 max(vy): '+str(max(VY1)))
print('Q9 max(vz): '+str(max(VZ1)))



#Q10
plt.clf()
plt.plot(T,VX1,'r',label='$v_x$')
plt.plot(T,VY1,'g',label='$v_y$')
plt.plot(T,VZ1,'b',label='$v_z$')
plt.legend()
plt.xlabel('temps en $\\mu s$')
plt.ylabel('vitesse en $m/s$')
plt.savefig('q10_durif_emilien.png')


#Q11
X1=trapeze(VX1)
Y1=trapeze(VY1)
Z1=trapeze(VZ1)
print('Q11 max(vx): '+str(max(X1)))
print('Q11 max(vy): '+str(max(Y1)))
print('Q11 max(vz): '+str(max(Z1)))

#Q12
plt.clf()
plt.plot(X1,Y1)
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.savefig('q12_durif_emilien.png')