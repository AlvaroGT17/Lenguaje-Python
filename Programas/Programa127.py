# Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'

def palabras(texto):
  contador=0
  for x in range(len(texto)):
    if texto[x]=="A" or texto[x]=="a":
      contador=contador+1
  return contador

# Cuerpo principal del programa:

cadena=input("Ingrese una cadena de texto: ")
print("El número de repeticiones del caracter 'a' es de:", palabras(cadena))
