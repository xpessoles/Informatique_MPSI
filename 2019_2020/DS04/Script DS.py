prenom, nom = input("Entrez votre prenom : "), input("Entrer votre nom de famille : ")

f = open("test.txt", "w")
f.write(f"Prenom : {prenom}; Nom de famille : {nom}")
