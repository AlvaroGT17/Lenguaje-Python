# Confeccionar un programa con las siguientes funciones:
#   1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
#   2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados y muestre el nombre del empleado con sueldo mayor.
# En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar a la función que muestra el nombre de empleado
# con sueldo mayor.

# bloque principal

# empleado1=cargar_empleado()
# empleado2=cargar_empleado()
# mayor_sueldo(empleado1,empleado2)


def cargar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    sueldo = input("Ingrese el sueldo del empleado: ")
    return (nombre, sueldo)


def mayor_sueldo(empleado1, empleado2):
    if empleado1[1] > empleado2[1]:
        return print("El empleado", empleado1[0], "tiene el mayor sueldo con un importe de: ", empleado1[1])
    else:
        return print("El empleado", empleado2[0], "tiene el mayor sueldo con un importe de: ", empleado2[1])

# bloque principal


empleado1 = cargar_empleado()
empleado2 = cargar_empleado()
mayor_sueldo(empleado1, empleado2)

