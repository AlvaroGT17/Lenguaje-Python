# Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
# Si el promedio es >=7 mostrar "Promocionado".
# Si el promedio es >=4 y <7 mostrar "Regular".
# Si el promedio es <4 mostrar "Reprobado".

nota1=int(input("Ingrese la primera nota del alumno: "))
nota2=int(input("Ingrese la segunda nota del alumno: "))
nota3=int(input("Ingrese la tercera nota del alumno: "))
promedio=(nota1+nota2+nota3)/3
print(promedio)

if promedio >= 7:
  print("Promocionado")
elif promedio >=4 and promedio<7:
  print("Regular")
else:
  print("Suspenso")

# En python los operadores lógicos como & no se representan con dicho simbolo sino que se escriben tal cual es decir en este ejercicio
# la sentencia del elif daba error por que al añadir el operador lógico "and" lo añadía como simbolo y no como la palabra escrita.