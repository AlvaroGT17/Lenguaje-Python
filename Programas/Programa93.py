# Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas de mayor a menor.
# Imprimir las notas y los nombres de los alumnos.


alumnos=[]
notas=[]

for x in range(5):
  alumnos.append(input(f"Ingrese el nombre del {x+1}º alumno: "))
  notas.append(float(input(f"Ingrese la nota del {x+1}º alumno: ")))

print(alumnos)
print(notas)

for y in range(4):
  for x in range(4-y):
    if notas[x]>notas[x+1]:
      auxnotas=notas[x]
      auxnombre=alumnos[x]
      notas[x]=notas[x+1]
      alumnos[x]=alumnos[x+1]
      notas[x+1]=auxnotas
      alumnos[x+1]=auxnombre

for x in range(5):
  print("El alumno ", alumnos[x],"tiene una nota de ", notas[x])