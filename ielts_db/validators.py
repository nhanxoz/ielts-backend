from django.core.exceptions import ValidationError
from .models import Account


def validate_username(username):
    if Account.objects.filter(**{'{}__iexact'.format(Account.USERNAME_FIELD): username}).exists():
        raise ValidationError('User with this {} already exists'.format(Account.USERNAME_FIELD))
    return username