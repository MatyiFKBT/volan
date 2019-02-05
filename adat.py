#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests


params = []
with open("param.txt", "r") as keresek:
    sor = keresek.read().split("\n")
    for x in sor:
        if x != "":
            params.append({'json' : x })

nyers = []
with requests.Session() as s:
    for x in range(0, len(params)):
        valasz = s.post('https://menetrendek.hu/menetrend/interface/index.php', data=params[x])
        nyers.append(json.loads(valasz.content))


db = open("adb.txt", "a")
for x in range(0, len(nyers)):
    for y in range(1, len(nyers[x]["results"]["talalatok"])):
        busz = nyers[x]["results"]["talalatok"][str(y)]
        db.write(busz["departureCity"] + ";" + busz["departureStation"] + ";" + busz["arrivalCity"] + ";" + busz["arrivalStation"] + ";" + busz["indulasi_ido"] + ";" + busz["erkezesi_ido"] + ";" + busz["talalat_kozlekedik"] + "\n")
db.close()
