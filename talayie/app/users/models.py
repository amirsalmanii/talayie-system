from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class Organization(db.Model):
    __tablename__ = 'organizations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    personnels = db.relationship('Personnel', backref='organization', lazy='dynamic')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    personnels = db.relationship('Personnel', backref='role', lazy='dynamic')


class Personnel(db.Model):
    __tablename__ = 'personnels'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    date_of_birth = db.Column(db.String(128))
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))
    organization = db.Column(db.Integer, db.ForeignKey('organizations.id'))


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    personnel = db.Column(db.Integer, db.ForeignKey('personnels.id'))
