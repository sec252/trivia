from flask_restx import Namespace, Resource, fields
from flask import request
from ..services.users import UserService


api = Namespace("users", "Users Resource")

users = api.model(
    "UsersModel",
    {
        "id": fields.Integer,
        "username": fields.String,
    },
)

user = api.model(
    "UserModel",
    {
        "id": fields.Integer,
        "username": fields.String,
        "role": fields.String(attribute="role.value"),
        "active": fields.Boolean,
    },
)


@api.route("/")
class UsersCollection(Resource):
    @api.marshal_with(users, envelope="users")
    def get(self):

        return UserService.get_users()

    @api.marshal_with(user, envelope="user")
    def post(self):
        payload = request.json
        return UserService.create_user(payload)


@api.route("/<int:user_id>")
@api.param("user_id", "User identifier")
class UserItem(Resource):
    @api.marshal_with(user, envelope="user")
    def get(self, user_id):
        return UserService.get_user_by_id(user_id)

    @api.marshal_with(user, envelope="user")
    def put(self, user_id):
        payload = request.json
        return UserService.edit_user(user_id, payload)

    def delete(self, user_id):
        return UserService.delete_user(user_id)
