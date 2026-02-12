from flask import Blueprint

affirmations_bp = Blueprint('affirmations', __name__)


@affirmations_bp.route('/affirmations', methods=['POST'])
def handle_affirmations():
    return {'message': 'affirmations endpoint'}
