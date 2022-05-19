# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos
# los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)

nombre=[]
edad=[]

for x in range(5):
  nombre.append(input("Ingrese el nombre de la persona a registrar: "))
  edad.append(int(input("Ahora ingrese su edad: ")))

for x in range(5):
  if edad[x]>=18:
    print(nombre[x])

print(nombre)
print(edad)