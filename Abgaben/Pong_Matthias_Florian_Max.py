'''
author: Florian, Matthias, Max
date: 21.7.2021
Ein Pong Spiel bei dem man verliert wenn der Ball den Boden berührt.
'''

import tkinter as tk
import random
import pygame as pg
#bild = ImageTk.PhotoImage(file = 'space.png')
from pygame import mixer

#Background Music
#mixer.music.load('Hard.wav')
#mixer.music.play(-1)

class Ball:
    def __init__(self, spielfeld, schlaeger):
        self.spielfeld = spielfeld
        self.schlaeger = schlaeger
        self.form = spielfeld.create_oval(10, 10, 30, 30, fill='magenta')
        self.spielfeld.move(self.form, 200, 100)
        self.xspeed = random.randrange(-3,3) # x-ache Geschwindigkeit random
        self.yspeed = 0.1 # Das ist die y-fache Geschwindigkeit
        self.hit_bottom = False
        self.score = 0

    def abprallen(self):
        self.spielfeld.move(self.form, self.xspeed, self.yspeed)
        position = self.spielfeld.coords(self.form)
        if position[1] <= 0:  # hat die obere Seite getroffen
            self.yspeed = 0.1 # nach unten
        if position[3] >= 400: # Der Ball isst hinuntergefallen
            self.hit_bottom = True
        if position[0] <= 0: # Trifft linke Seite
            self.xspeed = 0.1 # Er geht nach rechts
        if position[2] >= 500: # Der Ball trifft die rechte Seite
            self.xspeed = -0.1 # Der Ball geht nach links
        if self.hit_paddle(position) == True: # Der Ball trifft den Schläger
            self.yspeed = -0.1 # Der Ball geht nach oben
            self.xspeed = random.randrange(-3,3) # Zufallszahl nach rechts oder links
            self.score = self.score + 1 # Punktestand ist erhöht worden
    def hit_paddle(self, pos):
        paddle_pos = self.spielfeld.coords(self.schlaeger.form)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

class Schlaeger:
    def __init__(self,spielfeld):
        self.spielfeld = spielfeld
        self.form = spielfeld.create_rectangle(0,0,50,10,fill='cyan')
        self.spielfeld.move(self.form, 200,350)
        self.spielfeld.bind_all('<a>', self.nachlinks)
        self.spielfeld.bind_all('<d>', self.nachrechts)
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
        self.xspeed = 0.1
    def nachlinks(self, evt):
        self.xspeed = -0.1


fenster = tk.Tk()
bild = tk.PhotoImage(file='Space.png')
fenster.title('Erstes Spiel "Ping Pong')
spielfeld = tk.Canvas(fenster, width=500, height=400, bd=0, bg='purple3')
spielfeld.pack()
spielfeld.create_image(250,250, image=bild, anchor = 'center')
Schlaeger = Schlaeger(spielfeld)
Ball = Ball(spielfeld, Schlaeger)
while Ball.hit_bottom == False:
    Schlaeger.hinher()
    Ball.abprallen()
    fenster.update_idletasks()
    fenster.update()

fenster.mainloop()

