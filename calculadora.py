# Crear calculadora básica
def calculadora():
    print("Calculadora básica")
    
    # Pide al usuario dos números y los convierte a enteros
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    
    # Muestra las opciones de operaciones
    print("\nSelecciona la operación: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    # Pide al usuario seleccionar una operación
    opcion = input("Ingresa la opción (1/2/3/4): ")
    
    # Realiza la operación dependiendo de la opción seleccionada
    if opcion == '1':
        print(f"\nEl resultado de sumar {num1} + {num2} es: {num1 + num2}")
    elif opcion == '2':
        print(f"\nEl resultado de restar {num1} - {num2} es: {num1 - num2}")
    elif opcion == '3':
        print(f"\nEl resultado de multiplicar {num1} * {num2} es: {num1 * num2}")
    elif opcion == '4':
        # Verificar que el segundo número no sea cero antes de dividir
        if num2 != 0:
            print(f"\nEl resultado de dividir {num1} / {num2} es: {num1 / num2}")
        else:
            print("\nError: No se puede dividir entre 0")
    else:
        print("\nOpción inválida. Por favor elige la opción correcta.")

# Llamamos a la función de calculadora
calculadora()
