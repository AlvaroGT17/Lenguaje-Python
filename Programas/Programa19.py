# Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.

numero1=int(input("Deme el primer número"))
numero2=int(input("Deme el segundo número"))
numero3=int(input("Deme el tercer número"))

if numero1>numero2 and numero2>numero3:
  print("El mayor es ", numero1)
elif numero1<numero2 and numero2>numero3:
  print("El mayor es ", numero2)
elif numero1<numero3 and numero2<numero3:
  print("El mayor es ", numero3)