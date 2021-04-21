#jesus salvador valles maciel
#informatica
#Desarrollo de aplicaciones web
#practica_3.4_practicando Clases y Objetos


from claseEmpleado import *
from claseAgenteVentas import *
from claseTripulante import *
from claseGerente import *


Luis = Empleado("Luis", 21, "4523A", 1500)
print(Luis.nombre)
print(Luis.calcularSueldo(1000,500))

Raul = Gerente("Raul", 39, "732A", 3800)
print(Raul.nombre)
print(Raul.calcularSueldo(100,6000))