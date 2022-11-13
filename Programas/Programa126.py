# Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros
# los valores de dos de sus lados, En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar
# cual de los dos tiene una superficie mayor.

def rectangulo(lado1, lado2):
  superficie=lado1*lado2
  return superficie

def mayor(rectangulo1, rectangulo2):
  if rectangulo1>rectangulo2:
    return print("El rectangulo mayor es el rectangulo 1")
  else:
    return print("El rectangulo mayor es el rectangulo 2")

# Cuerpo principal del programa

numero1=int(input("Ingrese el primer lado del rectángulo: "))
numero2=int(input("Ingrese el segundo lado del rectángulo: "))
rectangulo1 = rectangulo(numero1, numero2)
print("El perímetro del rectángulo ingresado es: ",rectangulo(numero1, numero2))
numero1=int(input("Ingrese el primer lado del rectángulo: "))
numero2=int(input("Ingrese el segundo lado del rectángulo: "))
rectangulo2 = rectangulo(numero1, numero2)
print("El perímetro del rectángulo ingresado es: ",rectangulo(numero1, numero2))
print(mayor(rectangulo1, rectangulo2))