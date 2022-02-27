from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from ..services.auth import AuthService
from flask_jwt_extended import (
    jwt_required,
)

api = Namespace("auth", "Authentication Resource")

register = api.model(
    "Register",
    {
        "username": fields.String,
        "password": fields.String,
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
