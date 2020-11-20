import random
import os
import math
from constants import *


class Turn:

    def __init__ (self):
        self.command1 = None
        self.command2 = None

    def can_start(self):
        return self.command1 is not None 

class Command:
    def __init__ (self, action):
        self.action = action



class Batalla:

    def __init__ (self, heroe, enemigo):
        self.heroe = heroe
        self.enemigo = enemigo
        self.actual_turn = 0

    def is_finished(self):
        finished = self.heroe.current_hp <=0 or self.enemigo.current_hp <=0
        if finished:
            self.print_winner()
        return finished

    def print_winner(self):
        if self.heroe.current_hp <= 0 < self.enemigo.current_hp: 
            print("Ha ganado " + self.heroe.name)
        elif self.enemigo.current_hp <= 0 < self.heroe.current_hp:
            print("Ha ganado " + self.enemigo.name)
        else:
            print("Doble KO")

    def calculo_danyo(self, heroe, enemigo, critico):

        critico = False
        danyo_total = 0

        esCritico = random.randint(0,5)
        if esCritico == 1:
            critico = True
            danyo_total = math.floor(5*self.heroe.Str)
            enemigo.current_hp -= danyo_total
            
        else:
            variacion = random.randint(-5,5)
            danyo_total = math.floor(heroe.Str*4 + variacion)
            enemigo.current_hp -= danyo_total 
        return danyo_total

    def execute_turn(self, turn):
        
        
        _=os.system("cls")
        
        critico = False
        danyo_total = self.calculo_danyo(self.heroe, self.enemigo, critico)
        if critico:
            print("ATAQUE CRITICO!!")
        print(self.enemigo.name + " ha perdido " + str(danyo_total) + " puntos de vida!")
        

        self.actual_turn += 1

        



    def pinta_vida(self, personaje):
        actual = personaje.current_hp
        total = personaje.HP

        if actual >=0:
            porcent = math.floor(actual*10/total)
        else:
            porcent = 0
        
        print(" [ ", end = '')

        for iguales in range(porcent):
            print("=", end = '')

        for vacios in range(10-iguales):
            print(" ", end = '')

        print("] ")
        
        print("LvL:  ", personaje.level)
        print("HP:  ",actual, " / ", total)
        print("MP:  ",actual, " / ", total)
        print("")


    def pintar_stats_personajes(self):
        print(self.heroe.name + " tiene " + str(self.heroe.current_hp))
        self.pinta_vida(self.heroe)
        print(self.enemigo.name + " tiene " + str(self.enemigo.current_hp))
        self.pinta_vida(self.enemigo)
