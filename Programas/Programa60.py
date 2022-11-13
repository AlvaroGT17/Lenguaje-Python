# Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la
# cadena 'si' o 'no' por teclado. Mostrar la suma de los valores ingresados.

'''contestacion="si"
numero=0
suma=0

if contestacion == "Si" or contestacion=="si" or contestacion=="s" or contestacion=="S":
    numero=int(input("Ingrese un número: "))
    suma=suma+numero
    contestacion=input("¿Quiere ingresar mas números? ")
else:
  print("El resultado de la suma de los números ingresados es: ", suma)'''

# Despues de muchas vueltas la solución es la siguiente:


contestacion = "si"
suma = 0

while contestacion == "Si" or contestacion == "si" or contestacion == "s" or contestacion == "S" or contestacion == "SI" or contestacion == "sI":
    valor = int(input("Ingrese un valor:"))
    suma = suma+valor
    contestacion = input("Desea cargar otro numero (si/no):")

print("La suma de valores ingresados es", suma)

'''Por fin despues de mucho mirar y otro fallo igual en otro ejercicio me di cuenta de que siempre hay que poner la variable y la comparación
no vasta con poner la variable una vez y luego los comparadores, es variable y comparas, variable y comparas y asi siempre.'''