#'Authors Max,Hemma
# Date: 19.07.2021
# '
a = input("""Wann wurde Minecraft erfunden
>""")
if 2009 == int(a):
    print("Richtig")
    f1 = 1
else:
    print("Falsch")
    f1 = 0
b = input("""Wie viele leben hat eine Eisengohlem
>""")
if int(b) == 50:
    print("Richtig")
    f2 = 1
else:
    print("Falsch")
    f2 = 0
c = input("""Welches dieser Item hat kein Lichtlevel
        1. Brauner Pilz
        2. Verzauberungs Tisch
        3. Diamant Block
>""")
if int(c) == 1:
    print("Richtig")
    f3 = 1
else:
    print("Falsch")
    f3 = 0
score = f1 + f2 + f3
print(f"Deine Punktezahl is {score}")
