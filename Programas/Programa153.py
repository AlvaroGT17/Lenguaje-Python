'''Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con componentes de tipo tupla con
el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:
candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]
1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.'''


def ingreso():
  for x in range(3):
    candidato=input("Ingrese el nombre del candidato: ")
    for x in range(2):
      provincia=input("Ingrese el nombre de la provincia: ")
      votos=int(input("Ingrese los votos obtenido en ", provincia, ": "))
  