from flask_restx import Namespace, fields

ns = Namespace("game", description="game related operations")

publisher = ns.model("publisher", {
    "id": fields.String(description="publisher id"),
    "name": fields.String(description="name of the publisher"),
    "website": fields.Url(description="website of the publisher")
})

game = ns.model("game", {
    "id": fields.String(description="public ID of the game"),
    "title": fields.String(required=True, description="game title"),
    "tagline": fields.String(description="tagline to describe the game"),
    "website": fields.Url(description="website of the game"),
    "description": fields.String(description="extended description of the game"),
    "publisher": fields.Nested(publisher, description="the publisher associated with the game"),
})
