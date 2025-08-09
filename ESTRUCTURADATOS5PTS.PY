#ESTRUCTURA DE DATOS 5 PTS
"""
Crea un algoritmo que realice la sumatoria de los
numeros enteros comprendidos del 1 al 10,
es decir 1+2+3....+10
"""


#Codigo sencillo 

Suma = 0  #Mi variable de la suma

for numero in range(1,11): #Rescorrido de los numeros enteros
    Suma += numero #Suma cada numero a la variable suma

print ("La suma de los numeros enteros del 1 al 10 es:", Suma) #Me muestra mi resultado


#Codigo orientado a estructura de datos

numeros = list(range(1, 11)) #Mi lista con los numeros enteros del 1 al 10

print("Lista de numeros:",numeros) #Mostrar mi lista en estrucutura lineal

resultado = sum(numeros) #Funcion sum para sumar los elementos de mi lista

print("La suma de los números del 1 al 10 es:", resultado)

#Codigo orientado a estructura de datos con POO

class SumatoriaLista:
    def __init__(self, limite): #Constructor
        self.limite = limite    #Atributo
        
        self.numeros = list(range(1, limite + 1))  # Estructura de datos: lista

    def calcular(self):
        return sum(self.numeros)

mi_suma = SumatoriaLista(10) # Crear objeto con límite 10


print("Lista de números:", mi_suma.numeros) # Mostrar la lista


print("La suma de los números del 1 al 10 es:", mi_suma.calcular()) # Calcular y mostrar el resultado



