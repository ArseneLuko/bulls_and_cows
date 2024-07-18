"""
bulls_and_cows.py: druhý projekt (první varianta) do Engeto Online Python Akademie
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""
# importování
from random import randint
from threading import local

# vstupní proměnné
hlaseni = {
    "pozdrav": "Hi cowgirl or cowboy!",
    "uvod": "I've generated a random 4 digit number for you.",
    "vyzva": "Let's play a bulls and cows game.",
    "zadani": "Enter a number:",
    "oddelovac": 78 * "-",
    "delka_4": "The number must contain four digits. Guess again.",
    "neni_cislo": "It is necessary to enter digits from 0 to 9",
    "unikatni": "Digits must be unique.",
    "zacina_nulou": "The number must not start with '0'."
}

# definice funkcí
def vypis_radek(sdeleni: str=hlaseni["oddelovac"], pozice: str="stred"):
    """
    Vypíše vstup za znaky "|" na začátku a na konci v velkové délce 79 znaků.
    Bez argumentu vypíše řadu pomlček. Pro argument pozice je možné zadat 2 možnosi: "stred" - zarovnání na střed, "vpravo" - zaovnání vpravo a "vlevo" - zarovnání vlevo.
    """
    if pozice == "stred":
        print(f"|{sdeleni: ^78}", end="|\n") # 79 celkem: "|" + 78
    elif pozice == "vlevo":
        print(f"| {sdeleni: <77}", end="|\n") # 79 celkem: "| " + 77
    elif pozice == "vpravo":
        print(f"| {sdeleni: >76} ", end="|\n") # 79 celkem: "| " + 76 + " "

def vytvor_hadane_cislo() -> int:
    """
    Funkce vrátí náhodné celé čtyřmístné číslo, které nezačíná číslicí 0. Tedy číslo mezi 1000 a 9999.
    """
    return randint(1000, 9999)

def kontroluj_je_cislo(ke_kontrole: str) -> bool:
    """
    Funkce vrátí celé číslo (integer), jestliže uživatel zadal pouze číslice.
    """
    try:
        ke_kontrole = int(ke_kontrole)
    except ValueError:
        vypis_radek(hlaseni["neni_cislo"], "vpravo")
        vypis_radek()
        return False
    else:
        return True

def kontroluj_pocet_cislic(ke_kontrole: str) -> bool:
    """
    Funkce vrátí True, jestli je počet znaků roven 4.
    """
    if len(ke_kontrole) != 4:
        vypis_radek(hlaseni["delka_4"], "vpravo")
        vypis_radek()
        return False
    else:
        return True

def kontroluj_unikatni_cislice(ke_kontrole: str) -> bool:
    """
    Funkce vrátí True, jestliže jsou číslice v zadaném čísle unikátní (neopakují se).
    """
    if len(set(ke_kontrole)) != 4:
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

def zadej_cislo() -> int:
    while True:
        vypis_radek(hlaseni["zadani"], "vlevo")
        cislo = input(f"|{78 * ' '}| \x1B[79D") # posune kurzor o 79 míst vlevo
        # https://stackoverflow.com/questions/38246529/how-do-i-get-user-input-in-the-middle-of-a-sentence-fill-in-the-blank-style-us

        if not kontroluj_je_cislo(cislo):
            continue
        elif not kontroluj_pocet_cislic(cislo):
            continue
        elif not kontroluj_unikatni_cislice(cislo):
            continue
        elif not kontroluj_nezacina_nulou(cislo):
            continue
        else:
            return int(cislo)

# hlavní program
if __name__ == "__main__":
    # vytvoří hledané číslo
    hadane_cislo = vytvor_hadane_cislo()

    # vypíše hlavičku hry na obrazovku
    vypis_radek(), vypis_radek(hlaseni["pozdrav"])
    vypis_radek(), vypis_radek(hlaseni["uvod"]), vypis_radek(hlaseni["vyzva"])
    vypis_radek()
    
    
    pokus_uhodnuti = zadej_cislo()

    # test 
    bull, cow = "1 bull", "2 cows"
    vypis_radek(f"There are {bull} and {cow}")
    vypis_radek(f"Cislo {pokus_uhodnuti} je typu: {type(pokus_uhodnuti)}")
