# Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor
# e imprimir nuevamente.

numero=[80,56,60,75,12]

print("Esta es la lista de origen: ", numero)

for y in range(4):
  for x in range(4-y):
    if numero[x]>numero[x+1]:
      aux=numero[x]
      numero[x]=numero[x+1]
      numero[x+1]=aux

print("Esta es la lista ordenada de menor a mayor: ", numero)

for y in range(4):
  for x in range(4-y):
    if numero[x] < numero[x+1]:
      aux = numero[x]
      numero[x] = numero[x+1]
      numero[x+1] = aux

print("Esta es la lista ordenada de mayor a menor: ", numero)
