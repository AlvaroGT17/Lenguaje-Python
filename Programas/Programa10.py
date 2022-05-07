# Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.

numero1=int(input("Ingrese un número al azar: "))
numero2=int(input("Ingrese un segundo número al azar"))

if numero1>numero2:
  print("El número ", numero1, " es mayor que ", numero2)
else:
  print("El número ", numero2, " es mayor que ", numero1)

# Otra forma de hacer este ejercicio es de la siguiente manera: 

# num1=int(input("Ingrese primer valor:"))
# num2=int(input("ingrese segundo valor:"))
# print("El valor mayor es")
# if num1>num2:
#    print(num1)
# else:
#    print(num2)

# De esta manera queda mas claro ya que solo imprimes un solo mensaje y lo único que hará el programa es comparar los números.