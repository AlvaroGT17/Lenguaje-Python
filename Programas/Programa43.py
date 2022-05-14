# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su
# promedio. Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado.

#suma=0

#for x in range(11):
#  suma=suma+x

#print("La suma de la lista es: ",suma)
#promedio=suma/10
#print("El promedio es: ",promedio)

suma=0
numero=0

for x in range(11):
  numero=int(input("Ingrese un numero para la lista: "))
  suma=suma+numero

print("La suma de la lista es: ",suma)
promedio=suma/10
print("El promedio es: ",promedio)