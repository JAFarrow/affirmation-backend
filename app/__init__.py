from flask import Flask
from flask_cors import CORS

from app.config import Config
from .errorHandlers import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins=[app.config['FRONTEND_URL']])

    register_error_handlers(app)

    from .routes import register_routes

    register_routes(app)

    return app
