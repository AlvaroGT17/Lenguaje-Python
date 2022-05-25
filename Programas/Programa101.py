# Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela.
# Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.

alumno = []
notas = []
sublista = []
z=-1

for y in range(1, 4):
  alumno.append(input(f"Ingrese el nombre del alumno {y}: "))

print("")

for h in range(1,4):
  z=z+1
  for x in range(2):
    sublista.append(float(input(f"Ingrese la {x+1}º nota del alumno {alumno[z]}: ")))
  notas.append(sublista)
  sublista=[]

print("")
print(alumno)
print(notas)
print("")

for x in range(3):
  print(f"El alumno {alumno[x]}, tiene unas notas de {notas[x]}")

