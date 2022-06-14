# Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor.
# En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def ordenador(num1,num2,num3):
  for x in range(3):
    numaux=0
    if num1>num2:
      numaux=num1
      num1=num2
      num2=numaux
      if num2 > num3:
        numaux=num3
        num3=num2
        num2=numaux
    if num3 < num2:
      numaux = num3
      num3 = num2
      num2 = numaux
      if num2 < num1:
        numaux = num2
        num2 = num1
        num1 = numaux

  print("La lista de números ingresada después de ordenarla quedaría: ", num1, num2, num3)

def ingreso():
  numero1 = (int(input("Ingrese el primer número: ")))
  numero2 = (int(input("Ingrese el segundo número: ")))
  numero3 = (int(input("Ingrese el tercer número: ")))
  ordenador(numero1,numero2,numero3)

ingreso()
