import datetime
from werkzeug.exceptions import BadRequest
from flask import request, jsonify
from app.models.users import User, Role
from app.models.trivia import (
    Trivia,
    TriviaPool,
    TriviaUserPlays,
    TriviaIPPlay,
    TriviaUserScores,
)
from app.models.category import Category
from app.utils.helpers import isCorrect
from app import db
from flask_jwt_extended import (
    current_user,
    jwt_required,
)


class TriviaService:
    def get_trivia_pool_by_id(id):
        trivia_pool = TriviaPool.query.filter(TriviaPool.id == id).first()

        if not trivia_pool:
            raise BadRequest("Trivia not found")

        return trivia_pool

    def get_trivia_pools():
        args = request.args
        slug = args.get("slug", default=None, type=str)
        query = TriviaPool.query
        if slug:
            category = Category.query.filter(Category.slug == slug).first()
            if not category:
                raise BadRequest("Category does not exist")
            query = query.filter(TriviaPool.category_id == category.id)
        page = args.get("page", default=None, type=int)
        per_page = args.get("perPage", default=None, type=int)
        order = args.get("order", default="most", type=str)
        search = args.get("search", default=None)
        if order == "most":
            query = query.order_by(TriviaPool.plays.desc())
        elif order == "least":
            query = query.order_by(TriviaPool.plays.asc())
        elif order == "asc":
            query = query.order_by(TriviaPool.name.asc())
        elif order == "desc":
            query = query.order_by(TriviaPool.name.desc())
        elif order == "newest":
            query = query.order_by(TriviaPool.created_date.desc())
        else:
            query = query.order_by(TriviaPool.created_date.asc())
        if search:
            query = query.filter(TriviaPool.name.ilike(f"%{search}%"))
        trivia_pools = query.paginate(page=page, per_page=per_page)

        return trivia_pools

    def get_trivia_pools_by_slug():
        args = request.args
        query = TriviaPool.query.filter(TriviaPool.category_id == category.id).all()

        page = args.get("page", default=None, type=int)
        per_page = args.get("perPage", default=None, type=int)
        order = args.get("order", default="most", type=str)
        search = args.get("search", default=None)
        if order == "most":
            query = query.order_by(TriviaPool.plays.desc())
        elif order == "least":
            query = query.order_by(TriviaPool.plays.asc())
        elif order == "asc":
            query = query.order_by(TriviaPool.name.asc())
        elif order == "desc":
            query = query.order_by(TriviaPool.name.desc())
        elif order == "newest":
            query = query.order_by(TriviaPool.created_date.desc())
        else:
            query = query.order_by(TriviaPool.created_date.asc())
        if search:
            query = query.filter(TriviaPool.name.ilike(f"%{search}%"))
        trivia_pools = query.paginate(page=page, per_page=per_page)

        return trivia_pools

    def get_category_trivia_pools(id):
        trivia_pools = TriviaPool.query.filter(TriviaPool.category_id == id).all()
        return trivia_pools

    @jwt_required()
    def get_user_trivia_pools():
        trivia_pools = TriviaPool.query
        if current_user.role == Role.USER:
            trivia_pools = trivia_pools.filter(
                TriviaPool.creator_id == current_user.id
            ).all()

        if current_user.role == Role.ADMIN:
            trivia_pools = trivia_pools.all()

        return trivia_pools

    @jwt_required()
    def create_trivia_pool(payload):
        name = payload["name"]
        category_id = payload["category_id"]
        if not name:
            raise BadRequest("Trivia pool needs a name")
        if not category_id:
            raise BadRequest("Trivia pool needs a category")
        trivia_exists = TriviaPool.query.filter(TriviaPool.name == name).first()
        if trivia_exists:
            raise BadRequest(f"Trivia name: '{name}' already taken")
        else:
            trivia = TriviaPool(
                name=name.lower().title(),
                category_id=category_id,
                creator_id=current_user.id,
            )
            db.session.add(trivia)
            db.session.commit()
            return trivia

    @jwt_required()
    def edit_trivia_pool(id, payload):
        trivia_pool = TriviaService.get_trivia_pool_by_id(id)
        name = payload["name"]
        if not name:
            raise BadRequest("Trivia pool needs a name")

        trivia_pool.name = name.lower().title()

        db.session.commit()
        return trivia_pool

    @jwt_required()
    def delete_trivia(id):
        trivia = TriviaService.get_trivia_pool_by_id(id)
        Trivia.query.filter(Trivia.trivia_pool_id == trivia.id).delete(
            synchronize_session=False
        )
        TriviaUserPlays.query.filter(TriviaUserPlays.trivia_id == trivia.id).delete(
            synchronize_session=False
        )
        TriviaUserScores.query.filter(TriviaUserScores.trivia_id == trivia.id).delete(
            synchronize_session=False
        )
        db.session.delete(trivia)
        db.session.commit()
        return None

    def get_question_by_id(id):
        question = Trivia.query.filter(Trivia.id == id).first()

        if not question:
            raise BadRequest("Question does not exist")
        return question

    @jwt_required()
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

    @jwt_required()
    def delete_question(id):
        question = TriviaService.get_question_by_id(id)
        db.session.delete(question)
        db.session.commit()
        return None

    @jwt_required(optional=True)
    def update_play_by_id(id, payload):
        trivia = TriviaService.get_trivia_pool_by_id(id)
        user_id = payload["userId"]
        user = User.query.get(user_id)
        if user and user.id == current_user.id:
            user_plays = TriviaUserPlays.query.filter(
                TriviaUserPlays.trivia_id == trivia.id,
                TriviaUserPlays.user_id == user.id,
            ).first()
            if user_plays:
                user_plays.plays = user_plays.plays + 1
            else:
                db.session.add(
                    TriviaUserPlays(trivia_id=trivia.id, user_id=user.id, plays=1)
                )
        elif not current_user:
            ip = request.remote_addr
            ip_plays = TriviaIPPlay.query.filter(
                TriviaIPPlay.trivia_id == trivia.id, TriviaIPPlay.ip == ip
            ).first()
            if ip_plays:
                ip_plays.plays = ip_plays.plays + 1
            else:
                db.session.add(TriviaIPPlay(trivia_id=trivia.id, ip=ip, plays=1))

        trivia.plays = trivia.plays + 1
        db.session.commit()
        return trivia

    @jwt_required(optional=True)
    def create_score(id, payload):
        trivia = TriviaService.get_trivia_pool_by_id(id)
        user_id = payload["userId"]
        correct = payload["correct"]
        wrong = payload["wrong"]
        user = User.query.get(user_id)
        if user and user.id == current_user.id:

            new_score = TriviaUserScores(
                trivia_id=trivia.id, user_id=user.id, correct=correct, wrong=wrong
            )

            db.session.add(new_score)
            db.session.commit()

            return jsonify(
                {
                    "score": new_score.score,
                    "correct": new_score.correct,
                    "wrong": new_score.wrong,
                    "date": new_score.played_date,
                }
            )

        elif not current_user:
            total = correct + wrong
            return jsonify(
                {
                    "score": round((correct / total) * 100),
                    "correct": correct,
                    "wrong": wrong,
                    "date": datetime.datetime.utcnow(),
                }
            )

    @jwt_required(optional=True)
    def answer_question(id, payload):

        response = payload["response"]
        if not response:
            raise BadRequest("Need a response")
        question = TriviaService.get_question_by_id(id)

        return isCorrect(question.answer, response)
