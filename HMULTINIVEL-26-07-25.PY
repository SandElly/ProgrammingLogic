#HERENCIA MULTINIVEL
"""
CLASE PADRE: ABUELO
    Atributos: N/A
    Metodos: SABIDURIA
CLASE HIJA 1: PADRE
    Atributos: N/A
    Metodos: EXPERIENCIA
CLASE HIJA 2: HIJO
    Atributos: N/A
    Metodos: JUVENTUD
"""
class Abuelo:
    def Sabiduria(self):
        return "EL QUE MADRUGA DIOS LO AYUDA"

class Padre(Abuelo):
    def Experiencia(self):
        return "YA MADRUGO Y NO AYUDO"

class Hijo(Padre):
    def Juventud(self):
        return "SE QUEDO DORMIDO"
#------INTANCIAS----
Arturo = Hijo()
print(Arturo.Sabiduria()) #metodo heredado de la clase padee abuelo
print(Arturo.Experiencia())#expereencia es un metodo heredado de la clase hija 1
print(Arturo.Juventud())#metodo heredado clase hija 2




