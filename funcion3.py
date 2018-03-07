#       "dtstart": "2018-03-10 12:30:00.0",
#       "dtend": "2018-03-10 23:59:00.0",

import json
from pprint import pprint
from datetime import datetime, date, time, timedelta
import calendar


with open('300107-0-agenda-actividades-eventos.json') as data_file:    
 data = json.load(data_file)

  #pprint(data["@graph"]["excluded-days"])

 fecha1=input("Dime la fecha de inicio ej:(01/01/1990): ")
 fecha2=input("Dime la fecha de fin ej:(02/01/1990): ")

 if fecha1 <= fecha2:
    
    listado=[]


    for i in range(len(data["@graph"])):
        titulo=(data["@graph"][i]["title"])
        listemp=titulo

        fecha11=(data["@graph"][i]["dtstart"])
        fecha11=fecha11.split('-')
        fecha11d=fecha11[2]
        fecha11d=fecha11d.split(' ')
        fecha11d=fecha11d[0]
        fecha11m=fecha11[1]
        fecha11y=fecha11[0]
        fecha11=('%s/%s/%s' % (fecha11d,fecha11m,fecha11y))

        fecha12=(data["@graph"][i]["dtend"])
        fecha12=fecha12.split('-')
        fecha12d=fecha12[2]
        fecha12d=fecha12d.split(' ')
        fecha12d=fecha12d[0]
        fecha12m=fecha12[1]
        fecha12y=fecha12[0]
        fecha12=('%s/%s/%s' % (fecha12d,fecha12m,fecha12y))

        if fecha1 <= fecha11 and fecha11 <= fecha2:
            if fecha1 <= fecha12 and fecha12 <= fecha2:
                listado.append(listemp)  
            
              
                
        listemp=()


 else:
    print("Las fechas estan mal.")



if len(listado) == 0:
    print("No se encontro eventos en esas fechas.")
else:
    print(listado)
    print("Total eventos en el rango buscado: %d" % (len(listado)))