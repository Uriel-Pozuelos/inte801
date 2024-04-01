from models.usuario import Usuario
from db.db import db
from datetime import datetime


def seed_users():
    try:
        usuarios = Usuario.query.all()
    
        if len(usuarios) == 0:
            fecha = datetime.now().strftime("%Y-%m-%d")

            usuarios_seed = [
                {
                    "nombre": "Juan",
                    "apellido": "Perez",
                    "email": "jp@gmail.com",
                    "password": "jw4np3n",
                    "rol": "admin",
                    "estado": "activo",
                    "fecha_creacion": fecha,
                }
            ]

            for usuario in usuarios_seed:
                u = Usuario(**usuario)
                db.session.add(u)
                
            db.session.commit()
        
        return "ok"
    except Exception as e:
        print(e)
        return "error"
    
