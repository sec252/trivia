from werkzeug.exceptions import BadRequest
from app.models.users import User
from app import db

#  Dummy Data

users_list = [
    {"id": 1, "username": "David"},
    {"id": 2, "username": "Chance"},
    {"id": 3, "username": "Rob"},
]


class UserService:
    def get_user_by_id(id):
        user = User.query.filter(User.id == id).first()

        if not user:
            raise BadRequest("User not found")

        return user

    def get_users():
        users = User.query.all()
        if not users:
            return users_list

        return users

    def create_user(username):
        if not username:
            raise BadRequest("need user name")
        else:
            new_user = User(username=username)
            db.session.add(new_user)
            db.session.commit()
            return new_user

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
