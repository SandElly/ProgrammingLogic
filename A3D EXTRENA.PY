#ARREGLOS MULTIDIMENCIONALES (LIBRERIA)

import numpy as np

#CREACION DE ARREGLOS CON NUMPY
Arreglo3D = np.zeros((2,3,4),dtype=int) #Creando un arreglo de ceros 2x3x4
print(Arreglo3D)

#MODIFICACION ELEMENTOS
Arreglo3D[0][0][0]= 99
print(Arreglo3D)