# Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista.
# El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
# Mostrar la lista y la suma de todos sus elementos.

lista=[]
sublista=[]
cantidad=0
suma=0

cantidad=int(input("Ingrese el numero de sublistas que contendrá la lista: "))

for y in range(cantidad):
  cantidad=int(input(f"Ingrese el número de elementos que habrá en la sublista {y+1}: "))
  for x in range(cantidad):
    sublista.append(int(input(f"Ingrese el {x+1}º valor de la lista: ")))
  lista.append(sublista)
  sublista=[]

print(lista)

for y in range(len(lista)):
  for x in range(len(lista[y])):
    suma=suma+lista[y][x]

print("El valor de todos los datos de las sublistas es de: ",suma)