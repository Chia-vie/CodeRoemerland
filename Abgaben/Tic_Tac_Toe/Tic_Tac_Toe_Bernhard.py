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
def Gewinn():
    if (Spielzüge[0] == Spielzüge[1] == Spielzüge[2] or
        Spielzüge[3] == Spielzüge[4] == Spielzüge[5] or
        Spielzüge[6] == Spielzüge[7] == Spielzüge[8] or
        Spielzüge[0] == Spielzüge[3] == Spielzüge[6] or
        Spielzüge[1] == Spielzüge[4] == Spielzüge[7] or
        Spielzüge[2] == Spielzüge[5] == Spielzüge[8] or
        Spielzüge[0] == Spielzüge[4] == Spielzüge[8] or
        Spielzüge[2] == Spielzüge[4] == Spielzüge[6]):
            print(f'{Symbol} DU HAST GEWONNEN! GRATULIERE!')
            exit(0)


def Spieler():
    global Spielfeld
    zug = input(f'Spieler*in, in welches Feld möchtest du dein {Symbol} setzen? \n')
    Spielfeld = Spielfeld.replace(zug,Symbol)
    Spielzüge[int(zug)] = Symbol
    print(Spielfeld)
def SpielerWechsel():
        global Symbol
        if Symbol == 'X':
            Symbol = 'O'
        else:
            Symbol = 'X'
while wait == 1:
    Gewinn()
    Spieler()
    SpielerWechsel()



