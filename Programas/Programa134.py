# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y retornar el
# mayor y el menor valor de la lista. Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.


def ingreso():
  lista=[]
  for x in range(5):
    lista.append(int(input("Ingrese el número que quiera ingresar en la lista: ")))
  return lista

def mayormenor(datos):
  mayor=lista[0]
  menor=lista[0]
  for x in range(len(lista)):
    if mayor<lista[x]:
      mayor=lista[x]
    if menor>lista[x]:
      menor=lista[x]
  return print(f"El número de mayor valor ingresado en la lista es el {mayor} y el de menor valor es {menor}")

# Bloque principal:

lista= ingreso()
mayormenor(lista)