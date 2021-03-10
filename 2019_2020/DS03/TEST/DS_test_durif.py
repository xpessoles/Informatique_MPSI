alpha=21

m=2**64
a=6364136223846793005
c=1442695040888963407

def next(x):
    return (a*x+c) % m

def conv(x, n):
    return int((x*n) // m) # on reconvertit en "petit" entier si possible

def cree_tableau(alpha):
    x = alpha
    x = next(x)
    x = next(x)
    n = 1000 + conv(x, 1000)
    t = [0] * n
    for i in range(n):
      x = next(x)
      t[i] = conv(x, 5000)
    return t

t = cree_tableau(alpha)
#Q1
N=len(t)
print('Q1 : '+str(N))

#Q2
c=0
for x in t:
    if x>=3000:
        c+=1

print('Q2 : '+str(c))

#Q3
c=0
for x in t:
    if x%3==0:
        c+=1

print('Q3 : '+str(c))

#Q4
c=0
for j in range(N):
    for i in range(j):
        if t[i]<t[j]:
            c+=1

print('Q4 : '+str(c))

#Q5

u=10+alpha
U=[u]
c=0
S=u
for i in range(1,10**4-1):
    u=15091*u%64007
    U.append(u)
    S+=u
    if u%17==0:
        c+=1
d=0
for i in range(1,10**4-2):
    if abs(U[i]-U[i+1])<=1000:
        d+=1



print('Q5 : '+str(U[42]))
print('Q6 : '+str(U[-1]))
#print('Q7 : '+str(c))
print('Q7 : '+str(d))
print('Q8 : '+str(S))


#Q9
with open('zeta5.txt','r') as f:
    data=f.readlines()

c=0
for ligne in data[2:]:
    ligne=ligne.split(' ')
    if len(ligne)==8:
        for b in ligne[:5]:
            for i in range(7):
                if int(str(b[i:i+4]))==2000+alpha:
                    c+=1

print('Q9 : '+str(c))

#Q10
c=0
for ligne in data[1:]:
    ligne=ligne.split(' ')
    if len(ligne)==8:
        b1=''
        for b in ligne[:5]:
            b1+=b
        for i in range(50-3):
            if int(str(b1[i:i+4]))==2000+alpha:
                c+=1

print('Q10 : '+str(c))

#Q11
c=0
b1=''
for ligne in data[2:]:
    ligne=ligne.split(' ')
    if len(ligne)!=8:
        if b1!='':
            for i in range(500-3):
                if int(str(b1[i:i+4]))==2000+alpha:
                    c+=1
        b1=''
    else:
        for b in ligne[:5]:
            b1+=b

print('Q11 : '+str(c))
#Q11
c=0
b1=''
for ligne in data[2:]:
    ligne=ligne.split(' ')
    if len(ligne)==8:
        for b in ligne[:5]:
            b1+=b

for i in range(int(1e6)-3):
    if int(str(b1[i:i+4]))==2000+alpha:
        c+=1

print('Q12 : '+str(c))











