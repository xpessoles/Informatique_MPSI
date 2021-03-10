import sqlite3
db=sqlite3.connect('facturation.sqlite')
cursor=db.cursor()


##Recherche
def recherche_par_date(date1,date2):
    """input:2 dates de la forme 'aa-mm-jj'. on renvoie les commandes entre ces 2 dates"""
    req="SELECT * FROM COMMANDES WHERE DATE_COMMANDE>? and DATE_COMMANDE<?"
    cursor.execute(req,(date1,date2))
    liste=cursor.fetchall()
    return liste

def cherche_numero_comm(prod):
    """input:nom d'un produit(char).On renvoie les numero des commandes qui contient le produit introduit"""
    req="SELECT NO_COMMANDE FROM DETAILS_COMMANDES,PRODUITS WHERE PRODUITS.REF_PRODUIT=DETAILS_COMMANDES.REF_PRODUIT GROUP by PRODUITS.REF_PRODUIT HAVING NOM_PRODUIT=?"
    cursor.execute(req,(prod,))
    liste=cursor.fetchall()
    return liste

def cherche_pays(prod):
    """input:prod(char),on envoye les pays ou ce produit a ete vendu"""
    req="SELECT DISTINCT PAYS FROM CLIENTS join COMMANDES on CLIENTS.CODE_CLIENT=COMMANDES.CODE_CLIENT JOIN DETAILS_COMMANDES on COMMANDES.NO_COMMANDE=DETAILS_COMMANDES.NO_COMMANDE JOIN PRODUITS on DETAILS_COMMANDES.REF_PRODUIT=PRODUITS.REF_PRODUIT WHERE PRODUITS.NOM_PRODUIT=? "
    cursor.execute(req,(prod,))
    liste=cursor.fetchall()
    return liste


##Modification
def modif_coord_client(soc,adresse,ville,cod_post,categ):
    """input:le nom de la societe-soc(char),l'adresse(char), le ville(char),le cod_post(int) et la categorie qu'on veut modifier"""
    req="UPDATE CLIENTS set ADRESSE=?,VILLE=?,CODE_POSTAL=?,CATEGORIE=? WHERE SOCIETE=?"
    cursor.execute(req,(adresse,ville,cod_post,categ,soc))
    db.commit()
    db.close
    return None

def modifier_prix(prod,prix):
    """input:prod(char),prix(int) . Met a jour le prix d'un certain produit"""
    req='UPDATE PRODUITS set PRIX_UNITAIRE=? WHERE NOM_PRODUIT=?'
    cursor.execute(req,(prix,prod))
    db.commit()
    db.close
    return None

def eliminer_societe(soc):
    """input:soc(char)-c'est le nom de societe qu'on veut eliminer"""
    req='DELETE FROM CLIENTS WHERE SOCIETE=?'
    cursor.execute(req,(soc,))
    db.commit()
    db.close
    return None

##Les elements de la base

def produit():
    """input:NONE.Renvoie la liste de produit de notre societe"""
    req='SELECT NOM_PRODUIT FROM PRODUITS'
    cursor.execute(req)
    liste=cursor.fetchall()
    return liste

def nombre_command_total():
    """input:NONE.Renvoie le nombre de commandes"""
    req="SELECT count(*) as nb_comandes FROM COMMANDES"
    cursor.execute(req)
    nr=cursor.fetchone()[0]
    return nr

def moyenne_prix():
    """input:NONE.Renvoie la moyenne de prix des produits"""
    req="SELECT avg(prix_unitaire) FROM PRODUITS"
    cursor.execute(req)
    moyenne=cursor.fetchone()[0]
    return moyenne

def plus_vieux_client():
    """input:None.Renvoie une liste avec les plus vieux clients"""
    req='SELECT DISTINCT SOCIETE FROM CLIENTS,COMMANDES where DATE_COMMANDE=(SELECT min(date_commande) from COMMANDES)'
    cursor.execute(req)
    liste=cursor.fetchall()
    return liste


## Repartition de prix,commandes

def  repart_command():
    """input:NONE.Renvoie chaque societe et son nombre de commandes"""
    req="SELECT SOCIETE, count(*) as nb_comm FROM CLIENTS,COMMANDES WHERE CLIENTS.CODE_CLIENT=COMMANDES.CODE_CLIENT GROUP by CLIENTS.CODE_CLIENT"
    cursor.execute(req)
    liste=cursor.fetchall()
    return liste


def plus_chere():
    """input:NONE.Renvoie le plus grand prix d'un produit et les produits avec ce prix"""
    req1='SELECT max(prix_unitaire) as plus_grand FROM PRODUITS'
    req2='SELECT NOM_PRODUIT FROM PRODUITS WHERE PRIX_UNITAIRE=(SELECT max(PRIX_UNITAIRE) as plus_grand FROM PRODUITS ORDER by REF_PRODUIT)'
    cursor.execute(req1)
    max=cursor.fetchone()[0]
    cursor.execute(req2)
    name=cursor.fetchall()
    return max,[name[i][0]for i in range(len(name))]


def moins_chere():
    """input:NONE.Renvoie le plus grand prix d'un produit et les produits avec ce prix"""
    req1='SELECT min(prix_unitaire) as plus_petit FROM PRODUITS'
    req2='SELECT NOM_PRODUIT FROM PRODUITS WHERE PRIX_UNITAIRE=(SELECT min(PRIX_UNITAIRE) as plus_petit FROM PRODUITS ORDER by REF_PRODUIT)'
    cursor.execute(req1)
    min=cursor.fetchone()[0]
    cursor.execute(req2)
    name=cursor.fetchall()
    return min,[name[i][0]for i in range(len(name))]



def revenu_par_pays(pays):
    """input:pays(char)- on calcule la somme d'argent obtenu pour le pays qu'on introduit"""
    l=[]
    v=[]
    req1="SELECT QUANTITE FROM DETAILS_COMMANDES JOIN COMMANDES on DETAILS_COMMANDES.NO_COMMANDE=COMMANDES.NO_COMMANDE JOIN CLIENTS on COMMANDES.CODE_CLIENT=CLIENTS.CODE_CLIENT WHERE PAYS=?"
    cursor.execute(req1,(pays,))
    for row in cursor:
        l.append(row[0])
    req2= "SELECT PRIX_UNITAIRE FROM PRODUITS JOIN DETAILS_COMMANDES on PRODUITS.REF_PRODUIT=DETAILS_COMMANDES.REF_PRODUIT JOIN COMMANDES on DETAILS_COMMANDES.NO_COMMANDE=COMMANDES.NO_COMMANDE JOIN CLIENTS on COMMANDES.CODE_CLIENT=CLIENTS.CODE_CLIENT WHERE PAYS=?"
    cursor.execute(req2,(pays,))
    for row in cursor:
        v.append(row[0])
    somme=0
    for i in range (len(l)) :
        somme=somme+l[i]*v[i]
    return somme











