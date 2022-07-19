# Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18
# (como mínimo se envía un entero a la función)

def edades(edad1, *lista):
  contador=0
  if edad1>=18:
    contador=contador+1
  for x in range (len(lista)):
    if lista[x]>=18:
      contador=contador+1
  return contador

# Cuerpo principal del programa:

contador=edades(34,2,54,23,12,11,43,54,6,22,1,18)
print("El números de mayores de edad es: ",contador)
