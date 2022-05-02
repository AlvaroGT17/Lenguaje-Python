# Realizar la carga del precio de un producto y la cantidad a llevar. 
# Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)

precio=int(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese cuantos productos lleva el cliente: "))

dinero_abonar=precio*cantidad

print("El cliente debe abonar ", dinero_abonar, " €")