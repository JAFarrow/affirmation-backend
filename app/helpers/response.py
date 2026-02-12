from typing import Any, Optional, Required

def structureResponse(
    success: Required[bool],
    message: Required[str],
    data: Optional[dict] = None,
    errors: Optional[dict] = None
) -> dict:
    response = {
        'success': success,
        'message': message
    }

    if data is not None:
        response['data'] = data

    if errors is not None:
        response['errors'] = errors

    return response