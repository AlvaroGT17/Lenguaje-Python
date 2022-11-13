cmd# Desarrollar una función que reciba un string como parámetro y nos muestre la cantidad de vocales.
# Llamarla desde el bloque principal del programa 3 veces con string distintos.


def contador(palabra):
  cantidad = 0
  for x in range(len(palabra)):
    if palabra[x] == "a" or palabra[x] == "A" or palabra[x] == "e" or palabra[x] == "E" or palabra[x] == "i" or palabra[x] == "I" or palabra[x] == "o" or palabra[x] == "O" or palabra[x] == "u" or palabra[x] == "U":
      cantidad=cantidad+1
  print("La palabra", palabra, "contiene ", cantidad, "vocales.")

def introducir():
  palabra=(input("Introduzca la palabra a analizar: "))
  contador(palabra)

# Cuerpo del programa.

introducir()
introducir()
introducir()
