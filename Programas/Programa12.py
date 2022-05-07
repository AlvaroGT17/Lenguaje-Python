# Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

nota1=int(input("Introduzca la primera nota del alumno: "))
nota2=int(input("Introduzca la segunda nota del alumno: "))
nota3=int(input("Introduzca la tercera nota del alumno: "))
promedio=nota1+nota2+nota3/3

if promedio >= 7:
  print("El alumno promociona")