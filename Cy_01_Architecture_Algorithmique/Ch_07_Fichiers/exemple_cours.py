f =open('Cy_01_Ch_07_Cours_PDF.tex', 'r',encoding='utf8')

x = f.readline()
y = f.readline()
f.close()

f=open('test.txt','w')
f.write('Hello')
f.close()