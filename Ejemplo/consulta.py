#top de animes con una api
#instala modulo requests, pip3 install requests

"""
import requests

url = 'https://api.jikan.moe/v4/top/anime'
data = requests.get(url)
if data.status_code == 200:
    data = data.json()
    for e in data['data']:
        print(e['title'])
"""

import requests
import json
cedula = input("Digite su cedula\n")
url = 'https://api.digital.gob.do/v3/cedulas/'+cedula
data = requests.get(url)
rjson = data.json()
if "Nombre" in rjson:
    print(rjson['Nombre'])