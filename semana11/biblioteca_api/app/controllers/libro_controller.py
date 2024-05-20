from flask import Blueprint, request, jsonify,redirect,url_for
from models.libro_model import Libro
from views import libros_view
from utils.decorators import jwt_required, roles_required
# Crear un blueprint para el controlador de libroes
libros_bp= Blueprint("libros", __name__)


# Ruta para obtener la lista de libroes
@libros_bp.route("/libros", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_libros():
    libro = Libro.get_all()
    return libros_view.render_libro_list(libros=libro)


# Ruta para obtener un libro específico por su ID
@libros_bp.route("/libros/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_libro(id):
    libro = Libro.get_by_id(id)
    if libro:
        return libros_view.render_libro_detail(libro)
    return "libro no encontrado", 404


# Ruta para crear un nuevo libro
@libros_bp.route("/libro/create", methods=["GET","POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_libro():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        edicion = request.form["edicion"]
        disponibilidad = request.form["disponibilidad"]
        # Crear un nuevo libro y guardarlo en la base de datos
        libro = Libro(titulo=titulo,autor = autor,edicion=edicion,disponibilidad=disponibilidad)
        libro.save()
        return redirect(url_for("libros.get_libros"))

    return libros_view.create()


# Ruta para actualizar un libro existente
@libros_bp.route("/libros/<int:id>", methods=["GET","POST"])
@jwt_required
@roles_required(roles=["admin"])
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
        return redirect(url_for("libros.get_libros"))
  

    return libros_view.update(libro)


# Ruta para eliminar un libro existente
@libros_bp.route("/libros/<int:id>", methods=["DELETE"])
@roles_required(roles=["admin"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return "error Libro no encontrado",404

    # Eliminar el libro de la base de datos
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
