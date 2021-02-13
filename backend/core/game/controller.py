from flask import request
from flask_restx import Namespace, Resource, fields
from sqlalchemy.exc import IntegrityError

from .models import Game as GameDAO

game_dao = GameDAO()

ns = Namespace("game", description="game related operations")
game = ns.model("game", {
    "id": fields.String(description="public ID of the game"),
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
        return GameDAO().get_list()

    @ns.response(201, 'Game successfully created.')
    @ns.response(500, "Unhandled servor error.")
    @ns.doc('create a new game')
    @ns.expect(game, Validate=True)
    def post(self):
        """Creates a new game."""
        data = request.json
        try:
            game = game_dao.create(**data)
            response_object = {
                'status': "success",
                "messages": f"Successfully created game { game.title }.",
            }
            return response_object, 201
        except IntegrityError as e:
            response_object = {
                "status": "fail",
                "message": "Game already exists."
            }
            return response_object, 409
        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "There was an unspecified error."
            }
            return response_object, 500

@ns.route('/<id>')
@ns.param('id', 'Unique id of game')
@ns.response(404, 'Game not found.')
class Game(Resource):
    @ns.doc('Get a game by public ID.')
    @ns.marshal_with(game)
    def get(self, id):
        """Get a game from the database given its public ID."""
        game = game_dao.get_by_id(id)
        if not game:
            ns.abort(404)
        else:
            return game, 200

    @ns.response(200, "Game successfully deleted.")
    @ns.doc("Delete a game using the title as a reference. This endpoint is not case sensitive.")
    @ns.marshal_with(game)
    def delete(self, id):
        """Delete a game from the database using its title."""
        game = game_dao.get_by_id(id)
        # TODO better error handling -- e.g. if the game doesn't exist already
        if not game:
            ns.abort(404)
        else:
            game.delete()
            response_object = {
                'status': "success",
                "messages": f"Successfully deleted game { game.title }.",
            }
            return response_object, 200

@ns.route('/<title>')
@ns.param('title', 'Unique title of game')
@ns.response(404, 'Game not found.')
class Game(Resource):
    @ns.doc('Get a game by title. This endpoint is not case sensitive.')
    @ns.marshal_with(game)
    def get(self, title):
        """Get a game from the database given its title."""
        game = game_dao.get_by_title(title)
        if not game:
            ns.abort(404)
        else:
            return game, 200

    @ns.response(200, "Game successfully deleted.")
    @ns.doc("Delete a game using the title as a reference. This endpoint is not case sensitive.")
    @ns.marshal_with(game)
    def delete(self, title):
        """Delete a game from the database using its title."""
        game = game_dao.get_by_title(title)
        # TODO better error handling -- e.g. if the game doesn't exist already
        if not game:
            ns.abort(404)
        else:
            game.delete()
            response_object = {
                'status': "success",
                "messages": f"Successfully deleted game { game.title }.",
            }
            return response_object, 200
