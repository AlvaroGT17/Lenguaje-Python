# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los
# datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años) Imprimir la edad promedio de las personas.


def personaedad():
  persona=[]
  edad=[]
  for x in range(5):
    persona.append(input(f"Ingrese el nombre de la {x+1}º persona: "))
    edad.append(int(input(f"Ingrese la edad de la {x+1}º persona: ")))
  print("Las listas quedaran de la siguiente manera")
  return [persona,edad]

def seleccionador(persona, edad):
  print("Las personas de la lista mayores de edad son:")
  for x in range(len(persona)):
    if edad[x]>=18:
      print(f"{persona[x]}, con una edad de {edad[x]}.")

def promedio(edad):
  suma=0
  for x in range(len(edad)):
    suma=suma+edad[x]
  promedio=suma//(len(edad))
  return print("El promedio de las edades ingresadas es: ", promedio)

# Bloque principal:

persona, edad=personaedad()
seleccionador(persona,edad)
promedio(edad)