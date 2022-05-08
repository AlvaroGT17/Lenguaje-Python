# Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la leyenda
#  "Alguno de los números es menor a diez".

numero1=int(input("Deme el primer número: "))
numero2=int(input("Deme el segundo número: "))
numero3=int(input("Deme el tercer número: "))

if numero1<10 or numero2<10 or numero3<10:
  print("Alguno de los valores es menor a diez")