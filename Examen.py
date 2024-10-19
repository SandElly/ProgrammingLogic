#Primer paso crea un sistema que verifique el acceso basado en un nombre de usuario y contraseña (aqui coloco variables y las nombro) 
Nombredeusuario = "Sandelly"
Contraseñadeusuario = "1509560Sa"
#Si el usuario ingresa correcto nombre mas contraseña que muestre mensaje de bienvenida que coloco en la line 9 a la variable le coloque el input para que el usuario ingrese
Usuario = input("Ingrese su Nombre de su usuario:")
Contraseña = input("Ingrese la Contraseña de su usuario:")
#Usando operadores relacionados y logicos para validar los datos (aqui coloco mi si mas mi condicional mas su logico que es el and y == los valores sean iguales)
if Usuario == Nombredeusuario and Contraseñadeusuario ==Contraseñadeusuario:
   print("Hola bienvenido cuentas con el acceso correcto")
#Agrega una funcionalidad adicionalque perimita sumar dos numeros si el acceso es correcto (tome de base lo de la calculadora int entero y le agregue la suma)
   num1 = int(input("Ingrese el primer numero:"))
   num2 = int(input("Ingrese el segundo numero:"))
   print("Resultado:", num1 + num2)
else:
   print("Acceso denegado intenta de nuevo.")
#Por ultimo coloque el else igual como en la calculadora que me traiga lo que es mi opcion invalida o incorrecta