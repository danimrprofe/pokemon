from ascii import *
from imprimir import *

class Habitacion:
    nombre = "plaza"
    direccion =""            
    siguientehabitacion=""
    habitacionescontiguas={
        'izquierda' : 'hospital',
        'derecha' : 'colegio',
        'delante' : 'carretera',
    }
    descripcionentrada =  'Abres los ojos. Ves un cielo borroso lleno de nubes. De repente, una luz cegadora lo llena todo.\n'\
            'Poco a poco consigues volver a ponerte en pie. \nEstás en una plaza, nadie a tu alrededor.\n'\
            'La lluvia cae incesante. Es mejor ponerse a cubierto'
    def __init__ (self):
        print("nueva habitacion")
    def describirhabitacion(self):
        imprimeEntreLineas(self.descripcionentrada)
    def mostraracciones(self):
        print(">> ¿Que haces?")
        print("+------------------------------------+")
        print("Mirar a la [izquierda]")
        print("Mirar a la [derecha]")
        print("Mirar [delante]")
        print("[moverse]")
        self.direccion = input()
    def moverse(self):
        print(">> ¿Dónde quieres ir")
        print("+------------------------------------+")
        print("Ir hacia la [izquierda]")
        print("Ir hacia la [derecha] ")
        print("Ir hacia [delante]")
        self.direccion = input()
    def mirar(self):
        
        if self.direccion == "izquierda":
            imprimir("Mirando a la izquierda, ves un edificio muy antiguo, casi en ruinas. Parece un antiguo colegio ya abandonado")
            pintar_colegio()
        elif self.direccion == "delante":
            imprimir("Enfrente, ves una carretera. No pasa ningún coche, no se ve a nadie. Quizá podría ir a ver si pasa alguien")
        elif self.direccion == "derecha":
            imprimir("Mirando a la derecha, ves una carretera. No pasa ningún coche, no se ve a nadie. Quizá podría ir a ver si pasa alguien")
    def tomardecision(self):
        self.siguientehabitacion = self.habitacionescontiguas[self.direccion]
        print("Entras en",self.siguientehabitacion)