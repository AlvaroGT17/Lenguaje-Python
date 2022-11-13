# Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año
# (enero, febrero o marzo) Cargar por teclado el valor numérico del día, mes y año.

dia=int(input("Introduzca el día de la fecha: "))
mes=int(input("Introduzca el mes de la fecha: "))
año=int(input("Introduzca el año de la fecha: "))

if mes<=1 or mes<=3:
  print("Esta fecha esta dentro del primer trimestre.")
