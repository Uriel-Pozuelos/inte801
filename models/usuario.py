from db.db import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Usuario(db.Model):
  __tablename__ = 'usuario'
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(50))
  apellido = db.Column(db.String(50))
  email = db.Column(db.String(50))
  password = db.Column(db.String(50))
  rol = db.Column(db.String(50))
  estado = db.Column(db.String(50))
  fecha_creacion = db.Column(db.String(50),default=db.func.current_timestamp())
  
  db.Index('idx_usuario_email', email, unique=True)

  """
  funcion para que en base al rol se la sesion del rol correspondiente
  roles:compras,ventas,produccion, administrador
  engine: mysql
  """
  def get_session(self):
    if self.rol == 'compras':
      engine = create_engine('mysql+pymysql://compras:contraseña_compras@127.0.0.1:3306/cookies')
      Session = sessionmaker(bind=engine)
      return Session()
    elif self.rol == 'ventas':
      engine = create_engine('mysql+pymysql://ventas:contraseña_ventas@127.0.0.1:3306/cookies')
      Session = sessionmaker(bind=engine)
      return Session()
    elif self.rol == 'produccion':
      engine = create_engine('mysql+pymysql://produccion:contraseña_produccion@127.0.0.1:3306/cookies')
      Session = sessionmaker(bind=engine)
      return Session()
    elif self.rol == 'admin':
      engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/cookies')
      Session = sessionmaker(bind=engine)
      return Session()
    else:
      return None
    
  def serialize(self):
    return {
      'id': self.id,
      'nombre': self.nombre,
      'apellido': self.apellido,
      'email': self.email,
      'password': self.password,
      'rol': self.rol,
      'estado': self.estado,
      'fecha_creacion': self.fecha_creacion
    }



