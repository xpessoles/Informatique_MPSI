def moy(T):
    """moyenne du tableau de nombres T"""
    n = len(T)
    S = 0
    for e in T :
        S = S + e
    return S / n

def moyennes(fichier_notes,fichier_moyennes,sep=','):
    """Lit fichier_notes
       Pour chaque étudiant, calcule sa moyenne
       Écrit le résultat dans fichier_moyennes
       Format prévu : csv, séparateur sep"""
    # On lit fichier_notes
    etudiants = [] # Tableau des étudiants
    with open(fichier_notes,'r') as f :
        # Première ligne : titres
        titres = [f.readline().split(sep)[0],'Moyenne']
        # Ensuite : données des étudiants
        T = f.readlines()
    for e in T :
        L = e.strip().split(sep)
        prenom = L[0]
        notes = []
        for x in L[1:]:
            if x != '':
                notes.append(float(x))
        etudiants.append([prenom, str(moy(notes))])
    # On écrit fichier_moyennes
    with open(fichier_moyennes,'w') as f :
        # Première ligne : titres
        f.write(sep.join(titres))
        # Ensuite : données des étudiants
        for e in etudiants :
            f.write('\n'+sep.join(e))
    return None
    
