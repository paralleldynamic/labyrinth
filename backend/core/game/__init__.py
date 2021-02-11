from flask import Blueprint
from flask_restx import Api

from core.game.controller import ns as game_ns

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

api.add_namespace(game_ns, path='/game')
