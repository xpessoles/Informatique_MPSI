# with open('teste_encodage.txt','w',encoding='utf8') as f:
#     f.write('ça va ?')
#
# with open('teste_encodage.txt','r',encoding='utf8') as f:
#     a=f.read()
#
#

with open('sainte_lyon.csv','r',encoding='utf8') as f:
    f.readline()
    T=f.readlines()
    T2=[]
    for x in T:
        nom,chrono=x.strip().split(';')
        h,m,s=chrono.split(':')
        tp=int(h)*3600+int(m)*60+int(s)
        v=72/tp*3600
