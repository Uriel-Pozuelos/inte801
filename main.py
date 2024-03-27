from flask import Flask,render_template
from routes.login import login
from dotenv import load_dotenv
from config import DevConfig
# from csrf import CSRFProtect
from flask_wtf.csrf import CSRFProtect
from flask import request
import json
from forms import PruebaForm
from models.usuario import Usuario
from db.db import db,create_db
from lib.jwt import token_required,allowed_roles
load_dotenv()



app = Flask(__name__)
app.config.from_object(DevConfig)
csrf = CSRFProtect(app)
app.register_blueprint(login)




@app.route('/b', methods=['GET', 'POST'])
@token_required
@allowed_roles(['admin'])
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


@app.route('/a')
def a():
    #obtener todos los usuarios
    usuarios = Usuario.query.all()
    #convertir a diccionario
    usuarios = [usuario.serialize() for usuario in usuarios]
    print(usuarios)
    return 'ok'


@app.route('/p')
def p():
    return render_template('pages/produccion/index.html')





if __name__ == '__main__':
    csrf.init_app(app)
    create_db(app)
    app.run(debug=True, port=5000)