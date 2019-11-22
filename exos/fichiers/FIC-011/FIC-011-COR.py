def carac(nom_de_fichier):
    """Renvoie une liste contenant le nombre de caractères
       de chaque ligne de nom_de_fichier"""
    with open(nom_de_fichier,'r',encoding='utf8') as f:
        lignes = f.readlines()
        print(lignes)
    return [len(x.strip('\n')) for x in lignes]


nom_de_fichier='complot_contre_lamerique.txt'
T=carac(nom_de_fichier)