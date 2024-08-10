"""
bulls_and_cows.py: druhý projekt (první varianta) do Engeto Online Python Akademie
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""

# importování
from random import randint
from time import time
from sys import argv

# importování jazyka podle parametru
if (len(argv) > 1) and argv[1] == '-cz':
    from bulls_cows_lang import hlaseni_cz as hlaseni
    from bulls_cows_lang import pridej_sklonovani_cz as pridej_sklonovani
else:
    from bulls_cows_lang import hlaseni_en as hlaseni
    from bulls_cows_lang import pridej_sklonovani_en as pridej_sklonovani

# globální proměnné proměnné
ukonceni = ("quit", "q", "konec", "k")
pocet_pokusu = 0

# definice funkcí
def vypis_radek(sdeleni: str=hlaseni["oddelovac"], pozice: str="stred",
                opakovani: int=1):
    """
    Vypíše vstup mezi znaky "|" na začátku a na konci v velkové délce 79 znaků.
    Bez argumentu vypíše řadu pomlček. Pro argument pozice je možné zadat 2 možnosi: "stred" - zarovnání na střed (defaultní), "vpravo" - zaovnání vpravo a "vlevo" - zarovnání vlevo.
    """
    for _ in range(opakovani):
        if pozice == "stred":
            print(f"|{sdeleni: ^78}", end="|\n") # 79 celkem: "|" + 78
        elif pozice == "vlevo":
            print(f"| {sdeleni: <77}", end="|\n") # 79 celkem: "| " + 77
        elif pozice == "vpravo":
            print(f"| {sdeleni: >76} ", end="|\n") # 79 celkem: "| " + 76 + " "

def vypis_statistiky(pokusy, cas):
    vypis_radek(hlaseni["pokusy"].format(pokusy))
    vypis_radek(hlaseni["cas"].format(round(cas // 60), round(cas % 60)))
    vypis_radek(hlaseni["prumer"].format(round(cas / pokusy, 1)))
    vypis_radek()

def vytvor_hadane_cislo(velikost: int) -> str:
    """
    Funkce vrátí náhodné celé číslo (ve formátu textu), které nezačíná číslicí 0. Počet číslic je zvolen uživatelem. 
    """
    while True:
        nahodne_cislo = randint(int("1" + (velikost - 1) * "0"), int(velikost * "9"))
        # pokud je každé číslo jen jednou, bude množina (set) stejně velká jako list, ale pokud se nějaká číslice opakuje, v množině se vysktne jen jednou a tím pádem nebude mít set a list stejnou velikost
        if len(set(str(nahodne_cislo))) != len(list(str(nahodne_cislo))):
            continue
        break
    return str(nahodne_cislo)

def zadej_delku_cisla() -> int:
    """
    Funkce vrátí celé číslo v rozmezí 3 až 7.
    """
    vypis_radek(hlaseni["vyzva_pocet"], "vlevo")
    while True:
        vypis_radek(hlaseni["zadani_pocet"], "vlevo")
        velikost_cisla = input(f"|{78 * ' '}| \x1B[79D")
        if velikost_cisla.lower() in (ukonceni):
            vypis_radek(hlaseni["konec_bez_cisla"])
            vypis_radek(opakovani=2)
            quit()
        if velikost_cisla.isdecimal() and (2 < int(velikost_cisla) < 8):
            break
        vypis_radek(hlaseni["zadani_platny"], "vpravo")
    return int(velikost_cisla)

def kontroluj_je_cislo(ke_kontrole: str) -> bool:
    """
    Funkce vrátí True, jestliže uživatel zadal pouze číslice.
    """
    if not ke_kontrole.isdigit():
        vypis_radek(hlaseni["neni_cislo"], "vpravo")
        vypis_radek()
        return False
    else:
        return True

def kontroluj_pocet_cislic(ke_kontrole: str) -> bool:
    """
    Funkce vrátí True, jestli je počet znaků roven "velikost_cisla".
    """
    if len(ke_kontrole) != len(str(hadane_cislo)):
        vypis_radek(hlaseni["delka"].format(len(str(hadane_cislo))), "vpravo")
        vypis_radek()
        return False
    else:
        return True

def kontroluj_unikatni_cislice(ke_kontrole: str) -> bool:
    """
    Funkce vrátí True, jestliže jsou číslice v zadaném čísle unikátní (neopakují se).
    """
    if len(set(ke_kontrole)) != len(list(ke_kontrole)):
        vypis_radek(hlaseni["unikatni"], "vpravo")
        vypis_radek()
        return False
    else:
        return True

def kontroluj_nezacina_nulou(ke_kontrole: str) -> bool:
    """
    Funkce vrátí True, jestliže zadané číslo nezačíná 0.
    """
    if ke_kontrole[0] == "0":
        vypis_radek(hlaseni["zacina_nulou"], "vpravo")
        vypis_radek()
        return False
    else:
        return True

def zadej_cislo() -> str:
    """
    Vrátí čtyřmísnté číslo, zadané uživatelem. Funkce vrátí číslo pouze pokud projde přes všechny podmínky:\n
        1. zadané znaky jsou pouze číslice\n
        2. počet zadaných číslic je přesně čtyři\n
        3. všechny číslice jsou unikátní\n
        4. číslo nezačíná číslicí '0'\n
    """
    while True:
        vypis_radek(hlaseni["hadej_cislo"], "vlevo")
        cislo = input(f"| {velikost_cisla * '_'}{(77 - velikost_cisla) * ' '}| \x1B[79D").strip() # posune kurzor o 79 míst vlevo
        # https://stackoverflow.com/questions/38246529/how-do-i-get-user-input-in-the-middle-of-a-sentence-fill-in-the-blank-style-us

        # jestliže některá z kontrol neproběhne (Flase), vrátí True a provede příkaz 'continue'
        if cislo.lower() in (ukonceni):
            vypis_radek(hlaseni["konec"])
            vypis_radek(opakovani=2)
            quit()

        if ((not kontroluj_je_cislo(cislo)) or
            (not kontroluj_pocet_cislic(cislo)) or
            (not kontroluj_unikatni_cislice(cislo)) or
            (not kontroluj_nezacina_nulou(cislo))):
            continue
        else:
            return cislo

def zhodnoceni_pokusu(pokus: str, cislo: str) -> tuple: 
    byci = 0
    kravy = 0

    for pozice, polozka in enumerate(pokus):
        if cislo[pozice] == pokus[pozice]:
            byci += 1
        elif polozka in cislo:
            kravy += 1

    # nastaví množné/jednotné číslo a vytvoří string pro return
    byci = pridej_sklonovani(byci, druh="bull")
    kravy = pridej_sklonovani(kravy, druh="cow")
    return(byci, kravy)

# hlavní program
if __name__ == "__main__":
    # proměnné
    zatim_nezname_cislo = True
    
    # vypíše hlavičku hry na obrazovku
    vypis_radek(opakovani=2), vypis_radek(hlaseni["pozdrav"])
    vypis_radek(), vypis_radek(hlaseni["vyzva"]), vypis_radek(hlaseni["uvod"])
    vypis_radek(hlaseni["pravidla-1"]), vypis_radek(hlaseni["pravidla-2"])
    vypis_radek(hlaseni["pravidla-konec"])
    vypis_radek()

    # vytvoří hádané číslo v délce uživatelského vstupu
    hadane_cislo = vytvor_hadane_cislo(velikost_cisla := zadej_delku_cisla())
    # vypis_radek(hadane_cislo, "stred") # debugování, vypíše číslo
    
    vypis_radek(hlaseni["generovano"].format(velikost_cisla))
    vypis_radek(hlaseni["mereni_casu"])
    input(f"|{78 * ' '}| \x1B[79D")
    vypis_radek(opakovani=2)
    zacatecni_cas = time()
    while zatim_nezname_cislo: # nekonečná smyčka pro hádání čísla, ukončí se při uhodnutí
        pokus_uhodnuti, pocet_pokusu = zadej_cislo(), pocet_pokusu + 1

        if not pokus_uhodnuti == hadane_cislo:
            byci, kravy = zhodnoceni_pokusu(pokus_uhodnuti, hadane_cislo)
            vypis_radek(hlaseni["hodnoceni"].format(byci, kravy))
            vypis_radek()
        else:
            zatim_nezname_cislo = False
            vysledny_cas = round(time() - zacatecni_cas, 1)
            vypis_radek(hlaseni["gratulace"])
            vypis_statistiky(pokusy=pocet_pokusu, cas=vysledny_cas)