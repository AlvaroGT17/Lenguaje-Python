# Solicitar por teclado 3 enteros. El primer valor indica la cantidad de elementos que crearemos en la lista.
# El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal
# y el tercero sera el numero de listas internas en las sublistas.
# Mostrar la lista y la suma de todos sus elementos.

lista=[]
sublista=[]
listainterna=[]
cantidad=0
suma=0

cantidad=int(input("Ingrese el número de sublistas que habrá en la lista principal: "))

for x in range(cantidad):
  cantidad=int(input(f"Ingrese el numero de listas internas que tendrá la sublista {x+1}: "))
  for y in range(cantidad):
    cantidad=int(input(f"Ingrese el numero de elementos que tendrá la lista interna {x+1}: "))
    for z in range(cantidad):
      listainterna.append(int(input(f"Ingrese el {z+1}º valor de la lista interna {y+1}: ")))
    sublista.append(listainterna)
    listainterna=[]
  lista.append(sublista)
  sublista=[]

print(lista)

for x in range(len(lista)):
  for y in range(len(lista[x])):
    for z in range(len(lista[x][y])):
      suma=suma+lista[x][y][z]

print(f"El resultado de la suma de todos los valores es de: {suma}")