#HERENCIA MULTIPLE
"""
CLASE PADRE 1: Volador
    Atributos: N/A
    Metodos: Volar
CLASE PADRE 2: Nadador
    Atributos: N/A
    Metodos: Nadar
CLASE HIJA 1: Pato
    Atributos: N/A
    Metodos: N/A
"""

class Volador:
    def Volar(self):
        return "Puedo volar"   #en la vida real meretorna un valor una cantidad
    
class Nadador:
    def Nadar(self):
        return "Puedo nadar"
    
class Pato(Volador,Nadador):
    pass   #como no tiene atributo y metodo se pasa

#-----Instancia-----
Animal = Pato()  #como no tiene atributo se queda vacio
print(Animal.Volar())  #ES UN METOD HEREDADO DE LA CLASE PADRE VOLADOR 1
print(Animal.Nadar()) #CLASE PADRE NADAR 2

