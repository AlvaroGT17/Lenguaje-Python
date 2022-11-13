# Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

def mayor(num1, num2):
  if num1>num2:
    numeromayor=num1
  else:
    numeromayor=num2
  return numeromayor

# Cuerpo del programa:

numero1=int(input("Ingrese el primer numero para compararlo: "))
numero2=int(input("Ingrese el segundo numero para comparar: "))
resultado=mayor(numero1, numero2)
print("El numero mayor de los ingresados es: ", resultado)