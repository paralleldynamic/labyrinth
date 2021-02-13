from datetime import datetime

from core.database import Column, PkModel, db
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def get_by_title(cls, search):
        return cls.query.filter(cls.title.ilike(search)).first_or_404()

    def __repr__(self):
        return f"<Game({self.title})>"
