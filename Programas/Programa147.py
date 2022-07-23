# Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe retornar.
# La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.

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