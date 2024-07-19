"""
bulls_and_cows.py: druhý projekt (první varianta) do Engeto Online Python Akademie
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""
# importování
from random import randint

# vstupní proměnné
hlaseni = {
    "pozdrav": "Hi cowgirl or cowboy!",
    "uvod": "I've generated a random 4 digit number for you.",
    "vyzva": "Let's play a bulls and cows game.",
    "zadani": "Enter a number:",
    "oddelovac": 78 * "-",
    "delka_4": "The number must contain four digits. Guess again.",
    "neni_cislo": "It is necessary to enter digits from 0 to 9. Guess again.",
    "unikatni": "Digits must be unique. Guess again.",
    "zacina_nulou": "The number must not start with '0'. Guess again."
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
    """
    Vrátí čtyřmísnté číslo, zadané uživatelem. Funkce vrátí číslo pouze pokud projde přes všechny podmínky:\n
        1. zadané znaky jsou pouze číslice\n
        2. počet zadaných číslic je přesně čtyři\n
        3. všechny číslice jsou unikátní, neopakují se\n
        4. číslo nezačíná číslicí '0'\n
    """
    while True:
        vypis_radek(hlaseni["zadani"], "vlevo")
        cislo = input(f"|{78 * ' '}| \x1B[79D") # posune kurzor o 79 míst vlevo
        # https://stackoverflow.com/questions/38246529/how-do-i-get-user-input-in-the-middle-of-a-sentence-fill-in-the-blank-style-us

        # jestliže některá z kontrol neproběhne (Flase), vrátí True a provede příkaz 'continue'
        if ((not kontroluj_je_cislo(cislo)) or
            (not kontroluj_pocet_cislic(cislo)) or
            (not kontroluj_unikatni_cislice(cislo)) or
            (not kontroluj_nezacina_nulou(cislo))):
            continue
        else:
            return int(cislo)

def pridej_sklonovani(pocet):
    if pocet != 1:
        return "s"
    else:
        return ""

def zhodnoceni_pokusu(pokus: int, cislo: int) -> tuple:
    
    cislo_s = str(cislo)
    pokus_s = str(pokus)
    byci = 0
    kravy = 0

    for pozice, polozka in enumerate(pokus_s):
        if (polozka in cislo_s and
            cislo_s[pozice] != pokus_s[pozice]):
            kravy += 1
        if cislo_s[pozice] == pokus_s[pozice]:
            byci += 1

    # nastaví množné/jednotné číslo a vytvoří string pro return
    byci = str(byci) + " bull" + pridej_sklonovani(byci)
    kravy = str(kravy) + " cow" + pridej_sklonovani(kravy)
    return(byci, kravy)

# hlavní program
if __name__ == "__main__":
    # proměnné
    zatim_nezname_cislo = True
    pocet_pokusu = 0

    # vytvoří hádané číslo
    hadane_cislo = vytvor_hadane_cislo()

    # vypíše hlavičku hry na obrazovku
    vypis_radek(), vypis_radek(hlaseni["pozdrav"])
    vypis_radek(), vypis_radek(hlaseni["uvod"]), vypis_radek(hlaseni["vyzva"])
    vypis_radek(hadane_cislo) # slouž pro testování, vypíše číslo
    vypis_radek()
    
    while zatim_nezname_cislo: # nekonečná smyčka pro hádání čísla, ukončí se při uhodnutí
        pokus_uhodnuti, pocet_pokusu = zadej_cislo(), pocet_pokusu + 1

        if not pokus_uhodnuti == hadane_cislo:
            byci, kravy = zhodnoceni_pokusu(pokus_uhodnuti, hadane_cislo)
            vypis_radek(f"There are {byci} and {kravy}")
            vypis_radek()
        else:
            zatim_nezname_cislo = False
            vypis_radek("!!! Congratulations !!!")
            vypis_radek(f"Number of attempts needed to guess: >{pocet_pokusu}<")
            vypis_radek()
