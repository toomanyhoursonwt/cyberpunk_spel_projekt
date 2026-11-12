import random as rand
import math
namn_karaktar = input("Vad är din karaktärs namn? ")
karaktar_stats = {
    "kraft":10, #direkt påverkan på dmg
    "hälsa":10, #direkt påverkan på, start 100 hp
    "medvetenhet":10, #chans att börja turn först
    "försvar":5, #block chans 
}

#fråga om input med x poaäng som man kan tilldela mellan stats