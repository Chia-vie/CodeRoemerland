'''
author: Christine Ackerl
date: 18. 07. 2021
Dieses Script berechnet die Fläche eines Kreises bei gegebenem Radius.
Es enthält einige Fehler. Findest du sie?
Schreibe die jeweiligen Fehlermeldungen als Kommentare neben die jeweilige Zeile und korrigiere den Code.
'''

radius = float(input('Gib den Radius eines Kreises in cm ein! '))
pi = 3.1415692
flaeche = radius ** 2 * pi
print (f'Die Fläche des Kreises beträgt  {flaeche}  Quadratzentimeter')
