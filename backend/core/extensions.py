from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
cors = CORS()
jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()
