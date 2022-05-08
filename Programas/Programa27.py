# Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se
# calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)

numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
numero3=int(input("Ingrese el tercer número: "))

if numero1>numero2 and numero2>numero3:
  mayor=numero1
elif numero2>numero1 and numero2>numero3:
  mayor=numero2
else:
  mayor=numero3

if numero1<numero2 and numero2<numero3:
  menor=numero1
elif numero2<numero2 and numero2<numero3:
  menor=numero2
else:
  menor=numero3

if mayor==numero1 and menor==numero3:
  medio=numero2
elif mayor==numero1 and menor==numero2:
  medio=numero3
elif mayor==numero2 and menor==numero3:
  medio=numero1
elif mayor==numero2 and menor==numero1:
  medio=numero3
elif mayor==numero3 and menor==numero2:
  medio=numero1
else:
  medio=numero2

diferenciaMayorMedio=mayor-medio
diferenciaMedioMenor=medio-menor

print("El numero mayor es: ", mayor)
print("El numero menor es: ", medio)
print("El numero medio es: ", menor)
print("La diferencia entre el número mayor ", mayor, "y el número medio", medio, " es: ", diferenciaMayorMedio)
print("La diferencia entre el número medio ", medio, "y el número menor", menor, " es: ", diferenciaMedioMenor)