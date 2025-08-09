#INSTRUCCIONES: clase llamada libro

class Libro:
    def __init__(self,Titulo,Autor,Publicacion,Genero): #constructor. (dentro de self van los atributos).

        
        self.Titulo = Titulo   # (titulo es primer atributo)
        self.Autor = Autor
        self.Publicacion = Publicacion
        self.Genero = Genero 



#constructor: es un metodo especial dentro de una clase 
#que se llama autom cuando se crea una instancia.
# su funcion principal es inicializar el objeto asignando valores iniciales. 
#self es un parametro, que nos sirve para inicializar nuestros atributos
#def inicialisador de metodos solamente en python

    def mostrar_informacion(self): #metodo que muestra la info
        print(f"Titulo {self.Titulo}")
        print(f"Autor {self.Autor}")
        print(f"Publicacion: {self.Publicacion}")
        print(f"Genero: {self.Genero}")
        print("-"*30) 

#-----------CREACION DE INSTANCIAS---------

libro1 = Libro("Cien años de soledad","Gabriel Garcia Marquez","1967","Realismo magico")
libro2 = Libro("1987","George Orwell","1949","Distopia")
libro3 = Libro("Orgullo y Prejuicio","Jane Austen","1813","Fabula")
libro4 = Libro("El Principito","Antoine de Saint-Exupery","1943", "Fabula")
libro5 = Libro("Sapiens","Yubal Noah","2011","Ensayo Historico")

#---------ACCEDIENDO A LOS OBJETOS CON SUS ATRIBUTOS-------

libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro3.mostrar_informacion()
libro4.mostrar_informacion()
libro5.mostrar_informacion()