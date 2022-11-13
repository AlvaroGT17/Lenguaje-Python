# En una empresa se almacenaron los sueldos de 10 personas.
# Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
#   1) Carga de los sueldos en una lista.
#   2) Impresión de todos los sueldos.
#   3) Cuántos tienen un sueldo superior a $4000.
#   4) Retornar el promedio de los sueldos.
#   5) Mostrar todos los sueldos que están por debajo del promedio.

def sueldos():
  honorarios=[]
  for x in range(10):
    honorarios.append(int(input(f"Ingrese el sueldo del {x+1}º operario: ")))
  print("Los sueldos ingresados quedan de la siguiente manera: ", honorarios)
  return honorarios

def sueldocribado(honorarios):
  contador=0
  for x in range(len(honorarios)):
    if honorarios[x]>4000:
      contador= contador+1
  return print(f"El número de operarios que superan los 4000€ son: {contador}")

def promedio(honorarios):
  suma=0
  promedio=0
  for x in range(len(honorarios)):
    suma= suma+honorarios[x]
  promedio = suma/(len(honorarios))
  print(f"El promedio de todos los sueldos es de: {promedio}")
  return promedio

def sueldosinferiores(honorarios):
  for x in range(len(honorarios)):
    if honorarios[x] < 4000:
      print(f"El {x+1}º sueldo es inferior a '4000' con un valor de: {honorarios[x]}")

# Bloque principal:

honorarios=sueldos()
sueldocribado(honorarios)
valorPromedio=promedio(honorarios)
sueldosinferiores(honorarios)