# Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e
# imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.

pais=[]
poblacion=[]

for x in range(5):
  pais.append(input(f"Ingrese el nombre del {x+1}º País: "))
  poblacion.append(float(input(f"Ingrese la población del {x+1}º País: ")))

print("")

for x in range(5):
  print("El país ",pais[x], "tiene ",poblacion[x],"habitantes.")

input("Presione enter para continuar...")

for y in range(4):
  for x in range(4-y):
    if pais[x]>pais[x+1]:
      auxpais=pais[x]
      auxpoblacion=poblacion[x]
      pais[x]=pais[x+1]
      poblacion[x]=poblacion[x+1]
      pais[x+1]=auxpais
      poblacion[x+1]=auxpoblacion

print("")
print("Este es el aspecto de las listas ordenadas alfabéticamente por el nombre del país")
print("")


for x in range(5):
  print("El país ", pais[x], "tiene ", poblacion[x], "habitantes.")

input("Presione enter para continuar...")

for y in range(4):
  for x in range(4-y):
    if poblacion[x]<poblacion[x+1]:
      auxpais = pais[x]
      auxpoblacion = poblacion[x]
      pais[x] = pais[x+1]
      poblacion[x] = poblacion[x+1]
      pais[x+1] = auxpais
      poblacion[x+1] = auxpoblacion

print("")
print("Este es el aspecto de las listas ordenadas de mayor a menor según el numero de habitantes del país")
print("")

for x in range(5):
  print("El país ", pais[x], "tiene ", poblacion[x], "habitantes.")
