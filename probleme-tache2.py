#!/usr/bin/python3.4

import random, requests, json
result=random.random() * 1000
print(result)


x = {}
x["id-project"] = "PROJECT1"
x["id-tache"] = "1"
x["result"]= result
myparam = {"data" : json.dumps(x)}
r = requests.post("http://192.168.59.241:5000/rabbit/DONE",data=myparam)
print("RESULTAT ENVOYE")
