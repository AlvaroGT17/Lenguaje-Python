# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

x=1
contador=int(input("Ha cuantas personas van a medir? "))
altura=0
sumaaltura=0
promedio=0

while x<=contador:
  altura=float(input("Ingrese la altura: "))
  sumaaltura=sumaaltura+altura
  x=x+1

promedio=sumaaltura/contador

print("El promedio de las alturas es de: ", promedio)
