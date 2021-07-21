import tkinter as tk

class Sternchen():
    def __init__(self,feld):
        self.feld=feld
        self.points= [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
        self.form = feld.create_polygon(self.points,fill='red',width=2,outline='purple')
        self.feld.move(self.form, 200, 100)
        self.x = 0
        self.y = 0
        self.istinnerhalb = True
        self.move()

    def innerhalb(self):
        self.position = self.feld.coords(self.form)
        if (self.position[0]<=0
            or self.position[5]<=0
            or self.position[0]>=500
            or self.position[5]>=400):
            self.istinnerhalb = False
        else:
            self.istinnerhalb = True

    def move(self):
        if not self.istinnerhalb:
            self.x = 0
            self.y = 0
        #self.position = self.feld.coords(self.form)
        self.feld.move(self.form, self.x, self.y)
        self.feld.after(100, self.move)
        self.innerhalb()
        #print(self.position)

    # for motion in negative x direction
    def left(self):
        if not self.istinnerhalb and not self.position[0]<=0:
            self.istinnerhalb = True
        #print(event.keysym)
        self.x = -5
        self.y = 0

    # for motion in positive x direction
    def right(self):
        if not self.istinnerhalb and not self.position[0]>=500:
            self.istinnerhalb = True
        #print(event.keysym)
        self.x = 5
        self.y = 0

    # for motion in positive y direction
    def up(self):
        if not self.istinnerhalb and not self.position[5]<=0:
            self.istinnerhalb = True
        #print(event.keysym)
        self.x = 0
        self.y = -5

    # for motion in negative y direction
    def down(self):
        if not self.istinnerhalb and not self.position[5]>=500:
            self.istinnerhalb = True
        #print(event.keysym)
        self.x = 0
        self.y = 5

class Kreis():
    def __init__(self,feld):
        self.feld=feld
        #self.points= [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
        self.form = feld.create_oval(0,0,10,10,fill='red',width=2,outline='purple')
        self.feld.move(self.form, 100, 100)
        self.x = 0
        self.y = 0
        self.move()

    def move(self):
        self.feld.move(self.form, self.x, self.y)
        self.feld.after(100, self.move)

    # for motion in negative x direction
    def left(self):
        self.x = -5
        self.y = 0

    # for motion in positive x direction
    def right(self):
        self.x = 5
        self.y = 0

    # for motion in positive y direction
    def up(self):
        self.x = 0
        self.y = -5

    # for motion in negative y direction
    def down(self):
        self.x = 0
        self.y = 5


fenster = tk.Tk()

fenster.config(bg = 'royalblue')
fenster.title('Eine Einführung in tkinter')
feld = tk.Canvas(fenster, width=500, height=400, bd=0, bg='pale turquoise')
feld.pack()
stern = Sternchen(feld)
kreis = Kreis(feld)
fenster.bind("<KeyPress-Left>", lambda e: stern.left())
fenster.bind("<KeyPress-Right>", lambda e: stern.right())
fenster.bind('<KeyPress-Up>', lambda e: stern.up())
fenster.bind("<KeyPress-Down>", lambda e: stern.down())


fenster.bind("a", lambda e: kreis.left())
fenster.bind("d", lambda e: kreis.right())
fenster.bind('w', lambda e: kreis.up())
fenster.bind("s", lambda e: kreis.down())
fenster.update()
fenster.mainloop()