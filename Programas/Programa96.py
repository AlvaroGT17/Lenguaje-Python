# Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
# Calcular y mostrar la suma de cada lista contenida en la lista principal.

listaprincipal=[]
listasecundaria1=[]
listasecundaria2=[]
listasumada=[]
sumando1=0
sumando2=0

for x in range(5):
  listasecundaria1.append(int(input("Introduce el valor deseado para la sublista1: ")))
for x in range(5):
  listasecundaria2.append(int(input("Introduce el valor deseado para la sublista2: ")))

listaprincipal.append(listasecundaria1)
listaprincipal.append(listasecundaria2)

print(listaprincipal)

for x in range(len(listasecundaria1)):
  sumando1=(listaprincipal[0][x])
  sumando2=(listaprincipal[1][x])
  listasumada.append(sumando1+sumando2)

print(listasumada)

'''Las soluciones propuestas por el profesor son las siguientes:

lista=[[1,1,1,1,1], [2,2,2,2,2]]

suma1=lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]+lista[0][4]
print(suma1)
suma2=lista[1][0]+lista[1][1]+lista[1][2]+lista[1][3]+lista[1][4]
print(suma2)
print("----------")

suma1=0
for x in range(len(lista[0])):
    suma1=suma1+lista[0][x]
suma2=0
for x in range(len(lista[1])):
    suma2=suma2+lista[1][x]
print(suma1)
print(suma2)
print("----------")

for k in range(len(lista)):
    suma=0
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
    print(suma)'''