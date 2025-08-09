#ARREGLO BIDIMENCIONALES (LISTAS NATIVAS)

#CREACION CON DIFERENTES ELEMENTOS

Arreglo1 = [ #3x5
    [1,2,3,4,5], #fila 1  la coma es para indicarle que continue
    [6,7,8,9,10], #fila 2
    [11,12,13,14,15] #fila 3
]

#CREACION CON UN SOLO ELEMENTO    (declaracion de variable)
filas = 3
columnas = 5

Arreglo2 = [[0 for _ in range(columnas)] for _ in range(filas)]
#Arreglo de un solo elemento (0) en todas las filas y columnas

print(Arreglo1)
print("-"*30)
print(Arreglo2)
print("-"*30)
 
#ACCEDER A ELEMENTOS ESPECIFICOS

Elemento = Arreglo1[1][3] #accediendo a 9 llamar al numero que queremos del arreglo 1
print(Elemento)
print("-"*30)

#ACCEDER A UNA FILA COMPLETA 
Fila1 = Arreglo1[0]
print(Fila1)
print("-"*30)

#MODIFCIAR ELEMENTOS
Arreglo1[0][4] = 50
print(Arreglo1)
print("-"*30)

#ITERACION RECORRER 
for i in Arreglo1: #Recorrer arreglo con bucles
    for e in i: #bucle anidado
        print(e,end=" ") #parametro coloque un espacio
    print() #Nueva linea despues de cada fila