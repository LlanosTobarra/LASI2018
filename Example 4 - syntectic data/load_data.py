import pandas as pd
import json
from elasticsearch import Elasticsearch

username="elastic"
password="Pssmdc3otlRjjxYlNe23"

'''
El objetivo de este script es cargar en ElasticSearch el excel ejemplo. Nos servirá como base para
trabajar.
El fichero que queremos cargar está en formato excel, tenemos que pasarlo a JSON
nos apoyamos en pandas.
'''
#Abrimos el fichero
df=pd.read_csv("out2.csv",sep=',')
#cogemos la hoja del excel

print("Open file")
#exportamos el dataframe a JSON. La orientación por defecto es columnas, para que trate cada registro como un elemento
#hay que poner el orient como records.
tmp=df.to_json(orient='records')
print("File to JSON")

#conexión al cluster de Elasticsearh
es = Elasticsearch(['localhost'],http_auth=(username,password),port=9200,)
#es=Elasticsearch(['localhost'],port=9200)
print("Connected to ElasticSearch")
print(es.info())
#cargamos de uno en uno
df_json= json.loads(tmp)
print("Start loading")
i=0
for doc in df_json:
    print(i)
    es.index(index="lasi2018-lak17", doc_type="registry",body=doc)
    i=i+1
print("Ended")