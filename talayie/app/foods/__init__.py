from flask import Blueprint
from flask_restx import Namespace
from app import api

APP_NAMESPACE = 'food'
food = Blueprint(APP_NAMESPACE, __name__)
food_ns = Namespace(APP_NAMESPACE)
api.add_namespace(food_ns)

from . import views, models