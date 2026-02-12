from flask import Flask

from app.config import Config
from .errorHandlers import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_error_handlers(app)

    from .routes import register_routes

    register_routes(app)

    return app
