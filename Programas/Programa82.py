# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético.

nombre=[]

for x in range(5):
  nombre.append(input("Ingrese un nombre: "))

menor=nombre[0]
for x in range(1,5):
  if nombre[x]<menor:
    menor=nombre[x]

print("El nombre menor alfabeticamente es: ", menor)