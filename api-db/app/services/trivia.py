from werkzeug.exceptions import BadRequest
from flask import request
from app.models.users import User
from app.models.trivia import Trivia, TriviaPool
from app import db

#  Dummy Data
users_list = [
    {"id": 1, "username": "David"},
    {"id": 2, "username": "Chance"},
    {"id": 3, "username": "Rob"},
]


class TriviaService:
    def get_trivia_pool_by_id(id):
        trivia_pool = TriviaPool.query.filter(TriviaPool.id == id).first()

        if not trivia_pool:
            raise BadRequest("Trivia not found")

        return trivia_pool

    def get_trivia_pools():
        trivia_pools = TriviaPool.query.all()
        if not trivia_pools:
            return []

        return trivia_pools

    def create_trivia_pool(payload):
        name = payload["name"]
        if not name:
            raise BadRequest("Trivia pool needs a name")
        else:
            trivia = TriviaPool(name=name)
            db.session.add(trivia)
            db.session.commit()
            return trivia

    def edit_trivia_pool(id, payload):
        trivia_pool = TriviaService.get_trivia_pool_by_id(id)
        name = payload["name"]
        if not name:
            raise BadRequest("Trivia pool needs a name")

        trivia_pool.name = name

        db.session.commit()
        return trivia_pool

    def delete_trivia(id):
        trivia = TriviaService.get_trivia_pool_by_id(id)
        db.session.delete(trivia)
        db.session.commit()
        return None

    def get_quesition_by_id(id):
        question = Trivia.query.filter(Trivia.id == id).first()

        if not question:
            raise BadRequest("Question does not exist")
        return question

    def create_question(id, payload):

        text = payload["text"]
        answer = payload["answer"]

        if not text or not answer:
            raise BadRequest("Missing fields")
        else:
            trivia_pool = TriviaService.get_trivia_pool_by_id(id)
            new_question = Trivia(
                text=text, answer=answer, trivia_pool_id=trivia_pool.id
            )
            db.session.add(new_question)
            db.session.commit()
            return new_question

    def delete_question(id):
        # TODO DELETE QUESTION BY ID
        question = TriviaService.get_quesition_by_id(id)
        db.session.delete(question)
        db.session.commit()
        return None
