# Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
# y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.

numero=int(input("Ingrese un número cualquiera entre 0 y 999: "))

if numero>999:
  print("El número ", numero, " tiene mas de tres dígitos.")
elif numero>99:
  print("El número ", numero, " tiene tres dígitos.")
elif numero>=10:
  print("El número ", numero, " tiene dos dígitos.")
elif numero>=0:
  print("El número ", numero, " tiene un dígito.")
else:
  print("ERROR!!! El numero ", numero, " es negativo y no esta autorizado.")