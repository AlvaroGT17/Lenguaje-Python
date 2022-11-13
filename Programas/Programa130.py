# Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero.
# Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

#  lista = [3, 7, 8, 10, 2]
#  multiplicar(lista, 3)


def multiplicador(lista, multiplicado):
  listaresuelta=[]
  for x in range(len(lista)):
    numeroindibidual=lista[x]*multiplicado
    listaresuelta.append(numeroindibidual)
  return print(listaresuelta)

lista = [3, 7, 8, 10, 2]
multiplicado=(int(input("Ingrese el número por el cual sera multiplicado la lista: ")))

print(lista)
multiplicador(lista, multiplicado)

