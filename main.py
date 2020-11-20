from constants import *
import os
from personaje import *
from batalla import *

_=os.system("cls")

print("""\
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|


                    """)

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
