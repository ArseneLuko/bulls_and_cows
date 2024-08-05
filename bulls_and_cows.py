"""
bulls_and_cows.py: druhý projekt (první varianta) do Engeto Online Python Akademie
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""
# importování
from random import randint

# globální proměnné proměnné
ukonceni = ("quit", "q")
pocet_pokusu = 0
hlaseni = {
    "pozdrav": "Hi cowgirl or cowboy!",
    "uvod": "I will generat a random X-digit number for you.",
    "vyzva": "Let's play The bulls and cows game.",
    "vyzva_pocet": "Choose how many digits the number will contain.",
    "zadani_pocet": "Enter a number between 3 to 7:",
    "zadani_platny": "Enter a valid entry - only one number from 3 to 7.",
    "hadej_cislo": "Enter your guess:",
    "generovano": "I've thought a number, let's guess it.",
    "oddelovac": 78 * "-",
    "delka": "Must have the same number of digits as you have chosen. Guess again.",
    "neni_cislo": "It is necessary to enter digits from 0 to 9. Guess again.",
    "unikatni": "Digits must be unique. Guess again.",
    "zacina_nulou": "The number must not start with '0'. Guess again.",
    "konec": "Thanks for playing! But sorry, I'll not tell you the number.",
    "konec_bez_cisla": "Thanks for playing! See you next time."
}

# definice funkcí
def vypis_radek(sdeleni: str=hlaseni["oddelovac"], pozice: str="stred"):
    """
    Vypíše vstup mezi znaky "|" na začátku a na konci v velkové délce 79 znaků.
    Bez argumentu vypíše řadu pomlček. Pro argument pozice je možné zadat 2 možnosi: "stred" - zarovnání na střed (defaultní), "vpravo" - zaovnání vpravo a "vlevo" - zarovnání vlevo.
    """
    if pozice == "stred":
        print(f"|{sdeleni: ^78}", end="|\n") # 79 celkem: "|" + 78
    elif pozice == "vlevo":
        print(f"| {sdeleni: <77}", end="|\n") # 79 celkem: "| " + 77
    elif pozice == "vpravo":
        print(f"| {sdeleni: >76} ", end="|\n") # 79 celkem: "| " + 76 + " "

def vytvor_hadane_cislo(velikost: int) -> int:
    """
    Funkce vrátí náhodné celé číslo, které nezačíná číslicí 0. Počet číslic je zvolen uživatelem.
    """
    while True:
        nahodne_cislo = randint(int("1" + (velikost - 1) * "0"), int(velikost * "9"))
        # pokud je každé číslo jen jednou, bude množina (set) stejně velká jako list, ale pokud se nějaká číslice opakuje, v množině se vysktne jen jednou a tím pádem nebude mít set a list stejnou velikost
        if len(set(str(nahodne_cislo))) != len(list(str(nahodne_cislo))):
            continue
        break
    return nahodne_cislo

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
            vypis_radek()
            vypis_radek()
            quit()
        if velikost_cisla.isdecimal() and (2 < int(velikost_cisla) < 8):
            break
        vypis_radek(hlaseni["zadani_platny"], "vpravo")
    vypis_radek(hlaseni["generovano"])
    vypis_radek()
    vypis_radek()
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
        vypis_radek(hlaseni["delka"], "vpravo")
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

def zadej_cislo() -> int:
    """
    Vrátí čtyřmísnté číslo, zadané uživatelem. Funkce vrátí číslo pouze pokud projde přes všechny podmínky:\n
        1. zadané znaky jsou pouze číslice\n
        2. počet zadaných číslic je přesně čtyři\n
        3. všechny číslice jsou unikátní\n
        4. číslo nezačíná číslicí '0'\n
    """
    while True:
        vypis_radek(hlaseni["hadej_cislo"], "vlevo")
        cislo = input(f"|{78 * ' '}| \x1B[79D") # posune kurzor o 79 míst vlevo
        # https://stackoverflow.com/questions/38246529/how-do-i-get-user-input-in-the-middle-of-a-sentence-fill-in-the-blank-style-us

        # jestliže některá z kontrol neproběhne (Flase), vrátí True a provede příkaz 'continue'
        if cislo.lower() in (ukonceni):
            vypis_radek(hlaseni["konec"])
            vypis_radek()
            vypis_radek()
            quit()

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

    # vypíše hlavičku hry na obrazovku
    vypis_radek(), vypis_radek(hlaseni["pozdrav"])
    vypis_radek(), vypis_radek(hlaseni["vyzva"]), vypis_radek(hlaseni["uvod"])
    vypis_radek()

    # vytvoří hádané číslo v délce uživatelského vstupu
    hadane_cislo = vytvor_hadane_cislo(zadej_delku_cisla())
    # vypis_radek(hadane_cislo, "stred") # debugování, vypíše číslo
    
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