# Das ist Hangman von Florian
import string
from colorama import Fore
from colorama import init as colorama_init
import random
# Das ist ein String der mögleiche Wörter enthält
wörter = 'Käse, Pluto, Videospiel, Computer, Mund, Klassenraum, Kek, Fensterscheibe, Dachschaden, Bonuspunkt, Kamera, Gabel, Heizung, Raum, Fortnite, Kabel, Apfel, Kiwi, Mango, Tastatur, Zebra, Schalosien, Bombe, Hut, Chips, Burger, Monitor, Maus, Tisch, Fernbedienung, Lade, Sofa, Wolkenkrater, Weihnachtsbaum, Internet, Zahl, Name, Keramikteller, Berpackung, Lampe, Kasten, Schokoriegel, Uhr, Uhrenturm, Stadt, Hauptplatz, Gesetz, Präsident, Amerika, Deutschland, Auto, Polizei, Schusswaffe'
# String in Liste umwandeln
wörter = list(wörter.split(', '))
# Ein zufälliges Wort auswählen
wort = list(wörter[random.randint(0,len(wörter))].upper())
leben = 9
# Gezeigt wird ein String aus lauter Leerzeichen.
wort_display=[]
möglich = set(string.ascii_lowercase)
geraten = set()
richtig = set()

for i,buchstabe in enumerate(wort):
    wort_display.append(Fore.MAGENTA + '__')
    richtig.add(buchstabe)
while True:
    print(*wort_display, sep=' ')
    guess = input(Fore.CYAN + 'Gib einen Buchstaben ein \n').upper()

    if not guess in geraten:
        geraten.add(guess)
        möglich.discard(guess)
        if guess in richtig:
            print(Fore.GREEN + 'Super! Der Buchstabe war richtig!')
            Indices = [n for n,letter in enumerate(wort) if letter == guess]
            for ind in Indices:
                wort_display[ind]=''+guess+''
            print(*wort_display,sep=' ')
            richtig.discard(guess)
        else:
            print(Fore.RED + 'Diesen Buchstaben enthält dieses Wort leider nicht.')
            leben -= 1
    else:
        print(Fore.YELLOW + 'Den Buchstaben {guess} hast du schon benutzt.')
    if leben == 0:
        break
print(Fore.LIGHTBLUE_EX + f'''
--------
|      |
|      o
|     \|/
|      T
|    /   \\
Du hast verloren
Das wort war {wort}
''')
