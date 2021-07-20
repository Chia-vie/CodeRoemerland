'''
author: Bernhard Wolf
date: 20.07.2021
Tic-Tac-Toe Spiel.
'''
Symbol = 'X'
wait = 1

Spielfeld = '''
    ___ ___ ___ 
    |_0_|_1_|_2_|
    |_3_|_4_|_5_|
    |_6_|_7_|_8_|
    '''
Spielzüge = ['0','1','2','3','4','5','6','7','8']
print('Hallo! Spielen wir Tic Tac Toe!')
print('Spieler*in 1, du bist X')
print('Spieler*in 2, du bist O')
print(f'''
Hier ist euer Spielfeld:
{Spielfeld}
Spieler*in 1, du beginnst. 
''')
while wait == 1:
    if (Spielzüge[0] == Spielzüge[1] == Spielzüge[2] or
    Spielzüge[3] == Spielzüge[4] == Spielzüge[5] or
    Spielzüge[6] == Spielzüge[7] == Spielzüge[8] or
    Spielzüge[0] == Spielzüge[3] == Spielzüge[6] or
    Spielzüge[1] == Spielzüge[4] == Spielzüge[7] or
    Spielzüge[2] == Spielzüge[5] == Spielzüge[8] or
    Spielzüge[0] == Spielzüge[4] == Spielzüge[8] or
    Spielzüge[2] == Spielzüge[4] == Spielzüge[6]):
        print(f'{Symbol} DU HAST GEWONNEN! GRATULIERE!')
        break

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
    Symbol = 'X'
    zug = input(f'Spieler*in 1, in welches Feld möchtest du dein {Symbol} setzen? \n')
    Spielfeld = Spielfeld.replace(zug,Symbol)
    Spielzüge[int(zug)] = Symbol
    print(Spielfeld)

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


