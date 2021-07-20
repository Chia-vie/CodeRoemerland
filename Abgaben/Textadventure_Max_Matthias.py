'''
author: Christine Ackerl
date: 20.07.2021
So ähnlich könnte dein Text-Adventure beginnen.
Welches Abenteuer wartet auf uns?
'''

import time

# Begrüßung

print('''
       
       
*         *
      
        *
    
  --------___
              ------->
   *     *
       v58
''')
time.sleep(1)
print('Moin Leude Trymax hier.')
time.sleep(1)
print('Es wird bald Nacht und wir haben einen weiten Weg vor uns.')
time.sleep(1)
weiter = input('Bist du sicher, dass du das wirklich durchziehen möchtest? \n').upper()
time.sleep(1)
if weiter != 'JA':
    print('Ich glaub mein Pfeif schweint ist das dein ernst!? Dann halt nicht tschuss.')
    quit()
print('Gut. Ich bin beruhigt einen so menschlichen Wesen an meiner Seite zu haben. Es wird sicher nicht einfach.')
name = input('Sage mir, wie darf ich dich ansprechen?\n')
time.sleep(1)
print(f'So soll es sein,{name}.')
time.sleep(1)
print('Komm, wir haben keine Zeit zu verlieren.')
time.sleep(1)
print('''
      / \\    
     /   \\
    /o    \\ /\\
www/ooo      \\www
     Y
''')
time.sleep(1)
pfad = input('Erkenst du auch den Berg dort vorne? Sollen wir ihn schnell überqueren (q) oder lieber herumgehen aber dass wurde länger dauern? (h)\n').upper()
time.sleep(1)
if pfad == 'Q':
    print('Das wird ein steiler Weg. Aber wir werden es schaffen.')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    wasser = input('Puh... Das war anstrengend. Ich brauche etwas zu Essen. Hast du Essen dabei?\n').upper()
    time.sleep(1)
    if wasser != 'JA':
        idee=input('Oh nein... Was sollen wir nur machen?\n').lower()
        if idee == 'canibalismus':
            print(f"Eine fabelhafte Idee {name}")
            time.sleep(1)
            print("Erzähler: Und dann wurdest du gegessen")
            time.sleep(1)
            print("GAME OVER")
            quit()
        time.sleep(1)
        print(f'Du meinst es hilft wenn wir {idee}?')
        time.sleep(1)
        print(f'Oh! Sieh nur! da vorne ist ein Beerenstrauch!')
        time.sleep(1)
        print('''
              ,-.
           ,-( O )-.
        ,-(_  O O __)
        (_  O )  __)-'
          `-(__O_)-'
             |__|
        ''')
        trinken=input('Meinst du die Beeren ist in nicht giftig?\n').upper()
        time.sleep(1)
        if trinken == 'JA':
            print(f'{name}: Ich glaube nicht')
            print('Hmmm Lecker')
            time.sleep(1)
            print('*Stirbt*')
            time.sleep(1)
            print('GAME OVER')
            quit()
        else:
            print("Ich probiere sie trotzdem")
            time.sleep(1)
            print("Hmmm Lecker")
            time.sleep(1)
            print("*Stirbt*")
            time.sleep(1)
            print("GAME OVER")
            quit()
    elif wasser == 'JA':
        quit
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
        time.sleep(2)
        print("???:reeeeeeeeeeeeeeeeee")
        print(f"Schau mal {name} da lauf jemand mit einer Schaufel auf uns zu")
        time.sleep(1)
        print("Warte mal hat er es auf uns abgesehen?")
        time.sleep(1)
        laufen = input(f"SCHELL {name} WAS SOLLEN WIR TUN? WEG LAUFEN (L) ODER KÄMPFEN (K) \n").upper()
        if laufen == "K":
            print("???:REEEEEEEEEEEEEEEEEEEEEEEEEE")
            time.sleep(1)
            print(f"""Erzähler:Der Verrückte mit der schaufel lief einen Hügel hinauf
sprang und schlug {name} mit der Schaufel in den Boden""")
            print("GAME OVER")
            quit()
        else:
            print("Erzähler:Ihr lauft in eine Höhle und versteckt euch darin")
            time.sleep(1)
            ende = input(f"""Hey {name} ich glaube wir haben ihn abgehängt.
Sollen wir uns wo anders verstecken? \n""").upper()
            if ende == "JA":
                print("Mist er hat uns gefunden")
                print("*BONK*")
                print("GAME OVER")
                quit()
            else:
                print("Ok lass uns tiefer in die Hölle gehen")
                time.sleep(1)
                print("""*tap*
                *tap*
                *tap*
                """)
                time.sleep(1)
                print("WOW. Schau dir diesen Schatz an!!")
                print("Toll du hast gewonnen")
