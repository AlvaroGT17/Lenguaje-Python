# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
# " ", en cambio una cadena vacía es ""

oracion=input("Ingresa una oración: ")
x=0
espacios=0
while x<len(oracion):
  if oracion[x]==" ":
    espacios=espacios+1
  x=x+1

print("La oración cuenta con ", espacios, "espacios.")
