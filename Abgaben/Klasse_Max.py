class Player():
    def __int__(self, name, mana, HP):
        self.name = name
        self.mana = mana
        self.HP = HP

    def Hose(self,farbe):
        self.Hose = f"{self.name}\'s Hose: {farbe}"
        return self.Hose

    def Jacke(self,farbe):
        self.Jacke = f"{self.name}\'s Jacke: {farbe}"
        return self.jacke

    def Kleidung(self):
        self.kleidung = self.Jacke + self.Hose
        return self.Kleidung

    def gun(self):
        self.gun = f"{self.name}\'s Gun"
        return self.gun

Spieler = Player("LeFoxy",128,24)
print(Spieler.name)
print(Spieler.Hose("schwarz"))
print(Spieler.Jacke("grün"))
print(Spieler.Kleidung())
print(Spieler.gun())
