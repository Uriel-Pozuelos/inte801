from db.db import db


class PasswordHistories(db.Model):
  __tablename__ = 'password_histories'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer)
  password = db.Column(db.String(50))
  fecha_creacion = db.Column(db.String(50),default=db.func.current_timestamp())
  
  def serialize(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'password': self.password,
      'fecha_creacion': self.fecha_creacion
    }