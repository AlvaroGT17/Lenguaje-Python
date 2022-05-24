# Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

'''sueldo=[]


for x in range(5):
  sueldo.append(int(input("Ingresa el sueldo del operario: ")))

print(sueldo)

x=0

for h in range(4):
  for x in range(4):
    if sueldo[x]>=sueldo[x+1]:
      aux=sueldo[x]
      sueldo[x]=sueldo[x+1]
      sueldo[x+1]=aux

print(sueldo)'''

# Aunque una forma mucho más eficiente de proceder es haciendo que el for interno realice menos comprobaciones
# a medida que avanza el for externo.

sueldo=[]


for x in range(5):
  sueldo.append(int(input("Ingresa el sueldo del operario: ")))

print(sueldo)

x=0

for h in range(4):
  for x in range(4-h):
    if sueldo[x]>=sueldo[x+1]:
      aux=sueldo[x]
      sueldo[x]=sueldo[x+1]
      sueldo[x+1]=aux

print(sueldo)