# Se tiene la siguiente lista:

# lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

# Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
# Volver a imprimir la lista.

'''
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)

for x in range(len(lista[0])):
    if lista[0][x]>50:
        lista[0][x]=0

print(lista)
'''

'''En vista de que no me salia sin necesidad de ayuda he modificado el ejercicio y ahora no solo lo hace lo de la primera parte del ejercicio
si no que lo hace en todas las sublistas'''

lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

for y in range(len(lista)):
  for x in range(len(lista[y])):
    if lista[y][x]>50:
      lista[y][x]=0

print(lista)