import json
# leemos el fichero
with open('mondial.json', 'r') as myfile:
    data=myfile.read()
# lo parseamos (unmarshalling) a objeto
completo = json.loads(data)
mondial = completo['mondial']
for coleccion in mondial:
    with open(coleccion+'.json','+w') as target:
        json.dump(mondial[coleccion], target)