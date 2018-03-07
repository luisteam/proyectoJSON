import json

from pprint import pprint

with open('300107-0-agenda-actividades-eventos.json') as data_file:    
 data = json.load(data_file)


listado=[]
listemp=[]




for i in range(len(data["@graph"])):
	titulo=(data["@graph"][i]["title"])
	listemp.append(titulo)
	precio=(data["@graph"][i]["price"])
	if precio == 1:
		listemp.append('Gratuito')
	else:
		listemp.append('Pago')

	listado.append(listemp)
	listemp=[]


print(listado)