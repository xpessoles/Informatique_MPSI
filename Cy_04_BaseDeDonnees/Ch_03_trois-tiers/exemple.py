import sqlite3

connexion=sqlite3.connect('mpsimdb.sqlite')

curseur=connexion.cursor()

curseur.execute("SELECT * FROM PERSONNE")

#print(curseur.fetchall())

T=[]
for ligne in curseur:
    T.append(list(ligne))