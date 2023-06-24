from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from config import config

db = SQLAlchemy()
api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    api.init_app(app)
    
    from .users import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    from .orders import order as order_blueprint
    app.register_blueprint(order_blueprint, url_prefix='/order')

    from .foods import food as food_blueprint
    app.register_blueprint(food_blueprint, url_prefix='/food')

    return app