# Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros, retornar la suma de dichos parámetros.


def funcion_suma(v1,v2,*array):
  suma=v1+v2
  for x in range(len(array)):
    suma=suma+array[x]
  return suma

# Bloque principal del programa:

print(funcion_suma(1,2))
print(funcion_suma(1,2,3,4))
print(funcion_suma(1,2,3,4,5,6))