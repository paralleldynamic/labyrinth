from flask import Blueprint
from flask_restx import Api

from core.user.controller import ns as user_ns

blueprint = Blueprint('user_api', __name__)
api = Api(blueprint)

api.add_namespace(user_ns, path='/user')
