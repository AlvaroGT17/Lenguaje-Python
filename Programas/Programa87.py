# Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una tercer lista que surja de la
# suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.

lista1=[]
lista2=[]
lista3=[]

for x in range(4):
  lista1.append(int(input("Ingrese un número en la 1º lista: ")))
  lista2.append(int(input("Ingrese un número en la 2º lista: ")))

for x in range(4):
  lista3.append(lista1[x]+lista2[x])

print(lista1)
print(lista2)
print(lista3)
