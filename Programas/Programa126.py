# Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros
# los valores de dos de sus lados

def rectangulo(lado1, lado2):
  superficie=lado1*lado2
  return superficie


# Cuerpo principal del programa

numero1=int(input("Ingrese el primer lado del rectángulo: "))
numero2=int(input("Ingrese el segundo lado del rectángulo: "))
print("El perímetro del rectángulo ingresado es: ",rectangulo(numero1, numero2))