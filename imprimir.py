import sys
import time
def imprimir(cadena):
    for letter in cadena:
        sys.stdout.write(letter)
        time.sleep(.1)