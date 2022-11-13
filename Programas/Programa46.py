# Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)
# Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. Lo primero que se hace es cargar una variable
# que indique la cantidad de valores a ingresar. Dicha variable se carga antes de entrar a la estructura repetitiva for.

n=int(input("Ingrese el numero de cantidades a ingresar: "))
numero=0
cantidad=0

for x in range(n):
  numero=int(input("Ingrese el número deseado "))
  if numero>= 1000:
    cantidad=cantidad+1

print("El número de cantidades iguales o superiores a 1000 es de: ",cantidad)