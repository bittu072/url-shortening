from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL")
    return value

def validate_dot_com(value):
    if not "com" in value:
        raise value.ValidationError("Invalid URL because of no .com in url")
    return value
