from flask import Blueprint
from flask import request, jsonify
from ..helpers import structureResponse, validateAffirmationForm
from ..controllers import generate_affirmation

affirmations_bp = Blueprint('affirmations', __name__)


@affirmations_bp.route('/affirmations', methods=['POST'])
def handle_affirmations():
    data = request.form
    validateAffirmationForm(data)
    
    response = generate_affirmation(data)
    
    return jsonify(response), 200
