from datetime import date #esto es una importacion de la libreria datetime para manejar fechas

# ==============================
# Clase Usuario
# ==============================
class Usuario: #se crea la clase usuario con los atributos id_usuario, nombre y email 
    #que es una clase? es un molde para crear objetos que comparten atributos y comportamientos similares
    def _init_(self, id_usuario, nombre, email): #def quiere decir definir una funcion
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.libros = []  # Libros prestados o consultados

    def registrar(self): #se crea el metodo registrar que imprime un mensaje de exito al registrar un usuario
        print(f"Usuario {self.nombre} registrado con éxito.") 

    def consultar_libros(self):
        if not self.libros: #si la lista de libros esta vacia imprime que no tiene libros registrados
            print(f"{self.nombre} no tiene libros registrados.")
        else:
            print(f"Libros de {self.nombre}:") #si tiene libros registrados imprime la lista de libros con su estado
            for libro in self.libros:
                print(f" - {libro.titulo} ({libro.estado})") #imprime el titulo y el estado del libro


# ==============================
# Clase Libro
# ==============================
class Libro: #se crea la clase libro con los atributos id_libro, titulo, autor, estado y usuario_asociado
    def _init_(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.estado = "Disponible"
        self.usuario_asociado = None #usuario asociado al libro (si está prestado) el none quiere decir que no tiene ningun usuario asociado al libro

    def gestionar_libro(self): #se crea el metodo gestionar_libro que imprime el titulo y el estado del libro
        print(f"Libro: {self.titulo} - Estado: {self.estado}") #imprime el titulo y el estado del libro

    def registrar_usuario(self, usuario): #se crea el metodo registrar_usuario que asocia un usuario al libro y lo agrega a la lista de libros del usuario
        self.usuario_asociado = usuario #asocia el usuario al libro
        usuario.libros.append(self) #agrega el libro a la lista de libros del usuario
        print(f"Libro '{self.titulo}' registrado al usuario {usuario.nombre}") #imprime un mensaje de exito al registrar el libro al usuario


# ==============================
# Clase Bibliotecario (Préstamos)
# ==============================
class Bibliotecario: #se crea la clase bibliotecario con los atributos id_prestamo, libro, usuario, fecha_inicio y fecha_fin
    def _init_(self, id_prestamo, libro, usuario, fecha_inicio=None, fecha_fin=None): 
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio if fecha_inicio else date.today() #si no se proporciona fecha_inicio, se asigna la fecha actual
        self.fecha_fin = fecha_fin

    def crear_prestamo(self): #se crea el metodo crear_prestamo que verifica si el libro esta disponible y lo presta al usuario
        if self.libro.estado == "Disponible": #si el estado del libro es disponible
            self.libro.estado = "Prestado" #cambia el estado del libro a prestado
            self.libro.registrar_usuario(self.usuario) #registra el usuario al libro
            print(f"Préstamo creado: {self.libro.titulo} → {self.usuario.nombre}") #imprime un mensaje de exito al crear el prestamo
        else:
            print(f"El libro '{self.libro.titulo}' no está disponible.") #si el libro no esta disponible imprime un mensaje de error

    def cerrar_prestamo(self): #se crea el metodo cerrar_prestamo que verifica si el libro esta prestado y lo devuelve al usuario
        if self.libro.estado == "Prestado": #si el estado del libro es prestado
            self.libro.estado = "Disponible" #cambia el estado del libro a disponible
            self.fecha_fin = date.today() #asigna la fecha actual a la fecha_fin
            print(f"Préstamo cerrado: {self.libro.titulo} devuelto por {self.usuario.nombre}") #imprime un mensaje de exito al cerrar el prestamo
        else:
            print(f"El libro '{self.libro.titulo}' ya estaba disponible.") #si el libro ya estaba disponible imprime un mensaje de error