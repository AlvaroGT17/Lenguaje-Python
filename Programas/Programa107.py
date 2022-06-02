# Desarrollar un programa que cree una lista de 50 elementos.
# El primer elemento es una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.
# La lista debería tener esta estructura y asignarle esos valores a medida que se crean los elementos:

# [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], etc....]

lista=[]
cantidad=1
valor=1

for x in range(50):
  lista.append([])
  for x in range(cantidad):
    lista[x].append(valor)
    valor=valor+1
  cantidad=cantidad+1

print(lista)  