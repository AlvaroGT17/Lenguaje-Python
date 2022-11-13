'''Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al ingresar el valor -1.
Dejar como comentario dentro del código fuente el enunciado del problema. '''

numero=0
suma=0

while numero!=-1:
  numero=int(input("Ingrese un numero: "))
  suma=suma+numero

print("La suma obtenido de los números ingresados es: ", suma)