# Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor.
# La segunda que solicite la carga de dos valores y muestre el producto de los mismos.
# LLamar desde el bloque del programa principal a ambas funciones.

def potencia():
  valor1=int(input("Ingresa un número cualquiera: "))
  cuadrado=valor1**2
  print("El cuadrado del número ingresado es: ",cuadrado)

def multiplicacion():
  valor2=int(input("Ingrese de nuevo otro número: "))
  valor3=int(input("Ingrese de nuevo otro número: "))
  producto=valor2*valor3
  print("El resultado de la multiplicaciónes: ",producto)

potencia()
multiplicacion()
