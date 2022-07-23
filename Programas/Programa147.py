# Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. Modificar la lista y luego convertir la lista en tupla.

def cargarfecha():
  dia=int(input("Ingrese el día: "))
  mes=int(input("Ingrese el mes: "))
  año=int(input("Ingrese el año: "))
  return (dia,mes,año)

def imprimir_fecha(fecha):
  print(fecha[0],fecha[1],fecha[2],sep="/")

# Bloque principal del programa.

fecha=cargarfecha()
imprimir_fecha(fecha)
fecha=list(fecha)
print(fecha)
fecha[1]=23
imprimir_fecha(fecha)
fecha=tuple(fecha)
print(fecha)