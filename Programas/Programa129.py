# Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implementar una función que imprima el mayor y el menor
# valor de la lista.

def mayormenor(numeracion):

  comparadormayor=numeracion[0]
  for x in range(1,len(numeracion)):
    if numeracion[x]>comparadormayor:
      comparadormayor=numeracion[x]

  comparadormenor=numeracion[0]
  for x in range(1,len(numeracion)):
    if numeracion[x]<comparadormenor:
      comparadormenor=numeracion[x]

  return print(f"El número de mayor valor es {comparadormayor} y el número de menor valor es {comparadormenor}  ")


lista=[]

for x in range(5):
  datos=int(input(f"Ingrese el {x+1}º número de la lista: "))
  lista.append(datos)

print("La lista quedará de la siguiente manera", lista)
mayormenor(lista)