# Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.

paises=[]
aux=""

for x in range(5):
  paises.append(input("Ingrese el nombre del país deseado: "))

print(paises)

for y in range(4):
  for x in range(4-y):
    if paises[x]>paises[x+1]:
      aux=paises[x]
      paises[x]=paises[x+1]
      paises[x+1]=aux

print(paises)