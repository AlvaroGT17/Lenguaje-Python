# Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene.
# En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces.
# Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.


def conteo(cadena):
  numeroletras=len(cadena)
  return numeroletras

def comparacion(num1, num2):
  if num1>num2:
    return num1
  else:
    return num2

def palabra(string1, string2):
  numeroletras1 = len(string1)
  numeroletras2 = len(string2)

  if numeroletras1 > numeroletras2:
    return string1
  elif numeroletras1==numeroletras2:
    iguales="ninguna por que son iguales"
    return iguales
  else:
    return string2

# Cuerpo del programa

palabras1=(input("Ingrese la cadena de caracteres deseada: "))
numero1=(conteo(palabras1))
palabras2=(input("Ingrese la cadena de caracteres deseada: "))
numero2=(conteo(palabras2))
print(f"La cadena de caracteres con más letras es: {palabra(palabras1, palabras2)}, con un total de {comparacion(numero1, numero2)} caracteres.")