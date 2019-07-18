# -*- coding: utf-8 -*
#Installation du module xlutils
#pip install xlutils
import numpy as np
import xlrd
import datetime
import os, glob
Mois=['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Décembre']

#RAZ du fichier log
f=open('log.txt','w')

path=r"progression_2019_2020_IPT_MPSI_0.xlsx"#chemin de la progression
path_classe=''
path_site='site'#Chemin pour exporter les pdf vers site
nligne=40#Derniere ligne où figure une donnée
delta_td=1#position du jour des TD dans la semaine
delta_cours=1#position du jour des cours dans la semaine
delta_tp=3#position du jour des TD dans la semaine

#Ouverture de la progression excel
classeur=xlrd.open_workbook(path)
feuilles=classeur.sheet_names()

#Ouverture de la feuille du semanier
d0=datetime.date(1900,1,1)
for f in feuilles:
    if "Semanier" in f:
        fs=classeur.sheet_by_name(f)


def lire_semanier(fs):
    """a partir d'une feuille excel correspondant au sémanier de la progression renvoie deux listes de tuple donnant des infos sur les cours et td : (date,cycle,numero,nom du cycle,nom du document, supports d'application pour le cours)"""
    liste_cours=[]
    liste_cycle=[]
    liste_tp=[]
    info_cours=[]
    info_tp=[]
    for k in range(1,nligne):
    #for k in range(1,2):
        if 'Vacances' not in str(fs.cell_value(k,0)):
            delta = datetime.timedelta(days=(fs.cell_value(k,1)-2))
            d_s=d0+delta#Date du début de la semaine
            d_cours=d_s+datetime.timedelta(delta_cours)#Date du cours
            d_td=d_s+datetime.timedelta(delta_td)#Date du TD
            d_tp=d_s+datetime.timedelta(delta_tp)#Date du TD
            num_cours=int(fs.cell_value(k,4)) #Numero du chapitre
            n_tp=int(fs.cell_value(k,8)) #Numero du TP
            if fs.cell_value(k,2)!='':
                n_cycle=int(fs.cell_value(k,2))#numero du cycle
                name_cycle=fs.cell_value(k,3)#nom du cycle
                liste_cycle.append(n_cycle)
            else:
                n_cycle=liste_cycle[-1]
                # name_cycle=liste_name_cycle[-1]
            n_cours='C'+str(n_cycle)+'-'+str(num_cours)#numero du cours Ci-j avec i le cycle et j le chapitre
            # #Gestion des cours
            if n_cours not in liste_cours:
                name_cours=fs.cell_value(k,5)
                liste_cours.append(n_cours)
                supports=fs.cell_value(k,11)
                competences=fs.cell_value(k,13)
                figures=fs.cell_value(k,15)
                date_cours=str(d_cours.day)+' '+Mois[d_cours.month-1]+' '+str(d_cours.year)
                info_cours.append((date_cours,n_cycle,num_cours,name_cycle,name_cours,supports,competences,figures))
            # #Gestion des TP
            if n_tp not in liste_tp:
                name_tp=fs.cell_value(k,9)
                n_tp=int(fs.cell_value(k,8))
                supports=fs.cell_value(k,12)
                competences=fs.cell_value(k,13)
                figures=fs.cell_value(k,15)
                liste_tp.append(n_tp)
                date_tp=str(d_tp.day)+' '+Mois[d_tp.month-1]+' '+str(d_tp.year)
                info_tp.append((date_tp,n_cycle,n_tp,name_cycle,name_tp,supports,competences,figures))
    return info_tp,info_cours
            
(info_tp,info_cours)=lire_semanier(fs)

#A partir des infos de cours ou TP, écrire dans l'entête les infos correspondantes dans le chemin spécifié nommé rep
(date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures)=info_cours[0]

rep='/Users/emiliendurif/Documents/prepa/MPSI/ipt_mpsi_lamartin/Informatique_MPSI/Cy_01_Architecture_Algorithmique/Ch_01_ArchitectureMaterielleLogicielle/Cours'
with open(rep+'/info_entete.tex','w',encoding='iso-8859-1') as f:
    texte_entete=''
    with open('style/info_Entete0.tex','r',encoding='iso-8859-1') as f0:
        ligne=f0.readline()
        while ligne!='':
            ligne=f0.readline()
            if '\\def\\xxnumpartie' in ligne:
                texte_entete+='\\def\\xxnumpartie{'+str(n_cycle)+'}\n'
            elif '\\def\\xxpartie' in ligne:
                texte_entete+='\\def\\xxpartie{'+str(name_cycle)+'}\n'
            elif '\\def\\xxchapitre' in ligne:
                texte_entete+='\\def\\xxnomchapitre{'+str(name_activite)+'}\n'
            elif '\\def\\xxnumchapitre' in ligne:
                texte_entete+='\\def\\xxnumchapitre{'+str(num_activite)+'}\n'
            elif '\\def\\xxdate' in ligne:
                texte_entete+='\\def\\xxdate{'+date+'}\n'
            elif '\\chapterimage{' in ligne:
                texte_entete+='\\chapterimage{'+figures+'}\n'
            else: 
                texte_entete+=ligne
    f.write(texte_entete)
        
        
        #     col_d=13#Colonne du nom des dossiers
        #     if fs.cell_value(k,col_d) !='':
        #         rep=fs.cell_value(k,col_d)
        #     rep0=os.listdir(path_classe+'/'+rep)
        #     for rep_cours in rep0:
        #         #Edition des entetes
        #         if n_cours in rep_cours:#Se positionner dans un repertoire de cours
        #             name_cours=fs.cell_value(k,5)#nom du cours
        #             d_cours_f=str(d_cours.day)+' '+Mois[d_cours.month-1]+' '+str(d_cours.year)#Date du cours écrite en français
        #             with open(path_classe+'/'+rep+'/'+rep_cours+'/entete.tex','w',encoding='iso-8859-1') as f:
        #                 f.write('\\renewcommand{\\cycle}{'+n_cycle+' : '+name_cycle+'}\n')
        #                 f.write('\\renewcommand{\\cycleresume}{'+n_cycle+' : '+cycle_resume+'}\n')
        #                 f.write('\\renewcommand{\\titre}{'+name_cours+'}\n')
        #                 f.write('\\renewcommand{\\numero}{'+n_cours+'}\n')
        #                 f.write('\\renewcommand{\\auteur}{Emilien DURIF}\n')
        #                 f.write('\\renewcommand{\\etablissement}{Lycée La Martinière Monplaisir Lyon}\n')
        #                 f.write("\\renewcommand{\\discipline}{Sciences Industrielles pour l'Ingénieur}\n")
        #                 if answer=='1':
        #                     f.write('\\renewcommand{\\classe}{Classe préparatoire M.P.S.I.}\n')
        #                 elif answer=='2':
        #                     f.write('\\renewcommand{\\classe}{Classe préparatoire P.S.I.}\n')
        #                 f.write('\\renewcommand{\\annee}{2018 - 2019}\n')
        #                 f.write('\\renewcommand{\\icone}{/Users/emiliendurif/Documents/prepa/latex/images/logo_martiniere.jpg}\n')
        #                 f.write('\\renewcommand{\\competences}{}\n')
        #                 f.write('\\renewcommand{\\date}	{'+d_cours_f+'}\n')
        #         
        # liste_cours.append(n_cours)#Validation du nouveau cours

                    

