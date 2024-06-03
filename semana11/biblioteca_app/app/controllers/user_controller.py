from flask import Blueprint, request, jsonify,redirect,url_for,flash
from models.user_model import User
from flask_login import current_user,login_user,logout_user,login_required
from werkzeug.security import check_password_hash
from views import user_view
user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("user.profile",id=current_user))
    return redirect(url_for("user.login"))

@user_bp.route("/user/create", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        roles = request.form["role"]

        existing_user = User.find_by_username(username)
        if existing_user:
            flash("El nombre de usuario no disponible","error")
            return  redirect(url_for("user.register"))
        else:
            new_user = User(username, password, roles)
            new_user.save()
            flash("usuario creado exitosamente","success")
            return redirect(url_for("user.profile"),new_user.id)
    return user_view.registro()

@user_bp.route("/users")
@login_required
def list_users():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route("/user/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.find_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Inicio de sesion exitoso","success")
            if user.has_role("admin"):
                return redirect(url_for("user.list_users"))
            else:
                return redirect(url_for("user.profile",id=user.id))
    return user_view.login()

@user_bp.route("/profile/<int:id>")
@login_required
def profile(id):
    user = User.get_by_id(id)
    return user_view.perfil(user)
@user_bp.route("/user/logout")
def logout():
    logout_user()
    return redirect(url_for("user.login"))