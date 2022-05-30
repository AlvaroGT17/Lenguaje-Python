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
promedio=[]
mayortemperatura=0

# Intento fallido: 

'''for x in range(4):
  paises.append(input(f"Ingrese el nombre del {x+1}º País: "))
  for y in range(3):
    ingresotemperatura.append(float(input(f"Ingrese la {y+1}º temperatura del {x+1}º país introducido: ")))
  temperaturas.append(ingresotemperatura)
  ingresotemperatura=[]

print("La lista de países introducidos son: ",paises)
print("La temperatura de los países respectivamente es: ",temperaturas)

for x in range(len(paises)):
  print (f"El país {paises[x]} tiene un promedio de temperaturas de:")
  for y in range(len(temperaturas)):
    for z in range(len(temperaturas[y])):
      suma=(suma+temperaturas[y][z])//3
    promedio.append(suma)
    suma=0
  print(promedio)





    if promedio>mayortemperatura:
      mayortemperatura=x
    promedio=0
print("El país con mayor temperatura es: ",paises[mayortemperatura])'''


paises = []
temperaturas = []
promediotemp = []

for x in range(4):
    nom = input("Ingrese el nombre del pais:")
    paises.append(nom)
    temp1 = int(input("Ingrese primer temperatura:"))
    temp2 = int(input("Ingrese segunda temperatura:"))
    temp3 = int(input("Ingrese tercer temperatura:"))
    temperaturas.append([temp1, temp2, temp3])

print("Paises y temperaturas medias de los ultimos tres meses mensuales")
for x in range(4):
    print(paises[x], temperaturas[x][0],
          temperaturas[x][1], temperaturas[x][2])

for x in range(4):
    pro = (temperaturas[x][0]+temperaturas[x][1]+temperaturas[x][2])//3
    promediotemp.append(pro)

print("Paises y temperaturas medias trimestrales")
for x in range(4):
    print(paises[x], promediotemp[x])

posmayor = 0
for x in range(1, 4):
    if promediotemp[x] > promediotemp[posmayor]:
        posmayor = x
print("Pais con temperatura media trimestral mayor:", paises[posmayor])
