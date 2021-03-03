from datetime import datetime

from core.database import Column, PkModel, db, reference_col, relationship
class Game(PkModel):
    """Game model for storing the menu of games that I want to recommend to my friends."""
    __tablename__ = "games"

    public_id = Column(db.String(100), unique=True)
    title = Column(db.String(255), unique=True, nullable=False)
    tagline = Column(db.String(255))
    website = Column(db.String(255))
    description = Column(db.Text())
    publisher_id = reference_col("publishers", nullable=False)
    publisher = relationship("Publisher", backref="games")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def get_by_title(cls, search):
        return cls.query.filter(cls.title.ilike(search)).first_or_404()

    def __repr__(self):
        return f"<Game({self.title})>"

class Publisher(PkModel):
    """Publishers of games."""
    __tablename__ = "publishers"

    name = Column(db.String(255))
    website = Column(db.String(255))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"<Publisher({self.name})>"
