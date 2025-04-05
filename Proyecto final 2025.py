import matplotlib.pyplot as plt
#import numpy as np (En este codigo no sera usado)
#[] usado para la creacion de listas y acceder a los elementos


# Aqui se definen las tareas predeterminadas del usuario
tareas = [
    "Presentación de Contratos",
    "Lavar el carro",
    "Entregar contratos PyME",
    "Recoger mi INE",
    "Ir al super",
    "Pintarme las uñas"
]

# Apartado de lista de tareas completadas
tareas_completadas = []

#Funciones del programa 

#Apartado donde el usuario agrega una tarea nueva a la lista predeterminada
def agregar_tarea():
    tarea = input("Ingresa una tarea nueva: ")
    tareas.append(tarea)
    print("Tarea agregada, bien hecho")

#Apartado para eliminar
def eliminar_tarea():
    tarea = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
    if tarea < len(tareas) and tarea >= 0:
        tareas.pop(tarea)
        print("Tarea eliminada exitosamente")
    else:
        print("La tarea no existe en la lista")

#Apartado para mostrar 
def mostrar_tareas():
    if tareas:
        print("Lista de tareas: ")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes")

#Apartado para marcar tarea completada
def completar_tarea():
    mostrar_tareas()
    tarea_completada = int(input("Ingresa el número de la tarea completada: ")) - 1
    if tarea_completada < len(tareas) and tarea_completada >= 0:
        tarea = tareas.pop(tarea_completada)
        tareas_completadas.append(tarea)
        print(f"Tarea '{tarea}' completada")
    else:
        print("Tarea no válida.")

#Apartado del estatus de las tareas se utilizo la funcion len (es la cantidad de elementos en mi lista de tareas)
#Por ejemplo si mi lista contiene 6 elementos me va devolver 6
def graficar_tareas():
    tareas_pendientes = len(tareas)
    tareas_realizadas = len(tareas_completadas)

    # En este apartado se crea la grafica de tareas pendientes y completadas
    labels = ['Tareas Pendientes', 'Tareas Completadas']
    values = [tareas_pendientes, tareas_realizadas]

    plt.bar(labels, values, color=['purple', 'blue'])
    plt.title("Tareas Pendientes vs Completadas")
    plt.xlabel("Estado de las Tareas")
    plt.ylabel("Número de Tareas")
    plt.show()

# Menu interactivo donde el usuario eligira las opciones dinamicas
while True:
    print("\nOpciones:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Completar tarea")
    print("5. Graficar estado de tareas")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        completar_tarea()
    elif opcion == "5":
        graficar_tareas()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
