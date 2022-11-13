# Realizar un programa que lea los lados de n triángulos, e informar:
#  a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#  b) Cantidad de triángulos de cada tipo.

lado1=0
lado2=0
lado3=0
equilatero=0
isosceles=0
escaleno=0

numero=int(input("Ingrese el número de triángulos a analizar: "))

for x in range(numero):
  lado1=float(input("Ingrese el tamaño del 1º lado: "))
  lado2=float(input("Ingrese el tamaño del 2º lado: "))
  lado3=float(input("Ingrese el tamaño del 3º lado: "))
  if lado1==lado2 and lado2==lado3:
    print("Este triangulo es equilátero")
    equilatero=equilatero+1
  elif lado1==lado2 and lado1!=lado3:
    print("Este triangulo es isosceles")
    isosceles=isosceles+1
  elif lado1==lado3 and lado1!=lado2:
    print("Este triangulo es isosceles")
    isosceles=isosceles+1
  elif lado2==lado3 and lado2!=lado1:
    print("Este triangulo es isosceles")
    isosceles=isosceles+1
  elif lado1!=lado2 and lado2!=lado3:
    print("Este triangulo es escaleno")
    escaleno=escaleno+1

print("El número de triángulos equiláteros es de: ",equilatero)
print("El número de triángulos isosceles es de: ",isosceles)
print("El número de triángulos escaleno es de: ",escaleno)