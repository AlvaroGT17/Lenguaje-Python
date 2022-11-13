# Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
# Definir las siguientes funciones:
#   1) Cargar los nombres de artículos y sus precios.
#   2) Imprimir los nombres y precios.
#   3) Imprimir el nombre de artículo incrementando su valor 5%
#   4) el nombre de artículo con un precio mayor
#   5) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.


def ingreso():
  articulo=[]
  precio=[]
  for x in range(5):
    articulo.append(input("Ingrese el nombre de producto: "))
    precio.append(float(input("Ingrese el precio del producto antes ingresado: ")))
  print(f"La lista de artículos es {articulo} y la de precios es {precio}")
  print("")
  return [articulo, precio]

def impresion(articulo, precio):
  for x in range(len(articulo)):
    print(f"El articulo {articulo[x]} tiene un precio {precio[x]}€")
  print("")


def incrementoprecio(articulo, precio):
  aumento=0
  for x in range(len(articulo)):
    aumento=precio[x]+(precio[x]*0.21)
    print(f"El articulo {articulo[x]} tiene un precio {aumento}€ con un aumento del 21% por el I.V.A")
    aumento=0
  print("")

def mayorvalor(articulo, precio):
  nombrearticulo=""
  precioarticulo=0
  for x in range(len(articulo)):
    if precio[x]>precioarticulo:
      precioarticulo=precio[x]
      nombrearticulo=articulo[x]
  print(f"El articulo con mayor valor es el articulo {nombrearticulo} con un precio de {precioarticulo}€")
  print("")


def mayoqueseleccion(articulo, precio):
  nombrearticulo = ""
  precioarticulo = 0
  valor=float(input("Ingrese el valor de referencia: "))
  for x in range(len(articulo)):
    if precio[x] < valor:
        precioarticulo = precio[x]
        nombrearticulo = articulo[x]
        print(f"El articulo {nombrearticulo} tiene el precio por debajo del ingresado, {valor}€, teniendo un precio de {precioarticulo}€")
    elif precio[x] == valor:
      precioarticulo = precio[x]
      nombrearticulo = articulo[x]
      print(f"El articulo {nombrearticulo} tiene el precio exacto ingresado {valor}€")

# Cuerpo principal del programa:

articulo, precio=ingreso()
impresion(articulo, precio)
incrementoprecio(articulo, precio)
mayorvalor(articulo, precio)
mayoqueseleccion(articulo, precio)
