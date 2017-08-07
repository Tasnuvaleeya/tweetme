from django.core.exceptions import ValidationError
# from .models import Tweet


def validate_content(value):
    content =value
    if content=='':
        raise ValidationError("Content Can not be blank")
    return value