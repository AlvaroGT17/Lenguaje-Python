# Confeccionar un programa con las siguientes funciones:
#  1)Cargar una lista de 5 enteros.
#  2)Retornar el mayor y menor valor de la lista mediante una tupla.
# Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

def cargaDeValores():
  lista=[]
  for x in range(5):
    lista.append(int(input("Ingrese el valor deseado: ")))
  return lista

def seleccionador(lista):
  mayor=0
  for x in range(len(lista)):
    if lista[x]>mayor:
      mayor=lista[x]
  menor=mayor
  for x in range(len(lista)):
    if lista[x]<menor:
      menor=lista[x]
  return (menor,mayor)

# Bloque principal del programa.

lista=cargaDeValores()
menor,mayor=seleccionador(lista)
print("El número menor que se ha ingresado es:", menor)
print("El número menor que se ha ingresado es:", mayor)