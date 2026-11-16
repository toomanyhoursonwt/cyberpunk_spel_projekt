import random as rand
import math
print("Welcome to the game...")
print("----------------------")

namn_karaktar = input("Vad är din karaktärs namn? ")
karaktar_stats = {
    "kraft":10, #direkt påverkan på dmg
    "hälsa":10, #direkt påverkan på, start 100 hp
    "medvetenhet":10, #chans att börja turn först
    "försvar":5, #block chans 20% max 80%
}

#fråga om input med x poaäng som man kan tilldela mellan stats:
poang = 5
for x in range(5):
    print(f"Du har {poang} poäng att dela ut till dina stats.")
    print(f"Dina stats är {karaktar_stats}")
    try:
        uppgradering = int(input("Tryck [1] för att öka kraft    Tryck [2] för att öka hälsa    Tryck [3] för att öka medvetenhet   Tryck [4] för att öka försvar  "))
    except:
        print("Skriv ett tal 1-4")
        continue
    if uppgradering == 1:
        (
            
        )

class Entity: 
    def __init__(self, kraft, hälsa, försvar):
        self.kraft = kraft
        self.hälsa = hälsa
        self.försvar = försvar
        pass

    def print_info(self):
        print(f"Det här är en {self.kraft} med {self.hälsa} hästkrafter")

young_cyberpunk = Entity("Lamborghini", 1000, 2024)

young_cyberpunk.print_info()