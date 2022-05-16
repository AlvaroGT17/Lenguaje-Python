# Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre.

nombre=input("Ingrese un nombre minúsculas: ")

if nombre[0] == "a" or nombre[0] == "e" or nombre[0] == "i" or nombre[0] == "o" or nombre[0] == "u":
  print("El nombre introducido empieza por vocal")
else:
  print("El nombre introducido empieza por consonante")