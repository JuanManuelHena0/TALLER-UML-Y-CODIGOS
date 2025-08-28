import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

// ==============================
// Clase Usuario
// ==============================
class Usuario {
    private int idUsuario;
    private String nombre;
    private String email;
    private List<Libro> libros;

    public Usuario(int idUsuario, String nombre, String email) {
        this.idUsuario = idUsuario;
        this.nombre = nombre;
        this.email = email;
        this.libros = new ArrayList<>();
    }

    public void registrar() {
        System.out.println("Usuario " + nombre + " registrado con éxito.");
    }

    public void consultarLibros() {
        if (libros.isEmpty()) {
            System.out.println(nombre + " no tiene libros registrados.");
        } else {
            System.out.println("Libros de " + nombre + ":");
            for (Libro libro : libros) {
                System.out.println(" - " + libro.getTitulo() + " (" + libro.getEstado() + ")");
            }
        }
    }

    public List<Libro> getLibros() {
        return libros;
    }
}

// ==============================
// Clase Libro
// ==============================
class Libro {
    private int idLibro;
    private String titulo;
    private String autor;
    private String estado;
    private Usuario usuarioAsociado;

    public Libro(int idLibro, String titulo, String autor) {
        this.idLibro = idLibro;
        this.titulo = titulo;
        this.autor = autor;
        this.estado = "Disponible";
        this.usuarioAsociado = null;
    }

    public void gestionarLibro() {
        System.out.println("Libro: " + titulo + " - Estado: " + estado);
    }

    public void registrarUsuario(Usuario usuario) {
        this.usuarioAsociado = usuario;
        usuario.getLibros().add(this);
        System.out.println("Libro '" + titulo + "' registrado al usuario " + usuarioAsociado.nombre);
    }

    // Getters y Setters
    public String getTitulo() {
        return titulo;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
}

// ==============================
// Clase Bibliotecario (Préstamos)
// ==============================
class Bibliotecario {
    private int idPrestamo;
    private Libro libro;
    private Usuario usuario;
    private LocalDate fechaInicio;
    private LocalDate fechaFin;

    public Bibliotecario(int idPrestamo, Libro libro, Usuario usuario) {
        this.idPrestamo = idPrestamo;
        this.libro = libro;
        this.usuario = usuario;
        this.fechaInicio = LocalDate.now();
        this.fechaFin = null;
    }

    public void crearPrestamo() {
        if (libro.getEstado().equals("Disponible")) {
            libro.setEstado("Prestado");
            libro.registrarUsuario(usuario);
            System.out.println("Préstamo creado: " + libro.getTitulo() + " → " + usuario.nombre);
        } else {
            System.out.println("El libro '" + libro.getTitulo() + "' no está disponible.");
        }
    }

    public void cerrarPrestamo() {
        if (libro.getEstado().equals("Prestado")) {
            libro.setEstado("Disponible");
            this.fechaFin = LocalDate.now();
            System.out.println("Préstamo cerrado: " + libro.getTitulo() + " devuelto por " + usuario.nombre);
        } else {
            System.out.println("El libro '" + libro.getTitulo() + "' ya estaba disponible.");
        }
    }
}

// ==============================
// Clase principal (Main)
// ==============================
public class Main {
    public static void main(String[] args) {
        // Crear usuario
        Usuario usuario1 = new Usuario(1, "Juan", "juan@email.com");
        usuario1.registrar();

        // Crear libros
        Libro libro1 = new Libro(101, "Cien años de soledad", "Gabriel García Márquez");
        Libro libro2 = new Libro(102, "El Quijote", "Miguel de Cervantes");

        // Consultar libros de Juan
        usuario1.consultarLibros();

        // Crear préstamo
        Bibliotecario prestamo1 = new Bibliotecario(1, libro1, usuario1);
        prestamo1.crearPrestamo();

        // Consultar libros de Juan
        usuario1.consultarLibros();

        // Cerrar préstamo
        prestamo1.cerrarPrestamo();
        libro1.gestionarLibro();
    }
}