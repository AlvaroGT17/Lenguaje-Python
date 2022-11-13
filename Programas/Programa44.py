# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

nota=0
mayor=0
menor=0

for x in range(11):
  nota=int(input("Ingrese la nota del alumno: "))
  if nota >=7:
    mayor=mayor+1
  else:
    menor=menor+1

print("Alumnos con buenas notas: ",mayor)
print("Alumnos con notas reguleras: ",menor)

