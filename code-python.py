#!/usr/bin/python3.4

import random
result=random.random() * 100
print(result)
return(result)
import requests, json

x = {}
x["id-p"] = "RABBITMQ"
x["id-t"] = "1"
x["result"]= result
myparam = {"data" : json.dumps(x)}
r = requests.post("http://192.168.59.241:5000/rabbit/DONE",data=myparam)
print("statut : {}".format(r.status_code))
print(r.text)
