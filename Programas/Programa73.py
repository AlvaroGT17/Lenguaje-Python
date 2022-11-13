# Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

lista=[8,7,6,9,2]
x=0

while x<len(lista):
  if lista[x]>=7:
    print(lista[x])
  x=x+1
