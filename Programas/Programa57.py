'''Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma. Definir varias líneas de comentarios
indicando el nombre del programa, el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios. '''

numero=0
suma=0

for x in range(10):
  numero=int(input("Ingrese un número: "))
  suma=suma+numero

print("La suma de los números es: ", suma)

'''Titulo: Suma'''
# Autor: Alvaro
# Fecha de ultima modificación: 16-05-2022
