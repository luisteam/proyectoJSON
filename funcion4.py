#Niños
#Mayores
#Jovenes
#Niños,Familias
#Mujeres
#Mujeres,Familias
#Jovenes,Niños

import json

from pprint import pprint

with open('300107-0-agenda-actividades-eventos.json') as data_file:    
 data = json.load(data_file)

 listemp=[]

for i in range(len(data["@graph"])):
	titulo=(data["@graph"][i]["title"])
	listemp.append(titulo)