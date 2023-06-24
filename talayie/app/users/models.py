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
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    personnel_id = db.Column(db.Integer, db.ForeignKey('personnels.id'))
    orders = db.relationship('Order', backref='client', lazy='dynamic')

    @staticmethod
    def get_or_create(personnel_id):
        '''
        always use this function when create or get object
        example:
        Client.get_or_create(personnel_id=3)
        '''
        personnel = Personnel.query.get(personnel_id)
        if personnel:
            client = Client.query.filter_by(personnel_id=personnel_id).first()
            if client:
                return client
            else:
                new_client = Client(personnel_id=personnel_id)
                db.session.add(new_client)
                db.session.commit()
                return new_client
        else:
            return {"message": "he/she is not our Personnel"}
