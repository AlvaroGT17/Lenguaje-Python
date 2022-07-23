# Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. Modificar la lista y luego convertir la lista en tupla.

pruevatupla=(1, 3, 5)
print(pruevatupla)
lista=list(pruevatupla)
print(lista)
lista.append(45)
print(lista)
conversiontupla=tuple(lista)
print(conversiontupla)