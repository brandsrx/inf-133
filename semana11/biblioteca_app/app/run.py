from flask import Flask
from flask_login import LoginManager

from controllers.libro_controller import libros_bp
from controllers.user_controller import user_bp
from database import db
from models.user_model import User

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///libro.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"]="clave-secreta"

login_manager = LoginManager()
#Especifica la ruta de inicio de sesion
login_manager.login_view = "user.login"
login_manager.init_app(app)



#funcio para cargarn un usuario basado en su ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    

# Inicializa la base de datos
db.init_app(app)

# Registra el blueprint de animales en la aplicación
app.register_blueprint(libros_bp)
app.register_blueprint(user_bp)

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)
