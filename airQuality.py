import urllib.request, json, os
import pymongo
from datetime import datetime

villes = ["paris", "london", "madrid", "berlin", "amsterdam", "moscow", "shanghai", "beijin", "tokyo", "seoul", "hongkong", "singapore", "newyork", "chicago", "boston", "l.a.", "toronto", "melbourne", "sydney",]

for v in villes:
    date = datetime.now()
    nomFichier = "/boot/CO2/" + v + date.strftime("%m-%d-%Y_%H:%M:%S")+ ".json"

    with urllib.request.urlopen("https://api.waqi.info/feed/"+ v +"/?token=872697cc1982e50fe12fc319ad65f52f0ea61eda") as url:
        data1 = json.load(url)

    with open(nomFichier, "a") as myfile:
        myfile.write(json.dumps(data1))
    
    bashCommand = "mongoimport --db test --collection CO2 " + nomFichier
    os.system(bashCommand)

