# Definir mis tareas del día
tareas = [
    "Presentación de Contratos",
    "Lavar el carro",
    "Entregar contratos PyME",
    "Recoger mi INE",
    "Ir al super",
    "Pintarme las uñas"
]

# Agregar al listado
def agregar_tarea():
    tarea = input("Ingresa una tarea nueva: ")
    tareas.append(tarea)
    print("Tarea agregada, bien hecho")

def eliminar_tarea():
    tarea = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
    if tarea < len(tareas) and tarea >= 0:
        tareas.pop(tarea)
        print("Tarea eliminada exitosamente")
    else:
        print("La tarea no existe en la lista")

def mostrar_tareas():
    if tareas:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas")

# Ejemplo de uso
while True:
    print("\nOpciones:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
