from flask import Flask,render_template
from routes.home.index import home
from dotenv import load_dotenv
from config import DevConfig
from flask_wtf.csrf import CSRFProtect
from flask import request
import json
from forms import PruebaForm
from db.db import db
from lib.jwt import token_required
load_dotenv()



app = Flask(__name__)
app.config.from_object(DevConfig)
csrf = CSRFProtect(app)
app.register_blueprint(home)


@app.route('/')
def index():
    nombres = ['Juan', 'Pedro', 'Luis']
    apellidos = ['Perez', 'Gomez', 'Gonzalez']
    form = PruebaForm()
    return render_template('pages/home/index.html', nombres=nombres, titulo='Home klkk', apellidos=apellidos, form=form)


@app.route('/b', methods=['GET', 'POST'])
@token_required
def b():

    if request.method == 'POST':
        print(request.form)
        datos = json.loads(request.form['datos'])
        
        c =json.loads(datos['nombres'])
        print(c)
        print(type(c))


    nombres = ['Juan', 'Pedro', 'Luis']
    apellidos = ['Perez', 'Gomez', 'Gonzalez']

    return render_template('pages/home/index.html', nombres=nombres, titulo='Home klkk', apellidos=apellidos)


def convertir_a_diccionario(datos):
    """
    Convierte una lista de tuplas en un diccionario donde
    las claves son los primeros elementos de las tuplas y
    los valores son las listas cargadas desde las cadenas JSON.
    
    Args:
        datos: Lista de tuplas (clave, cadena JSON)
    
    Returns:
        dict: Diccionario con las claves y listas correspondientes
    """
    diccionario = {}
    
    for key, value in datos:
        diccionario[key] = json.loads(value)
    
    return diccionario

@app.route('/a')
def a():
    nombres = ['Juan','Pedro','Luis']
    return  render_template('pages/a/a.html', titulo='A klkk',nombres=nombres)



if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)