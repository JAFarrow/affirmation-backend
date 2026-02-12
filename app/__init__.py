from flask import Flask

from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes import register_routes

    register_routes(app)

    return app
