from db.db import db


class VerificationCode(db.Model):
    __tablename__ = 'verification_code'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def serialize(self):
        return {
            'id': self.id,
            'code': self.code,
            'user_id': self.user_id
        }