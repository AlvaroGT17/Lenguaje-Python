# Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de
# caracteres debe retornar el que tiene un valor de componente más baja.
# En el bloque principal iniciamos por asignación la lista de string:

#    palabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
#    print("Palabra con mas caracteres:", mascaracteres(palabras))



def numerocaracteres(palabras):
  numeroletras=0
  palabralista=""
  posicionlista=0
  numeroletrasiguales = 0
  palabralistaiguales = ""
  posicionlistaiguales = 0

  for x in range(len(palabras)):
    if len(palabras[x])>numeroletras:
      numeroletras = len(palabras[x])
      palabralista=palabras[x]
      posicionlista=x

    if len(palabras[x]) == numeroletras:
      numeroletrasiguales = len(palabras[x])
      palabralistaiguales = palabras[x]
      posicionlistaiguales = x
      if palabralista>palabralistaiguales:
        palabralista=palabralistaiguales

  return print(f"La palabra mas larga es {palabralista} con una cantidad de caracteres de {numeroletras}")

# Bloque principal:

cadena=["enero", "febrero", "marzo", "abril", "mayo", "junio"]

numerocaracteres(cadena)