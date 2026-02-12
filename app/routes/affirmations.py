from flask import Blueprint
from flask import request, jsonify
from ..helpers import structureResponse, validateAffirmationForm

affirmations_bp = Blueprint('affirmations', __name__)


@affirmations_bp.route('/affirmations', methods=['POST'])
def handle_affirmations():
    data = request.form
    errors = validateAffirmationForm(data)
    if errors:
        return jsonify(structureResponse(
            success=False,
            message='Form validation failed.',
            errors=errors
        )), 400
    return jsonify(structureResponse(
        success=True,
        message='Hello World.'
    ))
