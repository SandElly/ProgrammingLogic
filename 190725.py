
class CuentaBancaria:
    def __init__(self,Titular,Saldo):
        self.__Titular = Titular
        self.__Saldo = Saldo

    def GetSaldo(self):
        return self.__Saldo
    
    def Despositar(self,Cantidad):
        if Cantidad > 0:
            self.__Saldo += Cantidad

    def Retirar(self,Cantidad):
        if 0 < Cantidad <= self.__Saldo:
            self.__Saldo -= Cantidad

#Instancias 
Cuenta1 = CuentaBancaria("Mateo",1000)
Cuenta1.Despositar(500)
Cuenta1.Retirar(200)
print(Cuenta1.GetSaldo()) # Imprima el saldo actual


            