from flask import Flask

from config import Config
from .api.routes import api
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)


app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(api)

from . import routes
from . import models