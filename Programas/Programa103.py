# Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista.
# El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
# Mostrar la lista y la suma de todos sus elementos.

from re import S


listaprincipal=[]
listasinternas=[]
suma=0

numeroprincipal=int(input("Ingrese el numero de sublistas que tendrá la lista principal: "))

for y in range(numeroprincipal):
  numerosecundario=int(input(f"Ingrese el número de elementos que contendrá la sublista {y+1}: "))
  for x in range(numerosecundario):
    listasinternas.append(int(input(f"Ingrese el {x+1}º numero de la lista interna: ")))
  listaprincipal.append(listasinternas)
  listasinternas=[]

print(listaprincipal)

for y in range(len(listaprincipal)):
  for x in range(len(listaprincipal[y])):
    suma=suma+listaprincipal[y][x]

print("El resultado de la suma de todos los valores de las sublistas es: ",suma)