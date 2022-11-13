# Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

sueldos=[]
sueldooperario=float(input("Ingresa el sueldo del operario "))
sueldos.append(sueldooperario)
suma=sueldooperario

for x in range(4):
  sueldos.append(sueldooperario)
  sueldooperario=float(input("Ingresa el sueldo del operario "))
  suma=suma+sueldooperario

print("La suma de los sueldos es: ",suma)
promedio=(suma/5)
print(sueldos)
print("El promedio de los de los es: ", promedio)


'''Una forma mucho mas fácil y mas clara de resolver este problema seria de la siguiente manera:

sueldos=[]
suma=0
for x in range(5):
    valor=float(input("Ingrese el sueldo del operario:"))
    sueldos.append(valor)
    suma=suma+valor

print("Lista de sueldos")
print(sueldos)
promedio=suma/5
print("Promedio de sueldos")
print(promedio)'''