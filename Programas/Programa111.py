# Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

lista=[]
sublista=[]
posicion=0

for x in range(5):
  lista.append(int(input("Ingrese un numero en el lista: ")))

print("Lista completa: ", lista)

while posicion<(len(lista)):
  if lista[posicion] >=10:
    sublista.append(lista.pop(posicion))
    print(sublista)
  else:
    posicion=posicion+1

print("Lista reducida: ", sublista)