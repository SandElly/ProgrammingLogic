#ARREGLO DE PAISES
paises = ["MEXICO","EGIPTO","COREA","JAPON","TAILANDIA"]
print("Primer pais:", paises[0])
print("Ultimo pais:", paises[4])
print("Todos los paises:", paises)

#ARREGLO DE NUMEROS
numeros = [1,5,19,2,30,8,15,3]
mayores_a_5 = [num for num in numeros if num > 5]
print ("Numeros mayores a 5:", mayores_a_5)


numeros = [1, 5, 19, 2, 30, 8, 15, 3]

# Contar cuántos números mayores a 5 hay
conteo = 0
for num in numeros:
    if num > 5:
        conteo += 1

# Crear arreglo vacío del tamaño necesario
mayores = [0] * conteo

# Llenar el nuevo arreglo con los números mayores a 5
i = 0
for num in numeros:
    if num > 5:
        mayores[i] = num
        i += 1

print("Números mayores a 5:", mayores)

numeros = [1, 5, 19, 2, 30, 8, 15, 3]
mayores = []

for num in numeros:
    if num > 5:
        mayores.append(num)

print("Números mayores a 5:", mayores)