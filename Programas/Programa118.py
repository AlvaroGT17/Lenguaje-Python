# Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

def  cuadrado(valor1):
  perimetro=valor1*4
  print("El perímetro del cuadrado es: ",perimetro)

def cuadrado2(valor1):
  superficie=valor1*2
  print("La superficie del cuadrado es: ", superficie)

def ingreso():
  valor=(float(input("Ingrese el valor de un lado: ")))
  eleccion=(int(input("Ingrese 1 para conocer el perímetro o 2 para conocer la superficie: ")))

  if eleccion == 1:
    cuadrado(valor)
  else:
    cuadrado2(valor)

# Seccion principal

ingreso()
