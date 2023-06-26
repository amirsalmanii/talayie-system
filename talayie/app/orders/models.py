import datetime
from app import db
from app.foods.models import Food


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    is_paid = db.Column(db.Boolean, default=False)
    paid_date = db.Column(db.DateTime) #TODO when paid is true set time
    create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    total_price = db.Column(db.Integer)
    table_number = db.Column(db.Integer)
    order_items = db.relationship('OrderItem', backref='order', lazy='dynamic')
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))

    def calculate_total_price(self):
        all_items = self.order_items.all()
        total_price = 0
        for item in all_items:
            total_price += item.price

        self.total_price = total_price
    
    def pay_order(self):
        self.is_paid = True
        self.paid_date = datetime.datetime.utcnow()


class OrderItem(db.Model):
    __tablename__ = 'orderitems'
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    count = db.Column(db.Integer)
    price = db.Column(db.Integer) #TODO function for calculate total price of this order items
    foods = db.relationship("Food", backref="orderitems")

    def calculate_total_price(self):
        food_obj = Food.query.get(self.food_id)
        if food_obj:
            self.price = food_obj.price * self.count
