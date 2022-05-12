# Una planta que fabrica perfiles de hierro posee un lote de n piezas. Confeccionar un programa que pida ingresar por teclado
# la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida
# en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

x=1
barrasutiles=0

contador=int(input("Dígame el número de barras que trae el lote: "))

while x<=contador:
  largo=float(input("Ingrese la longitud del perfil: "))
  if largo >= 1.20 and largo <= 1.30:
    print("La barra es apta")
    barrasutiles=(barrasutiles+1)
    print("Las barras acumuladas son: ",barrasutiles)
  x=x+1

  print("El número de barras útiles en el pack es de ", barrasutiles, "Und.")