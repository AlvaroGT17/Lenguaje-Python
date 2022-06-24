# Confeccionar un programa que permita:
#   1) Cargar una lista de 10 elementos enteros.
#   2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
#   3) Imprimir las dos listas generadas.


def ingreso():
  lista=[]
  for x in range(10):
    lista.append(int(input(f"Ingrese el {x+1}º número: ")))
  return lista

def seleccionador(lista):
  listapositivos=[]
  listanegativos=[]
  for x in range(len(lista)):
    if lista[x]>=0:
      listapositivos.append (lista[x])
    else:
      listanegativos.append (lista[x])
  print("La lista generada con los números positivos es: ", listapositivos)
  print("La lista generada con los números negativos es: ", listanegativos)

# Cuerpo principal del programa:

lista=ingreso()
seleccionador(lista)