from flask import Blueprint, request, jsonify,redirect,url_for
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def index():
    return redirect(url_for("user.profile", id=User.id))

@user_bp.route("/user/create", methods=["POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        roles = request.form["role"]

        existing_user = User.find_by_username(username)
        if existing_user:
            return  "El nombre de usuario ya está en uso", 400
        new_user = User(username, password, roles)
        new_user.save()

    return "Usuario creado exitosamente" , 201


@user_bp.route("/user/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.find_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            # Si las credenciales son válidas, genera un token JWT
            access_token = create_access_token(
                identity={"username": username, "roles": user.roles}
            )
            return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
