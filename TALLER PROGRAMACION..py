from datetime import date

# ==============================
# Clase Usuario
# ==============================
class Usuario:
    def _init_(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.libros = []  # Libros prestados o consultados

    def registrar(self):
        print(f"Usuario {self.nombre} registrado con éxito.")

    def consultar_libros(self):
        if not self.libros:
            print(f"{self.nombre} no tiene libros registrados.")
        else:
            print(f"Libros de {self.nombre}:")
            for libro in self.libros:
                print(f" - {libro.titulo} ({libro.estado})")


# ==============================
# Clase Libro
# ==============================
class Libro:
    def _init_(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.estado = "Disponible"
        self.usuario_asociado = None

    def gestionar_libro(self):
        print(f"Libro: {self.titulo} - Estado: {self.estado}")

    def registrar_usuario(self, usuario):
        self.usuario_asociado = usuario
        usuario.libros.append(self)
        print(f"Libro '{self.titulo}' registrado al usuario {usuario.nombre}")


# ==============================
# Clase Bibliotecario (Préstamos)
# ==============================
class Bibliotecario:
    def _init_(self, id_prestamo, libro, usuario, fecha_inicio=None, fecha_fin=None):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio if fecha_inicio else date.today()
        self.fecha_fin = fecha_fin

    def crear_prestamo(self):
        if self.libro.estado == "Disponible":
            self.libro.estado = "Prestado"
            self.libro.registrar_usuario(self.usuario)
            print(f"Préstamo creado: {self.libro.titulo} → {self.usuario.nombre}")
        else:
            print(f"El libro '{self.libro.titulo}' no está disponible.")

    def cerrar_prestamo(self):
        if self.libro.estado == "Prestado":
            self.libro.estado = "Disponible"
            self.fecha_fin = date.today()
            print(f"Préstamo cerrado: {self.libro.titulo} devuelto por {self.usuario.nombre}")
        else:
            print(f"El libro '{self.libro.titulo}' ya estaba disponible.")