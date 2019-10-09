from math import sqrt

def f(x):
    if x >= -4 and x<= -2:
        return 2
    elif x >= -2 and x <= 0:
        return -x
    elif x >= 0 and x <= 4:
        return 0
    else:
        return "non définie"
        
def prod_impairs(n):
    produit=1
    for i in range(2*n+2):
        if i%2==1:
            produit=produit*i
    return (produit)



def suite():
    
    n=1
    somme=1
    while somme<1000:
        print(n)
        somme+=sqrt(1/n)
        n+=1
    return n





def fonction(k):
    a=len (str(abs(k)))
    return a


def nb_chiffres(nombre):
    n=0
    while(nombre>0):
        nombre//=10
        n+=1
    return n

def f2(x):
    print(x*x)
    
somme = 0
for k in range(16):
    produit = 1
    for i in range(1,k+1):
        produit *= i
    somme += 1/produit
# print(somme)