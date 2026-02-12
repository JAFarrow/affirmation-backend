class AppError(Exception):
    def __init__(self, message: str, status_code: int = 500, errors: dict | None = None):
        self.message = message
        self.status_code = status_code
        self.errors = errors or {}
        super().__init__(message)


class ValidationError(AppError):
    def __init__(self, errors: dict):
        super().__init__(
            message="Validation failed.",
            status_code=400,
            errors=errors
        )


class LLMConnectionError(AppError):
    def __init__(self, message="Failed to reach LLM service."):
        super().__init__(message, 503)


class LLMServiceError(AppError):
    def __init__(self, message="LLM service error."):
        super().__init__(message, 502)
