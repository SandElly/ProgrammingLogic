class Estudiante:
    def _init_(self, Nombre, Edad):  # constructor
        self._nombre = Nombre          # atributo privado
        self.setEdad(Edad)             # usar setter para asignar edad

    def getEdad(self):
        return self._edad              # usa _edad, ya inicializada por el setter

    def setEdad(self, Edad):
        if 0 < Edad < 100:
            self._edad = Edad
        else:
            print("Edad no válida")


# Instancias
Mateo = Estudiante("Mateo", 20)
print(Mateo.getEdad())     #  Imprime 20

Mateo.setEdad(120)         #  Edad no válida
print(Mateo.getEdad())     #  Sigue siendo 20