from flask_restx import Resource, fields
from app import db, api 
from . import food_ns
from .models import Food, Category


@food_ns.route("/categories")
class FoodCategories(Resource):
    # serializers
    category_list_serializer = api.model(
        "Category",
        {
            "id": fields.Integer,
            "name": fields.String
        }
    )

    create_update_food_category_serializer = api.model(
        "Category",
        {
            "name":fields.String,
        }
    )

    @food_ns.marshal_list_with(category_list_serializer)
    def get(self):
        return Category.query.all()
    
    @food_ns.expect(create_update_food_category_serializer)
    @food_ns.marshal_with(category_list_serializer)
    def post(self):
        data = food_ns.payload
        name = data.get("name")
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return new_category


@food_ns.route("/")
class FoodListCreate(Resource):
    # serializers
    nested_category_list_serializer = api.model(
        "Category",
        {
            "name": fields.String
        }
    )

    food_list_serializer = api.model(
        "Food",
        {
            "id": fields.Integer,
            "name": fields.String,
            "price": fields.Integer,
            "is_available": fields.Boolean,
            "categories": fields.Nested(nested_category_list_serializer),
        }
    )

    food_create_update_serializer = api.model(
        "Food",
        {
            "name": fields.String,
            "price": fields.Integer,
            "is_available": fields.Boolean,
            "category_id": fields.Integer,
        }
    )

    @food_ns.marshal_list_with(food_list_serializer)
    def get(self):
        return Food.query.filter_by(is_available=True).all()
    
    @food_ns.marshal_with(food_list_serializer)
    @food_ns.expect(food_create_update_serializer)
    def post(self):
        # for admin panel
        data = food_ns.payload
        name, price = data.get("name"), data.get("price")
        is_available, category_id = data.get("is_available"), data.get("category_id")
        
        new_food = Food(name=name, price=price, is_available=is_available, category_id=category_id)
        db.session.add(new_food)
        db.session.commit()
        return new_food
