from flask import request
from flask_jwt_extended import create_access_token
from flask_restx import Resource
from sqlalchemy.exc import IntegrityError
from pprint import pprint

from .contracts import ns, authorization, credentials
from .models import User as UserDAO

@ns.route('/login')
class Login(Resource):
    @ns.doc('login a user')
    @ns.expect(credentials, Validate=True)
    @ns.marshal_with(authorization, skip_none=True)
    def post(self):
        """Attempts to login a user"""
        data = request.form or request.json
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
            if not (user and user.check_password(password)):
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
                "username": username,
            }
            response_code = 200
        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "There was an unspecified error."
            }
            response_code = 500
            pprint(e)
        finally:
            return response_object, response_code

@ns.route('/register')
class Register(Resource):
    @ns.doc('register a new user')
    @ns.expect(credentials, Validate=True)
    @ns.marshal_with(authorization, skip_none=True)
    def post(self):
        """Attempts to register a new user."""
        data = request.form or request.json
        expected_data = ['username', 'email', 'password', 'invitation_code']
        username, email, password, invitation_code = (data.get(key, None) for key in expected_data)
        pprint([username, email, password, invitation_code])
        if not all([username, email, password]):
            response_object = {
                "status": "error",
                "message": "Missing required information to register a new user."
            }
            response_code = 400
            return response_object, response_code
        # TODO extend invitation codes
        if invitation_code != "this test invitation lol":
            response_object = {
                "status": "error",
                "message": "Invalid invitation code. Please try again."
            }
            response_code = 400
            return response_object, response_code
        try:
            user = UserDAO.create(username=username, email=email, password=password)
            access_token = create_access_token(identity=user.username)
            response_object = {
                "status": "success",
                "message": "User is registered.",
                "access_token": access_token,
                "username": username,
            }
            response_code = 201
        except IntegrityError as e:
            response_object = {
                "status": "fail",
                "message": "Username or email already in use."
            }
            response_code = 409
        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "There was an unspecified error."
            }
            response_code = 500
        finally:
            return response_object, response_code
