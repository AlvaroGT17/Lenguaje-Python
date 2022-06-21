# Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y nos retorne el producto de
# todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa.


def multiplicador(datos):
  multiplicacion=1
  for x in range(len(datos)):
    multiplicacion=multiplicacion*datos[x]
  return print("El producto de todos los valores de la lista es: ", multiplicacion)

# Bloque principal:

lista=[23,12,54,65,34,23,67,87,89,45,2,34,45]

multiplicador(lista)