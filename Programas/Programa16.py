# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

numero=int(input("Ingrese un número:"))

if numero>0:
  print("El número es positivo.")
elif numero==0:
  print("El número es nulo.")
else:
  print("El número es negativo.")