from app import db
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def authenticate(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User %r>" % self.username
