# CLASE CON ATRIBUTOS PUBLICOS
# CLASE COCHE
# ATRIBUTOS: MARCA, MODELO

class Coche:
    def __init__(self, marca, modelo):  # Constructor
        self.marca = marca              # Atributo público
        self.modelo = modelo            # Atributo público

    def MostrarInformacion(self):       # Método para mostrar info
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# CREACIÓN DE OBJETO
coche1 = Coche("BMW","X6")
coche1.MostrarInformacion()
#CLASE CON ATRIBUTOS PROTEGIDOS
#ATRIBUTO PROTEGIDO COLOR

class Vehiculo: #clase
    def __init__(self,color):
        self._color = color #atributo protegido

    def Detalle_color(self): #metodo protegido
        return f"Este es un vehiculo de color: {self._color}"
    
class Camion(Vehiculo): #subclase
    def __init__(self, color,carga):
        super().__init__(color)
        self.carga = carga

    def MostrarInfo(sefl):
        print(f"El color del camion es: {sefl._color}") #accedemos al atributo protegido
        print(sefl.Detalle_color()) #llamando al metodo protegido

#objeto es tambien llamado instancia
#CREACION DE OBJETOS
Vehiculo1 = Camion ("Rojo",5)
Vehiculo1.MostrarInfo()

#ATRIBUTO PRIVADOS

class CuentaBancaria:
    def __init__(self,saldoinicial,): #constructor
        self.__saldoincial = saldoinicial #atibuto privado con __ va toar el saldo inicial
        self.__numerocuenta = "8037241" #atributo privado este con mumero de cuenta de fault ejj

    def despositar(self,Cantidad): 
        if Cantidad > 0:                                #if y elf son condiciones
            self.__saldoincial += Cantidad  #aqui das la orden de que se va sumar dinero a tu saldo incial
            print(f"Se depositaron {Cantidad}, nuevo saldo: {self.__saldoincial}")

    def retirar(self,cantidad):
        if cantidad <= self.__saldoincial:
            self.__saldoincial -= cantidad
            print(f"Se retiraron {cantidad}, nuevo saldo): {self.__saldoincial}")

        else: 
            print("Fondos insuficientes")

    def obtenersaldo(self):
        return self.__saldoincial
    
    def obtenernumerocuenta (self):
        return self.__numerocuenta
    
#CREAR OBJETOS
Micuenta = CuentaBancaria(5000)
Micuenta.despositar(100)
Micuenta.retirar(1100)
print(f"Saldo actual: {Micuenta.obtenersaldo()}")
print(f"Numero de cuenta: {Micuenta.obtenernumerocuenta()}")


#INTENDANDO ACCEDER DIRECTAMENTE A UN ATRIBUTO PRIVADO
#print(Micuenta.__saldoincial)

