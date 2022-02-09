from flask_restx import Namespace, Resource

api = Namespace('users', 'Users Resource' )

#  Dummy Data

users_list = [
    {
        "id": 1,
        "username": "David"
    },
     {
        "id": 2,
        "username": "Chance"
    },
      {
        "id": 1,
        "username": "Rob"
    }
]

@api.route("/")
class UsersCollection(Resource):
    def get(self):
        return users_list
    

        