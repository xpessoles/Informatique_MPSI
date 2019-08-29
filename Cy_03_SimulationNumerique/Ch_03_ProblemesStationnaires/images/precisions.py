from math import sin, cos, log, sqrt, pi
import matplotlib.pyplot as plt
def dichotomie_for(f, a, b, n):
    """Itérations de la dichotomie pour f(x)=0
       Préconditions : f(a) * f(b) <= 0
                       f continue sur [a,b]
                       epsilon > 0"""
    c, d = a, b
    fc, fd = f(c), f(d)
    L = []
    for i in range(n+1):
        m = (c + d) / 2.
        L.append(m)
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
    return L

def newton_for(f, fp, x0, n):
    """Itérations de la méthode de Newton pour f=0
       départ : x0, f' = fp, critère d'arrêt epsilon"""
    u = x0
    v = u - f(u)/fp(u)
    L = [u]
    for i in range(n):
        u, v = v, v - f(v)/fp(v)
        L.append(u)
    return L

def secante_for(f,u0,u1,n):
    """Zéro de f par la méthode de la sécante
    u0,u1 : deux premiers points
    eps : critère d'arrêt"""
    u,v = u0,u1
    L = [u]
    for i in range(n):
        p = (f(u)-f(v)) / (u-v)
        u,v = v,u - f(u)/p
        L.append(u)
    return L

def f(x) :
    return x**2-2

def fp(x) :
    return 2*x

def erreur(x,z):
    """log10 de l'erreur d'approximation de z par x"""
    if abs(x-z) <= 10**-16 : 
        return -16
    else : 
        return log(abs(x-z),10)

def compare_newton(n,nom_de_fichier):
    les_k = list(range(n+1))
    carre = newton_for(f,fp,2,n)
    y1 = [abs(c-sqrt(2)) for c in carre]
    sinus1 = newton_for(sin,cos,2,n)
    y2 = [abs(s-pi) for s in sinus1]
    sinus2 = newton_for(sin,cos,1,n)
    y3 = [abs(s) for s in sinus2]
    plt.clf()
    plt.plot(les_k,y1,'-b',label="$f:x\\mapsto x^2-2,\\ u_0=2,\\ \\ell=\\sqrt{2}$",linewidth=3)
    plt.plot(les_k,y2,'--r',label="$f=\\sin,\\ u_0=2,\\ \\ell=\\pi$",linewidth=3)
    plt.plot(les_k,y3,'-.g',label="$f=\\sin,\\ u_0=1,\\ \\ell=0$",linewidth=3)
    plt.xlabel("$n$")
    plt.ylabel("$\\left| u_n - \\ell \\right|$")
    plt.yscale('log')
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)

def compare_dicho_newton(n,nom_de_fichier):
    les_k = list(range(n+1))
    carren = newton_for(f,fp,2,n)
    y1 = [abs(c-sqrt(2)) for c in carren]
    carred = dichotomie_for(f,1,2,n)
    y2 = [abs(d-sqrt(2)) for d in carred]
    plt.clf()
    plt.plot(les_k,y1,'-b',label="Méthode de Newton, $u_0=2$",linewidth=3)
    plt.plot(les_k,y2,'--r',label="Méthode de la dichotomie sur $[1,2]$",linewidth=3)
    plt.xlabel("$n$")
    plt.ylabel("$\\log_{10}\\left| u_n - \\sqrt{2} \\right|$")
    plt.yscale('log')
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)

def compare_dicho(n,nom_de_fichier):
    les_k = list(range(n+1))
    carre = dichotomie_for(f,1,2,n)
    y1 = [erreur(c,sqrt(2)) for c in carre]
    sinus1 = dichotomie_for(sin,3,4,n)
    y2 = [erreur(s,pi) for s in sinus1]
    sinus2 = dichotomie_for(sin,-.5,.5,n)
    y3 = [erreur(s,0) for s in sinus2]
    plt.clf()
    plt.plot(les_k,y1,'-b',label="$f:x\\mapsto x^2$, sur $[1,2]$",linewidth=3)
    plt.plot(les_k,y2,'--r',label="$f=\\sin$, sur $[3,4]$",linewidth=3)
    plt.plot(les_k,y3,'-.g',label="$f=\\sin$, sur sur $[-1/2,1/2]$",linewidth=3)
    plt.xlabel("$n$")
    plt.ylabel("$\\log_{10}\\left| u_n - \\ell \\right|$")
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)

def compare_newton_secante(n,nom_de_fichier):
    les_k = list(range(n+1))
    carren = newton_for(f,fp,2,n)
    y1 = [abs(c-sqrt(2)) for c in carren]
    carres = secante_for(f,2,1,n)
    y2 = [abs(d-sqrt(2)) for d in carres]
    plt.clf()
    plt.plot(les_k,y1,'-b',label="Méthode de Newton, $u_0=2$",linewidth=3)
    plt.plot(les_k,y2,'--r',label="Méthode de la sécante, $u_0=2$, $u_1=1$",linewidth=3)
    plt.xlabel("$n$")
    plt.ylabel("$\\left| u_n - \\sqrt{2} \\right|$")
    plt.yscale('log')
    plt.legend(loc=0)
    plt.savefig(nom_de_fichier)

if __name__ == '__main__':
    compare_newton(5,'precision_newton.png')
    compare_newton_secante(6,'comparaison_newton_secante.png')

