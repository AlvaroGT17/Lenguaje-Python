# Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno.

n=int(input("Ingrese cuanto número quiere que se impriman: "))
intervalos=int(input("En que número de intervalo quiere que se impriman los números??? "))
x=1
while x<=n:
  print(x)
  x=x+intervalos
