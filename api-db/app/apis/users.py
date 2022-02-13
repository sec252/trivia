from flask_restx import Namespace, Resource, fields
from flask import request


api = Namespace("users", "Users Resource")

user = api.model(
    "UserModel",
    {
        "id": fields.Integer,
        "username": fields.String,
    },
)
#  Dummy Data

users_list = [
    {"id": 1, "username": "David"},
    {"id": 2, "username": "Chance"},
    {"id": 3, "username": "Rob"},
]


@api.route("/")
class UsersCollection(Resource):
    @api.marshal_with(user, envelope="users")
    def get(self):
        from app.models.users import User

        users = User.query.all()
        if not users:
            return users_list

        return users

    @api.marshal_with(user, envelope="user")
    def post(self):
        from app.models.users import User
        from app import db

        username = request.json["username"]
        if not username:
            print("Error")
        else:
            new_user = User(username=username)
            db.session.add(new_user)
            db.session.commit()
            return new_user
