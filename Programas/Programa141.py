# Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.
'''
for x in range(10):
  if x==9:
    print(x)
  else:
    print(x, end=",")'''
    
# Otra solución mas compleja es la siguiente:

def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")


# bloque principal

lista=cargar()
imprimir(lista)