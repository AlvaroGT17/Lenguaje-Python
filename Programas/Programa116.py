# Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma.
# Mostrar finalmente un mensaje de despedida del programa.

def mensaje(mensaje):
  print("***********************************************")
  print(mensaje)
  print("***********************************************")

def suma():
  valor1=(int(input("Ingrese el primer valor: ")))
  valor2=(int(input("Ingrese el segundo valor: ")))
  suma= valor1+valor2
  print("El resultado de la suma de los dos valores es: ",suma)

mensaje("Bienvenido al programa de SUMA")
suma()
mensaje("Gracias por usar este programa")