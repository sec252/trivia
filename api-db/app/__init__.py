from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from .api import blueprint as api

app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
app.register_blueprint(api)


@app.route("/")
def hello_world():
    return jsonify(hello="world")
