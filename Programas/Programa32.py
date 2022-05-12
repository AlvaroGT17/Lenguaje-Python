# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

x=1
notasbuenas=0
notasregulares=0

while x<=10:
  notas=float(input("Ingrese la nota del alumno: "))
  if notas>=7:
    notasbuenas=notasbuenas+1
  else:
    notasregulares=notasregulares+1
  x=x+1

print("El número de alumnos con notas buenas es de: ", notasbuenas)
print("El número de alumnos con notas regulares es de: ", notasregulares)