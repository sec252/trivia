from flask_restx import Namespace, Resource, fields
from flask import request
from ..services.users import UserService
from app.models.users import User
from flask_jwt_extended import jwt_required, current_user
from app import jwt

api = Namespace("users", "Users Resource")

users = api.model(
    "UserModel",
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
        "active": fields.Boolean,
    },
)

# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@api.route("/")
class UsersCollection(Resource):
    @api.marshal_with(users, envelope="users")
    def get(self):

        return UserService.get_users()

    @api.marshal_with(user, envelope="user")
    def post(self):
        username = request.json["username"]
        return UserService.create_user(username)


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
