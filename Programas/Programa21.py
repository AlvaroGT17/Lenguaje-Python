# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.

dia=int(input("Introduzca el día de la fecha: "))
mes=int(input("Introduzca el mes de la fecha: "))
año=int(input("Introduzca el año de la fecha: "))

if dia>=24 and mes==12 or dia<=6 and mes==1:
  print("La fecha corresponde a navidad")
