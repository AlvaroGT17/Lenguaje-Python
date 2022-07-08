# Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. Definir un segundo parámetro llamado termino
# que por defecto almacene el valor 10. Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
# Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.

def tablamultiplicar(numero,cantidad=11):
  for x in range(cantidad):
    if (x+1)==cantidad:
      print(x*numero)
    else:
      print(x*numero,",",sep=" ", end="")
  print("")


# Bloque principal del programa

print("La tabla del 5")
tablamultiplicar(5)
print("La tabla del 7 con 6 resultados")
tablamultiplicar(7,6)
print("La tabla del 2 con 4 resultados")
tablamultiplicar(cantidad=4,numero=2)