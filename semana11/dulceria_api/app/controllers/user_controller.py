from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from utils.decorators import jwt_required, roles_required
from views.user_view import render_user_profile
user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    roles = data.get("role")
    print(data)
    if not username or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    existing_user = User.find_by_username(username)
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400
    print(roles)
    new_user = User(username, password, roles)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201
@user_bp.route("/profile",methods=["GET"])
@roles_required(roles=["user"])
def perfil():
    return render_user_profile(User)
    

@user_bp.route("/user/<int:id>",methods=["DELETE"])
@roles_required(roles=["admin"])
def delete_dulce(id):
    user = User.get_by_id(id)

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    # Eliminar el dulce de la base de datos
    user.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204

    

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.find_by_username(username)
    if user and check_password_hash(user.password_hash, password):
        # Si las credenciales son válidas, genera un token JWT
        access_token = create_access_token(
            identity={"username": username, "roles": user.roles}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
