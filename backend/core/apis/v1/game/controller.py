from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, marshal
from sqlalchemy.exc import IntegrityError

from .contracts import ns, game, publisher
from .models import Game as GameDAO, Publisher as PublisherDAO

@ns.route('/')
class GameList(Resource):
    @ns.doc('list of all games')
    @ns.marshal_list_with(game)
    @jwt_required
    def get(self):
        """List of all games."""
        return GameDAO.get_list()

    @ns.response(201, 'Game successfully created.')
    @ns.response(500, "Unhandled server error.")
    @ns.doc('create a new game')
    @ns.expect(game, Validate=True)
    @jwt_required
    def post(self):
        """Creates a new game."""
        data = request.form or request.json
        try:
            created_game = GameDAO.create(**data)
            response_object = {
                "status": "success",
                "messages": f"Successfully created game { created_game.title }.",
                "game": marshal(created_game, game),
            }
            response_code = 201
        except IntegrityError as e:
            response_object = {
                "status": "fail",
                "message": "Game already exists."
            }
            response_code = 409
            raise e
        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "Unhandled server error."
            }
            response_code = 500
            print(e)
            raise e
        finally:
            return response_object, response_code

@ns.route('/id/<id>')
@ns.param('id', 'Unique id of game')
@ns.response(404, 'Game not found.')
class Game(Resource):
    @ns.doc('Get a game by public ID.')
    @ns.marshal_with(game)
    @jwt_required
    def get(self, id):
        """Get a game from the database given its public ID."""
        game = GameDAO.get_by_id(id)
        if not game:
            ns.abort(404)
        else:
            return game, 200

    @ns.response(200, "Success.")
    @ns.response(500, "Unhandled server error.")
    @ns.doc("Update a game using the id. Expects a game.")
    @ns.expect(game, Validate=True)
    @jwt_required
    def post(self, id):
        """Update a game from the database given its public ID."""
        data = request.form or request.json
        game = GameDAO.get_by_id(id)
        if not game:
            ns.abort(404)


    @ns.response(200, "Game successfully deleted.")
    @ns.doc("Delete a game using the id as a reference.")
    @jwt_required
    def delete(self, id):
        """Delete a game from the database using its title."""
        game = GameDAO.get_by_id(id)
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

@ns.route('/title/<title>')
@ns.param('title', 'Unique title of game')
@ns.response(404, 'Game not found.')
class Game(Resource):
    @ns.doc('Get a game by title. This endpoint is not case sensitive.')
    @ns.marshal_with(game)
    @jwt_required
    def get(self, title):
        """Get a game from the database given its title."""
        game = GameDAO.get_by_title(title)
        if not game:
            ns.abort(404)
        else:
            return game, 200

    @ns.response(200, "Game successfully deleted.")
    @ns.doc("Delete a game using the title as a reference. This endpoint is not case sensitive.")
    @jwt_required
    def delete(self, title):
        """Delete a game from the database using its title."""
        game = GameDAO.get_by_title(title)
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
