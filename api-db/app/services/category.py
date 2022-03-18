from unicodedata import category
from werkzeug.exceptions import BadRequest
from flask import request
from app.models.category import Category
from app import db


class CategoryService:
    def get_category_by_id(id):
        category = Category.query.filter(Category.id == id).first()

        if not category:
            raise BadRequest("Category not found")

        return category

    def get_categories():
        categories = Category.query.all()
        if not categories:
            return []

        return categories

    def create_category(payload):
        name = payload["name"]
        img_url = payload["imgUrl"]

        if not name:
            raise BadRequest("Category pool needs a name")
        category_exists = Category.query.filter(Category.name == name).first()

        if category_exists:
            raise BadRequest("Category already exists")

        else:
            category = Category(name=name, img_url=img_url)
            db.session.add(category)
            db.session.commit()
            return category
