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

## Miért ne?
- a jelenlegi verzióban macerás letölteni az adatbázist (leírás lentebb)
- Python-t, valamint a szkriptekhez szükséges modulokat kell telepíteni az eszközre, amin futtatni akarod 
- nincsenek érintési pontok
- csak Volán járatok
- nincs grafikus interfész

# Első futtatás

### az adatbázis lekérése
0. Töröld a params.txt tartalmát, ha tesztelni szeretnéd az szkriptet, akkor hagyd ki ezt a lépést és menj a *program futtatása* részre.
1. Látogasd meg a <https://menetrendek.hu/>-t
2. Töltsd ki az adatokat, az alábbiak szerint:
   * Honnan? - egyértelmű
   * Hová? - egyértelmű
   * **CSAK VOLÁN JÁRATOK** legyen bejelölve!
   * Dátum - tetszés szerint, ha teljes adatbázist szeretnél ezeket jelöld be:
     * Bármely nap
     * Egész nap
3. Mielőtt elindítanád a keresést, nyisd meg a fejlesztői eszközöket a böngésződben:
<br>*Én most Firefoxban mutatom be neked, hogy hogyan haladj tovább. Ha Chrome-os vagy (botnet pls), akkor ügyeskedd ki magadnak, vagy telepíts Firefoxot!*
   1. nyomd meg a Ctrl + Shift + Q billentyűkombinációt,
   2. a weboldalon klikkelj a KERESÉS gombra,
   3. a "File" oszlopban találsz egy "talalatok_json.php" nevű állományt, klikk rá,
   4. jobbodalt kattints a "Params" fülre,
   5. a Form data-n belül kattints a "json:" után lévő szövegre, hogy kijelöld,
   6. ezt másold ki, és illeszd be a params.txt fileba, (A fileban hagytam egy sort példának, azt nyugodtan kitörölheted)
   <br>Példa:
   ![segítség](https://raw.githubusercontent.com/b9nc9/menetrendek/master/segitseg.png)
   <br>*Ha több útvonalat szeretnél felvenni a későbbi adatbázisba, akkor ismételd meg ezt a procedúrát az 1-es lépéstől! **Ügyelj arra, hogy a sorokat Enter-rel válaszd el!***
   7. parancssorban futtasd az adat.py szkriptet! (python adat.py)

### a program futtatása
1. parancssorban futtasd a menetrend.py szkriptet! (python volan.py)
2. kövesd a szkript utasításait!
3. fuss a buszhoz!

# Jelmagyarázat
Ha sikerült mindent a leírtak alapján beállítanod és az szkript kilistázta a kívánt menetrended, akkor kétféle jelzést láthatsz a buszok mellett:
1. [+] - a busz még nem ment el
2. [-] - a busz már elment
<br>Logikus, nem?

# Függőségek
* Windows/Linux/OSX: Python 3, egyértelműen
* Android/iOS-en jailbreak, valamilyen Terminal emulátor, Python 3
* Python modulok: chardet, requests, urllib3

   
