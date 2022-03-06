from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash
from app.models.users import User
from flask import jsonify
from flask_jwt_extended import (
    create_access_token,
    unset_jwt_cookies,
    current_user,
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

            return jsonify(access_token=access_token)
        raise BadRequest("Username is already taken")

    def login_user(username, password):
        user = User.query.filter(User.username == username).first()
        if not user:
            raise BadRequest("Invalid Credentials")
        if user.authenticate(password):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token)
        raise BadRequest("Invalid Credentials")

    def logout_user():
        response = jsonify({"msg": "Logout successful"})
        unset_jwt_cookies(response)
        return response

    @jwt_required()
    def user():
        return current_user
