# ---------------------------
# POO: Universidad - Carrera - Estudiante
# ---------------------------

class Universidad:
    def __init__(self, nombre):            # Constructor
        self.nombre = nombre               # Atributo

    def __str__(self):
        return self.nombre


class Carrera:
    def __init__(self, nombre, especialidad):  # Constructor
        self.nombre = nombre                   # Atributo
        self.especialidad = especialidad       # Atributo

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Estudiante:
    def __init__(self, nombre, edad, carrera, universidad):  # Constructor
        self.nombre = nombre                                  # Atributos
        self.edad = edad
        self.carrera = carrera
        self.universidad = universidad

    def ficha(self):
        return (f"Estudiante: {self.nombre}\n"
                f"Edad: {self.edad}\n"
                f"Universidad: {self.universidad}\n"
                f"Carrera: {self.carrera}")

# ---------------------------
# Crear objetos y pedir la salida
# ---------------------------

uni = Universidad("UANL")
car = Carrera("Ingeniería en Sistemas", "Desarrollo de Software")

# El objeto debe llamarse 'persona' (como pide la libreta)
persona = Estudiante("Sandra Arrieta", 30, car, uni)

# Imprimir la especialidad y la edad (requisito)
print("Especialidad:", persona.carrera.especialidad)
print("Edad:", persona.edad)

# (Opcional) Imprimir ficha completa
# print(persona.ficha())