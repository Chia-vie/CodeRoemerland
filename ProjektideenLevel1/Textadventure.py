'''
author: Christine Ackerl
date: 20.07.2021
So ähnlich könnte dein Text-Adventure beginnen.
Welches Abenteuer wartet auf uns?
'''

import time

# Begrüßung

print('''
       
      /| 
*    / |    *
    /  |
   (   |  *
    \\  |
     \\ |
   *  \\|     *
       v
''')
time.sleep(1)
print('Guten Abend.')
time.sleep(1)
print('Es wird bald dunkel und wir haben einen weiten Weg vor uns.')
time.sleep(1)
weiter = input('Bist du sicher, dass du mutig genug für dieses Abenteuer bist? \n').upper()
time.sleep(1)
if weiter != 'JA':
    print('Ich dachte mir schon, dass du nicht stark genug bist. Ich wünsche dir ein schönes Leben.')
    quit()
print('Gut. Ich bin beruhigt einen so mutigen Menschen an meiner Seite zu haben. Es wird sicher nicht einfach.')
name = input('Sage mir, wie darf ich dich ansprechen?\n')
time.sleep(1)
print(f'So soll es sein, {name}.')
time.sleep(1)
print('Komm, wir haben keine Zeit zu verlieren.')
time.sleep(1)
print('''
      / \\    
     /   \\
    /o    \\
www/ooo    \\www
     Y
''')
time.sleep(1)
pfad = input('Siehst du den Berg dort vorne? Was meinst du, sollen wir ihn überqueren (q) oder lieber herumgehen? (h)\n').upper()
time.sleep(1)
if pfad == 'Q':
    print('Das wird ein steiler Weg. Aber wir werden es schaffen.')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    wasser = input('Puh... Das war anstrengend. Ich brauche etwas zu trinken. Hast du Wasser dabei?\n').upper()
    time.sleep(1)
    if wasser != 'JA':
        idee=input('Oh nein... Was sollen wir nur machen?\n')
        time.sleep(1)
        print(f'Du meinst es hilft wenn wir {idee}?')
        time.sleep(1)
        print(f'Oh! Sieh nur! da vorne ist ein Brunnen!')
        time.sleep(1)
        print('''
           ___
          |  *
          |  *
         _|________
        |          |
        |          |
        |          |
        ''')
        trinken=input('Meinst du das Wasser ist in Ordnung?\n').upper()
        time.sleep(1)
        if trinken == 'JA':
            print('WÜRG')
            time.sleep(1)
            print('WORGXKWTIGJASDLFJ!!!')
            time.sleep(1)
            print('GAME OVER')
            quit()
elif pfad == 'H':
    print('Das wird uns viel Zeit kosten, aber vielleicht ist es besser so.')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('Wir sind fast angekommen.')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('Drei Stunden später')
    time.sleep(1)
    print('Es ist so dunkel, ich kann überhaupt nichts sehen.')
    time.sleep(1)
    print('Oh! Sieh nur! Da vorne ist ein Licht!')
    licht = input('Sollen wir hingehen? \n').upper()
    if licht == 'JA':
        print('PENG!')
        print('GAME OVER!')
        quit()
    else:
        time.sleep(1)
        print('Du hast wahrscheinlich recht. Lass uns lieber in der Dunkelheit bleiben.')



