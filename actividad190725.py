#DADO EL SIGUIENTE ARREGLO SUMAR TODOS SUS ELEMENTOS: 


matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

suma_total = 0 #variable para guardar suma

for fila in matriz: #iteracion
    for elemento in fila:
        suma_total += elemento
print("La suma de todos los elementos es:" , suma_total)