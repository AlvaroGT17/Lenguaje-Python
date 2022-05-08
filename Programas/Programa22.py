# Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda
# "Todos los números son menores a diez".

numero1=int(input("Deme el primer número: "))
numero2=int(input("Deme el segundo número: "))
numero3=int(input("Deme el tercer número: "))

if numero1<10 and numero2<10 and numero3<10:
  print("Todos los números son mas pequeños de 10")