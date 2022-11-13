# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo.
# El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

base=0
altura=0
area=0
cantidad=0

c=int(input("Cuantos triangulos van a introducir: "))

for x in range(c):
  base=float(input("Ingrese el valor de la base: "))
  altura=float(input("Ingrese el valor de la altura: "))
  area=(base+altura)/2
  print("El triangulo número: ", x,)
  print("tiene una base de ", base, "una altura de ", altura, "y un area de ", area)
  if area>12:
    cantidad=cantidad+1

print("La cantidad de triángulos cuya superficie es mayor a 12 es de: ", cantidad)