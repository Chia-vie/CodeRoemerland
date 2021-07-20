import random
import string

# Das ist ein String der mögleiche Wörter enthält
wörter = 'Quizshow, Vollmond, Hollywood, Puderzucker, Dumpfbacke, Kuddelmuddel, Hund, Oper, Mond, Mars, Quiz, Auto, Zebra, Venus, Zwiebelsuppe, Nahrungsmittel, Finanzamt'
# String in Liste umwandeln
wörter = list(wörter.split(', '))
# Ein zufälliges Wort auswählen
wort = list(wörter[random.randint(0,len(wörter))].upper())
#print(wort)

# Gezeigt wird ein String aus lauter Leerzeichen.
wort_display=[]
möglich = set(string.ascii_lowercase)
geraten = set()
richtig = set()
for i,buchstabe in enumerate(wort):
    wort_display.append(' __ ')
    richtig.add(buchstabe)

print(*wort_display, sep=' ')
guess = input('Gib einen Buchstaben ein \n').upper()

if not guess in geraten:
    geraten.add(guess)
    möglich.discard(guess)
    if guess in richtig:
        print('Super!')
        ind = wort.index(guess)
        wort_display[ind]=''+guess+''
        print(*wort_display,sep=' ')
        richtig.discard(guess)
else:
    print(f'Du hast bereits den Buchstaben {guess} versucht.')









