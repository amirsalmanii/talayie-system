import datetime
from app import db


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    is_paid = db.Column(db.Boolean, default=False)
    paid_date = db.Column(db.DateTime) #TODO when paid is true set time
    create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    total_price = db.Column(db.Integer)
    table_number = db.Column(db.Integer)
    order_items = db.relationship('OrderItem', backref='role', lazy='dynamic')
    client = db.Column(db.Integer, db.ForeignKey('clients.id'))


class OrderItem(db.Model):
    __tablename__ = 'orderitems'
    id = db.Column(db.Integer, primary_key=True)
    # food = db.Column(db.Integer, db.ForeignKey('foods.id'))
    order = db.Column(db.Integer, db.ForeignKey('orders.id'))
    count = db.Column(db.Integer)
    price = db.Column(db.Integer) #TODO function for calculate total price of this order items
