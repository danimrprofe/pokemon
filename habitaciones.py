from habitacion import Habitacion

class Colegio(Habitacion):
    nombre = "Colegio"
    direccion =""            
    siguientehabitacion=""
    habitacionescontiguas={
        'izquierda' : 'consergería',
        'derecha' : 'baño',
        'delante' : 'pasillo',
        'detras' : 'plaza',
    }
    descripcionentrada =  'Entras en lo que parece el hall del colegio. Un largo pasillo al frente sin luz\n'\
            'Parece que hace tiempo que nadie entra aquí.\n'\
            
class Plaza(Habitacion):
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