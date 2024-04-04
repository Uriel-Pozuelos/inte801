from flask import Flask, render_template, request
from routes.login import login
from dotenv import load_dotenv
from config import DevConfig
from flask_wtf.csrf import CSRFProtect
from models.usuario import Usuario
from routes.recetas import recetas
from routes.proveedores import proveedores
from routes.usuario import usuario
from routes.venta import ventas
from db.db import db, create_db
from lib.jwt import token_required, allowed_roles
from db import seeder
import json

load_dotenv()

app = Flask(__name__)
app.config.from_object(DevConfig)
csrf = CSRFProtect(app)
app.register_blueprint(recetas)
app.register_blueprint(login)
app.register_blueprint(proveedores)
app.register_blueprint(usuario)
app.register_blueprint(ventas)

@app.route("/b", methods=["GET", "POST"])
@token_required
@allowed_roles(["admin"])
def b():
    if request.method == "POST":
        print(request.form)
        datos = json.loads(request.form["datos"])

        c = json.loads(datos["nombres"])
        print(c)
        print(type(c))

    nombres = ["Juan", "Pedro", "Luis"]
    apellidos = ["Perez", "Gomez", "Gonzalez"]

    return render_template(
        "pages/home/index.html",
        nombres=nombres,
        titulo="Home klkk",
        apellidos=apellidos,
    )


@app.route("/a")
def a():
    # obtener todos los usuarios
    usuarios = Usuario.query.all()
    # convertir a diccionario
    usuarios = [usuario.serialize() for usuario in usuarios]
    print(usuarios)
    return "ok"


if __name__ == "__main__":
    csrf.init_app(app)
    create_db(app)

    with app.app_context():
        print("Creando usuarios...")
        seeder.seed_users()
        print("Se crearon correctamente los usuarios...")

    app.run(debug=True, port=5000)
