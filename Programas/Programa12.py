# Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

nota1=float(input("Introduzca la primera nota del alumno: "))
nota2=float(input("Introduzca la segunda nota del alumno: "))
nota3=float(input("Introduzca la tercera nota del alumno: "))
promedio=(nota1+nota2+nota3)/3

if promedio < 7:
  print("La nota media del alumno es: ", promedio)
  print("A tomar por el culo REPITE CABRóN.")
elif promedio >= 7:
  print("La nota media del alumno es: ", promedio)
  print("El alumno promociona")