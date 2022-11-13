# Proyecto correspondiente al día 2 del curso en el crearemos una calculadora.

print("- Calculadora de exponentes -")
valor_1 = input("Introduzca el primer valor: \n")
valor_2 = input("Introduzca el segundo valor: \n")

resultado = float(valor_1) ** float(valor_2)

print(f"El resultado de {valor_1} elevado a {valor_2} es igual a {round(resultado,2)}")
