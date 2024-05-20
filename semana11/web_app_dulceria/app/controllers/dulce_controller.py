from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

# Importamos el decorador de roles
from utils.decorators import role_required

# Importamos la vista de usuarios
from views import dulces_view

# Importamos el modelo de usuario
from models.dulces_model import Dulce

# Un Blueprint es un objeto que agrupa
# rutas y vistas
dulce_bp = Blueprint("user", __name__)

@dulce_bp.route("/users")
@login_required
@role_required(roles=["admin", "user"])
def list_dulces():
    # Obtenemos todos los usuarios
    users = Dulce.get_all()
    # Llamamos a la vista de usuarios
    return dulces_view.usuarios(users)


# Definimos la ruta "/users" asociada a la función registro
# que nos devuelve la vista de registro
@dulce_bp.route("/dulces/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_user():
    if request.method == "POST":
        # Obtenemos los datos del formulario
        marca = request.form["marca"]
        peso = request.form["peso"]
        sabor = request.form["sabor"]
        origen = request.form["origen"]

        # Creamos un nuevo usuario
        dulce = Dulce(marca=marca,peso = peso,sabor=sabor,origen=origen)
        dulce.save()
        flash("Dulce registrado exitosamente", "success")
        return redirect(url_for("user.list_users"))
    # Llamamos a la vista de registro
    return dulces_view.registro()


# Actualizamos la información del usuario por su id
# Ya estamos en la vista de actualizar
# por lo que obtenemos los datos del formulario
# y actualizamos la información del usuario
@dulce_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_user(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return "Usuario no encontrado", 404
    if request.method == "POST":
        # Obtenemos los datos del formulario
        marca = request.form["marca"]
        peso = request.form["peso"]
        sabor = request.form["sabor"]
        origen = request.form["origen"]
        # Actualizamos los datos del usuario
        dulce.update(marca=marca,peso = peso,sabor=sabor,origen=origen)
        # Guardamos los cambios
        return redirect(url_for("user.list_users"))
    return dulces_view.actualizar(dulce)


@dulce_bp.route("/users/<int:id>/delete")
@login_required
@role_required("admin")
def delete_user(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return "Usuario no encontrado", 404
    dulce.delete()
    return redirect(url_for("user.list_users"))

