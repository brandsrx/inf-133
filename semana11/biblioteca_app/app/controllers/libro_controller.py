from flask import Blueprint, request, flash,redirect,url_for
from models.libro_model import Libro
from views import libros_view
# Crear un blueprint para el controlador de libroes
libros_bp= Blueprint("libros", __name__)


# Ruta para obtener la lista de libroes
@libros_bp.route("/libros", methods=["GET"])
def list_libros():
    libro = Libro.get_all()
    return libros_view.render_libro_list(libros=libro)


# Ruta para obtener un libro específico por su ID
@libros_bp.route("/libros/<int:id>", methods=["GET"])
def get_libro(id):
    libro = Libro.get_by_id(id)
    if libro:
        return libros_view.render_libro_detail(libro)
    flash("no se ha podido encontrar el libro")
    return redirect(url_for("libros.list_libros"))


# Ruta para crear un nuevo libro
@libros_bp.route("/libro/create", methods=["GET","POST"])
def create_libro():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        edicion = request.form["edicion"]
        disponibilidad = request.form["disponibilidad"]
        # Crear un nuevo libro y guardarlo en la base de datos
        libro = Libro(titulo=titulo,autor = autor,edicion=edicion,disponibilidad=disponibilidad)
        libro.save()
        flash("Libro creador exitosamente","success")
        return redirect(url_for("libros.get_libros"))

    return libros_view.create()


# Ruta para actualizar un libro existente
@libros_bp.route("/libros/<int:id>", methods=["GET","POST"])
def update_libro(id):
    libro = Libro.get_by_id(id)
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        edicion = request.form["edicion"]
        disponibilidad = request.form["disponibilidad"]
        # Crear un nuevo libro y guardarlo en la base de datos
        libro.update(titulo=titulo,autor = autor,edicion=edicion,disponibilidad=disponibilidad)
        libro.save()
        flash("El libro se actualizo correctamente")
        return redirect(url_for("libros.get_libros"))
  

    return libros_view.update(libro)


# Ruta para eliminar un libro existente
@libros_bp.route("/libros/<int:id>", methods=["DELETE"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        flash("No se ha encontrado el libro")
    # Eliminar el libro de la base de datos
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    flash("Libro se borro exitosamente")
    return redirect(url_for("libros.list_libros"))
