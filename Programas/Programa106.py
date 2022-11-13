# Definir una lista y almacenar los nombres de 3 empleados.
# otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
# Imprimir los nombres de empleados y los días que faltó.
# Mostrar los empleados con la cantidad de inasistencias.
# Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.

empleados=[]
diasempleado=[]
diasfaltantes=[]
mayorinasistencia=[]
cantidad=0

nombre1=input("Ingrese el nombre del primer empleado: ")
nombre2=input("Ingrese el nombre del segundo empleado: ")
nombre3=input("Ingrese el nombre del tercer empleado: ")
empleados=[nombre1,nombre2,nombre3]
print(empleados)

for x in range(3):
  cantidad=int(input(f"Ingrese el número de días que falto el trabajador {empleados[x]}: "))
  mayorinasistencia.append(cantidad)
  if cantidad>0:
    diasempleado.append([0])
    diasempleado=[]
  for y in range(cantidad):
    diasempleado.append(int(input("Ingrese el número de día del mes que falto el trabajador:")))
  diasfaltantes.append(diasempleado)
  diasempleado=[]
  print(diasfaltantes)

for k in range(3):
  for x in range(len(diasfaltantes[k])):
    print(f"El empleado {empleados[k]} falto {diasfaltantes[k][x]}")


print(f"El empleado {empleados[0]} falto {mayorinasistencia[0]} dias.")
print(f"El empleado {empleados[1]} falto {mayorinasistencia[1]} dias.")
print(f"El empleado {empleados[2]} falto {mayorinasistencia[2]} dias.")

#print(mayorinasistencia)

if mayorinasistencia[0] > mayorinasistencia[1] and mayorinasistencia[0] > mayorinasistencia[2]:
    print("El empleado que mas a faltado es: ", empleados[0])
elif mayorinasistencia[0] < mayorinasistencia[1] and mayorinasistencia[1] > mayorinasistencia[2]:
    print("El empleado que mas a faltado es: ", empleados[1])
elif mayorinasistencia[0] < mayorinasistencia[2] and mayorinasistencia[1] > mayorinasistencia[2]:
    print("El empleado que mas a faltado es: ", empleados[1])

print("")

if mayorinasistencia[0] < mayorinasistencia[1] and mayorinasistencia[0] < mayorinasistencia[2]:
    print("El empleado que menos a faltado es: ", empleados[0])
elif mayorinasistencia[0] > mayorinasistencia[1] and mayorinasistencia[1] < mayorinasistencia[2]:
    print("El empleado que menos a faltado es: ", empleados[1])
elif mayorinasistencia[0] > mayorinasistencia[2] and mayorinasistencia[1] < mayorinasistencia[2]:
    print("El empleado que menos a faltado es: ", empleados[1])

for k in range(3):
  for x in range(len(diasfaltantes[k])):
    if len(diasfaltantes[k]) < 1:
      print(f"El empleado {empleados[k]} falto menos de un dia")
