# Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un país y la cantidad de habitantes.
# Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar el nombre del país con mayor cantidad
# de habitantes.

def creacion_lista():
    pais_habitantes = []
    for x in range(5):
        pais = input("Ingrese el nombre del País: ")
        habitantes = int(input("Ingrese el número de habitantes: "))
        pais_habitantes.append((pais, habitantes))
        pais = ""
        habitantes = 0
    return pais_habitantes


def imprimirLista(lista):
    for x in range(len(lista)):
        print(
            "El país ", lista[x][0], "tiene una población de: ", lista[x][1], "habitantes.")


def mayorPais(lista):
    mayor = 0
    for x in range(len(lista)):
        if lista[x][1] > lista[mayor][1]:
            mayor = x
    print("El país ", lista[mayor][0],
          "es el que más pablación tiene con un número de: ", lista[mayor][1], "habitantes.")


# Bloque principal del programa.

lista = creacion_lista()
imprimirLista(lista)
mayorPais(lista)