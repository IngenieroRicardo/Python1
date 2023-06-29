lineas = ["Linea 1\n", "Linea 2\n", "Linea 3\n"] 

file = open('texto.txt', 'w')
file.writelines(lineas)
file.close()
