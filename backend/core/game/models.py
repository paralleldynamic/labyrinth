from datetime import datetime

from core.database import Column, PkModel, db, reference_col, relationship
class Game(PkModel):
    """Game model for storing the menu of games that I want to recommend to my friends."""
    __tablename__ = "games"

    # public_id = Column(db.String(100), unique=True)
    title = Column(db.String(255), unique=True, nullable=False)
    publisher_website = Column(db.String(255))
    logo_img_src = Column(db.String(255))
    logo_img_alt = Column(db.String(255))
    logo_img_style = Column(db.JSON())
    tagline = Column(db.String(255))
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # @classmethod
    # def get_by_id(cls, id):
    #     return cls.query.filter_by(public_id=id).first_or_404()

    @classmethod
    def get_by_title(cls, search):
        return cls.query.filter(cls.title.ilike(search)).first_or_404()

    def __repr__(self):
        return f"<Game '{self.title}'>"
