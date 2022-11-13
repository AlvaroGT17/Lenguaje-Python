# Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus últimos tres sueldos
# (estos tres valores en una tupla)
# El programa debe tener las siguientes funciones:
#   1)Carga de los nombres de empleados y sus últimos tres sueldos.
#   2)Imprimir el monto total cobrado por cada empleado.
#   3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
# Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:

# Ejemplo: empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]

def ingreso_empleados():
  empleados_sueldos=[]

  for x in range(5):
    empleado=input(f"Ingrese el nombre del empleado Nº{x+1}: ")
    sueldo1=int(input("Ingrese el sueldo del 1º mes: "))
    sueldo2=int(input("Ingrese el sueldo del 2º mes: "))
    sueldo3=int(input("Ingrese el sueldo del 3º mes: "))
    empleados_sueldos.append([empleado,(sueldo1,sueldo2,sueldo3)])

  print(empleados_sueldos)
  return empleados_sueldos

def total_sueldos(empleados_sueldos):
  ganancias_totales=[]
  for x in range(len(empleados_sueldos)):
    total = empleados_sueldos[x][1][0] + empleados_sueldos[x][1][1] + empleados_sueldos[x][1][2]
    print("El empleado ", empleados_sueldos[x][0],"cobro un total de: ",total)
    ganancias_totales.append((empleados_sueldos[x][0],total))
  print(ganancias_totales)
  return ganancias_totales

def sueldos_mayores(ganancias_totales):
  for x in range(len(ganancias_totales)):
    if ganancias_totales[x][1]>10000:
      print("El trabajador", ganancias_totales[x][0], "tiene unas ganancias por encima de 10000 €")
    else:
      print("El trabajador", ganancias_totales[x][0], "no llega a la media.")


# Cuerpo principal del programa.

empleados_sueldos=ingreso_empleados()
ganancias_totales=total_sueldos(empleados_sueldos)
sueldos_mayores(ganancias_totales)