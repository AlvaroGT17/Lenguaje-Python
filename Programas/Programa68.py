# Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. Controlar que el string ingresado tenga entre
# 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error.


numero=0

clave=input("Ingresa una clave de entre 10 y 20 caracteres.")
numero=len(clave)

if numero>=10 and numero<=20:
  print("Contraseña aceptada.")
else:
  if numero<10:
    print("ERROR!!! La contraseña solo tiene ", numero, "caracteres.")
  elif numero>20:
    print("ERROR!!! La contraseña tiene mas de 20 caracteres.")

'''Una forma mas directa de hacer este ejercicio es el siguiente

clave=input("Ingrese una clave que tenga entre 10 y 20 caracteres:")
if len(clave)>=10 and len(clave)<=20:
    print("Largo correcto")
else:
    print("Largo incorrecto")
'''
