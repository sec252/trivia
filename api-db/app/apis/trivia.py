from flask_restx import Namespace, Resource, fields
from flask import request
from ..services.trivia import TriviaService

api = Namespace("trivias", "Trivia Resource")

trivia_question = api.model(
    "TriviaQuestion",
    {
        "id": fields.Integer,
        "text": fields.String,
        "answer": fields.String,
    },
)

trivia_pools = api.model(
    "TriviaPools",
    {
        "id": fields.Integer,
        "name": fields.String,
        "questions": fields.List(fields.Nested(trivia_question)),
    },
)


#  Dummy Data


@api.route("/")
class TriviaPoolCollection(Resource):
    @api.marshal_with(trivia_pools, envelope="body")
    def get(self):
        return TriviaService.get_trivia_pools()

    @api.marshal_with(trivia_pools, envelope="trivia")
    def post(self):
        payload = request.json
        return TriviaService.create_trivia_pool(payload)


@api.route("/<int:trivia_pool_id>")
@api.param("trivia_pool_id", "Trivia Pool Identifier")
class TriviaPoolItem(Resource):
    @api.marshal_with(trivia_pools, envelope="trivia")
    def get(self, trivia_pool_id):
        return TriviaService.get_trivia_pool_by_id(trivia_pool_id)

    @api.marshal_with(trivia_pools, envelope="trivia")
    def put(self, trivia_pool_id):
        payload = request.json
        return TriviaService.edit_trivia_pool(trivia_pool_id, payload)

    def delete(self, trivia_pool_id):
        return TriviaService.delete_trivia(trivia_pool_id)


@api.route("/<int:trivia_pool_id>/questions")
@api.param("trivia_pool_id", "Trivia Pool Identifier")
class TriviaPoolQuestions(Resource):
    @api.marshal_with(trivia_pools, envelope="trivia")
    def get(self, trivia_pool_id):
        # Get all questions of given trivia pool
        return TriviaService.get_trivia_pool_by_id(trivia_pool_id)

    @api.marshal_with(trivia_question, envelope="question")
    def post(self, trivia_pool_id):
        payload = request.json
        return TriviaService.create_question(trivia_pool_id, payload)


@api.route("/questions/<int:question_id>")
@api.param("question_id", "Question Identifier")
class TriviaPoolQuestions(Resource):
    def delete(self, question_id):
        # Get all questions of given trivia pool
        return TriviaService.delete_question(question_id)
