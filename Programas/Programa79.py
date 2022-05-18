# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
# que permita almacenar los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

turnomañana=[]
turnotarde=[]
suma=0

for x in range(4):
  sueldo=float(input("Ingrese lo que gana este operario de mañana: "))
  turnomañana.append(sueldo)

x=0

for x in range(4):
  sueldo=float(input("Ingrese lo que gana este operario de tarde: "))
  turnotarde.append(sueldo)

print("Los salarios de los trabajadores del turno de mañana son: ", turnomañana)
print("Los salarios de los trabajadores del turno de tarde son: ", turnotarde)