# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo
# multiplica por el tercero.

numero1=int(input("Deme el primer número: "))
numero2=int(input("Deme el segundo número: "))
numero3=int(input("Deme el tercer número: "))

if numero1==numero2 and numero1==numero3:
  print((numero1+numero2)*numero3)