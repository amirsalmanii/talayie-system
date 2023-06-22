from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return self.email
    
    def genrate_password_hash_(self, password_raw):
        self.password_hash = generate_password_hash(password_raw)
        
    def check_user_password(self,password_raw):
        return check_password_hash(self.password_hash, password_raw)
