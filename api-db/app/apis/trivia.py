from flask_restx import Namespace, Resource, fields
from flask import request


api = Namespace("trivias", "Trivia Resource")

trivia_pool = api.model(
    "TriviaPool",
    {
        "id": fields.Integer,
        "name": fields.String,
    },
)
#  Dummy Data


@api.route("/")
class TriviaCollection(Resource):
    @api.marshal_with(trivia_pool, envelope="body")
    def get(self):
        from app.models.trivia import TriviaPool

        trivia_pools = TriviaPool.query.all()
        if not trivia_pools:
            return []

        return trivia_pools

    @api.marshal_with(trivia_pool, envelope="trivia")
    def post(self):
        from app.models.trivia import TriviaPool
        from app import db

        name = request.json["name"]
        if not name:
            print("Error")
        else:
            trivia = TriviaPool(name=name)
            db.session.add(trivia)
            db.session.commit()
            return trivia
