# Sjednotit všechny 4 slovníky do jednoho,

# done přihlásit a uvítat uživatele a vypsat nabídku služeb,

# done umožnit výběr ze služeb,

# done první služba, vypsat všechny dostupné filmy,

# druhá služba, vypsat detaily jednoho filmu,
# třetí služba, doporučit film,
# ukončení programu.
# import pandas as pd
import random

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

films = {
"Shawshank Redemption" : film_1,
"The Godfather" : film_2,
"The Dark Knight" : film_3,
"The Prestige" : film_4
}

import random

def nahodny_film(filmy):
    nahodny_klic = random.choice(list(filmy.keys()))
    nahodny_film = filmy[nahodny_klic]
    print(f"Doporučený film: {nahodny_film['JMENO']}")


def vypis_detaily_filmu(jmeno_filmu, filmy):
    if jmeno_filmu in filmy:
        film = filmy[jmeno_filmu]
        print(f"Detaily filmu {jmeno_filmu}:")
        print(f"Jméno: {film['JMENO']}")
        print(f"Hodnocení: {film['HODNOCENI']}")
        print(f"Rok: {film['ROK']}")
        print(f"Režisér: {film['REZISER']}")
        print(f"Stopáž: {film['STOPAZ']} minut")
        print(f"Hrají: {', '.join(film['HRAJI'])}")
    else:
        print(f"Film s jménem {jmeno_filmu} nebyl nalezen.")



def action_pick():
    print(" Vyberte si funcki")
    print("---------------------------")
    print("1) vypsat všechny dostupné filmy / 2) vypsat detaily jednoho filmu / 3) doporučit film")
    action_choose = str(input())

    if action_choose == "1":
      for key, value in films.items():
        jmeno = value["JMENO"]
        print(f"{key} : {jmeno}")

    elif action_choose =="2":
      vypis_detaily_filmu(str(input("zadejte název filmu: ")), films)

    elif action_choose == "3":
       nahodny_film(films)

users = ["marek"]
def login():
    vstup = str(input("Zadjete své jméno: "))
    if vstup in users:
        print("Vítejte")
        action_pick()
    else:
        print("přístup zamítnut")
# login()
action_pick()
