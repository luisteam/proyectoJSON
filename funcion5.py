import json

from pprint import pprint

with open('300107-0-agenda-actividades-eventos.json') as data_file:    
 data = json.load(data_file)

 listemp=[]

 nombre=input("Dime un evento en concreto: ")
 fecha=input("Ahora su fecha de apertura y te dare su ubicacion ej:(02/01/1990): ")


 for i in range(len(data["@graph"])):
    titulo=(data["@graph"][i]["title"])
    fecha11=(data["@graph"][i]["dtstart"])
    fecha11=fecha11.split('-')
    fecha11d=fecha11[2]
    fecha11d=fecha11d.split(' ')
    fecha11d=fecha11d[0]
    fecha11m=fecha11[1]
    fecha11y=fecha11[0]
    fecha11=('%s/%s/%s' % (fecha11d,fecha11m,fecha11y))
        
    if nombre == titulo:
        if fecha11 == fecha:
            gps=(data["@graph"][i]["location"])
            latitud=(gps["latitude"])
            longitud=(gps["longitude"])


print(" ")
print("Aqui tienes: ")
print("https://www.google.es/maps/@%s,%s,15z?hl=es" % (latitud,longitud))
print(" ")