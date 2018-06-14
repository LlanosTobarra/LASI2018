import json
import requests
from elasticsearch import Elasticsearch

'''
El objetivo de este script es cargar en ElasticSearch información relacionada con la Guerra de las Galaxias
desde el sitio web http:/swapi.co.
Idea vista en: https://tryolabs.com/blog/2015/02/17/python-elasticsearch-first-steps/
'''

#conexión al cluster de Elasticsearh
es =  Elasticsearch(['localhost'],
                        http_auth=('loaddata', 'lasi2018'),
                        port=9200,
                    )
#cargamos personajes
print("Personajes")
i = 1
r = requests.get('http://swapi.co/api/people/'+ str(i))
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='lasi2018-sw1', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1

print("Peliculas")
#cargamos películas
i = 1
r = requests.get('https://swapi.co/api/films/'+ str(i))
while r.status_code == 200:
    r = requests.get('https://swapi.co/api/films/'+ str(i))
    es.index(index='lasi2018-sw2', doc_type='films', id=i, body=json.loads(r.content))
    i=i+1
    print(i)
   
    
print("Naves")
#cargamos naves
i = 2
r = requests.get('https://swapi.co/api/starships/'+ str(i))
while r.status_code == 200:
    r = requests.get('https://swapi.co/api/starships/'+ str(i))
    es.index(index='lasi2018-sw3', doc_type='starships', id=i, body=json.loads(r.content))
    i=i+1
    print(i)

print("Planetas")
#cargamos planetas
i = 1
r = requests.get('https://swapi.co/api/planets/'+ str(i))
while r.status_code == 200:
    r = requests.get('https://swapi.co/api/planets/'+ str(i))
    es.index(index='lasi2018-sw4', doc_type='planets', id=i, body=json.loads(r.content))
    i=i+1
    print(i)  


