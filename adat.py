#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import datetime

# ÁLLOMÁSOKHOZ TARTOZÓ INFORMÁCIÓ LEKÉRÉSE
def Allomasok(param):
    with requests.Session() as s:
        valasz = s.post('https://menetrendek.hu/menetrend/interface/index.php', data=param)
        lista = json.loads(valasz.content)
        return lista

def AllomasParam(varos, datum):
    return  '{"func":"getStationOrAddrByText","params":{"inputText":"%s","searchIn":["stations"],"searchDate":"%s","maxResults":30,"networks":[1,2,3],"currentLang":"hu"}}' % (varos, datum)


datum = datetime.datetime.now().strftime("%Y-%m-%d")
indulas = input("Honnan: ")
vegallomas = input("Hova: ")
megalloparam = [{'json' : AllomasParam(indulas, datum)}, {'json' : AllomasParam(vegallomas, datum)}]

indulOpciok = Allomasok(megalloparam[0])
vegOpciok = Allomasok(megalloparam[1])
# ÁLLOMÁSOK VÉGE

# FELHASZNÁLÓI INPUT
def Parameterek(datum, honnan_type, honnan_lsname, honnan_eovx, honnan_eovy, honnan_ls_id, honnan_settlement_id, honnan_site_code, honnan_zoom, hova_type, hova_lsname, hova_eovx, hova_eovy, hova_ls_id, hova_settlement_id, hova_site_code, hova_zoom):
    honnan_lsname = honnan_lsname.replace(' ', '+')
    hova_lsname = hova_lsname.replace(' ', '+')
    return '{"func":"getRoutes","params":{"datum":"%s","erk_stype":"%s","ext_settings":"block","filtering":0,"helyi":"No","honnan":"%s","honnan_eovx":"%s","honnan_eovy":"%s","honnan_ls_id":%d,"honnan_settlement_id":"%s","honnan_site_code":%d,"honnan_zoom":%d,"hour":"21","hova":"%s","hova_eovx":"%s","hova_eovy":"%s","hova_ls_id":%d,"hova_settlement_id":"%s","hova_site_code":%d,"hova_zoom":%d,"ind_stype":"%s","keresztul_stype":"%s","maxatszallas":"5","maxvar":"240","maxwalk":"700","min":"22","napszak":0,"naptipus":1,"odavissza":0,"preferencia":"1","rendezes":"1","submitted":1,"talalatok":1,"target":0,"utirany":"oda","var":"0"}}' % (datum, honnan_type, honnan_lsname, honnan_eovx, honnan_eovy, honnan_ls_id, honnan_settlement_id, honnan_site_code, honnan_zoom, hova_lsname, hova_eovx, hova_eovy, hova_ls_id, hova_settlement_id, hova_site_code, hova_zoom, hova_type, hova_type)

def Listaz(lista):
    n = 0
    for x in lista["results"]:
        n+=1
        print(str(n) + ": " + x["lsname"])

params = []
def Valaszt(params, honnanLista, hovaLista):
    print("HONNAN OPCIÓK:")
    Listaz(indulOpciok)
    print("\nHOVA OPCIÓK:")
    Listaz(vegOpciok)
    index_honnan = input("Honnan azonosító: ")
    index_hova = input("Hova azonosító: ")
    a = honnanLista["results"][int(index_honnan)-1]
    b = hovaLista["results"][int(index_hova)-1]
    params.append({'json' : Parameterek(datum, a["type"], a["lsname"], a["eovx"], a["eovy"], a["ls_id"], a["settlement_id"], a["site_code"], a["zoom"], b["type"], b["lsname"], b["eovx"], b["eovy"], b["ls_id"], b["settlement_id"], b["site_code"], b["zoom"])})
    params.append({'json' : Parameterek(datum, b["type"], b["lsname"], b["eovx"], b["eovy"], b["ls_id"], b["settlement_id"], b["site_code"], a["zoom"], a["type"], a["lsname"], a["eovx"], a["eovy"], a["ls_id"], a["settlement_id"], a["site_code"], a["zoom"])})

Valaszt(params, indulOpciok, vegOpciok)


# ADATBÁZIS ELKÉSZÍTÉSE
nyers = []
with requests.Session() as s:
    for x in range(0, len(params)):
        valasz = s.post('https://menetrendek.hu/menetrend/interface/index.php', data=params[x])
        nyers.append(json.loads(valasz.content))


db = open("adatok.txt", "a")
print(len(nyers))
for x in range(0, len(nyers)):
    for y in range(1, len(nyers[x]["results"]["talalatok"])):
        busz = nyers[x]["results"]["talalatok"][str(y)]
        db.write(busz["departureCity"] + ";" + busz["departureStation"] + ";" + busz["arrivalCity"] + ";" + busz["arrivalStation"] + ";" + busz["indulasi_ido"] + ";" + busz["erkezesi_ido"] + ";" + busz["talalat_kozlekedik"] + "\n")
db.close()
#ADATBÁZIS KÉSZ
