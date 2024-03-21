from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



#crear la base de datos si no existe
def create_db(app):
    print('Creando base de datos')
    db.init_app(app)
    with app.app_context():
        # saber el nombre de la base de datos
        nombre_db = app.config['SQLALCHEMY_DATABASE_URI']
        print(nombre_db)
        nombre_db = nombre_db.split('/')[-1]
        print(nombre_db)
        db.create_all()
        db.session.commit()

