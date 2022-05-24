# Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de dichos empleados.
# Imprimir la lista de sueldos ordenamos de menor a mayor.

sueldo=[]

cantidad=int(input("Ingrese el número de trabajadores que operan en la empresa: "))

for x in range(cantidad):
  sueldo.append(float(input("Ingrese el salario del trabajador: ")))

print(sueldo)

for y in range(cantidad-1):
  for x in range(cantidad-1-y):
    if sueldo[x]>sueldo[x+1]:
      aux=sueldo[x]
      sueldo[x]=sueldo[x+1]
      sueldo[x+1]=aux

print(sueldo)