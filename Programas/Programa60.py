# Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la
# cadena 'si' o 'no' por teclado. Mostrar la suma de los valores ingresados.


'''contestacion="si"
numero=0
suma=0

if contestacion == "Si" or "si" or "s" or "S":
    numero=int(input("Ingrese un número: "))
    suma=suma+numero
    contestacion=input("¿Quiere ingresar mas números? ")
else:
  print("El resultado de la suma de los números ingresados es: ", suma)'''

# Despues de muchas vueltas la solución es la siguiente:

opcion = "si"
suma = 0

while opcion == "si":
    valor = int(input("Ingrese un valor:"))
    suma = suma+valor
    opcion = input("Desea cargar otro numero (si/no):")

print("La suma de valores ingresados es", suma)