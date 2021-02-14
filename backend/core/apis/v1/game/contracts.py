from flask_restx import Namespace, fields

ns = Namespace("game", description="game related operations")

game = ns.model("game", {
    "id": fields.String(description="public ID of the game"),
    "title": fields.String(required=True, description="game title"),
    "publisher_website": fields.String(description="website of publisher of the game"),
    "logo_img_src": fields.String(description="source for the game's logo"),
    "logo_img_alt": fields.String(description="alt text for the "),
    "tagline": fields.String(description="tagline to describe the game"),
})
