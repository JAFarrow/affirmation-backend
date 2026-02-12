from .affirmations import affirmations_bp

def register_routes(app):
    app.register_blueprint(affirmations_bp)