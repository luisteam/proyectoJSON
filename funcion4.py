#Niños
#Mayores
#Jovenes
#Familias
#Mujeres

import json

from pprint import pprint

with open('300107-0-agenda-actividades-eventos.json') as data_file:
 data = json.load(data_file)

lista=[]

inicio=("Dime un genero en concreto a buscar en la lista: ")
generos=[inicio," "," Niños"," Mayores"," Jovenes"," Familias"," Mujeres"," "]

for i in generos:
	print(i)

busqueda=input("Escribe un genero: ")

for i in range(len(data["@graph"])):
	objeto=(data["@graph"][i])

	if 'audience' in objeto:
		audiencia=(objeto["audience"])
		titulo=(data["@graph"][i]["title"])

		if busqueda.upper() in audiencia.upper():
			lista.append(titulo)

		if busqueda.upper() in audiencia.upper():
			lista.append(titulo)

		if busqueda.upper() in audiencia.upper():
			lista.append(titulo)

		if busqueda.upper() in audiencia.upper():
			lista.append(titulo)

		if busqueda.upper() in audiencia.upper():
			lista.append(titulo)

if len(lista) >= 1:
	print(lista)
	print(" ")
	print("Esta es la lista con el tipo de evento %s, hay %d eventos." % (busqueda,len(lista)))
else:
	print("Esta es la lista con el tipo de evento %s, hay %d eventos." % (busqueda,len(lista)))