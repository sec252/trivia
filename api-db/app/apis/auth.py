from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.auth import AuthService


api = Namespace("auth", "Authentication Resource")

user = api.model(
    "UserModel",
    {
        "id": fields.Integer,
        "username": fields.String,
        "active": fields.Boolean,
        "role": fields.String(attribute="role.value"),
    },
)


@api.route("/register")
class RegisterUser(Resource):
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        return AuthService.register_user(username, password)


@api.route("/login")
class LoginUser(Resource):
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        return AuthService.login_user(username, password)


@api.route("/logout")
class LogoutUser(Resource):
    def post(self):
        return AuthService.logout_user()


@api.route("/user")
class AuthUser(Resource):
    @api.marshal_with(user, envelope="user")
    def get(self):
        return AuthService.user()
