from typing import final
from flask import request
from flask_jwt_extended import create_access_token
from flask_restx import Namespace, Resource, fields
from sqlalchemy.exc import IntegrityError

from .models import User as UserDAO

ns = Namespace("user", description="user related operations")
user = ns.model("", {
    "id": fields.String(description="public ID of the user"),
    "username": fields.String(description="unique, user-selected handle"),
    "email": fields.String(description="user's email address"),
    "password": fields.String(description="user password"),
})

@ns.route('/login')
class Login(Resource):
    @ns.doc('login a user')
    @ns.marshal_list_with(user, envelope='data')
    @ns.expect(user, Validate=True)
    def post():
        data = request.json
        username = data.get('username', None)
        password = data.get('password', None)
        if not (username and password):
            response_object = {
                "status": "error",
                "message": "Missing username or password."
            }
            response_code = 400
        try:
            user = UserDAO.get_by_username(username)
            if not user.check_password(password):
                response_object = {
                    "status": "error",
                    "message": "Invalid username or password.",
                }
                response_code = 401
                return response_object, response_code
            access_token = create_access_token(identity=username)
            response_object = {
                "status": "success",
                "message": "User is authenticated.",
                "access_token": access_token,
            }
            response_code = 200
        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "There was an unspecified error."
            }
            response_code = 500
            raise e
        finally:
            return response_object, response_code

@ns.route('/register')
class Register(Resource):
    @ns.doc('register a new user')
    @ns.marshal_list_with(user, envelope='data')
    @ns.expect(user, Validate=True)
    def post(self):
        """Attempts to register a new user."""
        data = request.json
        expected_data = ['username', 'email', 'password']
        username, email, password = (data.get(key, None) for key in expected_data)
        if not (username and email and password):
            response_object = {
                "status": "error",
                "message": "Missing required information to register a new user."
            }
            response_code = 400
            return response_object, response_code
        try:
            user = UserDAO(username, email, password)
            access_token = create_access_token(identity=user.username)
            response_object = {
                "status": "success",
                "message": "User is registered.",
                "access_token": access_token,
            }
            response_code = 201
        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "There was an unspecified error."
            }
            response_code = 500
            raise e
        finally:
            return response_object, response_code
