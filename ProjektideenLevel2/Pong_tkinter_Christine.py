'''
author: Christine Ackerl
date: 21. 07.2021
Ein einfaches Spiel mit tkinter
'''

import tkinter as tk
import random

# Wir erstellen ein Fenster

class Ball:
    def __init__(self, spielfeld, schlaeger):
        self.spielfeld = spielfeld
        self.schlaeger = schlaeger
        self.form = spielfeld.create_oval(10, 10, 30, 30, fill='white') # (x0,y0,x1,y1)
        self.spielfeld.move(self.form, 200, 100)
        self.xspeed = random.randrange(-3,3)#  x-ache Geschwindigkeit random
        self.yspeed = -1  #y-ache Geschwindigkeit
        self.hit_bottom = False
        self.score = 0

    def abprallen(self):
        self.spielfeld.move(self.form, self.xspeed, self.yspeed)
        position = self.spielfeld.coords(self.form)
        if position[1] <= 0: # trifft oberre Seite
            self.yspeed = 3 # nach unten
        if position[3] >= 400: # ist hinuntergefallen
            self.hit_bottom = True
        if position[0] <= 0: # trifft linke Seite ,pos[0] nach rechts
            self.xspeed = 3 # nach rechts
        if position[2] >= 500: # trifft rechte S
            self.xspeed = -3 # nach links
        if self.hit_paddle(position) == True: # trifft Schläger
            self.yspeed = -3 # nach oben
            self.xspeed = random.randrange(-3,3) # zufallszahl nach links oder rechts
            self.score = self.score + 1 # Punktestand erhöht

    def hit_paddle(self, pos):
        paddle_pos = self.spielfeld.coords(self.schlaeger.form)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

class Schlaeger:
    def __init__(self,spielfeld):
        self.spielfeld = spielfeld
        self.form = spielfeld.create_rectangle(0,0,100,10,fill='black')
        self.spielfeld.move(self.form, 200,350)
        self.spielfeld.bind_all('<KeyPress-Left>', self.nachlinks)
        self.spielfeld.bind_all('<KeyPress-Right>', self.nachrechts)
        self.xspeed=0

    def hinher(self):
        self.spielfeld.move(self.form, self.xspeed, 0)
        pos = self.spielfeld.coords(self.form)
        # wenn Paddle trift rechte oder linke seite der Wand  wurde dann hier Geschwindigkeit
        # null defeniert
        if pos[0] <= 0:
            self.xspeed = 0
        if pos[2] >= 500:
            self.xspeed = 0

    def nachrechts(self, evt):
        self.xspeed = 3
    def nachlinks(self, evt):
        self.xspeed = -3

fenster = tk.Tk()
fenster.title('Volleyball')
spielfeld = tk.Canvas(fenster, width=500, height=400, bd=0, bg='royalblue')
spielfeld.pack()
Schlaeger = Schlaeger(spielfeld)
Ball = Ball(spielfeld, Schlaeger)
while Ball.hit_bottom == False:
    Schlaeger.hinher()
    Ball.abprallen()
    fenster.update_idletasks()
    fenster.update()


fenster.mainloop()
