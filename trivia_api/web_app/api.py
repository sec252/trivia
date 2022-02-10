from flask import Blueprint
from flask_restx import Api


from .apis.users import api as ns1


blueprint = Blueprint('api', __name__, url_prefix='/api/')

api = Api(
    blueprint,
    title='My Title',
    version='1.0',
    description='A description'
  )

api.add_namespace(ns1)