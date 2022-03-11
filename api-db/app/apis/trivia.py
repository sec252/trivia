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

author = api.model(
    "Author",
    {
        "id": fields.Integer,
        "username": fields.String,
    },
)
category = api.model(
    "Category",
    {
        "id": fields.Integer,
        "name": fields.String,
    },
)
plays = api.model(
    "Plays",
    {
        "plays": fields.Integer,
    },
)
trivia_pools = api.model(
    "TriviaPools",
    {
        "id": fields.Integer,
        "name": fields.String,
        "createdDate": fields.String(attribute="created_date"),
        "category": fields.String,
        "plays": fields.Integer,
        "author": fields.Nested(author),
    },
)

trivia = api.model(
    "Trivia",
    {
        "id": fields.Integer,
        "name": fields.String,
        "questions": fields.List(fields.Nested(trivia_question)),
        "category": fields.String,
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
    @api.marshal_with(trivia, envelope="trivia")
    def get(self, trivia_pool_id):
        return TriviaService.get_trivia_pool_by_id(trivia_pool_id)

    @api.marshal_with(trivia, envelope="trivia")
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


@api.route("/user")
class TriviaPoolUserCollection(Resource):
    @api.marshal_with(trivia_pools, envelope="body")
    def get(self):
        return TriviaService.get_user_trivia_pools()


@api.route("/category/<int:id>")
@api.param("id", "Category Identifier")
class TriviaPoolCategoryCollection(Resource):
    @api.marshal_with(trivia_pools, envelope="body")
    def get(self, id):
        return TriviaService.get_category_trivia_pools(id)


@api.route("/<int:trivia_pool_id>/plays")
@api.param("trivia_pool_id", "Trivia Pool Identifier")
class TriviaPlaysItem(Resource):
    @api.marshal_with(plays, envelope="body")
    def put(self, trivia_pool_id):
        payload = request.json
        return TriviaService.update_play_by_id(trivia_pool_id, payload)
