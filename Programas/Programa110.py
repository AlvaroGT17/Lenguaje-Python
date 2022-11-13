# Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
# Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
# Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

empleados=[]
sueldos=[]
posicion=0

numeroempleados=int(input("Ingrese el número de empleados que tendrá la lista: "))

for x in range(numeroempleados):
  empleados.append(input(f"Ingrese el nombre del {x+1}º empleado: "))
  sueldos.append(int(input(f"Ingrese el sueldo del empleado {empleados[x]}: ")))

print(empleados)
print(sueldos)

while posicion<len(empleados):
  if sueldos[posicion]>10000:
    empleados.pop(posicion)
    sueldos.pop(posicion)
  else:
    posicion=posicion+1

print("La lista de nombres modificada queda así", empleados)
print("La lista de sueldos modificada queda así", sueldos)
