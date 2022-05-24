# Crear una lista por asignación. La lista tiene que tener 5 elementos.
# Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos elementos, la tercera tres elementos
# y así sucesivamente. Sumar todos los valores de las listas.

listadelistas=[]
sublista=[]

for y in range(1,6):
  for x in range(y):
    sublista.append(int(input(f"Ingresa un número para introducirlo en la sublista {y}: ")))
    print(sublista)
    listadelistas.append(sublista)
    print(listadelistas)
  sublista=[]
input("presiona enter para continuar...")


print(listadelistas)