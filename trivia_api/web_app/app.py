from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .api import blueprint as api

app = Flask(__name__)
app.register_blueprint(api)


if __name__ == '__main__':
    app.run(debug=True)