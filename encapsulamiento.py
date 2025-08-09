#Definir una clase llamada "estudiante" con:
#Atributos: Nombre(privado), edad.
#Metodos: Necesarios para vialidad y la edad  antes ce asignarla.
#NOTAAAA: LA EDAD TIENE QUE SER MAYO DE 19 PERO MENOR A 100.
class Estudiante: #CLASE
    def __init__(self, Nombre, Edad): #CONSTRUCTOOOR
        self.__Nombre = Nombre #ATRIBUTO PRIVADO
        self.SetEdad(Edad) #modificar esta funcion con Set

#obtener mi edad
    def GetEdad(self): #inicializador es self
        return self.__Edad 
    def SetEdad(self, Edad):
        if 0 < Edad < 100: 
            self.__Edad = Edad
        #si 0 es menor de edad y edad es mayor a 100.... se modificara la edad
        else:
            print("Edad no Valida")
        
#INSTANCIAS
Mateo = Estudiante("Mateo", 20)
print(Mateo.GetEdad()) #quiero que me traiga.. la edad, 20

Mateo.SetEdad(120) #cambiar edad
print(Mateo.GetEdad())