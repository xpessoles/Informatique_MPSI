## Code corrigé CCP 2016

from numpy import *
import matplotlib.pyplot as plt
import random as rd

#Tailles

to=64*64*352*12/8

# Taux de compresion
tau=(to-1000000)/to

# entropie

H_exemple=-(2*0.3*log2(0.3)+4*0.1*log2(0.1))

S=[4,5,7,0,7,8,4,1,7,4]

def entropie(S):
    #Q4
    valeurs=list(set(S))
    #Q5
    proba=[S.count(i)/len(S) for i in valeurs]
    #Q6
    H=-sum([i*log2(i) for i in proba])
    return H

##################### Zone test ###################################
bloc_image=[rd.randint(0,4096) for i in range(64*32)]
###################################################################

#Q7
H=entropie(bloc_image)
print('Taux de compression limite',(12-H)/(12))


#Q8
def pretraitement12(donnees_brutes):
    luminance_moy=[]
    for i in range(64):
        somme=0
        for indice in [0,10,20,30]:
            somme+=donnees_brutes[indice][i]
        luminance_moy.append(somme/4)
    j_max=0
    luminance_max=luminance_moy[0]
    for j in range(64):
        if luminance_moy[j]>luminance_max:
            luminance_max=luminance_moy[j]
            j_max=j
    return(array([luminance_moy]),luminance_max,j_max)

#Q9
def pretraitement34(donnees_brutes,luminance_max,j_max):
    spectre_max=ones((32,1))
    for i in range(32):
        spectre_max[i][0]=donnees_brutes[i][j_max]
    spectre_max=spectre_max/luminance_max
    return spectre_max

#Q10
def pretraitement5(luminance_moy,spectre_max):
    matrice_modele=ones((32,64))
    for i in range(32):
        for j in range(64):
            matrice_modele[i][j]=luminance_moy[0][j]*spectre_max[i][0]
    return matrice_modele

######################### Zone test ################################
donnees_brutes=random.rand(32,64)
#donnees_brutes=ones([32,64])

lmoy,lmax,jmax=pretraitement12(donnees_brutes)

sm=pretraitement34(donnees_brutes,lmax,jmax)

mm=pretraitement5(lmoy,sm)

#print(mm)

#####################################################################

#Q12

def prediction(x):
    return [x[i]-x[i-1] for i in range(1,len(x))]# on pourrait mettre 32 à la place de len(x)
    
#Q13

def mappage(erreur,x):
    delta=[]
    for i in range(1,len(x)):
        theta=min([x[i-1],4095-x[i-1]])
        if erreur[i-1]<=theta and erreur[i-1]>=0:
            delta.append(2*erreur[i-1])
        elif erreur[i-1]<0 and erreur[i-1]>=-theta:
            delta.append(-2*erreur[i-1]-1)
        else:
            delta.append(theta-erreur[i-1])
    return delta
            

######################## Zone test ##################################
L=list(range(0,20,2))
#print(prediction(L))

x=[2025,2027,2032,2041,2050,2053,2052,2050]
erreur=prediction(x)
delta=mappage(erreur,x)
print(delta)
######################################################################

def codage(delta_k,p_opt):#résultat sous forme d'un tableau
    #Q15    
    quotient=delta_k//2**p_opt
    code1=[1 for i in range(quotient)]
    code1+=[0]
    #Q16
    reste=delta_k%2**p_opt#codable sur p_opt bits
    code2=[int(i) for i in bin(reste)[2:]]
    for i in range(p_opt-len(code2)):
        code2=[0]+code2
    code=code1+code2
    return code

#Q18
Gms=1.32724e20
Gmv=3.24916e14
rv=1.08209e11
omega=3.23639e-7
phi=0
eval_sm=lambda x,y,t:[-Gms*x/(x**2+y**2)**(3/2)-Gmv*(x-rv*cos(omega*t+phi))/((x-rv*cos(omega*t+phi))**2+(y-rv*sin(omega*t+phi)))**(3/2),-Gms*y/(x**2+y**2)**(3/2)-Gmv*(y-rv*sin(omega*t+phi))/((x-rv*cos(omega*t+phi))**2+(y-rv*sin(omega*t+phi))**2)**(3/2)]#lol

######################### Zone test ###################################
n=30*24*3600
delta_t=1
#######################################################################
#Q21- Je ne trouve pas de valeurs dans les sujet, j'ai mis la valeur du rayon moyen de l'orbite terrestre et la vitesse de libération
x=[149.6e9]#en m
y=[0]
u=[0]
v=[11200]

t=arange(0,n*delta_t,delta_t)

#Q22

 for i in range(1,n):
    x.append(x[-1]+delta_t*u[-1])
    y.append(y[-1]+delta_t*v[-1])
    cauchy=eval_sm(u[-1],v[-1],t[i-1])
    u.append(u[-1]+delta_t*cauchy[0])
    v.append(v[-1]+delta_t*cauchy[1])

#si on doit retourner des vecteurs sous frome d'array, on ajoute:
x=array([x])
y=array([y])
u=array([u])
v=array([v])

#Q23

def vitesse_sonde(u,v,t):#u et v sont des array (1,n)
    norme_v=sqrt(u[0]**2+v[0]**2)/1000#c'est ce qui est pratique avec les array!
    print(norme_v)
    plt.plot(t,norme_v)
    plt.xlabel('Temps (s)')
    plt.ylabel('Vitesse (km/s)')
    plt.title('Vitesse de la sonde')
    plt.grid()
    plt.show()