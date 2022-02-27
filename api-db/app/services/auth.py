from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash
from app.models.users import User
from flask import jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    jwt_required,
)
from app import db


class AuthService:
    def register_user(username, password):
        user = User.query.filter(User.username == username).first()

        if not user:
            new_user = User(
                username=username, password=generate_password_hash(password)
            )
            db.session.add(new_user)
            db.session.commit()
            access_token = create_access_token(identity=new_user.id)
            refresh_token = create_refresh_token(identity=new_user.id)
            response = jsonify({"msg": "Sign up successful"})
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            return response
        raise BadRequest("Username is already taken")

    def login_user(username, password):
        user = User.query.filter(User.username == username).first()
        if not user:
            raise BadRequest("Invalid Credentials")
        if user.authenticate(password):
            response = jsonify({"msg": "login successful"})
            access_token = create_access_token(identity=user.id)
            set_access_cookies(response, access_token)
            refresh_token = create_refresh_token(identity=user.id)
            response = jsonify({"msg": "Login successful"})
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            return response
        raise BadRequest("Invalid Credentials")

    def logout_user():
        response = jsonify({"msg": "Logout successful"})
        unset_jwt_cookies(response)
        return response
