# Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.

x=0
superior=0

lista=[102,99,88,509,234,675,897,0]

while x<len(lista):
  if lista[x]>=100:
    superior=superior+1
  x=x+1

print("En la lista de números hay ", superior, " números superiores a 100.")