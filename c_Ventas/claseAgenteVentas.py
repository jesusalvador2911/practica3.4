from claseEmpleado import *
from claseTripulante import *
from claseGerente import *

class AgenteVentas(Empleado):
    def __init__(self, nombre, edad, legajo, sueldo, mostrador):
        self.numeroMostrador=mostrador
        super().__init__(nombre, edad, legajo, sueldo)
#jesus salvador valles maciel
#informatica
#Desarrollo de aplicaciones web
#practica_3.4_practicando Clases y Objetos
