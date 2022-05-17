# Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda
# la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.

oracion=input("Escribe una oración.")
oracionminusculas=oracion.lower()
x=0
vocales=0

print("La oracion pasada todo a minusculas es: ")
print(oracionminusculas)

while x<len(oracionminusculas):
  if oracionminusculas[x]=="a" or oracionminusculas[x]=="e" or oracionminusculas[x]=="i" or oracionminusculas[x]=="o" or oracionminusculas[x]=="u":
    vocales=vocales+1
  x=x+1

print(" La oración consta de ", vocales, "vocales.")
