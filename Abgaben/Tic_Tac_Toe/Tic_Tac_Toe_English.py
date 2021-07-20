Symbol = 'X'
wait = 1
Spielfeld = '''
    ___ ___ ___ 
    |_0_|_1_|_2_|
    |_3_|_4_|_5_|
    |_6_|_7_|_8_|
    '''
Spielzüge = ['0','1','2','3','4','5','6','7','8']
print('Hello! Lets play tic-tac-toe!')
print('Player 1, you are X')
print('Player 2, you are O')
print(f'''
Here is your matchfield:
{Spielfeld}
Player 1 you start. 
''')
while wait == 1:
    zug = input(f'Where do you want to put your {Symbol}\n')
    Spielfeld = Spielfeld.replace(zug,Symbol)
    Spielzüge[int(zug)] = Symbol
    print(Spielfeld)
    if (Spielzüge[0] == Spielzüge[1] == Spielzüge[2] or
    Spielzüge[3] == Spielzüge[4] == Spielzüge[5] or
    Spielzüge[6] == Spielzüge[7] == Spielzüge[8] or
    Spielzüge[0] == Spielzüge[3] == Spielzüge[6] or
    Spielzüge[1] == Spielzüge[4] == Spielzüge[7] or
    Spielzüge[2] == Spielzüge[5] == Spielzüge[8] or
    Spielzüge[0] == Spielzüge[4] == Spielzüge[8] or
    Spielzüge[2] == Spielzüge[4] == Spielzüge[6]):
        print(f'{Symbol} Wins!')
        break
    if Symbol == 'X':
       Symbol = 'O'
    else:
        Symbol = 'X'


