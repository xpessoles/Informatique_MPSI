with open("moyennes_matieres.csv","r") as f : 
    _ = f.readline()
    coeffs = f.readline().strip().split(';')
    T = f.readlines()

n = len(coeffs)
S = 0 # Somme des coefficients
for i in range(1,n):
    coeffs[i] = int(coeffs[i])
    S = S + coeffs[i]
coeffs.append(S)

for i in range(len(T)) :
    T[i] = T[i].strip().split(';')
    for j in range(1,n):
        T[i][j] = float(T[i][j].replace(',','.'))

for e in T : 
    moy = 0
    for i in range(1,n):
        moy = moy + coeffs[i]*e[i]
    moy = moy / coeffs[-1]
    e.append(moy)

with open("moyennes_ponderees.csv","w") as f : 
    f.write("Prénoms;Moyennes pondérées")
    for e in T : 
        f.write('\n'+';'.join([str(e[0]),str(e[-1])]))
