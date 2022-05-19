# Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas.
# Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

productos=[]
precios=[]
cantidad=0

for x in range(5):
  productos.append(input("Ingrese el nombre del producto: "))
  precios.append(int(input("Ingrese el precio del producto: ")))

for x in range(1,5):
  if precios[0]<precios[x]:
    cantidad=cantidad+1

print("El número de productos con un precio superior al primer producto es: ", cantidad)