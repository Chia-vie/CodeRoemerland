'''
Autor: Kilian Mayerhofer-Bollek
Datum 21.7.2021
Ein einfaches Spiel mit tkinter
'''
import tkinter as tk
import random




class Ball:
    def __init__(self,spielfeld,schleager):
        self.spielfeld = spielfeld
        self.schleager = schleager
        self.form=spielfeld.create_oval(10,10,40,40,fill='green')
        self.xges=random.uniform(0,0.1)
        self.yges=-0.1
        self.hit_bottom =False


    def abprallen(self):
        self.spielfeld.move(self.form,self.xges,self.yges)
        position=self.spielfeld.coords(self.form)
        if position[1]<=0:
            self.yges=0.1
        if position[3]>=400:
            self.hit_bottom=True
        if position[0]<= 0:
            self.xges=0.1
        if position[2]>=500:
            self.xges=-0.1
        if self.hit_paddle(position) == True:
            self.yges = -0.1
            self.xges = random.uniform(-1,1)


    def hit_paddle(self, pos):
        paddle_pos = self.spielfeld.coords(self.schleager.form)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


class Schlaeger:
    def __init__(self,spielfeld):
        self.spielfeld=spielfeld
        self.form=spielfeld.create_rectangle(0,0,120,10,fill='black')
        self.spielfeld.move(self.form,200,350)
        self.spielfeld.bind_all('a',self.links)
        self.spielfeld.bind_all('d',self.rechts)
        self.xges=0

    def hinher(self):
        self.spielfeld.move(self.form, self.xges, 0)
        pos= self.spielfeld.coords(self.form)
        if pos[0]<= 0:
            self.xges=0
        if pos [2]>=500:
            self.xges=0

    def links(self,event):
        self.xges=-0.1
        self.yges=0

    def rechts(self,event):
        self.xges=0.1
        self.yges=0


fenster =tk.Tk()
fenster.title('Ping Pong')
spielfeld=tk.Canvas(fenster, width=500, height=400, bd=0, bg ='royalblue')
spielfeld.pack()
Schlaeger=Schlaeger(spielfeld)
Ball=Ball(spielfeld,Schlaeger)
while Ball.hit_bottom == False:
    Schlaeger.hinher()
    Ball.abprallen()
    fenster.update_idletasks()
    fenster.update()

fenster.mainloop()









