# Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores.
# Debe tener tres parámetros por defecto.

def suma(v1,v2,v3=0,v4=0,v5=0):
  resultado=v1+v2+v3+v4+v5
  return resultado

# Cuerpo principal del programa
print("Suma 3 + 3 es igual a: ", suma(3,3))
print("Suma 3 + 3 + 9 es igual a: ", suma(3,3,9))
print("Suma 3 + 3 + 9 + 14 es igual a: ", suma(3,3,9,14))
print("Suma 3 + 3 + 9 + 14 +23 es igual a: ", suma(3,3,9,14,23))