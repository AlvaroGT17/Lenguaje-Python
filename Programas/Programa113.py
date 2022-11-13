# Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
# Repetir la carga e impresión de la suma 5 veces.
# Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.

def bienvenida():
  print("************************************")
  print(" Bienvenidos a la simplecalculadora ")
  print("************************************")

def separacion():
  print("")
  print("Sigiente sección")
  print("")

def finalizacion():
  print("**********************************************")
  print(" Gracias por haber usado la simplecalculadora ")
  print("**********************************************")

def ingresoysuma():
  valor1=int(input("Ingrese el primer sumando: "))
  valor2 = int(input("Ingrese el segundo sumando: "))
  suma=valor1+valor2
  print("El resultado de la suma es: ", suma)

def repeticiones():
  for x in range(5):
    ingresoysuma()
    separacion()


# Comienzo del programa.

bienvenida()
separacion()
repeticiones()
separacion()
finalizacion()
