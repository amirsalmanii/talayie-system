import datetime
from app import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    foods = db.relationship("Food", backref="category", lazy='dynamic')


class Food(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    price = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    order_items = db.relationship("OrderItem", backref="food", lazy='dynamic')

