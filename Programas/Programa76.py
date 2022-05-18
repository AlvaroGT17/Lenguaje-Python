# Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero.
# Mostrar finalmente el tamaño de la lista.

lista=[]

numero=int(input("Ingrese un número entero para agregarlo al array: "))

while numero!=0:
  lista.append(numero)
  numero=int(input("Ingrese un número entero para agregarlo al array o 0 para finalizar el ingreso de valores: "))

print(lista)
print("El tamaño del array es de ", (len(lista)), "elementos.")
