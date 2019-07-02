#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, date


class Busz:
    def __init__(self, sor):
        l = sor.split(";")
        self.indulasi_varos = l[0]
        self.indulasi_allomas = l[1]
        self.erkezesi_varos = l[2]
        self.erkezesi_allomas = l[3]
        self.indulasi_ido = l[4]
        self.erkezesi_ido = l[5]
        self.kozlekedik = l[6].strip()

    def Elment(self):
        most = datetime.now()
        indul = self.indulasi_ido.split(":")
        jar = datetime(most.year,most.month,most.day,int(indul[0]),int(indul[1]),most.second)
        if(most > jar):
            print("[-]", end=" ")
        else:
            print("[+]", end=" ")
    
    def TolIg(self):
        print(("{0}, {1} - {2}, {3}").format(self.indulasi_varos, self.indulasi_allomas, self.erkezesi_varos, self.erkezesi_allomas))


    def MaJar(self):
        most = datetime.now()
        if (self.kozlekedik == "naponta"):
            self.TolIg()
            self.Elment()
            print("{0} - {1}".format(self.indulasi_ido, self.erkezesi_ido))
        elif (self.kozlekedik == "munkanapokon" and date.weekday(most) < 5):
            self.TolIg()
            self.Elment()
            print("{0} - {1}".format(self.indulasi_ido, self.erkezesi_ido))
        elif (self.kozlekedik == "munkaszüneti napok kivételével naponta" and date.weekday(most) < 6):
            self.TolIg()
            self.Elment()
            print("{0} - {1}".format(self.indulasi_ido, self.erkezesi_ido))
        elif (self.kozlekedik == "szabadnap kivételével naponta" and date.weekday(most) != 5):
            self.TolIg()
            self.Elment()
            print("{0} - {1}".format(self.indulasi_ido, self.erkezesi_ido))
        elif (self.kozlekedik == "munkaszüneti napokon" and date.weekday(most) == 6):
            self.TolIg()
            self.Elment()
            print("{0} - {1}".format(self.indulasi_ido, self.erkezesi_ido))
        elif (self.kozlekedik == "szabad- és munkaszüneti napokon" and date.weekday(most) > 4):
            self.TolIg()
            self.Elment()
            print("{0} - {1}".format(self.indulasi_ido, self.erkezesi_ido))
        elif (self.kozlekedik == "szabadnapokon" and date.weekday(most) == 5):
            self.TolIg()
            self.Elment()
            print("{0} - {1}".format(self.indulasi_ido, self.erkezesi_ido))
        elif (self.kozlekedik == "iskolai előadási napokon" and most.month != 7 and most.month != 8 and date.weekday(most) != 5 and date.weekday(most) != 6) or (most.month == 6 and most.day <= 15 and date.weekday(most) != 5 and date.weekday(most) != 6):
            self.TolIg()
            self.Elment()
            print("{0} - {1}".format(self.indulasi_ido, self.erkezesi_ido))



        
def FelhBevitel(lista):
    be = abs(int(input(">")))
    try:
        return lista[be-1]
    except IndexError:
        print("Nincs ilyen elem.")
        return FelhBevitel(lista)

def Main():
    buszok = []

    with open("adatok.txt", "r") as be:
        for x in be:
            buszok.append(Busz(x))
    #INDULÁSI VÁROS KIVÁLASZTÁSA
    print("Melyik városból?")
    lista_honnan = set()
    for x in buszok:
        lista_honnan.add(x.indulasi_varos)
    lista_honnan = list(lista_honnan)

    for index, x in enumerate(lista_honnan):
        print(("[{0}] {1}").format(index+1, x))

    varos = FelhBevitel(lista_honnan)



    #INDULÁSI ÁLLOMÁS KIVÁLASZTÁSA
    print("Melyik állomásról?")
    lista_allomasok = set()
    for x in buszok:
        if(x.indulasi_varos == varos):
            lista_allomasok.add(x.indulasi_allomas)

    lista_allomasok = list(lista_allomasok)

    for index, x in enumerate(lista_allomasok):
        print(("[{0}] {1}").format(index+1, x))

    allomas = FelhBevitel(lista_allomasok)


    #CÉLVÁROS KIVÁLASZTÁSA
    print("Melyik városba?")
    lista_veg = set()
    for x in buszok:
        if(x.indulasi_varos == varos and x.indulasi_allomas == allomas):
            lista_veg.add(x.erkezesi_varos)

    lista_veg = list(lista_veg)

    for index, x in enumerate(lista_veg):
        print(("[{0}] {1}").format(index+1, x))

    veg = FelhBevitel(lista_veg)

    #CÉLÁLLOMÁS KIVÁLASZTÁSA
    print("Melyik megállóba?")
    lista_vegallomas = set()
    for x in buszok:
        if(x.indulasi_varos == varos and x.indulasi_allomas == allomas and veg == x.erkezesi_varos):
            lista_vegallomas.add(x.erkezesi_allomas)

    lista_vegallomas = list(lista_vegallomas)

    for index, x in enumerate(lista_vegallomas):
        print(("[{0}] {1}").format(index+1, x))

    vegallomas = FelhBevitel(lista_vegallomas)


    #EREDMÉNYEK KIÍRÁSA
    for x in buszok:
        if(x.indulasi_varos == varos and x.indulasi_allomas == allomas and veg == x.erkezesi_varos and vegallomas == x.erkezesi_allomas):
            x.MaJar()
