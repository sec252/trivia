from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
jwt = JWTManager(app)

from .api import blueprint as api

app.register_blueprint(api)
