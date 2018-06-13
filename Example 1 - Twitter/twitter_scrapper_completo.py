# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:21:08 2017

@author: Llanos
"""

#llamamos a la librería
import tweepy
import json
#creamos cuatro variables para poner nuestros códigos. 
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

#cargamos el cliente de ElasticSearch
from elasticsearch import Elasticsearch

#creamos una clase que hereda a StreamListener
class StreamWriter(tweepy.StreamListener):
    def __init__(self, topic_name, *args, **kwargs):
        tweepy.StreamListener.__init__(self,*args, **kwargs)
        self.topic_name = topic_name

        #creamos la conexión a ElasticSearch
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        print("Conectados a ElasticSearch")
        print(self.es.info())

        

    def on_data(self, data):
        try:
            print(data)
            self.es.index(index="LASI2018-{0}".format(self.topic_name), doc_type="tweet",body=json.loads(data))
        except Exception as e:
            print("Excepción durante la ejecución {0}".format(e))
        return True



#Se crea el token de autenticación
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#obtenemos el manejador de la api
api = tweepy.API(auth)

#Abrimos un stream de Twitter usando nuestra clase
msl= StreamWriter("uned")
miStream = tweepy.Stream(auth = api.auth, listener=msl)

#capturamos los tweets, vamos a capturar también excepciones por si acaso
try:
    miStream.filter(track=[u'uned',u'@uned',u'unedianos'])
except Exception as e:
    print("Excepción durante la ejecución {0}".format(e))