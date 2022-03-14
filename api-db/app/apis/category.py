from flask_restx import Namespace, Resource, fields
from flask import request
from ..services.category import CategoryService

api = Namespace("category", "Category Resource")

category = api.model(
    "Category",
    {
        "id": fields.Integer,
        "name": fields.String,
    },
)


#  Dummy Data


@api.route("/")
class CategoryCollection(Resource):
    @api.marshal_with(category, envelope="categories")
    def get(self):
        return CategoryService.get_categories()

    @api.marshal_with(category, envelope="category")
    def post(self):
        payload = request.json
        return CategoryService.create_category(payload)
