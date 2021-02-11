import logging
import sys

from flask import Flask, render_template

from core.extensions import (
    cors,
    db,
    migrate,
)
import core.game as game


def create_app(config_object:object) -> Flask:
    """Application factory.

    :param config_object: the configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    # register_errorhandlers(app)
    register_shellcontext(app)
    # register_commands(app)
    configure_logger(app)
    return app


def register_extensions(app:Flask) -> None:
    """Register FLask extensions."""
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(game.blueprint)
    return None


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db,}

    app.shell_context_processor(shell_context)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
