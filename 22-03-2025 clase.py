#•	Ejercicio 1: Contador del 1 al 10 usando while.
# Inicializamos una variable ejercicio 1
contador = 0
# Condición del bucle while fstring es mi variable contador es para hacer la cadena mas limpia
while contador < 11:
    print(f"El contador es: {contador}")
    # Incrementamos la variable contador
    contador += 1

print("¡Bucle terminado!")


#•	Ejercicio 2: Juego de adivinar un número secreto entre 1 y 10.
import random  # Importamos la librería random para generar un número aleatorio

# Generar un número secreto aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Se inicia el juego
print("¡Bienvenido al juego de adivinar el número secreto!")
intentos = 0  # Variable para contar los intentos del jugador

# Bucle para que el jugador intente adivinar
while True:
    # Solicitar un número al jugador
    numero_adivinado = int(input("Adivina el número secreto (entre 1 y 10): "))
    intentos += 1  # Incrementamos el contador de intentos

    # Verificar si el número adivinado es correcto
    if numero_adivinado == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos.")
        break  # Si adivina correctamente, terminamos el juego
    elif numero_adivinado < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")


#• Ejercicio 3: Menú interactivo que permita elegir opciones hasta seleccionar "Salir".
def opcion1():
    print("Has seleccionado la opción 1: Mostrar tareas")

def opcion2():
    print("Has seleccionado la opción 2: Agregar tarea")

def opcion3():
    print("Has seleccionado la opción 3: Eliminar tarea")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

# Bucle para mostrar el menú hasta que el usuario elija salir
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")






suma = 0
numero = None

while numero != 0:
    numero = int(input("Ingrese el número: "))
    if numero != 0:  # Solo sumamos si el número no es 0
        suma += numero

print("La suma total es:")
print(suma)