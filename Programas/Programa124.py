# Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def promedio(num1, num2, num3):
  prome=(num1+num2+num3)/3
  return prome

# Cuerpo del programa

numero1=int(input("Ingrese el número que dese: "))
numero2=int(input("Ingrese el número que dese: "))
numero3=int(input("Ingrese el número que dese: "))
print("El promedio de los número ingresados es: ", promedio(numero1, numero2, numero3))