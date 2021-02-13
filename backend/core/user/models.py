
from core.database import Column, PkModel, db, reference_col, relationship
from core.extensions import bcrypt

class Role(PkModel):
    """A specific user role with various permissions"""
    __tablename__ = "roles"

    name = Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name, **kwargs):
        """Constructor"""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represents instance as a unique string."""
        return f"<Role({self.name})>"

class User(PkModel):
    """A user for the website"""
    __tablename__ = "users"

    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(254), unique=True, nullable=False)
    # password is stored as a hashed value
    password = Column(db.LargeBinary(128), nullable=True)
    first_name = Column(db.String(), nullable=True)
    last_name = Column(db.String(), nullable=True)
    active = Column(db.Boolean(), default=False)

    def __init__(self, username, email, password=None, **kwargs):
        """Constructor"""
        super().__init__(username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password"""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password"""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name"""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represents instance as a unique string."""
        return f"<Role({self.name})>"
