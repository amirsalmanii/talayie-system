import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from app import create_app, db
from app.foods.models import Category, Food
from app.users.models import (
   Organization,
   Role,
   Personnel,
   Client
)
from app.orders.models import Order, OrderItem


app_config = os.environ.get('FLASK_CONFIG') or 'default'
app = create_app(app_config)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
   # you can add your models here for flask shell import auto
   return dict(
      db=db,
      Category=Category,
      Food=Food,
      Organization=Organization,
      Role=Role,
      Personnel=Personnel,
      Client=Client,
      Order=Order,
      OrderItem=OrderItem,
   )