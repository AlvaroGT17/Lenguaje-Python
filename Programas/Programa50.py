# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

numero=int(input("Ingrese un numero del 1 al 10: "))
resultado=0

if numero>=1 and numero<=10:
  print("Número aceptado")
  for x in range(13):
    resultado=numero*x
    print(resultado)
else:
  print("Número fuera de rango")