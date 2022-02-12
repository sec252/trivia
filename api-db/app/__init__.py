from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .api import blueprint as api

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
app.register_blueprint(api)


@app.route("/")
def hello_world():
    return jsonify(hello="world")
