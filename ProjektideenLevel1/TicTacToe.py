'''
author: Christine Ackerl
date: 20.07.2021
Das ist ein unvollständiges Tic-Tac-Toe Spiel.
Kannst du es vervollständigen?
'''

# So sieht das Spielfeld am Anfang aus.
# Der/die User*in kann ein Feld auswählen indem er/sie die jeweilige Zahl eingibt.
Spielfeld =  '''
 ___ ___ ___ 
|_1_|_2_|_3_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|
'''

# Hier werden alle Spielzüge gespeicher.
# Die Zahlen werden im Lauf des Spiels durch X oder O ersetzt.
Spielzüge = ['1','2','3','4','5','6','7','8','9']

# Begrüßung
print('Hallo! Spielen wir Tic Tac Toe!')
print('Spieler*in 1, du bist X')
print('Spieler*in 2, du bist O')

# Spielfeld ausgeben
print(f'''
Hier ist euer Spielfeld:
{Spielfeld}
Spieler*in 1, du beginnst. 
''')

# Zu Beginn ist das Symbol X
Symbol = 'X'
# Spielerin 1 macht einen Zug
zug = input(f'Spieler*in 1, in welches Feld möchtest du dein {Symbol} setzen? \n')
# Im Spielfeld wird die entsprechende Zahl durch ein X ersetzt
Spielfeld = Spielfeld.replace(zug,Symbol)
# Der Spielzug wird in der Liste der Spielzüge gespeichert
Spielzüge[int(zug)] = Symbol
# Neues Spielfeld ausgeben
print(Spielfeld)

# Jetzt müssen wir überprüfen ob der/die Spieler*in gewonnen hat
'''
Das sind alle möglichen Positionen der Symbole in denen die Spielerin gewinnt:

 ___ ___ ___     ___ ___ ___     ___ ___ ___ 
|_X_|_X_|_X_|   |___|___|___|   |___|___|___|
|___|___|___|   |_X_|_X_|_X_|   |___|___|___|
|___|___|___|   |___|___|___|   |_X_|_X_|_X_|

 ___ ___ ___     ___ ___ ___     ___ ___ ___     
|_X_|___|___|   |___|_X_|___|   |___|___|_X_|
|_X_|___|___|   |___|_X_|___|   |___|___|_X_|
|_X_|___|___|   |___|_X_|___|   |___|___|_X_|

 ___ ___ ___     ___ ___ ___ 
|_X_|___|___|   |___|___|_X_| 
|___|_X_|___|   |___|_X_|___|
|___|___|_X_|   |_X_|___|___|

Dasselbe gilt natürlich auch für 'O'.
'''
# Wir sehen in der Liste der Spielzüge nach ob eine der Gewinnmöglichkeiten zutrifft
if (Spielzüge[0] == Spielzüge[1] == Spielzüge[2] or
Spielzüge[3] == Spielzüge[4] == Spielzüge[5] or
Spielzüge[6] == Spielzüge[7] == Spielzüge[8] or
Spielzüge[0] == Spielzüge[3] == Spielzüge[6] or
Spielzüge[1] == Spielzüge[4] == Spielzüge[7] or
Spielzüge[2] == Spielzüge[5] == Spielzüge[8] or
Spielzüge[0] == Spielzüge[4] == Spielzüge[8] or
Spielzüge[2] == Spielzüge[4] == Spielzüge[6]):
    # Falls ja, hat der/die Spielerin gewonnen
    print(f'{Symbol} DU HAST GEWONNEN! GRATULIERE!')

# Wenn gerade Spieler*in 1 an der Reihe war kommt jetzt Spieler*in 2 dran, und umgekehrt
if Symbol == 'X':
    Symbol = 'O'
else:
    Symbol = 'X'

# Der/die Spielerin macht einen Zug
zug = input(f'Spieler*in 2, in welches Feld möchtest du dein {Symbol} setzen? \n')
# Spielfeld erneuern
Spielfeld=Spielfeld.replace(zug,Symbol)
# Spielzug speichern
Spielzüge[int(zug)] = Symbol
# Neues Spielfeld ausgeben
print(Spielfeld)


