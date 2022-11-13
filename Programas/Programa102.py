'''Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:

a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado'''

nombre=[]
sueldo=[]
sumasueldos=[]
mes1=0
mes2=0
mes3=0
mayor=0

for x in range(3):
  nombre.append(input("Ingrese el nombre del empleado. "))
  mes1=(float(input("Ingrese el sueldo del 1º mes: ")))
  mes2=(float(input("Ingrese el sueldo del 2º mes: ")))
  mes3=(float(input("Ingrese el sueldo del 3º mes: ")))
  sueldo.append([mes1,mes2,mes3])
  sumameses=mes1+mes2+mes3
  sumasueldos.append([sumameses])

print(nombre)
print(sueldo)
print(sumasueldos)

if sumasueldos[0]>sumasueldos[1] and sumasueldos[0]>sumasueldos[2]:
  mayor=nombre[0]
elif sumasueldos[1]>sumasueldos[0] and sumasueldos[1]>sumasueldos[2]:
  mayor=nombre[1]
elif sumasueldos[2]>sumasueldos[1]and sumasueldos[2]>sumasueldos[0]:
  mayor=nombre[2]

print("El operario que mas a ganado es ",mayor)