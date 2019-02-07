    __      __   _             
    \ \    / /  | |            
     \ \  / /__ | | __ _ _ __  
      \ \/ / _ \| |/ _` | '_ \ 
       \  / (_) | | (_| | | | |
        \/ \___/|_|\__,_|_| |_|.py

Offline szkript, ami a menetrendek.hu-s adatbázissal funkcionál.

## Miért?
+ az adatbázis beszerzése után offline működik, így internet kapcsolat nélkül is tudsz buszt keresni magadnak (persze a meglévő adatbázisból)
+ nem kell Origo-s híreket bámulnod
+ nincs idegesítő pop-up, amikor elindítod a szkriptet, mint a menetrendek.hu-n
+ nem kell megvárnod, hogy az auto-complete betöltsön, majd az annak segítségével kiválasztott állomasokkal keress
+ [Android App!](https://github.com/b9nc9/VolanAndroid)

## Miért ne?
- Python-t, valamint a szkriptekhez szükséges modulokat kell telepíteni az eszközre, amin futtatni akarod 
- nincsenek érintési pontok
- csak Volán járatok

# Első futtatás

### az adatbázis lekérése
2019. feb. 06-tól a lekérdezés csupán csak ennyiből áll:
![segítség](https://raw.githubusercontent.com/b9nc9/volan/master/volan.png)
(Egy lekérdezés felveszi az adatbázisba az oda- és visszautat.)

### a program futtatása
1. parancssorban futtasd a volan.py szkriptet! (python volan.py)
2. kövesd a szkript utasításait!
3. fuss a buszhoz!

# Jelmagyarázat
Ha sikerült mindent a leírtak alapján beállítanod és az szkript kilistázta a kívánt menetrended, akkor kétféle jelzést láthatsz a buszok mellett:
1. [+] - a busz még nem ment el
2. [-] - a busz már elment
<br>Logikus, nem?

# Függőségek
* Windows/Linux/OSX: Python 3, egyértelműen
* Android/iOS-en jailbreak, valamilyen Terminal emulátor (Adnroidra a [Termux](https://termux.com/)-ot ajánlom), Python 3
* Python modulok: chardet, requests, urllib3
