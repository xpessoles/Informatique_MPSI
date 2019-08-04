def int2tex(i):
    if i in [35,36,37,38,95,123,125,126]:
        return '\\'+chr(i)
    elif i == 92:
        return '\\textbackslash'
    elif i == 94:
        return '\\textasciicircum'
    else :
        return chr(i)
    

def construit(nom_de_fichier):
    with open(nom_de_fichier,'w') as f:
        f.write('\\begin{figure}[!h]\n')
        f.write('\\begin{center}\n')
        f.write('\\begin{tabular}{c|c|c|c|c|c|c|c|c|c}\n')
        f.write('\\No & Symbole & \\No & Symbole & \\No & Symbole & \\No & Symbole & \\No & Symbole \\\\\n')
        for i in range(32,47):
            f.write(str(i)+'&\\texttt{'+int2tex(i)+'}&')
            f.write(str(i+20)+'&\\texttt{'+int2tex(i+20)+'}&')
            f.write(str(i+40)+'&\\texttt{'+int2tex(i+40)+'}&')
            f.write(str(i+60)+'&\\texttt{'+int2tex(i+60)+'}&')
            f.write(str(i+80)+'&\\texttt{'+int2tex(i+80)+'}\\\\\n')
        for i in range(47,52):
            f.write(str(i)+'&\\texttt{'+int2tex(i)+'}&')
            f.write(str(i+20)+'&\\texttt{'+int2tex(i+20)+'}&')
            f.write(str(i+40)+'&\\texttt{'+int2tex(i+40)+'}&')
            f.write(str(i+60)+'&\\texttt{'+int2tex(i+60)+'}&')
            f.write(' & \\\\\n')
        f.write('\\end{tabular}\n')
        f.write('\\caption{Table des caractères ASCII}\n')
        f.write('\\label{table.ascii}\n')
        f.write('\\end{center}\n')
        f.write('\\end{figure}')
    return None
