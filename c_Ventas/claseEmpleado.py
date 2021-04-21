#jesus salvador valles maciel
#informatica
#Desarrollo de aplicaciones web
#practica_3.4_practicando Clases y Objetos
class Empleado:
    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre=nombre
        self.edad=edad
        self.legajo=legajo
        self.sueldoBase=sueldo
    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase-descuentos+bonos