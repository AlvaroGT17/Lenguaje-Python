# Definir por asignación una lista de enteros en el bloque principal del programa.
# Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor
# valor y la última recibe la lista y retorna el menor.

def suma(datos):
  resultado = 0
  for x in range(len(datos)):
    resultado=resultado+datos[x]
  return print("La suma de los datos de la lista es: ", resultado)

def mayorvalor(datos):
  resultado = datos[0]
  for x in range(1,len(datos)):
    if datos[x]>resultado:
      resultado = datos[x]
  return print("El mayor número de la lista es: ", resultado)


def menorvalor(datos):
  resultado = datos[0]
  for x in range(1,len(datos)):
    if datos[x] < resultado:
      resultado = datos[x]
  return print("El menor número de la lista es: ", resultado)

# Bloque principal del programa.

lista=[]
tamañolista=int(input("Ingrese el número de datos que tendrá la lista: "))

for x in range(tamañolista):
  datoslista=int(input("Ingrese el número a agregar en la lista: "))
  lista.append(datoslista)

print("Asi es como quedará la lista almacenada: ", lista)

print(suma(lista))
print(mayorvalor(lista))
print(menorvalor(lista))