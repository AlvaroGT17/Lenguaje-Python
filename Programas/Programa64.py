# Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un carácter "@".

correo=input("Ingrese un mail: ")
cantidad=0
x=0

while x<len(correo):
    if correo[x] == "@":
        cantidad = cantidad+1
    x = x+1
if cantidad >= 1:
    print("El correo electrónico es correcto, contiene solo un carácter @.")
else:
    print("El correo electrónico es incorrecto")
