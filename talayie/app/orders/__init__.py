from flask import Blueprint
from flask_restx import Namespace
from app import api

APP_NAMESPACE = 'order'
order = Blueprint(APP_NAMESPACE, __name__)
order_ns = Namespace(APP_NAMESPACE)
api.add_namespace(order_ns)

from . import views, models