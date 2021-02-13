from flask import request

from flask_restx import Namespace, Resource, fields
from sqlalchemy.exc import IntegrityError

from .models import User as UserDAO

ns = Namespace("user", description="user related operations")
user = ns.model("", {
    "id": fields.String(description="public ID of the user"),
    "username": fields.String(description="unique, user-selected handle"),
    "email": fields.String(description="user's email address"),
})

