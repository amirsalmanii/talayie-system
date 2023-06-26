from flask_restx import Resource, fields
from app import db, api 
from . import order_ns
from .models import Order, OrderItem
from app.users.models import Client


@order_ns.route("/user/<int:personnel_id>")
class ClientOrderDetailCreate(Resource):
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

    order_list_serializer = api.model(
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

    order_create_update_serializer = api.model(
        "Order",
        {
            "is_paid": fields.Boolean,
        }
    )

    order_item_serializer_2 = api.model(
        "OrderItem",
        {
            "items": fields.String, # "[1, 2, 3]"
            "table_number": fields.Integer,
            "items_counts": fields.String,
        }
    )

    @order_ns.marshal_with(order_list_serializer)
    def get(self, personnel_id):
        client = Client.query.filter_by(personnel_id=personnel_id).first()
        try:
            last_client_order = client.orders.all()[-1]
            last_client_order.calculate_total_price()
            return last_client_order
        except:
            return {}
    
    @order_ns.marshal_with(order_list_serializer)
    @order_ns.expect(order_item_serializer_2)
    def post(self, personnel_id):
        data = order_ns.payload
        table_number = data.get("table_number")
        items = eval(data.get("items"))
        items_counts = eval(data.get("items_counts"))
        client = Client.query.filter_by(personnel_id=personnel_id).first()
        if client:
            
            new_order = Order(table_number=table_number, client_id=client.id)
            db.session.add(new_order)
            db.session.commit()
            
            for index, food in enumerate(items):
                new_order_item = OrderItem(
                    food_id=food,
                    order_id=new_order.id,
                    count=items_counts[index]
                )
                new_order_item.calculate_total_price()
                db.session.add(new_order_item)
                db.session.commit()
            
            new_order.calculate_total_price()
            return new_order
        else:
            return Client.get_or_create(personnel_id)


@order_ns.route("/pay/order/")
class PayOrder(Resource):
    # serializer
    serializer_pay_order = api.model(
        "Order",
        {
            "id": fields.Integer,
        }
    )

    @order_ns.expect(serializer_pay_order)
    def put(self):
        order_id = order_ns.payload.get("id")    
        order_obj = Order.query.get(order_id)
        if order_obj:
            order_obj.pay_order()
            return {"message": "success"}
        return {}
