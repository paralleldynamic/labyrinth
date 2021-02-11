from flask import request
from flask_restx import Namespace, Resource, fields

from .models import get_a_game, get_all_games, save_new_game

ns = Namespace("game", description="game related operations")
game = ns.model("game", {
    "id": fields.String(description="public ID of game"),
    "title": fields.String(required=True, description="game title"),
    "publisher_website": fields.String(description="website of publisher of the game"),
    "logo_img_src": fields.String(description="source for the game's logo"),
    "logo_img_alt": fields.String(description="alt text for the "),
    "tagline": fields.String(description="tagline to describe the game"),
})

@ns.route('/')
class GameList(Resource):
    @ns.doc('list_of_games')
    @ns.marshal_list_with(game, envelope='data')
    def get(self):
        """List of all games."""
        return get_all_games()

    @ns.response(201, 'Game successfully created.')
    @ns.doc('create a new game')
    @ns.expect(game, Validate=True)
    def post(self):
        """Creates a new Game"""
        data = request.json
        return save_new_game(data)

@ns.route('/<title>')
@ns.param('title', 'Unique title of game')
@ns.response(404, 'Game not found.')
class Game(Resource):
    @ns.doc('get a game')
    @ns.marshal_with(game)
    def get(self, title):
        """get a game given its title"""
        game = get_a_game(title)
        if not game:
            ns.abort(404)
        else:
            return game
