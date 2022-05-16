'''Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con mayor altura.'''


nombre1=input("Ingrese el nombre del sujeto 1: ")
edad1=int(input("Ingrese la edad del sujeto 1: "))
altura1=float(input("Ingrese la altura del sujeto 1: "))

nombre2=input("Ingrese el nombre del sujeto 2: ")
edad2=int(input("Ingrese la edad del sujeto 2: "))
altura2=float(input("Ingrese la altura del sujeto 2: "))

if altura1>altura2:
  print("El sujeto más alto es: ", nombre1)
else:
  print("El sujeto mas alto es: ", nombre2)

