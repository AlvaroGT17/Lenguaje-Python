# Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

cordenadasx=int(input("Deme el número de las ordenadas: "))
cordenadasy=int(input("Deme el número de las abcisas: "))

if cordenadasx==0 or cordenadasy==0:
  print("Los valores no pueden ser igual a 0")
elif cordenadasx<0 and cordenadasy>0:
  print("Los valores apuntan al cuadrante superior izquierdo")
elif cordenadasx>0 and cordenadasy>0:
  print("Los valores apuntan al cuadrante superior derecho")
elif cordenadasx<0 and cordenadasy<0:
  print("Los valores apuntan al cuadrante inferior izquierdo")
else:
  print("Los valores apuntan al cuadrante inferior derecho")