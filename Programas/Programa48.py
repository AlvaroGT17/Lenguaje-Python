# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

suma=0

for x in range(1,11):
  valor=int(input("Ingrese el número que dese "))
  if x>5:
    suma=suma+valor
print(suma)
