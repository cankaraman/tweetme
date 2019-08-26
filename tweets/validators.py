
from django.core.exceptions import ValidationError

# Create your models here.

def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("Cannot be blank")
    return value
