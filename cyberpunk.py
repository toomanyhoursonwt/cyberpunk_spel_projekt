import random as rand
import math
import funktioner
import listor_namn

STEG_FALLA = 1
STEG_FIENDE = 2
STEG_KISTA = 3

print("""
 /$$$$$$$$                  /$$                          
|__  $$__/                 | $$                          
   | $$  /$$$$$$   /$$$$$$$| $$$$$$$  /$$$$$$$   /$$$$$$ 
   | $$ /$$__  $$ /$$_____/| $$__  $$| $$__  $$ /$$__  $$
   | $$| $$$$$$$$| $$      | $$  \ $$| $$  \ $$| $$  \ $$
   | $$| $$_____/| $$      | $$  | $$| $$  | $$| $$  | $$
   | $$|  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$/
   |__/ \_______/ \_______/|__/  |__/|__/  |__/ \______/ 
                                                         
                                                         
                                                         
 /$$$$$$$            /$$ /$$                             
| $$__  $$          | $$|__/                             
| $$  \ $$  /$$$$$$ | $$ /$$ /$$$$$$$   /$$$$$$          
| $$  | $$ /$$__  $$| $$| $$| $$__  $$ /$$__  $$         
| $$  | $$| $$$$$$$$| $$| $$| $$  \ $$| $$  \ $$         
| $$  | $$| $$_____/| $$| $$| $$  | $$| $$  | $$         
| $$$$$$$/|  $$$$$$$| $$| $$| $$  | $$|  $$$$$$$         
|_______/  \_______/|__/|__/|__/  |__/ \____  $$         
                                            | $$         
                                            | $$         
                                            |__/         
""")
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

class Item:
    def __init__(self, namn, kraft, försvar, hälsa, medvetenhet):
        self.namn = namn
        self.kraft = kraft
        self.försvar = försvar
        self.hälsa = hälsa
        self.medvetenhet = medvetenhet


poang = 5
while poang > 0:
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

print(f"Dina stats är {karaktar_stats}")
playerhp = funktioner.halsa(karaktar_stats["hälsa"])

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
    steg = funktioner.steg()
    if steg == STEG_FALLA:
        falla = funktioner.skada(rand.randint(5, 15), playerhp)
    elif steg == STEG_FIENDE:
        startattack = funktioner.start_attack(karaktar_stats["medvetenhet"])
        fiende = Entity(listor_namn.enemy_name[rand.randrange(len(listor_namn.enemy_name))], rand.randint(4, 10), 
                        funktioner.halsa(rand.randint(5, 12)), 5)
        print(f"Du stötte på fienden {fiende.namn} med {fiende.hälsa} hp")
        if startattack == True:
            print("Du börjar striden!")
            while True:
                if funktioner.parera(fiende.försvar) == False:
                    hp_skillnad = fiende.hälsa
                    fiende.hälsa = funktioner.skada(karaktar_stats["kraft"], fiende.hälsa)
                    hp_skillnad = hp_skillnad - fiende.hälsa
                    if fiende.hälsa < 0:
                        fiende.hälsa = 0
                    print(f"Fienden tog {hp_skillnad} skada och har nu {fiende.hälsa} hp kvar")
                    if fiende.hälsa == 0:
                        print(f"Du besegrade {fiende.namn}!")
                        break
                else:
                    print(f"{fiende.namn} lyckades blockera attacken utan att ta skada")
                #FÖR SPELARE:
                if funktioner.parera(karaktar_stats["försvar"]) == False:
                    hp_skillnad2 = playerhp
                    playerhp = funktioner.skada(fiende.kraft, playerhp)
                    hp_skillnad2 = hp_skillnad2 - playerhp
                    if playerhp < 0:
                        playerhp = 0
                    print(f"Du tog {hp_skillnad2} skada och har nu {playerhp} hp kvar")
                    if playerhp == 0:
                        print(f"Du dog... GAME OVER")
                        break
                else:
                    print("Du lyckades blockera attacken utan att ta skada")
                print("")
        elif startattack == False:
            print("Fienden börjar striden!")
            while True:
                if funktioner.parera(karaktar_stats["försvar"]) == False:
                    hp_skillnad2 = playerhp
                    playerhp = funktioner.skada(fiende.kraft, playerhp)
                    hp_skillnad2 = hp_skillnad2 - playerhp
                    if playerhp < 0:
                        playerhp = 0
                    print(f"Du tog {hp_skillnad2} skada och har nu {playerhp} hp kvar")
                    if playerhp == 0:
                        print(f"Du dog... GAME OVER")
                        break
                else:
                    print("Du lyckades blockera attacken utan att ta skada")
                #FÖR FIENDER
                if funktioner.parera(fiende.försvar) == False:
                    hp_skillnad = fiende.hälsa
                    fiende.hälsa = funktioner.skada(karaktar_stats["kraft"], fiende.hälsa)
                    hp_skillnad = hp_skillnad - fiende.hälsa
                    if fiende.hälsa < 0:
                        fiende.hälsa = 0
                    print(f"Fienden tog {hp_skillnad} skada och har nu {fiende.hälsa} hp kvar")
                    if fiende.hälsa == 0:
                        print(f"Du besegrade {fiende.namn}!")
                        break
                else:
                    print(f"{fiende.namn} lyckades blockera attacken utan att ta skada")                
                print("")            
    else:
        pass
    aventyr = aventyr + 1