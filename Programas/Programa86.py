# En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
# b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición,
#    colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
# c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.


alumno=[]
notas=[]
calificacion=""
muybueno=0

for x in range(4):
  alumno.append(input("Ingrese el nombre del alumno: "))
  notas.append(int(input("Ingrese la nota del alumno: ")))

for x in range(4):
  if notas[x]>=8:
    calificacion="Muy bueno"
    muybueno=muybueno+1
  elif notas[x]>4 and notas[x]<7:
    calificacion="Bueno"
  elif notas[x]<4:
    calificacion="Insuficiente"

  print("El alumno ", alumno[x], "Tiene unas notas de: ", notas[x], " le corresponde una calificación: ", calificacion)
print("El número de alumnos con una calificación de muy bueno son: ", muybueno)