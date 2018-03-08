import json

from pprint import pprint

with open('300107-0-agenda-actividades-eventos.json') as data_file:    
 data = json.load(data_file)

niños=[]
mayores=[]

for i in range(len(data["@graph"])):
	objeto=(data["@graph"][i])

	if 'audience' in objeto:
		audiencia=(objeto["audience"])
		titulo=(data["@graph"][i]["title"])

		if "Niños" in audiencia:
			niños.append(titulo)

		if "Mayores" in audiencia:
			mayores.append(titulo)

print("Numero de eventos para: Niños: %d, Mayores: %d." % (len(niños),len(mayores)))