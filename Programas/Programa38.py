# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores,
# por ejemplo 11%2 retorna un 1):
# if valor%2==0:

cantidad=int(input("Ingrese el número de registros que desea: "))
x=1
pares=0
impares=0

while x<=cantidad:
  numero=int(input("Ingresa un número "))
  if numero%2==0:
    pares=pares+1
  else:
    impares=impares+1
  x=x+1

print("En la lista hubo ", pares, "números pares")
print("En la lista hubo ", impares, "números impares")