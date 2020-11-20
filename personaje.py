import math
from constants import *
from ataque import *

class Personaje:

    def __init__ (self, nombrePersonaje, clasePersonaje, nivel):
        self.name = nombrePersonaje
        self.clase = clasePersonaje

        self.level = nivel

        # Parámetros base        
        self.SpdBase = 5
        self.StrBase = 10
        self.MagBase = 10
        self.HPMod = 250
        self.MPMod = 200

        if clasePersonaje == "Mercenario":
            self.StrBase += 5
            self.MagBase -= 5
        elif clasePersonaje == "Mago":
            self.StrBase -= 5
            self.MagBase += 5
        elif clasePersonaje == "Arquero":
            self.StrBase -= 5
            self.MagBase += 5
        
        # Parámetros variables con el nivel
        self.Spd = self.SpdBase + (self.level*1/10)
        self.Str = self.StrBase + (self.level*3/10)
        self.Mag = self.MagBase + (self.level*3/10)
        self.HP = math.floor(self.Str + self.HPMod*self.level/5)
        self.MP = math.floor(self.Mag + self.MPMod*self.level/100)

 
        
        self.ataques =[] #vector de ataques
        self.stats = {}
        self.current_status = 0
        self.current_hp = self.HP

        # Configuración de ataques

        # Ataques

        if clasePersonaje == "Mercenario":
            self.ataques = [Ataque("Ataque físico", PHYSICAL, 5)]
        elif clasePersonaje == "Mago":
            self.ataques = [Ataque("Magia",  SPECIAL, 5)]            
        elif clasePersonaje == "Arquero":
            self.ataques = [Ataque("Disparo",  PHYSICAL, 5)]
        self.ataques + [Ataque("Objetos",  SPECIAL, 5)]
