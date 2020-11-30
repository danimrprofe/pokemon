from constants import *
import os
from personaje import *
from batalla import *
import partida
from habitacion import *

_=os.system("cls")

print("""\
______                                                   
| ___ \                                                  
| |_/ /__ _ _ __ ___   ___  _ __   __ _  ___  ___  _ __  
|    // _` | '_ ` _ \ / _ \| '_ \ / _` |/ _ \/ _ \| '_ \ 
| |\ \ (_| | | | | | | (_) | | | | (_| |  __/ (_) | | | |
\_| \_\__,_|_| |_| |_|\___/|_| |_|\__, |\___|\___/|_| |_|
                                   __/ |                 
                                  |___/       

                    """)

'''
print("Elige un tipo de personaje:")
print()



# Seleccionar un rol

roles = ["Mercenario","Mago", "Arquero"]

for rol in roles:
    print("[" + rol + "] " )

print("\n")
    
# Elegir un nombre
clasePersonaje = input("Escribe el rol que quieres:")
nombrePersonaje = input("Escribe un nombre para tu personaje: ")

_=os.system("cls")

personaje = Personaje(nombrePersonaje,clasePersonaje, 1)
'''







while True:
    hab = Habitacion()
    hab.describirhabitacion()
    while hab.direccion != 'moverse':
        hab.mostraracciones()
        hab.mirar()
    hab.moverse()
    hab.tomardecision()

enemigo = Personaje("Zombie", "monstruo", 4)




# Batalla1

battle = Batalla(personaje,enemigo)

def ask_command(personaje):
    command = None

    print()
    print("Ataques disponibles:")
    print()

    for ataque in personaje.ataques:
        print("* " + ataque.nombre)

    command = input("Que debería " + personaje.name+ " hacer?")



    return command

# Al comienzo hay que mostrar primero los stats de los personajes
battle.pintar_stats_personajes()

while not battle.is_finished():
    # Pedir los comandos a los entrenadores
    
    
    
    #command2 = ask_command (enemigo)

    turn = Turn()
    turn.command1 = ask_command (personaje)
    

    if turn.can_start():
        # Ejecutar turno
        battle.execute_turn(turn)
        battle.pintar_stats_personajes()
