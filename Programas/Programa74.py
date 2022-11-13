# Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.

nombres=["Jesus", "Aaron", "Alvaro", "Raul", "Juan"]
x=0
contador=0

while x<len(nombres[x]):
  if len(nombres[x])>=5:
    contador=contador+1
  x=x+1

print("Hay ", contador, "nombres con 5 o más letras")
