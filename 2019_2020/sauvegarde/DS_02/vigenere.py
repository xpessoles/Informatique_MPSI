alphabet= "abcdefghijklmnopqrstuvwxyz"

mot,cle = 'anticonstitutionnellement','roue'

def decalage(c,n):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    ind=alphabet.index(c)
    return alphabet[(ind+n)%26]

def chiffrement_cesar(mess,n):
    code = ''
    for lettre in mess : 
        if lettre.isalpha() :
            code = code+decalage(lettre,n)
    return code

def decryptage_cesar(code):
    for n in range(26) : 
        print(n,chiffrement_cesar(code,-n))


for i in range(26):
    alphabet = alphabet[1:]+alphabet[:1]
    print (alphabet)

def generer_table():
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    table = []
    for i in range(26):
        ligne=[]
        ligne = [c for c in alphabet] # Création de la liste des lettres
        table.append(ligne) # Ajout de la liste des lettres
        alphabet = alphabet[1:]+alphabet[:1] # Décalage de l'alphabet
    return table

def generer_cle_1(mot,cle):
    # generation de la table clef en utilisant la concaténation de chaînes de caractères
    nb = len(mot)//len(cle)+1
    ch_cle=nb*cle
    ch_cle = ch_cle[0:len(mot)]
    tab_cle = [car for car in ch_cle]
    return tab_cle

def mystere1(mot,cle):
    nb = len(mot)//len(cle)+1
    ch_cle=nb*cle
    ch_cle = ch_cle[0:len(mot)]
    tab_cle = [car for car in ch_cle]
    return tab_cle


def generer_cle_2(mot,cle):
    tab_cle = []
    for i in range(len(mot)):
        id = i%len(cle)
        tab_cle.append(cle[id])
    return tab_cle

def code_vigenere(mot,cle):
    alphabet= "abcdefghijklmnopqrstuvwxyz"

    # On genere la table de vigenere
    table = generer_table()
    # On genere la clef
    tab_cle = generer_cle_1(mot,cle)
    # On genere le code
    code = ""
    for i in range(len(mot)):
        ligne = mot[i]
        col   = tab_cle[i]
        id_ligne = alphabet.index(ligne)
        id_col = alphabet.index(col)
        code = code+table[id_ligne][id_col]
    return code

def decode_vigenere(ch):
    L = len(cle)
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    N = len(alphabet)
    decode = ""
    for i in range(len(ch)):
        d = i
        while d>L-1:
            d = d - L
        index = alphabet.index(ch[i]) - alphabet.index(cle[d])
        if index < 0 :
            index = index + N
        j = alphabet[index]
        decide = decode + j
    return decode