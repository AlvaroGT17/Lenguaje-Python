# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos
# que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa
# deberá informar el importe que gasta la empresa en sueldos al personal.

x=1
contador=int(input("Cuantos trabajadores tiene la empresa? "))
sueldo=0
totalSalario=0
bienpagados=0
malpagados=0

while x<=contador:
  sueldo=float(input("Ingrese el salario del trabajador "))
  totalSalario=totalSalario+sueldo
  if sueldo < 300:
    malpagados=malpagados+1
  else:
    bienpagados=bienpagados+1
  x=x+1

print("El número de trabajadores con buenos sueldos es de: ", bienpagados)
print("El número de trabajadores con malos sueldos es de: ", malpagados)
print("La empresa esta gastando en sueldos: ", totalSalario," €")