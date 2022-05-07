# Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos.

#sueldo=int(input("Ingrese el sueldo del operario: "))
#if sueldo > 3000:
#  input("Hacienda a este lo cruje")
#else:
#  input("Este sera pobre toda su vida")


# aquí el fallo se encuentra en que en la salida por pantalla he usado input y es print el comando que hay que utilizar; a sinple vista parece
# que hacen lo mimo pero en realidad lo que hace input es mostrar un mensaje por pantalla y esperar que introduzcamos un valor por teclado, para
# guardarlo en una variable, mientras que print lo que hace es mostrar un mensaje por pantalla y esperar una pulsación de teclado para continuar.
# por lo que el ejercicio deberia quedar así.

sueldo=int(input("Ingrese el sueldo del operario: "))
if sueldo > 3000:
  print("Hacienda a este lo cruje")
else:
  print("Este sera pobre toda su vida")