hlaseni_en = {
    "pozdrav": "Hi cowgirl or cowboy!",
    "uvod": "I will generat a random X-digit number for you.",
    "pravidla-1": "If palces match I'll give you a bull,",
    "pravidla-2": "if places are differn I'll give you a cow.",
    "pravidla-konec": "You can quit by typing: 'quit' or 'q'",
    "vyzva": "Let's play The bulls and cows game.",
    "vyzva_pocet": "Choose how many digits the number will contain.",
    "zadani_pocet": "Enter a number between 3 to 7:",
    "zadani_platny": "Enter a valid entry - only one number from 3 to 7.",
    "generovano": "I've thought a {} digit number, let's guess it.",
    "hadej_cislo": "Enter your guess:",
    "oddelovac": 78 * "-",
    "delka": "The number must contain of {} digits. Guess again.",
    "neni_cislo": "It is necessary to enter digits from 0 to 9. Guess again.",
    "unikatni": "Digits must be unique. Guess again.",
    "zacina_nulou": "The number must not start with '0'. Guess again.",
    "konec": "Thanks for playing! But sorry, I'll not tell you the number.",
    "konec_bez_cisla": "Thanks for playing! See you next time.",
    "hodnoceni": "There are {} and {}",
    "gratulace": "!!! Congratulations !!!",
    "pokusy": "Number of attempts needed to guess: >{}<",
    "cas": "Seconds needed to guess: >{}<",
    "prumer": "Avarage seconds per try: >{}<",
    "mereni_casu": "Press Enter to start timing..."
}

hlaseni_cz = {
    "pozdrav": "Zdravím Tě, hráči * hráčko!",
    "uvod": "Vytvořím pro Tebe X-místné číslo, které budeš hádat,",
    "pravidla-1": "když bude číslice na správném místě, dostaneš býka,",
    "pravidla-2": "když bude číslice na jiném místě, dostaneš krávu.",
    "pravidla-konec": "Hru můžeš ukončit zadáním 'konec' nebo 'k'",
    "vyzva": "Pojďme hrát hru: The bulls and cows game.",
    "vyzva_pocet": "Zadej kolik číslic bude mít hadané číslo.",
    "zadani_pocet": "Zadej číslo mezi 3 a 7:",
    "zadani_platny": "Zadej platný vstup - pouze celé číslo od 3 do 7.",
    "generovano": "Mám {} místné číslo, zkus jej uhodnout.",
    "hadej_cislo": "Hádej číslo:",
    "oddelovac": 78 * "-",
    "delka": "Číslo musí mít {} číslic. Hádej znovu.",
    "neni_cislo": "Zadávej pouze číslice od 0 do 9. Hádej znovu.",
    "unikatni": "Číslice musí být unikátní. Hádej znovu.",
    "zacina_nulou": "Číslo nesmí začínat nulou. Hádej znovu.",
    "konec": "Díky za hru! Ale nečekej, že Ti číslo prozradím ;).",
    "konec_bez_cisla": "Díky za hru! Přijď příště.",
    "hodnoceni": "Počet {} a {}",
    "gratulace": "!!! Gratulace !!!",
    "pokusy": "Celkový počet pokusů: >{}<",
    "cas": "Celkový čas (sekundy): >{}<",
    "prumer": "Průměrný čas na jeden pokus (sekundy): >{}<",
    "mereni_casu": "Stiskni Enter pro zahájení měření času..."
}

def pridej_sklonovani_en(pocet: int, druh: str) -> str:
    """
    Podle počtu přidá k druhu koncov= "s" - 0 nebo více než jedna.
    """
    if pocet != 1:
        return str(pocet) + " " + druh + "s"
    else:
        return str(pocet) + " " + druh
    
def pridej_sklonovani_cz(pocet: int, druh: str) -> str:
    """
    Podle druhu vypíše v češtině název druhu a počet.
    """
    if druh == "bull":
        return "býků: " + str(pocet)
    elif druh == "cow":
        return "krav: " + str(pocet)