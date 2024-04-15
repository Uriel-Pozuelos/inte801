
from flask import Flask, render_template, request,g,redirect,url_for
from routes.dashboard import dashboard
from routes.login import login
from dotenv import load_dotenv
from config import DevConfig
from flask_wtf.csrf import CSRFProtect
from models.usuario import Usuario
from routes.recetas import recetas
from routes.solicitud_produccion import solicitud
from routes.poduccion import produccion
from routes.proveedores import proveedores
from routes.compras import compras
from routes.usuario import usuario
from routes.venta import ventas
from routes.insumos import insumos
from db.db import db, create_db
from lib.jwt import token_required, allowed_roles
from routes.inventario_mp import inventario_mp
from routes.inventario_galletas import inventario_galletas
from lib.jwt import get_role
from models.usuario import Usuario
from db import seeder
import json
from db.db import db,create_db
from lib.jwt import token_required,allowed_roles,decodeToken,get_email

from apscheduler.schedulers.background import BackgroundScheduler

from lib.security import safe


load_dotenv()

app = Flask(__name__)
app.config.from_object(DevConfig)
csrf = CSRFProtect(app)

app.register_blueprint(recetas)
app.register_blueprint(login)
app.register_blueprint(produccion)
app.register_blueprint(solicitud)
app.register_blueprint(proveedores)
app.register_blueprint(usuario)
app.register_blueprint(ventas)
app.register_blueprint(compras)
app.register_blueprint(inventario_mp)
app.register_blueprint(inventario_galletas)
app.register_blueprint(insumos)
app.register_blueprint(dashboard)


@app.before_request
def before_request():
    rol = get_role()
    g.rol = rol if rol else 'invitado'
    email = get_email()
    if email:
        g.nombre = Usuario.query.filter_by(email=get_email()).first().nombre
    

    allowed_routes = [
        {
            'rol': 'produccion',
            'routes': [
                {
                'ruta': 'produccion.index',
                'name': 'Produccion',
                'icon': None
            },
                {
                'ruta': 'inventario_mp.index',
                'name': 'Inventarios',
                'icon': None
            },
            {
                'ruta': 'dashboard.index',
                'name': 'Dashboard',
                'icon': None
            }
            ]
            
        },
        {
            'rol': 'compras',
            'routes': [
                {
                'ruta': 'compras.index',
                'name': 'Compras',
                'icon': None
            },
                {
                'ruta': 'proveedores.index',
                'name': 'Proveedores',
                'icon': None
            },{
                'ruta': 'insumos.index',
                'name': 'Insumos',
                'icon': None
            }
            ]
        },{
            'rol': 'ventas',
            'routes': [
                {
                'ruta': 'recetas.index',
                'name': 'Recetas',
                'icon': None
                },
                {
                    'ruta': 'ventas.index',
                    'name': 'Ventas',
                    'icon': None
                }
            ]
        
        }]
    #agrergar rutas de admin, haciendo un merge de las rutas de los otros roles
    admin_routes = [
        {
            'rol': 'admin',
            'routes': []
        }
    ]
    for route in allowed_routes:
        admin_routes[0]['routes'] += route['routes']
    allowed_routes += admin_routes


    g.allowed_routes = allowed_routes
    
@app.route("/")
@app.route("/home")
def index():
    rol = g.rol
    print(rol)
    if rol == 'invitado':
        return redirect('/login')
    if rol == 'admin':
        return redirect('/recetas')
    if rol == 'produccion':
        return redirect('/produccion')
    if rol == 'compras':
        return redirect('/compras')
    if rol == 'ventas':
        return redirect('/recetas')



@app.route("/b", methods=["GET", "POST"])

def b():
    users = [
        {
            "id": 1,
            "name": "Juan",
            "email": "juan",
        },
        {
            "id": 2,
            "name": "Pedro",
            "email": "pedro",
        },
        {
            "id": 3,
            "name": "Maria",
            "email": "maria",
        },
    ]
        
    return render_template(
        "pages/home/index.html",
        users=users,
        titulo="Home klkk"
    )


@app.route("/a")
def a():
    # obtener todos los usuarios
    usuarios = Usuario.query.all()
    # convertir a diccionario
    usuarios = [usuario.serialize() for usuario in usuarios]
    print(usuarios)
    return 'ok'

# manerjar rutas que no existen
@app.errorhandler(404)
def page_not_found(e):
    if g.rol == 'invitado':
        return redirect('/')
    return render_template('pages/404/404log.html'), 404

def task():
    print("Hola mundo")


if __name__ == "__main__":
    csrf.init_app(app)
    create_db(app)
    
    # cron = BackgroundScheduler()
    # cron.add_job(task, "interval", seconds=5)
    # cron.start()

    with app.app_context():
        print("Creando usuarios...")
        seeder.seed_users()
        print("Se crearon correctamente los usuarios...")
    app.run(debug=True, port=5001)
