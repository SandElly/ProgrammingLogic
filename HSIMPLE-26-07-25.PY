#HERENCIA SIMPLE
"""
CLASE PADRE: Animal
    Atributos: Nombre
    Metodos: Caminar
CLASE HIJA: Perro
    Atributos: N/A
    Metodos: Sonido
"""

class Animal:
    def __init__(self,nombre): #CONTRUCTOR
        self.nombre = nombre #Atributo publico

    def Caminar(self): #METODO DE LA CLASE PADRE
        return "Este animal esta caminando"

class Perro(Animal): #Clase hija 
    def Sonido(self): #METODO DE LA CLASE HIJA
        return "Ladrido"
    
#-------INSTACIA (OBJETO)---------
Perro1 = Perro("Roy")
print(Perro1.Caminar()) #METODO HEREDADO DE MI CLASE PADRE
print(Perro1.Sonido()) #METODO DEFINIDO DE LA CLASE HIJA 


    