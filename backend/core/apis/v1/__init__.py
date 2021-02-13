from flask import Blueprint
from flask_restx import Api

from .game.controller import ns as game_ns
from .user.controller import ns as user_ns

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

api.add_namespace(game_ns, path='/game')
api.add_namespace(user_ns, path='/user')
