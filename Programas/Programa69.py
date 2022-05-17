# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

x=0
suma=0
lista=[1,2,3,4,5]

while x<len(lista):
  suma=suma+lista[x]
  x=x+1
  
print("Los elementos de la lista son: ", lista)
print("Y su suma da: ", suma)
