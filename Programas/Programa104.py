# Definir dos listas de 3 elementos.
# La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
# La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
# Imprimir los nombres del padre, la madre y sus hijos.
# También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.


padres=[]
hijos=[]
grupos=[]

cantidad=int(input("Ingrese el numero de familias a registrar: "))

for x in range(cantidad):
  for y in range(2):
    if y==0:
      grupos.append(input(f"Ingrese el nombre del padre de la {x+1}º familia: "))
    elif y==1:
        grupos.append(input(f"ingrese el nombre de la madre de la {x+1}º familia: "))
  padres.append(grupos)
  grupos=[]
  cantidad=int(input(f"Ingrese el número de hijos que tiene la {x+1}º familia: "))
  for z in range(cantidad):
    grupos.append(input(f"Introduzca el nombre del {z+1}º hijo de la familia: "))
  hijos.append(grupos)
  grupos=[]

print(padres)
print(hijos)

for x in range(len(padres)):
  print("Padre: ", padres[x][0])
  print("Madre: ", padres[x][1])
  print("El nombre de los hijos es:")
  for y in range(len(hijos[x])):
    print(hijos[x][y])

for x in range(len(padres[x])):
  print(f"El señor {padres[x][0]} tiene: {len(hijos[x])}")