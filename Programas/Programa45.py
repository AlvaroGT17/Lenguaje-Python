# Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5.
# Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.

multipo3=0
multipo5=0

for x in range(11):
  numero=int(input("Ingrese un numero cualquiera: "))
  if numero%3==0 and numero%5==0:
    print("Este número es múltiplo de 3 y de 5")
    multipo3=multipo3+1
    multipo5=multipo5+1
  elif numero%3==0:
    print("Este número es múltiplo de 3")
    multipo3=multipo3+1
  elif numero%5==0:
    print("Este número es múltiplo de 5")
    multipo5=multipo5+1

print("De los números ingresados son múltiplos de 3: ",multipo3)
print("De los números ingresados son múltiplos de 5: ",multipo5)