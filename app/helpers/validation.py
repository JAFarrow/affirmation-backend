from ..models import MoodEnum
from ..errors import ValidationError

def validateAffirmationForm(form: dict) -> None:
    username = form.get('username', None)
    mood = form.get('mood', None)
    details = form.get('details', None)

    errors = {}

    if not username or not isinstance(username, str):
        errors['username'] = "Username is required."

    if not mood or mood and mood not in [m.value for m in MoodEnum]:
        errors['mood'] = "Invalid mood."

    if details is not None and not isinstance(details, str):
        errors['details'] = "Details must be a string."

    if errors:
        raise ValidationError(errors)