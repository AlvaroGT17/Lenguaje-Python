# Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre.

nombre=input("Ingrese un nombre minúsculas: ")

if nombre[0]=="a" or "e" or "i" or "o" or "u":
  print("El nombre introducido empieza por vocal")
else:
  print("El nombre introducido empieza por consonante")