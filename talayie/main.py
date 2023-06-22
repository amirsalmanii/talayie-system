import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from app import create_app, db

app_config = os.environ.get('FLASK_CONFIG') or 'default'
app = create_app(app_config)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
   # you can add your models here for flask shell import auto
   return dict(db=db)