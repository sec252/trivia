from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash
from app.models.users import User, Role
from app import db
from flask_jwt_extended import (
    current_user,
    jwt_required,
)

#  Dummy Data


class UserService:
    def get_user_by_id(id):
        user = User.query.filter(User.id == id).first()

        if not user:
            raise BadRequest("User not found")

        return user

    @jwt_required()
    def get_users():
        users = User.query
        if current_user.role == Role.USER:
            users = users.filter(User.id == current_user.id).all()

        if current_user.role == Role.ADMIN:
            users = users.all()

        return users

    @jwt_required()
    def create_user(payload):
        if current_user.role == Role.ADMIN:
            username = payload["username"]
            password = payload["password"]
            if not username:
                raise BadRequest("need user name")
            else:
                new_user = User(
                    username=username, password=generate_password_hash(password)
                )
                db.session.add(new_user)
                db.session.commit()
                return new_user
        raise BadRequest("Not authorized")

    def edit_user(id, payload):
        user = UserService.get_user_by_id(id)
        username = payload["username"]
        if not username:
            raise BadRequest("need username")
        active = payload["active"]
        user.username = username
        user.active = active
        db.session.commit()
        return user

    def delete_user(id):
        user = UserService.get_user_by_id(id)
        db.session.delete(user)
        db.session.commit()
        return None
