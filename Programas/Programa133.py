# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y mostrar
# todos los valores mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.


def ingreso():
  lis=[]
  for x in range(5):
    lis.append(int(input("Ingrese el numero que desea agregar a la lista: ")))
  print("La lista quedara de la siguiente manera: ", lis)
  return lis

def clasificador(lis):
  listadefinitiva=[]
  for x in range(5):
    if lis[x]>10:
      listadefinitiva.append (lis[x])
  return print("Los número mayores de 10 de la lista ingresada son: ", listadefinitiva)

# Bloque principal:

lis=ingreso()
clasificador(lis)
