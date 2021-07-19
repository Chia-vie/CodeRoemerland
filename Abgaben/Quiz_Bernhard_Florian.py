print('Wilkommen zum Quiz')
x = 0
while True:
    antwortnumero = 'Mars'
    frage1 = input('Wie heißt der 4te Planet im Sonnensytem? ')
    if frage1 == antwortnumero:
        print('Gut Gemacht, du bekommst 1 Punkt für eine richtige Antwort!')
        x += 1
    else:
        print('Die Antwort ist leider nicht richtig!')

    antwort2 = 'Venus'
    frage2 = input('Was ist der heißeste Planet im Sonnensystem? ')
    if frage2 == antwort2:
        print('Gut Gemacht, du bekommst 1 Punkt für eine richtige Antwort!')
        x += 1
    else:
        print('Die Antwort ist leider nicht richtig!')

    antwort3 = 'Saturn'
    frage3 = input('Welcher Planet hat einen Ring? ')
    if frage3 == antwort3:
        print('Gut Gemacht, du bekommst 1 Punkt für eine richtige Antwort!')
        x += 1
    else:
        print('Die Antwort ist leider nicht richtig!')
    print(f'Dein Punktestand ist {x}.')
    nochmal = input('Nochmal? ')
    if nochmal != 'ja':
     break
