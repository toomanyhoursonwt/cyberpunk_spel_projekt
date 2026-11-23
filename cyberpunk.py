import random as rand
import math
import funktioner
print("Welcome to the game...")
print("----------------------")

namn_karaktar = input("Vad är din karaktärs namn? ")
karaktar_stats = {
    "kraft":10, #direkt påverkan på dmg
    "hälsa":10, #direkt påverkan på, start 100 hp
    "medvetenhet":10, #chans att börja turn först
    "försvar":5, #block chans 20% max 80%
}

class Entity: 
    def __init__(self, namn, kraft, hälsa, försvar):
        self.namn = namn
        self.kraft = kraft
        self.hälsa = hälsa
        self.försvar = försvar
        pass

    def print_info(self):
        print(f"Det här är {self.namn} med {self.hälsa} hp")

young_cyberpunk = Entity("Lamborghini", 10, 1000, 2024)

young_cyberpunk.print_info()

class Item:
    def __init__(self, namn, kraft, försvar, hälsa, medvetenhet):
        self.namn = namn
        self.kraft = kraft
        self.försvar = försvar
        self.hälsa = hälsa
        self.medvetenhet = medvetenhet


stats_typshi = 0
poang = 5
while stats_typshi < 5:
    print(f"Du har {poang} poäng att dela ut till dina stats.")
    print(f"Dina stats är {karaktar_stats}")
    try:
        uppgradering = int(input("Tryck [1] för att öka kraft    Tryck [2] för att öka hälsa    Tryck [3] för att öka medvetenhet   Tryck [4] för att öka försvar  "))
    except:
        print("Skriv ett tal 1-4")
    if uppgradering == 1:
        karaktar_stats["kraft"] += 1
    elif uppgradering == 2:
        karaktar_stats["hälsa"] += 1
    elif uppgradering == 3:
        karaktar_stats["medvetenhet"] += 1
    elif uppgradering == 4:
        karaktar_stats["försvar"] += 1
    poang = poang - 1
    stats_typshi = stats_typshi - 1

print(f"Dina stats är {karaktar_stats}")

aventyr = 0
while aventyr < 10:
    val = input("Välj att fortsätta på din resa vänster[v] eller höger[h]")
    if val == "v" or val == "V":
        print("Du gick vänster...")
    elif val == "h" or val == "H":
        print("Du gick höger...")
    else:
        print("Skriv v eller h")
        continue
    aventyr = aventyr + 1