#f=open('complot_contre_lamerique.txt','r',encoding='utf8')


def carac(nom_de_fichier):
    """Renvoie une liste contenant le nombre de caractères
       de chaque ligne de nom_de_fichier"""
    with open(nom_de_fichier,'r',encoding='utf8') as f:
        lignes = f.readlines()
    return [len(x.strip('\n')) for x in lignes]


nom_de_fichier='complot_contre_lamerique.txt'
T=carac(nom_de_fichier)

def compte_carac(carac,nom_de_fichier):
    with open(nom_de_fichier,'r',encoding='utf8') as f:
        ligne='_'
        S=0
        while ligne!='':
            ligne = f.readline().lower()
            for c in ligne:
                if c==carac.lower():
                    S+=1
        return S

def compte_carac2(carac,nom_de_fichier):
    with open(nom_de_fichier,'r',encoding='utf8') as f:
        texte=f.read()
        return texte.lower().count(carac)

def stat_carac(nom_de_fichier):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    occurences=[]
    for car in alphabet:
        occurences.append(compte_carac(car,nom_de_fichier))
    return occurences

import matplotlib.pyplot as plt
from numpy import arange



def trace_stat_carac(nom_de_fichier):
    y=stat_carac(nom_de_fichier)
    plt.clf()
    plt.plot(y,'ro')
    plt.xlabel("Numéro de la lettre dans l'alphabet")
    plt.ylabel('occurences')
    plt.savefig('graphe_occurences.png')
    plt.show()

alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet_liste=len(alphabet)*[]
for c in alphabet:
    alphabet_liste.append(c)
def trace_stat_carac_bis(nom_de_fichier):
    y=stat_carac(nom_de_fichier)
    plt.clf()
    for i,yi in enumerate(y):
        plt.plot([i,i],[0,yi],'r-',linewidth=5)
    plt.ylabel('occurences')
    plt.xticks(arange(26),tuple(alphabet_liste))
    plt.savefig('histo_occurences.png')
    plt.show()


def trace_stat_carac_pourcent(nom_de_fichier):
    y=stat_carac(nom_de_fichier)
    plt.clf()
    for i,yi in enumerate(y):
        plt.plot([i,i],[0,100*yi/sum(y)],'r-',linewidth=5)
    plt.ylabel('occurences')
    plt.xticks(arange(26),tuple(alphabet_liste))
    plt.savefig('histo_occurences_pourcent.png')
    plt.show()

