from flask_restx import Resource, fields
from app import db, api 
from . import order_ns
from .models import Order, OrderItem
from app.users.models import Client


@order_ns.route("/user/<int:personnel_id>")
class ClientOrderDetail(Resource):
    # serializer
    food_serializer = api.model(
        "Food",
        {
            "name": fields.String,
            "price": fields.Integer
        }
    )
    order_items_serializer = api.model(
        "OrderItem",
        {
            "foods": fields.Nested(food_serializer),
            "count": fields.Integer,
            "price": fields.Integer,
        }
    )

    order_serializer = api.model(
        "Order", {
            "id": fields.Integer,
            "is_paid": fields.Boolean,
            "paid_date": fields.DateTime,
            "create_date": fields.DateTime,
            "total_price": fields.Integer,
            "table_number": fields.Integer,
            "order_items": fields.List(fields.Nested(order_items_serializer)),
        }
    )

    @order_ns.marshal_with(order_serializer)
    def get(self, personnel_id):
        client = Client.query.filter_by(personnel_id=personnel_id).first()
        try:
            last_client_order = client.orders.all()[-1]
            return last_client_order
        except:
            return {}
