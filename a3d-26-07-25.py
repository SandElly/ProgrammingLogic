#ARREGLOS MULTIDIMENSIONALES LISTAS

#CREACION 
Arreglo3D = [ #CREACION DE UN ARREGLO DE 2 X 3 X 4    2BLOQUES 3 FILAS Y 4 COLUMNAS
    [ #PRIMER BLOQUE X=0 INDICE
        [1,2,3,4],#PRIMER FILA Y=0
        [5,6,7,8],#SEGUNDA FILA Y=1
        [9,10,11,12]#TERCERA FILA Y=2
    ],
    [#SEGUNDO BLOQUE X=1 INDICE
        [13,14,15,16],#FILA 1 Y=0
        [17,18,19,20],#FILA 2 Y=1
        [21,22,23,24]#FILA 3 Y=2
    ]
]

print("El elemento:",Arreglo3D[1][2][3]) #24
print("El elemento:",Arreglo3D[0][1][2])#7 
print("El elemento:",Arreglo3D[0][0][3])#4


##ITERACION
for x in range (len(Arreglo3D)): #PROFUNDIDAD (BLOQUES)
    for y in range(len(Arreglo3D[x])): #BUSCAR EN FILAS YA TENIENDO MI PROFUNDIDAD (FILAS)
        for z in range(len(Arreglo3D[x][y])): #columnas aqui las va revisar
            print(f"Arreglo3D[{x}][{y}][{z}] = {Arreglo3D[x][y][z]}")