# Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee. Luego imprimir el último elemento de la
# lista principal.

listadelistas=[]
sublista=[]
cantidad=0
subcantidad=0

cantidad=int(input("Cuantas sublistas desea crear? "))

for y in range(cantidad):
  subcantidad=int(input("De cuantos datos constara esta sublista?: "))
  for x in range(subcantidad):
    sublista.append(float(input(f"Ingrese el valor deseado para la sublista Nº {x}: ")))
  listadelistas.append(sublista)
  sublista=[]

print("Este es el aspecto de la lista principal: ", listadelistas)

print(listadelistas[cantidad-1])