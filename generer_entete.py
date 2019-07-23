# -*- coding: utf-8 -*
#Installation du module xlutils
#pip install xlutils
import numpy as np
import xlrd
import datetime
import os, glob, platform

Mois=['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Décembre']

#RAZ du fichier log
f=open('log.txt','w')

path=r"progression_2019_2020_IPT_MPSI.xlsx"#chemin de la progression
path_classe=''
path_site='site'#Chemin pour exporter les pdf vers site
nligne=40#Derniere ligne où figure une donnée
delta_td=1#position du jour des TD dans la semaine
delta_cours=1#position du jour des cours dans la semaine
delta_tp=3#position du jour des TD dans la semaine

####
#Definition des colonnes dans le tableau excel
####
col_date,col_num_cycle,col_name_cycle,col_num_cours,col_num_tp,col_name_cours,col_name_tp,col_supports_TD,col_supports_tp,col_competences_cours,col_competences_tp,col_figures,col_ref_cours\
=1,2,3,4,8,5,9,10,11,12,13,16,17

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
            delta = datetime.timedelta(days=(fs.cell_value(k,col_date)-2))
            d_s=d0+delta#Date du début de la semaine
            d_cours=d_s+datetime.timedelta(delta_cours)#Date du cours
            d_td=d_s+datetime.timedelta(delta_td)#Date du TD
            d_tp=d_s+datetime.timedelta(delta_tp)#Date du TD
            num_cours=int(fs.cell_value(k,col_num_cours)) #Numero du chapitre
            n_tp=int(fs.cell_value(k,col_num_tp)) #Numero du TP
            if fs.cell_value(k,col_num_cycle)!='':
                n_cycle=int(fs.cell_value(k,col_num_cycle))#numero du cycle
                name_cycle=fs.cell_value(k,col_name_cycle)#nom du cycle
                liste_cycle.append(n_cycle)
            else:
                n_cycle=liste_cycle[-1]
                # name_cycle=liste_name_cycle[-1]
            n_cours='C'+str(n_cycle)+'-'+str(num_cours)#numero du cours Ci-j avec i le cycle et j le chapitre
            # #Gestion des cours
            if n_cours not in liste_cours:
                name_cours=fs.cell_value(k,col_name_cours)
                liste_cours.append(n_cours)
                supports=fs.cell_value(k,col_supports_TD)
                competences=fs.cell_value(k,col_competences_cours)
                figures=fs.cell_value(k,col_figures)
                date_cours=str(d_cours.day)+' '+Mois[d_cours.month-1]+' '+str(d_cours.year)
                ref_cours=str(n_cycle)+'-'+str(num_cours)
                info_cours.append((date_cours,n_cycle,num_cours,name_cycle,name_cours,supports,competences,figures,ref_cours))
            # #Gestion des TP
            if n_tp not in liste_tp:
                name_tp=fs.cell_value(k,col_name_tp)
                num_tp=int(fs.cell_value(k,col_num_tp))
                if num_tp<10:
                    num_tp='0'+str(num_tp)
                else:
                    num_tp=str(num_tp)
                supports=fs.cell_value(k,col_supports_tp)
                competences=fs.cell_value(k,col_competences_tp)
                figures=fs.cell_value(k,col_figures)
                liste_tp.append(n_tp)
                ref_cours=fs.cell_value(k,col_ref_cours)#Reference du cours correspondant
                date_tp=str(d_tp.day)+' '+Mois[d_tp.month-1]+' '+str(d_tp.year)
                info_tp.append((date_tp,n_cycle,num_tp,name_cycle,name_tp,supports,competences,figures,ref_cours))
    return info_tp,info_cours
            
(info_tp,info_cours)=lire_semanier(fs)

#A partir des infos de cours ou TP, écrire dans l'entête les infos correspondantes dans le chemin spécifié nommé rep
(date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_cours[0]


    
def trouver_repertoire(info_activite):
    """Renvoie le repertoire dans lequel ecrire les infos de l'activité"""
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
    n_cycle,num_activite=ref_cours.split(';')[0].split('-')
    for r in os.listdir():
        if 'Cy_0'+str(n_cycle) in r:
            rep_cycle=r
            for r1 in os.listdir(rep_cycle+'/'):
                if 'Ch_0'+str(num_activite) in r1:
                    rep_chapitre=r1
    rep=rep_cycle+'/'+rep_chapitre
    return rep
    
def genere_fichiers_tex(info_activite,type_activite):
    '''Genere le fichier .tex à partir de l'activite donne et du bon repertoire'''
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
    rep=trouver_repertoire(info_activite)
    if type_activite=='cours':
        os.system('cp style/Cy_i_Ch_j_Cours.tex '+rep+'/cours/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours.tex')
        os.system('cp style/Cy_i_Ch_j_Cours_PDF.tex '+rep+'/cours/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours_PDF.tex')
        changer_ligne(rep+'/cours/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours_PDF.tex','\\input{Cy_01_Ch_01_Cours.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours.tex}')
    elif type_activite=='tp':
        os.system('cp style/Cy_i_Ch_j_TP_0k.tex '+rep+'/cours/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours.tex')
    
def changer_ligne(fichier,ancienne_ligne,nouvelle_ligne):
    with open(fichier,'r',encoding='utf-8') as f:
        texte=f.readlines()
    with open(fichier,'w',encoding='utf-8') as f:
        for ligne in texte:
            if ancienne_ligne in ligne:
                f.write(nouvelle_ligne)
            else:
                f.write(ligne)

#rep='Cy_01_Architecture_Algorithmique/Ch_01_ArchitectureMaterielleLogicielle/Cours'
# def genere_entete_cours(rep,info_activite):
#     """A partir du cours dont le chemin est donne par rep la fonction genere l'entete donnant toutes infos permettant de generer l'entete du cours."""
#     (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
#     with open(rep+'/cours/info_entete.tex','w',encoding='utf-8') as f:
#         texte_entete=''
#         with open('style/info_Entete0.tex','r',encoding='utf-8') as f0:
#             ligne=f0.readline()
#             while ligne!='':
#                 ligne=f0.readline()
#                 if '\\def\\xxnumpartie' in ligne:
#                     texte_entete+='\\def\\xxnumpartie{'+str(n_cycle)+'}\n'
#                 elif '\\def\\xxpartie' in ligne:
#                     texte_entete+='\\def\\xxpartie{'+str(name_cycle)+'}\n'
#                 elif '\\def\\xxnomchapitre' in ligne:
#                     texte_entete+='\\def\\xxnomchapitre{'+name_activite+'}\n'
#                 elif '\\def\\xxnumchapitre' in ligne:
#                     texte_entete+='\\def\\xxnumchapitre{'+str(num_activite)+'}\n'
#                 elif '\\def\\xxdate' in ligne:
#                     texte_entete+='\\def\\xxdate{'+date+'}\n'
#                 elif '\\chapterimage{' in ligne:
#                     texte_entete+='\\chapterimage{'+figures+'}\n'
#                 else: 
#                     texte_entete+=ligne
#         f.write(texte_entete)
        
        
def genere_entete(rep,info_activite,type_activite):
    """A partir du cours dont le chemin est donne par rep la fonction genere l'entete donnant toutes infos permettant de generer l'entete du cours."""
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
    if type_activite=='cours':
        file_entete=rep+'/cours/info_entete.tex'
    elif type_activite=='tp':
        n_cycle,num_activite=ref_cours.split(';')[0].split('-')
        file_entete=rep+'/TP'+num_activite+'/info_entete.tex'
        #Il faut s'assurer que le repertoire existe.
    else:
        print("mauvais choix d'activite")
    with open(rep+'/cours/info_entete.tex','w',encoding='utf-8') as f:
        texte_entete=''
        with open('style/info_Entete0.tex','r',encoding='utf-8') as f0:
            ligne=f0.readline()
            while ligne!='':
                ligne=f0.readline()
                if '\\def\\xxnumpartie' in ligne:
                    texte_entete+='\\def\\xxnumpartie{'+str(n_cycle)+'}\n'
                elif '\\def\\xxpartie' in ligne:
                    texte_entete+='\\def\\xxpartie{'+str(name_cycle)+'}\n'
                elif '\\def\\xxnomchapitre' in ligne:
                    texte_entete+='\\def\\xxnomchapitre{'+name_activite+'}\n'
                elif '\\def\\xxnumchapitre' in ligne:
                    texte_entete+='\\def\\xxnumchapitre{'+str(num_activite)+'}\n'
                elif '\\def\\xxdate' in ligne:
                    texte_entete+='\\def\\xxdate{'+date+'}\n'
                elif '\\chapterimage{' in ligne:
                    texte_entete+='\\chapterimage{'+figures+'}\n'
                elif '\\begin{itemize}[label=\\ding{112},font=\\color{ocre}]' in ligne:
                    texte_entete+='\\begin{itemize}[label=\\ding{112},font=\\color{ocre}]\n\\item '+competences+'\n'
                else: 
                    texte_entete+=ligne
        f.write(texte_entete)

for cours in info_cours:
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=cours
    rep=trouver_repertoire(cours)
    genere_fichiers_tex(cours,'cours')
    genere_entete(rep,cours,'cours')

        
        
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

                    

