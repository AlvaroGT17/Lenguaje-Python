# Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
# Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
# Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
# a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
# b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
# c - Calcular la temperatura media trimestral de cada país.
# c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
# b - Imprimir el nombre del pais con la temperatura media trimestral mayor.

paises=[]
temperaturas=[]
ingresotemperatura=[]
suma=0
promedio=0


for x in range(4):
  paises.append(input(f"Ingrese el nombre del {x+1}º País: "))
  for y in range(3):
    ingresotemperatura.append(float(input(f"Ingrese la {y+1}º temperatura del {x+1}º país introducido: ")))
  temperaturas.append(ingresotemperatura)
  ingresotemperatura=[]

print(paises)
print(temperaturas)

for x in range(len(paises)):
  print (paises[x])
  for y in range(len(temperaturas)):
    for z in range(len(temperaturas[y])):
      suma=suma+temperaturas[y][z]
    promedio=suma/3
    suma=0

  print(promedio)
  promedio=0