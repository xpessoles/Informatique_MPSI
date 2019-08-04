#! /usr/bin/python
# -*- coding: utf-8 -*-

# lecture
with open('09-patrimoines-2012-2013.csv', 'rt') as f:
  f.readline() # on ignore la première ligne
  d = f.readlines() # les données intéressantes
# finlecture
# traitementuneligne
def traite_ligne(li):
  v = li.strip().split(';')
  r = (float(v[2]) - float(v[1])) * 0.25
  return v[0] + ';' + str(r) + '\n'
# fintraitementuneligne
# traitementfichier
with open('09-reste-apres-taxation.csv', 'wt') as f:
  f.write('Nom;Reste après taxe (M euros)\n')
  for x in d:
    f.write(traite_ligne(x))
# fintraitementfichier
