import numpy as np
import matplotlib.pyplot as plt

"""Partie 1: queqlques listes pour faire les tests"""

name='test.png'
xtest1=[-1,0,1]
ytest1=[3,3,4]

xtest2=[-2,7,9,4,3]
ytest2=[0.5,-4,-2,0.2,10]


xtest3=[-2,-0.5,8,-1,2,4]
ytest3=[-5,4,8,0,-3,7]

pointstest1=[[1,2],[4,3],[7,4],[8,6]]
pointstest2=[(1,2),(4,8)]

xtest12=[1,1,0]

xprof1=[]
yprof1=[]

xprof2=[]
yprof2=[]

pointsprof=[]

"""Partie 2: quelques fonctions de calcul, de recherche et de traçage, utiles pour la suite"""

def carre(x):
    return x**2

def integrale(a,b,p,N):
#Approximation de l'intégrale de a à b de f, Méthode des trapèzes, N trapèzes
    S = 0.5*(Horner(p,a) + Horner(p,b))
    h = (b-a)/N
    for k in range(1,N) :
        S = S + Horner(p,a + k*h)
    return S*h


def polynom_sympas(x):
        return 4*x**3 + 3*x**2 + 2*x +1

def facto(n):
    facto = 1
    for i in range(1,n+1):
        facto = facto*i
    return facto

def moins_un_puissance_n(n):
    return (-1)**n

def suitesympa(n):
    return n * (-1)**n

def moyenne(L):
    return sum(L)/len(L)

def variance(L):
    moy = moyenne(L)
    for i in range(len(L)):
        L[i] = (L[i]**2)
    return moyenne(L)-(moy**2)

def ecarttype(L):
    return variance(L)**(1/2)

def indicemini(L):
    im = 0
    for i in range(1,len(L)):
        if L[i]<L[im]:
            im = i
    return im

def conversion(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    return x,y

def Horner(p,x):
    eval = p[0]
    for coeff in p[1:]:
        eval = eval*x + coeff
    return eval

def graph(p,a,b):
    x = np.linspace(a,b,(b-a)*1000+1)
    y = []
    y2 = []
    for i in x:
        y.append(Horner(p,i))
        y2.append(0)
    plt.clf()
    plt.plot(x,y)
    plt.plot(x,y2,color='k')
    plt.show()
def graphorthonorme(p,a,b):
    x = np.linspace(a,b,(b-a)*1000+1)
    y = []
    y2 = []
    for i in x:
        y.append(Horner(p,i))
        y2.append(0)
    plt.clf()
    plt.axis('equal')
    plt.plot(x,y)
    plt.plot(x,y2,color='k')
    plt.show()

def partiesliste(a):
    p = []
    i, imax = 0, 2**len(a)-1
    while i <= imax:
        s = []
        j, jmax = 0, len(a)-1
        while j <= jmax:
            if (i>>j)&1 == 1:
                s.append(a[j])
            j += 1
        p.append(s)
        i += 1
    return p

def sommepolys(L):
    p = []
    for i in range(len(L[0])):
        somme = 0
        for j in range(len(L)):
            somme = somme + L[j][i]
        p.append(somme)
    return p

def estpossible (x,y):
    count = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] == x[j]:
                count = count +1
    if len(x) != len(y):
        count = -1
    if count != 0:
       return False
    else :
        return True
"""Partie 3: l'interpolation de Lagrange"""

def interpolation(x,y):
#On vérifie d'abord que l'interpolation est possible. Pour cela, on compte le nombre de double présence d'une abscisse dans la liste x, et on vérifie que les listes ont bien la bonne taille. Le message d'erreur adéquat est renvoyé si nécessaire.
    count = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] == x[j]:
                count = count +1
    if len(x) != len(y):
        count = -1
    if count != 0:
        if count == -1:
            return "vos deux listes n'ont pas de la même taille"
        else:
            return "l'une des abscisses est en double"
    else:
#Si tout va bien, on peut lancer l'interpolation.
#On commence par noté n la taille de x, pusiqu'on va le réutiliser plusieur fois.
        n = len(x)
#On crée ensuite l'ensemble des polynômes de bases de l'interpolation. Ce sont tous les (X - x_1)(X - x_2)...(X- x_n), auquel on enlève chaque valeur de la liste x une fois. On représente comme une liste de racines [x_1 , x_2 ... x_n].
        polyliste = []
        for i in range(n):
            L = []
            for j in x:
                if x[i] != j:
                    L.append(j)
            polyliste.append(L)
#On crée ensuite la liste des coefficients multiplicateurs correspondants à chaque polynômes, qui sont y_i / P(i), ou P(i) est l'évaluation du iè polynôme crée précédemment, (c'est à dire le produit des (X - x[j]),pour j != i).
        coeffliste = []
        for i in range(n):
            coeff = 1
            for j in range(n):
                if j != i:
                    coeff = coeff*(x[i]-x[j])
            coeffliste.append(coeff**-1 * y[i])
#Ainsi, chaque polynôme de polyliste multiplié par son coefficient multiplicateur respectif vaut y_i en x_i, et 0 pour tout autre x_j dans x
#Ensuite, chaque polynôme est réécrit sous forme de liste de ses coefficients, du plus dominant jusqu'au coefficient constant. Chaque coefficient i étant la somme des produits éléments de chaque combinaison possible de i éléments parmi les racines.
        polyasommer = []
        for i in range(n):
            polycoefficient = []
            p = (partiesliste(polyliste[i]))
            for i in range(n):
                somme = 0
                for j in p:
                    if len(j) == i:
                        produit = 1
                        for k in range(i):
                            produit = produit*-j[k]
                        somme = somme + produit
                polycoefficient.append(somme)
            polyasommer.append(polycoefficient)

#Il ne reste plus qu'à coefficienter ces polynômes, en multipliant chaque coefficient de chaque polynôme par le coeficient multiplicateur allant correspondant au polynôme.
        for i in range(n):
            for j in range(len(polyasommer[i])):
                polyasommer[i][j] = polyasommer[i][j]*coeffliste[i]
#Enfin, on somme les polynômes et on renvoie le résultat
        return sommepolys(polyasommer)




def tracage(x,y,p,nom_fichier):
#Cette fonction permet de tracer le graph du polynôme obtenu p, auquel on rajoute les points demandés pour vérifier que tout semble foncitonner.
    delta = (max(x)-min(x))/32
    abs = np.linspace(min(x)-delta,max(x)+delta,1000*len(x)+1)
    ord = []
    for w in abs:
        ord.append(Horner(p,w))
    plt.clf()
    plt.plot(abs,ord,color='b')
    plt.plot(x,y,color='r',linestyle='',marker='*')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.autoscale(axis='2', tight='2')
    plt.title("Tracé du polynôme d'interpolation de Lagrange")
    plt.savefig(nom_fichier)
    plt.show()

def lagrange(x,y,nom_fichier):
#C'est cette fonction là que l'on utilisera. En plus de renvoyer les coefficients ou les erreurs, elle trace le polynôme et rajoute les points par dessus pour verifier que cela fonctionne
    p = interpolation(x,y)
    if type(p) == str:
        return p
    else:
        tracage(x,y,p,nom_fichier)
        return p

"""Partie 4: Quelques fonctions dérivées"""

def lagrangepoints(points,nom_fichier):
#Cette fonction permet de réaliser une interpolation à partir d'une liste de points
    x,y = conversion(points)
    p = lagrange(x,y,nom_fichier)
    return p


def evallagrange(x,y,x0):
#Cette fonciton évalue le polynôme d'interpolation de Lagrange de x et y en x0.
    p = interpolation(x,y)
    return Horner(p,x0)

def randomlagrange(a,b,c,d,n,nom_fichier):
#choisis aléatoirement n points dont les abscisses sont comprises entre a et b et les ordonnées entre d et d, et trace le polynôme d'ineterpolation qui lui est associé
    x = np.random.random(n) *(a-b) - a
    y= np.random.random(n) *(c-d) -c
    p = lagrange(x,y,nom_fichier)
    return p

def randomlagrangecentre(a,n,nom_fichier):
#fait la même chose, mais centre l'aléatoire pour x et pour y dans un rayon de a autour de 0
    x=np.random.random(n)*2*a - a
    y=np.random.random(n)*2*a - a
    p = lagrange(x,y,nom_fichier)
    return p

"""Partie 5: Recherche du meilleur polynôme d'un degré infiérieur"""

def erreur(y2,y):
    #C'est ici que l'on définie l'erreur d'approximation du polynôme. y est la liste des ordonnées cherchées, y2 la liste des ordonnées obtenues, on fait la moyenne des carrés des écarts.
    erreur=[]
    for i in range(len(y)):
        erreur.append((y2[i]-y[i])**2)
    return moyenne(erreur)

def approximationdegfixe(x,y,m,nom_fichier):
    count = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] == x[j]:
                count = count +1
    if len(x) != len(y):
        count = -1
    if count != 0:
        if count == -1:
            return "vos deux listes n'ont pas de la même taille"
        else:
            return "l'une des abscisses est en double"
    else:
        partiesx = partiesliste(x)
        partiesy = partiesliste(y)
        erreurs = []
        polysfaits = []
        for i in range(len(partiesx)):
            if len(partiesx[i]) == m+1:
                l = lagrang(partiesx[i],partiesy[i])
                y2 =[]
                for j in x:
                    y2.append(Horner(l,j))
                erreurs.append(erreurmoyenne(y,y2))
                polysfaits.append(i)
        erreurmin = min(erreurs)
        indice_du_meilleur_polynome = indicemini(erreurs)
        meilleur_polynome = polysfaits[indice_du_meilleur_polynome]
        polylagrange = interpolation(partiesx[meilleur_polynome],partiesy[meilleur_polynome])
        tracage(x,y,polylagrange,nom_fichier)
        return polylagrange

def approximationdegmax(x,y,m,nom_fichier):
    count = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] == x[j]:
                count = count +1
    if len(x) != len(y):
        count = -1
    if count != 0:
        if count == -1:
            return "vos deux listes n'ont pas de la même taille"
        else:
            return "l'une des abscisses est en double"
    else:
        partiesx = partiesliste(x)
        partiesy = partiesliste(y)
        erreurs = []
        polysfaits = []
        for i in range(len(partiesx)):
            if 1 <= len(partiesx[i]) <= m+1:
                l = lagrang(partiesx[i],partiesy[i])
                y2 =[]
                for j in x:
                    y2.append(Horner(l,j))
                erreurs.append(erreurmoyenne(y,y2))
                polysfaits.append(i)
        erreurmin = min(erreurs)
        indice_du_meilleur_polynome = indicemini(erreurs)
        meilleur_polynome = polysfaits[indice_du_meilleur_polynome]
        polylagrange = interpolation(partiesx[meilleur_polynome],partiesy[meilleur_polynome])
        tracage(x,y,polylagrange,nom_fichier)
        return polylagrange


"""Partie 6: on fait des stats"""

def randominterpolationcentre(a,n):
#fait la même chose, mais centre l'aléatoire pour x et pour y dans un rayon de a autour de 0, sans tracer
    x=np.random.random(n)*2*a - a
    y=np.random.random(n)*2*a - a
    p = interpolation(x,y)
    return p



def stats_random_centre(a,p,m,nom_fichier_moyenne,nom_fichier_ecarttype):
#ici, on réalise m interpolations aléatoires de n points centrés en 0 dans un rayon de n. On note les coefficients de chaque polynôme, puis on fait l'écart type et la moyenne afin de rechercher un lien possible entre a et n, et les moyennes et variances.
    polys=[]
    for i in range(m):
        polys.append(randominterpolationcentre(a,p))
    coefficients = []
    for i in range(p):
        coefficients.append([])
    for i in range(p):
        for j in range(m):
            coefficients[i].append(polys[j][i])
    ecarttypes = []
    moyennes = []
    for i in coefficients:
        ecarttypes.append(ecarttype(i))
        moyennes.append(moyenne(i))
    plt.clf()
    plt.bar(range(1,len(moyennes)+1),moyennes, color='b', width = 0.5)
    plt.title('valeurs moyennes des coefficients (par degrés décroissants)')
    plt.xlabel('dominance du coeffient')
    plt.ylabel('coefficient moyen')
    plt.show()
    plt.savefig(nom_fichier_ecarttype)
    plt.clf()
    plt.bar(range(1,len(ecarttypes)+1),ecarttypes,color = 'r',width=0.5)
    plt.title('écart-types des coefficients (par degré décroissant')
    plt.xlabel('coefficient')
    plt.ylabel('écart-type')
    plt.show()
    plt.savefig(nom_fichier_moyenne)
    return moyennes, ecarttypes

#On va ici faire la même chose, mais en fesant varié a de 2**-n à 2**n, on va ensuite tracer les suites des moyennes des cofficients et des ecart-types des coefficients. n est la moitié du nombre de points, m le nombre de polynomes aléatoirement générés, p est le nombre de points de l'interpolation (ne pas dépasser 4-5).

def suitestatsrandom(n,m,p,nom_fichier_moyenne,nom_fichier_ecarttype):
    moys=[]
    ectypes = []
    indices=[]
    for i in range(p):
        moys.append([])
        ectypes.append([])
    for i in range(-n,n+1):
        polys = []
        for j in range(m):
            polys.append(randominterpolationcentre(2**i,p))
        coefficients = []
        for j in range(p):
            coefficients.append([])
        for j in range(p):
            for k in range(m):
                coefficients[j].append(polys[k][j])
        ecarttypes = []
        moyennes = []
        for j in coefficients:
            ecarttypes.append(ecarttype(j))
            moyennes.append(moyenne(j))
        for j in range(p):
            moys[j].append(moyennes[j])
            ectypes[j].append(ecarttypes[j])
        indices.append(i)
    plt.clf()
    for i in range(len(moys)):
        plt.plot(indices,moys[i],marker = '*',linestyle = '')
    plt.legend('0123456789')
    plt.yscale('log')
    plt.show()
    plt.savefig(nom_fichier_moyenne)

    for i in range(len(moys)):
        plt.plot(indices,ectypes[i],marker = '*',linestyle = '')
    plt.legend('0123456789')
    plt.yscale('log')
    plt.show()
    plt.savefig(nom_fichier_ecarttype)




"""Partie 7: Et si on fesait des suites ?"""

#Voici quelques suites simples que l'on pourra utiliser
def suitegeometrique(u0,q,n):
    return u0 * q**n

def suitearithmetique(u0,r,n):
    return u0 + r*n

def suiteexponentielle(K,c,n):
    return K*np.exp(c*n)

def suitelogarithmique(K,c,n):
    return K+np.log(c+n)


def serieharmonique(n):
    H = 0
    for i in range(1,n+1):
        H += 1/i
    return H


#Nous allons d'abord étudier la progression de la suite des coefficients dominants, ainsi que celle des coefficients constant lorsque les abscisses sont les n premiers éléments de la suite logarithmique avec K=0 et c = 1 et lorsque les ordonées sont les n premiers éléments de la serie harmonique, (avec H0 = 0)
#attention, au dela de 14 cela devient très lent, mais il suffit d'aller jusqu'a 10 pour voir le résultat : il semble sans appel

def suitecoeffs1(n,nom_fichier):
    x = []
    y = []
    u = []
    v = []
    indices = []
    for i in range(n):
        x.append(suitelogarithmique(0,1,i))
        y.append(serieharmonique(i))
        indices.append(i)
        l = interpolation(x,y)
        u.append(l[0])
        v.append(l[-1])
    zeros = [0]*(n)
    plt.clf()
    plt.plot(indices,zeros,color= 'k',linestyle='--')
    plt.plot(indices,u,linestyle = '',marker='*',color='r')
    plt.plot(indices,v,linestyle = '',marker='*',color='b')
    plt.ylabel('coefficiant dominants en rouges, constante en bleu')
    plt.legend('0uv')
    plt.show()
    plt.savefig(nom_fichier)
    return l

#Nous allons ensuite étudier la progression des 5 suites de coefficients lorsque les abscisses sont les 5 premiers termes de la suite géométrique de raison n et de premier terme 1, et lorsque les ordonnées sont les 5 premiers éléments de la suite arithémtique de raison n et de premier terme nul.

def suitecoeffs2(n,nom_fichier):

    u = [[],[],[],[],[]]
    indices = []
    for i in range(2,n+1):
        x = []
        y = []
        for j in range(5):
            x.append(suitegeometrique(1,i,j))
            y.append(suitearithmetique(0,i,j))
        l = interpolation(x,y)
        for j in range(5):
            u[j].append(l[j])
        indices.append(i)
    plt.clf()
    zeros = [0]*(n-1)
    plt.plot(indices,zeros,linestyle = '--',color='k')
    for j in range(5):
        plt.plot(indices,u[j],linestyle = '',marker='*')
    plt.legend('0123456789')
    plt.show()
    plt.savefig(nom_fichier)

"""Partie 8 : Lagrange à l'infini"""

#Nous allons maintenant étudier la progression des coefficients de l'interpolation dans une suite qui à chaque terme transforme la liste des ordonnées y en liste des abscisses x , et la liste des coefficients en liste des ordonnées pour interpoler à nouveau, si possible bien entendu.

def infinilagrange(x, y, n , nom):
    u=[]
    indice=[]
    coeffs=[]
    k=0
    a=x
    b=y
    while k<n and estpossible(a,b):
        indice.append(k)
        b,a =interpolation(a,b),b
        u.append(b)
        k+=1
    for i in range (len(u[0])):
        coeffs.append([])
        for j in range(len(u)):
            coeffs[i].append(u[j][i])
    plt.clf()
    for i in range (len(coeffs)):
        plt.plot(coeffs[i],marker = '*',linestyle='')
    plt.yscale('log')
    plt.legend("0123456789")
    plt.show()
    plt.savefig(nom)

def infinilagrange2(x, y, n , nom):
    u=[]
    indice=[]
    coeffs=[]
    k=0
    a=x
    b=y
    while k<n and estpossible(a,b):
        indice.append(k)
        a,b =interpolation(a,b),a
        u.append(b)
        k+=1
    for i in range (len(u[0])):
        coeffs.append([])
        for j in range(len(u)):
            coeffs[i].append(u[j][i])
    plt.clf()
    for i in range (len(coeffs)):
        plt.plot(coeffs[i],marker = '*',linestyle='')
    plt.yscale('log')
    plt.legend("0123456789")
    plt.show()
    plt.savefig(nom)

def randominfinilagrange (a,m,n, nom):
    x=np.random.random(m)*2*a - a
    y=np.random.random(m)*2*a - a
    infinilagrange(x,y,n,nom)

"""Partie 9: approximation d'une fonction grâce à une interpolation"""

#On cherche à approximé une fonction f par un polynôme. Pour cela, on crée le polynôme d'interpolation des familles x et f(x), puis on renvoie le polynôme. Ce polynôme est proche de la fonction autour des points d'abcsisses de la liste x.

def approx_lagrange(x,f,nom_fichier):
    y = []
    for i in x:
        y.append(f(i))
    lagrange(x,y,nom_fichier)
    return interpolation(x,y)


"""Partie 10 : Et si on fesait du dessin ?"""

#Cette fonction permet de tracer la partie de la figure souhaitée.


def graphfigure(p,a,b,couleur):
    x = np.linspace(a,b,(b-a)*1000+1)
    y = []
    y2 = []
    for i in x:
        y.append(Horner(p,i))
    plt.plot(x,y,color=couleur)


#On va maintenant dessiner un coeur a partir de 2 parmaètres. Les coubres sont des polynômes d'interpolation, passants par des points stratégiques

def coeur(a,b,couleurint,couleurbord,nom_fichier):
    c = a*np.sqrt(2)/4
    xg = [-a,-a/2 -c,-a/2,-a/2 +c,0]
    xd = [a, a/2 + c, a/2, a/2 - c, 0]
    yh = [0,c,a/2,c,0]
    yb = [0,-b/2,-5*b/6,-19*b/20,-b]

    p1 = interpolation(xd,yh)
    p2 = interpolation(xg,yb)
    p3 = interpolation(xd,yb)
    p4 = interpolation(xg,yh)

    xg=np.linspace(-a,0,1000*a+1)
    xd=np.linspace(0,a,1000*a+1)
    ybg=[]
    yhd=[]
    ybd=[]
    yhg=[]
    for i in range (len(xg)):
        ybg.append(Horner(p2,xg[i]))
        yhd.append(Horner(p1,xd[i]))

    for i in range(len(xg)):
        ybd.append(ybg[-i-1])
        yhg.append(yhd[-i-1])
    plt.clf()

    plt.xticks([],[])
    plt.yticks([],[])
    plt.axis('equal')
    plt.fill_between(xd, yhd, ybd, where=ybd<yhd, color=couleurint)
    plt.fill_between(xg, yhg, ybg, where=ybg<yhg, color=couleurint)
    graphfigure(p1,min([0,a]),max([0,a]),couleurbord)
    graphfigure(p2,min([0,-a]),max([0,-a]),couleurbord)
    graphfigure(p3,min([0,a]),max([0,a]),couleurbord)
    graphfigure(p4,min([0,-a]),max([0,-a]),couleurbord)
    plt.show()
    plt.savefig(nom_fichier)

#On va maintenant essayer de tracer un cercle
#Cette fonction trace un polygone régulier encré dans un cercle de rayon 1, qualitatif. Il se rapproche d'un cercle quand n tend vers l'infini

def polygoneregulier(n,nom_fichier):
    x= []
    y = []
    z = np.linspace(0,np.pi*2,n+1)
    for i in z:
        x.append(np.cos(i))
        y.append(np.sin(i))
    plt.clf()
    plt.axis('equal')
    plt.plot(x,y)
    plt.show()

#On calcul le polynôme qui passe par n points du demi de cercle également répartis

def demicerclelagrange(n):
    x= []
    y = []
    z = np.linspace(0,np.pi,n)
    for i in z:
        x.append(np.cos(i))
        y.append(np.sin(i))
    return interpolation(x,y)

#On calculs les polynômes passant par les cercles les un après les autres, on calcul leur intégrale pour vérifier si cela tend bien vers pi/4
def suitedemicercle(n):
    u = []
    indices = []
    for i in range(1,n+1):
        u.append(integrale(-1,1,demicerclelagrange(i),100))
        indices.append(i)
    plt.clf()
    plt.plot(indices,u,marker='*',color='r',linestyle='')
    plt.show()

def quartcerclelagrange(n):
    x= []
    y = []
    z = np.linspace(0,np.pi/2,n)
    for i in z:
        x.append(np.cos(i))
        y.append(np.sin(i))
    return interpolation(x,y)

#On calculs les polynômes passant par les cercles les un après les autres, on calcul leur intégrale pour vérifier si cela tend bien vers pi/4
def suitequartcercle(n):
    u = []
    indices = []
    for i in range(1,n+1):
        u.append(integrale(0,1,quartcerclelagrange(i),100))
        indices.append(i)
    plt.clf()
    plt.plot(indices,u,marker='*',color='r',linestyle='')
    plt.show()

def suitemorceauxdecercle(m,n,nom_fichier):
    ecartypes=[]
    indices=[]
    for i in range(1,n+1):
        u = []
        indices.append(i)
        for j in range(1,m+1):
            u.append((integrale(np.cos(np.pi/(2**i)),1,quartcerclelagrange(j),100))+(np.cos(np.pi/(2**i))*np.sin(np.pi/(2**i))/2))
        ecartypes.append(ecarttype(u))
    plt.clf()
    plt.plot(indices,ecartypes)
    plt.show()


















