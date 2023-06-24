from flask import Blueprint
from flask_restx import Namespace
from app import api

APP_NAMESPACE = 'user'
user = Blueprint(APP_NAMESPACE, __name__)
user_ns = Namespace(APP_NAMESPACE)
api.add_namespace(user_ns)

from . import views, models