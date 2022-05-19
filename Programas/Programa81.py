# Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde
# se encuentra.

lista=[]

for x in range(5):
  lista.append(int(input("Ingrese un número para añadir a la lista: ")))

menor=lista[0]
posicion=0

for x in range (1,5):
  if lista[x]<menor:
    menor=lista[x]
    posicion=x


print("El contenido de la lista es: ", lista)
print("El menor de la lista es: ", menor)
print("Y ocupa la posición: ", x)