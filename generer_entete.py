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

answer=input('classe ? (1 : MPSI, 2: PSI)')

if answer=='1':
    path=r"/Users/emiliendurif/Documents/prepa/MPSI/organisation_programme/progression_2018_2019_MPSI.xlsx"
    path_classe='/Users/emiliendurif/Documents/prepa/MPSI/2018-2019/'
    path_site='/Users/emiliendurif/Documents/prepa/MPSI/site'
    nligne=40#Derniere ligne où figure une donnée
    delta_td=1#position du jour des TD dans la semaine
    delta_cours=1#position du jour des cours dans la semaine
elif answer=='2':
    path=r"/Users/emiliendurif/Documents/prepa/PSI/organisation_psi/progression_2018_2019_PSI_emilien.xlsx"
    path_classe='/Users/emiliendurif/Documents/prepa/PSI/2018-2019/'
    path_site='/Users/emiliendurif/Documents/prepa/PSI/organisation_psi/site'
    nligne=27#Derniere ligne où figure une donnée
    delta_td=4#position du jour des TD dans la semaine
    delta_cours=2#position du jour des cours dans la semaine
else:
    print('Mauvais choix')
    answer=input('classe ? (1 : MPSI, 2: PSI)')
#Ouverture de la progression excel
classeur=xlrd.open_workbook(path)
feuilles=classeur.sheet_names()

#Ouverture de la feuille du semanier
for f in feuilles:
    if "Semanier" in f:
        fs=classeur.sheet_by_name(f)
liste_cours=[]
liste_td=[]
liste_cycle=[]
liste_name_cycle=[]
d0=datetime.date(1900,1,1)
for k in range(1,nligne):
#for k in range(1,2):
    if 'Vacances' not in str(fs.cell_value(k,0)):
        delta = datetime.timedelta(days=(fs.cell_value(k,1)-2))
        d_s=d0+delta#Date du début de la semaine
        d_cours=d_s+datetime.timedelta(delta_cours)#Date du cours
        d_td=d_s+datetime.timedelta(delta_td)#Date du TD
        if fs.cell_value(k,2)!='':
            n_cycle=fs.cell_value(k,2)#numero du cycle
            name_cycle=fs.cell_value(k,3)#nom du cycle
            cycle_resume=fs.cell_value(k,14)#nom du cycle resume
            liste_cycle.append(n_cycle)
            liste_name_cycle.append(name_cycle)
        else:
            n_cycle=liste_cycle[-1]
            name_cycle=liste_name_cycle[-1]
        n_cours=fs.cell_value(k,4)#numero du cours
        #Gestion des cours
        if n_cours not in liste_cours:
            col_d=13#Colonne du nom des dossiers
            if fs.cell_value(k,col_d) !='':
                rep=fs.cell_value(k,col_d)
            rep0=os.listdir(path_classe+'/'+rep)
            for rep_cours in rep0:
                #Edition des entetes
                if n_cours in rep_cours:#Se positionner dans un repertoire de cours
                    name_cours=fs.cell_value(k,5)#nom du cours
                    d_cours_f=str(d_cours.day)+' '+Mois[d_cours.month-1]+' '+str(d_cours.year)#Date du cours écrite en français
                    with open(path_classe+'/'+rep+'/'+rep_cours+'/entete.tex','w',encoding='iso-8859-1') as f:
                        f.write('\\renewcommand{\\cycle}{'+n_cycle+' : '+name_cycle+'}\n')
                        f.write('\\renewcommand{\\cycleresume}{'+n_cycle+' : '+cycle_resume+'}\n')
                        f.write('\\renewcommand{\\titre}{'+name_cours+'}\n')
                        f.write('\\renewcommand{\\numero}{'+n_cours+'}\n')
                        f.write('\\renewcommand{\\auteur}{Emilien DURIF}\n')
                        f.write('\\renewcommand{\\etablissement}{Lycée La Martinière Monplaisir Lyon}\n')
                        f.write("\\renewcommand{\\discipline}{Sciences Industrielles pour l'Ingénieur}\n")
                        if answer=='1':
                            f.write('\\renewcommand{\\classe}{Classe préparatoire M.P.S.I.}\n')
                        elif answer=='2':
                            f.write('\\renewcommand{\\classe}{Classe préparatoire P.S.I.}\n')
                        f.write('\\renewcommand{\\annee}{2018 - 2019}\n')
                        f.write('\\renewcommand{\\icone}{/Users/emiliendurif/Documents/prepa/latex/images/logo_martiniere.jpg}\n')
                        f.write('\\renewcommand{\\competences}{}\n')
                        f.write('\\renewcommand{\\date}	{'+d_cours_f+'}\n')
                
        liste_cours.append(n_cours)#Validation du nouveau cours

                    

