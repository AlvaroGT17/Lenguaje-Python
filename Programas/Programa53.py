# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

numero=0
negativos=0
positivos=0
multiplos=0
suma=0

for x in range(10):
  numero=int(input("Ingrese un número: "))

  if numero<0:
    negativos=negativos+1
  if numero>0:
    positivos=positivos+1
  if (numero%15)==0:
    multiplos=multiplos+1
  if (numero%2)==0:
    suma=suma+numero

print("La cantidad de valores ingresados negativos es de: ", negativos)
print("La cantidad de valores ingresados positivos es de: ", positivos)
print("La cantidad de múltiplos de 15 es de: ", multiplos)
print("El valor acumulado de los números ingresados que son pares es de: ", suma)