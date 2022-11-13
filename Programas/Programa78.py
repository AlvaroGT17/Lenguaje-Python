# Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de las mismas.
# Contar cuántas personas son más altas que el promedio y cuántas más bajas.

personas=[]
sumaalturas=0
superiorpromedio=0
inferiorpromedio=0

for x in range(5):
  altura=float(input("Ingrese la altura "))
  personas.append(altura)
  sumaalturas=sumaalturas+altura

promedio=sumaalturas/5

print(personas)
print(promedio)

x=0

for x in range(5):
  if personas[x]>promedio:
    superiorpromedio=superiorpromedio+1
  else:
    if personas[x]<promedio:
      inferiorpromedio=inferiorpromedio+1

print("El numero de personas por encima del promedio es: ", superiorpromedio)
print("El numero de personas por debajo del promedio es: ", inferiorpromedio)
