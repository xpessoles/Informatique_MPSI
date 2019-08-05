#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "Xavier Pessoles"
""" Génération de la banque d'exos"""

import os
os.chdir("C:\GitHub\Informatique_MPSI\exos")
dossiers_exos = os.listdir()
dossiers_exos.remove("architecture")
fid = open("..\\Livrets\\Banque_Exercices\\banque.tex","w")
for dossier in dossiers_exos:
    exos_tex = os.listdir(dossier)
    dos = dossier.replace('_'," ")
    fid.write("\\section*{"+dos+"}\n")
    for exo in exos_tex :
        if 'tex' in exo and not('cor') in exo:
            grpath = exo[:-4]
            fid.write("\\renewcommand{\\xxexo}{"+exo+"} \n")
            fid.write("\\subsection*{\\xxexo} \n")
            fid.write("\\graphicspath{{../../exos/"+dossier+"/"+grpath+"/}}\n")
            fid.write("\\input{../../exos/"+dossier+"/\\xxexo} \n \n")

fid.close()
    