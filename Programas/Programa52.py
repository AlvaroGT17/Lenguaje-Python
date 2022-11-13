# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese
# la cantidad de puntos a procesar.

cantidad=int(input("Cuantas coordenadas quiere introducir? "))
x=0
y=0
cuadrante1=0
cuadrante2=0
cuadrante3=0
cuadrante4=0

for f in range(cantidad):
  x=float(input("Ingrese el valor x de la coordenada "))
  y=float(input("Ingrese el valor y de la coordenada "))

  if x>0 and y>0:
    cuadrante2=cuadrante2+1
  elif x<0 and y>0:
    cuadrante1=cuadrante1+1
  elif x<0 and y<0:
    cuadrante3=cuadrante3+1
  else:
    cuadrante4=cuadrante4+1

print("El número de coordenadas en el 1º cuadrante es de: ", cuadrante1)
print("El número de coordenadas en el 2º cuadrante es de: ", cuadrante2)
print("El número de coordenadas en el 3º cuadrante es de: ", cuadrante3)
print("El número de coordenadas en el 4º cuadrante es de: ", cuadrante4)