#HERENCIA HIBIRDA
"""
CLASE PADRE: MOTOR
    Atributos: N/A
    Metodos: ENCENDER MOTOR
CLASE HIJA 1: RUEDAS
    Atributos: N/A
    Metodos: RODANDO
CLASE HIJA 2: AUTO
    Atributos: N/A
    Metodos: CONDUCIR
CLASE HIJA 3: AUTO ELECTRICO
    Atributos: N/A
    Metodos: CARGAR
"""

class Motor:
    def Encender(self):
        return "Encendiendo motor...."

class Ruedas(Motor):
    def Rodando(self):
        return "Ruedas rodando"

class Auto(Motor):
    def Conducir(self):
        return "Conduciendo auto"
    
class AutoElectrico(Ruedas,Auto):
    def Cargar(self):
        return "Cargando...."

#----------Instancia-----------
Tesla =AutoElectrico()


print(Tesla.Encender()) #metodo heredado de la clase padre motor
print(Tesla.Rodando())#metodo heredado de la clase hija ruedas
print(Tesla.Conducir())#metodo heredado de la clase hija auto
print(Tesla.Cargar())#metodo heredado de la clase hija autoelectrico


