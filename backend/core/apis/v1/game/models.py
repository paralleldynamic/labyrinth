from core.database import Column, PkModel, db, reference_col, relationship.

game_tags = db.Table('game_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    db.Column('game_id', db.Integer, db.ForeignKey('games.id'), primary_key=True),
)
class Game(PkModel):
    """Game model for storing the menu of games that I want to recommend to my friends."""
    __tablename__ = "games"

    public_id = Column(db.String(100), unique=True)
    title = Column(db.String(255), unique=True, nullable=False)
    tagline = Column(db.String(255))
    website = Column(db.String(255))
    description = Column(db.Text())
    publisher_id = reference_col("publishers", nullable=False)
    tags = relationship('tags', secondary=game_tags, backref=('tags'))

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

    name = Column(db.String(255), nullable=False)
    website = Column(db.String(255))
    games = relationship("games", backref="publisher")

    @classmethod
    def get_by_name(cls, search):
        return cls.query.filter(cls.name.ilike(search)).first()

    @classmethod
    def get_or_create(cls, publisher):
        id  = publisher.get('id')
        name = publisher.get('name')
        print(id, name)
        if id:
            p = cls.get_by_id(id)
            print(f'found by id publisher {p}')
        elif name:
            p = cls.get_by_name(name)
            print(f'found by name publisher {p}')
        if not p:
            p = cls(**publisher)
            print(f'created publisher {p}')
        return p

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"<Publisher({self.name})>"

class TagCategory(PkModel):
    """Categories which tags can be a part of."""
    __tablename__ = "tag_categories"

    category = Column(db.String(255))
    tags = relationship("tag", backref="tag_category")

    def __repr__(self):
        return f"<TagCategory({self.category})>"

class Tag(PkModel):
    """Tags to for qualitative attributes."""
    __tablename__ = "tags"

    tag = Column(db.String(255))
    category = reference_col("tag_categories", nullable=False)

    def __repr__(self):
        return f"<Tag({self.tag})>"
