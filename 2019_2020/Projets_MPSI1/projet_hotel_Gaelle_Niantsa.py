"""Fonctions principales"""
import time
import sqlite3
bDD= sqlite3.connect('hotel_gaelle-niantsa.db')
curseur=bDD.cursor()
print("Bienvenue à l'hôtel Pointcarré")

def fct_principale():
    time.sleep(1.0)
    bDD=sqlite3.connect('hotel_gaelle-niantsa.db')
    curseur=bDD.cursor()
    print("\nPour faire une réservation tapez 1")
    print("Pour annuler une réservation tapez 2")
    print("Pour consulter votre réservation tapez 3")
    print("Pour modifier votre réservation tapez 4")
    print("Pour quitter tapez 0")
    num=int(input ())
    if num==1 :
        return reserv()
    elif num==2:
        return annuler_reservation()
    elif num==3 :
        return consulter_reservation()
    elif num==4 :
        return modifier_reservation()
    elif num==0:
        print("Au revoir")
        bDD.close()
        time.sleep(2.0)

def reserv():
    n=int(input("Voulez-vous faire une réservation? \nSi oui, tapez 1, sinon tapez 0 pour retourner au menu principal\n"))
    if n==1:
        print("Pour quelles dates voulez-vous réserver ?")
        date_arr=str(input("Date d'arrivée au format année-mois-jour \t"))
        date_dep=str(input("Date de départ au format année-mois-jour \t"))
        curseur.execute("SELECT * FROM CALENDRIER WHERE JOUR BETWEEN "\
                        ":d1 AND :d2",{"d1":date_arr,"d2":date_dep})
        date_res=normaliser(curseur.fetchall())         # On enregistre tous les jours pour lesquels le client veut réserver
        nb_ch=int(input("Combien de chambres voulez-vous réserver ? \t"))
        print("Voulez-vous réserver une chambre Simple, Double ou une Suite ")
        cat_chambres=[]
        num_chambres=[]
        ind_ch=["1ère","2eme","3eme","4eme","5eme","6eme","7eme","8eme","9eme","10eme"]
        for i in range(nb_ch):
            print(ind_ch[i],"chambre")                          # Enregistrement de la catégorie de chaque chambre
            cat_ch=input()
            cat_chambres.append(cat_ch)
            num_ch=chambre_dispo(date_arr,date_dep,cat_ch)
            num_chambres.append(num_ch)
        nom_cli=input("Veuillez rentrez votre nom \t")                     # Enregistrement des informations CLIENT
        prenom_cli=input("Veuillez rentrez votre prénom \t")
        date_naissance_cli=input("Veuillez rentrez votre date de naissance au format année-mois-jour \t")
        curseur.execute("SELECT DISTINCT ID_CLIENT FROM CLIENTS WHERE NOM=? "\
                        "AND PRENOM=? AND DATE_NAISSANCE=?",(nom_cli,prenom_cli,date_naissance_cli))
        mem=curseur.fetchall()
        if len(mem)==0:
            curseur.execute("SELECT MAX(ID_CLIENT) FROM CLIENTS")
            id_max=curseur.fetchone()[0]                            #si le client est déjà enregistré on récupère son id                                                 
            id_cli=id_max +1#sinon on lui attribue un id en prenant l'id actuel le plus grand +1 
            contact_cli=input("Veuillez rentrez votre numéro de téléphone \t")
            curseur.execute("INSERT INTO CLIENTS (NOM, PRENOM,ID_CLIENT,DATE_NAISSANCE,CONTACT)"\
                            "VALUES(?,?,?,?,?)",(nom_cli,prenom_cli,id_cli,date_naissance_cli,contact_cli)) 
        else:
            id_cli=int(normaliser(mem)[0])  
        curseur.execute("INSERT INTO PLANNING (ID_CLIENT,DATE_ARRIVEE,DATE_DEPART)"\
                        "VALUES(?,?,?)",(id_cli,date_arr,date_dep))
        for num_ch in num_chambres:
            for date in date_res:
                curseur.execute("INSERT INTO RESERVATIONS (ID_CLIENT,NUM_CHAMBRE,DATE_RES) "\
                                "VALUES (?,?,?)",(id_cli,num_ch,date))
        bDD.commit()
        print("Votre réservation à bien été prise en compte")
    return fct_principale()

def annuler_reservation():
    n=int(input("Voulez-vous annuler une réservation? \nSi oui, tapez 1, sinon 2 :\n"))
    if n==1:
        print("Veuillez entrer votre nom en majuscule: ")
        nom=input()
        print("Veuillez entrer votre prénom: ")
        prenom=input()
        reponse=curseur.execute("SELECT ID_CLIENT FROM CLIENTS WHERE NOM=? AND PRENOM=?", (nom, prenom))
        id_aux=reponse.fetchall()
        if len(id_aux)==0:
            print("Vous n'êtes pas dans notre base de données merci de vérifier vos informations")
        else:
            id_cli=normaliser(id_aux)[0]
            DA=input("Veuillez entrer la date d'arrivée:\n")
            DD=input("Veuillez entrer la date de départ: \n")
            curseur.execute("DELETE FROM RESERVATIONS WHERE RESERVATIONS.ID_CLIENT=? AND DATE_RES BETWEEN ? AND ?", (id_cli,DA,DD))
            print("La réservation a été annulée.")
    bDD.commit()
    return fct_principale()

def consulter_reservation():
    n=int(input("Si vous voulez consulter vos dates tapez 1, votre/vos chambre(s) tapez 2,"\
                "vos informations client tapez 3 , si vous voulez retourner à l'écran principal, tapez 0 \t"))
    if n==0:
        return fct_principale()
    nom=input("Veuillez entrer votre nom en majuscule: \t")
    prenom=input("Veuillez rentrez votre prénom \t")
    reponse=curseur.execute("SELECT ID_CLIENT FROM CLIENTS WHERE NOM=? AND PRENOM=?", (nom, prenom))
    id_aux=reponse.fetchall()
    if len(id_aux)==0:
        print("Vous n'êtes pas dans notre base de données merci de vérifier vos informations")
    else:
        id_cli=normaliser(id_aux)[0]
        if n==1:
            arrivee=curseur.execute("SELECT DATE_ARRIVEE FROM PLANNING WHERE ID_CLIENT=:id",{"id":id_cli})
            dates_arr=normaliser(curseur.fetchall())
            depart=curseur.execute("SELECT DATE_DEPART FROM PLANNING WHERE ID_CLIENT=:id",{"id":id_cli})
            dates_dep=normaliser(curseur.fetchall())
            nb_res=len(dates_arr)
            print(" Vous avez fait ",nb_res,"réservation(s) :")
            for i in range (nb_res):
                print("Réservation", i+1, "\n date d'arrivée :",dates_arr[i] ,"\t date de départ :",dates_dep[i])
        elif n==2:
            print("Pour quelle réservation voulez-vous consulter vos chambres ? \t")
            arr=input("Date d'arrivée\t")
            dep=input("Date de départ\t")
            curseur.execute("SELECT DISTINCT NUM_CHAMBRE FROM RESERVATIONS WHERE ID_CLIENT=? AND DATE_RES BETWEEN ? AND ?",(id_cli,arr,dep))                
            num_ch=normaliser(curseur.fetchall())
            types=[]
            for ch in num_ch:
                curseur.execute("SELECT DISTINCT TYPE FROM CHAMBRES WHERE NUM_CHAMBRE=:num",{"num":ch})
                types.append(curseur.fetchone())
            types=normaliser(types)
            ind_ch=["1ère","2eme","3eme","4eme","5eme","6eme","7eme","8eme","9eme","10eme"]
            for i in range(len(num_ch)):
                print(ind_ch[i],"chambre :",types[i], " numéro :",num_ch[i],)
        elif n==3:
            curseur.execute("SELECT DATE_NAISSANCE,CONTACT FROM CLIENTS WHERE ID_CLIENT=:id",{"id":id_cli})               
            infos=curseur.fetchall()[0]
            print("Date de naissance : ",infos[0],"\nNuméro de téléphone :",infos[1])
            print("Si les informations sont incorrectes merci de les modifier \t")
    return fct_principale()
                
def modifier_reservation():
    n=int(input("Voulez-vous modifier une réservation? \nSi oui, tapez 1, sinon tapez 2 pour retourner au menu principal\n"))
    if n==1:
        nom=input("Veuillez entrer votre nom en majuscule:\n ")
        prenom=input("Veuillez entrer votre prénom:\n ")
        reponse=curseur.execute("SELECT ID_CLIENT FROM CLIENTS WHERE NOM=? AND PRENOM=?", (nom, prenom)) #prend l'id du client
        id=reponse.fetchall()
        if len(id)==0:
            print("Vous n'êtes pas dans notre base de données merci de vérifier vos informations")
        else:
            id=normaliser(id)[0]
        print("Si vous souhaitez modifier:\nVos informations, tapez 1\nVotre réservation (Date d'arrivée et de départ et chambres), tapez 2\nRetourner au menu principal, tapez 3\n")
        n1=int(input())
        if n1==1:
            print("Veuillez entrer vos informations")
            nv_nom=input("Nom (en majuscule):")
            nv_prenom=input("Prénom: ")
            nv_naissance=input("Date de naissance: ")
            nv_contact=input("Contact: ")
            curseur.execute("UPDATE CLIENTS SET NOM=?, PRENOM=?,DATE_NAISSANCE=?,CONTACT=? WHERE ID_CLIENT=?", (nv_nom, nv_prenom,nv_naissance,nv_contact, id))
            #met à jour le nom et le prénom
            print("Vos informations ont été mises a jour.")
            bDD.commit()
        elif n1==2:
            DAI=input("Veuillez entrer la date d'arrivée initial (année-mois-jour): \n")
            DDI=input("Veuillez entrer la date de départ initial (année-mois-jour): \n")
            curseur.execute("DELETE FROM RESERVATIONS WHERE ID_CLIENT=? AND DATE_RES BETWEEN ? AND ?", (id, DAI,DDI)) #supprime dans réservations
            curseur.execute("DELETE FROM PLANNING WHERE ID_CLIENT=? AND DATE_ARRIVEE=?", (id, DAI)) #supprime dans planning
            date_arr=input("Entrez votre nouvelle date d'arrivée année-mois-jour \t")
            date_dep=input("Entrez votre nouvelle date de départ année-mois-jour \t")
            curseur.execute("SELECT * FROM CALENDRIER WHERE JOUR BETWEEN "\
            ":d1 AND :d2",{"d1":date_arr,"d2":date_dep})
            date_res=normaliser(curseur.fetchall())     # On enregistre tous les jours pour lesquels le client veut réserver
            nb_ch=int(input("Combien de chambres voulez-vous réserver ? \t"))
            print("Voulez-vous réserver une chambre Simple, Double ou une Suite ")
            cat_chambres=[]
            num_chambres=[]
            ind_ch=["1ère","2eme","3eme","4eme","5eme","6eme","7eme","8eme","9eme","10eme"]
            for i in range(nb_ch):
                print(ind_ch[i],"chambre")     # Enregistrement de la catégorie de chaque chambre
                cat_ch=input()
                cat_chambres.append(cat_ch)
                num_ch=chambre_dispo(date_arr,date_dep,cat_ch)
                num_chambres.append(num_ch)
                curseur.execute("INSERT INTO PLANNING (ID_CLIENT,DATE_ARRIVEE,DATE_DEPART)"\
                "VALUES(?,?,?)",(id,date_arr,date_dep))
            for num_ch in num_chambres:
                for date in date_res:
                    curseur.execute("INSERT INTO RESERVATIONS (ID_CLIENT,NUM_CHAMBRE,DATE_RES) VALUES (?,?,?)",(id,num_ch,date))
            
            print("Vos modifications ont été enregistrées")
    return fct_principale()
  
"""Fonctions secondaires"""

def chambre_dispo(date_arr,date_dep,categorie):
    """renvoie un num_CHAMBRE libre de catégorie demandée"""
    curseur.execute("SELECT RESERVATIONS.NUM_CHAMBRE FROM RESERVATIONS,CHAMBRES WHERE RESERVATIONS.NUM_CHAMBRE=CHAMBRES.NUM_CHAMBRE AND TYPE=? AND DATE_RES BETWEEN ? AND ?",(categorie,date_arr,date_dep))
    ch_occ_aux=curseur.fetchall()
    ch_occ=normaliser(ch_occ_aux)
    curseur.execute("SELECT DISTINCT NUM_CHAMBRE FROM CHAMBRES WHERE TYPE= :cat",{"cat":categorie})
    ch_ttes=normaliser(curseur.fetchall())
    if len(ch_occ)==0:
        return ch_ttes[0]
    else :
        ch_libres=[]
        for ch in ch_ttes:
            if not (ch in ch_occ):
                ch_libres.append(ch)
    return ch_libres[0]

def normaliser(l_aux):
    """Permet de remettre sous une forme "normale" les listes renvoyées par curseur.fetchall"""
    l_fin=[]
    for c in l_aux:
        ch=str(c)
        aux=ch.strip('(').strip(')').strip(',')
        l_fin.append(aux)
    return l_fin
    
fct_principale()

