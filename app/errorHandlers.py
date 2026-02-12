from flask import jsonify
from .helpers import structureResponse
from .errors import AppError


def register_error_handlers(app):

    @app.errorhandler(AppError)
    def handle_app_error(err: AppError):
        return jsonify(structureResponse(
            success=False,
            message=err.message,
            errors=err.errors
        )), err.status_code


    @app.errorhandler(Exception)
    def handle_unexpected_error(err: Exception):
        return jsonify(structureResponse(
            success=False,
            message="Unexpected server error."
        )), 500
