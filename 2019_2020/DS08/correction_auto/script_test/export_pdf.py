import os
import subprocess

files=os.listdir()
cmd_print='/usr/local/bin/pdftk '
for f in files:
    if '.' not in f and (f!='tops' and f!='topdf' and f!='mypdf' and f!='export_pdf' and f!='test_TP'):
        #print(f)
        file=f+'/'+'testeur.pdf'
        os.system('cp '+file+' '+f+'.pdf')
        cmd="/usr/local/bin/pdftk "+file+" dump_data | sed -e '/NumberOfPages/!d;s/NumberOfPages: //'"
        reply = subprocess.Popen(cmd, universal_newlines=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 shell=True)
        nbpage=int(reply.stdout.readline()[:-1])
        nbpage_sup=nbpage%4
        #print(nbpage,nbpage_sup)
        cmd_print+=file+' '+nbpage_sup*' blank.pdf '

cmd_print+=' cat output bilan_total.pdf'

os.system(cmd_print)


