"""
Modul pro ukládání statistiky malé hry Bulls and Cows.
"""

import csv

from bulls_and_cows import vypis_radek

SOUBOR_TOP_10 = "top10.csv"

def uloz_do_souboru():
    pass

def nacti_obsah_souboru(soubor):
    with open(soubor) as nacteny_soubor:
        return tuple(csv.DictReader(nacteny_soubor))

def vypis_top_10():
    zaznamy = nacti_obsah_souboru(SOUBOR_TOP_10)
    vypis_radek()
    vypis_radek(f"{'Pořadí': >6} | {'Jméno': ^32} | Pokusů", "stred")
    for i in range(len(zaznamy)):
        vypis_radek(f"{zaznamy[i]['poradi']: >6} | {zaznamy[i]['jmeno']: <32} | {zaznamy[i]['pocet_pokusu']: >6}", "stred")
    vypis_radek()

if __name__ == "__main__":
    vypis_top_10()