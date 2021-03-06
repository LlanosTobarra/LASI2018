# Workshop:  "Data analysis with Elasticsearch and Kibana"
<p align="center">
  <img src="http://portal.uned.es/NUEVOWEB/IMAGENES/logo_uned.gif" height="50"/>
  <img src="https://www.scc.uned.es/iconos/Logo_SCC.png" height="50"/>
  <img src="https://snola.es/wp-content/uploads/2016/04/SNOLA_-2.png" height="50" />                                                        
</p>

LASI 2018 - 18-19 June León (https://lasi18.snola.es/)

The following repository contains materials for the Workshop 

## Initial instructions

The basic platform for Windows computers can be downloaded from the following link: https://goo.gl/i2FSqe
You need to have installed lasted version of Java Software Developers Kit. You can obtained from the following link:
If you prefer install everything from zero at the docs folders there is a setup.pdf with details.

There is an alternative option for non-Windows systems using docker (https://hub.docker.com/r/sebp/elkx/). Instructions to deploy the composed container are detailed in the web. Once the composed docker is running there are several python scripts in each example folder in order to load data inside Elasticsearch.

There is also a common cloud instance of Elasticsearch and Kibana. Ask lecturers for usernames and passwords.

## Datasets 


First dataset is based on xAPI data dedicated to predict student's academic performance. More data about this dataset can be found in the following articles:

  
- Amrieh, E. A., Hamtini, T., & Aljarah, I. (2016). Mining Educational Data to Predict Student’s academic Performance using Ensemble Methods. International Journal of Database Theory and Application, 9(8), 119-136.

- Amrieh, E. A., Hamtini, T., & Aljarah, I. (2015, November). Preprocessing and analyzing educational data set using X-API for improving student's performance. In Applied Electrical Engineering and Computing Technologies (AEECT), 2015 IEEE Jordan Conference on (pp. 1-5). IEEE.

Second dataset has been generated using the following script: https://github.com/jiscdev/lakhak

Additionally, some twitter data and Star Wars data is loaded.
