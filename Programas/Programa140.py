# Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo
# y el nombre. Hacer la llamada de la función mediante argumentos nombrados.

def operarios(nombre,preciohora,cantidadhoras):
  sueldo=cantidadhoras*preciohora
  print("El trabajador ",nombre, "trabajó una cantidad de horas ",cantidadhoras, "y percibira por ello un sueldo de: ",sueldo)

# Cuerpo principal del programa

operarios("Juan",3.43,80)
operarios(preciohora=5.45,cantidadhoras=200,nombre="Pepe")