# Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.

lista=[]
posicion=0

for x in range(10):
  lista.append(int(input("Ingrese un numero del 1 al 10: ")))

print(f"La lista completa es: {lista}")

while posicion<(len(lista)):
  if lista[posicion]==5:
    lista.pop(posicion)
  else:
    posicion=posicion+1

print(f"La lista después de eliminar elementos queda: {lista}")