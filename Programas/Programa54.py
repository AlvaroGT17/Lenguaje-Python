# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
#   a) Obtener el promedio de las edades de cada turno(tres promedios)
#   b) Imprimir dichos promedios(promedio de cada turno)
#   c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

from cgi import print_arguments


edad=0
sumamañana=0
sumatarde=0
sumanoche=0
promediomañana=0
promediotarde=0
promedionoche=0

for x in range(5):
  edad=int(input("Ingrese la edad del alumno: "))
  sumamañana=sumamañana+edad
  promediomañana=sumamañana/5

print(promediomañana)

for y in range(6):
  edad = int(input("Ingrese la edad del alumno: "))
  sumatarde=sumatarde+edad
  promediotarde=sumatarde/6

print(promediotarde)

for z in range(11):
  edad = int(input("Ingrese la edad del alumno: "))
  sumanoche=sumanoche+edad
  promedionoche=sumanoche/11

print(promedionoche)

if promediomañana>promediotarde and promedionoche<=promediotarde:
  print("El promedio del turno de mañana es el mayor.")
elif promediomañana<promediotarde and promedionoche<promediotarde:
  print("El promedio del turno de tarde es el mayor.")
else:
  print("El promedio del turno de noche es el mayor.")