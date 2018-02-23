#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests

payload = []
with open("param.txt", "r") as keresek:
    sor = keresek.read().split("\n")
    for x in sor:
        if x != "":
            payload.append(json.loads(x))

nyers = []
with requests.Session() as s:
    for x in payload:
        p = s.post('https://menetrendek.hu/uj_menetrend/hu/talalatok_json.php', data=x)
        nyers.append(json.loads(p.content))

db = open("adb.txt", "a")
for x in nyers:
    for y in range(1,len(x["talalatok"])):
        if ',' in x["talalatok"][str(y)]["departureStation"] and x["talalatok"][str(y)]["departureCity"] == "":
            felbont = x["talalatok"][str(y)]["departureStation"].split(',')
            x["talalatok"][str(y)]["departureCity"] = felbont[0]
            x["talalatok"][str(y)]["departureStation"] = felbont[1].strip()
        if ',' in x["talalatok"][str(y)]["arrivalStation"] and x["talalatok"][str(y)]["arrivalCity"] == "":
            felbont = x["talalatok"][str(y)]["arrivalStation"].split(',')
            x["talalatok"][str(y)]["arrivalCity"] = felbont[0]
            x["talalatok"][str(y)]["arrivalStation"] = felbont[1].strip()
            
        db.write(x["talalatok"][str(y)]["departureCity"] + ";"  + x["talalatok"][str(y)]["departureStation"] + ";" + x["talalatok"][str(y)]["arrivalCity"] + ";" + x["talalatok"][str(y)]["arrivalStation"] + ";" + x["talalatok"][str(y)]["indulasi_ido"] + ";" + x["talalatok"][str(y)]["erkezesi_ido"] + ";" + x["talalatok"][str(y)]["talalat_kozlekedik"] + "\n")

db.close()
