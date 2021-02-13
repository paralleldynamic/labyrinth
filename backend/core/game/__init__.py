from flask import Blueprint
from flask_restx import Api

from core.game.controller import ns as game_ns

blueprint = Blueprint('game_api', __name__)
api = Api(blueprint)

api.add_namespace(game_ns, path='/game')
