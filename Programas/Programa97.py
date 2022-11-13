# Crear una lista por asignación. La lista tiene que tener 5 elementos.
# Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos elementos, la tercera tres elementos
# y así sucesivamente. Sumar todos los valores de las listas.

listadelistas=[]
sublista=[]
valor=0

# Construir los sublistados

for y in range(1,6):
  for x in range(y):
    sublista.append(int(input(f"Ingresa un número para introducirlo en la sublista {y}: ")))
    print(sublista)
  listadelistas.append(sublista)
  sublista=[]
  print(listadelistas)
input("presiona enter para continuar...")

print("")
print(listadelistas)

# Aquí lo que hacemos es recorrer de nuevo el listado principal con el primer for y con el segundo for repasamos el contenido de las sublistas 
# y ejecutamos la suma de los valores.

for k in range(len(listadelistas)):
    for x in range(len(listadelistas[k])):
      valor=valor+listadelistas[k][x]
    print(valor)

print("El valor de todos los campos de la lista y sublistas es de: ",valor)
