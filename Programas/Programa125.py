# Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

def perimetro(num1):
  resultado=num1*4
  return resultado

# Cuerpo principal del programa

lado=int(input("Ingrese la longitud del lado del cual hallaremos su perímetro:"))
print("El perímetro de cuadrado es: ", perimetro(lado))