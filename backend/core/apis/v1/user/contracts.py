from flask_restx import Namespace, fields

ns = Namespace("user", description="user related operations")

# API model contracts for user endpoints

# response for an authentication request
authorization = ns.model("authorization", {
    "status": fields.String(description="status of authorization request"),
    "message": fields.String(description="detailed explanation of status"),
    "access_token": fields.String(description="a JWT access token that has been authorized for a user"),
    "username": fields.String(description="username of user who has been logged in"),
})

# an expected credential JSON object for logging in or registering
credentials = ns.model("credentials", {
    # TODO: refactor user model so that there can be a randomized public ID for each user
    # dev database does not allow for UUID4().int values
    # "id": fields.String(description="public ID of the user"),
    "username": fields.String(description="unique, user-selected handle"),
    "email": fields.String(description="user's email address"),
    "password": fields.String(description="user password"),
    "invitation_code": fields.String(description="invitation code to register a new account",)
})
