"""
bulls_and_cows.py: druhý projekt (první varianta) do Engeto Online Python Akademie
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""
# importování
from random import randint

# vstupní proměnné
pozdrav = "Hi cowgirl or cowboy!"
uvod = "I've generated a random 4 digit number for you."
vyzva = "Let's play a bulls and cows game."
zadani = "Enter a number:"
oddelovac = 78 * "-"
delka_4 = "The number must contain four digits. Guess again."

# definice funkcí
def vypis_radek(sdeleni: str=oddelovac, pozice: str="stred"):
    """
    Vypíše vstup za znak "|" na začátku v velkové délce 79 znaků.
    Bez argumentu vypíše řadu pomlček.
    """
    if pozice == "stred":
        print(f"|{sdeleni: ^78}", end="|\n")
    elif pozice == "vlevo":
        print(f"| {sdeleni: <77}", end="|\n")

def vytvor_hadane_cislo() -> int:
    """
    Funkce vrátí náhodné celé čtyřmístné číslo, které nezačíná číslicí 0. Tedy číslo mezi 1000 a 9999.
    """
    return randint(1000, 9999)

def zadej_cislo() -> int:
    while True:
        vypis_radek(zadani, "vlevo")
        cislo = input(f"|{78 * ' '}| \x1B[79D") # posune kurzor o 79 míst vlevo
        # https://stackoverflow.com/questions/38246529/how-do-i-get-user-input-in-the-middle-of-a-sentence-fill-in-the-blank-style-us
        if len(cislo) != 4:
            vypis_radek(delka_4, "vlevo")
            vypis_radek()
            continue
        else:
            return cislo

# hlavní program
if __name__ == "__main__":
    # vytvoří hledané číslo
    hadane_cislo = vytvor_hadane_cislo()

    # vypíše hlavičku hry na obrazovku
    vypis_radek(), vypis_radek(pozdrav)
    vypis_radek(), vypis_radek(uvod), vypis_radek(vyzva)
    vypis_radek()
    
    
    pokus_uhodnuti = zadej_cislo()

    # test 
    bull, cow = "1 bull", "2 cows"
    vypis_radek(f"There are {bull} and {cow}", "vlevo")
