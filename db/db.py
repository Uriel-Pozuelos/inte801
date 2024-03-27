from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



#crear la base de datos si no existe
def create_db(app):
    print('Creando base de datos')
    db.init_app(app)
    with app.app_context():
        
       
        db.create_all()
        db.session.commit()

