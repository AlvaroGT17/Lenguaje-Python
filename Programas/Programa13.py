# Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

numero=int(input("Igrese un numero: "))

if numero >= 10:
  print("El numero ", numero, " tine dos dígitos.")
else:
  print("El número ", numero, " tiene un solo dígito.")