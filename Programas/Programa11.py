# Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y 
# diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

# numero1=int(input("Ingrese un número: "))
# numero2=int(input("ingrese un segundo número: "))
# suma=numero1+numero2
# diferencia=numero1-numero2
# producto=numero1*numero2
# division=numero1/numero2

# if numero1 > numero2:
#   print("El número ", numero1, " es mayor que ", numero2, "por lo que su suma es: ", suma, "y su diferencia es: ", diferencia)
# else:
#   print("El número ", numero2, " es mayor que ", numero1, "por lo que su producto es: ", producto, "y su división es: ", division)


# Otra cosa a tener en cuenta en el ejercicio es que los números fueran iguales para lo que podriamos 
# introducir un "elif" siendo como resultado:

numero1=int(input("Ingrese un número: "))
numero2=int(input("ingrese un segundo número: "))
suma=numero1+numero2
diferencia=numero1-numero2
producto=numero1*numero2
division=numero1/numero2

if numero1 > numero2:
  print("El número ", numero1, " es mayor que ", numero2, "por lo que su suma es: ", suma, "y su diferencia es: ", diferencia)
elif numero1 == numero2:
  print("Los números son iguales.")
else:
  print("El número ", numero2, " es mayor que ", numero1, "por lo que su producto es: ", producto, "y su división es: ", division)
