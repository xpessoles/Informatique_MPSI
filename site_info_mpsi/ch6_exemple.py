def recherche(m,s):
    """Recherche le mot m dans la chaîne s
    Préconditions : m et s sont des chaînes de caractères"""
    long_s = len(s) # Longueur de s
    long_m = len(m) # Longueur de m
    for i in range(long_s-long_m+1):
        # Invariant : m n'a pas été trouvé dans s[0:i+long_m-1]
        print(s[i:i+long_m])
        if s[i:i+long_m] == m: # On a trouvé m
            return True
    return False

print(recherche('42','Les 7 samouraïs'))