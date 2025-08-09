#HERENCIA JERARQUICA
"""
CLASE PADRE: VEHICULO
    Atributos: N/A
    Metodos: ENCENDER
CLASE HIJA 1: AUTO
    Atributos: N/A
    Metodos: MANEJAR
CLASE HIJA 2: MOTOCLICLETA
    Atributos: N/A
    Metodos: CONDUCIR
"""
class Vehiculo:
    def Encender(self):
        return "Encendiendo vehiculo"
    
class Auto(Vehiculo):
    def Manejar(self):
        return "Manejando auto"
    
class Motocicleta(Vehiculo):
    def Conducir(self):
        return "Conduciendo motoclicleta"

#------instancia-----
Auto1 = Auto()
print(Auto1.Encender()) #metodo herado de la clase padre
print(Auto1.Manejar())#metodo definido de la clase hija 1

Moto1 = Motocicleta()
print(Moto1.Encender())#metodo herado de la clase padre
print(Moto1.Conducir())#metodo definido de la clase hija 2


