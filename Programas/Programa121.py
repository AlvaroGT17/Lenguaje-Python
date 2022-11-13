# Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def lado_cuadrado(lado):
  superficie=lado*lado
  return superficie

# Cuerpo principal del programa:

valor=int(input("Ingrese el valor del lado del cuadrado deseado: "))
superficie=lado_cuadrado(valor)
print ("La superficie del cuadrado es:", superficie, "mm2")