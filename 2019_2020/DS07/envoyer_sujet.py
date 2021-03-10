import email
import imaplib
import os
import sys
import smtplib
import getpass
import time,pdb
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders






#Parametre du compte d'envoi
qui='elevepsi.lamartin@gmail.com'
userName='elevepsi.lamartin'
passwd='Lina22122018'

#Parametre devoir

####MPSI INFO Machine enonce
sujet="DS8 d'informatique sur machine"
rep0='/Users/emiliendurif/Dropbox/cpge/ipt_mpsi_ds/DS08/'
donnees_groupes='/Users/emiliendurif/Documents/prepa/MPSI/organisation_programme/mpsi2_2019_2020_groupe.csv'
# donnees_groupes='/Users/emiliendurif/Documents/prepa/MPSI/organisation_programme/mpsi1_2019_2020_groupe0.csv'
rep_copies=rep0+'copies/'
prefixe_fichier_note=rep0+'fiches/bilan_'
prefixe_copie=''
nom_prof='Emilien Durif et Xavier Pessoles'


fichier_enonce='/Users/emiliendurif/Dropbox/cpge/ipt_mpsi_ds/DS08_pdf.pdf'

# body = "Bonjour %s,\nvous trouverez en fichier joint la base de donnee pour votre devoir et l'enoncé'.\nBien Cordialement \n%s"% (ligne[1],nom_prof)

travail_de_groupe=False




def envoieUnMessage(userName, passwd, body, files, adresse) :
    # Le message si pas de PJ ...
    # qui = mail['from']
    # sujet = mail['subject']
    # adresse = recuperationAdresseMail(qui)
    message = MIMEMultipart()
    message['From'] = 'Emilien DURIF <'+ userName+'>'
    message['To'] = ','.join(adresse)
    #msg['Date'] = formatdate(localtime=True)
    message['Subject'] = sujet
    msg=body
    message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))    ## Attache du message à l'objet "message", et encodage en UTF-8
    #Ajout de pièce jointe
    for file in files:
        piece = open(file, "rb")
        part = MIMEBase('application', 'octet-stream')    ## Encodage de la pièce jointe en Base64
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" % file.split('/')[-1])
        message.attach(part)    ## Attache de la pièce jointe à l'objet "message"
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #server_ssl.ehlo()   # optional
    server_ssl.login(userName, passwd)
    # email_text = """From: %s\nTo: %s\nSubject: %s\n\n%s
    # """ % ('Emilien DURIF <'+ userName+'>', ", ".join([adresse]), sujet,body)
    email_text= message.as_string().encode('utf-8')
    server_ssl.sendmail(userName, adresse, email_text)
    server_ssl.close()
    print("Message envoyé à " + str(adresse))


def trouver_nom_fichier(nom):
    if ' ' in nom:
        noms_fichier=nom.split(' ')
        nom_fichier=''
        for noms in noms_fichier:
            nom_fichier+=noms+'_'
        nom_fichier=nom_fichier[:-1]
    else:
        nom_fichier=nom
    return nom_fichier

def trouver_fiche_bilan(nom):
    liste_fichier=os.listdir(rep0+'fiches/')
    for fichier in liste_fichier:
        if nom.split(' ')[0].lower() in fichier.lower() or nom.split('-')[0].lower() in fichier.lower() or nom.split(' ')[-1].lower() in fichier.lower() or nom.split('-')[-1].lower() in fichier.lower():
            fiche_bilan=fichier
            return rep0+'fiches/'+fiche_bilan
        else:
            fiche_bilan=''
    return fiche_bilan

def trouver_copie(nom):
    liste_fichier=os.listdir(rep_copies)
    for fichier in liste_fichier:
        if nom.split(' ')[0].lower() in fichier.lower() or nom.split('-')[0].lower() in fichier.lower() or nom.split(' ')[-1].lower() in fichier.lower() or nom.split('-')[-1].lower() in fichier.lower():
            fiche_bilan=fichier
            return rep_copies+fiche_bilan
        else:
            fiche_bilan=''
    return fiche_bilan

with open(donnees_groupes,'r',encoding='utf8') as f:
    data=f.readlines()
    k=0
    liste_absents=[]
    for ligne in data[1:]:
        ligne=ligne.split(";")
        adresse=ligne[3].strip()
        #adresse=ligne[7].strip()#test avec mon adresse mail
        groupe=ligne[2]
        prenom=ligne[1]
        nom=ligne[0]
        option=ligne[6]
        # body = "Bonjour %s,\nvous trouverez en fichier joint votre fiche de notation ainsi que le corrigé du %s.\nBien Cordialement, \n%s"% (ligne[1],rep0.split('/')[-2],nom_prof)
        "Bonjour %s,\nvous trouverez en fichier joint la base de donnee pour votre devoir et l'enoncé'.\nBien Cordialement \n%s"% (ligne[1],nom_prof)
        files=[fichier_enonce]
        elif prefixe_copie=='':
            files=[fiche_bilan]
        else:
            files=[fiche_bilan,copie]
        if fichier_corrige!='':
            files.append(fichier_corrige)
        if 'mpsi1' in donnees_groupes:
            adresses=[adresse,'Xavier.Pessoles@ac-lyon.fr']
        else:
            adresses=[adresse]
        #if option=='SII 4H':
        if os.path.exists(fiche_bilan) == False:
            liste_absents.append(nom)
        if os.path.exists(fiche_bilan) == True:
            k+=1
            print(k,nom,prenom,adresses,copie,files)
            #envoieUnMessage(userName, passwd,body,files,adresses)






