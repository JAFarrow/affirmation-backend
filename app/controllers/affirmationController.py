from ..services import callLLM
from ..helpers import structureResponse
from flask import jsonify
from openai import APIConnectionError, APITimeoutError, APIError

def generate_affirmation(data: dict) -> dict:
    mood = data.get('mood')
    details = data.get('details', None)
    response = callLLM(mood, details)

    return structureResponse(
            success=True,
            message="Affirmation successfully generated.",
            data={"affirmation": response}
    )