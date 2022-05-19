# Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se
# encuentra en 2 o más posiciones en la lista)

numero=[]

for x in range(5):
  numero.append(int(input("Ingrese un número para añadir a la lista: ")))

mayor=0
for x in range(1,5):
  if mayor<numero[x]:
    mayor=numero[x]

print("El número mayor es el: ", mayor)

repetido=0

for x in range(1,5):
  if mayor==numero[x]:
    repetido=repetido+1

if mayor>1:
  print("El número ", mayor, "se repite ", repetido, "veces.")