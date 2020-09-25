def f(n):
    """Fonction de Syracuse.
    Précondition : n est un entier strictement positif"""
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def syracuse(n):
    """Renvoie le premier entier k tel que f\^k(n) = 0.
    Précondition : n est un entier strictement positif"""
    x = n
    k = 0
    while x != 1:
        x = f(x)
        k = k + 1
        print('k=',k,'et x=',x)
    return k