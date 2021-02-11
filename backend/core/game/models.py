from datetime import datetime

from core.database import Column, PkModel, db, reference_col, relationship

class Game(PkModel):
    """Game model for storing the menu of games that I want to recommend to my friends."""
    __tablename__ = "games"

    public_id = Column(db.String(100), unique=True)
    title = Column(db.String(255), unique=True, nullable=False)
    publisher_website = Column(db.String(255))
    logo_img_src = Column(db.String(255))
    logo_img_alt = Column(db.String(255))
    logo_img_style = Column(db.JSON())
    tagline = Column(db.String(255))
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)

    def __repr__(self):
        return f"<Game '{self.title}'>"


def save_new_game(data):
    game = Game.query.filter_by(title=data['title']).first()
    if not game:
        new_game = Game(
            title = data['title'],
            publisher_website = data['publisher_website'],
            logo_img_src = data['logo_img_src'],
            logo_img_alt = data['logo_img_alt'],
            tagline = data['tagline'],
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        if data.get('logo_img_style'):
            Game.logo_img_style = data['logo_img_style']
        db.session.add(new_game)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully added game.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Game already exists.'
        }
        return response_object, 409

def get_all_games():
    return Game.query.all()

def get_a_game(title):
    return Game.query.filter_by(title=title).first()
