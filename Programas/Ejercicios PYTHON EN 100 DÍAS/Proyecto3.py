# Este proyecto corresponde al dia número 3 en el haremos una calculadora con las funciones básicas.

print('Bienvenido a la calculadora de "Programación Fácil"\n')

print("¿Que operación desea realizar? \n")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicación")
print("4.- División")
print("5.- Potencia de un número\n")

selection = int(input("Marque el número de la operación deseada: \n"))

match selection:
    case 1:
        print("Ha seleccionado la Suma.")
        number1 = float(input("Ingrese el primer sumando: "))
        number2 = float(input("Ingrese el segundo sumando: "))
        result = number1+number2
        print("¿Como prefiere el resultado?")
        print("1.- Exacto")
        print("2.- Redondeado")
        selection=int(input(""))
        if selection == 1:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado de la operación es: ({result})")
        elif selection== 2:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado redondeado es: {round(result,2)}")

    case 2:
        print("Ha seleccionado la resta.")
        number1 = float(input("Ingrese el minuendo: "))
        number2 = float(input("Ingrese el sustraendo: "))
        result = number1-number2
        print("¿Como prefiere el resultado?")
        print("1.- Exacto")
        print("2.- Redondeado")
        selection = int(input(""))
        if selection == 1:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado de la operación es: ({result})")
        elif selection == 2:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado redondeado es: {round(result,2)}")
    case 3:
        print("Ha seleccionado la multiplicación")
        number1 = float(input("Ingrese el multiplicando: "))
        number2 = float(input("Ingrese el multiplicador: "))
        result = number1*number2
        print("¿Como prefiere el resultado?")
        print("1.- Exacto")
        print("2.- Redondeado")
        selection = int(input(""))
        if selection == 1:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado de la operación es: ({result})")
        elif selection == 2:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado redondeado es: {round(result,2)}")
    case 4:
        print("Ha seleccionado la división")
        number1 = float(input("Ingrese el dividendo: "))
        number2 = float(input("Ingrese el divisor: "))
        result = number1/number2
        result2 = number1 % number2
        print("¿Como prefiere el resultado?")
        print("1.- Exacto")
        print("2.- Redondeado")
        selection = int(input(""))
        if selection == 1:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado de la operación es: ({result})")
        elif selection == 2:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado redondeado es: {round(result,2)}")
    case 5:
        print("Ha seleccionado la potencia de un número")
        number1 = float(input("Ingrese la base de la potencia: "))
        number2 = float(input("Ingrese el exponente de la potencia: "))
        result = number1**number2
        print("¿Como prefiere el resultado?")
        print("1.- Exacto")
        print("2.- Redondeado")
        selection = int(input(""))
        if selection == 1:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado de la operación es: ({result})")
        elif selection == 2:
            print(f"Los valores seleccionados son {number1} y {number2} y el resultado redondeado es: {round(result,2)}")
    case _:
        print("La opción introducida es errónea, reinicie el programa")
