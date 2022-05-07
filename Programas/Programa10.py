# Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.

numero1=int(input("Ingrese un número al azar: "))
numero2=int(input("Ingrese un segundo número al azar"))

if numero1>numero2:
  print("El número ", numero1, " es mayor que ", numero2)
else:
  print("El número ", numero2, " es mayor que ", numero1)