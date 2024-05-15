from flask import Blueprint, request, jsonify
from models.libro_model import Libro
from views.libros_view import render_libro_list, render_libro_detail
from utils.decorators import jwt_required, roles_required
# Crear un blueprint para el controlador de libroes
libros_bp= Blueprint("libros", __name__)


# Ruta para obtener la lista de libroes
@libros_bp.route("/libros", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_libros():
    libro = Libro.get_all()
    return jsonify(render_libro_list(libro))


# Ruta para obtener un libro específico por su ID
@libros_bp.route("/libros/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_libro(id):
    libro = Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error": "libro no encontrado"}), 404


# Ruta para crear un nuevo libro
@libros_bp.route("/libros", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_libro():

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")
    # Validación simple de datos de entrada
    if not titulo or not autor or not edicion or  disponibilidad is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo libro y guardarlo en la base de datos
    libro = Libro(titulo=titulo,autor = autor,edicion=edicion,disponibilidad=disponibilidad)
    libro.save()

    return jsonify(render_libro_detail(libro)), 201


# Ruta para actualizar un libro existente
@libros_bp.route("/libros/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "libro no encontrado"}), 404

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")
    # Actualizar los datos del libro
    libro.update(titulo=titulo,autor = autor,edicion=edicion,disponibilidad=disponibilidad)

    return jsonify(render_libro_detail(libro))


# Ruta para eliminar un libro existente
@libros_bp.route("/libros/<int:id>", methods=["DELETE"])
@roles_required(roles=["admin"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "libro no encontrado"}), 404

    # Eliminar el libro de la base de datos
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
