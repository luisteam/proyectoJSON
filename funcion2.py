import json

from pprint import pprint

with open('300107-0-agenda-actividades-eventos.json') as data_file:    
 data = json.load(data_file)


 #pprint(data["@graph"]["excluded-days"])


niños=[]
mayores=[]

listemp=[]




for i in range(len(data["@graph"])):
	titulo=(data["@graph"][i]["title"])
	listemp.append(titulo)
	audiencia=(data["@graph"][i]["excluded-days"])
	pprint(audiencia)

























#	if audiencia == "Niños":
#		listado.append(niños)
#		listemp=[]
#	if audiencia == "Mayores":
#		listado.append(mayores)
#		listemp=[]
#	
#
#
#
#print(len(niños),len(mayores))