# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.

x=0
ingreso=0
lista=[]

while x<5:
  ingreso=int(input("Ingrese un número para añadirlo al arry. "))
  lista.append(ingreso)
  x=x+1

print(lista)



