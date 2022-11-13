# Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
# Imprimir sus elementos accediendo de diferentes modos.

lista1=[]
lista2=[]
lista3=[]
lista4=[]
listadelistas=[]


for x in range(3):
  lista1.append(int(input("Ingrese el valor para la 1º lista: ")))
for x in range(3):
  lista2.append(int(input("Ingrese el valor para la 2º lista: ")))
for x in range(3):
  lista3.append(int(input("Ingrese el valor para la 3º lista: ")))
for x in range(3):
  lista4.append(int(input("Ingrese el valor para la 4º lista: ")))

listadelistas.append(lista1)
listadelistas.append(lista2)
listadelistas.append(lista3)
listadelistas.append(lista4)

# imprimimos la lista completa
print(listadelistas)
print("---------")
# imprimimos la primer componente
print(listadelistas[0])
print("---------")
# imprimimos la primer componente de la lista contenida
# en la primer componente de la lista principal
print(listadelistas[0][0])
print("---------")
# imprimimos con un for la lista contenida en la primer componente
for x in range(len(listadelistas[0])):
    print(listadelistas[0][x])
print("---------")
# imprimimos cada elemento entero de cada lista contenida en la lista
for k in range(len(listadelistas)):
    for x in range(len(listadelistas[k])):
        print(listadelistas[k][x])
