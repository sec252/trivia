from unicodedata import category
from werkzeug.exceptions import BadRequest
from flask import request
from app.models.users import User, Role
from app.models.trivia import Trivia, TriviaPool
from app.models.category import Category
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

        trivia_pool.name = name.lower()

        db.session.commit()
        return trivia_pool

    def delete_trivia(id):
        trivia = TriviaService.get_trivia_pool_by_id(id)
        Trivia.query.filter(Trivia.trivia_pool_id == trivia.id).delete(
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
        question = TriviaService.get_question_by_id(id)
        db.session.delete(question)
        db.session.commit()
        return None

    # TODO need to update triva plays so that users
    # that played this trivia should not be able to update
    # the play again. Also need to start saving ip addresses
    # and doing the same. They cannot update the same trivia plays
    # again.
    def update_play_by_id(id, payload):
        trivia = TriviaService.get_trivia_pool_by_id(id)
        user_id = payload["userId"]
        user = User.query.get(user_id)
        print(user)
        trivia.plays = trivia.plays + 1
        db.session.commit()
        return trivia
