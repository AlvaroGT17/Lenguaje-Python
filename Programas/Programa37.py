# Realizar un programa que permita cargar dos listas de 15 valores cada una.
# Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

x=1
y=1
valor1=0
valor2=0
numero=0

while x<=15:
  numero=int(input("Ingrese un número para la primera lista: "))
  valor1=valor1+numero
  x=x+1

while y<=15:
  numero=int(input("Ingrese un número para la segunda lista: "))
  valor2=valor2+numero
  y=y+1

if valor1>valor2:
  print("La primera lista es la mayor")
elif valor1==valor2:
  print("Las dos listas son iguales")
else:
  print("La segunda lista es la mayor")