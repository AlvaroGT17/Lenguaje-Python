# Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

numero1=int(input("Deme el primer número: "))
numero2=int(input("Deme el segundo número: "))
numero3=int(input("Dame el tercer número: "))

if numero1>numero2 and numero1>numero3:
  print("El numero ", numero1, "es el mayor.")
elif numero1<numero2 and numero2>numero3:
  print("El numero ", numero2, "es el mayor.")
else:
  print("El numero ", numero3, "es el mayor.")