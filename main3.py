try:
  file = open("archivo_inexistente.txt", 'r')
  lineas = file.readlines()
  print(lineas[0])
except:
  print("Error al abrir el archivo")
finally:
  quit()
