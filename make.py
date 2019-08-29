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

#Separateur de dossier
if platform.system()=='Windows':
    sep='\\'
else:
    sep='/'

####
#Definition des colonnes dans le tableau excel
####





def lire_semanier(path):
    """a partir d'une feuille excel correspondant au sémanier de la progression renvoie deux listes de tuple donnant des infos sur les cours et td : (date,cycle,numero,nom du cycle,nom du document, supports d'application pour le cours)"""
    #Ouverture de la progression excel
    classeur=xlrd.open_workbook(path)
    feuilles=classeur.sheet_names()
    
    #Ouverture de la feuille du semanier
    d0=datetime.date(1900,1,1)
    for f in feuilles:
        if "Semanier" in f:
            fs=classeur.sheet_by_name(f)
    col_date,col_num_cycle,col_name_cycle,col_num_cours,col_num_tp,col_name_cours,col_name_tp,col_supports_TD,col_supports_tp,col_competences_cours,col_competences_tp,col_figures,col_ref_cours\
    =1,2,3,4,8,5,9,10,11,12,13,16,17
    nligne=40#Derniere ligne où figure une donnée
    delta_td=1#position du jour des TD dans la semaine
    delta_cours=1#position du jour des cours dans la semaine
    delta_tp=3#position du jour des TD dans la semaine
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
    rep=rep_cycle+sep+rep_chapitre
    return rep
    
def genere_fichiers_tex(info_activite,type_activite):
    '''Genere le fichier .tex à partir de l'activite donne et du bon repertoire'''
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
    rep=trouver_repertoire(info_activite)
    if type_activite=='cours':
        os.system('cp style'+sep+'Cy_i_Ch_j_Cours.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours.tex')
        os.system('cp style'+sep+'Cy_i_Ch_j_Cours_PDF.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours_PDF.tex')
        os.system('cp style'+sep+'Cy_i_livret_Ch_j.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_0'+str(num_activite)+'.tex')
        os.system('cp style'+sep+'Cy_i_Ch_j_TD_j.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_TD_0'+str(num_activite)+'.tex')
        # print(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours_PDF.tex')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours_PDF.tex','\\input{Cy_01_Ch_01_Cours.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_0'+str(num_activite)+'.tex','\\input{Cy_01_Ch_01_Cours.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_0'+str(num_activite)+'.tex','\\input{Cy_01_Ch_01_TD_01.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_TD_0'+str(num_activite)+'.tex}')
    elif type_activite=='tp':
        num_chapitre=ref_cours.split(';')[0].split('-')[1]
        if os.path.exists(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite)==False:
            os.mkdir(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite)
        os.system('cp style'+sep+'Cy_i_Ch_j_TP_k.tex '+rep+'/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite+'.tex')
        os.system('cp style'+sep+'Cy_i_Ch_j_TP_k_pdf.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite+'_pdf.tex')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite+'_pdf.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite+'.tex}')
    
def changer_ligne(fichier,ancienne_ligne,nouvelle_ligne):
    with open(fichier,'r',encoding='utf-8') as f:
        texte=f.readlines()
    with open(fichier,'w',encoding='utf-8') as f:
        for ligne in texte:
            if ancienne_ligne in ligne:
                f.write(nouvelle_ligne)
            else:
                f.write(ligne)



def trouver_chapitre(ref_cours):
    '''A partir de la reference du cours, trouve le ou les numero de chapitre et renvoie dans num_chapitre'''
    num_chapitre=ref_cours.split(';')
    if len(num_chapitre)<=1:
        num_chapitre=ref_cours.split('-')[1]
    else:
        num_chap=''
        for chap in num_chapitre:
            num_chap+=chap.split('-')[1]+' et '
        num_chapitre=num_chap[:-4]
    return num_chapitre
    
def trouve_exo_source(support):
    '''A partir d'un support renvoie le nom de l'exo et sa source'''
    classeur=xlrd.open_workbook('inventaire_exos.xlsx')
    feuilles=classeur.sheet_names()
    col_domaine,col_fichier,col_exo,col_sources=0,1,2,3
    exo,source='',''
    for f in feuilles:
        if "exos" in f:
            fs=classeur.sheet_by_name(f)
            k=1
            while fs.cell_value(k,0)!='fin':
                if fs.cell_value(k,col_domaine)+'/'+fs.cell_value(k,col_fichier)==support:
                    exo=fs.cell_value(k,col_exo)
                    source=fs.cell_value(k,col_sources)
                k+=1
    return exo,source

def genere_entete(rep,info_activite,type_activite):
    """A partir du cours dont le chemin est donne par rep la fonction genere l'entete donnant toutes infos permettant de generer l'entete du cours."""
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
    #competences=competences.split(';')
    num_chapitre=trouver_chapitre(ref_cours)
    if type_activite=='cours':
        chemin_relatif='../../'
    if type_activite=='tp':
        chemin_relatif='../../../'
    if type_activite=='cours':
        file_entete=rep+sep+'info_entete.tex'
        if os.path.exists(rep+sep+'cours/'):
            os.system('rm -Rf '+rep+sep+'cours/')
        if os.path.exists(rep+sep+'TD_01/'):
            os.system('rm -Rf '+rep+sep+'TD_01/')
        if os.path.exists(rep+sep+'TP_01/'):
            os.system('rm -Rf '+rep+sep+'TP_01/')
        if os.path.exists(rep+sep+'cours.tex')==False:
            os.system('cp style/cours0.tex '+rep+sep+'cours.tex')
        if os.path.exists(rep+sep+'td.tex')==False:
            os.system('cp style/td0.tex '+rep+sep+'td.tex')
        if os.path.exists(rep+sep+'images/')==False:
            os.system('mkdir '+rep+sep+'images/')
    elif type_activite=='tp':
        file_entete=rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre[0])+'_TP_'+num_activite+sep+'info_entete.tex'
    else:
        print("mauvais choix d'activite")
    with open(file_entete,'w',encoding='utf-8') as f:
        texte_entete=''
        with open('style'+sep+'info_Entete0.tex','r',encoding='utf-8') as f0:
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
                    texte_entete+='\\def\\xxnumchapitre{'+str(num_chapitre)+'}\n'
                elif '\\def\\xxnumactivite' in ligne:
                    texte_entete+='\\def\\xxnumactivite{'+str(num_activite)+'}\n'
                elif '\\def\\xxchapitre' in ligne:
                    texte_entete+='\\def\\xxchapitre{'+str(num_chapitre)+'}\n'
                elif '\\def\\xxdate' in ligne:
                    texte_entete+='\\def\\xxdate{'+date+'}\n'
                elif '\\chapterimage{' in ligne:
                    texte_entete+='\\chapterimage{'+figures+'}\n'
                elif '\\lstinputpath{}' in ligne:
                    texte_entete+='\\lstinputpath{'
                    for support in supports.split(';'):
                        texte_entete+='{'+chemin_relatif+'exos/'+support+'/}'
                    texte_entete+='}\n'
                elif '\\graphicspath{{../../style/png/}{images/}' in ligne:
                    texte_entete+='\\graphicspath{{'+chemin_relatif+'style/png/}{images/}'
                    for support in supports.split(';'):
                        texte_entete+='{'+chemin_relatif+'exos/'+support+'/}'
                    texte_entete+='}\n'
                elif '\\begin{itemize}[label=\\ding{112},font=\\color{ocre}]' in ligne:
                    texte_entete+='\\begin{itemize}[label=\\ding{112},font=\\color{ocre}]\n'
                    code_competence,nom_long,nom_court=trouver_texte_competence(competences,path)
                    for k in range(len(code_competence)):
                        texte_entete+='\\item '+code_competence[k]+' : '+nom_court[k]+'\n'
                elif '%Infos sur les supports' in ligne:
                    texte_entete+='%Infos sur les supports\n'
                    for support in supports.split(';'):
                        exo,source=trouve_exo_source(support)
                        texte_entete+='\\def\\xxtitreexo{'+exo+'}\n'
                        texte_entete+='\\def\\xxsourceexo{\\hspace{.2cm} \\footnotesize{'+source+'}}\n'
                else: 
                    texte_entete+=ligne
        f.write(texte_entete)

def trouver_texte_competence(competences,path):
    '''A partir d'une liste de competence renvoie la competence detaillee'''
    classeur=xlrd.open_workbook(path)
    feuilles=classeur.sheet_names()
    col_code,col_nom_long,col_nom_court=0,1,2
    for f in feuilles:
        if "Competences" in f:
            fs=classeur.sheet_by_name(f)
            k=1
            nom_court=[]
            nom_long=[]
            code_competence=[]
            while fs.cell_value(k,0)!='fin':
                if fs.cell_value(k,col_code) in competences and fs.cell_value(k,col_code)!='':
                    nom_court.append(fs.cell_value(k,col_nom_court))
                    nom_long.append(fs.cell_value(k,col_nom_long))
                    code_competence.append(fs.cell_value(k,col_code))
                k+=1
    return code_competence,nom_long,nom_court
    
        
def genere_support(rep,info_activite,type_activite):
    '''A partir d'une activite genere le fichier support'''
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
    rep=trouver_repertoire(info_activite) 
    num_chapitre=trouver_chapitre(ref_cours)
    if type_activite=='cours':
        rep_activite=rep+sep+'td.tex'
        # print(num_activite,rep_activite,supports)
    elif type_activite=='tp':
        rep_activite=rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre[0])+'_TP_'+num_activite+sep+'tp.tex'
    with open(rep_activite,'w',encoding='utf-8') as f:
        if len(supports)>0:
            for support in supports.split(';'):
                if type_activite=='cours':
                    f.write('\\input{'+'../../exos/'+support+'}\n')
                elif type_activite=='tp':
                    f.write('\\input{'+'../../../exos/'+support+'}\n')
        else:
            f.write('\n')
    return None

# type_activite='tp'
# info_activite=info_tp[0]
# (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
# rep=trouver_repertoire(info_activite) 
# num_chapitre=trouver_chapitre(ref_cours)
# if type_activite=='cours':
#     rep_activite=rep+'/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TD_'+num_activite
# elif type_activite=='tp':
#     rep_activite=rep+'/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite
# with open(rep_activite+'/tp.tex','w',encoding='utf-8') as f:
#     for support in supports.split(';'):
#         f.write('\\input{'+'../../../exos/'+support+'}\n')
# #     



  
  #######
#Programme Principal
#######

(info_tp,info_cours)=lire_semanier(path)

for cours in info_cours:
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=cours
    rep=trouver_repertoire(cours)
    genere_fichiers_tex(cours,'cours')
    genere_entete(rep,cours,'cours')
    genere_support(rep,cours,'cours')
    
for tp in info_tp:
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=tp
    rep=trouver_repertoire(tp)
    genere_fichiers_tex(tp,'tp')
    genere_entete(rep,tp,'tp')
    genere_support(rep,tp,'tp')
    

