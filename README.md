# Bulls and cows
## Projekt na kurzu Pythonu na portále ENGETO (engeto.cz)
Bulls and cows je jednoduchá hra, která vygenruje náhodné 3 až 7místné číslo, podle zadání uživatele, které pak uživatel hádá. Hra trvá dokud hráč číslo neuhodne nebo neopustí hru zadáním: "quit", "q", "konec" nebo "k" (nezáleží na velikoti písmen). Skript lze spustit v českém jazyce pomocí parametru "-cz", jinak se skript spustí v angličtině.
Hra vznikla jako zadání pro kurz programování v Pythonu na portálu Engeto: https://engeto.cz

## Nastavení jazyka
Skript se implicitně spuští v anglickém jazyce, pro češtinu spusťte skript s parametrem -cz: ```python main.py -cz```


## Hodnocení od lektora: SPLNĚNO

### Co se mi líbilo:
Super pouziti type hints a dokumentace funkci - pozor ale na formatovani, ma to byt "def vypis_radek(sdeleni: str = hlaseni["oddelovac"])" - je tam ta mezera u =

L162 - super, ze pouzivas "if __name__ == "__main__""

L138 - plusove body za prehlednost

### Co by jsi měl/a zlepšit: 
Pozor, ze kdyz je v repozitari vice souboru tak nemusi na prvni pohled byt jasne, ktery je ten hlavni (pokud se nejmenuje main.py) - u malych projektu je to snazsi poznat ale program o 50 souborech uz by tohle oznaceni uvital.<br>
*poznámka autor: upraveno, skript se nyní jmenuje main.py*

bulls_cows_lang.py - takova drobnost do budoucna - tvuj navrh je super (mit moznost vice jazyku - to moc chvalim) ale casto se to dela tak, ze mas spise dict ktery ma klic ten jazyk a az potom ten string - ma to tu vyhodu, ze potom muzes mit nejaky config file (pro jednoduchost rekneme ze to bude zase jenom python script - v praxi se pouziva treba YAML) a tam budes mit neco jako LANG = "cz" a potom misto pouzivani jine promenne (hlaseni_cz vs hlaseni_en) v kodu budes mit print(hlaseni[LANG]["pozdrav"]) kde uplne nejlepsi je mit ty hodnoty "pozdrav" take nekde sjednocene jako treba POZDRAV = "pozdrav"). Potom cele volani bude print(hlaseni[LANG][POZDRAV]). Tvuj pristup s ifem pri -cz je take validni ale spise prestane byt prehledny pro vice jazyku - pokud to chces i tak delat pres prepinac a ne pres konfig tak take jde pouzit tu hodnotu z konzole jako klic toho dict - potom jenom budes kontrolovat jestli tam ten klic je a nebo neni (jestli ten jazyk podporujes a nebo ne).<br>
*poznámka autor: update*

L167 - tento zapis neni v Pythonu bezny, obecne jak Python nema stredniky a vse se resi odradkovanim a blokama tak davat vice prikazu na stejny radek akorat muze vest k chybam a v kodu se to nepouziva. Obecne pozor na tech vice veci na jednom radku - i treba L183 bych radeji rozepsal i kdyz je to syntakticky spravne - jedine, kde se toleruje vice veci na jednom radku je pri tom, kdyz mas treba funkci, ktera toho vraci vice a nebo treba pro unpacking pole<br>
*poznámka autor: opraveno*

L51 - trosku zbytecne to delat pres randint, kde je dost velka pradepodobnost, ze vygenerovane cislo bude mit duplicity a tak nesplni tu podminku a bude se to muset delat znova - nenapadl by te nejaky efektivnejsi zpusob, kde by jsi si treba vygeneroval nejakou sekvenci a z ni vzal vhodnou cast?<br>
*poznámka autor: update, nyní se číslo vybere pomocí metody listu "pop.()"*

L182 - klidne tady muzes pouzit True + break, ta promenna je trosku navic a kdyz ji jinak nepozivas tak bych ji tam asi ani nedaval - muze to byt matouci<br>
*poznámka autor: nyní ř. 205*

### Závěr:
Velmi pekny kod, ktery pouziva pokrocile techniky a plne splnuje pozadavky na druhy ukol. Jedina vytka je ke generovani nahodneho cisla - tam by bylo idealni se nad kodem jeste trochu zamyslet a zefektivnit. Ale i tak ukol akceptuji a chvalim zpracovani.

